(window.webpackJsonp=window.webpackJsonp||[]).push([[13],{446:function(t){t.exports=JSON.parse('{"data":{"認定こども園":8,"北播磨総合医療センター":5,"宝塚第一病院":8,"仁恵病院":14,"神戸市中央市民病院":36,"神戸赤十字病院":38,"神戸西警察署":12,"神戸市環境局":17,"グリーンアルス関係":54,"介護保険通所事業所":7,"ライブ関係":13,"海外渡航関係":26,"その他":306,"行動歴調査中":10,"特定できず":158},"last_update":"2020-07-02T00:00:00+09:00"}')},480:function(t,e,r){"use strict";r.r(e);var n=r(318),c=r(340),o=r(341),d=r(446),h=r(342),m=r(343),l=r(350),f=r(345),$=r(346),C=r(347),y=r(344),_=r(348),w=r(104),k={components:{ConfirmedCasesDetailsCard:m.a,ConfirmedCasesNumberCard:l.a,ConfirmedCasesAttributesCard:f.a,TestedNumberCard:$.a,PatientsByAge:C.a,PatientsByClusters:y.a,ChangesPatientsNumberCard:_.a},data:function(){var title,t;switch(this.$route.params.card){case"details-of-confirmed-cases":title=this.$t("検査陽性者の状況"),t=c.last_update;break;case"number-of-confirmed-cases":title=this.$t("陽性患者数"),t=n.last_update;break;case"attributes-of-confirmed-cases":title=this.$t("陽性患者の属性"),t=n.last_update;break;case"number-of-tested":title=this.$t("検査実施件数"),t=c.last_update;break;case"patients-by-age":title=this.$t("年代別陽性患者数"),t=o.last_update;break;case"patients-by-clusters":title=this.$t("クラスター別陽性患者数"),t=d.last_update;break;case"changes-in-number-of-hospitalized-patients":title=this.$t("治療中患者数の変化状況"),t=h.last_update}var data={title:title,updatedTimeStr:Object(w.d)(t)};return data},head:function(){var t="https://stop-covid19-hyogo.org",e=(new Date).getTime(),r="ja"===this.$i18n.locale?"".concat(t,"/ogp/").concat(this.$route.params.card,".png?t=").concat(e):"".concat(t,"/ogp/").concat(this.$i18n.locale,"/").concat(this.$route.params.card,".png?t=").concat(e),n="".concat(this.$t("兵庫県の新型コロナウイルス感染症 (COVID-19) に関する最新情報を提供するために、有志の仲間が開設したまとめサイトです。")+this.$t("兵庫県内の感染者数、検査実施件数、入院患者数などをわかりやすく伝えることで、現状を把握して適切な対策を取れるようにすることを目的としています。"));return{title:this.title,meta:[{hid:"og:url",property:"og:url",content:t+this.$route.path+"/"},{hid:"og:title",property:"og:title",content:this.title+" | "+this.$t("兵庫県 新型コロナウイルスまとめサイト")},{hid:"description",name:"description",content:n},{hid:"og:description",property:"og:description",content:n},{hid:"og:image",property:"og:image",content:r},{hid:"twitter:image",name:"twitter:image",content:r}]}}},v=r(4),component=Object(v.a)(k,(function(){var t=this.$createElement,e=this._self._c||t;return e("div",["details-of-confirmed-cases"==this.$route.params.card?e("confirmed-cases-details-card"):"number-of-confirmed-cases"==this.$route.params.card?e("confirmed-cases-number-card"):"attributes-of-confirmed-cases"==this.$route.params.card?e("confirmed-cases-attributes-card"):"number-of-tested"==this.$route.params.card?e("tested-number-card"):"patients-by-age"==this.$route.params.card?e("patients-by-age"):"patients-by-clusters"==this.$route.params.card?e("patients-by-clusters"):"changes-in-number-of-hospitalized-patients"==this.$route.params.card?e("changes-patients-number-card"):this._e()],1)}),[],!1,null,null,null);e.default=component.exports}}]);