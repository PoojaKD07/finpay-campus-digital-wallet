"""Design-level payment workflow from FinPay Lab 4.

This is intentionally a template, not a drop-in implementation. Reuse the
verified Lab 3 JWT identity. Resolve WalletID on the server, never from the
request body. Complete open assumption AS5 before deciding cashback credit
and TOPUP balance behaviour. Adapt locking to the chosen database engine.
"""

def process_payment(authenticated_student_id, merchant_id, amount_paise, idempotency_key):
    wallet = load_wallet_for_student(authenticated_student_id)
    if wallet is None:
        raise ValueError("Wallet not found")

    with database_transaction():
        # Idempotency is scoped to this wallet.
        previous = find_transaction(wallet["WalletID"], idempotency_key)
        if previous is not None:
            return previous

        merchant = load_merchant_and_cashback_rule(merchant_id)
        tier = load_wallet_tier(wallet["Tier"])

        if amount_paise <= 0:
            raise ValueError("Amount must be positive")
        if wallet["BalancePaise"] < amount_paise:
            raise ValueError("Insufficient balance")

        raw = calculate_cashback(amount_paise, merchant["Category"], wallet["Tier"])
        earned = sum_monthly_cashback(
            wallet["WalletID"], merchant["Category"], current_calendar_month()
        )
        cap = calculate_monthly_cap(
            merchant["BaseMonthlyCapPaise"], tier["CapMultX10"]
        )
        awarded = min(raw, max(0, cap - earned))

        # Insert payment history and update wallet in the same transaction.
        insert_payment_transaction(
            wallet_id=wallet["WalletID"],
            merchant_id=merchant_id,
            idempotency_key=idempotency_key,
            amount_paise=amount_paise,
            cashback_paise=awarded,
        )

        # Implement only after AS5 defines cashback-credit and TOPUP behaviour.
        update_wallet_balance_according_to_approved_policy(
            wallet["WalletID"], amount_paise, awarded
        )
        return {"cashback_awarded_paise": awarded}
