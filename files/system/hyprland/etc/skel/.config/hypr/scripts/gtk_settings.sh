#!/bin/sh

config="${XDG_CONFIG_HOME:-$HOME/.config}/gtk-3.0/settings.ini"
if [ ! -f "$config" ]; then exit 1; fi

gnome_schema="org.gnome.desktop.interface"

gtk_theme="$(grep 'gtk-theme-name' "$config" | sed 's/.*\s*=\s*//')"
icon_theme="$(grep 'gtk-icon-theme-name' "$config" | sed 's/.*\s*=\s*//')"
cursor_theme="$(grep 'gtk-cursor-theme-name' "$config" | sed 's/.*\s*=\s*//')"
font_name="$(grep 'gtk-font-name' "$config" | sed 's/.*\s*=\s*//')"
font_hinting="$(grep 'gtk-xft-hintstyle' "$config" | sed 's/.*\s*=\s*//')"
rgb_order="$(grep 'gtk-xft-rgba' "$config" | sed 's/.*\s*=\s*//')"
prefer_dark="$(grep 'gtk-application-prefer-dark-theme' "$config" | sed 's/.*\s*=\s*//')"

if [ "$prefer_dark" = 1 ]; then
  prefer_dark="prefer-dark"
else
  prefer_dark="prefer-light"
fi

# Theme
gsettings set "$gnome_schema" color-scheme "$prefer_dark"
gsettings set "$gnome_schema" gtk-theme "$gtk_theme"
gsettings set "$gnome_schema" icon-theme "$icon_theme"
gsettings set "$gnome_schema" cursor-theme "$cursor_theme"

# Fonts
gsettings set "$gnome_schema" font-name "$font_name"
gsettings set "$gnome_schema" document-font-name "$font_name"
# gsettings set org.gnome.desktop.interface monospace-font-name 'Overpass Mono 13'
gsettings set "$gnome_schema" font-antialiasing 'rgba'
gsettings set "$gnome_schema" font-hinting "$font_hinting"
gsettings set "$gnome_schema" font-rgba-order "$rgb_order"
