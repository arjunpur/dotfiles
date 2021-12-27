# See ~/.zshenv for environment variables

## ZSH Options
# Remove superfluous blanks from each command line being added to the history
# list
setopt histreduceblanks
# Remove command lines from the history list when the first character on the
# line is a space, or when one of the expanded aliases contains a leading space
setopt histignorespace
# Do not enter command lines into the history list if they are duplicates of the
# previous event.
setopt histignorealldups
# Switching directories for lazy people
setopt autocd
# Disable annoying confirm
setopt rmstarsilent
# Use vi key bindings in ZSH
setopt vi

## Design
# https://github.com/starship/starship
# https://starship.rs/config/#git-status
eval "$(starship init zsh)"
alias ls='ls -G'

## Plugins
# Using antigen for zsh plugin management https://github.com/zsh-users/antigen
source ~/.config/zsh/antigen.zsh
antigen bundle zsh-users/zsh-syntax-highlighting
antigen bundle zsh-users/zsh-autosuggestions
antigen apply

# Completion
# Initialize the completion system
autoload -Uz compinit
[[ -f  ~/.devenv-completion.sh ]] && source  ~/.devenv-completion.sh
zstyle ':completion:*' fzf-search-display true

## FZF Configuration
export ZSH_AUTOSUGGEST_USE_ASYNC=1
bindkey '^ ' autosuggest-accept
[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh

# Cache completion if nothing changed - faster startup time
typeset -i updated_at=$(date +'%j' -r ~/.zcompdump 2>/dev/null || stat -f '%Sm' -t '%j' ~/.zcompdump 2>/dev/null)
if [ $(date +'%j') != $updated_at ]; then
  compinit -i
else
  compinit -C -i
fi

## Languages

export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
if command -v pyenv 1>/dev/null 2>&1; then
  eval "$(pyenv init -)"
  eval "$(pyenv virtualenv-init -)"
fi

# Commented out nvm initialization in favor of system node
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" nvm node npm  # This loads nvm


## Aliases
alias gp='git push'
alias gs='git status'
alias plgo='cd /Users/apuri/plaid/go.git'
alias vim=nvim

function awsenv() {
  export AWS_ACCESS_KEY_ID=$(aws configure get aws_access_key_id)
  export AWS_SECRET_ACCESS_KEY=$(aws configure get aws_secret_access_key)
  export AWS_SESSION_TOKEN=$(aws configure get aws_session_token)
  export AWS_SECURITY_TOKEN=$(aws configure get aws_security_token)
}

function branch() {
  id=$(date +"%Y%m%d")
  branch="ap-$id-$1"
  git checkout -b $branch 
  git push --set-upstream origin $branch 
}

function compush() {
  git add "$1"
  git commit -m "$2" 
  git push --set-upstream origin `git rev-parse --abbrev-ref HEAD`
}

alias rdocker='env \
    DOCKER_TLS_VERIFY="1" \
    DOCKER_HOST="tcp://apuri.devenv.plaid.io:2376" \
    DOCKER_CERT_PATH="/Users/apuri/plaid/go.git/resources/development-certs/remote_devenv_certs" \
    docker'

fzg() {
    rg . -n $1 | \
    fzf \
        -m \
        --preview='IFS=":"; \
            read -Ar first_line <<< {1}; \
            line=${first_line[1]};
            file_name=${first_line[0]};
            start=$(($line - 5));
            if [ $start -lt 0 ]; then start=0; fi;
            end=$(($line + 5));
            bat --color="always" -H ${line} -r ${start}:${end} ${file_name}' \
                --border | \
    sed 's/[:].*$//'
}

ec2ip () {
        local instance_id="${1}" 
        printf "%s" "$(aws ec2 describe-instances --instance-ids "${instance_id}" | jq -r '.Reservations[].Instances[].PrivateIpAddress')"
}
