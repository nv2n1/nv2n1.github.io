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
<dt><code>%l</code></dt>
<dd>&#8211; show the current tty</dd>
<dt><code>%h, %n</code></dt>
<dd>&#8211; show the system node name (FQDN)</dd>
<dt><code>%D, %o</code></dt>
<dd>&#8211; show the name of the NIS domain</dd>
<dt><code>%d, %t</code></dt>
<dd>&#8211; show the current time and date</dd>
<dt><code>%s</code></dt>
<dd>&#8211; show the name of the operating system</dd>
<dt><code>%m</code></dt>
<dd>&#8211; show the machine (hardware) type</dd>
<dt><code>%r</code></dt>
<dd>&#8211; show the operating system release</dd>
<dt><code>%v</code></dt>
<dd>&#8211; show the operating system version</dd>
<dt><code>%%</code></dt>
<dd>&#8211; display a single &#8216;%&#8217; character</dd></dl>
<h2>Files</h2>
<p>/etc/issue.net</p>
<h2>See Also</h2>
<p>telnetd(8) </p>
