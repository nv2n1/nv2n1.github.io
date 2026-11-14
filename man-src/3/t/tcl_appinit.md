---
title: "tcl_appinit(3)"
name: "tcl_appinit"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_appinit/"
description: "Tcl_AppInit – perform application-specific initialization"
---

<p>Tcl_AppInit &#8211; perform application-specific initialization </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
int
<code>Tcl_AppInit</code>(<i>interp</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter for the application. </p>
</dl>
<h2>Description</h2>
<p><code>Tcl_AppInit</code> is a &#8220;hook&#8221; procedure that is invoked by the main programs for Tcl applications such as <code>tclsh</code> and <code>wish</code>. Its purpose is to allow new Tcl applications to be created without modifying the main programs provided as part of Tcl and Tk. To create a new application you write a new version of <code>Tcl_AppInit</code> to replace the default version provided by Tcl, then link your new <code>Tcl_AppInit</code> with the Tcl library. </p>
<p> <code>Tcl_AppInit</code> is invoked by <code>Tcl_Main</code> and <code>Tk_Main</code> after their own initialization and before entering the main loop to process commands. Here are some examples of things that <code>Tcl_AppInit</code> might do:</p>
<dl COMPACT>
<dt>[1]</p>
<dd>Call initialization procedures for various packages used by the application. Each initialization procedure adds new commands to <i>interp</i> for its package and performs other package-specific initialization.</p>
<dt>[2]</p>
<dd>Process command-line arguments, which can be accessed from the Tcl variables <code>argv</code> and <code>argv0</code> in <i>interp</i>.</p>
<dt>[3]</p>
<dd>Invoke a startup script to initialize the application.</dl>
<p> <code>Tcl_AppInit</code> returns <code>TCL_OK</code> or <code>TCL_ERROR</code>. If it returns <code>TCL_ERROR</code> then it must leave an error message in for the interpreter&#8217;s result; otherwise the result is ignored. </p>
<p> In addition to <code>Tcl_AppInit</code>, your application should also contain a procedure <code>main</code> that calls <code>Tcl_Main</code> as follows:</p>
<dl COMPACT>
<dd>
<pre>Tcl_Main(argc, argv, Tcl_AppInit);</pre>
</dl>
<p> The third argument to <code>Tcl_Main</code> gives the address of the application-specific initialization procedure to invoke. This means that you do not have to use the name <code>Tcl_AppInit</code> for the procedure, but in practice the name is nearly always <code>Tcl_AppInit</code> (in versions before Tcl 7.4 the name <code>Tcl_AppInit</code> was implicit; there was no way to specify the procedure explicitly). The best way to get started is to make a copy of the file <code>tclAppInit.c</code> from the Tcl library or source directory. It already contains a <code>main</code> procedure and a template for <code>Tcl_AppInit</code> that you can modify for your application. </p>
<h2>Keywords</h2>
<p>application, argument, command, initialization, interpreter</p>
