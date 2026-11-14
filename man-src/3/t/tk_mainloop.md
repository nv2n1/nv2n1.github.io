---
title: "tk_mainloop(3)"
name: "tk_mainloop"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_mainloop/"
description: "Tk_MainLoop – loop for events until all windows are deleted"
---

<p>Tk_MainLoop &#8211; loop for events until all windows are deleted </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
<code>Tk_MainLoop</code>()
<br>
<hr></pre>
<h2>Description</h2>
<p><code>Tk_MainLoop</code> is a procedure that loops repeatedly calling <code>Tcl_DoOneEvent</code>. It returns only when there are no applications left in this process (i.e. no main windows exist anymore). Most windowing applications will call <code>Tk_MainLoop</code> after initialization; the main execution of the application will consist entirely of callbacks invoked via <code>Tcl_DoOneEvent</code>. </p>
<h2>Keywords</h2>
<p>application, event, main loop</p>
