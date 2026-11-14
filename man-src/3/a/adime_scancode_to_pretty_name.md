---
title: "adime_scancode_to_pretty_name(3)"
name: "adime_scancode_to_pretty_name"
section: "3"
letter: "a"
url: "/docs/linux/man/3-adime_scancode_to_pretty_name/"
description: "adime_scancode_to_pretty_name"
---

<h2>NAME</h2>
<p> adime_scancode_to_pretty_name</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/adime.h">adime.h</a>&gt;</code> </p>
<p> <code>char *adime_scancode_to_pretty_name(int scancode, char *buf)</code></p>
<h2>DESCRIPTION</h2>
<p> The result from `adime_scancode_to_short_name()&#8217; is sometimes an abbreviation and may contain underscores. You may want to use this function instead if you are going to display the result for the user: it returns more user-friendly strings. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-adime_scancode_to_short_name/">adime_scancode_to_short_name</a></code>(3), <code><a href="/docs/linux/man/3-adime_short_name_to_scancode/">adime_short_name_to_scancode</a></code>(3) </p>
<h2>Index</h2>
