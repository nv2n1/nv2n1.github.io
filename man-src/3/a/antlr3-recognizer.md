---
title: "antlr3-recognizer(3)"
name: "antlr3-recognizer"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-recognizer/"
description: "ANTLR3_BASE_RECOGNIZER_struct –"
---

<h2 class="name">NAME</h2>
<p> ANTLR3_BASE_RECOGNIZER_struct &#8211; </p>
<p> Base tracking context structure for all types of recognizers.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;<a href="file:/usr/include/antlr3baserecognizer.h">antlr3baserecognizer.h</a>&gt;</p>
<h3>Data Fields</h3>
<p> <code>ANTLR3_BOOLEAN</code>(* <code>alreadyParsedRule</code> )(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>, <code>ANTLR3_MARKER</code> ruleIndex)<br />
 <i>Pointer to function that determines whether the rule has parsed input at the current index in the input stream. </i><br />
 void(* <code>beginBacktrack</code> )(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>, <code>ANTLR3_UINT32</code> level)<br />
 <i>Pointer to a function that is a hook to listen to token consumption during error recovery. </i><br />
 void(* <code>beginResync</code> )(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>)<br />
 <i>Pointer to a function that is a hook to listen to token consumption during error recovery. </i><br />
 <code>pANTLR3_BITSET</code>(* <code>combineFollows</code> )(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>, <code>ANTLR3_BOOLEAN</code> exact)<br />
 <i>Pointer to a function to combine follow bitsets. </i><br />
 <code>pANTLR3_BITSET</code>(* <code>computeCSRuleFollow</code> )(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>)<br />
 <i>Pointer to a function that computes the context-sensitive FOLLOW set for the current rule. </i><br />
 <code>pANTLR3_BITSET</code>(* <code>computeErrorRecoverySet</code> )(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>)<br />
 <i>Pointer to a function to computer the error recovery set for the current rule. </i><br />
 void(* <code>consumeUntil</code> )(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>, <code>ANTLR3_UINT32</code> tokenType)<br />
 <i>Pointer to function that consumes input until the next token matches the given token. </i><br />
 void(* <code>consumeUntilSet</code> )(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>, <code>pANTLR3_BITSET</code> set)<br />
 <i>Pointer to function that consumes input until the next token matches one in the given set. </i><br />
 <code>pANTLR3_DEBUG_EVENT_LISTENER</code> <code>debugger</code><br />
 <i>If set to something other than NULL, then this structure is points to an instance of the debugger interface. </i><br />
 void(* <code>displayRecognitionError</code> )(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>, <code>pANTLR3_UINT8</code> *tokenNames)<br />
 <i>Pointer to a function that is called to display a recognition error message. </i><br />
 void(* <code>endBacktrack</code> )(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>, <code>ANTLR3_UINT32</code> level, <code>ANTLR3_BOOLEAN</code> successful)<br />
 <i>Pointer to a function that is a hook to listen to token consumption during error recovery. </i><br />
 void(* <code>endResync</code> )(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>)<br />
 <i>Pointer to a function that is a hook to listen to token consumption during error recovery. </i><br />
 void(* <code>exConstruct</code> )(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>)<br />
 <i>Pointer to a function that can construct a generic exception structure with such information as the input stream can provide. </i><br />
 struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> <code>pANTLR3_BITSET_LIST</code> <code>follow</code> </p>
<p> void(* <code>free</code> )(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>)<br />
 <i>Pointer to a function that knows how to free the resources of a base recognizer. </i><br />
 void *(* <code>getCurrentInputSymbol</code> )(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>, <code>pANTLR3_INT_STREAM</code> istream)<br />
 <i>Pointer to a function that returns the current input symbol. </i><br />
 void *(* <code>getMissingSymbol</code> )(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>, <code>pANTLR3_INT_STREAM</code> istream, <code>pANTLR3_EXCEPTION</code> e, <code>ANTLR3_UINT32</code> expectedTokenType, <code>pANTLR3_BITSET_LIST</code> <code>follow</code>)<br />
 <i>Conjure up a missing token during error recovery. </i><br />
 <code>ANTLR3_UINT32</code>(* <code>getNumberOfSyntaxErrors</code> )(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>)<br />
 <i>Get number of recognition errors (lexer, parser, tree parser). </i><br />
 <code>pANTLR3_STACK</code>(* <code>getRuleInvocationStack</code> )(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>)<br />
 <i>Pointer to function that returns an ANTLR3_LIST of the strings that identify the rules in the parser that got you to this point. </i><br />
 <code>pANTLR3_STACK</code>(* <code>getRuleInvocationStackNamed</code> )(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>, <code>pANTLR3_UINT8</code> name) </p>
