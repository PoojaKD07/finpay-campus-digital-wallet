FinPay – Campus Digital Wallet & Cashback Management System

A Database-Driven Digital Wallet System with Tier-Based Cashback, Transaction Management, and Monthly Cashback Limits

---

1. Project Overview

FinPay is a campus-focused digital wallet and cashback management system designed to simplify cashless transactions between students and campus merchants.

The system provides a structured approach to wallet management, payment processing, merchant categorization, and cashback calculation. It incorporates tier-based cashback benefits and monthly cashback limits to support controlled and transparent reward distribution.

The project focuses on relational database design, data integrity, transaction consistency, and the implementation of business rules through a structured data model.

2. Key Objectives

- Design a normalized relational database for a campus digital wallet ecosystem.
- Manage student wallet accounts and wallet tiers.
- Support merchant-based transaction categorization.
- Calculate cashback using category-specific rates.
- Apply tier-based cashback multipliers.
- Enforce monthly cashback limits.
- Maintain transaction history for accurate cashback calculations.
- Prevent duplicate transaction processing through idempotency.
- Ensure consistency between payment processing and wallet updates.

3. System Architecture

FinPay follows a layered system-design approach that separates client interaction, business logic, and data persistence.

              STUDENT / MERCHANT
                      |
                      v
               APPLICATION LAYER
                      |
                      v
              AUTHENTICATION LAYER
                      |
                      v
                BUSINESS LOGIC
             /        |         \
            /         |          \
       Payment     Cashback     Wallet
      Processing   Calculation  Management
            \         |          /
             \        |         /
                      v
                DATABASE LAYER
                      |
                      v
              RELATIONAL DATABASE

Core processing flow:

1. A student initiates a payment.
2. The application validates the transaction request.
3. The system identifies the associated wallet and merchant category.
4. Cashback eligibility is evaluated.
5. The applicable tier multiplier and monthly limit are considered.
6. The transaction and associated wallet operations are designed to execute consistently.
7. The transaction is recorded for future reference and cashback calculations.

Note: This diagram represents the proposed system architecture. It should not be interpreted as proof that every layer has been fully integrated.

4. Core Modules

4.1 Student Management

Maintains student-related information and establishes the relationship between students and their wallets.

4.2 Wallet Management

Handles wallet account information and provides the foundation for wallet-related operations.

4.3 Merchant Management

Maintains merchant information and associates merchants with transaction categories.

4.4 Transaction Management

Maintains payment transaction records and supports transaction-history-based calculations.

4.5 Cashback Calculation

Calculates cashback based on:

- Transaction amount
- Merchant transaction category
- Applicable cashback percentage
- Student wallet tier
- Remaining monthly cashback eligibility

4.6 Wallet Tier Management

Supports three cashback benefit levels:

Tier| Cashback Multiplier| Monthly Cap Multiplier
BASIC| 1.0×| 1.0×
PRIME| 1.5×| 1.5×
PREMIUM| 2.0×| 2.0×

The tier multipliers are applied to the corresponding base cashback rules.

5. Cashback Business Rules

FinPay uses category-specific cashback rates and maximum cashback limits.

5.1 Base Cashback Configuration

Transaction Category| Cashback Rate| Maximum Cashback
CANTEEN| 2%| ₹50
STATIONERY| 1%| ₹20
TRANSPORT| 3%| ₹100
HOSTEL| 0.5%| ₹200
ONLINE| 1%| ₹30
TOPUP| 0%| ₹0

5.2 Cashback Calculation

The base cashback is determined using the transaction amount and the applicable category rate.

Base Cashback = Transaction Amount × Cashback Rate

The tier multiplier is then applied, followed by the applicable cashback limit.

Adjusted Cashback = Base Cashback × Tier Multiplier

Final Cashback = MIN(
    Adjusted Cashback,
    Tier-Adjusted Category Cap,
    Remaining Monthly Cashback Limit
)

The exact calculation must use the same monetary precision and rounding rules throughout the system.

5.3 Monetary Precision

All monetary values should be represented as integer paise rather than floating-point rupee values.

For example:

₹100.50 = 10050 paise

This avoids floating-point precision problems in financial calculations.

The calculation should use integer arithmetic and apply flooring only at the final cashback calculation stage.

5.4 Monthly Cashback Limit

Monthly cashback eligibility is calculated from transaction history.

The monthly cashback total is derived using an aggregate "SUM" operation rather than maintaining an independent monthly cashback counter.

