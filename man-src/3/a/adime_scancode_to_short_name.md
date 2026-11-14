---
title: "adime_scancode_to_short_name(3)"
name: "adime_scancode_to_short_name"
section: "3"
letter: "a"
url: "/docs/linux/man/3-adime_scancode_to_short_name/"
description: "adime_scancode_to_short_name"
---

<h2>NAME</h2>
<p> adime_scancode_to_short_name</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/adime.h">adime.h</a>&gt;</code> </p>
<p> <code>char *adime_scancode_to_short_name(int scancode, char *buf)</code></p>
<h2>DESCRIPTION</h2>
<p> Converts a keyboard scancode to a string. The string is exactly the text after `KEY_&#8217; in the macro name for the key (so the function returns &quot;DELETE&quot; if you feed it with KEY_DELETE). Returns the buffer, or NULL if the scancode didn&#8217;t match any known key. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-adime_scancode_to_pretty_name/">adime_scancode_to_pretty_name</a></code>(3), <code><a href="/docs/linux/man/3-adime_short_name_to_scancode/">adime_short_name_to_scancode</a></code>(3) </p>
<h2>Index</h2>
