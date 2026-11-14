---
title: "d_ctext_proc(3)"
name: "d_ctext_proc"
section: "3"
letter: "d"
url: "/docs/linux/man/3-d_ctext_proc/"
description: "d_text_proc, d_ctext_proc, d_rtext_proc – Dialogs procedure drawing text onto the screen. Allegro game programming library."
---

<h2>NAME</h2>
<p> d_text_proc, d_ctext_proc, d_rtext_proc &#8211; Dialogs procedure drawing text onto the screen. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int d_text_proc(int msg, DIALOG *d, int c);</code> </p>
<p> <code>int d_ctext_proc(int msg, DIALOG *d, int c);</code> </p>
<p> <code>int d_rtext_proc(int msg, DIALOG *d, int c);</code></p>
<h2>DESCRIPTION</h2>
<p> These draw text onto the screen. The dp field should point to the string to display. d_ctext_proc() centers the string horizontally, and d_rtext_proc() right aligns it. Any &#8216;&amp;&#8217; characters in the string will be replaced with lines underneath the following character, for displaying keyboard shortcuts (as in MS Windows). To display a single ampersand, put &quot;&amp;&amp;&quot;. To draw the text in something other than the default font, set the dp2 field to point to your custom font data. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-exgui/">exgui</a></code>(3), <code><a href="/docs/linux/man/3-exrgbhsv/">exrgbhsv</a></code>(3) </p>
<h2>Index</h2>
