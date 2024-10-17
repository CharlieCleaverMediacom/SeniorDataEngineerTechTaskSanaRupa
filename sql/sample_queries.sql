-- Write SQL queries to answer these questions using the data you have loaded into BigQuery:
-- 1. Find the top 5 users with the highest number of posts.

SELECT userId, username, COUNT(*) AS post_count
FROM srk_enriched_post_df
GROUP BY userId, username
ORDER BY post_count DESC
LIMIT 5;

--All 10 users have posted same no.of posts.
--Hence the result will vary based on the query.
--Above query gives the result of userId 1-5.
--Below query gives the result of userId 6-10.

SELECT userId
    FROM srk_enriched_posts
    GROUP BY userId
    ORDER BY COUNT(*) DESC
    LIMIT 5

-- 2. For each of these top 5 users, calculate the average post length.

--If we need to get the userId 1-5 and its average post length we can use the below query.

SELECT userId, username, avg(length(body)) AS average_post_length
FROM srk_enriched_posts
WHERE userId IN (select userId from (SELECT userId,username,count(*) AS post_count
    FROM srk_enriched_posts
    GROUP BY userId,username
    ORDER BY count(*) DESC LIMIT 5) temp)
GROUP BY userId, username;

-- By changing the sub-query we can get the userId 6-10

SELECT userId, username, avg(length(body)) AS average_post_length
FROM srk_enriched_posts
WHERE userId IN (SELECT userId
    FROM srk_enriched_posts
    GROUP BY userId
    ORDER BY COUNT(*) DESC
    LIMIT 5)
GROUP BY userId, username;

-- 3. Identify the day of the week when the most `lengthy` posts are created (assume all posts were created in the UTC timezone).

--As there is no created date in posts table not possible to identify the day of week when most of lengthy posts were created.