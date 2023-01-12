--- Create a table users with country field
CREATE TABLE IF NOT EXISTS users (
  id INT NOT NULL AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL UNIQUE,
  name VARCHAR(255), PRIMARY KEY (id),
  country ENUM('US', 'CO', 'TN') NOT NULL 'US'
);
