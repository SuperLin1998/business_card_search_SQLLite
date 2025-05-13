import psycopg2

try:
    conn = psycopg2.connect(
        host="34.169.83.246",   # 改成你的 Cloud SQL 公網 IP
        database="business-card-search20250430",
        user="postgres",
        password="20250430businesscard",
        port=5432
    )
    print("✅ 成功連線到 PostgreSQL")
    conn.close()
except Exception as e:
    print("❌ 無法連線：", e)
