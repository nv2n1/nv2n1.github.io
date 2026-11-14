---
title: "issue-net(5)"
name: "issue-net"
section: "5"
letter: "i"
url: "/docs/linux/man/5-issue-net/"
description: "issue.net – identification file for telnet sessions"
---

<p><code>issue.net </code> &#8211; identification file for telnet sessions</p>
<h2>Description</h2>
<p>The file /etc/issue.net is a text file which contains a message or system identification to be printed before the login prompt of a telnet session. It may contain various `%-char&#8217; (or, alternatively, &#8216;\-char&#8217;) sequences. The following sequences are supported by <code>telnetd</code></p>
<dl>
<dt><code>%l</code></p>
<dd>&#8211; show the current tty</p>
<dt><code>%h, %n</code></p>
<dd>&#8211; show the system node name (FQDN)</p>
<dt><code>%D, %o</code></p>
<dd>&#8211; show the name of the NIS domain</p>
<dt><code>%d, %t</code></p>
<dd>&#8211; show the current time and date</p>
<dt><code>%s</code></p>
<dd>&#8211; show the name of the operating system</p>
<dt><code>%m</code></p>
<dd>&#8211; show the machine (hardware) type</p>
<dt><code>%r</code></p>
<dd>&#8211; show the operating system release</p>
<dt><code>%v</code></p>
<dd>&#8211; show the operating system version</p>
<dt><code>%%</code></p>
<dd>&#8211; display a single &#8216;%&#8217; character</dl>
<h2>Files</h2>
<p>/etc/issue.net</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-telnetd/">telnetd</a>(8) </p>
