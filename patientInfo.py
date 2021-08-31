from google.cloud import bigquery

client = bigquery.Client()

query = """
    SELECT age, country, infected_by
    FROM red-truck-323016.CapstoneProject.PatientInfo
    WHERE age > '50s'
    GROUP BY age, country, infected_by
    ORDER BY age;
"""
results = client.query(query)

#job_config = bigquery.job.QueryJobConfig(use_query_cache=False)
#results = client.query(query, job_config=job_config)

for row in results:
    age = row['age']
    country = row['country']
    infected_by = row['infected_by']
    print(f'{age} | {country} | {infected_by}')

#print('-'*60)
#print(f'Created: {results.created}')
#print(f'Ended:   {results.ended}')
#print(f'Bytes:   {results.total_bytes_processed:,}')