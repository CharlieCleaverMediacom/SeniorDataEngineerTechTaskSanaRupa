1. Find the top 5 users with the highest number of posts.
Ans: [(1, 'Bret', 10), (2, 'Antonette', 10), (3, 'Samantha', 10), (4, 'Karianne', 10), (5, 'Kamren', 10)]
Query Used:
SELECT userId, username, COUNT(*) AS post_count
FROM srk_enriched_post_df
GROUP BY userId, username
ORDER BY post_count DESC
LIMIT 5;

2. For each of these top 5 users, calculate the average post length.
Ans: [(1, 'Bret', 164.5), (2, 'Antonette', 162.9), (3, 'Samantha', 153.8), (4, 'Karianne', 182.3), (5, 'Kamren', 162.5)]
Query Used:
SELECT userId, username, avg(length(body)) AS average_post_length
FROM srk_enriched_posts
WHERE userId IN (select userId from (SELECT userId,username,count(*) AS post_count
    FROM srk_enriched_posts
    GROUP BY userId,username
    ORDER BY count(*) DESC LIMIT 5) temp)
GROUP BY userId, username;

3. Identify the day of the week when the most `lengthy` posts are created (assume all posts were created in the UTC timezone).
Ans: As there is no created date in posts table not possible to identify the day of week when most of lengthy posts were created.