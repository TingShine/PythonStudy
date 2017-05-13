#coding=utf-8
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
if __name__ == '__main__':
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='*******',       #省略本人数据库密码
        charset="utf8",
        db='step1',
    )
    cursor = conn.cursor()
#将deptment.txt里的内容插入数据库中dept_name表中
    def prc_line(line):
        _result = line.decode("utf-8").strip().split(" ")
        return _result


    with open("university/department.txt","r") as f:
        datas = [prc_line(line) for line in f.readlines()]

    for d in datas:
        cursor.execute("insert into dept_name(dept_name,building,budget) values('%s','%s','%s')"%(d[0],d[1],d[2]))

    # cursor.execute("select * from dept_name")
    # lines = cursor.fetchall()
    # for line in lines:
    #     print line

    #将student.txt里的内容插入数据库中student表中
    def prs_line(line):
        _result = line.decode("utf-8").strip().split(" ")
        _result[0] = int(_result[0])
        _result[3] = int(_result[3])
        return _result


    with open("university/student.txt","r") as f:
        datas0 = [prs_line(line) for line in f.readlines()]

    for d in datas0:
        cursor.execute("insert into student(ID,name,sex,age,emotin_state,dept_name) values('%d','%s','%s','%d','%s','%s')"%(d[0],d[1],d[2],d[3],d[4],d[5]))


    # 将exam.txt里的内容插入数据库中exam表中
    def pre_line(line):
        _result = line.decode("utf-8").strip().split(" ")
        _result[0] = int(_result[0])
        return _result


    with open("university/exam.txt","r") as f:
        datas1 = [pre_line(line) for line in f.readlines()]

    for d in datas1:
        cursor.execute("insert into exam(student_ID,exam_name,grade) values('%d','%s','%s)"%(d[0],d[1],d[2]))
    conn.commit()
    cursor.close()
    conn.close()