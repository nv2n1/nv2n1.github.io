---
title: "suexec(8)"
name: "suexec"
section: "8"
letter: "s"
url: "/docs/linux/man/8-suexec/"
description: "suexec – Switch user before executing external programs"
---

<p>suexec &#8211; Switch user before executing external programs</p>
<h2>Synopsis</h2>
<p> <code>suexec</code> &#8211;<code>V</code><br />
&nbsp;<wbr> </p>
<h2>Summary</h2>
<p>&nbsp;<wbr> </p>
<p> suexec is used by the Apache HTTP Server to switch to another user before executing CGI programs. In order to achieve this, it must run as root. Since the HTTP daemon normally doesn&#8217;t run as root, the suexec executable needs the setuid bit set and must be owned by root. It should never be writable for any other person than root.<br />
&nbsp;<wbr> </p>
<p> For further information about the concepts and the security model of suexec please refer to the suexec documentation (<a rel="nofollow" href="http://httpd.apache.org/docs/2.4/suexec.html">http://httpd.apache.org/docs/2.4/suexec.html</a>).<br />
&nbsp;<wbr></p>
<h2>Options</h2>
<p>&nbsp;<wbr><br />
&nbsp;<wbr></p>
<dl>
<dt>-V</p>
<dd>If you are root, this option displays the compile options of suexec. For security reasons all configuration options are changeable only at compile time.<br />
&nbsp;<wbr> </p>
</dl>
