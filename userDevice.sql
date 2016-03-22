-- schema.sql

drop database if exists koovox;

create database koovox;

use koovox;

grant select, insert, update, delete on koovox.* to 'youqiukun'@'localhost' identified by '123456';

create table userdevice (
    `id` integer not null primary key auto_increment,
    `deviceId` varchar(50) not null,
    `deviceType` varchar(50) not null,
    `openId` varchar(50) not null,
	`fromUserName` varchar(50) not null,
    unique key `idx_name` (`deviceId`)
) ;

