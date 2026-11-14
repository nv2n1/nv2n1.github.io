---
title: "antlr3-skiptoken(3)"
name: "antlr3-skiptoken"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-skiptoken/"
description: "ANTLR3_TOKEN_SOURCE_struct –"
---

<p>ANTLR3_TOKEN_SOURCE_struct &#8211; </p>
<p> Definition of a token source, which has a pointer to a function that returns the next token (using a token factory if it is going to be efficient) and a pointer to an ANTLR3_INPUT_STREAM.</p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/antlr3tokenstream.h">antlr3tokenstream.h</a>&gt;</p>
<h3>Data Fields</h3>
<p><code>ANTLR3_COMMON_TOKEN</code> <code>eofToken</code><br />
 <i>A special pre-allocated token, which signifies End Of Tokens. </i><br />
 <code>pANTLR3_STRING</code> <code>fileName</code><br />
 <i>When the token source is constructed, it is populated with the file name from whence the tokens were produced by the lexer. </i><br />
 <code>pANTLR3_COMMON_TOKEN</code>(* <code>nextToken</code> )(struct <code>ANTLR3_TOKEN_SOURCE_struct</code> *tokenSource)<br />
 <i>Pointer to a function that returns the next token in the stream. </i><br />
 <code>ANTLR3_COMMON_TOKEN</code> <code>skipToken</code><br />
 <i>A special pre-allocated token, which is returned by </i><code>mTokens()</code> if the lexer rule said to just skip the generated token altogether.<br />
 <code>pANTLR3_STRING_FACTORY</code> <code>strFactory</code><br />
 <i>Whoever is providing tokens, needs to provide a string factory too. </i><br />
 void * <code>super</code><br />
 <i>Whatever is supplying the token source interface, needs a pointer to itself so that this pointer can be passed to it when the nextToken function is called. </i></p>
<h2>Detailed Description</h2>
<p>Definition of a token source, which has a pointer to a function that returns the next token (using a token factory if it is going to be efficient) and a pointer to an ANTLR3_INPUT_STREAM. </p>
<p> This is slightly different to the Java interface because we have no way to implement multiple interfaces without defining them in the interface structure or casting (void *), which is too convoluted.</p>
<h2>Field Documentation</h2>
<h3><code>ANTLR3_COMMON_TOKEN</code> <code>ANTLR3_TOKEN_SOURCE_struct::eofToken</code></h3>
<p>A special pre-allocated token, which signifies End Of Tokens. Because this must be set up with the current input index and so on, we embed the structure and return the address of it. It is marked as factoryMade, so that it is never attempted to be freed. </p>
<p> Referenced by antlr3LexerNew(), nextTokenStr(), setCharStream(), and tokLT().</p>
<h3><code>pANTLR3_STRING</code> <code>ANTLR3_TOKEN_SOURCE_struct::fileName</code></h3>
<p>When the token source is constructed, it is populated with the file name from whence the tokens were produced by the lexer. This pointer is a copy of the one supplied by the CharStream (and may be NULL) so should not be manipulated other than to copy or print it. </p>
<p> Referenced by setCharStream().</p>
<h3><code>pANTLR3_COMMON_TOKEN</code>(* <code>ANTLR3_TOKEN_SOURCE_struct::nextToken</code>)(struct <code>ANTLR3_TOKEN_SOURCE_struct</code> *tokenSource)</h3>
<p>Pointer to a function that returns the next token in the stream. </p>
<p> Referenced by antlr3LexerNew().</p>
<h3><code>ANTLR3_COMMON_TOKEN</code> <code>ANTLR3_TOKEN_SOURCE_struct::skipToken</code></h3>
<p>A special pre-allocated token, which is returned by <code>mTokens()</code> if the lexer rule said to just skip the generated token altogether. Having this single token stops us wasting memory by have the token factory actually create something that we are going to SKIP(); anyway. </p>
<p> Referenced by antlr3LexerNew(), and nextTokenStr().</p>
<h3><code>pANTLR3_STRING_FACTORY</code> <code>ANTLR3_TOKEN_SOURCE_struct::strFactory</code></h3>
<p>Whoever is providing tokens, needs to provide a string factory too. </p>
<p> Referenced by antlr3LexerNew(), setCharStream(), and toStringSS().</p>
<h3>void* <code>ANTLR3_TOKEN_SOURCE_struct::super</code></h3>
<p>Whatever is supplying the token source interface, needs a pointer to itself so that this pointer can be passed to it when the nextToken function is called. </p>
<p> Referenced by antlr3LexerNew(), nextToken(), and nextTokenStr(). </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
