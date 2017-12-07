eval "$(ssh-agent -s)"
ssh-add /root/.ssh/gitbot

yes | git clone git@github.com:PRNDcompany/heydealer-android-v4.git