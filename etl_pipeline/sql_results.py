import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('etl_challenge.db')
cursor = conn.cursor()

# Execute the queries
top_users_query = """
SELECT userId,username,COUNT(*) AS post_count
    FROM srk_enriched_posts
    GROUP BY userId,username
    ORDER BY post_count DESC
    LIMIT 5
"""
cursor.execute(top_users_query)
top_users = cursor.fetchall()

average_length_query = """
SELECT userId, username, avg(length(body)) AS average_post_length
FROM srk_enriched_posts
WHERE userId IN (select userId from (SELECT userId,username,count(*) AS post_count
    FROM srk_enriched_posts
    GROUP BY userId,username
    ORDER BY count(*) DESC LIMIT 5) temp)
GROUP BY userId, username;
"""
cursor.execute(average_length_query)
average_lengths = cursor.fetchall()

# Output results
print("Top 5 Users with Highest Number of Posts:", top_users)
print("Average Post Length for Top Users:", average_lengths)

# Close the connection
conn.close()
