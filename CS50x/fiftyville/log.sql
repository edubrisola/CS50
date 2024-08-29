-- Keep a log of any SQL queries you execute as you solve the mystery.

.tables
airports              crime_scene_reports   people
atm_transactions      flights               phone_calls
bakery_security_logs  interviews
bank_accounts         passengers

.schema crime_scene_reports
CREATE TABLE crime_scene_reports (
    id INTEGER,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    street TEXT,
    description TEXT,
    PRIMARY KEY(id)
);

.schema interviews
CREATE TABLE interviews (
    id INTEGER,
    name TEXT,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    transcript TEXT,
    PRIMARY KEY(id)
);

.schema bakery_security_logs
CREATE TABLE bakery_security_logs (
    id INTEGER,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    hour INTEGER,
    minute INTEGER,
    activity TEXT,
    license_plate TEXT,
    PRIMARY KEY(id)
);

.schema atm_transactions
CREATE TABLE atm_transactions (
    id INTEGER,
    account_number INTEGER,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    atm_location TEXT,
    transaction_type TEXT,
    amount INTEGER,
    PRIMARY KEY(id)
);

.schema people
CREATE TABLE people (
    id INTEGER,
    name TEXT,
    phone_number TEXT,
    passport_number INTEGER,
    license_plate TEXT,
    PRIMARY KEY(id)
);

.schema phone_calls
CREATE TABLE phone_calls (
    id INTEGER,
    caller TEXT,
    receiver TEXT,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    duration INTEGER,
    PRIMARY KEY(id)
);

.schema bank_accounts
CREATE TABLE bank_accounts (
    account_number INTEGER,
    person_id INTEGER,
    creation_year INTEGER,
    FOREIGN KEY(person_id) REFERENCES people(id)
);

.schema flights
CREATE TABLE flights (
    id INTEGER,
    origin_airport_id INTEGER,
    destination_airport_id INTEGER,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    hour INTEGER,
    minute INTEGER,
    PRIMARY KEY(id),
    FOREIGN KEY(origin_airport_id) REFERENCES airports(id),
    FOREIGN KEY(destination_airport_id) REFERENCES airports(id)
);

.schema airports
CREATE TABLE airports (
    id INTEGER,
    abbreviation TEXT,
    full_name TEXT,
    city TEXT,
    PRIMARY KEY(id)
);

.schema passengers
CREATE TABLE passengers (
    flight_id INTEGER,
    passport_number INTEGER,
    seat TEXT,
    FOREIGN KEY(flight_id) REFERENCES flights(id)
);

// CRIME SCENE REPORTS
SELECT description FROM crime_scene_reports WHERE description LIKE "%duck%";
+-----+------+-------+-----+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| id  | year | month | day |     street      |                                                                                                       description                                                                                                        |
+-----+------+-------+-----+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 295 | 2023 | 7     | 28  | Humphrey Street | Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery. |
+-----+------+-------+-----+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

// INTERVIEWS
SELECT * FROM interviews WHERE day = 28 AND month = 7 AND year = 2023;
+-----+---------+------+-------+-----+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| id  |  name   | year | month | day |                                                                                                                                                     transcript                                                                                                                                                      |
+-----+---------+------+-------+-----+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 161 | Ruth    | 2023 | 7     | 28  | Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away. If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.                                                          |
| 162 | Eugene  | 2023 | 7     | 28  | I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.                                                                                                 |
| 163 | Raymond | 2023 | 7     | 28  | As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket. |
+-----+---------+------+-------+-----+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

sqlite> SELECT * FROM interviews WHERE name = 'Richard';

// BAKERY LOGS
SELECT * FROM bakery_security_logs WHERE day = 28 AND month = 7 AND year = 2023 AND activity = 'exit';
+-----+------+-------+-----+------+--------+----------+---------------+
| id  | year | month | day | hour | minute | activity | license_plate |
+-----+------+-------+-----+------+--------+----------+---------------+
| 261 | 2023 | 7     | 28  | 10   | 18     | exit     | 94KL13X       | // Bruce
| 263 | 2023 | 7     | 28  | 10   | 19     | exit     | 4328GD8       | // Luca
| 264 | 2023 | 7     | 28  | 10   | 20     | exit     | G412CB7       |
| 267 | 2023 | 7     | 28  | 10   | 23     | exit     | 0NTHK55       |
+-----+------+-------+-----+------+--------+----------+---------------+

