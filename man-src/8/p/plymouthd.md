---
title: "plymouthd(8)"
name: "plymouthd"
section: "8"
letter: "p"
url: "/docs/linux/man/8-plymouthd/"
description: "plymouthd – The plymouth daemon"
---

<p>plymouthd &#8211; The plymouth daemon</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>plymouthd </code><code>[OPTION&#8230;]</code></dt></dl>
<h2>Description</h2>
<dd>The <code>plymouthd</code> daemon is usually run out of the initrd. It does the heavy lifting of the plymouth system, logging the session and showing the splash screen. </dd>
<p> The <code>plymouth</code> is used to send commands to plymouthd that control its behaviour.</p>
<h2>Options</h2>
<p>The following options are understood: </p>
<p> <code>&#8211;help</code></p>
<dl>
<dd>Show summary of options.</dd></dl>
<p> <code>&#8211;attach-to-session</code></p>
<dl>
<dd>Redirect console messages from screen to log.</dd></dl>
<p> <code>&#8211;no-daemon</code></p>
<dl>
<dd>Do not daemonize.</dd></dl>
<p> <code>&#8211;debug</code></p>
<dl>
<dd>Output debugging information.</dd></dl>
<p> <code>&#8211;debug-file=STRING</code></p>
<dl>
<dd>File to write debugging information to.</dd></dl>
<p> <code>&#8211;mode=MODE</code></p>
<dl>
<dd>Set mode to either boot or shutdown.</dd></dl>
<p> <code>&#8211;pid-file=STRING</code></p>
<dl>
<dd>Write the PID of the daemon to a file.</dd></dl>
<p> <code>&#8211;kernel-command-line=STRING</code></p>
<dl>
<dd>Fake kernel commandline to use.</dd></dl>
<p> <code>&#8211;tty=STRING</code></p>
<dl>
<dd>TTY to use instead of default.</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-grub/">grub</a></code>(8), <code><a href="/docs/linux/man/8-plymouth/">plymouth</a></code>(8), <code><a href="/docs/linux/man/1-plymouth/">plymouth</a></code>(1), m[blue]<code><a rel="nofollow" href="http://www.freedesktop.org/wiki/Software/Plymouth">http://www.freedesktop.org/wiki/Software/Plymouth</a></code>m[] </p>
