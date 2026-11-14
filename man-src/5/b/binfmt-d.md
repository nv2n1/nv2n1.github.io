---
title: "binfmt-d(5)"
name: "binfmt-d"
section: "5"
letter: "b"
url: "/docs/linux/man/5-binfmt-d/"
description: "binfmt.d – Configure additional binary formats for executables at boot"
---

<p>binfmt.d &#8211; Configure additional binary formats for executables at boot</p>
<h2>Synopsis</h2>
<p>/etc/binfmt.d/*.conf </p>
<p> /run/binfmt.d/*.conf </p>
<p> /usr/lib/binfmt.d/*.conf</p>
<h2>Description</h2>
<p>At boot, <code><a href="/docs/linux/man/8-systemd-binfmt-service/">systemd-binfmt.service</a></code>(8) reads configuration files from the above directories to register in the kernel additional binary formats for executables.</p>
<h2>Configuration Format</h2>
<p>Each file contains a list of binfmt_misc kernel binary format rules. Consult the kernel&#8217;s m[blue]<code>binfmt-misc.rst</code>m[]<font SIZE="-2">[1]</font> documentation file for more information on registration of additional binary formats and how to write rules. </p>
<p> Empty lines and lines beginning with ; and # are ignored. Note that this means you may not use ; and # as delimiter in binary format rules.</p>
<h2>Configuration Directories And Precedence</h2>
<p>Configuration files are read from directories in /etc/, /run/, /usr/local/lib/, and /lib/, in order of precedence, as listed in the SYNOPSIS section above. Files must have the &quot;.conf&quot; extension. Files in /etc/ override files with the same name in /run/, /usr/local/lib/, and /lib/. Files in /run/ override files with the same name under /usr/. </p>
<p> All configuration files are sorted by their filename in lexicographic order, regardless of which of the directories they reside in. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Thus, the configuration in a certain file may either be replaced completely (by placing a file with the same name in a directory with higher priority), or individual settings might be changed (by specifying additional settings in a file with a different name that is ordered later). </p>
<p> Packages should install their configuration files in /usr/lib/ (distribution packages) or /usr/local/lib/ (local installs). Files in /etc/ are reserved for the local administrator, who may use this logic to override the configuration files installed by vendor packages. It is recommended to prefix all filenames with a two-digit number and a dash, to simplify the ordering of the files. </p>
<p> If the administrator wants to disable a configuration file supplied by the vendor, the recommended way is to place a symlink to /dev/null in the configuration directory in /etc/, with the same filename as the vendor configuration file. If the vendor configuration file is included in the initrd image, the image has to be regenerated.</p>
<h2>Example</h2>
<p><code>Example 1.&nbsp;/etc/binfmt.d/wine.conf example:</code> </p>
<dl>
<dd>
<pre># Start WINE on Windows executables
:DOSWin:M::MZ::/usr/bin/wine:</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/8-systemd-binfmt-service/">systemd-binfmt.service</a></code>(8), <code><a href="/docs/linux/man/1-systemd-delta/">systemd-delta</a></code>(1), <code><a href="/docs/linux/man/8-wine/">wine</a></code>(8)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>binfmt-misc.rst</p>
<dl>
<dd><a rel="nofollow" href="https://www.kernel.org/doc/html/latest/admin-guide/binfmt-misc.html">https://www.kernel.org/doc/html/latest/admin-guide/binfmt-misc.html</a></dl>
