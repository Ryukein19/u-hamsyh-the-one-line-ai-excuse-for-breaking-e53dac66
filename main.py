import os
# One-liner entry (141 chars): the line below is the whole submission.
# Writes to /output/entry.txt.
LINE = "I did not break production. I merely gave it a surprise feature: a four-hour nap. The users called it an outage, but the servers needed rest."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
