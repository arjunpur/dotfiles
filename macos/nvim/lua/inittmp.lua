-- Reccomended by nvim-tree: https://github.com/kyazdani42/nvim-tree.lua#setup
vim.g.loaded = 1
vim.g.loaded_netrwPlugin = 1

require("plugins")
require("plugins.cmp")
require("plugins.kind")
require("plugins.lspconfig")
require("plugins.telescope")
require("plugins.colorscheme")
require("plugins.nvim-tree")
require("plugins.gitlinker")
require("plugins.nvim-tree")
require("plugins.copilot")

-- empty setup using defaults
