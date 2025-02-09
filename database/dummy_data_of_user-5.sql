-- Insert categories for user_id = 5
INSERT INTO categories (user_id, category_name, is_predefined) VALUES
    (5, 'Rent', FALSE),
    (5, 'Food', FALSE),
    (5, 'Utilities', FALSE),
    (5, 'Transportation', FALSE),
    (5, 'Gym', FALSE),
    (5, 'Medical', FALSE),
    (5, 'Entertainment', FALSE),
    (5, 'Travel', FALSE),
    (5, 'Shopping', FALSE),
    (5, 'Subscriptions', FALSE)
ON CONFLICT (user_id, category_name) DO NOTHING;

-- Insert expenses for user_id = 5
INSERT INTO expenses (user_id, category_id, amount, description, date) VALUES
    -- Rent (Monthly)
    (5, (SELECT id FROM categories WHERE user_id = 5 AND category_name = 'Rent'), 1550.00, 'Monthly Rent', '2023-01-01'),
    (5, (SELECT id FROM categories WHERE user_id = 5 AND category_name = 'Rent'), 1600.00, 'Monthly Rent', '2023-02-01'),
    (5, (SELECT id FROM categories WHERE user_id = 5 AND category_name = 'Rent'), 1650.00, 'Monthly Rent', '2024-01-01'),
    (5, (SELECT id FROM categories WHERE user_id = 5 AND category_name = 'Rent'), 1700.00, 'Monthly Rent', '2024-02-01'),
    (5, (SELECT id FROM categories WHERE user_id = 5 AND category_name = 'Rent'), 1750.00, 'Monthly Rent', '2025-01-01'),
    (5, (SELECT id FROM categories WHERE user_id = 5 AND category_name = 'Rent'), 1800.00, 'Monthly Rent', '2025-02-01'),

    -- Food (Weekly)
    (5, (SELECT id FROM categories WHERE user_id = 5 AND category_name = 'Food'), 70.00, 'Grocery Shopping', '2023-01-05'),
    (5, (SELECT id FROM categories WHERE user_id = 5 AND category_name = 'Food'), 80.00, 'Supermarket Visit', '2023-02-12'),
    (5, (SELECT id FROM categories WHERE user_id = 5 AND category_name = 'Food'), 90.00, 'Restaurant Bill', '2024-01-18'),
    (5, (SELECT id FROM categories WHERE user_id = 5 AND category_name = 'Food'), 95.00, 'Weekend Dining', '2024-02-22'),
    (5, (SELECT id FROM categories WHERE user_id = 5 AND category_name = 'Food'), 100.00, 'Fast Food', '2025-01-10'),
    (5, (SELECT id FROM categories WHERE user_id = 5 AND category_name = 'Food'), 110.00, 'Dinner Out', '2025-02-15'),

    -- Utilities (Monthly)
    (5, (SELECT id FROM categories WHERE user_id = 5 AND category_name = 'Utilities'), 115.00, 'Electricity Bill', '2023-01-15'),
    (5, (SELECT id FROM categories WHERE user_id = 5 AND category_name = 'Utilities'), 125.00, 'Water Bill', '2023-02-15'),
    (5, (SELECT id FROM categories WHERE user_id = 5 AND category_name = 'Utilities'), 135.00, 'Internet Bill', '2024-01-15'),
    (5, (SELECT id FROM categories WHERE user_id = 5 AND category_name = 'Utilities'), 145.00, 'Gas Bill', '2024-02-15'),
    (5, (SELECT id FROM categories WHERE user_id = 5 AND category_name = 'Utilities'), 155.00, 'Electricity Bill', '2025-01-15'),
    (5, (SELECT id FROM categories WHERE user_id = 5 AND category_name = 'Utilities'), 165.00, 'Water Bill', '2025-02-15'),

    -- Travel (Trips & Transportation)
    (5, (SELECT id FROM categories WHERE user_id = 5 AND category_name = 'Travel'), 300.00, 'Weekend Getaway', '2023-03-05'),
    (5, (SELECT id FROM categories WHERE user_id = 5 AND category_name = 'Travel'), 450.00, 'Flight Ticket', '2024-05-10'),
    (5, (SELECT id FROM categories WHERE user_id = 5 AND category_name = 'Travel'), 700.00, 'International Trip', '2025-07-15'),

    -- Shopping (Occasional)
    (5, (SELECT id FROM categories WHERE user_id = 5 AND category_name = 'Shopping'), 120.00, 'Clothing Purchase', '2023-06-15'),
    (5, (SELECT id FROM categories WHERE user_id = 5 AND category_name = 'Shopping'), 250.00, 'Electronics', '2024-09-10'),
    (5, (SELECT id FROM categories WHERE user_id = 5 AND category_name = 'Shopping'), 90.00, 'Home Decor', '2025-11-20'),

    -- Medical (Occasional)
    (5, (SELECT id FROM categories WHERE user_id = 5 AND category_name = 'Medical'), 200.00, 'Doctor Visit', '2023-03-15'),
    (5, (SELECT id FROM categories WHERE user_id = 5 AND category_name = 'Medical'), 150.00, 'Pharmacy', '2024-04-22'),
    (5, (SELECT id FROM categories WHERE user_id = 5 AND category_name = 'Medical'), 180.00, 'Surgery Consultation', '2025-08-10'),

    -- Subscriptions (Monthly)
    (5, (SELECT id FROM categories WHERE user_id = 5 AND category_name = 'Subscriptions'), 15.00, 'Netflix Subscription', '2023-01-10'),
    (5, (SELECT id FROM categories WHERE user_id = 5 AND category_name = 'Subscriptions'), 20.00, 'Spotify Subscription', '2024-02-15'),
    (5, (SELECT id FROM categories WHERE user_id = 5 AND category_name = 'Subscriptions'), 25.00, 'Amazon Prime', '2025-03-01'),

    -- Extra Data for Current Date
    (5, (SELECT id FROM categories WHERE user_id = 5 AND category_name = 'Food'), 85.00, 'Current Day Grocery Shopping', CURRENT_DATE),
    (5, (SELECT id FROM categories WHERE user_id = 5 AND category_name = 'Travel'), 60.00, 'Current Day Taxi Ride', CURRENT_DATE),
    (5, (SELECT id FROM categories WHERE user_id = 5 AND category_name = 'Medical'), 45.00, 'Current Day Pharmacy', CURRENT_DATE),
    (5, (SELECT id FROM categories WHERE user_id = 5 AND category_name = 'Subscriptions'), 30.00, 'Current Day Subscription Renewal', CURRENT_DATE);
