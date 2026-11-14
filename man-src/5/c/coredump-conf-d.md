---
title: "coredump-conf-d(5)"
name: "coredump-conf-d"
section: "5"
letter: "c"
url: "/docs/linux/man/5-coredump-conf-d/"
description: "coredump.conf, coredump.conf.d – Coredump storage configuration files"
---

<p>coredump.conf, coredump.conf.d &#8211; Coredump storage configuration files</p>
<h2>Synopsis</h2>
<p>/etc/systemd/coredump.conf </p>
<p> /etc/systemd/coredump.conf.d/*.conf </p>
<p> /run/systemd/coredump.conf.d/*.conf </p>
<p> /usr/lib/systemd/coredump.conf.d/*.conf</p>
<h2>Description</h2>
<p>These files configure the behaviour of <code><a href="/docs/linux/man/8-systemd-coredump/">systemd-coredump</a></code>(8), a handler for core dumps invoked by the kernel.</p>
<h2>Configuration Directories And Precedence</h2>
<p>Default configuration is defined during compilation, so a configuration file is only needed when it is necessary to deviate from those defaults. By default the configuration file in /etc/systemd/ contains commented out entries showing the defaults as a guide to the administrator. This file can be edited to create local overrides. </p>
<p> When packages need to customize the configuration, they can install configuration snippets in /usr/lib/systemd/*.conf.d/. Files in /etc/ are reserved for the local administrator, who may use this logic to override the configuration files installed by vendor packages. The main configuration file is read before any of the configuration directories, and has the lowest precedence; entries in a file in any configuration directory override entries in the single configuration file. Files in the *.conf.d/ configuration subdirectories are sorted by their filename in lexicographic order, regardless of which of the subdirectories they reside in. If multiple files specify the same option, the entry in the file with the lexicographically latest name takes precedence. It is recommended to prefix all filenames in those subdirectories with a two-digit number and a dash, to simplify the ordering of the files. </p>
<p> To disable a configuration file supplied by the vendor, the recommended way is to place a symlink to /dev/null in the configuration directory in /etc/, with the same filename as the vendor configuration file.</p>
<h2>Options</h2>
<p>All options are configured in the &quot;[Coredump]&quot; section: </p>
<p> <i>Storage=</i></p>
<dl>
<dd>Controls where to store cores. One of &quot;none&quot;, &quot;external&quot;, &quot;journal&quot;, and &quot;both&quot;. When &quot;none&quot;, the coredumps will be logged but not stored permanently. When &quot;external&quot; (the default), cores will be stored in /var/lib/systemd/coredump. When &quot;journal&quot;, cores will be stored in the journal and rotated following normal journal rotation patterns. When &quot;both&quot;, cores will be stored in both locations. </p>
<p> When cores are stored in the journal, they might be compressed following journal compression settings, see <code><a href="/docs/linux/man/5-journald-conf/">journald.conf</a></code>(5). When cores are stored externally, they will be compressed by default, see below.</dl>
<p> <i>Compress=</i></p>
<dl>
<dd>Controls compression for external storage. Takes a boolean argument, defaults to &quot;yes&quot;.</dl>
<p> <i>ProcessSizeMax=</i></p>
<dl>
<dd>The maximum size in bytes of a core which will be processed. Coredumps exceeding this size will be logged, but the backtrace will not be generated and the core will not be stored.</dl>
<p> <i>ExternalSizeMax=</i>, <i>JournalSizeMax=</i></p>
<dl>
<dd>The maximum (uncompressed) size in bytes of a core to be saved.</dl>
<p> <i>MaxUse=</i>, <i>KeepFree=</i></p>
<dl>
<dd>Enforce limits on the disk space taken up by externally stored coredumps. <code>MaxUse=</code> makes sure that old coredumps are removed as soon as the total disk space taken up by coredumps grows beyond this limit (defaults to 10% of the total disk size). <code>KeepFree=</code> controls how much disk space to keep free at least (defaults to 15% of the total disk size). Note that the disk space used by coredumps might temporarily exceed these limits while coredumps are processed. Note that old coredumps are also removed based on time via <code><a href="/docs/linux/man/8-systemd-tmpfiles/">systemd-tmpfiles</a></code>(8). Set either value to 0 to turn off size based clean-up.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-systemd-journald-service/">systemd-journald.service</a></code>(8), <code><a href="/docs/linux/man/1-coredumpctl/">coredumpctl</a></code>(1), <code><a href="/docs/linux/man/8-systemd-tmpfiles/">systemd-tmpfiles</a></code>(8) </p>
