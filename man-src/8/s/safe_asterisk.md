---
title: "safe_asterisk(8)"
name: "safe_asterisk"
section: "8"
letter: "s"
url: "/docs/linux/man/8-safe_asterisk/"
description: "safe_asterisk — A wrapper to run the asterisk executable in a loop"
---

<p><code>safe_asterisk</code> &#8212; A wrapper to run the asterisk executable in a loop</p>
<h2>Synopsis</h2>
<p><code>safe_asterisk</code> <i>[ asterisk_params ]</i> </p>
<h2>Description</h2>
<p><code>safe_asterisk </code> is a script that runs asterisk in a loop, which can be useful if you fear asterisk may crash. The script does not run in the background like a standard service. Rather, it runs in its own linux virtual console (9, by default). It also uses the option &#8216;-c&#8217; of <a href="/docs/linux/man/8-asterisk/">asterisk</a>(8) to avoid detaching asterisk from that terminal. safe_asterisk also runs asterisk with unlimited core file size, and thus asterisk will dump core in case of a crash. To get a &quot;picture&quot; of console 9, from another terminal (e.g: from a remote shell session) you can use:<br />
&nbsp;<wbr>&nbsp;<wbr>screendump 9 The init script of the Debian package should be able to run safe_asterisk as the asterisk service, if so configured. See coments in /etc/default/asterisk </p>
<h2>Files</h2>
<p><code>/tmp</code></p>
<dl>
<dd>safe_asterisk runs in that directory, rather than in / as usual.</dl>
<p> <code>/tmp/core</code></p>
<dl>
<dd>If core files were generated there, they may be</dl>
<p> <code>/etc/asterisk/startup.d</code></p>
<dl>
<dd>Files in this directory will be &#8216;source&#8217;d by the safe_asterisk script before it starts Asterisk proper, allowing them to set additional environment variables or run any other steps that are needed for your system.</dl>
<h2>Bugs</h2>
<p>While showing the output on a console is useful, using <a href="/docs/linux/man/1-screen/">screen</a>(1) as the terminal may be better. The script does not read configuration from standard location under /etc It uses fixed locations under /tmp , and thus may be exposed to a symlink attacks. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-asterisk/">asterisk</a>(8), <a href="/docs/linux/man/9-screendump/">screendump</a>(9) </p>
<h2>Author</h2>
<p>This manual page was written by Tzafrir Cohen &lt;tzafrir.cohen [at] xorcom.com&gt; Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 any later version published by the Free Software Foundation. </p>
<p> On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL.</p>
