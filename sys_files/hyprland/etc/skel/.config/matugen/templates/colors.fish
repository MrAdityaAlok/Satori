# vi: ft=fish

set -g fish_color_normal '{{colors.on_surface.default.hex}}'
set -g fish_color_command '{{colors.primary.default.hex}}'
set -g fish_color_keyword '{{colors.tertiary.default.hex}}'
set -g fish_color_quote '{{colors.secondary.default.hex}}'
set -g fish_color_redirection '{{colors.inverse_primary.default.hex}}'
set -g fish_color_end '{{colors.error.default.hex}}'
set -g fish_color_error '{{colors.error.default.hex}}'

set -g fish_color_param '{{colors.on_surface.default.hex}}'
set -g fish_color_option '{{colors.secondary.default.hex}}'
set -g fish_color_comment '{{colors.outline_variant.default.hex}}'
set -g fish_color_operator '{{colors.tertiary.default.hex}}'
set -g fish_color_escape '{{colors.outline.default.hex}}'

set -g fish_color_autosuggestion '{{colors.outline.default.hex}}'
set -g fish_color_cancel -r
set -g fish_color_valid_path --underline

set -g fish_color_selection --bold '--background={{colors.surface_variant.default.hex}}'
set -g fish_color_search_match '--background={{colors.tertiary_container.default.hex}}'

set -g fish_pager_color_progress '{{colors.on_surface.default.hex}}' '--background={{colors.primary_container.default.hex}}'
set -g fish_pager_color_prefix '{{colors.primary.default.hex}}' --bold --underline
set -g fish_pager_color_completion '{{colors.on_surface.default.hex}}'
set -g fish_pager_color_description '{{colors.on_surface_variant.default.hex}}'
set -g fish_pager_color_selected_background '--background={{colors.secondary_container.default.hex}}'
