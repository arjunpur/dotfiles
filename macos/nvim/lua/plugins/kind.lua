-- https://github.com/onsails/lspkind-nvim
-- This tiny plugin adds vscode-like pictograms to neovim built-in lsp

local lspkind = require('lspkind')
lspkind.init({
  symbol_map = {
    Copilot = "",
  },
})

vim.api.nvim_set_hl(0, "CmpItemKindCopilot", {fg ="#6CC644"})
lspkind.init()
