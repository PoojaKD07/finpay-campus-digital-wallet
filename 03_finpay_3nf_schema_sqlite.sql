PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS student (
    StudentID INTEGER PRIMARY KEY,
    StudentName TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS wallet_tier (
    Tier TEXT PRIMARY KEY CHECK (Tier IN ('BASIC','PRIME','PREMIUM')),
    RateMultX10 INTEGER NOT NULL CHECK (RateMultX10 > 0),
    CapMultX10 INTEGER NOT NULL CHECK (CapMultX10 > 0)
);

CREATE TABLE IF NOT EXISTS cashback_rule (
    Category TEXT PRIMARY KEY CHECK (Category IN
      ('CANTEEN','STATIONERY','TRANSPORT','HOSTEL','ONLINE','TOPUP')),
    BaseRateBps INTEGER NOT NULL CHECK (BaseRateBps >= 0),
    BaseMonthlyCapPaise INTEGER NOT NULL CHECK (BaseMonthlyCapPaise >= 0)
);

CREATE TABLE IF NOT EXISTS merchant (
    MerchantID INTEGER PRIMARY KEY,
    MerchantName TEXT NOT NULL,
    Category TEXT NOT NULL REFERENCES cashback_rule(Category)
);

CREATE TABLE IF NOT EXISTS wallet (
    WalletID INTEGER PRIMARY KEY,
    StudentID INTEGER NOT NULL UNIQUE REFERENCES student(StudentID),
    Tier TEXT NOT NULL REFERENCES wallet_tier(Tier),
    BalancePaise INTEGER NOT NULL CHECK (BalancePaise >= 0)
);

-- Use a non-reserved physical name for TRANSACTION.
CREATE TABLE IF NOT EXISTS payment_transaction (
    TransactionID INTEGER PRIMARY KEY,
    WalletID INTEGER NOT NULL REFERENCES wallet(WalletID),
    MerchantID INTEGER NOT NULL REFERENCES merchant(MerchantID),
    IdempotencyKey TEXT NOT NULL,
    AmountPaise INTEGER NOT NULL CHECK (AmountPaise > 0),
    CashbackPaise INTEGER NOT NULL CHECK (CashbackPaise >= 0),
    CreatedAt TEXT NOT NULL,
    UNIQUE (WalletID, IdempotencyKey)
);

CREATE INDEX IF NOT EXISTS idx_payment_wallet_created
ON payment_transaction(WalletID, CreatedAt);

INSERT OR IGNORE INTO wallet_tier VALUES
('BASIC',10,10), ('PRIME',15,15), ('PREMIUM',20,20);

INSERT OR IGNORE INTO cashback_rule VALUES
('CANTEEN',200,5000),
('STATIONERY',100,2000),
('TRANSPORT',300,10000),
('HOSTEL',50,20000),
('ONLINE',100,3000),
('TOPUP',0,0);
