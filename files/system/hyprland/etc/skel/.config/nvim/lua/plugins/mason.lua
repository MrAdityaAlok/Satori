return {
  {
    "mason-org/mason.nvim",
    opts = {
      ensure_installed = {
        "stylua",
        "shellcheck",
        "shfmt",
        "isort",
        "black",
        "prettierd",
      },
    },
  },
}
