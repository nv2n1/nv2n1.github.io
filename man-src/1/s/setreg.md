---
title: "setreg(1)"
name: "setreg"
section: "1"
letter: "s"
url: "/docs/linux/man/1-setreg/"
description: "setreg – Change settings for public key cryptography"
---

<h2>NAME</h2>
<p> setreg &#8211; Change settings for public key cryptography</p>
<h2>SYNOPSIS</h2>
<p> <code>setreg [options] [feature] [true|false]</code></p>
<h2>DESCRIPTION</h2>
<p> Allow to configure some optional settings for public key cryptography parameters used in Mono.</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-q</i></p>
<dd> Quiet mode. Limited display on console.</p>
<dt><i>-help, -h, -?, /?</i></p>
<dd> Display help about this tool.</dl>
<h2>FEATURES</h2>
<dl>
<dt><i>1</i></p>
<dd> Trust the test root certificates (both Microsoft and Mono). Depending on the value this will add (TRUE) or remove (FALSE) the two self-signed certificates from the current user Trust store.</dl>
<h2>AUTHOR</h2>
<p> Written by Sebastien Pouliot</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2004 Novell.</p>
<h2>MAILING LISTS</h2>
<p> Visit <a rel="nofollow" href="http://lists.ximian.com/mailman/listinfo/mono-list">http://lists.ximian.com/mailman/listinfo/mono-list</a> for details.</p>
<h2>WEB SITE</h2>
<p> Visit <a rel="nofollow" href="http://www.mono-project.com">http://www.mono-project.com</a> for details</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-chktrust/">chktrust</a>(1),</code><a href="/docs/linux/man/1-certmgr/">certmgr</a>(1),<code><a href="/docs/linux/man/1-makecert/">makecert</a>(1)</code> </p>
<h2>Index</h2>
