use digital_health;

insert into user (email, password, first_name, last_name, phone_number)
values ('jackie.woodburn@gmail.com', 'password_1', 'Jackie', 'Woodburn', '07512656498'),
('jessie.auguste@gmail.com', 'password_2', 'Jessie', 'Auguste', '07123456789'),
('suh.rashid@gmail.com', 'password_3', 'Suh', 'Rashid', '07712345678'),
('jake.peralta@yahoo.com', 'die_hard', 'Jake', 'Peralta', '07781234567'),
('amy.santiago@hotmail.com', 'b99_binders', 'Amy', 'Santiago', '07881234567'),
('raymond.holt@nypd.com', 'Ch3dd4rTheD0g', 'Raymond', 'Holt', '07899123456'),
('rosa.diaz@gmail.com', 'argo1234', 'Rosa', 'Diaz', '07885674321'),
('terry.jeffords@precinct.com', 'cagneyNlacey2', 'Terry', 'Jeffords', '07123987654');

insert into quiz_question (question_string)
values ('Where do you spend the most time online?'),
('How many hours per day do you spend looking at a screen?'),
('What is the most common way you practice mindfulness, if at all?'),
('What has been your most common mood in the past week?'),
('What sort of online content do you most want improve your digital relationship with?');

insert into quiz_answer_option (answer_string, question_id)
values ('News outlets', 1), ('Social media', 1), ('Learning resources', 1), ('Online video', 1),
('< 1 hour', 2), ('1-3 hours', 2), ('3-6 hours', 2), ('6-9 hours', 2), ('> 9 hours', 2),
('Yoga', 3), ('Meditation', 3), ('Breathing exercises', 3), ('Gardening', 3), ('Other', 3),
('Happy', 4), ('Calm', 4), ('Neutral', 4), ('Anxious', 4), ('Sad', 4), 
('News outlets', 5), ('Social media', 5), ('Learning resources', 5), ('Online video', 5);

insert into  quiz_user_answer (user_id, answer_1, answer_2, answer_3, answer_4, answer_5)
values (1, 4, 4, 2, 3, 2),
(2, 1, 3, 1, 2, 2),
(3, 1, 3, 5, 1, 4),
(4, 1, 2, 3, 3, 2),
(5, 3, 2, 1, 4, 5),
(6, 4, 2, 3, 4, 5),
(7, 3, 1, 4, 5, 3),
(8, 2, 5, 1, 1, 3);

insert into journal_entry (user_id, date, time, title, content)
values (1, CURDATE(), CURRENT_TIME(), 'Introductions', 'Hello this is my first blog post'),
(5, CURDATE(), CURRENT_TIME(), 'Something about Mindfulness', 'Today was a nice day blah blah blah.'),
(8, CURDATE(), CURRENT_TIME(), 'Dogs are Great', 'Dogs make me happy when I am stressed.'),
(4, CURDATE(), CURRENT_TIME(), 'Blue Light Bad', 'I want to recommend a blue light filter to the community. It helps me sleep.'),
(2, CURDATE(), CURRENT_TIME(), 'Yoga Before Bed', 'Recently swapped screentime for yoga before bed after reading a great article on Digital Health.'),
(6, CURDATE(), CURRENT_TIME(), 'Reduced time online', 'Today I was in a good mood and noticed it correlated to less time at my screen.');

insert into comment (user_id, journal_id, content, date, time)
values (1, 4, 'Have you tried blue light glasses?', CURDATE(), CURRENT_TIME()),
(4, 6, 'Congrats!', CURDATE(), CURRENT_TIME()),
(4, 1, 'Welcome to the club :)', CURDATE(), CURRENT_TIME()),
(8, 2, 'Blah blah blah.', CURDATE(), CURRENT_TIME()),
(5, 3, 'I like whippets best.', CURDATE(), CURRENT_TIME()),
(3, 5, 'Great work!', CURDATE(), CURRENT_TIME());

insert into user_goal (goal)
values ('Meditate every day.'),
("Write in my journal when I'm stressed."),
('Unfollow people on Instagram who give me unrealistic expectations.'),
("Limit my time on Twitter to 15 minutes per day."),
("Allocate time in the day to check the news, and don't check it outside of these times."),
("Make breathing exercises a part of my lunchtime routine.");

insert into habit_tracker (user_id, mindful_seconds, journal_words, articles_read, article_seconds_read)
values (1, 600, 0, 0, 0),
(2, 1200, 200, 0, 0),
(3, 0, 500, 4, 3000),
(4, 60, 0, 0, 0),
(5, 0, 0, 0, 0),
(6, 0, 0, 0, 0),
(7, 0, 0, 0, 0),
(8, 0, 0, 0, 0);

-- Have not yet input data to articles (external_author, external_source, article_tags, external_article)


