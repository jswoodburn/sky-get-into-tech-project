create database digital_health;
-- uncomment line 1 if running script for first time

use digital_health;

create table user (
user_id int auto_increment not null primary key,
email varchar(100) not null,
password varchar(50) not null,
first_name varchar(50) not null,
last_name varchar(50) not null,
phone_number char(11) not null
);

create table quiz_question (
question_id int auto_increment not null primary key,
question_string varchar(200) not null
);

create table quiz_answer_option (
answer_id int auto_increment not null primary key,
answer_string varchar(200) not null,
question_id int not null,
foreign key (question_id) references quiz_question (question_id)
);

create table quiz_user_answer (
user_id int not null primary key,
answer_1 int,
answer_2 int, 
answer_3 int,
answer_4 int,
answer_5 int,
foreign key (user_id) references user (user_id),
foreign key (answer_1) references quiz_answer_option (answer_id),
foreign key (answer_2) references quiz_answer_option (answer_id),
foreign key (answer_3) references quiz_answer_option (answer_id),
foreign key (answer_4) references quiz_answer_option (answer_id),
foreign key (answer_5) references quiz_answer_option (answer_id)
);

create table journal_entry (
journal_id int auto_increment not null primary key,
user_id int not null,
date date not null,
time time not null,
title varchar(100) not null,
content varchar(8000) not null,
foreign key (user_id) references user (user_id)
);

create table comment (
comment_id int auto_increment not null primary key,
user_id int not null,
journal_id int not null,
content varchar(3000) not null,
date date not null,
time time not null,
foreign key (user_id) references user (user_id),
foreign key (journal_id) references journal_entry (journal_id)
);

create table user_goal (
goal_id int auto_increment not null primary key,
goal varchar(200) not null
);

create table habit_tracker (
user_id int not null primary key,
mindful_seconds int,
journal_words int,
articles_read int,
article_seconds_read int,
foreign key (user_id) references user (user_id)
);

create table external_author (
author_id int auto_increment not null primary key,
author_name varchar(100) not null
); 

create table external_source (
source_id int auto_increment not null primary key,
source_name varchar(50) not null
);

create table article_tags (
tag_id int auto_increment not null primary key,
tag varchar(20) not null
);

create table external_article (
url varchar(600) not null primary key,
date_added date not null,
time_added time not null,
article_title varchar(500) not null,
article_author int,
publication int,
tag_1 int,
tag_2 int,
tag_3 int,
foreign key (article_author) references external_author (author_id),
foreign key (publication) references external_source (source_id),
foreign key (tag_1) references article_tags (tag_id),
foreign key (tag_2) references article_tags (tag_id),
foreign key (tag_3) references article_tags (tag_id)
);
