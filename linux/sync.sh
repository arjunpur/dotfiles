#!/bin/bash

RSYNC='rsync -ar --progress'
$RSYNC ~/.config/nvim .
$RSYNC ~/.config/alacritty .
$RSYNC ~/.config/kinto .
$RSYNC ~/.zshrc .
