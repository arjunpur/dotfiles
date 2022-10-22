local gitlinker = require("gitlinker")

gitlinker.setup({
  callbacks = {
    ["github.plaid.com"] = require"gitlinker.hosts".get_github_type_url,
  }
})
