---
title: "antlr3-ctx(3)"
name: "antlr3-ctx"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-ctx/"
description: "ANTLR3_LEXER_struct –"
---

<h2 class="name">NAME</h2>
<p> ANTLR3_LEXER_struct &#8211; </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;<a href="file:/usr/include/antlr3lexer.h">antlr3lexer.h</a>&gt;</p>
<h3>Data Fields</h3>
<p> void * <code>ctx</code><br />
 <i>A generated lexer has an </i><code>mTokens()</code> function, which needs the context pointer of the generated lexer, not the base lexer interface this is stored here and initialized by the generated code (or manually if this is a manually built lexer.<br />
 <code>pANTLR3_COMMON_TOKEN</code>(* <code>emit</code> )(struct <code>ANTLR3_LEXER_struct</code> *lexer)<br />
 <i>Pointer to a function that constructs a new token from the lexer stored information. </i><br />
 void(* <code>emitNew</code> )(struct <code>ANTLR3_LEXER_struct</code> *lexer, <code>pANTLR3_COMMON_TOKEN</code> token)<br />
 <i>Pointer to a function that emits the supplied token as the next token in the stream. </i><br />
 void(* <code>free</code> )(struct <code>ANTLR3_LEXER_struct</code> *lexer)<br />
 <i>Pointer to a function that knows how to free the resources of a lexer. </i><br />
 <code>ANTLR3_MARKER</code>(* <code>getCharIndex</code> )(struct <code>ANTLR3_LEXER_struct</code> *lexer) </p>
<p> <code>ANTLR3_UINT32</code>(* <code>getCharPositionInLine</code> )(struct <code>ANTLR3_LEXER_struct</code> *lexer) </p>
<p> <code>ANTLR3_UINT32</code>(* <code>getLine</code> )(struct <code>ANTLR3_LEXER_struct</code> *lexer)<br />
 <i>Pointer to function to return the current line number in the input stream. </i><br />
 <code>pANTLR3_STRING</code>(* <code>getText</code> )(struct <code>ANTLR3_LEXER_struct</code> *lexer)<br />
 <i>Pointer to function to return the text so far for the current token being generated. </i><br />
 <code>pANTLR3_INPUT_STREAM</code> <code>input</code><br />
 <i>A pointer to the character stream whence this lexer is receiving characters. </i><br />
 void(* <code>matchAny</code> )(struct <code>ANTLR3_LEXER_struct</code> *lexer)<br />
 <i>Pointer to a function that matches the next token/char in the input stream regardless of what it actaully is. </i><br />
 <code>ANTLR3_BOOLEAN</code>(* <code>matchc</code> )(struct <code>ANTLR3_LEXER_struct</code> *lexer, <code>ANTLR3_UCHAR</code> c)<br />
 <i>Pointer to a function that matches and consumes the specified character from the input stream. </i><br />
 <code>ANTLR3_BOOLEAN</code>(* <code>matchRange</code> )(struct <code>ANTLR3_LEXER_struct</code> *lexer, <code>ANTLR3_UCHAR</code> low, <code>ANTLR3_UCHAR</code> high)<br />
 <i>Pointer to a function that matches any character in the supplied range (I suppose it could be a token range too but this would only be useful if the tokens were in tsome guaranteed order which is only going to happen with a hand crafted token set). </i><br />
 <code>ANTLR3_BOOLEAN</code>(* <code>matchs</code> )(struct <code>ANTLR3_LEXER_struct</code> *lexer, <code>ANTLR3_UCHAR</code> *string)<br />
 <i>Pointer to a function that attempts to match and consume the specified string from the input stream. </i><br />
 void(* <code>mTokens</code> )(void *<code>ctx</code>)<br />
 <i>Pointer to the user provided (either manually or through code generation function that causes the lexer rules to run the lexing rules and produce the next token if there iss one. </i><br />
 void(* <code>popCharStream</code> )(struct <code>ANTLR3_LEXER_struct</code> *lexer)<br />
 <i>Pointer to a function that abandons the current input stream, whether it is empty or not and reverts to the previous stacked input stream. </i><br />
 void(* <code>pushCharStream</code> )(struct <code>ANTLR3_LEXER_struct</code> *lexer, <code>pANTLR3_INPUT_STREAM</code> <code>input</code>)<br />
 <i>Pointer to a function that switches the current character input stream to a new one, saving the old one, which we will revert to at the end of this new one. </i><br />
 <code>pANTLR3_BASE_RECOGNIZER</code> <code>rec</code><br />
 <i>Pointer to the implementation of a base recognizer, which the lexer creates and then overrides with its own lexer oriented functions (the default implementation is parser oriented). </i><br />
 void(* <code>recover</code> )(struct <code>ANTLR3_LEXER_struct</code> *lexer)<br />
 <i>Pointer to a function that recovers from an error found in the input stream. </i><br />
 void(* <code>setCharStream</code> )(struct <code>ANTLR3_LEXER_struct</code> *lexer, <code>pANTLR3_INPUT_STREAM</code> <code>input</code>)<br />
 <i>Pointer to a function that sets the charstream source for the lexer and causes it to be reset. </i><br />
 void * <code>super</code><br />
 <i>If there is a super structure that is implementing the lexer, then a pointer to it can be stored here in case implementing functions are overridden by this super structure. </i></p>
<h2>Field Documentation</h2>
<h3>void* <code>ANTLR3_LEXER_struct::ctx</code></h3>
<p> A generated lexer has an <code>mTokens()</code> function, which needs the context pointer of the generated lexer, not the base lexer interface this is stored here and initialized by the generated code (or manually if this is a manually built lexer. </p>
<p> Referenced by nextTokenStr().</p>
<h3><code>pANTLR3_COMMON_TOKEN</code>(* <code>ANTLR3_LEXER_struct::emit</code>)(struct <code>ANTLR3_LEXER_struct</code> *lexer)</h3>
<p> Pointer to a function that constructs a new token from the lexer stored information. </p>
<p> Referenced by antlr3LexerNew().</p>
<h3>void(* <code>ANTLR3_LEXER_struct::emitNew</code>)(struct <code>ANTLR3_LEXER_struct</code> *lexer, <code>pANTLR3_COMMON_TOKEN</code> token)</h3>
<p> Pointer to a function that emits the supplied token as the next token in the stream. </p>
<p> Referenced by antlr3LexerNew().</p>
<h3>void(* <code>ANTLR3_LEXER_struct::free</code>)(struct <code>ANTLR3_LEXER_struct</code> *lexer)</h3>
<p> Pointer to a function that knows how to free the resources of a lexer. </p>
<p> Referenced by antlr3LexerNew().</p>
<h3><code>ANTLR3_MARKER</code>(* <code>ANTLR3_LEXER_struct::getCharIndex</code>)(struct <code>ANTLR3_LEXER_struct</code> *lexer)</h3>
<p> Referenced by antlr3LexerNew(), emit(), getText(), and nextTokenStr().</p>
<h3><code>ANTLR3_UINT32</code>(* <code>ANTLR3_LEXER_struct::getCharPositionInLine</code>)(struct <code>ANTLR3_LEXER_struct</code> *lexer)</h3>
<p> Referenced by antlr3LexerNew().</p>
<h3><code>ANTLR3_UINT32</code>(* <code>ANTLR3_LEXER_struct::getLine</code>)(struct <code>ANTLR3_LEXER_struct</code> *lexer)</h3>
<p> Pointer to function to return the current line number in the input stream. </p>
<p> Referenced by antlr3LexerNew(), and nextTokenStr().</p>
<h3><code>pANTLR3_STRING</code>(* <code>ANTLR3_LEXER_struct::getText</code>)(struct <code>ANTLR3_LEXER_struct</code> *lexer)</h3>
<p> Pointer to function to return the text so far for the current token being generated. </p>
<p> Referenced by antlr3LexerNew().</p>
<h3><code>pANTLR3_INPUT_STREAM</code> <code>ANTLR3_LEXER_struct::input</code></h3>
<p> A pointer to the character stream whence this lexer is receiving characters. TODO: I may come back to this and implement charstream outside the input stream as per the java implementation. </p>
<p> Referenced by alreadyParsedRule(), antlr3RecognitionExceptionNew(), displayRecognitionError(), emit(), getCharIndex(), getCharPositionInLine(), getLine(), getText(), matchAny(), matchc(), matchRange(), matchs(), memoize(), nextTokenStr(), popCharStream(), pushCharStream(), recover(), reset(), and setCharStream().</p>
<h3>void(* <code>ANTLR3_LEXER_struct::matchAny</code>)(struct <code>ANTLR3_LEXER_struct</code> *lexer)</h3>
<p> Pointer to a function that matches the next token/char in the input stream regardless of what it actaully is. </p>
<p> Referenced by antlr3LexerNew().</p>
<h3><code>ANTLR3_BOOLEAN</code>(* <code>ANTLR3_LEXER_struct::matchc</code>)(struct <code>ANTLR3_LEXER_struct</code> *lexer, <code>ANTLR3_UCHAR</code> c)</h3>
<p> Pointer to a function that matches and consumes the specified character from the input stream. As the input stream is required to provide characters via LA() as UTF32 characters it does not need to provide an implementation if it is not sourced from 8 bit ASCII. The default lexer implementation is source encoding agnostic, unless for some reason it takes two 32 bit characters to specify a single character, in which case the input stream and the lexer rules would have to match in encoding and then it would work &#8216;by accident&#8217; anyway. </p>
<p> Referenced by antlr3LexerNew().</p>
<h3><code>ANTLR3_BOOLEAN</code>(* <code>ANTLR3_LEXER_struct::matchRange</code>)(struct <code>ANTLR3_LEXER_struct</code> *lexer, <code>ANTLR3_UCHAR</code> low, <code>ANTLR3_UCHAR</code> high)</h3>
<p> Pointer to a function that matches any character in the supplied range (I suppose it could be a token range too but this would only be useful if the tokens were in tsome guaranteed order which is only going to happen with a hand crafted token set). </p>
<p> Referenced by antlr3LexerNew().</p>
<h3><code>ANTLR3_BOOLEAN</code>(* <code>ANTLR3_LEXER_struct::matchs</code>)(struct <code>ANTLR3_LEXER_struct</code> *lexer, <code>ANTLR3_UCHAR</code> *string)</h3>
<p> Pointer to a function that attempts to match and consume the specified string from the input stream. Note that strings muse be passed as terminated arrays of ANTLR3_UCHAR. Strings are terminated with 0xFFFFFFFF, which is an invalid UTF32 character </p>
<p> Referenced by antlr3LexerNew().</p>
<h3>void(* <code>ANTLR3_LEXER_struct::mTokens</code>)(void *<code>ctx</code>)</h3>
<p> Pointer to the user provided (either manually or through code generation function that causes the lexer rules to run the lexing rules and produce the next token if there iss one. This is called from <code>nextToken()</code> in the pANTLR3_TOKEN_SOURCE. Note that the input parameter for this funciton is the generated lexer context (stored in ctx in this interface) it is a generated function and expects the context to be the generated lexer. </p>
<p> Referenced by antlr3LexerNew(), and nextTokenStr().</p>
<h3>void(* <code>ANTLR3_LEXER_struct::popCharStream</code>)(struct <code>ANTLR3_LEXER_struct</code> *lexer)</h3>
<p> Pointer to a function that abandons the current input stream, whether it is empty or not and reverts to the previous stacked input stream. </p>
<p> Referenced by antlr3LexerNew(), and nextToken().</p>
<h3>void(* <code>ANTLR3_LEXER_struct::pushCharStream</code>)(struct <code>ANTLR3_LEXER_struct</code> *lexer, <code>pANTLR3_INPUT_STREAM</code> <code>input</code>)</h3>
<p> Pointer to a function that switches the current character input stream to a new one, saving the old one, which we will revert to at the end of this new one. </p>
<p> Referenced by antlr3LexerNew().</p>
<h3><code>pANTLR3_BASE_RECOGNIZER</code> <code>ANTLR3_LEXER_struct::rec</code></h3>
<p> Pointer to the implementation of a base recognizer, which the lexer creates and then overrides with its own lexer oriented functions (the default implementation is parser oriented). This also contains a token source interface, which the lexer instance will provide to anything that needs it, which is anything else that implements a base recognizer, such as a parser. </p>
<p> Referenced by antlr3LexerNew(), displayRecognitionError(), emit(), emitNew(), freeLexer(), getText(), matchc(), matchRange(), matchs(), nextToken(), nextTokenStr(), popCharStream(), pushCharStream(), reset(), and setCharStream().</p>
<h3>void(* <code>ANTLR3_LEXER_struct::recover</code>)(struct <code>ANTLR3_LEXER_struct</code> *lexer)</h3>
<p> Pointer to a function that recovers from an error found in the input stream. Generally, this will be a ANTLR3_EXCEPTION_NOVIABLE_ALT but it could also be from a mismatched token that the (*match)() could not recover from. </p>
<p> Referenced by antlr3LexerNew(), matchc(), matchRange(), matchs(), and nextTokenStr().</p>
<h3>void(* <code>ANTLR3_LEXER_struct::setCharStream</code>)(struct <code>ANTLR3_LEXER_struct</code> *lexer, <code>pANTLR3_INPUT_STREAM</code> <code>input</code>)</h3>
<p> Pointer to a function that sets the charstream source for the lexer and causes it to be reset. </p>
<p> Referenced by antlr3LexerNew(), popCharStream(), and pushCharStream().</p>
<h3>void* <code>ANTLR3_LEXER_struct::super</code></h3>
<p> If there is a super structure that is implementing the lexer, then a pointer to it can be stored here in case implementing functions are overridden by this super structure. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for ANTLR3C from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAZ">Author</a></p>
<dd></dl>
