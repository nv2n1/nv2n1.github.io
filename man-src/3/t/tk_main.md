---
title: "tk_main(3)"
name: "tk_main"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_main/"
description: "Tk_Main – main program for Tk-based applications"
---

<p>Tk_Main &#8211; main program for Tk-based applications </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
<code>Tk_Main</code>(<i>argc, argv, appInitProc</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>int <i>argc</i> (in) Number of elements in <i>argv</i>.</p>
<dd>char <i>*argv[]</i> (in) Array of strings containing command-line arguments.</p>
<dd>Tcl_AppInitProc <i>*appInitProc</i> (in) Address of an application-specific initialization procedure. The value for this argument is usually <code>Tcl_AppInit</code>. </p>
</dl>
<h2>Description</h2>
<p><code>Tk_Main</code> acts as the main program for most Tk-based applications. Starting with Tk 4.0 it is not called <code>main</code> anymore because it is part of the Tk library and having a function <code>main</code> in a library (particularly a shared library) causes problems on many systems. Having <code>main</code> in the Tk library would also make it hard to use Tk in C++ programs, since C++ programs must have special C++ <code>main</code> functions. </p>
<p> Normally each application contains a small <code>main</code> function that does nothing but invoke <code>Tk_Main</code>. <code>Tk_Main</code> then does all the work of creating and running a <code>wish</code>-like application. </p>
<p> When it is has finished its own initialization, but before it processes commands, <code>Tk_Main</code> calls the procedure given by the <i>appInitProc</i> argument. This procedure provides a &#8220;hook&#8221; for the application to perform its own initialization, such as defining application-specific commands. The procedure must have an interface that matches the type <code>Tcl_AppInitProc</code>:</p>
<dl COMPACT>
<dd>
<pre>typedef int Tcl_AppInitProc(Tcl_Interp *<i>interp</i>);</pre>
</dl>
<p> <i>AppInitProc</i> is almost always a pointer to <code>Tcl_AppInit</code>; for more details on this procedure, see the documentation for <code>Tcl_AppInit</code>. </p>
<h2>Keywords</h2>
<p>application-specific initialization, command-line arguments, main program</p>
