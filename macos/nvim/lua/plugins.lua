local install_path = "~/.local/share/nvim/site/pack/packer/start/packer.nvim"

if vim.fn.empty(vim.fn.glob(install_path)) > 0 then
  vim.fn.execute("!git clone https://github.com/wbthomason/packer.nvim " .. install_path)
  vim.cmd([[ packadd packer.nvim ]])
end

local use = require("packer").use
require("packer").startup(function()
  -- Packer can manage itself
  use 'wbthomason/packer.nvim'

  -- LSP and Autocompletion
  use("neovim/nvim-lspconfig") -- Collection of configurations for built-in LSP client
  use({
    "hrsh7th/nvim-cmp",
    requires = { { "onsails/lspkind-nvim" } },
  })
  use('tpope/vim-fugitive')
  -- https://github.com/hrsh7th/nvim-cmp/wiki/List-of-sources#lsp
  use("hrsh7th/cmp-buffer")
  use("hrsh7th/cmp-path")
  use("hrsh7th/cmp-cmdline")
  use("hrsh7th/cmp-nvim-lsp")
  use("hrsh7th/cmp-nvim-lsp-signature-help")
  use("L3MON4D3/LuaSnip")
  use("saadparwaiz1/cmp_luasnip")
  use("simrat39/rust-tools.nvim")
  use("tpope/vim-commentary")
  use('folke/tokyonight.nvim')
  use('kyazdani42/nvim-web-devicons')
  use('gbrlsnchs/telescope-lsp-handlers.nvim')
  use('github/copilot.vim')
  use {
    'nvim-treesitter/nvim-treesitter',
    run = function() require('nvim-treesitter.install').update({ with_sync = true }) end,
  }
  use {
    'nvim-lualine/lualine.nvim',
    requires = { 'kyazdani42/nvim-web-devicons', opt = true }
  }
  use {
    'nvim-telescope/telescope.nvim', tag = '0.1.0',
    requires = { { 'nvim-lua/plenary.nvim' } }
  }
  use {
    'kyazdani42/nvim-tree.lua',
    requires = {
      'kyazdani42/nvim-web-devicons', -- optional, for file icons
    },
    tag = 'nightly' -- optional, updated every week. (see issue #1193)
  }
  use {
    'ruifm/gitlinker.nvim',
    requires = 'nvim-lua/plenary.nvim',
  }
  use { 'nvim-telescope/telescope-fzf-native.nvim', run = 'make' }
end)
