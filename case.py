from google.cloud import bigquery

client = bigquery.Client()

query = """
    SELECT province, city, infection_case 
    FROM red-truck-323016.CapstoneProject.Case
    GROUP BY province, city, infection_case 
    ORDER BY infection_case desc 
    LIMIT 10;
"""
#results = client.query(query)

job_config = bigquery.job.QueryJobConfig(use_query_cache=False)
results = client.query(query, job_config=job_config)

for row in results:
    province = row['province']
    city = row['city']
    infection_case = row['infection_case']
    print(f'{province} | {city} | {infection_case}')

print('-'*60)
print(f'Created: {results.created}')
print(f'Ended:   {results.ended}')
print(f'Bytes:   {results.total_bytes_processed:,}')