# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
# 河北新合作网络科技有限公司
# 兰州壹玖壹玖电子商务有限公司 壹玖壹
# 北京华颜健康咨询有限公司 北京华
# 河北新合作网络科技有限公司 新
# 山西安健堂健康管理有限公司 山健堂
# 山西安运安环科技有限公司 山运安环
# 邢台万生大药房 万生大
# 常州途畅互联网科技有限公司合肥分公司 途畅互联
# 钟楼区北港可诺丹婷美容院 北港可诺
# 南京市江北新区春之燕美容店 江北新区
import os
import sys
sys.path.append('..')
from companynameparser import parser

a = [
    "深圳光明区三晟电子商务中心",
    "郑州经济开发区郑和热力公司",
    "佛山市禅城区百福具臻百货贸易行",
    "嘉兴市秀洲区洪合镇韵安服装厂",
    "兴仁市薏仁源农产品销售店",
    "江苏苏州箱包布塑胶公司",
    "北京伊禾赛生鲜食品有限公司",
    "西咸新区沣东新城未科诚百货店",
    "山西安健堂健康管理有限公司",
    "邢台万生大药房",
    "郑州市管城回族区咔悠化妆品商行",

    "沧州嘉诺温室大棚设施有限公司",
    "宁波海曙励信电脑商行",
    "南阳玉泽秀苑珠宝有限公司",
    "广东鹿山新材料股份有限公司",
    "广东粤电新会发电有限公司",
    "江苏苏州箱包布塑胶公司",
    "大丰区帮办信息服务站",
    "河北新合作网络科技有限公司",
    "徐州九州通医药公司",
    "合肥经济技术开发区妍丽雅服装店",
    "信阳市羊山新区沐香干果食品店",
    "巴马寿夫人健康产业有限公司",
    "庄浪县域起土特产批发零售店",
    "唯尚品百货商场（杭州）淘宝店",
    "潍坊综合保税区御见名匠专业护肤中心",
    "观途（上海）旅游服务中心（有限合伙）",
    "常州途畅互联网科技有限公司合肥分公司",
    "钟楼区北港可诺丹婷美容院",
    "南京市江北新区春之燕美容店",
    "西安运安环科技有限公司",
    "北新合作网络科技有限公司",
    "波澜格网络科技有限公司常州第一分公司",
    " 淮安迈捷生物科技有限公司",
    "南京佰达隆电子科技有限公司",
    "成都锤子科技有限公司",
    "上海览康贸易有限公司",
    "兰州壹玖壹玖电子商务有限公司",
    "北京华颜健康咨询有限公司",
    "洛阳市伊滨区小胖墩商贸行",
]


def load_file(file_path):
    subs = []
    if file_path and os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as fr:
            for line in fr:
                i = line.strip().split()[0]
                subs.append(i)
    return subs


if __name__ == '__main__':
    bug_input_file = 'bug_0508.txt'
    b = load_file(bug_input_file)
    a = a + b
    m = parser.Parser()
    for i in a:
        r = m.parse(i)
        print(i, r['brand'])

    print()
    for i in a:
        r = m.parse(i)
        print(i, r['place'], r['brand'], r['trade'], r['suffix'])
