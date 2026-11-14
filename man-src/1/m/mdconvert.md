---
title: "mdconvert(1)"
name: "mdconvert"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mdconvert/"
description: "mdconvert – Maildir mailbox UID storage scheme converter"
---

<h2 class="name">NAME</h2>
<p> mdconvert &#8211; Maildir mailbox UID storage scheme converter </p>
<h2>SYNOPSIS</h2>
<p> <code>mdconvert</code> [<i>options</i> &#8230;] <i>mailbox</i> &#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>mdconvert</code> converts Maildir mailboxes between the two UID storage schemes supported by <code>mbsync</code>. See <code>mbsync</code>&#8216;s manual page for details on these schemes.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code>, <code>&#8211;alt</code></p>
<dd> Convert to the <code>alternative</code> (Berkeley DB based) UID storage scheme.</p>
<dt><code>-n</code>, <code>&#8211;native</code></p>
<dd> Convert to the <code>native</code> (file name based) UID storage scheme. This is the default.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Displays a summary of command line options.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Displays version information.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-mbsync/">mbsync</a>(1)</p>
<h2>AUTHOR</h2>
<p> Written and maintained by Oswald Buddenhagen &lt;ossi [at] users.sf.net&gt;. </p>
<h2>Index</h2>