// ATM TRANSACTIONS
SELECT * FROM atm_transactions WHERE day = 28 AND month = 7 AND year = 2023 AND atm_location = 'Leggett Street';
+-----+----------------+------+-------+-----+----------------+------------------+--------+
| id  | account_number | year | month | day |  atm_location  | transaction_type | amount |
+-----+----------------+------+-------+-----+----------------+------------------+--------+
| 246 | 28500762       | 2023 | 7     | 28  | Leggett Street | withdraw         | 48     | // Luca
| 264 | 28296815       | 2023 | 7     | 28  | Leggett Street | withdraw         | 20     |
| 266 | 76054385       | 2023 | 7     | 28  | Leggett Street | withdraw         | 60     |
| 267 | 49610011       | 2023 | 7     | 28  | Leggett Street | withdraw         | 50     | // Bruce
| 269 | 16153065       | 2023 | 7     | 28  | Leggett Street | withdraw         | 80     |
| 288 | 25506511       | 2023 | 7     | 28  | Leggett Street | withdraw         | 20     |
| 313 | 81061156       | 2023 | 7     | 28  | Leggett Street | withdraw         | 30     |
| 336 | 26013199       | 2023 | 7     | 28  | Leggett Street | withdraw         | 35     |
+-----+----------------+------+-------+-----+----------------+------------------+--------+

// BANK ACCOUNTS

SELECT * FROM bank_accounts WHERE person_id IN
    (SELECT id FROM people WHERE name = 'Sofia' OR name = 'Luca' OR name = 'Kelsey' OR name = 'Bruce');

+----------------+-----------+---------------+
| account_number | person_id | creation_year |
+----------------+-----------+---------------+
| 49610011       | 686048    | 2010          | // Bruce
| 28500762       | 467400    | 2014          | // Luca
+----------------+-----------+---------------+

// TRANSACTIONS OF LUCA

SELECT * FROM atm_transactions WHERE account_number = '28500762';
+-----+----------------+------+-------+-----+----------------+------------------+--------+
| id  | account_number | year | month | day |  atm_location  | transaction_type | amount |
+-----+----------------+------+-------+-----+----------------+------------------+--------+
| 7   | 28500762       | 2023 | 7     | 26  | Leggett Street | deposit          | 75     |
| 246 | 28500762       | 2023 | 7     | 28  | Leggett Street | withdraw         | 48     |
+-----+----------------+------+-------+-----+----------------+------------------+--------+


// TRANSACTIONS OF BRUCE AND ROBIN

SELECT * FROM atm_transactions WHERE account_number = '94751264' or account_number = '49610011';
+------+----------------+------+-------+-----+----------------------+------------------+--------+
|  id  | account_number | year | month | day |     atm_location     | transaction_type | amount |
+------+----------------+------+-------+-----+----------------------+------------------+--------+
| 39   | 49610011       | 2023 | 7     | 26  | Leggett Street       | withdraw         | 10     | // Bruce
| 104  | 94751264       | 2023 | 7     | 26  | Daboin Sanchez Drive | withdraw         | 25     | // Robin
| 242  | 94751264       | 2023 | 7     | 27  | Carvalho Road        | deposit          | 55     |
| 267  | 49610011       | 2023 | 7     | 28  | Leggett Street       | withdraw         | 50     |
| 417  | 94751264       | 2023 | 7     | 29  | Blumberg Boulevard   | deposit          | 90     |
| 585  | 94751264       | 2023 | 7     | 30  | Daboin Sanchez Drive | deposit          | 10     |
| 652  | 94751264       | 2023 | 7     | 30  | Leggett Street       | withdraw         | 10     |
| 671  | 94751264       | 2023 | 7     | 30  | Humphrey Lane        | deposit          | 15     |
| 822  | 94751264       | 2023 | 7     | 31  | Carvalho Road        | deposit          | 100    |
| 901  | 94751264       | 2023 | 7     | 31  | Carvalho Road        | withdraw         | 35     |
| 1103 | 94751264       | 2023 | 8     | 1   | Daboin Sanchez Drive | deposit          | 40     |
| 1121 | 94751264       | 2023 | 8     | 1   | Blumberg Boulevard   | withdraw         | 5      |
| 1229 | 94751264       | 2023 | 8     | 1   | Humphrey Lane        | withdraw         | 40     |
+------+----------------+------+-------+-----+----------------------+------------------+--------+

