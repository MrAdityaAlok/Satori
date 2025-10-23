function kitty_theme --argument theme
    if ! set -ql theme
        echo "Name of theme not given."
        return 1
    end
    if not test -f ~/.config/kitty/kitty-themes/themes/$theme.conf
        if not wget "https://raw.githubusercontent.com/dexpota/kitty-themes/master/themes/$theme.conf" -P ~/.config/kitty/kitty-themes/themes
            return 1
        end
    end

    eval ( cd ~/.config/kitty/ && ln -sf ./kitty-themes/themes/$theme.conf ~/.config/kitty/theme.conf )
    echo " Set theme: $theme"
end
