local lsp = require('languages.lsp')

local M = {}

M.lsp = {
  capabilities = lsp.capabilities,
  on_attach = lsp.on_attach,
  flags = {
    debounce_text_changes = 150, -- Avoid slamming the LSP server
  }
}

return M
