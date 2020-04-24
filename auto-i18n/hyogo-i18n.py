import glob
import re
import os
import json
import datetime
import pathlib
from bs4 import BeautifulSoup

######
# 兵庫県版のi18n関連ファイルのうち、元となるja.jsonを自動生成するスクリプト。
# 東京都版の翻訳と兵庫県版の翻訳を両方使えるようにして、保守性を保つことを目的としています。
# このスクリプトは滋賀県版で使われている https://gist.github.com/rioil/d44a475710fa21c8d16f1d55b754e8e2 を元に作成されています。
# このようなスクリプトを公開してくださった方に感謝いたします。
######

# チェックするディレクトリのリスト
CHECK_DIR = ["pages", "components", "layouts", "data"]

# チェックするjsonファイルのリスト
JSON_FILES = ["patients.json", "age.json", "sickbeds_summary.json", "clusters_summary.json"]

# タグの正規表現パターン
tag_pattern_t = re.compile("\$t\('[^']*?'")
tag_pattern_tc = re.compile("\$tc\('[^']*?'")

# 文字エンコーディング
ENCODING = "UTF-8"

# 出力ファイル設定
OUTPUT_DIR = 'auto-i18n'
CHECK_RESULT = 'result.csv'

# 東京都版の翻訳ファイルパス
TOKYO_JA_JSON_PATH = os.path.join(os.pardir, "assets/locales/ja.json")

# 兵庫県版の翻訳ファイルパス
HYOGO_JA_JSON_PATH = os.path.join(os.pardir, "assets/locales-hyogo/ja.json")

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
        # リポジトリのルートからのパスをtoolからの相対パスに変換
        cdir = os.path.join(os.pardir, cdir)
        if "data" not in cdir:
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
                        elif file_name in JSON_FILES[1:]:  # 年代別患者数のデータと病床数のデータ、更にクラスター別患者数のデータ
                            # 年代別の場合、「90代以上」の翻訳が2020/04/13現在、東京都版に組み込まれていないのでそれを取得
                            # 病床数の場合は、2020/04/13現在表示していないが、今後再表示する場合に向けて取得
                            # クラスター別の場合は、クラスター名を翻訳するため取得
                            tags = list(json_content["data"].keys())
                        # 重複分を取り除く
                        all_tags = list(set(all_tags + tags))

    # 東京都版と兵庫県版のjsonをそれぞれ読み込む
    tokyo_json = json.load(tokyo_file)
    hyogo_json = json.load(hyogo_file)

    # 念のためassert
    assert isinstance(tokyo_json, dict)
    assert isinstance(hyogo_json, dict)

    # タグのチェック
    for tag in all_tags:
        # "."で区切られている特殊なもの("件.tested"や"件.reports"のような翻訳が複数あるもの)を判別する
        tag_splitted = tag.split(".")
        # タグが存在しなければ兵庫県版jsonに追加
        if tag not in tokyo_json and tag not in hyogo_json:
            if tag_splitted[0] in tokyo_json:
                if tag_splitted[1] in tokyo_json[tag_splitted[0]]:
                    continue
            elif tag_splitted[0] in hyogo_json:
                if tag_splitted[1] in hyogo_json[tag_splitted[0]]:
                    continue
            # N代の人は除外する(既に"{age}代"として存在するため)
            if tag[-1:] == "代":
                try:
                    int(tag[:-1])
                    continue
                except Exception:
                    pass
            print("Add TAG: " + tag + " to " + HYOGO_JA_JSON_PATH)
            hyogo_json[tag] = tag
            if not warn_count:
                result.write(",".join(["RUN", datetime.datetime.today().strftime("%Y/%m/%d %H:%M")]) + '\n')
            result.write(",".join(["TAG_ADD", tag]) + '\n')
            warn_count += 1

    made_json = hyogo_json

    hyogo_keys = list(made_json.keys())
    # 以前はなかったが、現在は東京都版に追加されている翻訳は取り除くのと
    # 以前はあったが、現在は兵庫県版で使用されていない翻訳を取り除く
    for hyogo_tag in hyogo_keys:
        if hyogo_tag in tokyo_json.keys() or hyogo_tag not in all_tags:
            made_json.pop(hyogo_tag)
            if not warn_count:
                result.write(",".join(["RUN", datetime.datetime.today().strftime("%Y/%m/%d %H:%M")]) + '\n')
            result.write(",".join(["TAG_REMOVE", hyogo_tag]) + '\n')
            warn_count += 1


with open(HYOGO_JA_JSON_PATH, mode="w", encoding=ENCODING) as hyogo_file:
    json.dump(made_json, hyogo_file, ensure_ascii=False, indent=2)


# タグ総数出力（言語ごとに別のタグとして数える）
print("total : " + str(len(all_tags)))
# 警告数(翻訳単語として登録されていなかった数)出力
print("warn : " + str(warn_count))
# ファイル総数出力
print("checked file: " + str(file_count))
