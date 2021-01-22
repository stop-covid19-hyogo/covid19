import glob
import re
import os
import json

from datetime import datetime, timedelta, timezone
from bs4 import BeautifulSoup

######
# 兵庫県版のi18n関連ファイルのうち、元となるja.jsonを自動生成するスクリプト。
# 東京都版の翻訳と兵庫県版の翻訳を両方使えるようにして、保守性を保つことを目的としています。
# このスクリプトは滋賀県版で使われている https://gist.github.com/rioil/d44a475710fa21c8d16f1d55b754e8e2 を元に作成されています。
# このようなスクリプトを公開してくださった方に感謝いたします。
######

# チェックするディレクトリのリスト
CHECK_DIR = ["pages", "components", "layouts", "data", "utils"]

# チェックするjsonファイルのリスト
JSON_FILES = ["patients.json", "news.json", "age.json", "sickbeds_summary.json", "clusters_summary.json"]

# チェックするTypeScriptファイルのリスト
# 現状はformatTable.tsしかないが、のちに表追加や、データ追加により必要になった場合は追加しなければならない。
TS_FILES = ["formatTable.ts"]

# タグの正規表現パターン
tag_pattern_t = re.compile("\$t\([ ]*?['|`][^']*?['|`]")
tag_pattern_tc = re.compile("\$tc\([ ]*?['|`][^']*?['|`]")

# tsファイル内のヘッダーの正規表現パターン
header_pattern = re.compile("\{ text: '[^']*?', value: '[^']*?'")

# 文字エンコーディング
ENCODING = "UTF-8"

# 出力ファイル設定
OUTPUT_DIR = 'auto-i18n'
CHECK_RESULT = 'result_hyogo.csv'

# 東京都版の翻訳ファイルパス
TOKYO_JA_JSON_PATH = os.path.join(os.pardir, "assets/locales/ja.json")

# 兵庫県版の翻訳ファイルパス
HYOGO_JA_JSON_PATH = os.path.join(os.pardir, "assets/locales-hyogo/ja.json")

# ログに用いる時間のタイムゾーン
jst = timezone(timedelta(hours=9), "JST")

# 全てのタグリスト
all_tags = []

# 警告の数
warn_count = 0

# チェックされたファイルの数
file_count = 0

# 作られたjson
made_json = {}

