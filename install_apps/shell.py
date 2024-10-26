from install_apps.utils import *

def configure_dotfiles():
    run_command("curl -o ~/.funcs.zsh https://raw.githubusercontent.com/JoseMartinsNetto/dotfiles/refs/heads/master/.funcs.zsh")
    run_command("curl -o ~/.gitconfig https://raw.githubusercontent.com/JoseMartinsNetto/dotfiles/refs/heads/master/.gitconfig")
    run_command("curl -o ~/.wezterm.lua https://raw.githubusercontent.com/JoseMartinsNetto/dotfiles/refs/heads/master/.wezterm.lua")
    run_command("curl -o ~/.zshrc https://raw.githubusercontent.com/JoseMartinsNetto/dotfiles/refs/heads/master/.zshrc")
    run_command("curl -o ~/.tmux.conf https://raw.githubusercontent.com/JoseMartinsNetto/dotfiles/refs/heads/master/.tmux.conf")

def configure_oh_myzsh():
    run_command('sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"')
    run_command("git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting")
    run_command("git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions")

def configure_shell():
    reload_source()

    # Setup git
    run_command("git config --global user.name 'José Martins'")
    run_command("git config --global user.email 'j.msantos.netto@gmail.com'")
    
     # Setup zsh
    configure_dotfiles()
    reload_source()
    configure_oh_myzsh()
    reload_source()