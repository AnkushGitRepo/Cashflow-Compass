-- Insert categories for user_id = 2
INSERT INTO categories (user_id, category_name, is_predefined) VALUES
    (2, 'Rent', FALSE),
    (2, 'Food', FALSE),
    (2, 'Utilities', FALSE),
    (2, 'Transportation', FALSE),
    (2, 'Gym', FALSE),
    (2, 'Medical', FALSE),
    (2, 'Entertainment', FALSE),
    (2, 'Shopping', FALSE),
    (2, 'Subscriptions', FALSE)
ON CONFLICT (user_id, category_name) DO NOTHING;

-- Insert expenses for user_id = 2
INSERT INTO expenses (user_id, category_id, amount, description, date) VALUES
    -- Rent (Monthly) for 2023, 2024, 2025
    (2, (SELECT id FROM categories WHERE user_id = 2 AND category_name = 'Rent'), 1300.00, 'Apartment Rent', '2023-01-01'),
    (2, (SELECT id FROM categories WHERE user_id = 2 AND category_name = 'Rent'), 1350.00, 'Apartment Rent', '2024-01-01'),
    (2, (SELECT id FROM categories WHERE user_id = 2 AND category_name = 'Rent'), 1400.00, 'Apartment Rent', '2025-01-01'),

    -- Food (Weekly Groceries & Dining) for 2023, 2024, 2025
    (2, (SELECT id FROM categories WHERE user_id = 2 AND category_name = 'Food'), 80.00, 'Grocery Shopping', '2023-01-07'),
    (2, (SELECT id FROM categories WHERE user_id = 2 AND category_name = 'Food'), 85.00, 'Grocery Shopping', '2024-01-07'),
    (2, (SELECT id FROM categories WHERE user_id = 2 AND category_name = 'Food'), 90.00, 'Grocery Shopping', '2025-01-07'),
    (2, (SELECT id FROM categories WHERE user_id = 2 AND category_name = 'Food'), 50.00, 'Fast Food', '2023-02-10'),
    (2, (SELECT id FROM categories WHERE user_id = 2 AND category_name = 'Food'), 60.00, 'Fast Food', '2024-02-10'),
    (2, (SELECT id FROM categories WHERE user_id = 2 AND category_name = 'Food'), 70.00, 'Fast Food', '2025-02-10'),

    -- Utilities (Electricity, Water, Internet Bills) for 2023, 2024, 2025
    (2, (SELECT id FROM categories WHERE user_id = 2 AND category_name = 'Utilities'), 100.00, 'Electricity Bill', '2023-02-15'),
    (2, (SELECT id FROM categories WHERE user_id = 2 AND category_name = 'Utilities'), 105.00, 'Electricity Bill', '2024-02-15'),
    (2, (SELECT id FROM categories WHERE user_id = 2 AND category_name = 'Utilities'), 110.00, 'Electricity Bill', '2025-02-15'),
    (2, (SELECT id FROM categories WHERE user_id = 2 AND category_name = 'Utilities'), 50.00, 'Water Bill', '2023-03-15'),
    (2, (SELECT id FROM categories WHERE user_id = 2 AND category_name = 'Utilities'), 55.00, 'Water Bill', '2024-03-15'),
    (2, (SELECT id FROM categories WHERE user_id = 2 AND category_name = 'Utilities'), 60.00, 'Water Bill', '2025-03-15'),

    -- Transportation (Public Transport, Fuel) for 2023, 2024, 2025
    (2, (SELECT id FROM categories WHERE user_id = 2 AND category_name = 'Transportation'), 25.00, 'Bus Pass', '2023-01-10'),
    (2, (SELECT id FROM categories WHERE user_id = 2 AND category_name = 'Transportation'), 30.00, 'Gas Refill', '2024-01-10'),
    (2, (SELECT id FROM categories WHERE user_id = 2 AND category_name = 'Transportation'), 35.00, 'Uber Ride', '2025-01-10'),

    -- Gym (Monthly Subscription) for 2023, 2024, 2025
    (2, (SELECT id FROM categories WHERE user_id = 2 AND category_name = 'Gym'), 45.00, 'Gym Membership', '2023-02-05'),
    (2, (SELECT id FROM categories WHERE user_id = 2 AND category_name = 'Gym'), 50.00, 'Gym Membership', '2024-02-05'),
    (2, (SELECT id FROM categories WHERE user_id = 2 AND category_name = 'Gym'), 55.00, 'Gym Membership', '2025-02-05'),

    -- Medical (Doctor, Pharmacy) for 2023, 2024, 2025
    (2, (SELECT id FROM categories WHERE user_id = 2 AND category_name = 'Medical'), 250.00, 'Doctor Visit', '2023-04-10'),
    (2, (SELECT id FROM categories WHERE user_id = 2 AND category_name = 'Medical'), 275.00, 'Pharmacy', '2024-04-10'),
    (2, (SELECT id FROM categories WHERE user_id = 2 AND category_name = 'Medical'), 300.00, 'Annual Checkup', '2025-04-10'),

    -- Entertainment (Movies, Events) for 2023, 2024, 2025
    (2, (SELECT id FROM categories WHERE user_id = 2 AND category_name = 'Entertainment'), 100.00, 'Concert Ticket', '2023-05-15'),
    (2, (SELECT id FROM categories WHERE user_id = 2 AND category_name = 'Entertainment'), 120.00, 'Streaming Services', '2024-05-15'),
    (2, (SELECT id FROM categories WHERE user_id = 2 AND category_name = 'Entertainment'), 140.00, 'Movie Night', '2025-05-15'),

    -- Shopping & Subscriptions for 2023, 2024, 2025
    (2, (SELECT id FROM categories WHERE user_id = 2 AND category_name = 'Shopping'), 250.00, 'Clothing Purchase', '2023-06-05'),
    (2, (SELECT id FROM categories WHERE user_id = 2 AND category_name = 'Shopping'), 300.00, 'Electronics', '2024-06-05'),
    (2, (SELECT id FROM categories WHERE user_id = 2 AND category_name = 'Shopping'), 350.00, 'Furniture', '2025-06-05'),

    -- Extra Data for Current Date
    (2, (SELECT id FROM categories WHERE user_id = 2 AND category_name = 'Food'), 55.00, 'Current Day Grocery Shopping', CURRENT_DATE),
    (2, (SELECT id FROM categories WHERE user_id = 2 AND category_name = 'Transportation'), 20.00, 'Current Day Uber Ride', CURRENT_DATE),
    (2, (SELECT id FROM categories WHERE user_id = 2 AND category_name = 'Medical'), 100.00, 'Current Day Pharmacy', CURRENT_DATE);
