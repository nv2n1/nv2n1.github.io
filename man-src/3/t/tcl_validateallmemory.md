---
title: "tcl_validateallmemory(3)"
name: "tcl_validateallmemory"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_validateallmemory/"
description: "Tcl_DumpActiveMemory, Tcl_InitMemory, Tcl_ValidateAllMemory – Validated memory allocation interface"
---

<p>Tcl_DumpActiveMemory, Tcl_InitMemory, Tcl_ValidateAllMemory &#8211; Validated memory allocation interface </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
int
<code>Tcl_DumpActiveMemory</code>(<i>fileName</i>)
void
<code>Tcl_InitMemory</code>(<i>interp</i>)
void
<code>Tcl_ValidateAllMemory</code>(<i>fileName, line</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Tcl interpreter in which to add commands.</p>
<dd>const char <i>*fileName</i> (in) For <code>Tcl_DumpActiveMemory</code>, name of the file to which memory information will be written. For <code>Tcl_ValidateAllMemory</code>, name of the file from which the call is being made (normally <code>__FILE__</code>).</p>
<dd>int <i>line</i> (in) Line number at which the call to <code>Tcl_ValidateAllMemory</code> is made (normally <code>__LINE__</code>). </p>
</dl>
<h2>Description</h2>
<p>These functions provide access to Tcl memory debugging information. They are only functional when Tcl has been compiled with <code>TCL_MEM_DEBUG</code> defined at compile-time. When <code>TCL_MEM_DEBUG</code> is not defined, these functions are all no-ops. </p>
<p> <code>Tcl_DumpActiveMemory</code> will output a list of all currently allocated memory to the specified file. The information output for each allocated block of memory is: starting and ending addresses (excluding guard zone), size, source file where <code>ckalloc</code> was called to allocate the block and line number in that file. It is especially useful to call <code>Tcl_DumpActiveMemory</code> after the Tcl interpreter has been deleted. </p>
<p> <code>Tcl_InitMemory</code> adds the Tcl <code>memory</code> command to the interpreter given by <i>interp</i>. <code>Tcl_InitMemory</code> is called by <code>Tcl_Main</code>. </p>
<p> <code>Tcl_ValidateAllMemory</code> forces a validation of the guard zones of all currently allocated blocks of memory. Normally validation of a block occurs when its freed, unless full validation is enabled, in which case validation of all blocks occurs when <code>ckalloc</code> and <code>ckfree</code> are called. This function forces the validation to occur at any point. </p>
<h2>See Also</h2>
<p>TCL_MEM_DEBUG, memory </p>
<h2>Keywords</h2>
<p>memory, debug</p>
