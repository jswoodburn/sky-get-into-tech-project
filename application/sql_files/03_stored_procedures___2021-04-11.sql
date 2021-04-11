use digital_health;

drop procedure if exists createJournalEntry;
delimiter //
create procedure createJournalEntry
(in id int, journal_title varchar(100), journal_content varchar(8000))
begin
insert into journal_entry (user_id, date, time, title, content)
values (id, CURDATE(), CURRENT_TIME(), journal_title, journal_content);
end //
delimiter ;

call createJournalEntry(1, 'Testing Procedure 2', 'A temporary journal to test stored procedures');

drop procedure if exists editJournalEntry;
delimiter //
create procedure editJournalEntry
(in id int, journal_content varchar(8000))
begin
update journal_entry set content = journal_content
where journal_id = id;
end //
delimiter ;

call editJournalEntry(8, 'A temporary journal to test stored procedures, that has now been edited.');
