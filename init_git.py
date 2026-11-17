import os, subprocess

os.chdir(r"Z:\학교실습\deploy_web")

def run(cmd):
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True, encoding="utf-8", errors="replace")
    print("CMD:", cmd)
    if res.stdout.strip():
        print("STDOUT:", res.stdout.strip())
    if res.stderr.strip():
        print("STDERR:", res.stderr.strip())

run("git init")
run("git config user.name khwan08")
run("git config user.email 276866752+khwan08@users.noreply.github.com")
run("git add -A")
run('git commit -m "Initial commit for GitHub Pages deployment"')
run("git branch -M main")
run("git status")
run("git log -1 --oneline")
