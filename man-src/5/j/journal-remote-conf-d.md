---
title: "journal-remote-conf-d(5)"
name: "journal-remote-conf-d"
section: "5"
letter: "j"
url: "/docs/linux/man/5-journal-remote-conf-d/"
description: "journal-remote.conf, journal-remote.conf.d – Journal remote service configuration files"
---

<p>journal-remote.conf, journal-remote.conf.d &#8211; Journal remote service configuration files</p>
<h2>Synopsis</h2>
<p>/etc/systemd/journal-remote.conf </p>
<p> /etc/systemd/journald.conf.d/*.conf </p>
<p> /run/systemd/journald.conf.d/*.conf </p>
<p> /usr/lib/systemd/journald.conf.d/*.conf</p>
<h2>Description</h2>
<p>These files configure various parameters of the systemd-remote-journal application, <code><a href="/docs/linux/man/8-systemd-journal-remote/">systemd-journal-remote</a></code>(8).</p>
<h2>Configuration Directories And Precedence</h2>
<p>Default configuration is defined during compilation, so a configuration file is only needed when it is necessary to deviate from those defaults. By default the configuration file in /etc/systemd/ contains commented out entries showing the defaults as a guide to the administrator. This file can be edited to create local overrides. </p>
<p> When packages need to customize the configuration, they can install configuration snippets in /usr/lib/systemd/*.conf.d/. Files in /etc/ are reserved for the local administrator, who may use this logic to override the configuration files installed by vendor packages. The main configuration file is read before any of the configuration directories, and has the lowest precedence; entries in a file in any configuration directory override entries in the single configuration file. Files in the *.conf.d/ configuration subdirectories are sorted by their filename in lexicographic order, regardless of which of the subdirectories they reside in. If multiple files specify the same option, the entry in the file with the lexicographically latest name takes precedence. It is recommended to prefix all filenames in those subdirectories with a two-digit number and a dash, to simplify the ordering of the files. </p>
<p> To disable a configuration file supplied by the vendor, the recommended way is to place a symlink to /dev/null in the configuration directory in /etc/, with the same filename as the vendor configuration file.</p>
<h2>Options</h2>
<p>All options are configured in the &quot;[Remote]&quot; section: </p>
<p> <i>Seal=</i></p>
<dl>
<dd>Periodically sign the data in the journal using Forward Secure Sealing.</dl>
<p> <i>SplitMode=</i></p>
<dl>
<dd>One of &quot;host&quot; or &quot;none&quot;.</dl>
<p> <i>ServerKeyFile=</i></p>
<dl>
<dd>SSL key in PEM format</dl>
<p> <i>ServerCertificateFile=</i></p>
<dl>
<dd>SSL CA certificate in PEM format.</dl>
<p> <i>TrustedCertificateFile=</i></p>
<dl>
<dd>SSL CA certificate.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd-journal-remote/">systemd-journal-remote</a></code>(1), <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/8-systemd-journald-service/">systemd-journald.service</a></code>(8) </p>
