---
title: "mailmail(1)"
name: "mailmail"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mailmail/"
description: "mailmail – Twisted sendmail compatibility script"
---

<h2>NAME</h2>
<p> mailmail &#8211; Twisted sendmail compatibility script</p>
<h2>SYNOPSIS</h2>
<p> <code>mailmail [recipient addresses]</code></p>
<h2>DESCRIPTION</h2>
<p> mailmail reads RFC822 message text from standard input and delivers them, using SMTP, to a Mail Transfer Agent listening at 127.0.0.1:25. It accepts (but does not necessarily implement) many of the standard <a href="/docs/linux/man/1-sendmail/">sendmail</a>(1) options, but it is preferable to list only the recipient addresses on the command line, and include a <code>From</code> header within the message text indicating the sender.</p>
<h2>AUTHOR</h2>
<p> Written by Jp Calderone</p>
<h2>REPORTING BUGS</h2>
<p> To report a bug, visit <i><a rel="nofollow" href="http://twistedmatrix.com/bugs/">http://twistedmatrix.com/bugs/</a></i></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2003-2008 Twisted Matrix Laboratories.<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>Index</h2>
