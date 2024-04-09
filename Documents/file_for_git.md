# This file descript my experian in git

At this url https://github.com/settings/tokens you can create token for remote creating repository

+ Next command crate remote repo

        curl -H "Authorization: token your_token" -d "{\"name\":\"name_repo\", \"private\":true}" https://api.github.com/user/repos
    + At this command ```your_token``` - token access to git
    + ```name_repo``` - name remote repo
+ Maybe you need use next command before command that create repo:
  + ```git config --global user.email "your_email"```
  + ```git config --global user.name "your_username"```