-- Derive monthly cashback; do not store a separate monthly counter.
-- Bind wallet_id, category, month_start and next_month_start.
SELECT COALESCE(SUM(pt.CashbackPaise), 0) AS EarnedPaise
FROM payment_transaction AS pt
JOIN merchant AS m ON m.MerchantID = pt.MerchantID
WHERE pt.WalletID = :wallet_id
  AND m.Category = :category
  AND pt.CreatedAt >= :month_start
  AND pt.CreatedAt < :next_month_start;
