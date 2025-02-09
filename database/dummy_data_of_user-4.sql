-- Insert categories for user_id = 4
INSERT INTO categories (user_id, category_name, is_predefined) VALUES
    (4, 'Rent', FALSE),
    (4, 'Food', FALSE),
    (4, 'Utilities', FALSE),
    (4, 'Transportation', FALSE),
    (4, 'Gym', FALSE),
    (4, 'Medical', FALSE),
    (4, 'Entertainment', FALSE)
ON CONFLICT (user_id, category_name) DO NOTHING;

-- Insert expenses for user_id = 4
INSERT INTO expenses (user_id, category_id, amount, description, date) VALUES
    -- Rent (Monthly) for 2023, 2024, and 2025
    (4, (SELECT id FROM categories WHERE user_id = 4 AND category_name = 'Rent'), 1350.00, 'Monthly Rent', '2023-01-01'),
    (4, (SELECT id FROM categories WHERE user_id = 4 AND category_name = 'Rent'), 1400.00, 'Monthly Rent', '2024-01-01'),
    (4, (SELECT id FROM categories WHERE user_id = 4 AND category_name = 'Rent'), 1450.00, 'Monthly Rent', '2025-01-01'),
    
    -- Food (Weekly) for 2023, 2024, and 2025
    (4, (SELECT id FROM categories WHERE user_id = 4 AND category_name = 'Food'), 50.00, 'Grocery Shopping', '2023-01-05'),
    (4, (SELECT id FROM categories WHERE user_id = 4 AND category_name = 'Food'), 65.00, 'Supermarket Visit', '2024-02-10'),
    (4, (SELECT id FROM categories WHERE user_id = 4 AND category_name = 'Food'), 75.00, 'Restaurant Bill', '2025-01-15'),

    -- Utilities (Monthly) for 2023, 2024, and 2025
    (4, (SELECT id FROM categories WHERE user_id = 4 AND category_name = 'Utilities'), 95.00, 'Electricity Bill', '2023-01-15'),
    (4, (SELECT id FROM categories WHERE user_id = 4 AND category_name = 'Utilities'), 110.00, 'Water Bill', '2024-02-15'),
    (4, (SELECT id FROM categories WHERE user_id = 4 AND category_name = 'Utilities'), 120.00, 'Gas Bill', '2025-01-15'),

    -- Transportation (Daily) for 2023, 2024, and 2025
    (4, (SELECT id FROM categories WHERE user_id = 4 AND category_name = 'Transportation'), 15.00, 'Uber Ride', '2023-01-03'),
    (4, (SELECT id FROM categories WHERE user_id = 4 AND category_name = 'Transportation'), 30.00, 'Gas Refill', '2024-02-10'),
    (4, (SELECT id FROM categories WHERE user_id = 4 AND category_name = 'Transportation'), 40.00, 'Taxi Ride', '2025-01-12'),

    -- Gym (Subscription) for 2023, 2024, and 2025
    (4, (SELECT id FROM categories WHERE user_id = 4 AND category_name = 'Gym'), 30.00, 'Monthly Gym Membership', '2023-01-07'),
    (4, (SELECT id FROM categories WHERE user_id = 4 AND category_name = 'Gym'), 35.00, 'Monthly Gym Membership', '2024-01-07'),
    (4, (SELECT id FROM categories WHERE user_id = 4 AND category_name = 'Gym'), 40.00, 'Monthly Gym Membership', '2025-01-07'),

    -- Medical (Occasional) for 2023, 2024, and 2025
    (4, (SELECT id FROM categories WHERE user_id = 4 AND category_name = 'Medical'), 150.00, 'Doctor Visit', '2023-02-20'),
    (4, (SELECT id FROM categories WHERE user_id = 4 AND category_name = 'Medical'), 200.00, 'Pharmacy', '2024-03-05'),
    (4, (SELECT id FROM categories WHERE user_id = 4 AND category_name = 'Medical'), 250.00, 'Dental Checkup', '2025-01-25'),

    -- Entertainment (Weekends) for 2023, 2024, and 2025
    (4, (SELECT id FROM categories WHERE user_id = 4 AND category_name = 'Entertainment'), 120.00, 'Movie Tickets', '2023-02-10'),
    (4, (SELECT id FROM categories WHERE user_id = 4 AND category_name = 'Entertainment'), 150.00, 'Concert Ticket', '2024-02-18'),
    (4, (SELECT id FROM categories WHERE user_id = 4 AND category_name = 'Entertainment'), 80.00, 'Streaming Services', '2025-01-05'),

    -- Extra Data for Current Date
    (4, (SELECT id FROM categories WHERE user_id = 4 AND category_name = 'Food'), 55.00, 'Current Day Grocery Shopping', CURRENT_DATE),
    (4, (SELECT id FROM categories WHERE user_id = 4 AND category_name = 'Transportation'), 20.00, 'Current Day Taxi Ride', CURRENT_DATE),
    (4, (SELECT id FROM categories WHERE user_id = 4 AND category_name = 'Medical'), 50.00, 'Current Day Pharmacy', CURRENT_DATE);
