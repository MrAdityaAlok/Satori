if type -q eza
    set -l ls_command "eza -1lmu --classify --icons --colour always --color-scale "
    alias ls "$ls_command"
    alias l "$ls_command"
    alias lsa "$ls_command"-albghHliS
    alias lst "$ls_command"-T
end

alias rm "rm -i"
alias mv "mv -i"
alias cp "cp -i"
