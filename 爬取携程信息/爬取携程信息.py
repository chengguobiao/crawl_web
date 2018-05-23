# _*_ coding:utf-8 _*_
# Author:liu

import urllib.request
from bs4 import BeautifulSoup



'''''
目标:获取酒店最低房价和评论总数
'''
url2 = "http://m.ctrip.com/html5/hotel/HotelDetail/435383.html"

html2 = urllib.request.urlopen(url2).read().decode('utf-8')

soup_comment = BeautifulSoup(html2, 'lxml')

soup_grades = BeautifulSoup(html3, 'lxml')

# 获取酒店各项评分数据
result_grades = soup_grades.find_all(attrs={"class": "ve-txt"})
result_grades = str(result_grades)
soup32 = BeautifulSoup(result_grades, 'lxml')

result33 = soup32.find_all('em')
userRecommendRate = result33[0].string
hRating = result33[1].string
eRating = result33[2].string
sRating = result33[3].string
iRating = result33[4].string

print("用户推荐为:{}".format(userRecommendRate))
print("卫生评分为:{}分".format(hRating))
print("环境评分为:{}分".format(eRating))
print("服务评分为:{}分".format(sRating))
print("设施评分为:{}分".format(iRating))

# 提取用户评论数据



for i in range(0, 10):
    result_pf = soup_grades.find_all(attrs={"class": "g-ve"})
    userRating = result_pf[i].string
    print("评分为:{}".format(userRating))

    # userName = result35[i].get_text()
    result_data = soup_grades.find_all(attrs={"class": "tree-ellips-line6"})
    commentText = result_data[i].get_text()
    print("评论内容为:{}".format(commentText))
