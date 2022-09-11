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
  -- https://github.com/hrsh7th/nvim-cmp/wiki/List-of-sources#lsp
  use("hrsh7th/cmp-buffer")
  use("hrsh7th/cmp-path")
  use("hrsh7th/cmp-cmdline")
	use("hrsh7th/cmp-nvim-lsp")
  use("hrsh7th/cmp-nvim-lsp-signature-help")
  use("L3MON4D3/LuaSnip")
  use("saadparwaiz1/cmp_luasnip")
  use("simrat39/rust-tools.nvim")
end)
