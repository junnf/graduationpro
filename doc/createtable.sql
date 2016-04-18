
create table user_dep(dep_num int(5) not null primary key ,
    name varchar(20) not null, passwd varchar(50),sexuality int(1));

create table class_table(course_id int(7) not null,week_num int(1) not null,
    week_day int(1) not null,time int(1) not null,location varchar(50) not null,
    class_id int(7) not null,primary key(course_id,week_num,week_day,time));
 
create table class(class_id int(7) not null primary key,class_name varchar(30) not null,
teacher_name varchar(15) not null,other varchar(100) not null);

create table user_student(uid int primary key not null,name varchar(20) unique key not null,
    passwd varchar(50) not null,sexuality int(1) not null, course_id int(7) not null,
    //CONSTRAINT user_clstble FOREIGN KEY (course_id) REFERENCES class_table(course_id));
    
    
insert into user_student values(201215121,'junningliu','ljn7168396',1,1110001);

insert into user_dep values(11101,'admin_a','ljn7168396123',1);
insert into class values(1110001,"liping","operating system","lianxifangshiTelEmailQQ");  


得到courseid conn.query("select * from user_student where name = 'junningliu'")[0]['course_id']

自然连接
conn.query('select * from class a NATURAL JOIN class_table where course_id = {};'.format(_course_id))


