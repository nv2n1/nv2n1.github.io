---
title: "antlr3-tokensource(3)"
name: "antlr3-tokensource"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-tokensource/"
description: "ANTLR3_TOKEN_STREAM_struct –"
---

<p>ANTLR3_TOKEN_STREAM_struct &#8211; </p>
<p> Definition of the ANTLR3 common token stream interface.</p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/antlr3tokenstream.h">antlr3tokenstream.h</a>&gt;</p>
<h3>Data Fields</h3>
<p><code>pANTLR3_COMMON_TOKEN</code>(* <code>_LT</code> )(struct <code>ANTLR3_TOKEN_STREAM_struct</code> *tokenStream, <code>ANTLR3_INT32</code> k)<br />
 <i>Get Token at current input pointer + i ahead where i=1 is next Token. </i><br />
 <code>pANTLR3_DEBUG_EVENT_LISTENER</code> <code>debugger</code><br />
 <i>Debugger interface, is this is a debugging token stream. </i><br />
 void(* <code>free</code> )(struct <code>ANTLR3_TOKEN_STREAM_struct</code> *tokenStream)<br />
 <i>Function that knows how to free the memory for an ANTLR3_TOKEN_STREAM. </i><br />
 <code>pANTLR3_COMMON_TOKEN</code>(* <code>get</code> )(struct <code>ANTLR3_TOKEN_STREAM_struct</code> *tokenStream, <code>ANTLR3_UINT32</code> i)<br />
 <i>Get a token at an absolute index i; 0..n-1. </i><br />
 <code>pANTLR3_TOKEN_SOURCE</code>(* <code>getTokenSource</code> )(struct <code>ANTLR3_TOKEN_STREAM_struct</code> *tokenStream)<br />
 <i>Where is this stream pulling tokens from? This is not the name, but a pointer into an interface that contains a ANTLR3_TOKEN_SOURCE interface. </i><br />
 <code>ANTLR3_BOOLEAN</code> <code>initialStreamState</code><br />
 <i>Indicates the initial stream state for </i><code>dbgConsume()</code>.<br />
 <code>pANTLR3_INT_STREAM</code> <code>istream</code><br />
 <i>All input streams implement the ANTLR3_INT_STREAM interface. </i><br />
 void(* <code>setDebugListener</code> )(struct <code>ANTLR3_TOKEN_STREAM_struct</code> *tokenStream, <code>pANTLR3_DEBUG_EVENT_LISTENER</code> <code>debugger</code>)<br />
 <i>Function that sets the token stream into debugging mode. </i><br />
 void(* <code>setTokenSource</code> )(struct <code>ANTLR3_TOKEN_STREAM_struct</code> *tokenStream, <code>pANTLR3_TOKEN_SOURCE</code> <code>tokenSource</code>)<br />
 <i>Function that installs a token source for teh stream. </i><br />
 void * <code>super</code><br />
 <i>Whatever is providing this interface needs a pointer to itself so that this can be passed back to it whenever the api functions are called. </i><br />
 <code>pANTLR3_TOKEN_SOURCE</code> <code>tokenSource</code><br />
 <i>Pointer to the token source for this stream. </i><br />
 <code>pANTLR3_STRING</code>(* <code>toString</code> )(struct <code>ANTLR3_TOKEN_STREAM_struct</code> *tokenStream)<br />
 <i>Return the text of all the tokens in the stream, as the old tramp in Leeds market used to say; &#8216;Get the lot!&#8217;. </i><br />
 <code>pANTLR3_STRING</code>(* <code>toStringSS</code> )(struct <code>ANTLR3_TOKEN_STREAM_struct</code> *tokenStream, <code>ANTLR3_UINT32</code> start, <code>ANTLR3_UINT32</code> stop)<br />
 <i>Return the text of all tokens from start to stop, inclusive. </i><br />
 <code>pANTLR3_STRING</code>(* <code>toStringTT</code> )(struct <code>ANTLR3_TOKEN_STREAM_struct</code> *tokenStream, <code>pANTLR3_COMMON_TOKEN</code> start, <code>pANTLR3_COMMON_TOKEN</code> stop)<br />
 <i>Because the user is not required to use a token with an index stored in it, we must provide a means for two token objects themselves to indicate the start/end location. </i></p>
