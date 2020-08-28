#!/bin/env python
# coding=utf-8

per_month = 7000
per_month2 = 6000

conf_list = [
    #{ 'name': 'test(自如)', 'per_month': per_month, 'srv_month': per_month * 0.08, 'srv_once': 0, 'insur': per_month, 'discount': { } },
    #{ 'name': 'test(链家)', 'per_month': per_month2, 'srv_month': 0, 'srv_once': per_month2, 'insur': per_month2, 'discount': { } },
    { 'name': '上奥世纪-89', 'per_month': 6800, 'srv_month': 0, 'srv_once': 6800, 'insur': 6800, 'discount': {}, 'floor': '中/18' },
    #{ 'name': '上奥-104', 'per_month': 7000, 'srv_month': 0, 'srv_once': 7000, 'insur': 7000, 'discount': {}, 'floor': '中/23' },
    { 'name': '万润-自如-70', 'per_month': 6960, 'srv_month': 556.8, 'srv_once': 0, 'insur': 6960, 'discount': {0:0.9}, 'floor': '9/12' },
    { 'name': '强佑-自如-64', 'per_month': 7590, 'srv_month': 607.2, 'srv_once': 0, 'insur': 7590, 'discount': {1:0.5, 0:0.9}, 'floor': '2/15' },
    { 'name': '育新-自如2-102', 'per_month': 7350, 'srv_month': 588, 'srv_once': 0, 'insur': 7350, 'discount': { }, 'floor': '21/22' },
    { 'name': '育新-自如-86', 'per_month': 7890, 'srv_month': 631.2, 'srv_once': 0, 'insur': 7890, 'discount': { 0: 0.85 }, 'floor': '17/20' },
    { 'name': '育新花园-84', 'per_month': 5500, 'srv_month': 0, 'srv_once': 5500, 'insur': 5500, 'discount': { }, 'floor': '低/20' },
    { 'name': '当前\t', 'per_month': 6300, 'srv_month': 0, 'srv_once': 0, 'insur': 0, 'discount': { }, 'floor': '24/24' },
    #   no elavator
    #{ 'name': '上地东里', 'per_month': 6500, 'srv_month': 0, 'srv_once': 6500, 'insur': 6500, 'discount': { } },
    #{ 'name': '621小区(自如)', 'per_month': 6990, 'srv_month': 559.2, 'srv_once': 0, 'insur': 6990, 'discount': { } },
    #{ 'name': '621小区(自如)', 'per_month': 6590, 'srv_month': 527.2, 'srv_once': 0, 'insur': 6590, 'discount': { } },
]

def show_price(conf):
    pay_period = 0
    pay_list = []
    pay_total = 0
    for i in range(1, 13):
        discount = conf['discount'].get(i, conf['discount'].get(0, 1))
        if 1 == i:
            pay_period += conf['insur']     # 押金
            pay_period += conf['srv_once']  # 中介费
        pay_period += conf['per_month'] * discount
        pay_period += conf['srv_month']
        if 0 == i % 3:
            #print(pay_period)
            pay_list.append(str(pay_period))
            pay_total += pay_period
            pay_period = 0
    first_half_year_total = float(pay_list[0]) + float(pay_list[1])
    second_half_year_total = float(pay_list[2]) + float(pay_list[3])
    pay_total -= conf['insur']
    #print(half_year_total)
    print('{}\t{}\t{}\t{}\t\t{}\t\t{}\t\t{}'.format(
        conf['name'], str(conf['per_month']) + ('-' if conf['discount'] else ''), conf.get('floor', '-'),
        '\t'.join(pay_list), first_half_year_total, second_half_year_total, pay_total))
    pass

def show_discount():
    origin = 8390
    new_total = 0
    old_total = 8390 * 12
    for i in range(1, 13):
        if 1 == i:
            month_pay = 0.5 * origin
        else:
            month_pay = 0.9 * origin
        new_total += month_pay
    print(old_total, new_total, new_total / 12)

if __name__ == "__main__":
    print('房子\t\t月租\t楼层\t一期\t二期\t三期\t四期\t\t上半年合计\t下半年合计\t全年合计')
    for conf in conf_list:
        show_price(conf)
    #show_discount()
    pass
