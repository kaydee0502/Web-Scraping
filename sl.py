#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 07:12:28 2021

@author: kaydee
"""

import scrapy
import requests
import matplotlib.pyplot as plt

url = "https://www.sololearn.com/Profile/5697123"

html = requests.get(url)

html = html.text

selector = scrapy.Selector(text=html)

courses_css = "div.userCourses"

courses = selector.css(courses_css)

courses_sections = courses.css("div > a::attr(title)")
xp = courses.css("div > p::text")
course_list = courses_sections.extract()

print(xp.extract())
print(courses_sections.extract())
xp_int = list(map(lambda x : int(x[:-3]),list(xp.extract())))


plt.bar(course_list,xp_int)
plt.xticks(rotation=90)
plt.xlabel("Courses")
plt.ylabel("XP")
plt.plot()