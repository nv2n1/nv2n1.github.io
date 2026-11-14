---
title: "tcl_findsymbol(3)"
name: "tcl_findsymbol"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_findsymbol/"
description: "Tcl_LoadFile, Tcl_FindSymbol – platform-independent dynamic library loading"
---

<p>Tcl_LoadFile, Tcl_FindSymbol &#8211; platform-independent dynamic library loading </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
int
<code>Tcl_LoadFile</code>(<i>interp, pathPtr, symbols, flags, procPtrs, loadHandlePtr</i>)
void *
<code>Tcl_FindSymbol</code>(<i>interp, loadHandle, symbol</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter to use for reporting error messages.</p>
<dd>Tcl_Obj <i>*pathPtr</i> (in) The name of the file to load. If it is a single name, the library search path of the current environment will be used to resolve it.</p>
<dd>const char *const <i>symbols[]</i> (in) Array of names of symbols to be resolved during the load of the library, or NULL if no symbols are to be resolved. If an array is given, the last entry in the array must be NULL.</p>
<dd>int <i>flags</i> (in) The value should normally be 0, but <i>TCL_LOAD_GLOBAL</i> or <i>TCL_LOAD_LAZY</i> or a combination of those two is allowed as well.</p>
<dd>void <i>*procPtrs</i> (out) Points to an array that will hold the addresses of the functions described in the <i>symbols</i> argument. Should be NULL if no symbols are to be resolved.</p>
<dd>Tcl_LoadHandle <i>*loadHandlePtr</i> (out) Points to a variable that will hold the handle to the abstract token describing the library that has been loaded.</p>
<dd>Tcl_LoadHandle <i>loadHandle</i> (in) Abstract token describing the library to look up a symbol in.</p>
<dd>const char <i>*symbol</i> (in) The name of the symbol to look up.
</dl>
<h2>Description</h2>
<p><code>Tcl_LoadFile</code> loads a file from the filesystem (including potentially any virtual filesystem that has been installed) and provides a handle to it that may be used in further operations. The <i>symbols</i> array, if non-NULL, supplies a set of names of symbols (typically functions) that must be resolved from the library and which will be stored in the array indicated by <i>procPtrs</i>. If any of the symbols is not resolved, the loading of the file will fail with an error message left in the interpreter (if that is non-NULL). The result of <code>Tcl_LoadFile</code> is a standard Tcl error code. The library may be unloaded with <code>Tcl_FSUnloadFile</code>. </p>
<p> <code>Tcl_FindSymbol</code> locates a symbol in a loaded library and returns it. If the symbol cannot be found, it returns NULL and sets an error message in the given <i>interp</i> (if that is non-NULL). Note that it is unsafe to use this operation on a handle that has been passed to <code>Tcl_FSUnloadFile</code>.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-tcl_fsloadfile/">Tcl_FSLoadFile</a>(3), <a href="/docs/linux/man/3-tcl_fsunloadfile/">Tcl_FSUnloadFile</a>(3), <a href="/docs/linux/man/n-load/">load</a>(n), <a href="/docs/linux/man/n-unload/">unload</a>(n)</p>
<h2>Keywords</h2>
<p>binary code, loading, shared library</p>
