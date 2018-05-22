#! /user/bin/env python
#coding:utf-8

import requests
import re

def getHtmlText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""

def parseHtml(InfoL,html):
    try:
        priceL=re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        titleL=re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(priceL)):
            price=eval(priceL[i].split(':')[1])
            title=eval(titleL[i].split(':')[1])
            InfoL.append([price,title])
    except:
        print('')

def printGoodsList(InfoL):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in InfoL:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))

def main():
    goods='背包'#str(input('需要的商品))
    depth=3  #int(input(需要搜索的页数))
    start_url='https://s.taobao.com/search?q='+goods
    InfoList=[]
    for i in range(depth):
        try:
            url=start_url+'&s='+str(44*i)
            html=getHtmlText(url)
            parseHtml(InfoList,html)
        except:
            continue
    printGoodsList(InfoList)

main()