<h2>Detailed Description</h2>
<p>Definition of the ANTLR3 common token stream interface. </p>
<p> <code>Remarks:</code></p>
<dl COMPACT>
<dd>Much of the documentation for this interface is stolen from Ter&#8217;s Java implementation.</dl>
<h2>Field Documentation</h2>
<h3><code>pANTLR3_COMMON_TOKEN</code>(* <code>ANTLR3_TOKEN_STREAM_struct::_LT</code>)(struct <code>ANTLR3_TOKEN_STREAM_struct</code> *tokenStream, <code>ANTLR3_INT32</code> k)</h3>
<p>Get Token at current input pointer + i ahead where i=1 is next Token. i&lt;0 indicates tokens in the past. So -1 is previous token and -2 is two tokens ago. LT(0) is undefined. For i&gt;=n, return Token.EOFToken. Return null for LT(0) and any index that results in an absolute address that is negative. </p>
<p> Referenced by antlr3CommonTokenDebugStreamSourceNew(), antlr3CommonTokenStreamNew(), antlr3RecognitionExceptionNew(), dbgConsume(), getMissingSymbol(), and setDebugListener().</p>
<h3><code>pANTLR3_DEBUG_EVENT_LISTENER</code> <code>ANTLR3_TOKEN_STREAM_struct::debugger</code></h3>
<p>Debugger interface, is this is a debugging token stream. </p>
<p> Referenced by antlr3CommonTokenDebugStreamSourceNew(), consumeInitialHiddenTokens(), dbgConsume(), and setDebugListener().</p>
<h3>void(* <code>ANTLR3_TOKEN_STREAM_struct::free</code>)(struct <code>ANTLR3_TOKEN_STREAM_struct</code> *tokenStream)</h3>
<p>Function that knows how to free the memory for an ANTLR3_TOKEN_STREAM. </p>
<p> Referenced by antlr3CTSFree(), and antlr3TokenStreamNew().</p>
<h3><code>pANTLR3_COMMON_TOKEN</code>(* <code>ANTLR3_TOKEN_STREAM_struct::get</code>)(struct <code>ANTLR3_TOKEN_STREAM_struct</code> *tokenStream, <code>ANTLR3_UINT32</code> i)</h3>
<p>Get a token at an absolute index i; 0..n-1. This is really only needed for profiling and debugging and token stream rewriting. If you don&#8217;t want to buffer up tokens, then this method makes no sense for you. Naturally you can&#8217;t use the rewrite stream feature. I believe DebugTokenStream can easily be altered to not use this method, removing the dependency. </p>
<p> Referenced by antlr3CommonTokenStreamNew(), consumeInitialHiddenTokens(), dbgConsume(), getTokensSet(), and toStringSS().</p>
<h3><code>pANTLR3_TOKEN_SOURCE</code>(* <code>ANTLR3_TOKEN_STREAM_struct::getTokenSource</code>)(struct <code>ANTLR3_TOKEN_STREAM_struct</code> *tokenStream)</h3>
<p>Where is this stream pulling tokens from? This is not the name, but a pointer into an interface that contains a ANTLR3_TOKEN_SOURCE interface. The Token Source interface contains a pointer to the input stream and a pointer to a function that returns the next token. </p>
<p> Referenced by antlr3CommonTokenStreamNew(), and toStringSS().</p>
<h3><code>ANTLR3_BOOLEAN</code> <code>ANTLR3_TOKEN_STREAM_struct::initialStreamState</code></h3>
<p>Indicates the initial stream state for <code>dbgConsume()</code>. </p>
<p> Referenced by antlr3CommonTokenDebugStreamSourceNew(), consumeInitialHiddenTokens(), dbgConsume(), dbgTokLT(), and setDebugListener().</p>
<h3><code>pANTLR3_INT_STREAM</code> <code>ANTLR3_TOKEN_STREAM_struct::istream</code></h3>
<p>All input streams implement the ANTLR3_INT_STREAM interface. .. </p>
<p> Referenced by alreadyParsedRule(), antlr3CommonTokenDebugStreamSourceNew(), antlr3CommonTokenStreamNew(), antlr3CTSFree(), antlr3RecognitionExceptionNew(), consumeUntil(), consumeUntilSet(), dbgTokLT(), displayRecognitionError(), getTokensSet(), match(), matchAny(), memoize(), mismatch(), recover(), recoverFromMismatchedElement(), recoverFromMismatchedSet(), recoverFromMismatchedToken(), setDebugListener(), synpred(), tokLT(), toString(), and toStringSS().</p>
<h3>void(* <code>ANTLR3_TOKEN_STREAM_struct::setDebugListener</code>)(struct <code>ANTLR3_TOKEN_STREAM_struct</code> *tokenStream, <code>pANTLR3_DEBUG_EVENT_LISTENER</code> <code>debugger</code>)</h3>
<p>Function that sets the token stream into debugging mode. </p>
<p> Referenced by antlr3CommonTokenStreamNew(), and setDebugListener().</p>
<h3>void(* <code>ANTLR3_TOKEN_STREAM_struct::setTokenSource</code>)(struct <code>ANTLR3_TOKEN_STREAM_struct</code> *tokenStream, <code>pANTLR3_TOKEN_SOURCE</code> <code>tokenSource</code>)</h3>
<p>Function that installs a token source for teh stream. </p>
<p> Referenced by antlr3CommonTokenStreamNew(), and antlr3CommonTokenStreamSourceNew().</p>
<h3>void* <code>ANTLR3_TOKEN_STREAM_struct::super</code></h3>
<p>Whatever is providing this interface needs a pointer to itself so that this can be passed back to it whenever the api functions are called. </p>
<p> Referenced by antlr3CommonTokenStreamNew(), antlr3CTSFree(), antlr3RecognitionExceptionNew(), consume(), get(), getMissingSymbol(), tokLT(), toString(), and toStringSS().</p>
<h3><code>pANTLR3_TOKEN_SOURCE</code> <code>ANTLR3_TOKEN_STREAM_struct::tokenSource</code></h3>
<p>Pointer to the token source for this stream. </p>
<p> Referenced by getTokenSource(), setTokenSource(), and tokLT().</p>
<h3><code>pANTLR3_STRING</code>(* <code>ANTLR3_TOKEN_STREAM_struct::toString</code>)(struct <code>ANTLR3_TOKEN_STREAM_struct</code> *tokenStream)</h3>
<p>Return the text of all the tokens in the stream, as the old tramp in Leeds market used to say; &#8216;Get the lot!&#8217;. </p>
<p> Referenced by antlr3CommonTokenStreamNew().</p>
<h3><code>pANTLR3_STRING</code>(* <code>ANTLR3_TOKEN_STREAM_struct::toStringSS</code>)(struct <code>ANTLR3_TOKEN_STREAM_struct</code> *tokenStream, <code>ANTLR3_UINT32</code> start, <code>ANTLR3_UINT32</code> stop)</h3>
<p>Return the text of all tokens from start to stop, inclusive. If the stream does not buffer all the tokens then it can just return an empty ANTLR3_STRING or NULL; Grammars should not access $ruleLabel.text in an action in that case. </p>
<p> Referenced by antlr3CommonTokenStreamNew(), toString(), and toStringTT().</p>
<h3><code>pANTLR3_STRING</code>(* <code>ANTLR3_TOKEN_STREAM_struct::toStringTT</code>)(struct <code>ANTLR3_TOKEN_STREAM_struct</code> *tokenStream, <code>pANTLR3_COMMON_TOKEN</code> start, <code>pANTLR3_COMMON_TOKEN</code> stop)</h3>
<p>Because the user is not required to use a token with an index stored in it, we must provide a means for two token objects themselves to indicate the start/end location. Most often this will just delegate to the other toString(int,int). This is also parallel with the pTREENODE_STREAM-&gt;toString(Object,Object). </p>
<p> Referenced by antlr3CommonTokenStreamNew(). </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
