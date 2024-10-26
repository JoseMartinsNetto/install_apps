from utils import run_command

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

def install_brew_packages():
    for package in brew_packages:
        run_command(f"brew install {package}")

def install_cask_apps():
    for app in cask_apps:
        run_command(f"brew install --cask {app}")