import random

capitals = {'山东': '济南',
            '河北': '石家庄',
            '吉林': '长春',
            '黑龙江': '哈尔滨',
            '辽宁': '沈阳',
            '内蒙古': '呼和浩特',
            '新疆': '乌鲁木齐',
            '甘肃': '兰州',
            '宁夏': '银川',
            '山西': '太原',
            '陕西': '西安',
            '河南': '郑州',
            '安徽': '合肥',
            '江苏': '南京',
            '浙江': '杭州',
            '福建': '福州',
            '广东': '广州',
            '江西': '南昌',
            '海南': '海口',
            '广西': '南宁',
            '贵州': '贵阳',
            '湖南': '长沙',
            '湖北': '武汉',
            '四川': '成都',
            '云南': '昆明',
            '西藏': '拉萨',
            '青海': '西宁',
            '天津': '天津',
            '上海': '上海',
            '重庆': '重庆',
            '北京': '北京',
            '台湾': '台北'}

paper_num = int(input("你要出几份卷子：\n"))
question_num=int(input("每套卷子有几道题：\n"))

for paper in range(paper_num):
    question_file=open('juanzi{}.txt'.format(paper + 1),mode='w',encoding='utf-8')
    answer_file=open('juanzi_ans{}.txt'.format(paper + 1),mode='w',encoding='utf-8')

    question_file.write( ' '*20+'省会匹配考试{}\n'.format(paper+1))
    question_file.write('姓名：\n年级：\n学号：\n')

    quesList=list(capitals.keys())
    random.shuffle(quesList)
    quesList=random.sample(quesList,question_num)

    for i in range(len(quesList)):
        question_file.write('{} 、 {}的省会是(    )\n'.format(i+1,quesList[i]))
        option='ABCD'
        #先加入正确答案
        each_answer_list=[capitals[quesList[i]]]
        #全部的错误答案
        wrong=list(capitals.values())
        wrong.remove(capitals[quesList[i]])
        #得到三个错误答案
        wrong=random.sample(wrong,3)
        #错误加正确得到全部答案
        each_answer_list += wrong
        random.shuffle(each_answer_list)
        k=0
        correct=''#正确答案
        for j in option:
            question_file.write('{} . {}\n'.format(j,each_answer_list[k]))
            if each_answer_list[k]==capitals[quesList[i]] :
                correct=j
            k+=1


        #把正确答案写入juanzi_ans{}
        answer_file.write('{} . {}\n'.format(i+1,correct))
    question_file.close()
    answer_file.close()


