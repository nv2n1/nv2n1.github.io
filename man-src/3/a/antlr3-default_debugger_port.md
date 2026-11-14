---
title: "antlr3-default_debugger_port(3)"
name: "antlr3-default_debugger_port"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-default_debugger_port/"
description: "include/antlr3debugeventlistener.h –"
---

<p>include/antlr3debugeventlistener.h &#8211; </p>
<p> The definition of all debugging events that a recognizer can trigger.</p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/antlr3defs.h">antlr3defs.h</a>&gt;<br />
 #include &lt;<a href="file:/usr/include/antlr3basetree.h">antlr3basetree.h</a>&gt;<br />
 #include &lt;<a href="file:/usr/include/antlr3commontoken.h">antlr3commontoken.h</a>&gt; </p>
<h3>Data Structures</h3>
<p>struct <code>ANTLR3_DEBUG_EVENT_LISTENER_struct</code><br />
 <i>The ANTLR3 debugging interface for communicating with ANLTR Works. </i></p>
<h3>Defines</h3>
<p>#define <code>DEFAULT_DEBUGGER_PORT</code> 0xBFCC;<br />
 <i>Default debugging port. </i></p>
<h3>Typedefs</h3>
<p>typedef struct <code>ANTLR3_DEBUG_EVENT_LISTENER_struct</code> <code>ANTLR3_DEBUG_EVENT_LISTENER</code><br />
 <i>The ANTLR3 debugging interface for communicating with ANLTR Works. </i></p>
<h2>Detailed Description</h2>
<p>The definition of all debugging events that a recognizer can trigger. </p>
<p> <code>Remarks:</code></p>
<dl COMPACT>
<dd>From the java implementation by Terence Parr&#8230; I did not create a separate AST debugging interface as it would create lots of extra classes and DebugParser has a dbg var defined, which makes it hard to change to ASTDebugEventListener. I looked hard at this issue and it is easier to understand as one monolithic event interface for all possible events. Hopefully, adding ST debugging stuff won&#8217;t be bad. Leave for future. 4/26/2006.</dl>
<h2>Define Documentation</h2>
<h3>#define DEFAULT_DEBUGGER_PORT 0xBFCC;</h3>
<p>Default debugging port. </p>
<p> Referenced by antlr3DebugListenerNew().</p>
<h2>Typedef Documentation</h2>
<h3>typedef struct <code>ANTLR3_DEBUG_EVENT_LISTENER_struct</code></h3>
<p><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> <code>ANTLR3_DEBUG_EVENT_LISTENER</code>&quot;</p>
<p> The ANTLR3 debugging interface for communicating with ANLTR Works. Function comments mostly taken from the Java version.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
