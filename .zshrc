#----------------------------------------------------------
# setting
#----------------------------------------------------------
export LANG=ja_JP.UTF-8
export BAT_THEME=zenburn
export ANDROID_HOME=$HOME/Library/Android/sdk
export PATH=$PATH:$ANDROID_HOME:$ANDROID_HOME/emulator:$ANDROID_HOME/tools/:$ANDROID_HOME/platform-tools
export PATH="$PATH:$HOME/flutter/bin"
export PATH="/Users/ageha/.rd/bin:$PATH"

export PATH="$PATH:$HOME/.local/bin/rust-analyzer"
#export PATH="$PATH:$HOME/.local/bin"
#export PATH="$PATH:$HOME/.local/bin"
#export PATH="$PATH:$HOME/.local/bin"
#export PATH="$PATH:$HOME/.local/bin"
#export PATH="$PATH:$HOME/.local/bin"
#export PATH="$PATH:$HOME/.local/bin"

if [ -e "$HOME/.anyenv" ]
then
    export ANYENV_ROOT="$HOME/.anyenv"
    export PATH="$ANYENV_ROOT/bin:$PATH"
    if command -v anyenv 1>/dev/null 2>&1
    then
        eval "$(anyenv init -)"
    fi
fi

source /usr/local/Caskroom/google-cloud-sdk/latest/google-cloud-sdk/path.zsh.inc
source /usr/local/Caskroom/google-cloud-sdk/latest/google-cloud-sdk/completion.zsh.inc
eval "$(starship init zsh)"

# zellij session reset
if [[ $(command -v zellij ) ]]; then
  alias rezellij='zellij kill-all-sessions -y'
fi

# exa(ls)
if [[ $(command -v exa) ]]; then
  alias e='exa --icons --git'
  alias l=e
  alias ls=e
  alias ea='exa -a --icons --git'
  alias la=ea
  alias ee='exa -aahl --icons --git'
  alias ll=ee
  alias et='exa -T -L 3 -a -I "node_modules|.git|.cache" --icons'
  alias lt=et
  alias eta='exa -T -a -I "node_modules|.git|.cache" --color=always --icons | less -r'
  alias lta=eta
  alias l='clear && ls'
fi

# lsd(ls)
if [[ $(command -v lsd) ]]; then
    alias ts='lsd -A --group-dirs=last'
    alias tt='lsd -Ahl --total-size --group-dirs=last'
    alias tree='lsd -A --tree --group-dirs=last'
    alias tr='lsd -Ahl --total-size --tree --group-dirs=last'
    alias tl='lsd -1FL --icon never --group-dirs first'
fi

# bat(cat)
if [[ $(command -v bat) ]]; then
    alias cat='bat --paging=never'
    alias less='bat'
    alias -g L='|bat --style=plain'
    ch() { cheat $* | bat --style=plain -l zsh }
    pop() { cd $(dirs -lp | bat -r 2: | fzf --no-sort --prompt='cd >') }
fi

# choose(cut)
if [[ $(command -v choose) ]]; then
    alias cut='choose'
fi

# duf(v)
if [[ $(command -v duf) ]]; then
    alias df='duf'
fi

# delta(diff)
if [[ $(command -v delta) ]]; then
    alias diff='delta'
fi

# procs(ps)
if [[ $(command -v procs) ]]; then
    alias ps='procs --tree'
fi

# zoxide（cd）
if [[ $(command -v zoxide) ]]; then
    eval "$(zoxide init --cmd j zsh)"
fi

# dust（du）
if [[ $(command -v dust) ]]; then
    alias du='dust'
fi

# fd(find)
if [[ $(command -v fd) ]]; then
    alias find='fd'
fi

# ripgrep(grep)
if [[ $(command -v rg) ]]; then
    alias grep='rg -S'
    alias -g G='|rg -S'
    jgrep() { gron | grep $* | gron -u }
fi

# bottom（top）
if [[ $(command -v btm) ]]; then
    alias top='btm'
fi

# gtime（time）
if [[ $(command -v gtime) ]]; then
    alias time='gtime'
fi

# trash（rm）
if [[ $(command -v trash) ]]; then
    alias rm='trash -F'
fi

if [[ $(command -v git) ]]; then
    alias g='git'
    alias ga='git add'
    alias gd='git diff'
    alias gs='git status'
    alias gp='git push'
    alias gb='git branch'
    alias gst='git status'
    alias gco='git checkout'
    alias gcp="git cherry-pick"
    alias gf='git fetch'
    alias gc='git commit'
    alias gl="git log"
    alias gm="git merge"
fi

if [[ $(command -v composer) ]]; then
  alias cda='composer dump-autoload'
  alias pmigrate='php artisan migrate'
  alias prollback='php artisan migrate:rollback'
  alias prefresh='php artisan migrate:refresh'
  alias pseed='php artisan db:seed'
fi

if [[ $(command -v bundle) ]]; then
    alias b='bundle'
    alias be='bundle exec'
    alias bx='bundle exec'
    alias bi='bundle install'
    alias bo='bundle outdated'
    alias bu='bundle update'
    alias rc='bundle exec rails c'
fi

if [[ $(command -v python) ]]; then
    alias python='python3'
    alias py='python'
    if [[ $(command -v pip) ]]; then
        alias pip='pip3'
        alias pi='pip install'
        alias pu='pip uninstall'
        alias pl='pip list'
        alias ps='pip show'
        alias pc='pip check'
  fi
fi

if [[ $(command -v docker) ]]; then
    alias d='docker'
    alias dp='docker ps'
    alias dk='docker kill'
    alias di='docker image'
    alias dil='docker image ls'
    alias dn='docker network'
    alias dnl='docker network ls'
    alias dv='docker volume'
    alias dvl='docker volume ls'
    alias dcnt='docker container'
    alias dcur='docker container ls -f status=running -l -q'
    alias dexec='docker container exec -it $(dcur)'
    alias drun='docker container run —rm -d'
    alias drunit='docker container run —rm -it'
    alias dport='docker container port $(dcur)'
    alias dstart='docker container start $(dcur)'
    alias drestart='docker container restart $(dcur)'
    alias dstop='docker container stop $(dcur)'
    if [[ $(command -v docker-compose) ]]; then
      alias dc='docker compose'
      alias dcp='docker compose ps'
      alias dcd='docker compose down'
      alias dck='docker compose kill'
      alias dcl='docker compose ls'
      alias dcl='docker compose logs -f'
      alias dcs='docker compose start'
      alias dcr='docker compose restart'
      alias dct='docker compose stop'

    fi
fi

alias .2='cd ../../'
alias .3='cd ../../../'
alias ls="ls -atG"
alias lls="ls -alF"
alias ll='ls -alF'
alias la='ls -A'
alias l='clear && ls -CF'
alias plack="plackup script/app.psgi -I../wanon2/lib"
alias ve='emacs -nw'
alias vv="vim"
alias v="vim"
alias :wq="exit"
alias :q="exit"
alias re="sudo supervisorctl restart plack; tail -f /var/log/supervisor/plack/error.txt"
alias ide="~/.scripts/ide.sh"
alias lab='jupyter lab'
