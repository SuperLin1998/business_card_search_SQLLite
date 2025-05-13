CREATE TABLE cards (
    id SERIAL PRIMARY KEY,
    filename VARCHAR(255),
    raw_text TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
