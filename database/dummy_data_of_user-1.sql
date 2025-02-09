-- Insert categories for user_id = 1
INSERT INTO categories (user_id, category_name, is_predefined) VALUES
    (1, 'Rent', FALSE),
    (1, 'Food', FALSE),
    (1, 'Utilities', FALSE),
    (1, 'Transportation', FALSE),
    (1, 'Gym', FALSE),
    (1, 'Medical', FALSE),
    (1, 'Entertainment', FALSE)
ON CONFLICT (user_id, category_name) DO NOTHING;

-- Insert expenses for user_id = 1
INSERT INTO expenses (user_id, category_id, amount, description, date) VALUES
    -- Rent (Monthly)
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Rent'), 1200.00, 'Monthly Rent', '2023-01-01'),
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Rent'), 1250.00, 'Monthly Rent', '2023-02-01'),
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Rent'), 1300.00, 'Monthly Rent', '2023-03-01'),
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Rent'), 1350.00, 'Monthly Rent', '2023-04-01'),
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Rent'), 1400.00, 'Monthly Rent', '2023-05-01'),
    
    -- Food (Weekly)
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Food'), 50.00, 'Grocery Shopping', '2023-01-05'),
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Food'), 45.00, 'Supermarket Visit', '2023-01-12'),
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Food'), 60.00, 'Restaurant Bill', '2023-01-19'),
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Food'), 55.00, 'Weekend Dining', '2023-01-26'),

    -- Utilities (Monthly)
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Utilities'), 90.00, 'Electricity Bill', '2023-01-15'),
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Utilities'), 85.00, 'Water Bill', '2023-02-15'),
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Utilities'), 100.00, 'Gas Bill', '2023-03-15'),

    -- Transportation (Daily Commuting)
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Transportation'), 10.00, 'Bus Fare', '2023-01-03'),
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Transportation'), 20.00, 'Taxi Ride', '2023-01-10'),
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Transportation'), 25.00, 'Gas Refill', '2023-01-17'),
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Transportation'), 15.00, 'Uber Ride', '2023-01-24'),

    -- Gym (Subscription)
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Gym'), 35.00, 'Monthly Gym Membership', '2023-01-07'),
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Gym'), 35.00, 'Monthly Gym Membership', '2023-02-07'),
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Gym'), 35.00, 'Monthly Gym Membership', '2023-03-07'),

    -- Medical (Occasional)
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Medical'), 200.00, 'Doctor Visit', '2023-02-20'),
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Medical'), 75.00, 'Pharmacy', '2023-03-05'),

    -- Entertainment (Weekends)
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Entertainment'), 100.00, 'Movie Tickets', '2023-02-10'),
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Entertainment'), 120.00, 'Concert Ticket', '2023-03-18'),
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Entertainment'), 80.00, 'Streaming Services', '2023-04-05');


-- Insert categories for user_id = 1
INSERT INTO categories (user_id, category_name, is_predefined) VALUES
    (1, 'Rent', FALSE),
    (1, 'Food', FALSE),
    (1, 'Utilities', FALSE),
    (1, 'Transportation', FALSE),
    (1, 'Gym', FALSE),
    (1, 'Medical', FALSE),
    (1, 'Entertainment', FALSE)
ON CONFLICT (user_id, category_name) DO NOTHING;

-- Insert expenses for user_id = 1
INSERT INTO expenses (user_id, category_id, amount, description, date) VALUES
    -- Rent (Monthly) for 2023, 2024, and 2025
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Rent'), 1450.00, 'Monthly Rent', '2024-01-01'),
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Rent'), 1500.00, 'Monthly Rent', '2024-02-01'),
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Rent'), 1550.00, 'Monthly Rent', '2025-01-01'),
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Rent'), 1600.00, 'Monthly Rent', '2025-02-01'),

    -- Food (Weekly) for 2024 and 2025
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Food'), 65.00, 'Grocery Shopping', '2024-01-05'),
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Food'), 70.00, 'Restaurant Bill', '2024-02-10'),
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Food'), 75.00, 'Weekend Dining', '2025-01-15'),
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Food'), 80.00, 'Grocery Shopping', '2025-02-20'),

    -- Utilities (Monthly) for 2024 and 2025
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Utilities'), 105.00, 'Electricity Bill', '2024-01-15'),
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Utilities'), 110.00, 'Water Bill', '2024-02-15'),
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Utilities'), 120.00, 'Gas Bill', '2025-01-15'),
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Utilities'), 125.00, 'Electricity Bill', '2025-02-15'),

    -- Transportation (Daily Commuting) for 2024 and 2025
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Transportation'), 30.00, 'Uber Ride', '2024-01-03'),
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Transportation'), 35.00, 'Gas Refill', '2024-02-10'),
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Transportation'), 40.00, 'Taxi Ride', '2025-01-12'),
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Transportation'), 45.00, 'Bus Fare', '2025-02-18'),

    -- Gym (Subscription) for 2024 and 2025
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Gym'), 40.00, 'Monthly Gym Membership', '2024-01-07'),
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Gym'), 40.00, 'Monthly Gym Membership', '2024-02-07'),
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Gym'), 45.00, 'Monthly Gym Membership', '2025-01-07'),
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Gym'), 50.00, 'Monthly Gym Membership', '2025-02-07'),

    -- Medical (Occasional) for 2024 and 2025
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Medical'), 300.00, 'Doctor Visit', '2024-02-20'),
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Medical'), 100.00, 'Pharmacy', '2024-03-05'),
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Medical'), 350.00, 'Surgery Consultation', '2025-01-25'),
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Medical'), 120.00, 'Pharmacy', '2025-02-15'),

    -- Entertainment (Weekends) for 2024 and 2025
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Entertainment'), 150.00, 'Movie Tickets', '2024-01-10'),
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Entertainment'), 200.00, 'Concert Ticket', '2024-02-18'),
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Entertainment'), 90.00, 'Streaming Services', '2025-01-05'),
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Entertainment'), 120.00, 'Video Games', '2025-02-10'),

    -- Extra Data for Current Date
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Food'), 55.00, 'Current Day Grocery Shopping', CURRENT_DATE),
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Transportation'), 20.00, 'Current Day Taxi Ride', CURRENT_DATE),
    (1, (SELECT id FROM categories WHERE user_id = 1 AND category_name = 'Medical'), 50.00, 'Current Day Pharmacy', CURRENT_DATE);
