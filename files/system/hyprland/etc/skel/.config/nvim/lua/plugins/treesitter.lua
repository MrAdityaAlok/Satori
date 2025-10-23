return {
  {
    "nvim-treesitter/nvim-treesitter",
    opts = function(_, opts)
      vim.list_extend(opts.ensure_installed, {
        "hyprlang",
        "go",
        "qmljs",
      })
      opts.auto_install = true
    end,
  },
}