// PEOPLE

SELECT * FROM people WHERE name = 'Luca' OR name = 'Bruce';
+--------+-------+----------------+-----------------+---------------+
|   id   | name  |  phone_number  | passport_number | license_plate |
+--------+-------+----------------+-----------------+---------------+
| 467400 | Luca  | (389) 555-5198 | 8496433585      | 4328GD8       |
| 686048 | Bruce | (367) 555-5533 | 5773159633      | 94KL13X       |
+--------+-------+----------------+-----------------+---------------+

/ SENDERS TO LUCA

SELECT * FROM people WHERE phone_number = '(544) 555-8087' OR phone_number = '(609) 555-5876';
+--------+---------+----------------+-----------------+---------------+
|   id   |  name   |  phone_number  | passport_number | license_plate |
+--------+---------+----------------+-----------------+---------------+
| 561160 | Kathryn | (609) 555-5876 | 6121106406      | 4ZY7I8T       |
+--------+---------+----------------+-----------------+---------------+

/ RECEIVERS FROM BRUCE

SELECT * FROM people WHERE phone_number = '(375) 555-8161';
+--------+-------+----------------+-----------------+---------------+
|   id   | name  |  phone_number  | passport_number | license_plate |
+--------+-------+----------------+-----------------+---------------+
| 864400 | Robin | (375) 555-8161 | NULL            | 4V16VO0       |
+--------+-------+----------------+-----------------+---------------+


// DAY 29 FLIGHTS
SELECT * FROM flights WHERE day = 29 AND month = 7 AND year = 2023 ORDER BY hour, minute;
+----+-------------------+------------------------+------+-------+-----+------+--------+
| id | origin_airport_id | destination_airport_id | year | month | day | hour | minute |
+----+-------------------+------------------------+------+-------+-----+------+--------+
| 36 | 8                 | 4                      | 2023 | 7     | 29  | 8    | 20     |
| 43 | 8                 | 1                      | 2023 | 7     | 29  | 9    | 30     |
| 23 | 8                 | 11                     | 2023 | 7     | 29  | 12   | 15     |
| 53 | 8                 | 9                      | 2023 | 7     | 29  | 15   | 20     |
| 18 | 8                 | 6                      | 2023 | 7     | 29  | 16   | 0      |
+----+-------------------+------------------------+------+-------+-----+------+--------+

// AIRPORTS
SELECT * FROM airports;
+----+--------------+-----------------------------------------+---------------+
| id | abbreviation |                full_name                |     city      |
+----+--------------+-----------------------------------------+---------------+
| 1  | ORD          | O'Hare International Airport            | Chicago       |
| 2  | PEK          | Beijing Capital International Airport   | Beijing       |
| 3  | LAX          | Los Angeles International Airport       | Los Angeles   |
| 4  | LGA          | LaGuardia Airport                       | New York City |
| 5  | DFS          | Dallas/Fort Worth International Airport | Dallas        |
| 6  | BOS          | Logan International Airport             | Boston        |
| 7  | DXB          | Dubai International Airport             | Dubai         |
| 8  | CSF          | Fiftyville Regional Airport             | Fiftyville    |
| 9  | HND          | Tokyo International Airport             | Tokyo         |
| 10 | CDG          | Charles de Gaulle Airport               | Paris         |
| 11 | SFO          | San Francisco International Airport     | San Francisco |
| 12 | DEL          | Indira Gandhi International Airport     | Delhi         |
+----+--------------+-----------------------------------------+---------------+

// PASSENGERS
SELECT * FROM passengers WHERE flight_id = 36;
+-----------+-----------------+------+
| flight_id | passport_number | seat |
+-----------+-----------------+------+
| 36        | 7214083635      | 2A   |
| 36        | 1695452385      | 3B   |
| 36        | 5773159633      | 4A   |
| 36        | 1540955065      | 5C   |
| 36        | 8294398571      | 6C   |
| 36        | 1988161715      | 6D   |
| 36        | 9878712108      | 7A   |
| 36        | 8496433585      | 7B   |
+-----------+-----------------+------+

