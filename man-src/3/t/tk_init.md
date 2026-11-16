---
title: "tk_init(3)"
name: "tk_init"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_init/"
description: "Tk_Init, Tk_SafeInit – add Tk to an interpreter and make a new Tk application."
---

<p>Tk_Init, Tk_SafeInit &#8211; add Tk to an interpreter and make a new Tk application. </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
int
<code>Tk_Init</code>(<i>interp</i>)
int
<code>Tk_SafeInit</code>(<i>interp</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter in which to load Tk. Tk should not already be loaded in this interpreter. </dd>
</dl>
<h2>Description</h2>
<p><code>Tk_Init</code> is the package initialization procedure for Tk. It is normally invoked by the <code>Tcl_AppInit</code> procedure for an application or by the <code>load</code> command. <code>Tk_Init</code> adds all of Tk&#8217;s commands to <i>interp</i> and creates a new Tk application, including its main window. If the initialization is successful <code>Tk_Init</code> returns <code>TCL_OK</code>; if there is an error it returns <code>TCL_ERROR</code>. <code>Tk_Init</code> also leaves a result or error message in <i>interp-&gt;result</i>. </p>
<p> If there is a variable <code>argv</code> in <i>interp</i>, <code>Tk_Init</code> treats the contents of this variable as a list of options for the new Tk application. The options may have any of the forms documented for the <code>wish</code> application (in fact, <code>wish</code> uses Tk_Init to process its command-line arguments). </p>
<p> <code>Tk_SafeInit</code> is identical to <code>Tk_Init</code> except that it removes all Tk commands that are considered unsafe. Those commands and the reasons for their exclusion are:</p>
<dl COMPACT>
<dt><code>bell</code></dt>
<dd>Continuous ringing of the bell is a nuisance.</dd>
<dt><code>clipboard</code></dt>
<dd>A malicious script could replace the contents of the clipboard with the string &#8220;<code>rm -r *</code>&#8221; and lead to surprises when the contents of the clipboard are pasted.</dd>
<dt><code>grab</code></dt>
<dd>Grab can be used to block the user from using any other applications.</dd>
<dt><code>menu</code></dt>
<dd>Menus can be used to cover the entire screen and to steal input from the user.</dd>
<dt><code>selection</code></dt>
<dd>See clipboard.</dd>
<dt><code>send</code></dt>
<dd>Send can be used to cause unsafe interpreters to execute commands.</dd>
<dt><code>tk</code></dt>
<dd>The tk command recreates the send command, which is unsafe.</dd>
<dt><code>tkwait</code></dt>
<dd>Tkwait can block the containing process forever</dd>
<dt><code>toplevel</code></dt>
<dd>Toplevels can be used to cover the entire screen and to steal input from the user.</dd>
<dt><code>wm</code></dt>
<dd>If toplevels are ever allowed, wm can be used to remove decorations, move windows around, etc. </dd>
</dl>
<h2>Keywords</h2>
<p>safe, application, initialization, load, main window</p>
