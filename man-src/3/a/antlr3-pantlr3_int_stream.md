---
title: "antlr3-pantlr3_int_stream(3)"
name: "antlr3-pantlr3_int_stream"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-pantlr3_int_stream/"
description: "PANTLR3_INT_STREAM –"
---

<p>PANTLR3_INT_STREAM &#8211; </p>
<h3>Functions</h3>
<p>ANTLR3_API <code>pANTLR3_INT_STREAM</code> <code>antlr3IntStreamNew</code> () </p>
<p> static void <code>freeStream</code> (<code>pANTLR3_INT_STREAM</code> stream) </p>
<h2>Function Documentation</h2>
<h3>ANTLR3_API <code>pANTLR3_INT_STREAM</code> antlr3IntStreamNew (void)</h3>
<p>References ANTLR3_CALLOC, ANTLR3_INT_STREAM_struct::free, and freeStream(). </p>
<p> Referenced by antlr3CommonTokenStreamNew(), antlr3CommonTreeNodeStreamNew(), antlr3CommonTreeNodeStreamNewStream(), and antlr3GenericSetupStream().</p>
<h3>static void freeStream (<code>pANTLR3_INT_STREAM</code> stream) [static]</h3>
<p>References ANTLR3_FREE. </p>
<p> Referenced by antlr3IntStreamNew().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
