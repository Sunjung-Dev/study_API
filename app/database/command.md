접속하기 
mysql -u root -p

database 목록 보기 
show databases;

테이블 생성하기 
create table tablename(
    column1 int primary key,

)

데이터베이스 사용하기 
use db이름 

테이블 생성 데이터 보기 
explain 테이블 이름;

데이터 삽입하기 
insert into 테이블 이름(values들);