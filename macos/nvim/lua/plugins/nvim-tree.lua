local nvimtree = require("nvim-tree")

nvimtree.setup({
  respect_buf_cwd = true,
  sync_root_with_cwd = true,
  hijack_unnamed_buffer_when_opening = true,
  update_focused_file = {
    enable      = true,
    update_root = true,
    ignore_list = {}
  }
})

vim.cmd("map <leader>nn :NvimTreeToggle<Cr>")
vim.cmd("map <leader>nf :NvimTreeFindFile<Cr>")
