---
title: "antlr3tokenstream(3)"
name: "antlr3tokenstream"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3tokenstream/"
description: "include/antlr3tokenstream.h –"
---

<h2 class="name">NAME</h2>
<p> include/antlr3tokenstream.h &#8211; </p>
<p> Defines the interface for an ANTLR3 common token stream.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;<a href="file:/usr/include/antlr3defs.h">antlr3defs.h</a>&gt;<br />
 #include &lt;<a href="file:/usr/include/antlr3string.h">antlr3string.h</a>&gt;<br />
 #include &lt;<a href="file:/usr/include/antlr3collections.h">antlr3collections.h</a>&gt;<br />
 #include &lt;<a href="file:/usr/include/antlr3input.h">antlr3input.h</a>&gt;<br />
 #include &lt;<a href="file:/usr/include/antlr3commontoken.h">antlr3commontoken.h</a>&gt;<br />
 #include &lt;<a href="file:/usr/include/antlr3bitset.h">antlr3bitset.h</a>&gt;<br />
 #include &lt;<a href="file:/usr/include/antlr3debugeventlistener.h">antlr3debugeventlistener.h</a>&gt; </p>
<h3>Data Structures</h3>
<p> struct <code>ANTLR3_COMMON_TOKEN_STREAM_struct</code><br />
 <i>Common token stream is an implementation of ANTLR_TOKEN_STREAM for the default parsers and recognizers. </i><br />
 struct <code>ANTLR3_TOKEN_SOURCE_struct</code><br />
 <i>Definition of a token source, which has a pointer to a function that returns the next token (using a token factory if it is going to be efficient) and a pointer to an ANTLR3_INPUT_STREAM. </i><br />
 struct <code>ANTLR3_TOKEN_STREAM_struct</code><br />
 <i>Definition of the ANTLR3 common token stream interface. </i></p>
<h3>Typedefs</h3>
<p> typedef struct <code>ANTLR3_COMMON_TOKEN_STREAM_struct</code> <code>ANTLR3_COMMON_TOKEN_STREAM</code><br />
 <i>Common token stream is an implementation of ANTLR_TOKEN_STREAM for the default parsers and recognizers. </i><br />
 typedef struct <code>ANTLR3_TOKEN_SOURCE_struct</code> <code>ANTLR3_TOKEN_SOURCE</code><br />
 <i>Definition of a token source, which has a pointer to a function that returns the next token (using a token factory if it is going to be efficient) and a pointer to an ANTLR3_INPUT_STREAM. </i><br />
 typedef struct <code>ANTLR3_TOKEN_STREAM_struct</code> <code>ANTLR3_TOKEN_STREAM</code><br />
 <i>Definition of the ANTLR3 common token stream interface. </i></p>
<h2>Detailed Description</h2>
<p> Defines the interface for an ANTLR3 common token stream. </p>
<p> Custom token streams should create one of these and then override any functions by installing their own pointers to implement the various functions.</p>
<h2>Typedef Documentation</h2>
<h3>typedef struct <code>ANTLR3_COMMON_TOKEN_STREAM_struct</code></h3>
<p>&nbsp;<wbr>&nbsp;<wbr><code>ANTLR3_COMMON_TOKEN_STREAM</code>&quot; </p>
<p> Common token stream is an implementation of ANTLR_TOKEN_STREAM for the default parsers and recognizers. You may of course build your own implementation if you are so inclined.</p>
<h3>typedef struct <code>ANTLR3_TOKEN_SOURCE_struct</code></h3>
<p>&nbsp;<wbr>&nbsp;<wbr><code>ANTLR3_TOKEN_SOURCE</code>&quot; </p>
<p> Definition of a token source, which has a pointer to a function that returns the next token (using a token factory if it is going to be efficient) and a pointer to an ANTLR3_INPUT_STREAM. This is slightly different to the Java interface because we have no way to implement multiple interfaces without defining them in the interface structure or casting (void *), which is too convoluted.</p>
<h3>typedef struct <code>ANTLR3_TOKEN_STREAM_struct</code></h3>
<p>&nbsp;<wbr>&nbsp;<wbr><code>ANTLR3_TOKEN_STREAM</code>&quot; </p>
<p> Definition of the ANTLR3 common token stream interface. <code>Remarks:</code></p>
<dl>
<dt>
<dd> Much of the documentation for this interface is stolen from Ter&#8217;s Java implementation.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for ANTLR3C from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAK">Author</a></p>
<dd></dl>