<p> <code>ANTLR3_MARKER</code>(* <code>getRuleMemoization</code> )(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>, <code>ANTLR3_INTKEY</code> ruleIndex, <code>ANTLR3_MARKER</code> ruleParseStart)<br />
 <i>Pointer to a function to return whether the rule has parsed input starting at the supplied start index before. </i><br />
 void *(* <code>match</code> )(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>, <code>ANTLR3_UINT32</code> ttype, <code>pANTLR3_BITSET_LIST</code> <code>follow</code>)<br />
 <i>Pointer to a function that matches the current input symbol against the supplied type. </i><br />
 void(* <code>matchAny</code> )(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>)<br />
 <i>Pointer to a function that matches the next token/char in the input stream regardless of what it actually is. </i><br />
 void(* <code>memoize</code> )(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>, <code>ANTLR3_MARKER</code> ruleIndex, <code>ANTLR3_MARKER</code> ruleParseStart)<br />
 <i>Pointer to function that records whether the rule has parsed the input at a current position successfully or not. </i><br />
 void(* <code>mismatch</code> )(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>, <code>ANTLR3_UINT32</code> ttype, <code>pANTLR3_BITSET_LIST</code> <code>follow</code>)<br />
 <i>Pointer to a function that works out what to do when a token mismatch occurs, so that Tree parsers can behave differently to other recognizers. </i><br />
 <code>ANTLR3_BOOLEAN</code>(* <code>mismatchIsMissingToken</code> )(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>, <code>pANTLR3_INT_STREAM</code> input, <code>pANTLR3_BITSET_LIST</code> <code>follow</code>)<br />
 <i>Pointer to a function that decides if the current token is one that can logically follow the one we were looking for, in which case the one we were looking for is probably missing from the input. </i><br />
 <code>ANTLR3_BOOLEAN</code>(* <code>mismatchIsUnwantedToken</code> )(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>, <code>pANTLR3_INT_STREAM</code> input, <code>ANTLR3_UINT32</code> ttype)<br />
 <i>Pointer to a function that decides if the token ahead of the current one is the one we were loking for, in which case the curernt one is very likely extraneous and can be reported that way. </i><br />
 struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> * <code>recognizer</code><br />
 <i>Pointer to common routine to handle single token insertion for recovery functions. </i><br />
 void(* <code>recover</code> )(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>)<br />
 <i>Pointer to a function that recovers from an error found in the input stream. </i><br />
 void *(* <code>recoverFromMismatchedSet</code> )(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>, <code>pANTLR3_BITSET_LIST</code> <code>follow</code>)<br />
 <i>Pointer to a function that recovers from a mismatched set in the token stream, in a similar manner to (*recoverFromMismatchedToken). </i><br />
 void *(* <code>recoverFromMismatchedToken</code> )(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>, <code>ANTLR3_UINT32</code> ttype, <code>pANTLR3_BITSET_LIST</code> <code>follow</code>)<br />
 <i>Pointer to a function that recovers from a mismatched token in the input stream. </i><br />
 void(* <code>reportError</code> )(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>)<br />
 <i>Pointer to a function to call to report a recognition problem. </i><br />
 void(* <code>reset</code> )(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>)<br />
 <i>Reset the recognizer. </i><br />
 <code>pANTLR3_RECOGNIZER_SHARED_STATE</code> <code>state</code><br />
 <i>A pointer to the shared recognizer state, such that multiple recognizers can use the same inputs streams and so on (in the case of grammar inheritance for instance. </i><br />
 void * <code>super</code><br />
 <i>Whatever super structure is providing this interface needs a pointer to itself so that this can be passed back to it whenever the api functions are called back from here. </i><br />
 <code>ANTLR3_BOOLEAN</code>(* <code>synpred</code> )(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>, void *ctx, void(*predicate)(void *ctx))<br />
 <i>Pointer to a function that returns whether the supplied grammar function will parse the current input stream or not. </i><br />
 <code>pANTLR3_HASH_TABLE</code>(* <code>toStrings</code> )(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>, <code>pANTLR3_HASH_TABLE</code>)<br />
 <i>Pointer to a function that converts an ANLR3_LIST of tokens to an ANTLR3_LIST of string token names. </i><br />
 <code>ANTLR3_UINT32</code> <code>type</code><br />
 <i>Indicates the type of recognizer that we are an instance of. </i></p>
<h2>Detailed Description</h2>
<p> Base tracking context structure for all types of recognizers.</p>
<h2>Field Documentation</h2>
<h3><code>ANTLR3_BOOLEAN</code>(* <code>ANTLR3_BASE_RECOGNIZER_struct::alreadyParsedRule</code>)(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>, <code>ANTLR3_MARKER</code> ruleIndex)</h3>
<p> Pointer to function that determines whether the rule has parsed input at the current index in the input stream. </p>
<p> Referenced by antlr3BaseRecognizerNew().</p>
<h3>void(* <code>ANTLR3_BASE_RECOGNIZER_struct::beginBacktrack</code>)(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>, <code>ANTLR3_UINT32</code> level)</h3>
<p> Pointer to a function that is a hook to listen to token consumption during error recovery. This is mainly used by the debug parser to send events to the listener. </p>
<p> Referenced by antlr3BaseRecognizerNew().</p>
<h3>void(* <code>ANTLR3_BASE_RECOGNIZER_struct::beginResync</code>)(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>)</h3>
<p> Pointer to a function that is a hook to listen to token consumption during error recovery. This is mainly used by the debug parser to send events to the listener. </p>
<p> Referenced by antlr3BaseRecognizerNew(), recover(), and recoverFromMismatchedToken().</p>
<h3><code>pANTLR3_BITSET</code>(* <code>ANTLR3_BASE_RECOGNIZER_struct::combineFollows</code>)(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>, <code>ANTLR3_BOOLEAN</code> exact)</h3>
<p> Pointer to a function to combine follow bitsets. <code>See also:</code></p>
<dl>
<dt>
<dd> antlr3CombineFollows() for details.</dl>
<p> Referenced by antlr3BaseRecognizerNew(), computeCSRuleFollow(), and computeErrorRecoverySet().</p>
<h3><code>pANTLR3_BITSET</code>(* <code>ANTLR3_BASE_RECOGNIZER_struct::computeCSRuleFollow</code>)(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>)</h3>
<p> Pointer to a function that computes the context-sensitive FOLLOW set for the current rule. <code>See also:</code></p>
<dl>
<dt>
<dd> antlr3ComputeCSRuleFollow() for details.</dl>
<p> Referenced by antlr3BaseRecognizerNew(), mismatchIsMissingToken(), and recoverFromMismatchedElement().</p>
<h3><code>pANTLR3_BITSET</code>(* <code>ANTLR3_BASE_RECOGNIZER_struct::computeErrorRecoverySet</code>)(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>)</h3>
<p> Pointer to a function to computer the error recovery set for the current rule. <code>See also:</code></p>
<dl>
<dt>
<dd> antlr3ComputeErrorRecoverySet() for details.</dl>
<p> Referenced by antlr3BaseRecognizerNew(), and recover().</p>
<h3>void(* <code>ANTLR3_BASE_RECOGNIZER_struct::consumeUntil</code>)(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>, <code>ANTLR3_UINT32</code> tokenType)</h3>
<p> Pointer to function that consumes input until the next token matches the given token. </p>
<p> Referenced by antlr3BaseRecognizerNew().</p>
<h3>void(* <code>ANTLR3_BASE_RECOGNIZER_struct::consumeUntilSet</code>)(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>, <code>pANTLR3_BITSET</code> set)</h3>
<p> Pointer to function that consumes input until the next token matches one in the given set. </p>
<p> Referenced by antlr3BaseRecognizerNew(), and recover().</p>
<h3><code>pANTLR3_DEBUG_EVENT_LISTENER</code> <code>ANTLR3_BASE_RECOGNIZER_struct::debugger</code></h3>
<p> If set to something other than NULL, then this structure is points to an instance of the debugger interface. In general, the debugger is only referenced internally in recovery/error operations so that it does not cause overhead by having to check this pointer in every function/method </p>
<p> Referenced by antlr3BaseRecognizerNew(), beginBacktrack(), beginResync(), endBacktrack(), endResync(), recoverFromMismatchedToken(), and setDebugListener().</p>
<h3>void(* <code>ANTLR3_BASE_RECOGNIZER_struct::displayRecognitionError</code>)(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>, <code>pANTLR3_UINT8</code> *tokenNames)</h3>
<p> Pointer to a function that is called to display a recognition error message. You may override this function independently of (*reportError)() above as that function calls this one to do the actual exception printing. </p>
<p> Referenced by antlr3BaseRecognizerNew(), antlr3LexerNew(), and reportError().</p>
<h3>void(* <code>ANTLR3_BASE_RECOGNIZER_struct::endBacktrack</code>)(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>, <code>ANTLR3_UINT32</code> level, <code>ANTLR3_BOOLEAN</code> successful)</h3>
<p> Pointer to a function that is a hook to listen to token consumption during error recovery. This is mainly used by the debug parser to send events to the listener. </p>
<p> Referenced by antlr3BaseRecognizerNew().</p>
<h3>void(* <code>ANTLR3_BASE_RECOGNIZER_struct::endResync</code>)(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>)</h3>
<p> Pointer to a function that is a hook to listen to token consumption during error recovery. This is mainly used by the debug parser to send events to the listener. </p>
<p> Referenced by antlr3BaseRecognizerNew(), recover(), and recoverFromMismatchedToken().</p>
<h3>void(* <code>ANTLR3_BASE_RECOGNIZER_struct::exConstruct</code>)(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>)</h3>
<p> Pointer to a function that can construct a generic exception structure with such information as the input stream can provide. </p>
<p> Referenced by antlr3BaseRecognizerNew(), antlr3ParserNew(), antlr3TreeParserNewStream(), matchc(), matchRange(), matchs(), mismatch(), noViableAlt(), and setCharStream().</p>
<h3>struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> <code>pANTLR3_BITSET_LIST</code> <code>ANTLR3_BASE_RECOGNIZER_struct::follow</code> [read]</h3>
<h3>void(* <code>ANTLR3_BASE_RECOGNIZER_struct::free</code>)(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>)</h3>
<p> Pointer to a function that knows how to free the resources of a base recognizer. </p>
<p> Referenced by antlr3BaseRecognizerNew(), antlr3LexerNew(), freeLexer(), and freeParser().</p>
<h3>void*(* <code>ANTLR3_BASE_RECOGNIZER_struct::getCurrentInputSymbol</code>)(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>, <code>pANTLR3_INT_STREAM</code> istream)</h3>
<p> Pointer to a function that returns the current input symbol. The is placed into any label for the associated token ref; e.g., x=ID. Token and tree parsers need to return different objects. Rather than test for input stream type or change the IntStream interface, I use a simple method to ask the recognizer to tell me what the current input symbol is. </p>
<p> This is ignored for lexers and the lexer implementation of this function should return NULL. </p>
<p> Referenced by antlr3BaseRecognizerNew(), antlr3LexerNew(), antlr3TreeParserNewStream(), match(), and recoverFromMismatchedToken().</p>
<h3>void*(* <code>ANTLR3_BASE_RECOGNIZER_struct::getMissingSymbol</code>)(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>, <code>pANTLR3_INT_STREAM</code> istream, <code>pANTLR3_EXCEPTION</code> e, <code>ANTLR3_UINT32</code> expectedTokenType, <code>pANTLR3_BITSET_LIST</code> <code>follow</code>)</h3>
<p> Conjure up a missing token during error recovery. The recognizer attempts to recover from single missing symbols. But, actions might refer to that missing symbol. For example, x=ID {f($x);}. The action clearly assumes that there has been an identifier matched previously and that $x points at that token. If that token is missing, but the next token in the stream is what we want we assume that this token is missing and we keep going. Because we have to return some token to replace the missing token, we have to conjure one up. This method gives the user control over the tokens returned for missing tokens. Mostly, you will want to create something special for identifier tokens. For literals such as &#8216;{&#8216; and &#8216;,&#8217;, the default action in the parser or tree parser works. It simply creates a CommonToken of the appropriate type. The text will be the token. If you change what tokens must be created by the lexer, override this method to create the appropriate tokens. </p>
<p> Referenced by antlr3BaseRecognizerNew(), antlr3LexerNew(), antlr3TreeParserNewStream(), recoverFromMismatchedSet(), and recoverFromMismatchedToken().</p>
<h3><code>ANTLR3_UINT32</code>(* <code>ANTLR3_BASE_RECOGNIZER_struct::getNumberOfSyntaxErrors</code>)(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>)</h3>
<p> Get number of recognition errors (lexer, parser, tree parser). Each recognizer tracks its own number. So parser and lexer each have separate count. Does not count the spurious errors found between an error and next valid token match </p>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>reportError()</code></dl>
<p> Referenced by antlr3BaseRecognizerNew().</p>
<h3><code>pANTLR3_STACK</code>(* <code>ANTLR3_BASE_RECOGNIZER_struct::getRuleInvocationStack</code>)(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>)</h3>
<p> Pointer to function that returns an ANTLR3_LIST of the strings that identify the rules in the parser that got you to this point. Can be overridden by installing your own function set. </p>
<p> <code>Todo</code></p>
<dl>
<dt>
<dd> Document how to override invocation stack functions.</dl>
<p> Referenced by antlr3BaseRecognizerNew().</p>
<h3><code>pANTLR3_STACK</code>(* <code>ANTLR3_BASE_RECOGNIZER_struct::getRuleInvocationStackNamed</code>)(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>, <code>pANTLR3_UINT8</code> name)</h3>
<p> Referenced by antlr3BaseRecognizerNew().</p>
<h3><code>ANTLR3_MARKER</code>(* <code>ANTLR3_BASE_RECOGNIZER_struct::getRuleMemoization</code>)(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>, <code>ANTLR3_INTKEY</code> ruleIndex, <code>ANTLR3_MARKER</code> ruleParseStart)</h3>
<p> Pointer to a function to return whether the rule has parsed input starting at the supplied start index before. If the rule has not parsed input starting from the supplied start index, then it will return ANTLR3_MEMO_RULE_UNKNOWN. If it has parsed from the suppled start point then it will return the point where it last stopped parsing after that start point. </p>
<p> Referenced by alreadyParsedRule(), and antlr3BaseRecognizerNew().</p>
<h3>void*(* <code>ANTLR3_BASE_RECOGNIZER_struct::match</code>)(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>, <code>ANTLR3_UINT32</code> ttype, <code>pANTLR3_BITSET_LIST</code> <code>follow</code>)</h3>
<p> Pointer to a function that matches the current input symbol against the supplied type. the function causes an error if a match is not found and the default implementation will also attempt to perform one token insertion or deletion if that is possible with the input stream. You can override the default implementation by installing a pointer to your own function in this interface after the recognizer has initialized. This can perform different recovery options or not recover at all and so on. To ignore recovery altogether, see the comments in the default implementation of this function in <code>antlr3baserecognizer.c</code> </p>
<p> Note that errors are signalled by setting the error flag below and creating a new exception structure and installing it in the exception pointer below (you can chain these if you like and handle them in some customized way). </p>
<p> Referenced by antlr3BaseRecognizerNew().</p>
<h3>void(* <code>ANTLR3_BASE_RECOGNIZER_struct::matchAny</code>)(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>)</h3>
<p> Pointer to a function that matches the next token/char in the input stream regardless of what it actually is. </p>
<p> Referenced by antlr3BaseRecognizerNew().</p>
<h3>void(* <code>ANTLR3_BASE_RECOGNIZER_struct::memoize</code>)(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>, <code>ANTLR3_MARKER</code> ruleIndex, <code>ANTLR3_MARKER</code> ruleParseStart)</h3>
<p> Pointer to function that records whether the rule has parsed the input at a current position successfully or not. </p>
<p> Referenced by antlr3BaseRecognizerNew().</p>
<h3>void(* <code>ANTLR3_BASE_RECOGNIZER_struct::mismatch</code>)(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>, <code>ANTLR3_UINT32</code> ttype, <code>pANTLR3_BITSET_LIST</code> <code>follow</code>)</h3>
<p> Pointer to a function that works out what to do when a token mismatch occurs, so that Tree parsers can behave differently to other recognizers. </p>
<p> Referenced by antlr3BaseRecognizerNew(), and antlr3TreeParserNewStream().</p>
<h3><code>ANTLR3_BOOLEAN</code>(* <code>ANTLR3_BASE_RECOGNIZER_struct::mismatchIsMissingToken</code>)(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>, <code>pANTLR3_INT_STREAM</code> input, <code>pANTLR3_BITSET_LIST</code> <code>follow</code>)</h3>
<p> Pointer to a function that decides if the current token is one that can logically follow the one we were looking for, in which case the one we were looking for is probably missing from the input. </p>
<p> Referenced by antlr3BaseRecognizerNew(), and recoverFromMismatchedSet().</p>
<h3><code>ANTLR3_BOOLEAN</code>(* <code>ANTLR3_BASE_RECOGNIZER_struct::mismatchIsUnwantedToken</code>)(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>, <code>pANTLR3_INT_STREAM</code> input, <code>ANTLR3_UINT32</code> ttype)</h3>
<p> Pointer to a function that decides if the token ahead of the current one is the one we were loking for, in which case the curernt one is very likely extraneous and can be reported that way. </p>
<p> Referenced by antlr3BaseRecognizerNew(), and recoverFromMismatchedToken().</p>
<h3>struct <code>ANTLR3_BASE_RECOGNIZER_struct</code>* <code>ANTLR3_BASE_RECOGNIZER_struct::recognizer</code> [read]</h3>
<p> Pointer to common routine to handle single token insertion for recovery functions.</p>
<h3>void(* <code>ANTLR3_BASE_RECOGNIZER_struct::recover</code>)(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>)</h3>
<p> Pointer to a function that recovers from an error found in the input stream. Generally, this will be a ANTLR3_EXCEPTION_NOVIABLE_ALT but it could also be from a mismatched token that the (*match)() could not recover from. </p>
<p> Referenced by antlr3BaseRecognizerNew().</p>
<h3>void*(* <code>ANTLR3_BASE_RECOGNIZER_struct::recoverFromMismatchedSet</code>)(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>, <code>pANTLR3_BITSET_LIST</code> <code>follow</code>)</h3>
<p> Pointer to a function that recovers from a mismatched set in the token stream, in a similar manner to (*recoverFromMismatchedToken). </p>
<p> Referenced by antlr3BaseRecognizerNew().</p>
<h3>void*(* <code>ANTLR3_BASE_RECOGNIZER_struct::recoverFromMismatchedToken</code>)(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>, <code>ANTLR3_UINT32</code> ttype, <code>pANTLR3_BITSET_LIST</code> <code>follow</code>)</h3>
<p> Pointer to a function that recovers from a mismatched token in the input stream. <code>See also:</code></p>
<dl>
<dt>
<dd> antlr3RecoverMismatch() for details.</dl>
<p> Referenced by antlr3BaseRecognizerNew(), match(), and mismatch().</p>
<h3>void(* <code>ANTLR3_BASE_RECOGNIZER_struct::reportError</code>)(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>)</h3>
<p> Pointer to a function to call to report a recognition problem. You may override this function with your own function, but refer to the standard implementation in <code>antlr3baserecognizer.c</code> for guidance. The function should recognize whether error recovery is in force, so that it does not print out more than one error messages for the same error. From the java comments in BaseRecognizer.java: </p>
<p> This method sets errorRecovery to indicate the parser is recovering not parsing. Once in recovery mode, no errors are generated. To get out of recovery mode, the parser must successfully match a token (after a resync). So it will go: </p>
<p> 1. error occurs 2. enter recovery mode, report error 3. consume until token found in resynch set 4. try to resume parsing 5. next <code>match()</code> will reset errorRecovery mode </p>
<p> Referenced by antlr3BaseRecognizerNew(), antlr3LexerNew(), nextTokenStr(), recoverFromMismatchedElement(), recoverFromMismatchedSet(), and recoverFromMismatchedToken().</p>
<h3>void(* <code>ANTLR3_BASE_RECOGNIZER_struct::reset</code>)(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>)</h3>
<p> Reset the recognizer. </p>
<p> Referenced by antlr3BaseRecognizerNew(), antlr3LexerNew(), setTokenStream(), and setTreeNodeStream().</p>
<h3><code>pANTLR3_RECOGNIZER_SHARED_STATE</code> <code>ANTLR3_BASE_RECOGNIZER_struct::state</code></h3>
<p> A pointer to the shared recognizer state, such that multiple recognizers can use the same inputs streams and so on (in the case of grammar inheritance for instance. </p>
<p> Referenced by alreadyParsedRule(), antlr3BaseRecognizerNew(), antlr3dfapredict(), antlr3LexerNew(), antlr3MTExceptionNew(), antlr3MTNExceptionNew(), antlr3RecognitionExceptionNew(), antlr3RewriteRuleElementStreamNewAE(), combineFollows(), displayRecognitionError(), emit(), emitNew(), freeBR(), freeLexer(), freeNodeRS(), freeParser(), freeRS(), getMissingSymbol(), getNumberOfSyntaxErrors(), getRuleMemoization(), getText(), match(), matchAny(), matchc(), matchRange(), matchs(), memoize(), mismatch(), mismatchIsMissingToken(), mismatchIsUnwantedToken(), nextToken(), nextTokenStr(), noViableAlt(), popCharStream(), pushCharStream(), recover(), recoverFromMismatchedElement(), recoverFromMismatchedSet(), recoverFromMismatchedToken(), reportError(), reset(), setCharStream(), and synpred().</p>
<h3>void* <code>ANTLR3_BASE_RECOGNIZER_struct::super</code></h3>
<p> Whatever super structure is providing this interface needs a pointer to itself so that this can be passed back to it whenever the api functions are called back from here. </p>
<p> Referenced by alreadyParsedRule(), antlr3LexerNew(), antlr3ParserNew(), antlr3RecognitionExceptionNew(), antlr3TreeParserNewStream(), consumeUntil(), consumeUntilSet(), displayRecognitionError(), match(), matchAny(), memoize(), mismatch(), recover(), recoverFromMismatchedElement(), recoverFromMismatchedSet(), recoverFromMismatchedToken(), reset(), and synpred().</p>
<h3><code>ANTLR3_BOOLEAN</code>(* <code>ANTLR3_BASE_RECOGNIZER_struct::synpred</code>)(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>, void *ctx, void(*predicate)(void *ctx))</h3>
<p> Pointer to a function that returns whether the supplied grammar function will parse the current input stream or not. This is the way that syntactic predicates are evaluated. Unlike java, C is perfectly happy to invoke code via a pointer to a function (hence that&#8217;s what all the ANTLR3 C interfaces do. </p>
<p> Referenced by antlr3BaseRecognizerNew().</p>
<h3><code>pANTLR3_HASH_TABLE</code>(* <code>ANTLR3_BASE_RECOGNIZER_struct::toStrings</code>)(struct <code>ANTLR3_BASE_RECOGNIZER_struct</code> *<code>recognizer</code>, <code>pANTLR3_HASH_TABLE</code>)</h3>
<p> Pointer to a function that converts an ANLR3_LIST of tokens to an ANTLR3_LIST of string token names. As this is mostly used in string template processing it may not be useful in the C runtime. </p>
<p> Referenced by antlr3BaseRecognizerNew().</p>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_BASE_RECOGNIZER_struct::type</code></h3>
<p> Indicates the type of recognizer that we are an instance of. The programmer may set this to anything of course, but the default implementations of the interface only really understand the built in types, so new error handlers etc would probably be required to as well. </p>
<p> Valid types are: </p>
<dl>
<dt>*</p>
<dd> <code>ANTLR3_TYPE_LEXER</code></p>
<dt>*</p>
<dd> <code>ANTLR3_TYPE_PARSER</code></p>
<dt>*</p>
<dd> <code>ANTLR3_TYPE_TREE_PARSER</code></dl>
<p> Referenced by alreadyParsedRule(), antlr3BaseRecognizerNew(), antlr3RecognitionExceptionNew(), antlr3TreeParserNewStream(), consumeUntil(), consumeUntilSet(), displayRecognitionError(), match(), matchAny(), memoize(), mismatch(), recover(), recoverFromMismatchedElement(), recoverFromMismatchedSet(), recoverFromMismatchedToken(), and synpred(). </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for ANTLR3C from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbBS">Author</a></p>
<dd></dl>
