return {
  {
    "rebelot/kanagawa.nvim",
    opts = {
      compile = true,
      transparent = true,
      theme = "dragon",
    },
  },
  {
    "folke/tokyonight.nvim",
    opts = {
      style = "night",
      transparent = true,
      styles = {
        sidebars = "transparent",
        -- floats = "transparent",
      },
      -- on_colors = function(colors)
      --   colors.comment = colors.fg_dark
      -- end,
    },
  },
}
