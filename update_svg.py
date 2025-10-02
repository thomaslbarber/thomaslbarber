import requests
import datetime

# GitHub repo info
OWNER = "thomas"
REPO = "thomaslbarber"
TOKEN = "${{ secrets.GITHUB_TOKEN }}"

# Time window (past 7 days)
since = (datetime.datetime.utcnow() - datetime.timedelta(days=7)).isoformat() + "Z"

# Fetch commits
url = f"https://api.github.com/repos/{OWNER}/{REPO}/commits"
params = {"since": since}
headers = {"Authorization": f"token {TOKEN}"}

r = requests.get(url, headers=headers, params=params)
commits = r.json()

commit_count = len(commits)

# Read template
with open("tamagotchi.svg", "r") as f:
    svg = f.read()

# Replace placeholder
svg = svg.replace("{{COMMITS}}", str(commit_count))

# Write updated SVG
with open("dist/tamagotchi.svg", "w") as f:
    f.write(svg)
