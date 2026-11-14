---
title: "tk_clearselection(3)"
name: "tk_clearselection"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_clearselection/"
description: "Tk_ClearSelection – Deselect a selection"
---

<p>Tk_ClearSelection &#8211; Deselect a selection </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
<code>Tk_ClearSelection</code>(<i>tkwin, selection</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tk_Window <i>tkwin</i> (in) The selection will be cleared from the display containing this window.</p>
<dd>Atom <i>selection</i> (in) The name of selection to be cleared. </p>
</dl>
<h2>Description</h2>
<p><code>Tk_ClearSelection</code> cancels the selection specified by the atom <i>selection</i> for the display containing <i>tkwin</i>. The selection need not be in <i>tkwin</i> itself or even in <i>tkwin</i>&#8216;s application. If there is a window anywhere on <i>tkwin</i>&#8216;s display that owns <i>selection</i>, the window will be notified and the selection will be cleared. If there is no owner for <i>selection</i> on the display, then the procedure has no effect. </p>
<h2>Keywords</h2>
<p>clear, selection</p>
