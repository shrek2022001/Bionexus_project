-- Create a new database
CREATE DATABASE IF NOT EXISTS bionexus_db_2;
USE bionexus_db_2;

-- Create a table for storing articles
CREATE TABLE IF NOT EXISTS articles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title TEXT,
    abstract TEXT,
    link TEXT
);

-- Create a table for storing authors
CREATE TABLE IF NOT EXISTS authors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name TEXT
);

-- Create a table to link articles and authors (many-to-many relationship)
CREATE TABLE IF NOT EXISTS article_authors (
    article_id INT,
    author_id INT,
    PRIMARY KEY (article_id, author_id),
    FOREIGN KEY (article_id) REFERENCES articles(id),
    FOREIGN KEY (author_id) REFERENCES authors(id)
);

SHOW columns FROM articles;
SELECT * FROM articles;
