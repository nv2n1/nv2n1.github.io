---
title: "tcl_translatefilename(3)"
name: "tcl_translatefilename"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_translatefilename/"
description: "Tcl_TranslateFileName – convert file name to native form and replace tilde with home directory"
---

<p>Tcl_TranslateFileName &#8211; convert file name to native form and replace tilde with home directory </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
char *
<code>Tcl_TranslateFileName</code>(<i>interp</i>, <i>name</i>, <i>bufferPtr</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter in which to report an error, if any.</p>
<dd>const char <i>*name</i> (in) File name, which may start with a &#8220;~&#8221;.</p>
<dd>Tcl_DString <i>*bufferPtr</i> (in/out) If needed, this dynamic string is used to store the new file name. At the time of the call it should be uninitialized or free. The caller must eventually call <code>Tcl_DStringFree</code> to free up anything stored here. </p>
</dl>
<h2>Description</h2>
<p>This utility procedure translates a file name to a platform-specific form which, after being converted to the appropriate encoding, is suitable for passing to the local operating system. In particular, it converts network names into native form and does tilde substitution. </p>
<p> However, with the advent of the newer <code>Tcl_FSGetNormalizedPath</code> and <code>Tcl_GetNativePath</code>, there is no longer any need to use this procedure. In particular, <code>Tcl_GetNativePath</code> performs all the necessary translation and encoding conversion, is virtual-filesystem aware, and caches the native result for faster repeated calls. Finally <code>Tcl_GetNativePath</code> does not require you to free anything afterwards. </p>
<p> If <code>Tcl_TranslateFileName</code> has to do tilde substitution or translate the name then it uses the dynamic string at <i>*bufferPtr</i> to hold the new string it generates. After <code>Tcl_TranslateFileName</code> returns a non-NULL result, the caller must eventually invoke <code>Tcl_DStringFree</code> to free any information placed in <i>*bufferPtr</i>. The caller need not know whether or not <code>Tcl_TranslateFileName</code> actually used the string; <code>Tcl_TranslateFileName</code> initializes <i>*bufferPtr</i> even if it does not use it, so the call to <code>Tcl_DStringFree</code> will be safe in either case. </p>
<p> If an error occurs (e.g. because there was no user by the given name) then NULL is returned and an error message will be left in the interpreter&#8217;s result. When an error occurs, <code>Tcl_TranslateFileName</code> frees the dynamic string itself so that the caller need not call <code>Tcl_DStringFree</code>. </p>
<p> The caller is responsible for making sure that the interpreter&#8217;s result has its default empty value when <code>Tcl_TranslateFileName</code> is invoked. </p>
<h2>See Also</h2>
<p>filename </p>
<h2>Keywords</h2>
<p>file name, home directory, tilde, translate, user</p>
