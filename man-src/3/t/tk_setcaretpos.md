---
title: "tk_setcaretpos(3)"
name: "tk_setcaretpos"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_setcaretpos/"
description: "Tk_SetCaretPos – set the display caret location"
---

<p>Tk_SetCaretPos &#8211; set the display caret location </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
int
<code>Tk_SetCaretPos</code>(<i>tkwin, x, y, height</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tk_Window <i>tkwin</i> (in) Token for window.</p>
<dd>int <i>x</i> (in) Window-relative x coordinate.</p>
<dd>int <i>y</i> (in) Window-relative y coordinate.</p>
<dd>int <i>h</i> (in) Height of the caret in the window. </p>
</dl>
<h2>Description</h2>
<p><code>Tk_SetCaretPos</code> sets the caret location for the display of the specified Tk_Window <i>tkwin</i>. The caret is the per-display cursor location used for indicating global focus (e.g. to comply with Microsoft Accessibility guidelines), as well as for location of the over-the-spot XIM (X Input Methods) or Windows IME windows. </p>
<h2>Keywords</h2>
<p>caret, cursor</p>
