---
title: "lsyncd(1)"
name: "lsyncd"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lsyncd/"
description: "lsyncd – a daemon to continuously synchronize directory trees"
---

<h2 class="name">NAME</h2>
<p> lsyncd &#8211; a daemon to continuously synchronize directory trees </p>
<h2>SYNOPSIS</h2>
<p> config file</p>
<dl>
<dt>
</dt><dd> &nbsp;<wbr> <code>lsyncd</code> [<i>OPTIONS</i>] <i>CONFIG-FILE</i></dd></dl>
<p> default rsync behaviour</p>
<dl>
<dt>
</dt><dd> &nbsp;<wbr> <code>lsyncd</code> [<i>OPTIONS</i>] -rsync <i>SOURCEDIR</i> <i>TARGET</i> &#8230;</dd></dl>
<p> default rync+ssh behaviour (moves and deletes through ssh)</p>
<dl>
<dt>
</dt><dd> &nbsp;<wbr> <code>lsyncd</code> [<i>OPTIONS</i>] -rsyncssh <i>SOURCEDIR</i> <i>TARGETHOST</i> <i>TARGETDIR</i> &#8230;</dd></dl>
<p> default direct behaviour (local file operations/rsync)</p>
<dl>
<dt>
</dt><dd> &nbsp;<wbr> <code>lsyncd</code> [<i>OPTIONS</i>] -direct <i>SOURCEDIR</i> <i>TARGETDIR</i> &#8230;</dd></dl>
<h2>DESCRIPTION</h2>
<p> <a href="/docs/linux/man/1-lsyncd/">Lsyncd</a>(1) watches local directory trees through an event monitor interface (inotify, fsevents). It aggregates and combines events for a few seconds and then spawns one or more processes to synchronize the changes. By default this is <a href="/docs/linux/man/1-rsync/">rsync</a>(1). Lsyncd is thus a light-weight asynchronous live mirror solution that is comparatively easy to install not requiring new filesystems or block devices and does not hamper local filesystem performance. </p>
<p> Rsync+ssh is an advanced action configuration that uses a <a href="/docs/linux/man/1-ssh/">SSH</a>(1) to act file and directory moves directly on the target instead of re-transmitting the move destination over the wire. </p>
<p> Fine-grained customization can be achieved through the CONFIG-FILE. Custom action configs can even be written from scratch in cascading layers ranging from shell scripts to code written in the <a href="/docs/linux/man/1-lua/">LUA</a>(1) language. This way simplicity can be balanced with powerfulness. See the online manual for details on the CONFIG-FILE <a rel="nofollow" href="https://github.com/axkibe/lsyncd/wiki/Manual-to-Lsyncd-2.0.x">https://github.com/axkibe/lsyncd/wiki/Manual-to-Lsyncd-2.0.x</a> . </p>
<p> Note that under normal configuration Lsyncd will delete pre-existing files in the target directories that are not present in the respective source directory.</p>
<h2>OPTIONS</h2>
<p> <code>-delay</code> <i>SECS</i></p>
<dl>
<dt>
</dt><dd> Overrides the default delay times.</dd></dl>
<p> <code>-help</code></p>
<dl>
<dt>
</dt><dd> Show a help message.</dd></dl>
<p> <code>-insist</code></p>
<dl>
<dt>
</dt><dd> Continues start up even if rsync cannot connect.</dd></dl>
<p> <code>-log</code> <i>LEVEL</i></p>
<dl>
<dt>
</dt><dd> Controls which kind of events are logged. By default Lsyncd logs <i>Normal</i> and <i>Error</i> Messages. <code>-log scarce</code> will make Lsyncd log Error messages only. <code>-log all</code> will log all debug messages.</dd></dl>
<p> <code>-log</code> <i>Category</i></p>
<dl>
<dt>
</dt><dd> Turns on a specific debug message. E.g. <code>-log Exec</code> will log all processes as they are spawned.</dd></dl>
<p> <code>-nodaemon</code></p>
<dl>
<dt>
</dt><dd> Lsyncd will not detach from the invoker and log as well to stdout/err.</dd></dl>
<p> <code>-pidfile</code> <i>FILE</i></p>
<dl>
<dt>
</dt><dd> Lsyncd will write its process ID in <i>FILE</i>.</dd></dl>
<p> <code>-runner</code> <i>FILE</i></p>
<dl>
<dt>
</dt><dd> Makes the Lsyncd core load the part of Lsyncd written in Lua from <i>FILE</i>.</dd></dl>
<p> <code>-version</code></p>
<dl>
<dt>
</dt><dd> Writes version information and exits.</dd></dl>
<h2>EXIT STATUS</h2>
<p> <code>0</code></p>
<dl>
<dt>
</dt><dd> Terminated on a TERM <a href="/docs/linux/man/7-signal/">signal</a>(7)</dd></dl>
<p> <code>-1</code></p>
<dl>
<dt>
</dt><dd> Failure (syntax, unrecoverable error condition, internal failure)</dd></dl>
<h2>SEE ALSO</h2>
<p> Online Manual: <a rel="nofollow" href="https://github.com/axkibe/lsyncd/wiki/Lsyncd-2.1.x-%E2%80%96-What's-New%3F">https://github.com/axkibe/lsyncd/wiki/Lsyncd-2.1.x-%E2%80%96-What&#8217;s-New%3F</a></p>
<h2>VERSION</h2>
<p> This man page is for <a href="/docs/linux/man/1-lsyncd/">lsyncd</a>(1) version 2.0.7</p>
<h2>AUTHOR</h2>
<p> Axel Kittenberger, &lt;axkibe [at] gmail.com&gt; 2010-2012</p>
<h2>COPYING</h2>
<p> Copyright (C) 2010-2012 Axel Kittenberger. Free use of this software is granted under the terms of the GNU General Public License (GPL) version 2, or any later version. Free redistrubition of this Documentation (/doc directory) is granted under the terms of the Creative Commons 3.0 Attribution License (CC-3.0-BY). </p>
