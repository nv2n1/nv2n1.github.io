---
title: "binfmt(5)"
name: "binfmt"
section: "5"
letter: "b"
url: "/docs/linux/man/5-binfmt/"
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
<p>Each file contains a list of binfmt_misc kernel binary format rules. Consult m[blue]<code>binfmt_misc.txt</code>m[]<font SIZE="-2">[1]</font> for more information on registration of additional binary formats and how to write rules. </p>
<p> Empty lines and lines beginning with ; and # are ignored. Note that this means you may not use ; and # as delimiter in binary format rules. </p>
<p> Each configuration file shall be named in the style of <i>program</i>.conf. Files in /etc/ override files with the same name in /usr/lib/ and /run/. Files in /run/ override files with the same name in /usr/lib/. Packages should install their configuration files in /usr/lib/, files in /etc/ are reserved for the local administrator, who may use this logic to override the configuration files installed from vendor packages. All files are sorted by their filename in lexicographic order, regardless of which of the directories they reside in. If multiple files specify the same binary type name, the entry in the file with the lexicographically latest name will be applied. </p>
<p> If the administrator wants to disable a configuration file supplied by the vendor, the recommended way is to place a symlink to /dev/null in /etc/binfmt.d/ bearing the same filename.</p>
<h2>Example</h2>
<p><code>Example 1.&nbsp;<wbr>/etc/binfmt.d/wine.conf example:</code> </p>
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
<dd>binfmt_misc.txt</p>
<dl>
<dd><a rel="nofollow" href="https://www.kernel.org/doc/Documentation/binfmt_misc.txt">https://www.kernel.org/doc/Documentation/binfmt_misc.txt</a></dl>
