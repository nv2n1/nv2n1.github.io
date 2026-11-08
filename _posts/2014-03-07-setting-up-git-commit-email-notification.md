---
title: "Configuring Email Notifications for Git Push Events"
date: 2014-03-07 10:09:09 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /setting-up-git-commit-email-notification/
---

Sending email notifications when commits are pushed to a central Git repository helps teams stay coordinated and maintains audit trails. This is handled through Git hooks—scripts triggered by repository events.

## How Post-Receive Hooks Work

When a client pushes to your Git server, the `post-receive` hook executes automatically. This hook lives at `GIT_DIR/hooks/post-receive` in your bare repository. You place an executable script there that generates and sends notification emails containing commit details, diffs, and metadata.

A typical notification email includes:

- Subject line with repository name, branch, and commit message
- Commit author, date, and message body
- List of changed files
- Full diff of the changes

## Installing Mail Dependencies

You need a mail transport agent to send emails. On modern systems, `heirloom-mailx` or `msmtp` provide the most reliable interface.

**On Fedora/RHEL/CentOS 9+:**

``` bash
sudo dnf install heirloom-mailx
```

**On Debian/Ubuntu:**

``` bash
sudo apt install heirloom-mailx
```

Use `heirloom-mailx` specifically—default alternatives lack options like `-r` (sender address) that hook scripts need.

If you don’t have a local mail service running, the hook can use SMTP directly instead (covered in the SMTP section below).

## Creating the Post-Receive Hook

Git ships with a reference implementation. Find it on your system:

``` bash
find /usr/share/git-core/contrib/hooks -name "post-receive.sample" 2>/dev/null
```

Or download the current version from the Git repository:

``` bash
curl -o post-receive \
  https://raw.githubusercontent.com/git/git/master/contrib/hooks/post-receive.sample
```

If you prefer to write your own minimal hook, here’s a practical example:

``` bash
#!/bin/bash

# Read configuration from repository config
REPO_NAME=$(git rev-parse --absolute-git-dir | xargs basename)
MAILINGLIST=$(git config hooks.mailinglist)
EMAILPREFIX=$(git config hooks.emailprefix "[GIT]")
SENDEREMAIL=$(git config hooks.senderEmail "git-notify@localhost")

# Process each ref that was pushed
while read oldrev newrev refname; do
  # Skip branch deletions
  [ "$newrev" = "0000000000000000000000000000000000000000" ] && continue

  BRANCH=$(basename "$refname")
  COMMIT_MSG=$(git log -1 --format=%s "$newrev")
  SUBJECT="$EMAILPREFIX [$REPO_NAME:$BRANCH] $COMMIT_MSG"

  # Build the email body
  {
    echo "Repository: $REPO_NAME"
    echo "Branch: $BRANCH"
    echo "Pushed by: $(git log -1 --format=%an $newrev)"
    echo "Commit: $newrev"
    echo "Date: $(git log -1 --format=%aI $newrev)"
    echo ""
    echo "=== Commit Message ==="
    git log -1 --format=%B "$newrev"
    echo ""
    echo "=== Files Changed ==="
    git diff-tree --name-status -r "$oldrev" "$newrev"
    echo ""
    echo "=== Diff ==="
    git diff-tree -p "$oldrev" "$newrev"
  } | mailx -s "$SUBJECT" -r "$SENDEREMAIL" $MAILINGLIST
done
```

## Installing the Hook

Copy the hook to your bare repository and make it executable:

``` bash
cp post-receive /path/to/repo.git/hooks/post-receive
chmod 755 /path/to/repo.git/hooks/post-receive
```

For managing hooks across multiple repositories, use symlinks:

``` bash
mkdir -p /opt/git-hooks
cp post-receive /opt/git-hooks/post-receive
chmod 755 /opt/git-hooks/post-receive

# Link to each repository
ln -sf /opt/git-hooks/post-receive /path/to/repo.git/hooks/post-receive
```

The script must be executable. If permissions are wrong, the hook silently fails—always test after installation.

## Configuring Repository Settings

Store notification preferences in the repository config:

