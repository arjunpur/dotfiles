local lsp = require('languages.lsp')

local M = {}

local black = {
	formatCommand = "black --line-length 100 --quiet -",
	formatStdin = true,
}
local flake8 = {
	lintCommand = "flake8 --max-line-length 100 --stdin-display-name ${INPUT} -",
	lintStdin = true,
	lintFormats = { "%f:%l:%c: %m" },
	lintIgnoreExitCode = true,
	lintSource = "flake8",
}
local mypy = {
	lintCommand = "mypy --show-column-numbers",
	lintFormats = {
		"%f:%l:%c: %trror: %m",
		"%f:%l:%c: %tarning: %m",
		"%f:%l:%c: %tote: %m",
	},
	lintIgnoreExitCode = true,
	lintSource = "mypy",
}

M.efm = {
	black,
	flake8,
	mypy,
}

M.all_format = { efm = "Black" }

M.default_format = "efm"

M.lsp = {
  capabilities = lsp.capabilities,
  on_attach = function(client)
    client.resolved_capabilities.document_formatting = false
    lsp.on_attach(client, 0)
  end,
  flags = {
    debounce_text_changes = 150, -- Avoid slamming the LSP server
  },
  settings = {
    python = {
      analysis = {
        autoSearchPaths = true,
        diagnosticMode = "workspace",
        useLibraryCodeForTypes = true,
        -- vsketch is installed via pipx in a separate virtualenv path so we need to tell pyright where this is
        -- https://github-wiki-see.page/m/neovim/nvim-lspconfig/wiki/Understanding-setup-%7B%7D
        -- https://github.com/microsoft/pylance-release/issues/1020
        extraPaths = {"/home/arjun/.local/pipx/venvs/vsketch/lib/python3.8/site-packages"},
      }
    }
  }
}

return M
