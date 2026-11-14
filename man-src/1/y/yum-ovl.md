---
title: "yum-ovl(1)"
name: "yum-ovl"
section: "1"
letter: "y"
url: "/docs/linux/man/1-yum-ovl/"
description: "yum-ovl – Performs an initial copy-up of yum(8) package database."
---

<h2>NAME</h2>
<p> yum-ovl &#8211; Performs an initial copy-up of <a href="/docs/linux/man/8-yum/">yum</a>(8) package database.</p>
<h2>OPTIONS</h2>
<p> <code>-d</code> <i>debug-level</i> If debug level is <i>2</i> and more, print out the number of files copied up from the lower layer</p>
<h2>DESCRIPTION</h2>
<p> Opening a file on OverlayFS in read-only mode causes the file from<br />
 lower layer to be opened, then later on, if the same file is opened<br />
 in write mode, a copy-up into the upper layer takes place,<br />
 resulting into a <code>new</code> file being opened.<br />
 Since <a href="/docs/linux/man/8-yum/">yum</a>(8) needs to open the <code>RPMdb</code> first read-only, and then<br />
 also with write access, we need to copy-up the files beforehand to<br />
 make sure that the access is consistent.</p>
<h2>FILES</h2>
<p> <i>/usr/lib/yum-plugins/ovl.py</i> Plugin itself </p>
<p> <i>/etc/yum/pluginconf.d/ovl.conf</i> Configuration file allowing to enable/disable the plugin</p>
<h2>AUTHOR</h2>
<p> Pavel Odvody <i>podvody [at] redhat.com</i></p>
<h2>LICENSE</h2>
<p> 2015, Red Hat, Licensed under GPLv2+</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-yum/">yum</a>(1) <a href="/docs/linux/man/8-yum/">yum</a>(8) <a href="/docs/linux/man/8-rpmdb/">rpmdb</a>(8) </p>
<h2>Index</h2>
