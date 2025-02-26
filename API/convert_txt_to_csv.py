import csv
import re
import os
def process_twitter_data(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        
        writer = csv.writer(outfile)
        writer.writerow(['TwitterID', 'Content', 'Hashtag'])
        
        for line in infile:
            line = line.strip()
            if not line.startswith('@'):
                continue
                
            # Split Twitter ID and content
            if ': ' in line:
                twitter_id, content = line.split(': ', 1)
            else:
                twitter_id = line
                content = ""
            
            # Extract hashtags using regex
            hashtags = list(set(re.findall(r'#(\w+)', content)))  # Extract without #
            
            # Write None explicitly if no hashtags
            hashtags_str = ', '.join(hashtags) if hashtags else 'None'
            
            writer.writerow([twitter_id, content, hashtags_str])

# Usage
os.makedirs("Temp", exist_ok=True)
process_twitter_data('sample_twitter.txt', 'Temp/sample_twitter_data.csv')
