---
title: "antlr3_token_down(3)"
name: "antlr3_token_down"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3_token_down/"
description: "include/antlr3commontoken.h –"
---

<p>include/antlr3commontoken.h &#8211; </p>
<p> Defines the interface for a common token.</p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/antlr3defs.h">antlr3defs.h</a>&gt; </p>
<h3>Data Structures</h3>
<p>struct <code>ANTLR3_COMMON_TOKEN_struct</code><br />
 <i>The definition of an ANTLR3 common token structure, which all implementations of a token stream should provide, installing any further structures in the custom pointer element of this structure. </i><br />
 struct <code>ANTLR3_TOKEN_FACTORY_struct</code><br />
 <i>ANTLR3 Token factory interface to create lots of tokens efficiently rather than creating and freeing lots of little bits of memory. </i></p>
<h3>Defines</h3>
<p>#define <code>ANTLR3_EOR_TOKEN_TYPE</code> 1 </p>
<p> #define <code>ANTLR3_FACTORY_POOL_SIZE</code> 1024<br />
 <i>How many tokens to allocate at once in the token factory. </i><br />
 #define <code>ANTLR3_MIN_TOKEN_TYPE</code> ANTLR3_TOKEN_UP + 1<br />
 <i>First token that can be used by users/generated code. </i><br />
 #define <code>ANTLR3_TEXT_CHARP</code> 1 </p>
<p> #define <code>ANTLR3_TEXT_NONE</code> 0 </p>
<p> #define <code>ANTLR3_TEXT_STRING</code> 2 </p>
<p> #define <code>ANTLR3_TOKEN_DEFAULT_CHANNEL</code> 0<br />
 <i>Default channel for a token. </i><br />
 #define <code>ANTLR3_TOKEN_DOWN</code> 2<br />
 <i>Imaginary token type to cause a traversal of child nodes in a tree parser. </i><br />
 #define <code>ANTLR3_TOKEN_EOF</code> (ANTLR3_CHARSTREAM_EOF &amp; 0xFFFFFFFF)<br />
 <i>End of file token. </i><br />
 #define <code>ANTLR3_TOKEN_INVALID</code> 0<br />
 <i>Indicator of an invalid token. </i><br />
 #define <code>ANTLR3_TOKEN_UP</code> 3<br />
 <i>Imaginary token type to signal the end of a stream of child nodes. </i><br />
 #define <code>HIDDEN</code> 99<br />
 <i>Reserved channel number for a HIDDEN token &#8211; a token that is hidden from the parser. </i></p>
<h3>Typedefs</h3>
<p>typedef struct <code>ANTLR3_COMMON_TOKEN_struct</code> <code>ANTLR3_COMMON_TOKEN</code><br />
 <i>The definition of an ANTLR3 common token structure, which all implementations of a token stream should provide, installing any further structures in the custom pointer element of this structure. </i><br />
 typedef struct <code>ANTLR3_TOKEN_FACTORY_struct</code> <code>ANTLR3_TOKEN_FACTORY</code><br />
 <i>ANTLR3 Token factory interface to create lots of tokens efficiently rather than creating and freeing lots of little bits of memory. </i></p>
<h2>Detailed Description</h2>
<p>Defines the interface for a common token. </p>
<p> All token streams should provide their tokens using an instance of this common token. A custom pointer is provided, wher you may attach a further structure to enhance the common token if you feel the need to do so. The C runtime will assume that a token provides implementations of the interface functions, but all of them may be rplaced by your own implementation if you require it.</p>
<h2>Define Documentation</h2>
<h3>#define ANTLR3_EOR_TOKEN_TYPE 1</h3>
<p>Referenced by combineFollows(), mismatchIsMissingToken(), and recoverFromMismatchedElement().</p>
<h3>#define ANTLR3_FACTORY_POOL_SIZE 1024</h3>
<p>How many tokens to allocate at once in the token factory. </p>
<p> Referenced by factoryClose(), newPool(), newPoolToken(), and newPoolTree().</p>
<h3>#define ANTLR3_MIN_TOKEN_TYPE ANTLR3_TOKEN_UP + 1</h3>
<p>First token that can be used by users/generated code.</p>
<h3>#define ANTLR3_TEXT_CHARP 1</h3>
<p>Referenced by antlr3CommonTreeNodeStreamNew(), createToken(), createTokenFromToken(), getText(), and setText8().</p>
<h3>#define ANTLR3_TEXT_NONE 0</h3>
<p>Referenced by antlr3SetTokenAPI(), emit(), and setText8().</p>
<h3>#define ANTLR3_TEXT_STRING 2</h3>
<p>Referenced by createTokenFromToken(), emit(), getText(), and setText().</p>
<h3>#define ANTLR3_TOKEN_DEFAULT_CHANNEL 0</h3>
<p>Default channel for a token. </p>
<p> Referenced by antlr3CommonTokenStreamSourceNew(), antlr3SetTokenAPI(), getMissingSymbol(), nextTokenStr(), reset(), and toString().</p>
<h3>#define ANTLR3_TOKEN_DOWN 2</h3>
<p>Imaginary token type to cause a traversal of child nodes in a tree parser. </p>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), and fillBuffer().</p>
<h3>#define ANTLR3_TOKEN_EOF (ANTLR3_CHARSTREAM_EOF &amp; 0xFFFFFFFF)</h3>
<p>End of file token. </p>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), antlr3dfapredict(), antlr3LexerNew(), antlr3RecognitionExceptionNew(), consumeUntil(), consumeUntilSet(), displayRecognitionError(), getMissingSymbol(), getText(), and nextToken().</p>
<h3>#define ANTLR3_TOKEN_INVALID 0</h3>
<p>Indicator of an invalid token. </p>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), antlr3LexerNew(), antlr3SetTokenAPI(), errorNode(), recoverFromMismatchedSet(), and reset().</p>
<h3>#define ANTLR3_TOKEN_UP 3</h3>
<p>Imaginary token type to signal the end of a stream of child nodes. </p>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), and fillBuffer().</p>
<h3>#define HIDDEN 99</h3>
<p>Reserved channel number for a HIDDEN token &#8211; a token that is hidden from the parser.</p>
<h2>Typedef Documentation</h2>
<h3>typedef struct <code>ANTLR3_COMMON_TOKEN_struct</code></h3>
<p>&nbsp;<wbr>&nbsp;<wbr><code>ANTLR3_COMMON_TOKEN</code>&quot; </p>
<p> The definition of an ANTLR3 common token structure, which all implementations of a token stream should provide, installing any further structures in the custom pointer element of this structure. <code>Remarks:</code></p>
<dl COMPACT>
<dd>Token streams are in essence provided by lexers or other programs that serve as lexers.</dl>
<h3>typedef struct <code>ANTLR3_TOKEN_FACTORY_struct</code></h3>
<p>&nbsp;<wbr>&nbsp;<wbr><code>ANTLR3_TOKEN_FACTORY</code>&quot; </p>
<p> ANTLR3 Token factory interface to create lots of tokens efficiently rather than creating and freeing lots of little bits of memory.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