SELECT * FROM people WHERE passport_number IN
   (SELECT passport_number FROM passengers WHERE flight_id = 36);
+--------+--------+----------------+-----------------+---------------+
|   id   |  name  |  phone_number  | passport_number | license_plate |
+--------+--------+----------------+-----------------+---------------+
| 395717 | Kenny  | (826) 555-1652 | 9878712108      | 30G67EN       |
| 398010 | Sofia  | (130) 555-0289 | 1695452385      | G412CB7       |
| 449774 | Taylor | (286) 555-6063 | 1988161715      | 1106N58       |
| 467400 | Luca   | (389) 555-5198 | 8496433585      | 4328GD8       |
| 560886 | Kelsey | (499) 555-9472 | 8294398571      | 0NTHK55       |
| 651714 | Edward | (328) 555-1152 | 1540955065      | 130LD9Z       |
| 686048 | Bruce  | (367) 555-5533 | 5773159633      | 94KL13X       |
| 953679 | Doris  | (066) 555-9701 | 7214083635      | M51FA04       |
+--------+--------+----------------+-----------------+---------------+

+--------+--------+----------------+-----------------+---------------+
|   id   |  name  |  phone_number  | passport_number | license_plate |
+--------+--------+----------------+-----------------+---------------+
| 398010 | Sofia  | (130) 555-0289 | 1695452385      | G412CB7       |
| 467400 | Luca   | (389) 555-5198 | 8496433585      | 4328GD8       |
| 560886 | Kelsey | (499) 555-9472 | 8294398571      | 0NTHK55       |
| 686048 | Bruce  | (367) 555-5533 | 5773159633      | 94KL13X       |
+--------+--------+----------------+-----------------+---------------+

SELECT license_plate FROM bakery_security_logs WHERE day = 28 AND month = 7 AND year = 2023 AND activity = 'exit'
AND license_plate IN
    (SELECT license_plate FROM people WHERE passport_number IN
   (SELECT passport_number FROM passengers WHERE flight_id = 36));
+---------------+
| license_plate |
+---------------+
| 94KL13X       |
| 4328GD8       |
| G412CB7       |
| 0NTHK55       |
| 1106N58       |
+---------------+

SELECT phone_number FROM people WHERE phone_number IN
   (SELECT phone_number FROM people WHERE passport_number IN
   (SELECT passport_number FROM passengers WHERE flight_id = 36));

+----------------+
|  phone_number  |
+----------------+
| (130) 555-0289 |
| (389) 555-5198 |
| (499) 555-9472 |
| (367) 555-5533 |
+----------------+


// PHONE CALLS
SELECT * FROM phone_calls WHERE day = 28 AND month = 7 AND year = 2023 AND duration <= 60;
+-----+----------------+----------------+------+-------+-----+----------+
| id  |     caller     |    receiver    | year | month | day | duration |
+-----+----------------+----------------+------+-------+-----+----------+
| 221 | (130) 555-0289 | (996) 555-8899 | 2023 | 7     | 28  | 51       |
| 224 | (499) 555-9472 | (892) 555-8872 | 2023 | 7     | 28  | 36       |
| 233 | (367) 555-5533 | (375) 555-8161 | 2023 | 7     | 28  | 45       | // Bruce Calls
| 234 | (609) 555-5876 | (389) 555-5198 | 2023 | 7     | 28  | 60       | // Luca Receives
| 251 | (499) 555-9472 | (717) 555-1342 | 2023 | 7     | 28  | 50       |
| 254 | (286) 555-6063 | (676) 555-6554 | 2023 | 7     | 28  | 43       |
| 255 | (770) 555-1861 | (725) 555-3243 | 2023 | 7     | 28  | 49       |
| 261 | (031) 555-6622 | (910) 555-3251 | 2023 | 7     | 28  | 38       |
| 279 | (826) 555-1652 | (066) 555-9701 | 2023 | 7     | 28  | 55       |
| 281 | (338) 555-6650 | (704) 555-2131 | 2023 | 7     | 28  | 54       |
+-----+----------------+----------------+------+-------+-----+----------+
