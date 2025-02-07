INSERT INTO users (username, password) VALUES
    ('ankush', '$2b$12$yGi6zKGbRYzH9aE08kKpO.O8KHZ6SrbmtwRh8xxmCg3LeKwkDbIFS'),
    ('het', '$2b$12$craQto3WlctEfWMmUpyyNeY7nzADwL91orH7xubzE.vk4ucAIykUW'),
    ('siddhi', '$2b$12$jypycBwrp25EnItKMTcxWe5KnFMkW3Qm8uExrHq1WglH10fIi6SPy'),
    ('shlok', '$2b$12$CKpsFw4f.5dxFEwH/aagOudLeBF/AL6TV3pvAfjoGiMg7nXIOFUdG'),
    ('dhwani', '$2b$12$RLTIJSbMtb3GzLTyYjlFwO1RWaTS3IhFbgdqmw2K9RXw8/S5xSAn.');


-- Insert Categories (Predefined + User Defined)
INSERT INTO categories (user_id, category_name, is_predefined) VALUES
    (NULL, 'Food', TRUE),
    (NULL, 'Rent', TRUE),
    (NULL, 'Utilities', TRUE),
    (NULL, 'Transportation', TRUE),
    (NULL, 'Entertainment', TRUE),
    (1, 'Gym', FALSE),
    (1, 'Medical', FALSE),
    (2, 'Shopping', FALSE),
    (3, 'Dining Out', FALSE),
    (4, 'Travel', FALSE),
    (5, 'Subscriptions', FALSE);

-- Insert Expenses (2 Years of Detailed Data for Each User)
INSERT INTO expenses (user_id, category_id, amount, description, date) VALUES
    -- John Doe (User 1)
    (1, 1, 250.00, 'Groceries from Walmart', '2023-01-10'),
    (1, 2, 1200.00, 'Monthly Rent', '2023-01-01'),
    (1, 3, 90.00, 'Electricity Bill', '2023-01-15'),
    (1, 4, 50.00, 'Uber Rides', '2023-01-05'),
    (1, 6, 30.00, 'Gym Membership', '2023-01-07'),
    (1, 7, 200.00, 'Doctor Consultation', '2023-01-20'),
    
    -- Alice Smith (User 2)
    (2, 1, 300.00, 'Groceries', '2023-02-12'),
    (2, 2, 1000.00, 'Rent Payment', '2023-02-01'),
    (2, 3, 80.00, 'Internet Bill', '2023-02-10'),
    (2, 5, 60.00, 'Netflix Subscription', '2023-02-08'),
    (2, 8, 500.00, 'Shopping Clothes', '2023-02-15'),
    
    -- Mike Jones (User 3)
    (3, 1, 270.00, 'Weekly Grocery', '2023-03-05'),
    (3, 2, 1100.00, 'House Rent', '2023-03-01'),
    (3, 3, 70.00, 'Gas Bill', '2023-03-20'),
    (3, 4, 45.00, 'Public Transport', '2023-03-18'),
    (3, 9, 100.00, 'Fine Dining', '2023-03-22'),

    -- Sarah Lee (User 4)
    (4, 1, 290.00, 'Supermarket Shopping', '2023-04-02'),
    (4, 2, 1250.00, 'Apartment Rent', '2023-04-01'),
    (4, 3, 110.00, 'Gas & Electricity', '2023-04-12'),
    (4, 10, 800.00, 'Flight to NY', '2023-04-25'),
    
    -- David Williams (User 5)
    (5, 1, 260.00, 'Grocery Bill', '2023-05-10'),
    (5, 2, 950.00, 'Rent Deposit', '2023-05-01'),
    (5, 5, 40.00, 'Amazon Prime', '2023-05-03'),
    (5, 11, 100.00, 'Spotify + Apple Music', '2023-05-20'),

    -- Expenses Over 2 Years (Repeat for Each User)
    (1, 1, 255.00, 'Groceries from Walmart', '2024-01-10'),
    (1, 2, 1300.00, 'Monthly Rent', '2024-01-01'),
    (1, 3, 95.00, 'Electricity Bill', '2024-01-15'),
    (1, 4, 55.00, 'Uber Rides', '2024-01-05'),
    (1, 6, 35.00, 'Gym Membership', '2024-01-07'),
    (1, 7, 250.00, 'Medical Checkup', '2024-01-20'),
    (2, 1, 320.00, 'Groceries', '2024-02-12'),
    (2, 2, 1050.00, 'Rent Payment', '2024-02-01'),
    (2, 3, 85.00, 'Internet Bill', '2024-02-10'),
    (2, 5, 70.00, 'Streaming Services', '2024-02-08'),
    (2, 8, 550.00, 'Shopping Clothes', '2024-02-15');

-- Insert User Logs (Track Actions)
INSERT INTO user_logs (user_id, action, timestamp) VALUES
    (1, 'Added expense for Groceries', '2023-01-10 10:30:00'),
    (1, 'Paid Monthly Rent', '2023-01-01 08:00:00'),
    (2, 'Subscribed to Netflix', '2023-02-08 12:45:00'),
    (3, 'Dined out at a restaurant', '2023-03-22 19:15:00'),
    (4, 'Booked flight to NY', '2023-04-25 15:00:00'),
    (5, 'Subscribed to Spotify', '2023-05-20 17:30:00'),
    (1, 'Updated expense for Uber rides', '2024-01-05 09:00:00'),
    (2, 'Paid Rent for February', '2024-02-01 10:00:00'),
    (3, 'Deleted an old expense', '2024-03-10 11:30:00'),
    (4, 'Viewed yearly spending report', '2024-04-15 14:45:00'),
    (5, 'Created a new expense category', '2024-05-05 16:10:00');

