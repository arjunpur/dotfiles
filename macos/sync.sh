#!/bin/bash

RSYNC='rsync -ar --delete --delete-excluded --progress'
$RSYNC --exclude nvim/vim_runtime/.git --exclude nvim/vim_runtime/temp_dirs ~/.config/nvim .
$RSYNC ~/.config/alacritty/alacritty.yml .
$RSYNC ~/.zshrc .
$RSYNC ~/.tmux.conf .
$RSYNC ~/.config/starship.toml .

