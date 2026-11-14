---
title: "tk_getnummainwindows(3)"
name: "tk_getnummainwindows"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_getnummainwindows/"
description: "Tk_MainWindow, Tk_GetNumMainWindows – functions for querying main window information"
---

<p>Tk_MainWindow, Tk_GetNumMainWindows &#8211; functions for querying main window information </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
Tk_Window
<code>Tk_MainWindow</code>(<i>interp</i>)
int
<code>Tk_GetNumMainWindows</code>()</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in/out) Interpreter associated with the application. </p>
</dl>
<h2>Description</h2>
<p>A main window is a special kind of toplevel window used as the outermost window in an application. </p>
<p> If <i>interp</i> is associated with a Tk application then <code>Tk_MainWindow</code> returns the application&#8217;s main window. If there is no Tk application associated with <i>interp</i> then <code>Tk_MainWindow</code> returns NULL and leaves an error message in <i>interp-&gt;result</i>. </p>
<p> <code>Tk_GetNumMainWindows</code> returns a count of the number of main windows currently open in the process. </p>
<h2>Keywords</h2>
<p>application, main window</p>
