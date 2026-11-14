---
title: "setlogcons(8)"
name: "setlogcons"
section: "8"
letter: "s"
url: "/docs/linux/man/8-setlogcons/"
description: "setlogcons – Send kernel messages to console N"
---

<p>setlogcons &#8211; Send kernel messages to console N</p>
<h2>Synopsis</h2>
<p><code>setlogcons</code> <i>N</i> </p>
<h2>Description</h2>
<p>The command <code>setlogcons</code> <i>N</i> sets all kernel messges to the console specified as N. By default kernel messages are sent to the current console. To change the level of messages sent, use <code>dmesg</code> </p>
<h2>Authors</h2>
<p><code>setlogcons</code> was originally written by Andries Brouwer for the kbd package. </p>
<p> This manual page was written by Alastair McKinstry.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-dmesg/">dmesg</a></code>(1) </p>
