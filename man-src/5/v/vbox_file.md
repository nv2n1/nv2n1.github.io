---
title: "vbox_file(5)"
name: "vbox_file"
section: "5"
letter: "v"
url: "/docs/linux/man/5-vbox_file/"
description: "vbox_file – file format"
---

<p>vbox_file &#8211; file format</p>
<h2>Format</h2>
<p>With version 2.0.0 of vbox the recorded files have a new header, that does not only include compression mode and connection information, but also information about the caller. </p>
<p> The current headers hold this information: </p>
<p> <code>time</code> of recording the message,<br />
 <code>compression</code> mode,<br />
 <code>CALLER</code> ID,<br />
 <code>name</code>,<br />
 <code>telephone</code> number,<br />
 <code>city</code> </p>
<p> With this information it&#8217;s possible for other programs to get the information about a message. The detailed format is described in the file libvbox.h as structure vaheader_t (this file is not included in debian gnu/linux; if you want to develop isdn programs you should get the source code).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-autovbox/">autovbox</a>(1), <a href="/docs/linux/man/1-vboxtoau/">vboxtoau</a>(1), <a href="/docs/linux/man/1-vboxmode/">vboxmode</a>(1), <a href="/docs/linux/man/1-vboxcnvt/">vboxcnvt</a>(1)</code></p>
<h2>Author</h2>
<p>This manual page was written by Andreas Jellinghaus &lt;aj [at] dungeon.inka.de&gt;, for Debian GNU/Linux and isdn4linux.</p>
