---
title: "antlr3-charposition(3)"
name: "antlr3-charposition"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-charposition/"
description: "ANTLR3_COMMON_TOKEN_struct –"
---

<p>ANTLR3_COMMON_TOKEN_struct &#8211; </p>
<p> The definition of an ANTLR3 common token structure, which all implementations of a token stream should provide, installing any further structures in the custom pointer element of this structure.</p>
<h2>Synopsis</h2>
<p> #include &lt;<a href="file:/usr/include/antlr3commontoken.h">antlr3commontoken.h</a>&gt;</p>
<h3>Data Fields</h3>
<p> <code>ANTLR3_UINT32</code> <code>channel</code><br />
 <i>The virtual channel that this token exists in. </i><br />
 <code>ANTLR3_INT32</code> <code>charPosition</code><br />
 <i>The character position in the line that this token was derived from. </i><br />
 void * <code>custom</code><br />
 <i>Pointer to a custom element that the ANTLR3 programmer may define and install. </i><br />
 <code>ANTLR3_BOOLEAN</code> <code>factoryMade</code><br />
 <i>Indicates that a token was produced from the token factory and therefore the the freeToken() method should not do anything itself because token factory is responsible for deleting it. </i><br />
 void(* <code>freeCustom</code> )(void *<code>custom</code>)<br />
 <i>Pointer to a function that knows how to free the custom structure when the token is destroyed. </i><br />
 <code>ANTLR3_UINT32</code>(* <code>getChannel</code> )(struct <code>ANTLR3_COMMON_TOKEN_struct</code> *token)<br />
 <i>Pointer to a function that gets the channel that this token was placed in (parsers can &#8216;tune&#8217; to these channels. </i><br />
 <code>ANTLR3_INT32</code>(* <code>getCharPositionInLine</code> )(struct <code>ANTLR3_COMMON_TOKEN_struct</code> *token)<br />
 <i>Pointer to a function that gets the offset in the line where this token exists. </i><br />
 <code>ANTLR3_UINT32</code>(* <code>getLine</code> )(struct <code>ANTLR3_COMMON_TOKEN_struct</code> *token)<br />
 <i>Pointer to a function that gets the &#8216;line&#8217; number where this token resides. </i><br />
 <code>ANTLR3_MARKER</code>(* <code>getStartIndex</code> )(struct <code>ANTLR3_COMMON_TOKEN_struct</code> *token)<br />
 <i>Pointer to a function that gets the start index in the input stream for this token. </i><br />
 <code>ANTLR3_MARKER</code>(* <code>getStopIndex</code> )(struct <code>ANTLR3_COMMON_TOKEN_struct</code> *token)<br />
 <i>Pointer to a function that gets the stop index in the input stream for this token. </i><br />
 <code>pANTLR3_STRING</code>(* <code>getText</code> )(struct <code>ANTLR3_COMMON_TOKEN_struct</code> *token)<br />
 <i>Pointer to function that returns the text pointer of a token, use </i><code>toString()</code> if you want a pANTLR3_STRING version of the token.<br />
 <code>ANTLR3_MARKER</code>(* <code>getTokenIndex</code> )(struct <code>ANTLR3_COMMON_TOKEN_struct</code> *token)<br />
 <i>Pointer to a function that returns an index 0&#8230;n-1 of the token in the token input stream. </i><br />
 <code>ANTLR3_UINT32</code>(* <code>getType</code> )(struct <code>ANTLR3_COMMON_TOKEN_struct</code> *token)<br />
 <i>Pointer to a function that returns the token type of this token. </i><br />
 <code>ANTLR3_MARKER</code> <code>index</code><br />
 <i>What the index of this token is, 0, 1, . </i><br />
 <code>pANTLR3_INPUT_STREAM</code> <code>input</code><br />
 <i>Pointer to the input stream that this token originated in. </i><br />
 <code>ANTLR3_UINT32</code> <code>line</code><br />
 <i>The line number in the input stream where this token was derived from. </i><br />
 void * <code>lineStart</code><br />
 <i>The offset into the input stream that the line in which this token resides starts. </i><br />
 void(* <code>setChannel</code> )(struct <code>ANTLR3_COMMON_TOKEN_struct</code> *token, <code>ANTLR3_UINT32</code> <code>channel</code>)<br />
 <i>Pointer to a function that sets the channel that this token should belong to. </i><br />
 void(* <code>setCharPositionInLine</code> )(struct <code>ANTLR3_COMMON_TOKEN_struct</code> *token, <code>ANTLR3_INT32</code> pos)<br />
 <i>Pointer to a function that sets the offset in the line where this token exists. </i><br />
 void(* <code>setLine</code> )(struct <code>ANTLR3_COMMON_TOKEN_struct</code> *token, <code>ANTLR3_UINT32</code> <code>line</code>)<br />
 <i>Pointer to a function that sets the &#8216;line&#8217; number where this token reside. </i><br />
 void(* <code>setStartIndex</code> )(struct <code>ANTLR3_COMMON_TOKEN_struct</code> *token, <code>ANTLR3_MARKER</code> <code>index</code>)<br />
 <i>Pointer to a function that sets the start index in the input stream for this token. </i><br />
 void(* <code>setStopIndex</code> )(struct <code>ANTLR3_COMMON_TOKEN_struct</code> *token, <code>ANTLR3_MARKER</code> <code>index</code>)<br />
 <i>Pointer to a function that sets the stop index in the input stream for this token. </i><br />
 void(* <code>setText</code> )(struct <code>ANTLR3_COMMON_TOKEN_struct</code> *token, <code>pANTLR3_STRING</code> <code>text</code>)<br />
 <i>Pointer to a function that &#8216;might&#8217; be able to set the text associated with a token. </i><br />
 void(* <code>setText8</code> )(struct <code>ANTLR3_COMMON_TOKEN_struct</code> *token, <code>pANTLR3_UINT8</code> <code>text</code>)<br />
 <i>Pointer to a function that &#8216;might&#8217; be able to set the text associated with a token. </i><br />
 void(* <code>setTokenIndex</code> )(struct <code>ANTLR3_COMMON_TOKEN_struct</code> *token, <code>ANTLR3_MARKER</code>)<br />
 <i>Pointer to a function that can set the token index of this token in the token input stream. </i><br />
 void(* <code>setType</code> )(struct <code>ANTLR3_COMMON_TOKEN_struct</code> *token, <code>ANTLR3_UINT32</code> ttype)<br />
 <i>Pointer to a function that sets the type of this token. </i><br />
 <code>ANTLR3_MARKER</code> <code>start</code><br />
 <i>The character offset in the input stream where the text for this token starts. </i><br />
 <code>ANTLR3_MARKER</code> <code>stop</code><br />
 <i>The character offset in the input stream where the text for this token stops. </i><br />
 <code>pANTLR3_STRING_FACTORY</code> <code>strFactory</code><br />
 <i>A string factory that we can use if we ever need the text of a token and need to manufacture a pANTLR3_STRING. </i><br />
 <code>ANTLR3_UINT32</code> <code>textState</code><br />
 <i>Indicates whether this token is carrying:. </i><br />
 union { </p>
<p> <code>pANTLR3_UCHAR</code> <code>chars</code><br />
 <i>Pointer that is used when the token just has a pointer to a char *, such as when a rewrite of an imaginary token supplies a string in the grammar. </i><br />
 <code>pANTLR3_STRING</code> <code>text</code><br />
 <i>Some token types actually do carry around their associated text, hence (*getText)() will return this pointer if it is not NULL. </i><br />
 } <code>tokText</code> </p>
<p> <code>pANTLR3_STRING</code>(* <code>toString</code> )(struct <code>ANTLR3_COMMON_TOKEN_struct</code> *token)<br />
 <i>Pointer to a function that returns this token as a text representation that can be printed with embedded control codes such as </i> </p>
<p>&nbsp;<wbr>replaced with the printable sequence&nbsp;<wbr>&#8216;\n&#8217;&nbsp;<wbr>This also yields a string structure that can be used more easily than the pointer to the input stream in certain situations.&nbsp;<wbr>&quot;<br />
 <code>ANTLR3_UINT32</code> <code>type</code><br />
 <i>The actual type of this token. </i><br />
 <code>ANTLR3_UINT32</code> <code>user1</code><br />
 <i>Because it is a bit more of a hassle to override an ANTLR3_COMMON_TOKEN as the standard structure for a token, a number of user programmable elements are allowed in a token. </i><br />
 <code>ANTLR3_UINT32</code> <code>user2</code><br />
 <i>Because it is a bit more of a hassle to override an ANTLR3_COMMON_TOKEN as the standard structure for a token, a number of user programmable elements are allowed in a token. </i><br />
 <code>ANTLR3_UINT32</code> <code>user3</code><br />
 <i>Because it is a bit more of a hassle to override an ANTLR3_COMMON_TOKEN as the standard structure for a token, a number of user programmable elements are allowed in a token. </i></p>
<h2>Detailed Description</h2>
<p> The definition of an ANTLR3 common token structure, which all implementations of a token stream should provide, installing any further structures in the custom pointer element of this structure. </p>
<p> <code>Remarks:</code></p>
<dl COMPACT>
<dt>
<dd> Token streams are in essence provided by lexers or other programs that serve as lexers.</dl>
<h2>Field Documentation</h2>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_COMMON_TOKEN_struct::channel</code></h3>
<p> The virtual channel that this token exists in. </p>
<p> Referenced by antlr3SetTokenAPI(), emit(), getChannel(), and setChannel().</p>
<h3><code>ANTLR3_INT32</code> <code>ANTLR3_COMMON_TOKEN_struct::charPosition</code></h3>
<p> The character position in the line that this token was derived from. </p>
<p> Referenced by emit(), getCharPositionInLine(), and setCharPositionInLine().</p>
<h3><code>pANTLR3_UCHAR</code> <code>ANTLR3_COMMON_TOKEN_struct::chars</code></h3>
<p> Pointer that is used when the token just has a pointer to a char *, such as when a rewrite of an imaginary token supplies a string in the grammar. No sense in constructing a pANTLR3_STRING just for that, as mostly the text will not be accessed &#8211; if it is, then we will build a pANTLR3_STRING for it a that point. </p>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), createToken(), createTokenFromToken(), getText(), and setText8().</p>
<h3>void* <code>ANTLR3_COMMON_TOKEN_struct::custom</code></h3>
<p> Pointer to a custom element that the ANTLR3 programmer may define and install. </p>
<p> Referenced by antlr3SetTokenAPI(), emit(), factoryClose(), and getMissingSymbol().</p>
<h3><code>ANTLR3_BOOLEAN</code> <code>ANTLR3_COMMON_TOKEN_struct::factoryMade</code></h3>
<p> Indicates that a token was produced from the token factory and therefore the the freeToken() method should not do anything itself because token factory is responsible for deleting it. </p>
<p> Referenced by antlr3LexerNew(), antlr3TokenFactoryNew(), newPoolToken(), newToken(), and nextTokenStr().</p>
<h3>void(* <code>ANTLR3_COMMON_TOKEN_struct::freeCustom</code>)(void *<code>custom</code>)</h3>
<p> Pointer to a function that knows how to free the custom structure when the token is destroyed. </p>
<p> Referenced by antlr3SetTokenAPI(), and factoryClose().</p>
<h3><code>ANTLR3_UINT32</code>(* <code>ANTLR3_COMMON_TOKEN_struct::getChannel</code>)(struct <code>ANTLR3_COMMON_TOKEN_struct</code> *token)</h3>
<p> Pointer to a function that gets the channel that this token was placed in (parsers can &#8216;tune&#8217; to these channels. </p>
<p> Referenced by antlr3SetTokenAPI(), createTokenFromToken(), serializeToken(), and toString().</p>
<h3><code>ANTLR3_INT32</code>(* <code>ANTLR3_COMMON_TOKEN_struct::getCharPositionInLine</code>)(struct <code>ANTLR3_COMMON_TOKEN_struct</code> *token)</h3>
<p> Pointer to a function that gets the offset in the line where this token exists. </p>
<p> Referenced by antlr3SetTokenAPI(), createTokenFromToken(), getCharPositionInLine(), getMissingSymbol(), serializeNode(), serializeToken(), and toString().</p>
<h3><code>ANTLR3_UINT32</code>(* <code>ANTLR3_COMMON_TOKEN_struct::getLine</code>)(struct <code>ANTLR3_COMMON_TOKEN_struct</code> *token)</h3>
<p> Pointer to a function that gets the &#8216;line&#8217; number where this token resides. </p>
<p> Referenced by antlr3SetTokenAPI(), createTokenFromToken(), getLine(), getMissingSymbol(), serializeNode(), serializeToken(), and toString().</p>
<h3><code>ANTLR3_MARKER</code>(* <code>ANTLR3_COMMON_TOKEN_struct::getStartIndex</code>)(struct <code>ANTLR3_COMMON_TOKEN_struct</code> *token)</h3>
<p> Pointer to a function that gets the start index in the input stream for this token. </p>
<p> Referenced by antlr3SetTokenAPI(), getText(), and toString().</p>
<h3><code>ANTLR3_MARKER</code>(* <code>ANTLR3_COMMON_TOKEN_struct::getStopIndex</code>)(struct <code>ANTLR3_COMMON_TOKEN_struct</code> *token)</h3>
<p> Pointer to a function that gets the stop index in the input stream for this token. </p>
<p> Referenced by antlr3SetTokenAPI(), getText(), and toString().</p>
<h3><code>pANTLR3_STRING</code>(* <code>ANTLR3_COMMON_TOKEN_struct::getText</code>)(struct <code>ANTLR3_COMMON_TOKEN_struct</code> *token)</h3>
<p> Pointer to function that returns the text pointer of a token, use <code>toString()</code> if you want a pANTLR3_STRING version of the token. </p>
<p> Referenced by antlr3SetTokenAPI(), createTokenFromToken(), getMissingSymbol(), serializeToken(), toString(), and toStringSS().</p>
<h3><code>ANTLR3_MARKER</code>(* <code>ANTLR3_COMMON_TOKEN_struct::getTokenIndex</code>)(struct <code>ANTLR3_COMMON_TOKEN_struct</code> *token)</h3>
<p> Pointer to a function that returns an index 0&#8230;n-1 of the token in the token input stream. </p>
<p> Referenced by antlr3SetTokenAPI(), createTokenFromToken(), dbgSetTokenBoundaries(), serializeToken(), setTokenBoundaries(), toString(), and toStringTT().</p>
<h3><code>ANTLR3_UINT32</code>(* <code>ANTLR3_COMMON_TOKEN_struct::getType</code>)(struct <code>ANTLR3_COMMON_TOKEN_struct</code> *token)</h3>
<p> Pointer to a function that returns the token type of this token. </p>
<p> Referenced by antlr3SetTokenAPI(), createTokenFromToken(), getMissingSymbol(), getTokensSet(), getType(), and serializeToken().</p>
<h3><code>ANTLR3_MARKER</code> <code>ANTLR3_COMMON_TOKEN_struct::index</code></h3>
<p> What the index of this token is, 0, 1, . ., n-2, n-1 tokens </p>
<p> Referenced by antlr3SetTokenAPI(), getTokenIndex(), and setTokenIndex().</p>
<h3><code>pANTLR3_INPUT_STREAM</code> <code>ANTLR3_COMMON_TOKEN_struct::input</code></h3>
<p> Pointer to the input stream that this token originated in. </p>
<p> Referenced by antlr3RecognitionExceptionNew(), antlr3SetTokenAPI(), createToken(), getMissingSymbol(), getStartIndex(), getText(), newPoolToken(), and setInputStream().</p>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_COMMON_TOKEN_struct::line</code></h3>
<p> The line number in the input stream where this token was derived from. </p>
<p> Referenced by antlr3SetTokenAPI(), emit(), getLine(), and setLine().</p>
<h3>void* <code>ANTLR3_COMMON_TOKEN_struct::lineStart</code></h3>
<p> The offset into the input stream that the line in which this token resides starts. </p>
<p> Referenced by emit(), and getMissingSymbol().</p>
<h3>void(* <code>ANTLR3_COMMON_TOKEN_struct::setChannel</code>)(struct <code>ANTLR3_COMMON_TOKEN_struct</code> *token, <code>ANTLR3_UINT32</code> <code>channel</code>)</h3>
<p> Pointer to a function that sets the channel that this token should belong to. </p>
<p> Referenced by antlr3SetTokenAPI(), createTokenFromToken(), and getMissingSymbol().</p>
<h3>void(* <code>ANTLR3_COMMON_TOKEN_struct::setCharPositionInLine</code>)(struct <code>ANTLR3_COMMON_TOKEN_struct</code> *token, <code>ANTLR3_INT32</code> pos)</h3>
<p> Pointer to a function that sets the offset in the line where this token exists. </p>
<p> Referenced by antlr3SetTokenAPI(), createTokenFromToken(), and getMissingSymbol().</p>
<h3>void(* <code>ANTLR3_COMMON_TOKEN_struct::setLine</code>)(struct <code>ANTLR3_COMMON_TOKEN_struct</code> *token, <code>ANTLR3_UINT32</code> <code>line</code>)</h3>
<p> Pointer to a function that sets the &#8216;line&#8217; number where this token reside. </p>
<p> Referenced by antlr3SetTokenAPI(), createTokenFromToken(), getMissingSymbol(), and nextTokenStr().</p>
<h3>void(* <code>ANTLR3_COMMON_TOKEN_struct::setStartIndex</code>)(struct <code>ANTLR3_COMMON_TOKEN_struct</code> *token, <code>ANTLR3_MARKER</code> <code>index</code>)</h3>
<p> Pointer to a function that sets the start index in the input stream for this token. </p>
<p> Referenced by antlr3SetTokenAPI(), nextTokenStr(), and tokLT().</p>
<h3>void(* <code>ANTLR3_COMMON_TOKEN_struct::setStopIndex</code>)(struct <code>ANTLR3_COMMON_TOKEN_struct</code> *token, <code>ANTLR3_MARKER</code> <code>index</code>)</h3>
<p> Pointer to a function that sets the stop index in the input stream for this token. </p>
<p> Referenced by antlr3SetTokenAPI(), nextTokenStr(), and tokLT().</p>
<h3>void(* <code>ANTLR3_COMMON_TOKEN_struct::setText</code>)(struct <code>ANTLR3_COMMON_TOKEN_struct</code> *token, <code>pANTLR3_STRING</code> <code>text</code>)</h3>
<p> Pointer to a function that &#8216;might&#8217; be able to set the text associated with a token. Imaginary tokens such as an ANTLR3_CLASSIC_TOKEN may actually do this, however many tokens such as ANTLR3_COMMON_TOKEN do not actaully have strings associated with them but just point into the current input stream. These tokens will implement this function with a function that errors out (probably drastically. </p>
<p> Referenced by antlr3SetTokenAPI().</p>
<h3>void(* <code>ANTLR3_COMMON_TOKEN_struct::setText8</code>)(struct <code>ANTLR3_COMMON_TOKEN_struct</code> *token, <code>pANTLR3_UINT8</code> <code>text</code>)</h3>
<p> Pointer to a function that &#8216;might&#8217; be able to set the text associated with a token. Imaginary tokens such as an ANTLR3_CLASSIC_TOKEN may actually do this, however many tokens such as ANTLR3_COMMON_TOKEN do not actully have strings associated with them but just point into the current input stream. These tokens will implement this function with a function that errors out (probably drastically. </p>
<p> Referenced by antlr3SetTokenAPI(), createTypeTokenText(), and getMissingSymbol().</p>
<h3>void(* <code>ANTLR3_COMMON_TOKEN_struct::setTokenIndex</code>)(struct <code>ANTLR3_COMMON_TOKEN_struct</code> *token, <code>ANTLR3_MARKER</code>)</h3>
<p> Pointer to a function that can set the token index of this token in the token input stream. </p>
<p> Referenced by antlr3SetTokenAPI(), and createTokenFromToken().</p>
<h3>void(* <code>ANTLR3_COMMON_TOKEN_struct::setType</code>)(struct <code>ANTLR3_COMMON_TOKEN_struct</code> *token, <code>ANTLR3_UINT32</code> ttype)</h3>
<p> Pointer to a function that sets the type of this token. </p>
<p> Referenced by antlr3CommonTokenNew(), antlr3LexerNew(), antlr3SetTokenAPI(), createToken(), createTokenFromToken(), createTypeToken(), createTypeTokenText(), and getMissingSymbol().</p>
<h3><code>ANTLR3_MARKER</code> <code>ANTLR3_COMMON_TOKEN_struct::start</code></h3>
<p> The character offset in the input stream where the text for this token starts. </p>
<p> Referenced by antlr3SetTokenAPI(), emit(), getStartIndex(), and setStartIndex().</p>
<h3><code>ANTLR3_MARKER</code> <code>ANTLR3_COMMON_TOKEN_struct::stop</code></h3>
<p> The character offset in the input stream where the text for this token stops. </p>
<p> Referenced by antlr3SetTokenAPI(), emit(), getStopIndex(), and setStopIndex().</p>
<h3><code>pANTLR3_STRING_FACTORY</code> <code>ANTLR3_COMMON_TOKEN_struct::strFactory</code></h3>
<p> A string factory that we can use if we ever need the text of a token and need to manufacture a pANTLR3_STRING. </p>
<p> Referenced by ANTLR3_TREE_ADAPTORNew(), antlr3CommonTreeNodeStreamNew(), antlr3CommonTreeNodeStreamNewStream(), antlr3LexerNew(), createToken(), getText(), newPoolToken(), setCharStream(), and setInputStream().</p>
<h3><code>pANTLR3_STRING</code> <code>ANTLR3_COMMON_TOKEN_struct::text</code></h3>
<p> Some token types actually do carry around their associated text, hence (*getText)() will return this pointer if it is not NULL. </p>
<p> Referenced by createTokenFromToken(), emit(), getText(), setText(), and setText8().</p>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_COMMON_TOKEN_struct::textState</code></h3>
<p> Indicates whether this token is carrying:. State | Meaning &#8212;&#8212;+&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8211; 0 | Nothing (neither rewrite text, nor setText) 1 | char * to user supplied rewrite text 2 | pANTLR3_STRING because of setText or similar action </p>
<p> Affects the union structure tokText below (uses 32 bit so alignment is always good) </p>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), antlr3SetTokenAPI(), createToken(), createTokenFromToken(), emit(), getText(), setText(), and setText8().</p>
<h3>union { &#8230; }</h3>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> <code>ANTLR3_COMMON_TOKEN_struct::tokText</code>&quot;</p>
<p> Referenced by antlr3CommonTreeNodeStreamNew(), createToken(), createTokenFromToken(), emit(), getText(), setText(), and setText8().</p>
<h3><code>pANTLR3_STRING</code>(* <code>ANTLR3_COMMON_TOKEN_struct::toString</code>)(struct <code>ANTLR3_COMMON_TOKEN_struct</code> *token)</h3>
<p> Pointer to a function that returns this token as a text representation that can be printed with embedded control codes such as </p>
<p>&nbsp;<wbr>replaced with the printable sequence&nbsp;<wbr>&#8216;\n&#8217;&nbsp;<wbr>This also yields a string structure that can be used more easily than the pointer to the input stream in certain situations.&nbsp;<wbr> </p>
<p> Referenced by antlr3SetTokenAPI(), createTokenFromToken(), and displayRecognitionError().</p>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_COMMON_TOKEN_struct::type</code></h3>
<p> The actual type of this token. </p>
<p> Referenced by antlr3SetTokenAPI(), displayRecognitionError(), emit(), getText(), getType(), nextToken(), setType(), and toString().</p>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_COMMON_TOKEN_struct::user1</code></h3>
<p> Because it is a bit more of a hassle to override an ANTLR3_COMMON_TOKEN as the standard structure for a token, a number of user programmable elements are allowed in a token. This is one of them. </p>
<p> Referenced by antlr3SetTokenAPI(), emit(), and getMissingSymbol().</p>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_COMMON_TOKEN_struct::user2</code></h3>
<p> Because it is a bit more of a hassle to override an ANTLR3_COMMON_TOKEN as the standard structure for a token, a number of user programmable elements are allowed in a token. This is one of them. </p>
<p> Referenced by antlr3SetTokenAPI(), emit(), and getMissingSymbol().</p>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_COMMON_TOKEN_struct::user3</code></h3>
<p> Because it is a bit more of a hassle to override an ANTLR3_COMMON_TOKEN as the standard structure for a token, a number of user programmable elements are allowed in a token. This is one of them. </p>
<p> Referenced by antlr3SetTokenAPI(), emit(), and getMissingSymbol(). </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for ANTLR3C from the source code.</p>
