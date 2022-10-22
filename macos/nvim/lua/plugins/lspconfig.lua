local lsp = require("lspconfig")

-- lsp.dockerls.setup(require("languages.docker").lsp)
lsp.gopls.setup(require("languages.go").lsp)
-- lsp.sumneko_lua.setup(require("languages.lua").lsp)
lsp.pyright.setup(require("languages.python").lsp)
-- lsp.yamlls.setup(require("languages.yaml").lsp)
-- lsp.jsonls.setup(require("languages.json").lsp)
lsp.tsserver.setup(require("languages.typescript").lsp)
lsp.sumneko_lua.setup(require("languages.lua").lsp)

-- Don't use the lsp field because I use rust-tools
-- instead of native LSP. rust-tools acts as a pass through
-- enhancer but takes additional options
-- https://sharksforarms.dev/posts/neovim-rust/
require('rust-tools').setup(require("languages.rust").opts)

lsp.efm.setup(require("languages.efm").lsp)
require"gitlinker".setup()



