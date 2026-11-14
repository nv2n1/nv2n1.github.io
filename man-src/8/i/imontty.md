---
title: "imontty(8)"
name: "imontty"
section: "8"
letter: "i"
url: "/docs/linux/man/8-imontty/"
description: "imontty – display status of all ISDN lines"
---

<p>imontty &#8211; display status of all ISDN lines</p>
<h2>Synopsis</h2>
<p><code>imontty</code> [ phonebook ]</p>
<h2>Description</h2>
<p><i>imontty</i> displays the status of all ISDN lines. No options are supported. Read access to <i>/dev/isdninfo</i> is required. It is possible to supply the name of a phonebook file. The phonebook file has the following format: </p>
<pre> number&lt;tab&gt;name for number</pre>
<p>The number must be the first thing on the line (no leading spaces). The name is separated from the number by a tab. Lines beginning with # are ignored, as are empty lines. The output is similar to this: </p>
<pre>ISDN channel status:
Channel Usage Type Number
----------------------------------------------------------
line0 Out Net 0204229700 
line0 Off </pre>
<p><i>Usage</i> is one of <code>Off</code>(line), <code>Out</code>(going), <code>In</code>(coming) or <code>Excl</code>(usive). <i>Type</i> is one of <code>raw</code> (raw device), <code>Modem</code> (modem/tty emulation), <code>Net</code> (IP interface), <code>Voice</code> (voice call) or <code>Fax</code> (fax transmission). <i>Number</i> is either the called party&#8217;s number (outgoing) or the calling party number (incoming). </p>
<h2>Author</h2>
<p>Volker Götz volker [at] oops.franken.de<br />
 manpage adapted from the README by Paul Slootman &lt;paul [at] isdn4linux.de&gt;</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-imon/">imon</a></i>(8) </p>
