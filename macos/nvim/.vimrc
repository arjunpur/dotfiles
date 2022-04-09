set runtimepath+=~/.config/nvim

source ~/.config/nvim/vim_runtime/vimrcs/basic.vim
source ~/.config/nvim/vim_runtime/vimrcs/filetypes.vim
source ~/.config/nvim/vim_runtime/vimrcs/plugins_config.vim
source ~/.config/nvim/vim_runtime/vimrcs/extended.vim

try
source ~/.config/nvim/vim_runtime/my_configs.vim
catch
endtry