``` bash
cd /path/to/repo.git
git config hooks.mailinglist "dev@example.com ops@example.com"
git config hooks.emailprefix "[DEPLOY]"
git config hooks.senderEmail "git-notify@example.com"
git config hooks.from "Git Notifications <git-notify@example.com>"
```

Or edit the config file directly:

``` ini
[hooks]
    mailinglist = dev@example.com ops@example.com
    emailprefix = [DEPLOY]
    senderEmail = git-notify@example.com
```

Optionally, update the repository description (shown in email headers and gitweb):

``` bash
echo "My Project Name" > /path/to/repo.git/description
```

## Using SMTP Instead of Local Mail

If you don’t have a mail daemon running, configure the hook to use SMTP directly. Modify the mailx command in your hook:

``` bash
echo "$email_body" | mailx \
  -S smtp="smtps://smtp.gmail.com:465" \
  -S smtp-use-starttls=no \
  -S smtp-auth="login" \
  -S smtp-auth-user="your-email@gmail.com" \
  -S smtp-auth-password="your-app-password" \
  -s "$SUBJECT" \
  -r "$SENDEREMAIL" \
  $MAILINGLIST
```

**For Gmail:** Use an App Password instead of your account password. Store credentials in `~/.mailrc` with mode `600`:

``` bash
account gmail {
  set smtp="smtps://smtp.gmail.com:465"
  set smtp-auth="login"
  set smtp-auth-user="your-email@gmail.com"
  set smtp-auth-password="your-app-password"
}
```

Then reference it in the hook:

``` bash
echo "$email_body" | mailx -A gmail -s "$SUBJECT" -r "$SENDEREMAIL" $MAILINGLIST
```

**For msmtp:** A cleaner alternative to mailx SMTP:

``` bash
echo "$email_body" | msmtp -a default -t
```

Configure `~/.msmtprc`:

``` ini
account default
host smtp.gmail.com
port 465
security tls
auth login
user your-email@gmail.com
password your-app-password
from git-notify@example.com
```

## Testing the Hook

Push a test commit to verify the hook executes:

``` bash
cd /path/to/local/repo
git commit --allow-empty -m "Test notification hook"
git push origin main
```

Check for errors in server logs:

``` bash
# Local mail service
tail -f /var/log/mail.log

# systemd journal
journalctl -u postfix -f

# Enable debug in mailx by adding -v flag to the hook command
```

## Troubleshooting

**Hook doesn’t execute:**

- Verify executable permissions: `ls -l /path/to/repo.git/hooks/post-receive`
- Confirm the repository is bare (contains a `hooks/` directory)
- Check server Git logs or systemd journal for errors
- Test manually: `echo "oldrev newrev refs/heads/main" | /path/to/repo.git/hooks/post-receive`

**Emails not being sent:**

- Test mailx manually: `echo "test body" | mailx -s "test" user@example.com`
- Verify mailing list config: `git config hooks.mailinglist`
- Check mail service is running: `systemctl status postfix` or equivalent
- If using SMTP, test credentials separately outside the hook
- Review mail service logs for rejected recipients or authentication failures

**Missing or incomplete commit details:**

- Ensure `oldrev` and `newrev` are being read correctly from stdin
- Verify git commands work as the Git system user: `sudo -u git git log -1`
- Check that the repository path is absolute in the hook script

**Permission denied when hook tries to access Git:**

- Run the hook as the Git repository owner
- If using systemd, ensure the Git service has appropriate permissions
- Verify `git config` values are readable by the hook user

## Best Practices

- Keep hooks in version control separately (e.g., `/opt/git-hooks`) so updates apply across all repositories consistently
- Use a dedicated sender email address for Git notifications to avoid spoofing concerns
- Filter these notifications into a separate mailbox to prevent team inbox noise
- For large teams, use a mailing list service instead of individual email addresses
- Store SMTP credentials securely—never hardcode passwords in hook scripts; use `.mailrc` or environment variables
- Test hooks after any changes in a non-production repository first
- Log hook execution to syslog for audit purposes: `logger "Git hook executed for $REPO_NAME"`
- Consider adding rate limiting if your team pushes very frequently to avoid notification spam
