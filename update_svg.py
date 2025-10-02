import requests
import datetime

OWNER = "thomas"
REPO = "thomaslbarber"
TOKEN = "${{ secrets.GITHUB_TOKEN }}"

since = (datetime.datetime.utcnow() - datetime.timedelta(days=7)).isoformat() + "Z"

url = f"https://api.github.com/repos/{OWNER}/{REPO}/commits"
params = {"since": since}
headers = {"Authorization": f"token {TOKEN}"}

r = requests.get(url, headers=headers, params=params)
commits = r.json()

commit_count = len(commits)

with open("dist/tamagotchi.svg", "r") as f:
    svg = f.read()

print(svg)

svg = svg.replace("{{COMMITS}}", str(commit_count))
print(svg)

with open("tamagotchi-out.svg", "w") as f:
    f.write(svg)
