-- Database and table used by video_game_management_system12_beta.py
-- Run with:  mysql -u root -p < schema.sql

CREATE DATABASE IF NOT EXISTS interactive;
USE interactive;

CREATE TABLE IF NOT EXISTS management (
  GAMEID    VARCHAR(20)  NOT NULL,
  GAMENAME  VARCHAR(100),
  GAMEYEAR  VARCHAR(4),
  SHORTID   VARCHAR(20),
  RATING    VARCHAR(30),
  COMPANY   VARCHAR(100),
  EXCLUSIVE VARCHAR(3),
  PLATFORM  VARCHAR(100),
  PRIMARY KEY (GAMEID)
);
