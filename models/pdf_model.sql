{{
  config(
    materialized='table'
  )
}}
 
select
    b.LEVEL,
    a.TITLE,
    b.YEAR,
    count(a.TOPIC_NAME) as Number_of_articles,
    MIN(LENGTH(b.SUMMARY)) AS "Min_Length_Summary",
    MAX(LENGTH(b.SUMMARY)) AS "Max_Length_Summary",
    MIN(LENGTH(b.LEARNING_OUTCOME)) AS "Min_Learning_Outcomes",
    MAX(LENGTH(b.LEARNING_OUTCOME)) AS "Max_Learning_Outcomes"
    from REFRESHER_READINGS.REFRESHER_READING_SCHEMA.PDFCONTENTDATA as a inner join REFRESHER_READINGS.REFRESHER_READING_SCHEMA.URLDATA as b on
    a.TOPIC_NAME = b.TOPIC_NAME
    group by
    b.LEVEL,
    a.TITLE,
    b.YEAR
    order by
    b.LEVEL,
    b.YEAR