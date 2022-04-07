# Tools that I use:
#   - Alacritty: A terminal emulator. Config stored at ~/.config/alacritty/alacritty.yml
#   - zsh: My shell.
#   - fzf: A fuzzy finder. Config stored at ~/.fzf.zsh, while repo stored at ~/.fzf
#   - nvim: My editor. Config stored at ~/.config/nvim/init.vim
#   - tmux: Terminal multiplexer. Config stored at ~/.config/.tmux.conf

setopt histignorealldups sharehistory

# Keep 1000 lines of history within the shell and save it to ~/.zsh_history:
HISTSIZE=10000
SAVEHIST=10000
HISTFILE=~/.zsh_history

# Use modern completion system
autoload -Uz compinit
compinit

# Default to cd'ing into a directory when no `cd` is supplied
setopt autocd

# https://github.com/starship/starship
# https://starship.rs/config/#git-status
eval "$(starship init zsh)"

# Vim based navigation in zsh
bindkey -v

# Using antigen for zsh plugin management https://github.com/zsh-users/antigen
source /home/arjun/.config/zsh/antigen.zsh
antigen bundle zsh-users/zsh-syntax-highlighting
antigen bundle zsh-users/zsh-autosuggestions
antigen apply

# zsh-autosuggestions: accept suggestion key binding
# https://github.com/zsh-users/zsh-autosuggestions
bindkey '^f' autosuggest-accept

# Delete previous words with ctrl-b
bindkey '^b' vi-backward-kill-word

# Source fzf configuration
source /usr/share/doc/fzf/examples/key-bindings.zsh
source /usr/share/doc/fzf/examples/completion.zsh

# Aliases
alias ls='ls --color=auto'
alias vim='nvim'

# Set up pyenv
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"
export PYENV_VIRTUALENV_DISABLE_PROMPT=1

alias luamake=/home/arjun/Projects/tools/lua-language-server/3rd/luamake/luamake
