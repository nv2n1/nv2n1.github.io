---
title: "antlr3recognizersharedstate(3)"
name: "antlr3recognizersharedstate"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3recognizersharedstate/"
description: "include/antlr3recognizersharedstate.h –"
---

<h2 class="name">NAME</h2>
<p> include/antlr3recognizersharedstate.h &#8211; </p>
<p> While the C runtime does not need to model the state of multiple lexers and parsers in the same way as the Java runtime does it is no overhead to reflect that model.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;<a href="file:/usr/include/antlr3defs.h">antlr3defs.h</a>&gt; </p>
<h3>Data Structures</h3>
<p> struct <code>ANTLR3_RECOGNIZER_SHARED_STATE_struct</code><br />
 <i>All the data elements required to track the current state of any recognizer (lexer, parser, tree parser). </i></p>
<h3>Typedefs</h3>
<p> typedef struct <code>ANTLR3_RECOGNIZER_SHARED_STATE_struct</code> <code>ANTLR3_RECOGNIZER_SHARED_STATE</code><br />
 <i>All the data elements required to track the current state of any recognizer (lexer, parser, tree parser). </i></p>
<h2>Detailed Description</h2>
<p> While the C runtime does not need to model the state of multiple lexers and parsers in the same way as the Java runtime does it is no overhead to reflect that model. </p>
<p> In fact the C runtime has always been able to share recognizer state. </p>
<p> This &#8216;class&#8217; therefore defines all the elements of a recognizer (either lexer, parser or tree parser) that are need to track the current recognition state. Multiple recognizers may then share this state, for instance when one grammar imports another.</p>
<h2>Typedef Documentation</h2>
<h3>typedef struct <code>ANTLR3_RECOGNIZER_SHARED_STATE_struct</code></h3>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> <code>ANTLR3_RECOGNIZER_SHARED_STATE</code>&quot;</p>
<p> All the data elements required to track the current state of any recognizer (lexer, parser, tree parser). May be share between multiple recognizers such that grammar inheritance is easily supported.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for ANTLR3C from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAI">Author</a></p>
<dd></dl>
