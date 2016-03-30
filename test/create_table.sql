create table user(id int primary key not null auto_increment,
    name varchar(15) not null,
    passwd varchar(50) not null,
    profession_id int not null,
    sex int not null,
    grade int not null,
    class int not null,
    tel char(11) not null,
    old int not null);
