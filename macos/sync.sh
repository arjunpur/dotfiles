#!/bin/bash

RSYNC='rsync -ar --delete --delete-excluded --progress'
$RSYNC ~/.config/alacritty/alacritty.yml .
$RSYNC ~/.zshrc .
$RSYNC ~/.tmux.conf .
$RSYNC ~/.config/starship.toml .
$RSYNC ~/.config/nvim/ nvim/

