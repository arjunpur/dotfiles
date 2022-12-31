local lsp = require('languages.lsp')

-- https://jdhao.github.io/2021/08/12/nvim_sumneko_lua_conf/
-- https://github.com/neovim/nvim-lspconfig/blob/master/doc/server_configurations.md#sumneko_lua
-- local sumneko_binary_path = vim.fn.exepath('lua-language-server')
-- local sumneko_root_path = vim.fn.fnamemodify(sumneko_binary_path, ':h')

local runtime_path = vim.split(package.path, ';')
table.insert(runtime_path, "lua/?.lua")
table.insert(runtime_path, "lua/?/init.lua")
table.insert(runtime_path, "/opt/homebrew/share/lua/5.4/?.lua")
table.insert(runtime_path, "/opt/homebrew/share/lua/5.4/?/init.lua")


local M = {}

M.lsp = {
  capabilities = lsp.capabilities,
  on_attach = lsp.on_attach,
  -- cmd = {sumneko_binary_path, "-E", sumneko_root_path .. "/main.lua"};
  settings = {
    Lua = {
      runtime = {
          -- Tell the language server which version of Lua you're using (most likely LuaJIT in the case of Neovim)
          version = 'Lua 5.4',
          -- Setup your lua path
          path = runtime_path,
      },
      diagnostics = {
          -- Get the language server to recognize the `vim` global
          globals = {'vim'},
      },
      workspace = {
          -- Make the server aware of Neovim runtime files
          library = {
            vim.api.nvim_get_runtime_file("", true),
            "/opt/homebrew/share/lua/5.4/",
          }
      },
      -- Do not send telemetry data containing a randomized but unique identifier
      telemetry = {
          enable = false,
      },
    },
  },
}

return M
