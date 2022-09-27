## ZSH Options
#
# Remove superfluous blanks from each command line being added to the history
# list
setopt histreduceblanks
# Use vi key bindings in ZSH
setopt vi
# Switching directories for lazy people
setopt autocd

source ~/.config/antigen.zsh
antigen bundle zsh-users/zsh-syntax-highlighting
antigen bundle zsh-users/zsh-autosuggestions
antigen apply

# ZSH Autosuggestions
export ZSH_AUTOSUGGEST_USE_ASYNC=1
bindkey '^ ' autosuggest-accept
ZSH_AUTOSUGGEST_STRATEGY=(history completion)

# Delete previous words with ctrl-b
bindkey '^b' vi-backward-kill-word

## Design
# https://github.com/starship/starship
# https://starship.rs/config/#git-status
eval "$(starship init zsh)"
alias ls='ls -G'

[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh

alias vim='nvim'

# Pyenv
export PYTHONPATH="${PYTHONPATH}:$HOME/Projects"
export PYTHONPATH="${PYTHONPATH}:$HOME/Projects/plotterdays"

export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

# Created by `pipx` on 2022-09-11 22:21:43
export PATH="$PATH:/Users/arjun/.local/bin"
