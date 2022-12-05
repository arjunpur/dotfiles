vim.o.completeopt = "menuone,noselect"
local cmp = require("cmp")
local luasnip = require("luasnip")

local has_words_before = function()
  local line, col = unpack(vim.api.nvim_win_get_cursor(0))
  return col ~= 0 and vim.api.nvim_buf_get_lines(0, line - 1, line, true)[1]:sub(col, col):match("%s") == nil
end

cmp.setup({
	snippet = {
		expand = function(args)
			require("luasnip").lsp_expand(args.body)
		end,
	},
	mapping = {
		["<C-j>"] = cmp.mapping.scroll_docs(-4),
		["<C-k>"] = cmp.mapping.scroll_docs(4),
		["<C-Space>"] = cmp.mapping.complete(),
		["<C-c>"] = cmp.mapping.close(),
		["<CR>"] = cmp.mapping.confirm({ select = true }),
    -- Tab scrolling for the autocomplete menu
    ["<Tab>"] = cmp.mapping(function(fallback)
      if cmp.visible() then
        cmp.select_next_item()
      elseif luasnip.expand_or_jumpable() then
        luasnip.expand_or_jump()
      elseif has_words_before() then
        cmp.complete()
      else
        fallback()
      end
    end, { "i", "s" }),
    ["<S-Tab>"] = cmp.mapping(function(fallback)
      if cmp.visible() then
        cmp.select_prev_item()
      elseif luasnip.jumpable(-1) then
        luasnip.jump(-1)
      else
        fallback()
      end
    end, { "i", "s" }),
  },
	sources = {
		{ name = "nvim_lsp" },
    { name = "copilot" },
		{ name = "buffer" },
		{ name = "path" },
		{ name = "luasnip" },
    { name = 'nvim_lsp_signature_help' }
	},
	formatting = {
		format = function(entry, vim_item)
			-- fancy icons and a name of kind
			-- vim_item.kind = require("lspkind").presets.default[vim_item.kind] .. " " .. vim_item.kind

			-- set a name for each source
			vim_item.menu = ({
				nvim_lsp = "[LSP]",
				luasnip = "[Snippet]",
				path = "[Path]",
				buffer = "[Buffer]",
				nvim_lua = "[Lua]",
        copilot = "[Copilot]"
			})[entry.source.name]
			return vim_item
		end,
	},
})
