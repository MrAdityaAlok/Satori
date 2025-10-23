if status is-interactive

    if uwsm check may-start
        exec uwsm start hyprland.desktop
    end

    zoxide init --cmd cd fish | source
    starship init fish | source

    gpgconf --launch gpg-agent # Start or re-use a gpg-agent
    set -e SSH_AGENT_PID
    set -gx SSH_AUTH_SOCK "$(gpgconf --list-dirs agent-ssh-socket)"
    gpg-connect-agent updatestartuptty /bye &>/dev/null

    # Set theme using matugen: (Using starship currently)
    fish_config theme choose Matugen
end
