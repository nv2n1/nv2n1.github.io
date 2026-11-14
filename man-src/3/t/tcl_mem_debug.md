---
title: "tcl_mem_debug(3)"
name: "tcl_mem_debug"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_mem_debug/"
description: "TCL_MEM_DEBUG – Compile-time flag to enable Tcl memory debugging"
---

<p>TCL_MEM_DEBUG &#8211; Compile-time flag to enable Tcl memory debugging </p>
<h2>Description</h2>
<p>When Tcl is compiled with <code>TCL_MEM_DEBUG</code> defined, a powerful set of memory debugging aids is included in the compiled binary. This includes C and Tcl functions which can aid with debugging memory leaks, memory allocation overruns, and other memory related errors.</p>
<h2>Enabling Memory Debugging</h2>
<p>To enable memory debugging, Tcl should be recompiled from scratch with <code>TCL_MEM_DEBUG</code> defined (e.g. by passing the <i>&#8211;enable-symbols=mem</i> flag to the <i>configure</i> script when building). This will also compile in a non-stub version of <code>Tcl_InitMemory</code> to add the <code>memory</code> command to Tcl. </p>
<p> <code>TCL_MEM_DEBUG</code> must be either left defined for all modules or undefined for all modules that are going to be linked together. If they are not, link errors will occur, with either <code>Tcl_DbCkfree</code> and <code>Tcl_DbCkalloc</code> or <code>Tcl_Ckalloc</code> and <code>Tcl_Ckfree</code> being undefined. </p>
<p> Once memory debugging support has been compiled into Tcl, the C functions <code>Tcl_ValidateAllMemory</code>, and <code>Tcl_DumpActiveMemory</code>, and the Tcl <code>memory</code> command can be used to validate and examine memory usage.</p>
<h2>Guard Zones</h2>
<p>When memory debugging is enabled, whenever a call to <code>ckalloc</code> is made, slightly more memory than requested is allocated so the memory debugging code can keep track of the allocated memory, and eight-byte &#8220;guard zones&#8221; are placed in front of and behind the space that will be returned to the caller. (The sizes of the guard zones are defined by the C #define <code>LOW_GUARD_SIZE</code> and #define <code>HIGH_GUARD_SIZE</code> in the file <i>generic/tclCkalloc.c</i> &#8212; it can be extended if you suspect large overwrite problems, at some cost in performance.) A known pattern is written into the guard zones and, on a call to <code>ckfree</code>, the guard zones of the space being freed are checked to see if either zone has been modified in any way. If one has been, the guard bytes and their new contents are identified, and a &#8220;low guard failed&#8221; or &#8220;high guard failed&#8221; message is issued. The &#8220;guard failed&#8221; message includes the address of the memory packet and the file name and line number of the code that called <code>ckfree</code>. This allows you to detect the common sorts of one-off problems, where not enough space was allocated to contain the data written, for example.</p>
<h2>Debugging Difficult Memory Corruption Problems</h2>
<p>Normally, Tcl compiled with memory debugging enabled will make it easy to isolate a corruption problem. Turning on memory validation with the memory command can help isolate difficult problems. If you suspect (or know) that corruption is occurring before the Tcl interpreter comes up far enough for you to issue commands, you can set <code>MEM_VALIDATE</code> define, recompile tclCkalloc.c and rebuild Tcl. This will enable memory validation from the first call to <code>ckalloc</code>, again, at a large performance impact. </p>
<p> If you are desperate and validating memory on every call to <code>ckalloc</code> and <code>ckfree</code> is not enough, you can explicitly call <code>Tcl_ValidateAllMemory</code> directly at any point. It takes a <i>char *</i> and an <i>int</i> which are normally the filename and line number of the caller, but they can actually be anything you want. Remember to remove the calls after you find the problem.</p>
<h2>See Also</h2>
<p>ckalloc, memory, Tcl_ValidateAllMemory, Tcl_DumpActiveMemory</p>
<h2>Keywords</h2>
<p>memory, debug</p>
