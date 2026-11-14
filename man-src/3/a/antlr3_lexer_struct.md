---
title: "antlr3_lexer_struct(3)"
name: "antlr3_lexer_struct"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3_lexer_struct/"
---

ANTLR3_LEXER_struct - 

<h2>Synopsis</h2>#include &lt;<a HREF="file:/usr/include/antlr3lexer.h">antlr3lexer.h</a>&gt;
<h3>Data Fields</h3>void * <b>ctx</b> 
 <i>A generated lexer has an </i><b>mTokens()</b> function, which needs the context pointer of the generated lexer, not the base lexer interface this is stored here and initialized by the generated code (or manually if this is a manually built lexer. 
 <b>pANTLR3_COMMON_TOKEN</b>(* <b>emit</b> )(struct <b>ANTLR3_LEXER_struct</b> *lexer) 
 <i>Pointer to a function that constructs a new token from the lexer stored information. </i> 
 void(* <b>emitNew</b> )(struct <b>ANTLR3_LEXER_struct</b> *lexer, <b>pANTLR3_COMMON_TOKEN</b> token) 
 <i>Pointer to a function that emits the supplied token as the next token in the stream. </i> 
 void(* <b>free</b> )(struct <b>ANTLR3_LEXER_struct</b> *lexer) 
 <i>Pointer to a function that knows how to free the resources of a lexer. </i> 
 <b>ANTLR3_MARKER</b>(* <b>getCharIndex</b> )(struct <b>ANTLR3_LEXER_struct</b> *lexer) 
 
 <b>ANTLR3_UINT32</b>(* <b>getCharPositionInLine</b> )(struct <b>ANTLR3_LEXER_struct</b> *lexer) 
 
 <b>ANTLR3_UINT32</b>(* <b>getLine</b> )(struct <b>ANTLR3_LEXER_struct</b> *lexer) 
 <i>Pointer to function to return the current line number in the input stream. </i> 
 <b>pANTLR3_STRING</b>(* <b>getText</b> )(struct <b>ANTLR3_LEXER_struct</b> *lexer) 
 <i>Pointer to function to return the text so far for the current token being generated. </i> 
 <b>pANTLR3_INPUT_STREAM</b> <b>input</b> 
 <i>A pointer to the character stream whence this lexer is receiving characters. </i> 
 void(* <b>matchAny</b> )(struct <b>ANTLR3_LEXER_struct</b> *lexer) 
 <i>Pointer to a function that matches the next token/char in the input stream regardless of what it actaully is. </i> 
 <b>ANTLR3_BOOLEAN</b>(* <b>matchc</b> )(struct <b>ANTLR3_LEXER_struct</b> *lexer, <b>ANTLR3_UCHAR</b> c) 
 <i>Pointer to a function that matches and consumes the specified character from the input stream. </i> 
 <b>ANTLR3_BOOLEAN</b>(* <b>matchRange</b> )(struct <b>ANTLR3_LEXER_struct</b> *lexer, <b>ANTLR3_UCHAR</b> low, <b>ANTLR3_UCHAR</b> high) 
 <i>Pointer to a function that matches any character in the supplied range (I suppose it could be a token range too but this would only be useful if the tokens were in tsome guaranteed order which is only going to happen with a hand crafted token set). </i> 
 <b>ANTLR3_BOOLEAN</b>(* <b>matchs</b> )(struct <b>ANTLR3_LEXER_struct</b> *lexer, <b>ANTLR3_UCHAR</b> *string) 
 <i>Pointer to a function that attempts to match and consume the specified string from the input stream. </i> 
 void(* <b>mTokens</b> )(void *<b>ctx</b>) 
 <i>Pointer to the user provided (either manually or through code generation function that causes the lexer rules to run the lexing rules and produce the next token if there iss one. </i> 
 void(* <b>popCharStream</b> )(struct <b>ANTLR3_LEXER_struct</b> *lexer) 
 <i>Pointer to a function that abandons the current input stream, whether it is empty or not and reverts to the previous stacked input stream. </i> 
 void(* <b>pushCharStream</b> )(struct <b>ANTLR3_LEXER_struct</b> *lexer, <b>pANTLR3_INPUT_STREAM</b> <b>input</b>) 
 <i>Pointer to a function that switches the current character input stream to a new one, saving the old one, which we will revert to at the end of this new one. </i> 
 <b>pANTLR3_BASE_RECOGNIZER</b> <b>rec</b> 
 <i>Pointer to the implementation of a base recognizer, which the lexer creates and then overrides with its own lexer oriented functions (the default implementation is parser oriented). </i> 
 void(* <b>recover</b> )(struct <b>ANTLR3_LEXER_struct</b> *lexer) 
 <i>Pointer to a function that recovers from an error found in the input stream. </i> 
 void(* <b>setCharStream</b> )(struct <b>ANTLR3_LEXER_struct</b> *lexer, <b>pANTLR3_INPUT_STREAM</b> <b>input</b>) 
 <i>Pointer to a function that sets the charstream source for the lexer and causes it to be reset. </i> 
 void * <b>super</b> 
 <i>If there is a super structure that is implementing the lexer, then a pointer to it can be stored here in case implementing functions are overridden by this super structure. </i>
<h2>Field Documentation</h2><h3>void* <b>ANTLR3_LEXER_struct::ctx</b></h3>A generated lexer has an <b>mTokens()</b> function, which needs the context pointer of the generated lexer, not the base lexer interface this is stored here and initialized by the generated code (or manually if this is a manually built lexer. 

 Referenced by nextTokenStr().
<h3><b>pANTLR3_COMMON_TOKEN</b>(* <b>ANTLR3_LEXER_struct::emit</b>)(struct <b>ANTLR3_LEXER_struct</b> *lexer)</h3>Pointer to a function that constructs a new token from the lexer stored information. 

 Referenced by antlr3LexerNew().
<h3>void(* <b>ANTLR3_LEXER_struct::emitNew</b>)(struct <b>ANTLR3_LEXER_struct</b> *lexer, <b>pANTLR3_COMMON_TOKEN</b> token)</h3>Pointer to a function that emits the supplied token as the next token in the stream. 

 Referenced by antlr3LexerNew().
<h3>void(* <b>ANTLR3_LEXER_struct::free</b>)(struct <b>ANTLR3_LEXER_struct</b> *lexer)</h3>Pointer to a function that knows how to free the resources of a lexer. 

 Referenced by antlr3LexerNew().
<h3><b>ANTLR3_MARKER</b>(* <b>ANTLR3_LEXER_struct::getCharIndex</b>)(struct <b>ANTLR3_LEXER_struct</b> *lexer)</h3>Referenced by antlr3LexerNew(), emit(), getText(), and nextTokenStr().
<h3><b>ANTLR3_UINT32</b>(* <b>ANTLR3_LEXER_struct::getCharPositionInLine</b>)(struct <b>ANTLR3_LEXER_struct</b> *lexer)</h3>Referenced by antlr3LexerNew().
<h3><b>ANTLR3_UINT32</b>(* <b>ANTLR3_LEXER_struct::getLine</b>)(struct <b>ANTLR3_LEXER_struct</b> *lexer)</h3>Pointer to function to return the current line number in the input stream. 

 Referenced by antlr3LexerNew(), and nextTokenStr().
<h3><b>pANTLR3_STRING</b>(* <b>ANTLR3_LEXER_struct::getText</b>)(struct <b>ANTLR3_LEXER_struct</b> *lexer)</h3>Pointer to function to return the text so far for the current token being generated. 

 Referenced by antlr3LexerNew().
<h3><b>pANTLR3_INPUT_STREAM</b> <b>ANTLR3_LEXER_struct::input</b></h3>A pointer to the character stream whence this lexer is receiving characters. TODO: I may come back to this and implement charstream outside the input stream as per the java implementation. 

 Referenced by alreadyParsedRule(), antlr3RecognitionExceptionNew(), displayRecognitionError(), emit(), getCharIndex(), getCharPositionInLine(), getLine(), getText(), matchAny(), matchc(), matchRange(), matchs(), memoize(), nextTokenStr(), popCharStream(), pushCharStream(), recover(), reset(), and setCharStream().
<h3>void(* <b>ANTLR3_LEXER_struct::matchAny</b>)(struct <b>ANTLR3_LEXER_struct</b> *lexer)</h3>Pointer to a function that matches the next token/char in the input stream regardless of what it actaully is. 

 Referenced by antlr3LexerNew().
<h3><b>ANTLR3_BOOLEAN</b>(* <b>ANTLR3_LEXER_struct::matchc</b>)(struct <b>ANTLR3_LEXER_struct</b> *lexer, <b>ANTLR3_UCHAR</b> c)</h3>Pointer to a function that matches and consumes the specified character from the input stream. As the input stream is required to provide characters via LA() as UTF32 characters it does not need to provide an implementation if it is not sourced from 8 bit ASCII. The default lexer implementation is source encoding agnostic, unless for some reason it takes two 32 bit characters to specify a single character, in which case the input stream and the lexer rules would have to match in encoding and then it would work 'by accident' anyway. 

 Referenced by antlr3LexerNew().
<h3><b>ANTLR3_BOOLEAN</b>(* <b>ANTLR3_LEXER_struct::matchRange</b>)(struct <b>ANTLR3_LEXER_struct</b> *lexer, <b>ANTLR3_UCHAR</b> low, <b>ANTLR3_UCHAR</b> high)</h3>Pointer to a function that matches any character in the supplied range (I suppose it could be a token range too but this would only be useful if the tokens were in tsome guaranteed order which is only going to happen with a hand crafted token set). 

 Referenced by antlr3LexerNew().
<h3><b>ANTLR3_BOOLEAN</b>(* <b>ANTLR3_LEXER_struct::matchs</b>)(struct <b>ANTLR3_LEXER_struct</b> *lexer, <b>ANTLR3_UCHAR</b> *string)</h3>Pointer to a function that attempts to match and consume the specified string from the input stream. Note that strings muse be passed as terminated arrays of ANTLR3_UCHAR. Strings are terminated with 0xFFFFFFFF, which is an invalid UTF32 character 

 Referenced by antlr3LexerNew().
<h3>void(* <b>ANTLR3_LEXER_struct::mTokens</b>)(void *<b>ctx</b>)</h3>Pointer to the user provided (either manually or through code generation function that causes the lexer rules to run the lexing rules and produce the next token if there iss one. This is called from <b>nextToken()</b> in the pANTLR3_TOKEN_SOURCE. Note that the input parameter for this funciton is the generated lexer context (stored in ctx in this interface) it is a generated function and expects the context to be the generated lexer. 

 Referenced by antlr3LexerNew(), and nextTokenStr().
<h3>void(* <b>ANTLR3_LEXER_struct::popCharStream</b>)(struct <b>ANTLR3_LEXER_struct</b> *lexer)</h3>Pointer to a function that abandons the current input stream, whether it is empty or not and reverts to the previous stacked input stream. 

 Referenced by antlr3LexerNew(), and nextToken().
<h3>void(* <b>ANTLR3_LEXER_struct::pushCharStream</b>)(struct <b>ANTLR3_LEXER_struct</b> *lexer, <b>pANTLR3_INPUT_STREAM</b> <b>input</b>)</h3>Pointer to a function that switches the current character input stream to a new one, saving the old one, which we will revert to at the end of this new one. 

 Referenced by antlr3LexerNew().
<h3><b>pANTLR3_BASE_RECOGNIZER</b> <b>ANTLR3_LEXER_struct::rec</b></h3>Pointer to the implementation of a base recognizer, which the lexer creates and then overrides with its own lexer oriented functions (the default implementation is parser oriented). This also contains a token source interface, which the lexer instance will provide to anything that needs it, which is anything else that implements a base recognizer, such as a parser. 

 Referenced by antlr3LexerNew(), displayRecognitionError(), emit(), emitNew(), freeLexer(), getText(), matchc(), matchRange(), matchs(), nextToken(), nextTokenStr(), popCharStream(), pushCharStream(), reset(), and setCharStream().
<h3>void(* <b>ANTLR3_LEXER_struct::recover</b>)(struct <b>ANTLR3_LEXER_struct</b> *lexer)</h3>Pointer to a function that recovers from an error found in the input stream. Generally, this will be a ANTLR3_EXCEPTION_NOVIABLE_ALT but it could also be from a mismatched token that the (*match)() could not recover from. 

 Referenced by antlr3LexerNew(), matchc(), matchRange(), matchs(), and nextTokenStr().
<h3>void(* <b>ANTLR3_LEXER_struct::setCharStream</b>)(struct <b>ANTLR3_LEXER_struct</b> *lexer, <b>pANTLR3_INPUT_STREAM</b> <b>input</b>)</h3>Pointer to a function that sets the charstream source for the lexer and causes it to be reset. 

 Referenced by antlr3LexerNew(), popCharStream(), and pushCharStream().
<h3>void* <b>ANTLR3_LEXER_struct::super</b></h3>If there is a super structure that is implementing the lexer, then a pointer to it can be stored here in case implementing functions are overridden by this super structure. 

<h2>Author</h2>Generated automatically by Doxygen for ANTLR3C from the source code.
