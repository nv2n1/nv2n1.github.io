---
title: "antlr3-tokfactory(3)"
name: "antlr3-tokfactory"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-tokfactory/"
description: "ANTLR3_RECOGNIZER_SHARED_STATE_struct –"
---

<p>ANTLR3_RECOGNIZER_SHARED_STATE_struct &#8211; </p>
<p> All the data elements required to track the current state of any recognizer (lexer, parser, tree parser).</p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/antlr3recognizersharedstate.h">antlr3recognizersharedstate.h</a>&gt;</p>
<h3>Data Fields</h3>
<p><code>ANTLR3_INT32</code> <code>backtracking</code><br />
 <i>If 0, no backtracking is going on. </i><br />
 <code>ANTLR3_UINT32</code> <code>channel</code><br />
 <i>The channel number for the current token. </i><br />
 void * <code>custom</code> </p>
<p> <code>ANTLR3_BOOLEAN</code> <code>error</code><br />
 <i>If set to ANTLR3_TRUE then the recognizer has an exception condition (this is tested by the generated code for the rules of the grammar). </i><br />
 <code>ANTLR3_UINT32</code> <code>errorCount</code><br />
 <i>When the recognizer terminates, the error handling functions will have incremented this value if any error occurred (that was displayed). </i><br />
 <code>ANTLR3_BOOLEAN</code> <code>errorRecovery</code><br />
 <i>This is true when we see an error and before having successfully matched a token. </i><br />
 <code>pANTLR3_EXCEPTION</code> <code>exception</code><br />
 <i>Points to the first in a possible chain of exceptions that the recognizer has discovered. </i><br />
 <code>ANTLR3_BOOLEAN</code> <code>failed</code><br />
 <i>In lieu of a return value, this indicates that a rule or token has failed to match. </i><br />
 <code>pANTLR3_STACK</code> <code>following</code><br />
 <i>Track the set of token types that can follow any rule invocation. </i><br />
 <code>ANTLR3_MARKER</code> <code>lastErrorIndex</code><br />
 <i>The index into the input stream where the last error occurred. </i><br />
 <code>pANTLR3_VECTOR</code> <code>rStreams</code><br />
 <i>A stack of token/tree rewrite streams that are available for use by a parser or tree parser that is using rewrites to generate an AST. </i><br />
 <code>pANTLR3_INT_TRIE</code> <code>ruleMemo</code><br />
 <i>ANTLR3_VECTOR of ANTLR3_LIST for rule memoizing. </i><br />
 <code>ANTLR3_UINT32</code> <code>sizeHint</code><br />
 <i>Track around a hint from the creator of the recognizer as to how big this thing is going to get, as the actress said to the bishop. </i><br />
 <code>pANTLR3_STACK</code> <code>streams</code><br />
 <i>Input stream stack, which allows the C programmer to switch input streams easily and allow the standard </i><code>nextToken()</code> implementation to deal with it as this is a common requirement.<br />
 <code>pANTLR3_STRING</code> <code>text</code><br />
 <i>Text for the current token. </i><br />
 <code>pANTLR3_COMMON_TOKEN</code> <code>token</code><br />
 <i>The goal of all lexer rules/methods is to create a token object. </i><br />
 <code>pANTLR3_UINT8</code> * <code>tokenNames</code><br />
 <i>Pointer to an array of token names that are generally useful in error reporting. </i><br />
 <code>ANTLR3_MARKER</code> <code>tokenStartCharIndex</code><br />
 <i>What character index in the stream did the current token start at? Needed, for example, to get the text for current token. </i><br />
 <code>ANTLR3_INT32</code> <code>tokenStartCharPositionInLine</code><br />
 <i>The character position of the first character of the current token within the line specified by tokenStartLine. </i><br />
 <code>ANTLR3_INT32</code> <code>tokenStartLine</code><br />
 <i>The input line (where it makes sense) on which the first character of the current token resides. </i><br />
 <code>pANTLR3_TOKEN_FACTORY</code> <code>tokFactory</code><br />
 <i>The goal of all lexer rules being to create a token, then a lexer needs to build a token factory to create them. </i><br />
 <code>pANTLR3_TOKEN_SOURCE</code> <code>tokSource</code><br />
 <i>A lexer is a source of tokens, produced by all the generated (or hand crafted if you like) matching rules. </i><br />
 <code>ANTLR3_UINT32</code> <code>type</code><br />
 <i>The token type for the current token. </i><br />
 <code>ANTLR3_UINT32</code> <code>user1</code><br />
 <i>User controlled variables that will be installed in a newly created token. </i><br />
 <code>ANTLR3_UINT32</code> <code>user2</code> </p>
