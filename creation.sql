create table band
(
	id serial primary key,
	name varchar(32)
);
create table students
(
	id serial primary key,
	name varchar(32),
	id_group integer references band (id)
);

create table cates
(
	id serial primary key,
	name varchar(50)
);

create table templates
(
	id serial primary key,
	name varchar(60),
	text text,
	id_cat int references cates (id)
);


create table variants
(
	id serial primary key,
	id_template int[],
	text text,
	answers text,
	num int
);
create table student_var
(
	id serial primary key,
	id_student int references students (id),
	id_var int references variants (id),
	data timestamp
);
create table tasks
(
	id serial,
	id_stud_var int references student_var (id),
	text_task text,
	text_ans text
);