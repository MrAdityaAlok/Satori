-- Options are automatically loaded before lazy.nvim startup
-- Default options that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/options.lua
-- Add any additional options here

local opt = vim.opt

opt.relativenumber = false

opt.guifont = "Iosevka Nerd Font:h13"

if vim.g.neovide then
  vim.g.neovide_opacity = 0.65
  vim.g.neovide_normal_opacity = 0.65
  -- vim.g.neovide_cursor_vfx_mode = "railgun"
end
