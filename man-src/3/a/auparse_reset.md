---
title: "auparse_reset(3)"
name: "auparse_reset"
section: "3"
letter: "a"
url: "/docs/linux/man/3-auparse_reset/"
description: "auparse_reset – reset audit parser instance"
---

<h2>NAME</h2>
<p> auparse_reset &#8211; reset audit parser instance</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;auparse.h&gt;</code> </p>
<p> int auparse_reset(auparse_state_t *au); </p>
<h2>DESCRIPTION</h2>
<p> auparse_reset resets all internal cursors to the beginning. It closes files, descriptors, and frees memory buffers. </p>
<h2>RETURN VALUE</h2>
<p> Returns -1 if an error occurs; otherwise, 0 for success. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-auparse_init/">auparse_init</a></code>(3), <code><a href="/docs/linux/man/3-auparse_destroy/">auparse_destroy</a></code>(3). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