<p> <code>ANTLR3_UINT32</code> <code>user3</code> </p>
<p> void * <code>userp</code><br />
 <i>User programmable pointer that can be used for instance as a place to store some tracking structure specific to the grammar that would not normally be available to the error handling functions. </i></p>
<h2>Detailed Description</h2>
<p>All the data elements required to track the current state of any recognizer (lexer, parser, tree parser). </p>
<p> May be share between multiple recognizers such that grammar inheritance is easily supported.</p>
<h2>Field Documentation</h2>
<h3><code>ANTLR3_INT32</code> <code>ANTLR3_RECOGNIZER_SHARED_STATE_struct::backtracking</code></h3>
<p>If 0, no backtracking is going on. Safe to exec actions etc&#8230; If &gt;0 then it&#8217;s the level of backtracking. </p>
<p> Referenced by antlr3BaseRecognizerNew(), match(), matchc(), matchRange(), matchs(), noViableAlt(), reset(), and synpred().</p>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_RECOGNIZER_SHARED_STATE_struct::channel</code></h3>
<p>The channel number for the current token. </p>
<p> Referenced by emit(), nextTokenStr(), and reset().</p>
<h3>void* <code>ANTLR3_RECOGNIZER_SHARED_STATE_struct::custom</code></h3>
<p>Referenced by emit().</p>
<h3><code>ANTLR3_BOOLEAN</code> <code>ANTLR3_RECOGNIZER_SHARED_STATE_struct::error</code></h3>
<p>If set to ANTLR3_TRUE then the recognizer has an exception condition (this is tested by the generated code for the rules of the grammar). </p>
<p> Referenced by antlr3dfapredict(), antlr3RecognitionExceptionNew(), nextTokenStr(), recover(), recoverFromMismatchedElement(), recoverFromMismatchedSet(), and recoverFromMismatchedToken().</p>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_RECOGNIZER_SHARED_STATE_struct::errorCount</code></h3>
<p>When the recognizer terminates, the error handling functions will have incremented this value if any error occurred (that was displayed). It can then be used by the grammar programmer without having to use static globals. </p>
<p> Referenced by antlr3BaseRecognizerNew(), getNumberOfSyntaxErrors(), reportError(), and reset().</p>
<h3><code>ANTLR3_BOOLEAN</code> <code>ANTLR3_RECOGNIZER_SHARED_STATE_struct::errorRecovery</code></h3>
<p>This is true when we see an error and before having successfully matched a token. Prevents generation of more than one error message per error. </p>
<p> Referenced by antlr3BaseRecognizerNew(), match(), matchAny(), reportError(), and reset().</p>
<h3><code>pANTLR3_EXCEPTION</code> <code>ANTLR3_RECOGNIZER_SHARED_STATE_struct::exception</code></h3>
<p>Points to the first in a possible chain of exceptions that the recognizer has discovered. </p>
<p> Referenced by antlr3MTExceptionNew(), antlr3MTNExceptionNew(), antlr3RecognitionExceptionNew(), displayRecognitionError(), freeBR(), mismatch(), mismatchIsUnwantedToken(), noViableAlt(), recoverFromMismatchedSet(), and recoverFromMismatchedToken().</p>
<h3><code>ANTLR3_BOOLEAN</code> <code>ANTLR3_RECOGNIZER_SHARED_STATE_struct::failed</code></h3>
<p>In lieu of a return value, this indicates that a rule or token has failed to match. Reset to false upon valid token match. </p>
<p> Referenced by alreadyParsedRule(), antlr3BaseRecognizerNew(), match(), matchAny(), matchc(), matchRange(), matchs(), memoize(), nextTokenStr(), noViableAlt(), recover(), recoverFromMismatchedElement(), recoverFromMismatchedSet(), reset(), and synpred().</p>
<h3><code>pANTLR3_STACK</code> <code>ANTLR3_RECOGNIZER_SHARED_STATE_struct::following</code></h3>
<p>Track the set of token types that can follow any rule invocation. Stack structure, to support: List&lt;BitSet&gt;. </p>
<p> Referenced by antlr3BaseRecognizerNew(), combineFollows(), freeParser(), mismatchIsMissingToken(), and reset().</p>
<h3><code>ANTLR3_MARKER</code> <code>ANTLR3_RECOGNIZER_SHARED_STATE_struct::lastErrorIndex</code></h3>
<p>The index into the input stream where the last error occurred. This is used to prevent infinite loops where an error is found but no token is consumed during recovery&#8230;another error is found, ad nauseam. This is a failsafe mechanism to guarantee that at least one token/tree node is consumed for two errors. </p>
<p> Referenced by antlr3BaseRecognizerNew(), recover(), and reset().</p>
<h3><code>pANTLR3_VECTOR</code> <code>ANTLR3_RECOGNIZER_SHARED_STATE_struct::rStreams</code></h3>
<p>A stack of token/tree rewrite streams that are available for use by a parser or tree parser that is using rewrites to generate an AST. This saves each rule in the recongizer from having to allocate and deallocate rewtire streams on entry and exit. As the parser recurses throgh the rules it will reach a steady state of the maximum number of allocated streams, which instead of deallocating them at rule exit, it will place on this stack for reuse. The streams are then all finally freed when this stack is freed. </p>
<p> Referenced by antlr3BaseRecognizerNew(), antlr3RewriteRuleElementStreamNewAE(), freeBR(), freeNodeRS(), and freeRS().</p>
<h3><code>pANTLR3_INT_TRIE</code> <code>ANTLR3_RECOGNIZER_SHARED_STATE_struct::ruleMemo</code></h3>
<p>ANTLR3_VECTOR of ANTLR3_LIST for rule memoizing. Tracks the stop token index for each rule. ruleMemo[ruleIndex] is the memoization table for ruleIndex. For key ruleStartIndex, you get back the stop token for associated rule or MEMO_RULE_FAILED. </p>
<p> This is only used if rule memoization is on. </p>
<p> Referenced by antlr3BaseRecognizerNew(), freeBR(), getRuleMemoization(), memoize(), and reset().</p>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_RECOGNIZER_SHARED_STATE_struct::sizeHint</code></h3>
<p>Track around a hint from the creator of the recognizer as to how big this thing is going to get, as the actress said to the bishop. This allows us to tune hash tables accordingly. This might not be the best place for this in the end but we will see. </p>
<p> Referenced by antlr3BaseRecognizerNew().</p>
<h3><code>pANTLR3_STACK</code> <code>ANTLR3_RECOGNIZER_SHARED_STATE_struct::streams</code></h3>
<p>Input stream stack, which allows the C programmer to switch input streams easily and allow the standard <code>nextToken()</code> implementation to deal with it as this is a common requirement. </p>
<p> Referenced by freeLexer(), nextToken(), popCharStream(), and pushCharStream().</p>
<h3><code>pANTLR3_STRING</code> <code>ANTLR3_RECOGNIZER_SHARED_STATE_struct::text</code></h3>
<p>Text for the current token. This can be overridden by setting this variable directly or by using the SETTEXT() macro (preferred) in your lexer rules. </p>
<p> Referenced by emit(), getText(), nextTokenStr(), reset(), and setCharStream().</p>
<h3><code>pANTLR3_COMMON_TOKEN</code> <code>ANTLR3_RECOGNIZER_SHARED_STATE_struct::token</code></h3>
<p>The goal of all lexer rules/methods is to create a token object. This is an instance variable as multiple rules may collaborate to create a single token. For example, NUM : INT | FLOAT ; In this case, you want the INT or FLOAT rule to set token and not have it reset to a NUM token in rule NUM. </p>
<p> Referenced by emit(), emitNew(), nextTokenStr(), reset(), and setCharStream().</p>
<h3><code>pANTLR3_UINT8</code>* <code>ANTLR3_RECOGNIZER_SHARED_STATE_struct::tokenNames</code></h3>
<p>Pointer to an array of token names that are generally useful in error reporting. The generated parsers install this pointer. The table it points to is statically allocated as 8 bit ascii at parser compile time &#8211; grammar token names are thus restricted in character sets, which does not seem to terrible. </p>
<p> Referenced by antlr3BaseRecognizerNew(), getMissingSymbol(), and reportError().</p>
<h3><code>ANTLR3_MARKER</code> <code>ANTLR3_RECOGNIZER_SHARED_STATE_struct::tokenStartCharIndex</code></h3>
<p>What character index in the stream did the current token start at? Needed, for example, to get the text for current token. Set at the start of nextToken. </p>
<p> Referenced by displayRecognitionError(), emit(), getText(), nextTokenStr(), reset(), and setCharStream().</p>
<h3><code>ANTLR3_INT32</code> <code>ANTLR3_RECOGNIZER_SHARED_STATE_struct::tokenStartCharPositionInLine</code></h3>
<p>The character position of the first character of the current token within the line specified by tokenStartLine. </p>
<p> Referenced by displayRecognitionError(), emit(), nextTokenStr(), and reset().</p>
<h3><code>ANTLR3_INT32</code> <code>ANTLR3_RECOGNIZER_SHARED_STATE_struct::tokenStartLine</code></h3>
<p>The input line (where it makes sense) on which the first character of the current token resides. </p>
<p> Referenced by displayRecognitionError(), emit(), nextTokenStr(), and reset().</p>
<h3><code>pANTLR3_TOKEN_FACTORY</code> <code>ANTLR3_RECOGNIZER_SHARED_STATE_struct::tokFactory</code></h3>
<p>The goal of all lexer rules being to create a token, then a lexer needs to build a token factory to create them. </p>
<p> Referenced by antlr3BaseRecognizerNew(), antlr3LexerNew(), emit(), freeBR(), freeLexer(), getMissingSymbol(), and setCharStream().</p>
<h3><code>pANTLR3_TOKEN_SOURCE</code> <code>ANTLR3_RECOGNIZER_SHARED_STATE_struct::tokSource</code></h3>
<p>A lexer is a source of tokens, produced by all the generated (or hand crafted if you like) matching rules. As such it needs to provide a token source interface implementation. </p>
<p> Referenced by antlr3BaseRecognizerNew(), antlr3LexerNew(), freeLexer(), and setCharStream().</p>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_RECOGNIZER_SHARED_STATE_struct::type</code></h3>
<p>The token type for the current token. </p>
<p> Referenced by emit(), and reset().</p>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_RECOGNIZER_SHARED_STATE_struct::user1</code></h3>
<p>User controlled variables that will be installed in a newly created token. </p>
<p> Referenced by emit().</p>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_RECOGNIZER_SHARED_STATE_struct::user2</code></h3>
<p>Referenced by emit().</p>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_RECOGNIZER_SHARED_STATE_struct::user3</code></h3>
<p>Referenced by emit().</p>
<h3>void* <code>ANTLR3_RECOGNIZER_SHARED_STATE_struct::userp</code></h3>
<p>User programmable pointer that can be used for instance as a place to store some tracking structure specific to the grammar that would not normally be available to the error handling functions. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
