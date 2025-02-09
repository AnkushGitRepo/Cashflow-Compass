-- Insert categories for user_id = 3
INSERT INTO categories (user_id, category_name, is_predefined) VALUES
    (3, 'Rent', FALSE),
    (3, 'Food', FALSE),
    (3, 'Utilities', FALSE),
    (3, 'Transportation', FALSE),
    (3, 'Gym', FALSE),
    (3, 'Medical', FALSE),
    (3, 'Entertainment', FALSE),
    (3, 'Shopping', FALSE),
    (3, 'Travel', FALSE)
ON CONFLICT (user_id, category_name) DO NOTHING;

-- Insert expenses for user_id = 3
INSERT INTO expenses (user_id, category_id, amount, description, date) VALUES
    -- Rent (Monthly) for 2023, 2024, and 2025
    (3, (SELECT id FROM categories WHERE user_id = 3 AND category_name = 'Rent'), 1250.00, 'Monthly Rent', '2023-01-01'),
    (3, (SELECT id FROM categories WHERE user_id = 3 AND category_name = 'Rent'), 1300.00, 'Monthly Rent', '2024-01-01'),
    (3, (SELECT id FROM categories WHERE user_id = 3 AND category_name = 'Rent'), 1350.00, 'Monthly Rent', '2025-01-01'),

    -- Food (Weekly & Daily)
    (3, (SELECT id FROM categories WHERE user_id = 3 AND category_name = 'Food'), 60.00, 'Groceries', '2023-02-05'),
    (3, (SELECT id FROM categories WHERE user_id = 3 AND category_name = 'Food'), 75.00, 'Restaurant', '2024-02-10'),
    (3, (SELECT id FROM categories WHERE user_id = 3 AND category_name = 'Food'), 50.00, 'Coffee & Snacks', '2025-02-15'),

    -- Utilities (Monthly)
    (3, (SELECT id FROM categories WHERE user_id = 3 AND category_name = 'Utilities'), 100.00, 'Electricity Bill', '2023-03-15'),
    (3, (SELECT id FROM categories WHERE user_id = 3 AND category_name = 'Utilities'), 110.00, 'Water Bill', '2024-03-15'),
    (3, (SELECT id FROM categories WHERE user_id = 3 AND category_name = 'Utilities'), 120.00, 'Gas Bill', '2025-03-15'),

    -- Transportation (Daily Commuting)
    (3, (SELECT id FROM categories WHERE user_id = 3 AND category_name = 'Transportation'), 20.00, 'Uber Ride', '2023-04-05'),
    (3, (SELECT id FROM categories WHERE user_id = 3 AND category_name = 'Transportation'), 30.00, 'Gas Refill', '2024-04-10'),
    (3, (SELECT id FROM categories WHERE user_id = 3 AND category_name = 'Transportation'), 25.00, 'Taxi Ride', '2025-04-20'),

    -- Gym (Subscription) for 2023, 2024, and 2025
    (3, (SELECT id FROM categories WHERE user_id = 3 AND category_name = 'Gym'), 40.00, 'Monthly Gym Membership', '2023-05-07'),
    (3, (SELECT id FROM categories WHERE user_id = 3 AND category_name = 'Gym'), 45.00, 'Monthly Gym Membership', '2024-05-07'),
    (3, (SELECT id FROM categories WHERE user_id = 3 AND category_name = 'Gym'), 50.00, 'Monthly Gym Membership', '2025-05-07'),

    -- Medical (Occasional) for 2023, 2024, and 2025
    (3, (SELECT id FROM categories WHERE user_id = 3 AND category_name = 'Medical'), 250.00, 'Doctor Visit', '2023-06-20'),
    (3, (SELECT id FROM categories WHERE user_id = 3 AND category_name = 'Medical'), 100.00, 'Pharmacy', '2024-06-05'),
    (3, (SELECT id FROM categories WHERE user_id = 3 AND category_name = 'Medical'), 350.00, 'Surgery Consultation', '2025-06-15'),

    -- Entertainment (Weekends) for 2023, 2024, and 2025
    (3, (SELECT id FROM categories WHERE user_id = 3 AND category_name = 'Entertainment'), 120.00, 'Concert Ticket', '2023-07-18'),
    (3, (SELECT id FROM categories WHERE user_id = 3 AND category_name = 'Entertainment'), 90.00, 'Streaming Services', '2024-07-05'),
    (3, (SELECT id FROM categories WHERE user_id = 3 AND category_name = 'Entertainment'), 100.00, 'Movie Tickets', '2025-07-10'),

    -- Shopping (Varied)
    (3, (SELECT id FROM categories WHERE user_id = 3 AND category_name = 'Shopping'), 200.00, 'Clothing', '2023-08-10'),
    (3, (SELECT id FROM categories WHERE user_id = 3 AND category_name = 'Shopping'), 150.00, 'Electronics', '2024-08-15'),
    (3, (SELECT id FROM categories WHERE user_id = 3 AND category_name = 'Shopping'), 250.00, 'Shoes', '2025-08-20'),

    -- Travel (Occasional)
    (3, (SELECT id FROM categories WHERE user_id = 3 AND category_name = 'Travel'), 500.00, 'Flight Ticket', '2023-09-25'),
    (3, (SELECT id FROM categories WHERE user_id = 3 AND category_name = 'Travel'), 300.00, 'Hotel Booking', '2024-09-10'),
    (3, (SELECT id FROM categories WHERE user_id = 3 AND category_name = 'Travel'), 450.00, 'Vacation Expenses', '2025-09-15'),

    -- Extra Data for Current Date
    (3, (SELECT id FROM categories WHERE user_id = 3 AND category_name = 'Food'), 70.00, 'Current Day Grocery Shopping', CURRENT_DATE),
    (3, (SELECT id FROM categories WHERE user_id = 3 AND category_name = 'Transportation'), 35.00, 'Current Day Taxi Ride', CURRENT_DATE),
    (3, (SELECT id FROM categories WHERE user_id = 3 AND category_name = 'Medical'), 75.00, 'Current Day Pharmacy', CURRENT_DATE),
    (3, (SELECT id FROM categories WHERE user_id = 3 AND category_name = 'Entertainment'), 50.00, 'Current Day Movie', CURRENT_DATE);