with open(os.path.join(os.pardir, OUTPUT_DIR, CHECK_RESULT), mode="a", encoding=ENCODING) as result, \
        open(TOKYO_JA_JSON_PATH, mode='r', encoding=ENCODING) as tokyo_file, \
        open(HYOGO_JA_JSON_PATH, mode='r', encoding=ENCODING) as hyogo_file:
    # ディレクトリ毎にテスト
    for cdir in CHECK_DIR:
        # リポジトリのルートからのパスをauto-i18nからの相対パスに変換
        cdir = os.path.join(os.pardir, cdir)
        if "data" not in cdir and "utils" not in cdir:
            # すべてのVueファイルを検索
            vue_files = glob.glob(cdir + os.sep + "**" + os.sep + "*.vue", recursive=True)
            file_count += len(vue_files)

            # 各Vueファイルについて処理
            for path in vue_files:
                with open(path, encoding=ENCODING) as file:
                    # ファイルの内容を文字列として取得
                    # ここで改行を空白として扱うのは、vue内のi18nタグが正しく認識できない場合があるため
                    content = ' '.join([l.strip() for l in file])
                    # 全タグを正規表現で取得
                    t_tags = [tag[4:(len(tag) - 1)] for tag in tag_pattern_t.findall(content) if
                              tag[4:(len(tag) - 1)] != '']
                    tc_tags = [
                        tag[5:(len(tag) - 1)] for tag in tag_pattern_tc.findall(content) if tag[5:(len(tag) - 1)] != ''
                    ]
                    # 「'」で始まっているタグがあるので修正
                    fixed_tags = []
                    for tag in t_tags:
                        start = 0
                        if tag[0] == "'":
                            start = 1
                        fixed_tags.append(tag[start:])
                    for tag in tc_tags:
                        start = 0
                        if tag[0] == "'":
                            start = 1
                        fixed_tags.append(tag[start:])
                    # i18nタグ内のpathを取得
                    soup = BeautifulSoup(content, "html.parser")
                    i18n_tags = [tag.get("path") for tag in soup.find_all("i18n")]

                    # タグを統合し、重複分を取り除く
                    all_tags = list(set(all_tags + fixed_tags + i18n_tags))
        elif "utils" in cdir:
            # すべてのtsファイルを検索
            ts_files = glob.glob(cdir + os.sep + "**" + os.sep + "*.ts", recursive=True)

            # 各tsファイルについて処理
            for path in ts_files:
                file_name = os.path.basename(path)
                # tsファイルが調べるべきtsであるか
                if file_name in TS_FILES:
                    # 調べるべきtsの場合、ファイルをカウント
                    file_count += 1
                    with open(path, encoding=ENCODING) as file:
                        # ファイルの内容を文字列として取得
                        content = ''.join([l.strip() for l in file])
                        # 抽出したヘッダー内のtextとvalueは変数として読み込まれることになるので、
                        # あらかじめ設定しておく
                        text = "text"
                        value = "value"
                        # ヘッダーを正規表現で取得し、textを抽出
                        headers = [eval(str_header + " }")[text] for str_header in header_pattern.findall(content)]
                        # Noは使っていないので、取り除く
                        for unused in ["No"]:
                            headers.pop(headers.index(unused))
                        # タグを統合し、重複分を取り除く
                        all_tags = list(set(all_tags + headers))

        else:
            # すべてのJsonファイルを検索
            json_files = glob.glob(cdir + os.sep + "**" + os.sep + "*.json", recursive=True)

            # 各jsonファイルについて処理
            for path in json_files:
                file_name = os.path.basename(path)
                # jsonファイルが調べるべきjsonであるか
                if file_name in JSON_FILES:
                    # 調べるべきjsonの場合、ファイルをカウント
                    file_count += 1
                    with open(path, encoding=ENCODING) as file:
                        # jsonを読み込み
                        json_content = json.load(file)
                        # タグリストを生成
                        tags = []
                        if file_name == JSON_FILES[0]:  # 陽性患者の属性データ
                            for patients in json_content["data"]:
                                # 居住地を取得
                                tags.append(patients["居住地"])
                        elif file_name == JSON_FILES[1]:  # ニュースデータ
                            for news in json_content["newsItems"]:
                                # ニュースの本文を取得
                                tags.append(news["text"])
                        elif file_name in JSON_FILES[2:]:  # 年代別患者数のデータと病床数のデータ、更にクラスター別患者数のデータ
                            # 年代別の場合、「90代以上」の翻訳が2020/04/13現在、東京都版に組み込まれていないのでそれを取得
                            # 病床数の場合は、2020/04/13現在表示していないが、今後再表示する場合に向けて取得
                            # クラスター別の場合は、クラスター名を翻訳するため取得
                            tags = list(json_content["data"].keys())
                        # 重複分を取り除く
                        all_tags = list(set(all_tags + tags))

    # 「その他」は内部で「その他.graph」に変換しているので除外する
    all_tags.pop(all_tags.index("その他"))

    # 翻訳が複数あるもの("."で区切られている特殊なもの)を保管するリスト
    has_many_tags = []

    # 仮のja.jsonを作る
    tentative_ja_json = {}
    for tag in all_tags:
        # "."で区切られている特殊なもの("件.tested"や"件.reports"のような翻訳が複数あるもの)を判別する
        # 普通のものに関しては、なにもせず代入する
        tag_splitted = tag.split(".")
        if len(tag_splitted) == 2:
            found = False
            for many_tag in has_many_tags:
                if tag_splitted[0] == many_tag[0] and tag_splitted[1] != many_tag[1]:
                    found = True
                    many_tag[2] = found
            # ogp.og:imageに関しては一つしかない例外なので、特例として処理する
            # また、その他.parentが兵庫県版には存在しないので、こちらも特例として処理する
            if tag_splitted[0] in ["ogp", "その他"]:
                found = True
            has_many_tags.append(tag_splitted + [found])
        else:
            # N代は除外する(既に"{age}代"として存在するため)
            if tag[-1:] == "代":
                try:
                    int(tag[:-1])
                    continue
                except Exception:
                    pass
            tentative_ja_json[tag] = tag

    # "."でわけられていたものに関して、複数あれば(many_tag[2]がtrueであれば)
    # 辞書型として展開して代入し、そうでなければ普通のキーとして代入する
    for many_tag in has_many_tags:
        if many_tag[2]:
            if tentative_ja_json.get(many_tag[0]):
                tentative_ja_json[many_tag[0]][many_tag[1]] = many_tag[0]
            else:
                tentative_ja_json[many_tag[0]] = {
                    many_tag[1]: many_tag[0]
                }
        else:
            full_tag = ".".join(many_tag[:2])
            tentative_ja_json[full_tag] = full_tag

    # 東京都版と兵庫県版のjsonをそれぞれ読み込む
    tokyo_json = json.load(tokyo_file)
    hyogo_json = json.load(hyogo_file)

    # 念のためassert
    assert isinstance(tokyo_json, dict)
    assert isinstance(hyogo_json, dict)

    # 東京都版の翻訳を取り除く
    for key in tokyo_json.keys():
        if tentative_ja_json.get(key):
            tentative_ja_json.pop(key)

    tentative_json_keys = list(tentative_ja_json.keys())
    hyogo_json_keys = list(hyogo_json.keys())

    # 以前はなかったが今はある翻訳を追加する
    for key in tentative_json_keys:
        hyogo_tag = hyogo_json.get(key)
        tentative_tag = tentative_ja_json.get(key)
        if not hyogo_tag:
            hyogo_json[key] = tentative_tag
            print("Add TAG: " + str(tentative_tag) + " to " + HYOGO_JA_JSON_PATH)
            if not warn_count:
                result.write(",".join(["RUN", datetime.now(jst).strftime("%Y/%m/%d %H:%M")]) + '\n')
            result.write(",".join(["TAG_ADD", str(tentative_tag)]) + '\n')
            warn_count += 1
        elif hyogo_tag != tentative_tag and isinstance(hyogo_tag, dict):
            tentative_dict_keys = tentative_tag.keys()
            for dict_key in tentative_dict_keys:
                if not hyogo_tag.get(dict_key):
                    hyogo_tag[dict_key] = tentative_tag[dict_key]
                    print("Add TAG: " + str(tentative_tag[dict_key]) + " to " + HYOGO_JA_JSON_PATH)
                    if not warn_count:
                        result.write(",".join(["RUN", datetime.now(jst).strftime("%Y/%m/%d %H:%M")]) + '\n')
                    result.write(",".join(["TAG_ADD", str(tentative_tag[dict_key])]) + '\n')
        if hyogo_tag:
            hyogo_json_keys.pop(hyogo_json_keys.index(key))

    # 以前はあったが今はない翻訳を削除する
    for key in hyogo_json_keys:
        ja_tag = hyogo_json.get(key)
        hyogo_json.pop(key)
        print("Remove TAG: " + str(ja_tag) + " from " + HYOGO_JA_JSON_PATH)
        if not warn_count:
            result.write(",".join(["RUN", datetime.now(jst).strftime("%Y/%m/%d %H:%M")]) + '\n')
        result.write(",".join(["TAG_REMOVE", str(ja_tag)]) + '\n')
        warn_count += 1

    made_json = hyogo_json

with open(HYOGO_JA_JSON_PATH, mode="w", encoding=ENCODING) as hyogo_file:
    json.dump(made_json, hyogo_file, ensure_ascii=False, indent=2)


# タグ総数出力（言語ごとに別のタグとして数える）
print("total : " + str(len(all_tags)))
# 警告数(翻訳単語として登録されていなかった数)出力
print("warn : " + str(warn_count))
# ファイル総数出力
print("checked file: " + str(file_count))
