---
title: "antlr3string(3)"
name: "antlr3string"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3string/"
description: "include/antlr3string.h –"
---

<h2 class="name">NAME</h2>
<p> include/antlr3string.h &#8211; </p>
<p> Simple string interface allows indiscriminate allocation of strings such that they can be allocated all over the place and released in one chunk via a string factory &#8211; saves lots of hassle in remembering what strings were allocated where.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;<a href="file:/usr/include/antlr3defs.h">antlr3defs.h</a>&gt;<br />
 #include &lt;<a href="file:/usr/include/antlr3collections.h">antlr3collections.h</a>&gt; </p>
<h3>Data Structures</h3>
<p> struct <code>ANTLR3_STRING_FACTORY_struct</code><br />
 <i>Definition of the string factory interface, which creates and tracks strings for you of various shapes and sizes. </i><br />
 struct <code>ANTLR3_STRING_struct</code><br />
 <i>Base string class tracks the allocations and provides simple string tracking functions. </i></p>
<h3>Typedefs</h3>
<p> typedef struct <code>ANTLR3_STRING_struct</code> <code>ANTLR3_STRING</code><br />
 <i>Base string class tracks the allocations and provides simple string tracking functions. </i><br />
 typedef struct <code>ANTLR3_STRING_FACTORY_struct</code> <code>ANTLR3_STRING_FACTORY</code><br />
 <i>Definition of the string factory interface, which creates and tracks strings for you of various shapes and sizes. </i></p>
<h2>Detailed Description</h2>
<p> Simple string interface allows indiscriminate allocation of strings such that they can be allocated all over the place and released in one chunk via a string factory &#8211; saves lots of hassle in remembering what strings were allocated where. </p>
<h2>Typedef Documentation</h2>
<h3>typedef struct <code>ANTLR3_STRING_struct</code></h3>
<p>&nbsp;<wbr>&nbsp;<wbr><code>ANTLR3_STRING</code>&quot; </p>
<p> Base string class tracks the allocations and provides simple string tracking functions. Mostly you can work directly on the string for things that don&#8217;t reallocate it, like strchr() etc. Perhaps someone will want to provide implementations for UTF8 and so on.</p>
<h3>typedef struct <code>ANTLR3_STRING_FACTORY_struct</code></h3>
<p>&nbsp;<wbr>&nbsp;<wbr><code>ANTLR3_STRING_FACTORY</code>&quot; </p>
<p> Definition of the string factory interface, which creates and tracks strings for you of various shapes and sizes.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for ANTLR3C from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAJ">Author</a></p>
<dd></dl>
