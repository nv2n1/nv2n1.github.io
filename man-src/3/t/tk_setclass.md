---
title: "tk_setclass(3)"
name: "tk_setclass"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_setclass/"
description: "Tk_SetClass, Tk_Class – set or retrieve a window’s class"
---

<p>Tk_SetClass, Tk_Class &#8211; set or retrieve a window&#8217;s class </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
<code>Tk_SetClass</code>(<i>tkwin, class</i>)
Tk_Uid
<code>Tk_Class</code>(<i>tkwin</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tk_Window <i>tkwin</i> (in) Token for window.</p>
<dd>char <i>*class</i> (in) New class name for window. </p>
</dl>
<h2>Description</h2>
<p><code>Tk_SetClass</code> is called to associate a class with a particular window. The <i>class</i> string identifies the type of the window; all windows with the same general class of behavior (button, menu, etc.) should have the same class. By convention all class names start with a capital letter, and there exists a Tcl command with the same name as each class (except all in lower-case) which can be used to create and manipulate windows of that class. A window&#8217;s class string is initialized to NULL when the window is created. </p>
<p> For main windows, Tk automatically propagates the name and class to the WM_CLASS property used by window managers. This happens either when a main window is actually created (e.g. in <code>Tk_MakeWindowExist</code>), or when <code>Tk_SetClass</code> is called, whichever occurs later. If a main window has not been assigned a class then Tk will not set the WM_CLASS property for the window. </p>
<p> <code>Tk_Class</code> is a macro that returns the current value of <i>tkwin</i>&#8216;s class. The value is returned as a Tk_Uid, which may be used just like a string pointer but also has the properties of a unique identifier (see the manual entry for <code>Tk_GetUid</code> for details). If <i>tkwin</i> has not yet been given a class, then <code>Tk_Class</code> will return NULL. </p>
<h2>Keywords</h2>
<p>class, unique identifier, window, window manager</p>