This approach helps avoid inconsistencies between transaction records and separately maintained totals.

6. Database Design

The database design consists of six primary entities.

Entity| Responsibility
STUDENT| Stores student information
WALLET| Maintains student wallet information
WALLET_TIER| Defines cashback benefit tiers
MERCHANT| Stores merchant information and categories
CASHBACK_RULE| Defines category-based cashback rules
TRANSACTION| Maintains payment transaction records

Entity Relationships

STUDENT
   |
   | 1 : 1 (as designed)
   |
 WALLET
   |
   | N : 1
   |
WALLET_TIER

MERCHANT
   |
   | 1 : N
   |
TRANSACTION
   |
   | N : 1
   |
 WALLET

CASHBACK_RULE
   |
   | Category-based rule association
   |
TRANSACTION

The relationship diagram is a conceptual representation. Final cardinalities and foreign-key constraints should match the implemented schema.

Database Design Principles

- Use primary keys to uniquely identify records.
- Use foreign keys to maintain referential integrity.
- Apply appropriate "NOT NULL", "UNIQUE", and "CHECK" constraints.
- Avoid unnecessary duplicate storage.
- Maintain transaction history for auditability.
- Follow Third Normal Form (3NF) principles in the relational design.

7. Data Integrity and Transaction Consistency

Financial transactions require strong consistency guarantees.

FinPay incorporates the following design considerations:

Idempotency

A unique constraint on the wallet and idempotency key prevents duplicate processing of the same payment request.

UNIQUE (WalletID, IdempotencyKey)

Atomic Payment Processing

Payment processing and related wallet updates should be performed within a single database transaction.

If an operation fails, the transaction should be rolled back to prevent partially applied updates.

Server-Side Wallet Identification

Wallet identity should be resolved and validated by the application server rather than trusted directly from an unverified client request.

Transaction History

Transaction records provide the basis for calculating monthly cashback totals and reviewing payment activity.

8. Repository Structure

The accompanying code-snippet collection is organized by functionality:

FinPay/
│
├── 01_calculate_cashback.py
├── 02_monthly_cap.py
├── 03_finpay_3nf_schema_sqlite.sql
├── 04_monthly_cashback_sum.sql
├── 05_payment_processing_design.py
├── 06_cashback_expected_results.py
├── 07_finpay_constants.py
│
└── README.md

File| Purpose
"01_calculate_cashback.py"| Cashback calculation logic
"02_monthly_cap.py"| Monthly cashback limit handling
"03_finpay_3nf_schema_sqlite.sql"| Relational database schema example
"04_monthly_cashback_sum.sql"| Monthly cashback aggregation query
"05_payment_processing_design.py"| Payment-processing design example
"06_cashback_expected_results.py"| Expected cashback calculation examples
"07_finpay_constants.py"| Cashback categories, rates, and tier constants

Repository scope: These files are reference code snippets illustrating selected FinPay design concepts. They do not, by themselves, constitute a complete deployable wallet application.


9. Validation and Testing Considerations

The following cases should be considered when validating the cashback and payment logic.

Test Scenario| Expected Behavior
Valid eligible transaction| Cashback calculated using applicable rules
TOPUP transaction| No cashback
BASIC tier transaction| Base cashback multiplier applied
PRIME tier transaction| 1.5× multiplier applied
PREMIUM tier transaction| 2.0× multiplier applied
Cashback exceeds category cap| Category cap enforced
Monthly cashback limit reached| No additional monthly cashback
Duplicate idempotency key| Duplicate processing prevented
Invalid wallet reference| Transaction rejected
Payment operation failure| Database transaction rolled back

These are validation scenarios, not claims that every test has already been executed.

10. Design Decisions and Engineering Considerations

Design Decision| Engineering Benefit
Integer paise representation| Avoids floating-point monetary inaccuracies
Normalized relational schema| Reduces unnecessary data duplication
Transaction-history aggregation| Keeps monthly cashback derived from recorded transactions
Idempotency constraint| Helps prevent duplicate payment processing
Atomic database operations| Maintains consistency during failures
Tier-based cashback rules| Supports configurable reward levels
Category-specific cashback caps| Controls cashback eligibility

11. Conclusion

FinPay demonstrates the design of a campus-oriented digital wallet and cashback management system with emphasis on database structure, financial calculation accuracy, transaction integrity, and configurable reward rules.

Its design combines normalized relational data modeling with tier-based cashback computation and monthly eligibility controls, providing a foundation for developing a more comprehensive campus payment platform.

