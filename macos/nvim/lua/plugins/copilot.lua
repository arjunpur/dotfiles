-- https://github.com/LunarVim/nvim-basic-ide/compare/master...copilot-0.7
vim.cmd[[imap <silent><script><expr> <C-a> copilot#Accept("\<CR>")]]
vim.g.copilot_no_tab_map = true
