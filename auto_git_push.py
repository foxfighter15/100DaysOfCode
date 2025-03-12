import os
import time

repo_path = "C:/Users/kashp/OneDrive/Desktop/100DaysOfCode"  # Apne Git repo ka exact path daalo
commit_message = "Auto-commit: New changes"

while True:
    os.system(f"cd {repo_path} && git add . && git commit -m '{commit_message}' && git push origin main")
    time.sleep(60)  # Har 60 sec baad auto push karega
