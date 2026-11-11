FinPay – Campus Digital Wallet and Cashback System

Project Overview

FinPay is a campus digital wallet and cashback system designed to manage student wallets, merchant payments, and tier-based cashback rewards.

The system uses a layered architecture and reuses the existing JWT authentication infrastructure.

Key Features

- Student wallet management
- Wallet balance tracking
- Merchant and category management
- BASIC, PRIME and PREMIUM membership tiers
- Category-based cashback calculation
- Monthly cashback limits
- Payment transaction management
- Duplicate payment protection using idempotency keys
- Secure wallet access using JWT authentication

Technology and Design

- Backend: Python
- Database: Relational Database (RDBMS)
- Authentication: Existing JWT infrastructure
- Database Design: Entity Relationship Modelling and 3NF
- Query Design: SQL
- Architecture: Layered Architecture

Cashback Categories

Category| BASIC Cashback Rate
CANTEEN| 2%
STATIONERY| 1%
TRANSPORT| 3%
HOSTEL| 0.5%
ONLINE| 1%
TOPUP| 0%

Wallet Tiers

Tier| Cashback Multiplier| Cap Multiplier
BASIC| 1.0x| 1.0x
PRIME| 1.5x| 1.5x
PREMIUM| 2.0x| 2.0x

Database Design

The normalized database consists of six main entities:

1. STUDENT
2. WALLET
3. WALLET_TIER
4. MERCHANT
5. CASHBACK_RULE
6. TRANSACTION

The database uses primary keys, foreign keys, unique constraints and check constraints to maintain data integrity.

Cashback Calculation

Cashback is calculated using integer paise and basis-point rates.

The calculation applies a single floor operation to avoid floating-point precision errors.

Monthly cashback is derived from transaction history using SQL aggregation and is restricted by the applicable wallet tier's monthly cap.

Security Design

- Reuse of existing JWT authentication.
- Student-specific wallet authorization.
- Wallet identity resolved on the server.
- Unique wallet-scoped idempotency keys.
- Atomic payment and wallet updates.
- Database constraints for transaction integrity.

Repository Structure

finpay-campus-digital-wallet/
│
├── src/
├── database/
├── tests/
├── docs/
├── README.md
└── requirements.txt

Adjust this structure to match the actual implementation before publishing.

Future Enhancements

- Payment history dashboard
- Wallet transaction reports
- Merchant analytics
- Cashback notifications
- Improved administrative dashboard
- Deployment and production configuration

Project Note

This repository documents the FinPay design and implementation components. Features should be marked as implemented only after integration and successful testing.

License

No license has been assigned yet. Open-source distribution requires approval from the project owners.
