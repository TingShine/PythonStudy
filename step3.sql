-- 1.把peoples表中school不是GDUFS的人全部找出来？（包括school为NULL的人）写出MySQL语句。
select * from peoples where school <> GDUFS or school is NULL;

-- 2.查找计算机系每次考试学生的平均成绩(最终显示学生姓名, 考试名称, 平均分)。
select name,exam_name,avg(grade) from peoples where department = "计算机系";

-- 3.查找女学霸（考试平均分达到80分或80分以上的女生的姓名, 分数）。
select name,grade from peoples where sex = 'f' 
and avg(grade)>=80;

-- 4.找出人数最少的院系以及其年度预算。
select department,budget from (select min(sum) from  sum where sum = count(ID) )

-- 5.计算机系改名了，改成计算机科学系（comp. sci.），写出mysql语句。
select replace('computer','w','n') from department --->comp.sci;

-- 6.修改每个系的年度预算，给该系的每个学生发2000元奖金。（修改每个系的年度预算为 原预算+该系人数*2000）
update department set budget = budget + (select count(ID) from student)*2000;

-- 7.向department表中插入一条数据, dept_name属性的值为avg_budget, building为空, 年度预算为所有院系的年度预算平均值.
insert into department values(NULL,NULL,'(select avg(budget) from department)');

-- 8. 删除计算机系中考试成绩平均分低于70的学生.
delete from exam where grade<70;

-- 9.找出所有正在谈恋爱,但是学习成绩不佳(考试平均分低于75)的学生,强制将其情感状态改为单身.
update student set emotion_state = 'single' where student.ID in(select ID from exam where grade < 70) and emotion_state = 'loving';

/*step3是由蒋盛义组的李立挺和曾云峰合作完成*/
