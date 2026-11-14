---
title: "antlr3baserecognizer(3)"
name: "antlr3baserecognizer"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3baserecognizer/"
description: "include/antlr3baserecognizer.h –"
---

<h2 class="name">NAME</h2>
<p> include/antlr3baserecognizer.h &#8211; </p>
<p> Defines the basic structure to support recognizing by either a lexer, parser, or tree parser.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;<a href="file:/usr/include/antlr3defs.h">antlr3defs.h</a>&gt;<br />
 #include &lt;<a href="file:/usr/include/antlr3exception.h">antlr3exception.h</a>&gt;<br />
 #include &lt;<a href="file:/usr/include/antlr3input.h">antlr3input.h</a>&gt;<br />
 #include &lt;<a href="file:/usr/include/antlr3tokenstream.h">antlr3tokenstream.h</a>&gt;<br />
 #include &lt;<a href="file:/usr/include/antlr3commontoken.h">antlr3commontoken.h</a>&gt;<br />
 #include &lt;<a href="file:/usr/include/antlr3commontreenodestream.h">antlr3commontreenodestream.h</a>&gt;<br />
 #include &lt;<a href="file:/usr/include/antlr3debugeventlistener.h">antlr3debugeventlistener.h</a>&gt;<br />
 #include &lt;<a href="file:/usr/include/antlr3recognizersharedstate.h">antlr3recognizersharedstate.h</a>&gt;<br />
 #include &lt;<a href="file:/usr/include/antlr3lexer.h">antlr3lexer.h</a>&gt;<br />
 #include &lt;<a href="file:/usr/include/antlr3parser.h">antlr3parser.h</a>&gt;<br />
 #include &lt;<a href="file:/usr/include/antlr3treeparser.h">antlr3treeparser.h</a>&gt; </p>
<h3>Data Structures</h3>
<p> struct <code>ANTLR3_BASE_RECOGNIZER_struct</code><br />
 <i>Base tracking context structure for all types of recognizers. </i></p>
<h3>Defines</h3>
<p> #define <code>ANTLR3_TYPE_LEXER</code> 0x0001<br />
 <i>Type indicator for a lexer recognizer. </i><br />
 #define <code>ANTLR3_TYPE_PARSER</code> 0x0002<br />
 <i>Type indicator for a parser recognizer. </i><br />
 #define <code>ANTLR3_TYPE_TREE_PARSER</code> 0x0004<br />
 <i>Type indicator for a tree parser recognizer. </i></p>
<h3>Typedefs</h3>
<p> typedef struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> <code>ANTLR3_BASE_RECOGNIZER</code><br />
 <i>Base tracking context structure for all types of recognizers. </i></p>
<h2>Detailed Description</h2>
<p> Defines the basic structure to support recognizing by either a lexer, parser, or tree parser. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for ANTLR3C from the source code. </p>
<h2>Index</h2>
