import subprocess

def run_command(command):
    result = subprocess.run(f"zsh -c '{command}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        print(f"Success: {command}")
    else:
        print(f"Error: {command}\n{result.stderr.decode('utf-8')}")

def reload_source():    
    run_command('source ~/.zshrc')