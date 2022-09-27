local lsp = require('languages.lsp')

local M = {}

M.server = {
  capabilities = lsp.capabilities,
  on_attach = lsp.on_attach,
  flags = {
    debounce_text_changes = 150, -- Avoid slamming the LSP server
  },
  settings = {
    -- to enable rust-analyzer settings visit:
    -- https://github.com/rust-analyzer/rust-analyzer/blob/master/docs/user/generated_config.adoc
    ["rust-analyzer"] = {
      -- enable clippy on save
      checkOnSave = {
        command = "clippy"
      },
    }
  }
}

M.tools = {
  autoSetHints = true,
  hover_with_actions = true,
  inlay_hints = {
    show_parameter_hints = false,
    parameter_hints_prefix = "",
    other_hints_prefix = "",
  },
}

local rust_tools_opts = {
  opts = {
    server = M.server,
    tools = M.tools,
  },
}

return rust_tools_opts

