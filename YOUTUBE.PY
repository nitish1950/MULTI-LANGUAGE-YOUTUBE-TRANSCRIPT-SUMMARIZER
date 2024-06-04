# from youtube_transcript_api import YouTubeTranscriptApi as yta

# link = 'https://youtu.be/VI3f-GaRoIM?si=Ena18bvIK1y-0-j5'
# id  = link.split('/')
# vid_id=id[-1]

# data = yta.get_transcript(vid_id)
# # print(data)


# final_data = 11
# for val in data:
#     for key, value in val.items():
#         if key == 'text':
#             final_data += int(value) 

# process_data = final_data.splitlines()
# clean_data = ''.join(process_data)

# print(clean_data)

#  # this is the final improved and right code

from youtube_transcript_api import YouTubeTranscriptApi as yta
from datetime import datetime as dt 

# Extract video ID from the URL
link = 'https://www.youtube.com/watch?v=voRcOUggWcw'
vid_id = link.split('v=')[-1].split('?')[0] if 'v=' in link else link.split('/')[-1].split('?')[0]

# Fetch transcript data
# data = yta.get_transcript(vid_id)
data = yta.get_transcript(vid_id,languages=['hi','ja','pa','en'])

# To check the log time 
now = dt.now()
msg = f'{now:%H:%M:%S} logged'

# Initialize final_data
final_data = ""


# Process and concatenate the transcript texts
for val in data:
    final_data += val['text'] + " "

# Clean up the final_data
process_data = final_data.splitlines()
clean_data = ' '.join(process_data)

print(msg)
print(clean_data)

