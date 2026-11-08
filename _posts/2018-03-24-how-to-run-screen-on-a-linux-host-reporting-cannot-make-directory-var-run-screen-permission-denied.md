---
title: "Using GNU Screen as a Non-Root User with SCREENDIR"
date: 2018-03-24 11:47:11 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-run-screen-on-a-linux-host-reporting-cannot-make-directory-var-run-screen-permission-denied/
---

When you compile or run screen on a remote host where you lack root privileges, you’ll often hit this error:

    Cannot make directory '/var/run/screen': Permission denied

This happens because screen needs a socket directory to manage sessions, and `/var/run/screen` is owned by root. If screen isn’t already installed system-wide, you can’t create this directory without elevated privileges.

The solution is simple: redirect screen to use a directory in your home folder instead.

## Setting up a custom socket directory

Create a `.screen` directory in your home folder with restrictive permissions:

``` bash
mkdir -p ~/.screen
chmod 700 ~/.screen
```

The `700` permissions (read, write, execute for owner only) are important — screen enforces strict permissions on its socket directory for security reasons and will refuse to work if permissions are too loose.

## Configuring screen to use the custom directory

Set the `SCREENDIR` environment variable to point to this directory before launching screen:

``` bash
export SCREENDIR=$HOME/.screen
screen
```

If this works, add it to your shell profile so it persists across sessions:

``` bash
echo 'export SCREENDIR=$HOME/.screen' >> ~/.bashrc
source ~/.bashrc
```

For bash login shells, you might also want to add it to `~/.bash_profile`:

``` bash
echo 'export SCREENDIR=$HOME/.screen' >> ~/.bash_profile
```

If you use zsh, add it to `~/.zshrc` instead:

``` bash
echo 'export SCREENDIR=$HOME/.screen' >> ~/.zshrc
```

## Verifying the setup

After setting `SCREENDIR`, start screen and verify it’s using the correct socket directory:

``` bash
screen -S test
```

Then in another terminal, check the sockets:

``` bash
ls -la ~/.screen/
```

You should see socket files like `S-username` (a directory) or individual socket files depending on your screen version.

## Troubleshooting

**“Socket directory must have 700 permissions”** — Make sure you ran `chmod 700 ~/.screen`. Screen will not work with world-readable or group-readable socket directories.

**“Cannot connect to existing session”** — If you set `SCREENDIR` in one terminal but not another, screen won’t find your existing sessions. Ensure the variable is set consistently in all shells where you want to access screen.

**Permission denied when reattaching** — If you’re switching users or the directory permissions changed, recreate it: `rm -rf ~/.screen && mkdir -p ~/.screen && chmod 700 ~/.screen`.

## Alternative: Using tmux

If you’re building from source anyway, consider using **tmux** instead. It’s more modern, actively maintained, and handles socket directories more gracefully:

``` bash
tmux new-session -s work
```

Tmux also stores sockets in `~/.tmux/` by default and requires no special configuration for non-root users.

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
