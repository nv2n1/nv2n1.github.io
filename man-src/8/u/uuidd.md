---
title: "uuidd(8)"
name: "uuidd"
section: "8"
letter: "u"
url: "/docs/linux/man/8-uuidd/"
description: "uuidd – UUID generation daemon"
---

<p>uuidd &#8211; UUID generation daemon</p>
<h2>Synopsis</h2>
<p><code>uuidd</code> [options]</p>
<h2>Description</h2>
<p>The <code>uuidd</code> daemon is used by the UUID library to generate universally unique identifiers (UUIDs), especially time-based UUIDs, in a secure and guaranteed-unique fashion, even in the face of large numbers of threads running on different CPUs trying to grab UUIDs.</p>
<h2>Options</h2>
<p><code>-d</code>, <code>&#8211;debug</code></p>
<dl>
<dd>Run uuidd in debugging mode. This prevents uuidd from running as a daemon.</dl>
<p> <code>-F</code>, <code>&#8211;no-fork</code></p>
<dl>
<dd>Do not daemonize using a double-fork.</dl>
<p> <code>-k</code>, <code>&#8211;kill</code></p>
<dl>
<dd>If currently a uuidd daemon is running, kill it.</dl>
<p> <code>-n</code>, <code>&#8211;uuids</code> <i>number</i></p>
<dl>
<dd>When issuing a test request to a running <code>uuidd</code>, request a bulk response of <i>number</i> UUIDs.</dl>
<p> <code>-P</code>, <code>&#8211;no-pid</code></p>
<dl>
<dd>Do not create a pid file.</dl>
<p> <code>-p</code>, <code>&#8211;pid</code> <i>path</i></p>
<dl>
<dd>Specify the pathname where the pid file should be written. By default, the pid file is written to <i>{runstatedir}/uuidd/uuidd.pid</i>.</dl>
<p> <code>-q</code>, <code>&#8211;quiet</code></p>
<dl>
<dd>Suppress some failure messages.</dl>
<p> <code>-r</code>, <code>&#8211;random</code></p>
<dl>
<dd>Test uuidd by trying to connect to a running uuidd daemon and request it to return a random-based UUID.</dl>
<p> <code>-S</code>, <code>&#8211;socket-activation</code></p>
<dl>
<dd>Do not create a socket but instead expect it to be provided by the calling process. This implies <code>&#8211;no-fork</code> and <code>&#8211;no-pid</code>. This option is intended to be used only with <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1). It needs to be enabled with a configure option.</dl>
<p> <code>-s</code>, <code>&#8211;socket</code> <i>path</i></p>
<dl>
<dd>Make uuidd use this pathname for the unix-domain socket. By default, the pathname used is <i>{runstatedir}/uuidd/request</i>. This option is primarily for debugging purposes, since the pathname is hard-coded in the <code>libuuid</code> library.</dl>
<p> <code>-T</code>, <code>&#8211;timeout</code> <i>number</i></p>
<dl>
<dd>Make <code>uuidd</code> exit after <i>number</i> seconds of inactivity.</dl>
<p> <code>-t</code>, <code>&#8211;time</code></p>
<dl>
<dd>Test <code>uuidd</code> by trying to connect to a running uuidd daemon and request it to return a time-based UUID.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dd>Output version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help screen and exit.</dl>
<h2>Example</h2>
<p>Start up a daemon, print 42 random keys, and then stop the daemon: </p>
<dl>
<dd>
<pre>uuidd -p /tmp/uuidd.pid -s /tmp/uuidd.socket
uuidd -d -r -n 42 -s /tmp/uuidd.socket
uuidd -d -k -s /tmp/uuidd.socket</pre>
</dl>
<h2>Author</h2>
<p>The <code>uuidd</code> daemon was written by</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-uuid/">uuid</a></code>(3), <code><a href="/docs/linux/man/1-uuidgen/">uuidgen</a></code>(1)</p>
<h2>Reporting Bugs</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>Availability</h2>
<p>The <code>uuidd</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;.</p>
