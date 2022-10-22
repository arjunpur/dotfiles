-- TODO: Convert these to use native neovim's remap
-- https://github.com/nvim-telescope/telescope.nvim#usage
--
local telescope = require("telescope")

vim.cmd("nnoremap <leader>ff <cmd>Telescope find_files<cr>")
vim.cmd("nnoremap <leader>fg <cmd>Telescope live_grep<cr>")
vim.cmd("nnoremap <leader>fb <cmd>Telescope buffers<cr>")
vim.cmd("nnoremap <leader>fh <cmd>Telescope help_tags<cr>")

telescope.load_extension('lsp_handlers')
-- telescope.load_extension('fzf')


