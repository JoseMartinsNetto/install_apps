import subprocess

brew_packages = [
    "git",
    "neovim",
    "wget",
    "htop",
    "ffmpeg",
    "gleam",
    "go",
    "nvm",
    "tmux",
    "rust"
]

cask_apps = [
    "visual-studio-code",
    "google-chrome",
    "docker",
    "jetbrains-toolbox",
    "c0re100-qbittorrent",
    "postman",
    "dbeaver-community",
    "whatsapp",
    "telegram",
    "franz",
    "obs",
    "wezterm",
    "accord",
    "microsoft-teams",
    "macs-fan-control",
    "devcleaner",
    "zed",
    "elmedia-player",
    "sherlock",
    "locationsimulator"
]

def run_command(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        print(f"Success: {command}")
    else:
        print(f"Error: {command}\n{result.stderr.decode('utf-8')}")

def install_brew_packages():
    for package in brew_packages:
        run_command(f"brew install {package}")

def install_cask_apps():
    for app in cask_apps:
        run_command(f"brew install --cask {app}")

def configure_dotfiles():
    run_command("curl -o ~/.zshrc https://raw.githubusercontent.com/JoseMartinsNetto/dotfiles/refs/heads/master/.funcs.zsh")
    run_command("curl -o ~/.zshrc https://raw.githubusercontent.com/JoseMartinsNetto/dotfiles/refs/heads/master/.gitconfig")
    run_command("curl -o ~/.zshrc https://raw.githubusercontent.com/JoseMartinsNetto/dotfiles/refs/heads/master/.wezterm.lua")
    run_command("curl -o ~/.zshrc https://raw.githubusercontent.com/JoseMartinsNetto/dotfiles/refs/heads/master/.zshrc")

def configure_oh_myzsh():
    run_command('"sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"')
    run_command("git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting")
    run_command("git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions")

def install_java():
    run_command('curl -s "https://get.sdkman.io" | bash')
    run_command("sdk install java 17.0.12-amzn")

def configure_shell():
    # Setup git
    run_command("git config --global user.name 'José Martins'")
    run_command("git config --global user.email 'j.msantos.netto@gmail.com'")
    
     # Setup zsh
    configure_dotfiles()
    configure_oh_myzsh()

if __name__ == "__main__":
    install_brew_packages()
    install_cask_apps()
    install_java()
    configure_shell()
    print("Setup completo!")