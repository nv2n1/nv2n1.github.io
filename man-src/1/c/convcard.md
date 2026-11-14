---
title: "convcard(1)"
name: "convcard"
section: "1"
letter: "c"
url: "/docs/linux/man/1-convcard/"
description: "convcard – converts a vCard version 2.1 in a vCard version 3.0 and vice versa"
---

<h2>NAME</h2>
<p> convcard &#8211; converts a vCard version 2.1 in a vCard version 3.0 and vice versa</p>
<h2>SYNTAX</h2>
<p> convcard <i>option</i> [<i>arguments</i>] [<i>option</i>] <i>FileName</i><br />
 convcard <i>FileName</i></p>
<h2>DESCRIPTION</h2>
<p> It converts a vCard version 2.1 in a vCard version 3.0 and vice versa.<br />
 By default the source file format is autodetected, and is converted to the other format.<br />
 <i>FileName</i> is the vCard to convert. Output will go to stdout.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;out</code> <i>FileName</i> Store the output in this file (No output to stdout)</p>
<dd>
<dt><code>&#8211;from-vcard2.1</code> Treat file as 2.1 vCard (No autodetection)</p>
<dd> Output will be a 3.0 vCard</p>
<dt><code>&#8211;from-vcard3.0</code> Treat file as 3.0 vCard (No autodetection)</p>
<dd> Output will be a 2.1 vCard</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-msynctool/">msynctool</a></code>(1)</p>
<h2>AUTHORS</h2>
<p> This manual page was written for the Debian GNU/Linux project by Matthias Jahn &lt;jahn.matthias [at] freenet.de&gt;. But it may be used by other distributions. </p>
<p> convcard was written by Armin Bauer and the OpenSync project </p>
<h2>Index</h2>
