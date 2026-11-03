import json, os, urllib.request

username = 'rrfnie'
token = os.environ.get('GITHUB_TOKEN', '')

def get(path):
    req = urllib.request.Request('https://api.github.com' + path)
    req.add_header('Accept', 'application/vnd.github+json')
    if token:
        req.add_header('Authorization', 'Bearer ' + token)
    with urllib.request.urlopen(req) as response:
        return json.load(response)

user = get('/users/' + username)
repos = get('/users/' + username + '/repos?per_page=100&sort=updated')
stars = sum(repo.get('stargazers_count', 0) for repo in repos)
forks = sum(repo.get('forks_count', 0) for repo in repos)
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="700" height="180" viewBox="0 0 700 180">
<rect width="700" height="180" rx="12" fill="#161b22"/>
<text x="30" y="42" fill="#f0f6fc" font-family="Arial,sans-serif" font-size="24" font-weight="bold">{username}'s GitHub Stats</text>
<text x="30" y="82" fill="#8b949e" font-family="Arial,sans-serif" font-size="15">Public repositories</text><text x="30" y="112" fill="#58a6ff" font-family="Arial,sans-serif" font-size="26" font-weight="bold">{user.get('public_repos', 0)}</text>
<text x="250" y="82" fill="#8b949e" font-family="Arial,sans-serif" font-size="15">Followers</text><text x="250" y="112" fill="#58a6ff" font-family="Arial,sans-serif" font-size="26" font-weight="bold">{user.get('followers', 0)}</text>
<text x="450" y="82" fill="#8b949e" font-family="Arial,sans-serif" font-size="15">Stars earned</text><text x="450" y="112" fill="#58a6ff" font-family="Arial,sans-serif" font-size="26" font-weight="bold">{stars}</text>
<text x="30" y="150" fill="#8b949e" font-family="Arial,sans-serif" font-size="14">Forks across public repositories: {forks}</text>
</svg>'''
open('github-stats.svg', 'w', encoding='utf-8').write(svg)
