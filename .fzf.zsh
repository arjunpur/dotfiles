# Setup fzf
# ---------
if [[ ! "$PATH" == */home/arjun/.fzf/bin* ]]; then
  export PATH="${PATH:+${PATH}:}/home/arjun/.fzf/bin"
fi

# Auto-completion
# ---------------
[[ $- == *i* ]] && source "/home/arjun/.fzf/shell/completion.zsh" 2> /dev/null

# Key bindings
# ------------
source "/home/arjun/.fzf/shell/key-bindings.zsh"
