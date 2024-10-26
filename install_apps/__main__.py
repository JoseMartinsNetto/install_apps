from install_apps.brew import *
from install_apps.utils import *
from shell import *

def install_java():
    run_command('curl -s "https://get.sdkman.io" | bash')
    reload_source()
    run_command("sdk install java 17.0.12-amzn")

def install_deno():
    run_command("curl -fsSL https://deno.land/install.sh | sh")

def install_rust():
    run_command("curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh")

def configure_nvim():
    run_command("git clone https://github.com/JoseMartinsNetto/nvim2.git ~/.config/nvim")

if __name__ == "__main__":
    # install_brew_packages()
    # install_cask_apps()
    # configure_shell()
    install_java()
    # install_deno()
    # install_rust()
    # configure_nvim()

    print("Setup completo!")