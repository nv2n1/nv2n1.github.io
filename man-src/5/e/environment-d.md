---
title: "environment-d(5)"
name: "environment-d"
section: "5"
letter: "e"
url: "/docs/linux/man/5-environment-d/"
description: "environment.d – Definition of user service environment"
---

<p>environment.d &#8211; Definition of user service environment</p>
<h2>Synopsis</h2>
<p>~/.config/environment.d/*.conf </p>
<p> /etc/environment.d/*.conf </p>
<p> /run/environment.d/*.conf </p>
<p> /usr/lib/environment.d/*.conf </p>
<p> /etc/environment</p>
<h2>Description</h2>
<p>Configuration files in the environment.d/ directories contain lists of environment variable assignments for services started by the systemd user instance. <code><a href="/docs/linux/man/8-systemd-environment-d-generator/">systemd-environment-d-generator</a></code>(8) parses them and updates the environment exported by the systemd user instance. See below for an discussion of which processes inherit those variables. </p>
<p> It is recommended to use numerical prefixes for file names to simplify ordering. </p>
<p> For backwards compatibility, a symlink to /etc/environment is installed, so this file is also parsed.</p>
<h2>Configuration Directories And Precedence</h2>
<p>Configuration files are read from directories in /etc/, /run/, /usr/local/lib/, and /lib/, in order of precedence, as listed in the SYNOPSIS section above. Files must have the &quot;.conf&quot; extension. Files in /etc/ override files with the same name in /run/, /usr/local/lib/, and /lib/. Files in /run/ override files with the same name under /usr/. </p>
<p> All configuration files are sorted by their filename in lexicographic order, regardless of which of the directories they reside in. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Thus, the configuration in a certain file may either be replaced completely (by placing a file with the same name in a directory with higher priority), or individual settings might be changed (by specifying additional settings in a file with a different name that is ordered later). </p>
<p> Packages should install their configuration files in /usr/lib/ (distribution packages) or /usr/local/lib/ (local installs). Files in /etc/ are reserved for the local administrator, who may use this logic to override the configuration files installed by vendor packages. It is recommended to prefix all filenames with a two-digit number and a dash, to simplify the ordering of the files. </p>
<p> If the administrator wants to disable a configuration file supplied by the vendor, the recommended way is to place a symlink to /dev/null in the configuration directory in /etc/, with the same filename as the vendor configuration file. If the vendor configuration file is included in the initrd image, the image has to be regenerated.</p>
<h2>Configuration Format</h2>
<p>The configuration files contain a list of &quot;<i>KEY</i>=<i>VALUE</i>&quot; environment variable assignments, separated by newlines. The right hand side of these assignments may reference previously defined environment variables, using the &quot;${OTHER_KEY}&quot; and &quot;$OTHER_KEY&quot; format. It is also possible to use &quot;${<i>FOO</i>:-<i>DEFAULT_VALUE</i>}&quot; to expand in the same way as &quot;${<i>FOO</i>}&quot; unless the expansion would be empty, in which case it expands to <i>DEFAULT_VALUE</i>, and use &quot;${<i>FOO</i>:+<i>ALTERNATE_VALUE</i>}&quot; to expand to <i>ALTERNATE_VALUE</i> as long as &quot;${<i>FOO</i>}&quot; would have expanded to a non-empty value. No other elements of shell syntax are supported. </p>
<p> Each <i>KEY</i> must be a valid variable name. Empty lines and lines beginning with the comment character &quot;#&quot; are ignored.</p>
<h3>Example</h3>
<p><code>Example 1. Setup environment to allow access to a program installed in /opt/foo</code> </p>
<p> /etc/environment.d/60-foo.conf: </p>
<dl>
<dd>
<pre> FOO_DEBUG=force-software-gl,log-verbose
 PATH=/opt/foo/bin:$PATH
 LD_LIBRARY_PATH=/opt/foo/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}
 XDG_DATA_DIRS=/opt/foo/share:${XDG_DATA_DIRS:-/usr/local/share/:/usr/share/}</pre>
</dl>
<h2>Applicability</h2>
<p>Environment variables exported by the user manager (<code>systemd &#8211;user</code> instance started in the user@<i>uid</i>.service system service) apply to any services started by that manager. In particular, this may include services which run user shells. For example in the GNOME environment, the graphical terminal emulator runs as the gnome-terminal-server.service user unit, which in turn runs the user shell, so that shell will inherit environment variables exported by the user manager. For other instances of the shell, not launched by the user manager, the environment they inherit is defined by the program that starts them. Hint: in general, <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5) units contain programs launched by systemd, and <code><a href="/docs/linux/man/5-systemd-scope/">systemd.scope</a></code>(5) units contain programs launched by something else. </p>
<p> Specifically, for ssh logins, the <code><a href="/docs/linux/man/8-sshd/">sshd</a></code>(8) service builds an environment that is a combination of variables forwarded from the remote system and defined by <code>sshd</code>, see the discussion in <code><a href="/docs/linux/man/1-ssh/">ssh</a></code>(1). A graphical display session will have an analogous mechanism to define the environment. Note that some managers query the systemd user instance for the exported environment and inject this configuration into programs they start, using <code>systemctl show-environment</code> or the underlying D-Bus call.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/8-systemd-environment-d-generator/">systemd-environment-d-generator</a></code>(8), <code><a href="/docs/linux/man/7-systemd-environment-generator/">systemd.environment-generator</a></code>(7) </p>
