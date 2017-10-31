
import requests
import json
from bs4 import BeautifulSoup

def getdict():
    session = requests.Session()

    logindata = {'j_username': ‘#’, 'j_password': ‘#’}
    loginurl = r'http://elearning.ustb.edu.cn/choose_courses/j_spring_security_check'
    loginpost = session.post(loginurl, data = logindata)

    getjsondata = {'listXnxq': '2017-2018-1','uid': ‘#’}
    getjsonurl = r'http://elearning.ustb.edu.cn/choose_courses/choosecourse/commonChooseCourse_courseList_loadTermCourses.action'
    getjsonpost = session.post(getjsonurl, data = getjsondata)
    lessonsjson = getjsonpost.content
    soup = BeautifulSoup(lessonsjson, "lxml")
    soup = soup.text
    lessonsdict = json.loads(soup)
    return lessonsdict



def output(f):
    lessonsdict = f()
    for key in lessonsdict.keys():
        if key == 'selectedCourses':
            # print(lessonsdict[key])
            lessonlist = lessonsdict[key]
            for i in range(len(lessonlist)):
                # print("序号：%s  值：%s\n" % (i + 1, lessonlist[i]))
                for key in lessonlist[i]:
                    if key == 'JSM':
                        # print(lessonlist[i][key])
                        for j in range(len(lessonlist[i][key])):
                            for key_ in lessonlist[i][key][j]:
                                if key_ == 'JSM':
                                    print(lessonlist[i][key][j][key_])
                    if key == 'DYKCM':
                        print(lessonlist[i][key])

def __main():
    output(getdict)


__main()
