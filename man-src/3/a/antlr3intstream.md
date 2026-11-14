---
title: "antlr3intstream(3)"
name: "antlr3intstream"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3intstream/"
description: "include/antlr3intstream.h –"
---

<h2 class="name">NAME</h2>
<p> include/antlr3intstream.h &#8211; </p>
<p> Defines the the class interface for an antlr3 INTSTREAM.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;<a href="file:/usr/include/antlr3defs.h">antlr3defs.h</a>&gt;<br />
 #include &lt;<a href="file:/usr/include/antlr3commontoken.h">antlr3commontoken.h</a>&gt; </p>
<h3>Data Structures</h3>
<p> struct <code>ANTLR3_INT_STREAM_struct</code> </p>
<h3>Defines</h3>
<p> #define <code>ANTLR3_CHARSTREAM</code> 0x0001<br />
 <i>Type indicator for a character stream. </i><br />
 #define <code>ANTLR3_COMMONTREENODE</code> 0x0004<br />
 <i>Type indicator for a common tree node stream. </i><br />
 #define <code>ANTLR3_INPUT_MASK</code> 0x0007<br />
 <i>Type mask for input stream so we can switch in the above types. </i><br />
 #define <code>ANTLR3_TOKENSTREAM</code> 0x0002<br />
 <i>Type indicator for a Token stream. </i></p>
<h3>Typedefs</h3>
<p> typedef struct <code>ANTLR3_INT_STREAM_struct</code> <code>ANTLR3_INT_STREAM</code> </p>
<h2>Detailed Description</h2>
<p> Defines the the class interface for an antlr3 INTSTREAM. </p>
<p> Certain functionality (such as DFAs for instance) abstract the stream of tokens or characters in to a steam of integers. Hence this structure should be included in any stream that is able to provide the output as a stream of integers (which is anything basically. </p>
<p> There are no specific implementations of the methods in this interface in general. Though for purposes of casting and so on, it may be necesssary to implement a function with the signature in this interface which abstracts the base immplementation. In essence though the base stream provides a pointer to this interface, within which it installs its normal <code>match()</code> functions and so on. Interaces such as DFA are then passed the pANTLR3_INT_STREAM and can treat any input as an int stream. </p>
<p> For instance, a lexer implements a pANTLR3_BASE_RECOGNIZER, within which there is a pANTLR3_INT_STREAM. However, a pANTLR3_INPUT_STREAM also provides a pANTLR3_INT_STREAM, which it has constructed from it&#8217;s normal interface when it was created. This is then pointed at by the pANTLR_BASE_RECOGNIZER when it is intialized with a pANTLR3_INPUT_STREAM. </p>
<p> Similarly if a pANTLR3_BASE_RECOGNIZER is initialized with a pANTLR3_TOKEN_STREAM, then the pANTLR3_INT_STREAM is taken from the pANTLR3_TOKEN_STREAM. </p>
<p> If a pANTLR3_BASE_RECOGNIZER is initialized with a pANTLR3_TREENODE_STREAM, then guess where the pANTLR3_INT_STREAM comes from? </p>
<p> Note that because the context pointer points to the actual interface structure that is providing the ANTLR3_INT_STREAM it is defined as a (void *) in this interface. There is no direct implementation of an ANTLR3_INT_STREAM (unless someone did not understand what I was doing here =;?P</p>
<h2>Define Documentation</h2>
<h3>#define ANTLR3_CHARSTREAM 0x0001</h3>
<p> Type indicator for a character stream. <code>Remarks:</code></p>
<dl>
<dt>
<dd> if a custom stream is created but it can be treated as a char stream, then you may OR in this value to your type indicator</dl>
<p> Referenced by antlr3AsciiFileStreamNew(), antlr3GenericSetupStream(), antlr3NewAsciiStringCopyStream(), antlr3NewAsciiStringInPlaceStream(), antlr3NewUCS2StringInPlaceStream(), and antlr3RecognitionExceptionNew().</p>
<h3>#define ANTLR3_COMMONTREENODE 0x0004</h3>
<p> Type indicator for a common tree node stream. <code>Remarks:</code></p>
<dl>
<dt>
<dd> if a custom stream is created but it can be treated as a common tree node stream, then you may OR in this value to your type indicator</dl>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), antlr3CommonTreeNodeStreamNewStream(), and antlr3RecognitionExceptionNew().</p>
<h3>#define ANTLR3_INPUT_MASK 0x0007</h3>
<p> Type mask for input stream so we can switch in the above types. <code>Remarks:</code></p>
<dl>
<dt>
<dd> DO NOT USE 0x0000 as a stream type!</dl>
<p> Referenced by antlr3RecognitionExceptionNew().</p>
<h3>#define ANTLR3_TOKENSTREAM 0x0002</h3>
<p> Type indicator for a Token stream. <code>Remarks:</code></p>
<dl>
<dt>
<dd> if a custom stream is created but it can be treated as a token stream, then you may OR in this value to your type indicator</dl>
<p> Referenced by antlr3CommonTokenStreamNew(), and antlr3RecognitionExceptionNew().</p>
<h2>Typedef Documentation</h2>
<h3>typedef struct <code>ANTLR3_INT_STREAM_struct</code></h3>
<p>&nbsp;<wbr>&nbsp;<wbr><code>ANTLR3_INT_STREAM</code>&quot;</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for ANTLR3C from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAO">Author</a></p>
<dd></dl>
