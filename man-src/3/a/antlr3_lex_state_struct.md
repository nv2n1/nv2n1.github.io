---
title: "antlr3_lex_state_struct(3)"
name: "antlr3_lex_state_struct"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3_lex_state_struct/"
description: "ANTLR3_LEX_STATE_struct –"
---

<p>ANTLR3_LEX_STATE_struct &#8211; </p>
<p> Structure for track lex input states as part of <code>mark()</code> and rewind() of lexer.</p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/antlr3input.h">antlr3input.h</a>&gt;</p>
<h3>Data Fields</h3>
<p><code>ANTLR3_INT32</code> <code>charPositionInLine</code><br />
 <i>The offset within the current line of the current character. </i><br />
 void * <code>currentLine</code><br />
 <i>Pointer into the input buffer where the current line started. </i><br />
 <code>ANTLR3_UINT32</code> <code>line</code><br />
 <i>The line number we are traversing in the input file. </i><br />
 void * <code>nextChar</code><br />
 <i>Pointer to the next character to be consumed from the input data This is cast to point at the encoding of the original file that was read by the functions installed as pointer in this input stream context instance at file/string/whatever load time. </i></p>
<h2>Detailed Description</h2>
<p>Structure for track lex input states as part of <code>mark()</code> and rewind() of lexer.</p>
<h2>Field Documentation</h2>
<h3><code>ANTLR3_INT32</code> <code>ANTLR3_LEX_STATE_struct::charPositionInLine</code></h3>
<p>The offset within the current line of the current character. </p>
<p> Referenced by antlr3AsciiMark(), and antlr3AsciiRewind().</p>
<h3>void* <code>ANTLR3_LEX_STATE_struct::currentLine</code></h3>
<p>Pointer into the input buffer where the current line started. </p>
<p> Referenced by antlr3AsciiMark(), and antlr3AsciiRewind().</p>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_LEX_STATE_struct::line</code></h3>
<p>The line number we are traversing in the input file. This gets incremented by a newline() call in the lexer grammer actions. </p>
<p> Referenced by antlr3AsciiMark(), and antlr3AsciiRewind().</p>
<h3>void* <code>ANTLR3_LEX_STATE_struct::nextChar</code></h3>
<p>Pointer to the next character to be consumed from the input data This is cast to point at the encoding of the original file that was read by the functions installed as pointer in this input stream context instance at file/string/whatever load time. </p>
<p> Referenced by antlr3AsciiMark(), and antlr3AsciiRewind(). </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
