---
title: "antlr3lexer(3)"
name: "antlr3lexer"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3lexer/"
description: "include/antlr3lexer.h –"
---

<h2 class="name">NAME</h2>
<p> include/antlr3lexer.h &#8211; </p>
<p> Base interface for any ANTLR3 lexer.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;<a href="file:/usr/include/antlr3defs.h">antlr3defs.h</a>&gt;<br />
 #include &lt;<a href="file:/usr/include/antlr3input.h">antlr3input.h</a>&gt;<br />
 #include &lt;<a href="file:/usr/include/antlr3commontoken.h">antlr3commontoken.h</a>&gt;<br />
 #include &lt;<a href="file:/usr/include/antlr3tokenstream.h">antlr3tokenstream.h</a>&gt;<br />
 #include &lt;<a href="file:/usr/include/antlr3baserecognizer.h">antlr3baserecognizer.h</a>&gt; </p>
<h3>Data Structures</h3>
<p> struct <code>ANTLR3_LEXER_struct</code> </p>
<h3>Defines</h3>
<p> #define <code>ANTLR3_STRING_TERMINATOR</code> 0xFFFFFFFF </p>
<h3>Typedefs</h3>
<p> typedef struct <code>ANTLR3_LEXER_struct</code> <code>ANTLR3_LEXER</code> </p>
<h2>Detailed Description</h2>
<p> Base interface for any ANTLR3 lexer. </p>
<p> An ANLTR3 lexer builds from two sets of components: </p>
<dl>
<dt>*</p>
<dd> The runtime components that provide common functionality such as traversing character streams, building tokens for output and so on.</p>
<dt>*</p>
<dd> The generated rules and struutre of the actual lexer, which call upon the runtime components.</dl>
<p> A lexer class contains a character input stream, a base recognizer interface (which it will normally implement) and a token source interface (which it also implements. The Tokensource interface is called by a token consumer (such as a parser, but in theory it can be anything that wants a set of abstract tokens in place of a raw character stream. </p>
<p> So then, we set up a lexer in a sequence akin to: </p>
<dl>
<dt>*</p>
<dd> Create a character stream (something which implements ANTLR3_INPUT_STREAM) and initialize it.</p>
<dt>*</p>
<dd> Create a lexer interface and tell it where it its input stream is. This will cause the creation of a base recognizer class, which it will override with its own implementations of some methods. The lexer creator can also then in turn override anything it likes.</p>
<dt>*</p>
<dd> The lexer token source interface is then passed to some interface that knows how to use it, byte calling for a next token.</p>
<dt>*</p>
<dd> When a next token is called, let ze lexing begin.</dl>
<h2>Define Documentation</h2>
<h3>#define ANTLR3_STRING_TERMINATOR 0xFFFFFFFF</h3>
<p> Referenced by matchs().</p>
<h2>Typedef Documentation</h2>
<h3>typedef struct <code>ANTLR3_LEXER_struct</code></h3>
<p>&nbsp;<wbr>&nbsp;<wbr><code>ANTLR3_LEXER</code>&quot;</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for ANTLR3C from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAL">Author</a></p>
<dd></dl>
