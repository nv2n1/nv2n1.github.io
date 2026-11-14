---
title: "killall5(8)"
name: "killall5"
section: "8"
letter: "k"
url: "/docs/linux/man/8-killall5/"
description: "killall5 — send a signal to all processes."
---

<p>killall5 &#8212; send a signal to all processes.</p>
<h2>Synopsis</h2>
<p><code>killall5</code> <code>-signalnumber</code> [<code>-o</code> <i>omitpid</i>[,<i>omitpid</i>&#8230;]] [<code>-o</code> <i>omitpid</i>[,<i>omitpid</i>&#8230;]&#8230;]</p>
<h2>Description</h2>
<p><code>killall5</code> is the SystemV killall command. It sends a signal to all processes except kernel threads and the processes in its own session, so it won&#8217;t kill the shell that is running the script it was called from. Its primary (only) use is in the <code>rc</code> scripts found in the /etc/init.d directory.</p>
<h2>Options</h2>
<dl>
<dt>-o <i>omitpid</i></p>
<dd>Tells <i>killall5</i> to omit processes with that process id.</dl>
<h2>Notes</h2>
<p><i>killall5</i> can also be invoked as pidof, which is simply a (symbolic) link to the <i>killall5</i> program.</p>
<h2>Exit Status</h2>
<p>The program return zero if it killed processes. It return 2 if no process were killed, and 1 if it was unable to find any processes (/proc/ is missing).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-halt/">halt</a></code>(8), <code><a href="/docs/linux/man/8-reboot/">reboot</a></code>(8), <code><a href="/docs/linux/man/8-pidof/">pidof</a></code>(8)</p>
<h2>Author</h2>
<p>Miquel van Smoorenburg, miquels [at] cistron.nl</p>
