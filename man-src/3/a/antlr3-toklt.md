---
title: "antlr3-toklt(3)"
name: "antlr3-toklt"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-toklt/"
description: "src/antlr3tokenstream.c –"
---

<p>src/antlr3tokenstream.c &#8211; </p>
<p> Default implementation of CommonTokenStream.</p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/antlr3tokenstream.h">antlr3tokenstream.h</a>&gt; </p>
<h3>Functions</h3>
<p>static <code>ANTLR3_UINT32</code> <code>_LA</code> (<code>pANTLR3_INT_STREAM</code> is, <code>ANTLR3_INT32</code> i) </p>
<p> ANTLR3_API <code>pANTLR3_COMMON_TOKEN_STREAM</code> <code>antlr3CommonTokenDebugStreamSourceNew</code> (<code>ANTLR3_UINT32</code> hint, <code>pANTLR3_TOKEN_SOURCE</code> source, <code>pANTLR3_DEBUG_EVENT_LISTENER</code> debugger) </p>
<p> ANTLR3_API <code>pANTLR3_COMMON_TOKEN_STREAM</code> <code>antlr3CommonTokenStreamNew</code> (<code>ANTLR3_UINT32</code> hint) </p>
<p> ANTLR3_API <code>pANTLR3_COMMON_TOKEN_STREAM</code> <code>antlr3CommonTokenStreamSourceNew</code> (<code>ANTLR3_UINT32</code> hint, <code>pANTLR3_TOKEN_SOURCE</code> source) </p>
<p> static void <code>antlr3CTSFree</code> (<code>pANTLR3_COMMON_TOKEN_STREAM</code> stream) </p>
<p> static void <code>antlr3TokenStreamFree</code> (<code>pANTLR3_TOKEN_STREAM</code> stream) </p>
<p> ANTLR3_API <code>pANTLR3_TOKEN_STREAM</code> <code>antlr3TokenStreamNew</code> () </p>
<p> static void <code>consume</code> (<code>pANTLR3_INT_STREAM</code> is)<br />
 <i>Move the input pointer to the next incoming token. </i><br />
 static void <code>consumeInitialHiddenTokens</code> (<code>pANTLR3_INT_STREAM</code> is)<br />
 <i>Debug only method to flag consumption of initial off-channel tokens in the input stream. </i><br />
 static void <code>dbgConsume</code> (<code>pANTLR3_INT_STREAM</code> is)<br />
 <i>As per ordinary consume but notifies the debugger about hidden tokens and so on. </i><br />
 static <code>ANTLR3_UINT32</code> <code>dbgLA</code> (<code>pANTLR3_INT_STREAM</code> is, <code>ANTLR3_INT32</code> i) </p>
<p> static <code>ANTLR3_MARKER</code> <code>dbgMark</code> (<code>pANTLR3_INT_STREAM</code> is) </p>
<p> static void <code>dbgRewindLast</code> (<code>pANTLR3_INT_STREAM</code> is) </p>
<p> static void <code>dbgRewindStream</code> (<code>pANTLR3_INT_STREAM</code> is, <code>ANTLR3_MARKER</code> marker) </p>
<p> static void <code>dbgSeek</code> (<code>pANTLR3_INT_STREAM</code> is, <code>ANTLR3_MARKER</code> index) </p>
<p> static <code>pANTLR3_COMMON_TOKEN</code> <code>dbgTokLT</code> (<code>pANTLR3_TOKEN_STREAM</code> ts, <code>ANTLR3_INT32</code> k)<br />
 <i>As per the normal tokLT but sends information to the debugger. </i><br />
 static void <code>discardOffChannel</code> (<code>pANTLR3_COMMON_TOKEN_STREAM</code> cts, <code>ANTLR3_BOOLEAN</code> discard) </p>
<p> static void <code>discardTokenType</code> (<code>pANTLR3_COMMON_TOKEN_STREAM</code> cts, <code>ANTLR3_INT32</code> ttype) </p>
<p> static void <code>fillBuffer</code> (<code>pANTLR3_COMMON_TOKEN_STREAM</code> tokenStream) </p>
<p> static <code>pANTLR3_COMMON_TOKEN</code> <code>get</code> (<code>pANTLR3_TOKEN_STREAM</code> ts, <code>ANTLR3_UINT32</code> i) </p>
<p> static <code>pANTLR3_STRING</code> <code>getSourceName</code> (<code>pANTLR3_INT_STREAM</code> is) </p>
<p> static <code>pANTLR3_LIST</code> <code>getTokenRange</code> (<code>pANTLR3_COMMON_TOKEN_STREAM</code> cts, <code>ANTLR3_UINT32</code> start, <code>ANTLR3_UINT32</code> stop) </p>
<p> static <code>pANTLR3_VECTOR</code> <code>getTokens</code> (<code>pANTLR3_COMMON_TOKEN_STREAM</code> cts) </p>
<p> static <code>pANTLR3_LIST</code> <code>getTokensList</code> (<code>pANTLR3_COMMON_TOKEN_STREAM</code> cts, <code>ANTLR3_UINT32</code> start, <code>ANTLR3_UINT32</code> stop, <code>pANTLR3_LIST</code> list) </p>
<p> static <code>pANTLR3_TOKEN_SOURCE</code> <code>getTokenSource</code> (<code>pANTLR3_TOKEN_STREAM</code> ts) </p>
<p> static <code>pANTLR3_LIST</code> <code>getTokensSet</code> (<code>pANTLR3_COMMON_TOKEN_STREAM</code> tokenStream, <code>ANTLR3_UINT32</code> start, <code>ANTLR3_UINT32</code> stop, <code>pANTLR3_BITSET</code> types)<br />
 <i>Given a start and stop index, return a List of all tokens in the token type BitSet. </i><br />
 static <code>pANTLR3_LIST</code> <code>getTokensType</code> (<code>pANTLR3_COMMON_TOKEN_STREAM</code> cts, <code>ANTLR3_UINT32</code> start, <code>ANTLR3_UINT32</code> stop, <code>ANTLR3_UINT32</code> type) </p>
<p> static <code>pANTLR3_COMMON_TOKEN</code> <code>LB</code> (<code>pANTLR3_COMMON_TOKEN_STREAM</code> tokenStream, <code>ANTLR3_INT32</code> i) </p>
<p> static <code>ANTLR3_MARKER</code> <code>mark</code> (<code>pANTLR3_INT_STREAM</code> is) </p>
<p> static void <code>release</code> (<code>pANTLR3_INT_STREAM</code> is, <code>ANTLR3_MARKER</code> mark) </p>
<p> static void <code>rewindLast</code> (<code>pANTLR3_INT_STREAM</code> is) </p>
<p> static void <code>rewindStream</code> (<code>pANTLR3_INT_STREAM</code> is, <code>ANTLR3_MARKER</code> marker) </p>
<p> static void <code>seek</code> (<code>pANTLR3_INT_STREAM</code> is, <code>ANTLR3_MARKER</code> index) </p>
<p> static void <code>setDebugListener</code> (<code>pANTLR3_TOKEN_STREAM</code> ts, <code>pANTLR3_DEBUG_EVENT_LISTENER</code> debugger) </p>
<p> static void <code>setTokenSource</code> (<code>pANTLR3_TOKEN_STREAM</code> ts, <code>pANTLR3_TOKEN_SOURCE</code> tokenSource) </p>
<p> static void <code>setTokenTypeChannel</code> (<code>pANTLR3_COMMON_TOKEN_STREAM</code> tokenStream, <code>ANTLR3_UINT32</code> ttype, <code>ANTLR3_UINT32</code> channel)<br />
 <i>A simple filter mechanism whereby you can tell this token stream to force all tokens of type ttype to be on channel. </i><br />
 static <code>ANTLR3_UINT32</code> <code>size</code> (<code>pANTLR3_INT_STREAM</code> is) </p>
<p> static <code>ANTLR3_UINT32</code> <code>skipOffTokenChannels</code> (<code>pANTLR3_COMMON_TOKEN_STREAM</code> tokenStream, <code>ANTLR3_INT32</code> i) </p>
<p> static <code>ANTLR3_UINT32</code> <code>skipOffTokenChannelsReverse</code> (<code>pANTLR3_COMMON_TOKEN_STREAM</code> tokenStream, <code>ANTLR3_INT32</code> i) </p>
<p> static <code>ANTLR3_MARKER</code> <code>tindex</code> (<code>pANTLR3_INT_STREAM</code> is) </p>
<p> static <code>pANTLR3_COMMON_TOKEN</code> <code>tokLT</code> (<code>pANTLR3_TOKEN_STREAM</code> ts, <code>ANTLR3_INT32</code> k)<br />
 <i>Get the ith token from the current position 1..n where k=1 is the first symbol of lookahead. </i><br />
 static <code>pANTLR3_STRING</code> <code>toString</code> (<code>pANTLR3_TOKEN_STREAM</code> ts) </p>
<p> static <code>pANTLR3_STRING</code> <code>toStringSS</code> (<code>pANTLR3_TOKEN_STREAM</code> ts, <code>ANTLR3_UINT32</code> start, <code>ANTLR3_UINT32</code> stop) </p>
<p> static <code>pANTLR3_STRING</code> <code>toStringTT</code> (<code>pANTLR3_TOKEN_STREAM</code> ts, <code>pANTLR3_COMMON_TOKEN</code> start, <code>pANTLR3_COMMON_TOKEN</code> stop) </p>
<h2>Detailed Description</h2>
<p>Default implementation of CommonTokenStream. </p>
<h2>Function Documentation</h2>
<h3>static <code>ANTLR3_UINT32</code> _LA (<code>pANTLR3_INT_STREAM</code> is, <code>ANTLR3_INT32</code> i) [static]</h3>
<p>Referenced by antlr3CommonTokenStreamNew().</p>
<h3>ANTLR3_API <code>pANTLR3_COMMON_TOKEN_STREAM</code> antlr3CommonTokenDebugStreamSourceNew (<code>ANTLR3_UINT32</code> hint, <code>pANTLR3_TOKEN_SOURCE</code> source, <code>pANTLR3_DEBUG_EVENT_LISTENER</code> debugger)</h3>
<p>References ANTLR3_INT_STREAM_struct::_LA, ANTLR3_TOKEN_STREAM_struct::_LT, ANTLR3_FALSE, antlr3CommonTokenStreamSourceNew(), ANTLR3_INT_STREAM_struct::consume, dbgConsume(), dbgLA(), dbgMark(), dbgRewindLast(), dbgRewindStream(), dbgSeek(), dbgTokLT(), ANTLR3_TOKEN_STREAM_struct::debugger, ANTLR3_TOKEN_STREAM_struct::initialStreamState, ANTLR3_TOKEN_STREAM_struct::istream, ANTLR3_INT_STREAM_struct::mark, ANTLR3_INT_STREAM_struct::rewind, ANTLR3_INT_STREAM_struct::rewindLast, ANTLR3_INT_STREAM_struct::seek, and ANTLR3_COMMON_TOKEN_STREAM_struct::tstream.</p>
<h3>ANTLR3_API <code>pANTLR3_COMMON_TOKEN_STREAM</code> antlr3CommonTokenStreamNew (<code>ANTLR3_UINT32</code> hint)</h3>
<p>References _LA(), ANTLR3_INT_STREAM_struct::_LA, ANTLR3_TOKEN_STREAM_struct::_LT, ANTLR3_MALLOC, ANTLR3_TOKENSTREAM, antlr3IntStreamNew(), antlr3TokenStreamNew(), antlr3VectorNew(), consume(), ANTLR3_INT_STREAM_struct::consume, discardOffChannel(), ANTLR3_COMMON_TOKEN_STREAM_struct::discardOffChannelToks, discardTokenType(), ANTLR3_COMMON_TOKEN_STREAM_struct::discardTokenType, ANTLR3_TOKEN_STREAM_struct::get, getSourceName(), ANTLR3_INT_STREAM_struct::getSourceName, getTokenRange(), ANTLR3_COMMON_TOKEN_STREAM_struct::getTokenRange, getTokens(), ANTLR3_COMMON_TOKEN_STREAM_struct::getTokens, getTokensList(), ANTLR3_COMMON_TOKEN_STREAM_struct::getTokensList, getTokenSource(), ANTLR3_TOKEN_STREAM_struct::getTokenSource, getTokensSet(), ANTLR3_COMMON_TOKEN_STREAM_struct::getTokensSet, getTokensType(), ANTLR3_COMMON_TOKEN_STREAM_struct::getTokensType, ANTLR3_INT_STREAM_struct::index, ANTLR3_TOKEN_STREAM_struct::istream, mark(), ANTLR3_INT_STREAM_struct::mark, ANTLR3_COMMON_TOKEN_STREAM_struct::p, release(), ANTLR3_INT_STREAM_struct::release, ANTLR3_INT_STREAM_struct::rewind, rewindLast(), ANTLR3_INT_STREAM_struct::rewindLast, rewindStream(), seek(), ANTLR3_INT_STREAM_struct::seek, setDebugListener(), ANTLR3_TOKEN_STREAM_struct::setDebugListener, setTokenSource(), ANTLR3_TOKEN_STREAM_struct::setTokenSource, setTokenTypeChannel(), ANTLR3_COMMON_TOKEN_STREAM_struct::setTokenTypeChannel, size(), ANTLR3_INT_STREAM_struct::size, ANTLR3_INT_STREAM_struct::super, ANTLR3_TOKEN_STREAM_struct::super, tindex(), ANTLR3_COMMON_TOKEN_STREAM_struct::tokens, tokLT(), toString(), ANTLR3_TOKEN_STREAM_struct::toString, toStringSS(), ANTLR3_TOKEN_STREAM_struct::toStringSS, toStringTT(), ANTLR3_TOKEN_STREAM_struct::toStringTT, ANTLR3_COMMON_TOKEN_STREAM_struct::tstream, and ANTLR3_INT_STREAM_struct::type. </p>
<p> Referenced by antlr3CommonTokenStreamSourceNew().</p>
<h3>ANTLR3_API <code>pANTLR3_COMMON_TOKEN_STREAM</code> antlr3CommonTokenStreamSourceNew (<code>ANTLR3_UINT32</code> hint, <code>pANTLR3_TOKEN_SOURCE</code> source)</h3>
<p>References ANTLR3_FALSE, ANTLR3_TOKEN_DEFAULT_CHANNEL, antlr3CommonTokenStreamNew(), antlr3CTSFree(), ANTLR3_COMMON_TOKEN_STREAM_struct::channel, ANTLR3_COMMON_TOKEN_STREAM_struct::channelOverrides, ANTLR3_COMMON_TOKEN_STREAM_struct::discardOffChannel, ANTLR3_COMMON_TOKEN_STREAM_struct::discardSet, ANTLR3_COMMON_TOKEN_STREAM_struct::free, ANTLR3_TOKEN_STREAM_struct::setTokenSource, and ANTLR3_COMMON_TOKEN_STREAM_struct::tstream. </p>
<p> Referenced by antlr3CommonTokenDebugStreamSourceNew().</p>
<h3>static void antlr3CTSFree (<code>pANTLR3_COMMON_TOKEN_STREAM</code> stream) [static]</h3>
<p>References ANTLR3_FREE, ANTLR3_COMMON_TOKEN_STREAM_struct::channelOverrides, ANTLR3_COMMON_TOKEN_STREAM_struct::discardSet, ANTLR3_LIST_struct::free, ANTLR3_TOKEN_STREAM_struct::free, ANTLR3_INT_STREAM_struct::free, ANTLR3_TOKEN_STREAM_struct::istream, ANTLR3_INT_STREAM_struct::super, ANTLR3_TOKEN_STREAM_struct::super, ANTLR3_COMMON_TOKEN_STREAM_struct::tokens, and ANTLR3_COMMON_TOKEN_STREAM_struct::tstream. </p>
<p> Referenced by antlr3CommonTokenStreamSourceNew().</p>
<h3>static void antlr3TokenStreamFree (<code>pANTLR3_TOKEN_STREAM</code> stream) [static]</h3>
<p>References ANTLR3_FREE. </p>
<p> Referenced by antlr3TokenStreamNew().</p>
<h3>ANTLR3_API <code>pANTLR3_TOKEN_STREAM</code> antlr3TokenStreamNew ()</h3>
<p>References ANTLR3_MALLOC, antlr3TokenStreamFree(), and ANTLR3_TOKEN_STREAM_struct::free. </p>
<p> Referenced by antlr3CommonTokenStreamNew().</p>
<h3>static void consume (<code>pANTLR3_INT_STREAM</code> is) [static]</h3>
<p>Move the input pointer to the next incoming token. The stream must become active with <a href="/docs/linux/man/1-lt/">LT</a>(1) available. <code>consume()</code> simply moves the input pointer so that <a href="/docs/linux/man/1-lt/">LT</a>(1) points at the next input symbol. Consume at least one token. </p>
<p> Walk past any token not on the channel the parser is listening to. </p>
<p> References ANTLR3_COMMON_TOKEN_STREAM_struct::p, ANTLR3_VECTOR_struct::size, skipOffTokenChannels(), ANTLR3_TOKEN_STREAM_struct::super, ANTLR3_INT_STREAM_struct::super, and ANTLR3_COMMON_TOKEN_STREAM_struct::tokens. </p>
<p> Referenced by antlr3CommonTokenStreamNew(), and dbgConsume().</p>
<h3>static void consumeInitialHiddenTokens (<code>pANTLR3_INT_STREAM</code> is) [static]</h3>
<p>Debug only method to flag consumption of initial off-channel tokens in the input stream. </p>
<p> References ANTLR3_FALSE, ANTLR3_DEBUG_EVENT_LISTENER_struct::consumeHiddenToken, ANTLR3_TOKEN_STREAM_struct::debugger, ANTLR3_TOKEN_STREAM_struct::get, ANTLR3_INT_STREAM_struct::index, ANTLR3_TOKEN_STREAM_struct::initialStreamState, and ANTLR3_INT_STREAM_struct::super. </p>
<p> Referenced by dbgConsume(), and dbgTokLT().</p>
<h3>static void dbgConsume (<code>pANTLR3_INT_STREAM</code> is) [static]</h3>
<p>As per ordinary consume but notifies the debugger about hidden tokens and so on. </p>
<p> References ANTLR3_TOKEN_STREAM_struct::_LT, ANTLR3_TRUE, consume(), ANTLR3_DEBUG_EVENT_LISTENER_struct::consumeHiddenToken, consumeInitialHiddenTokens(), ANTLR3_DEBUG_EVENT_LISTENER_struct::consumeToken, ANTLR3_TOKEN_STREAM_struct::debugger, ANTLR3_TOKEN_STREAM_struct::get, ANTLR3_INT_STREAM_struct::index, ANTLR3_TOKEN_STREAM_struct::initialStreamState, and ANTLR3_INT_STREAM_struct::super. </p>
<p> Referenced by antlr3CommonTokenDebugStreamSourceNew(), and setDebugListener().</p>
<h3>static <code>ANTLR3_UINT32</code> dbgLA (<code>pANTLR3_INT_STREAM</code> is, <code>ANTLR3_INT32</code> i) [static]</h3>
<p>Referenced by antlr3CommonTokenDebugStreamSourceNew(), and setDebugListener().</p>
<h3>static <code>ANTLR3_MARKER</code> dbgMark (<code>pANTLR3_INT_STREAM</code> is) [static]</h3>
<p>Referenced by antlr3CommonTokenDebugStreamSourceNew(), and setDebugListener().</p>
<h3>static void dbgRewindLast (<code>pANTLR3_INT_STREAM</code> is) [static]</h3>
<p>Referenced by antlr3CommonTokenDebugStreamSourceNew(), and setDebugListener().</p>
<h3>static void dbgRewindStream (<code>pANTLR3_INT_STREAM</code> is, <code>ANTLR3_MARKER</code> marker) [static]</h3>
<p>Referenced by antlr3CommonTokenDebugStreamSourceNew(), and setDebugListener().</p>
<h3>static void dbgSeek (<code>pANTLR3_INT_STREAM</code> is, <code>ANTLR3_MARKER</code> index) [static]</h3>
<p>Referenced by antlr3CommonTokenDebugStreamSourceNew(), and setDebugListener().</p>
<h3>static <code>pANTLR3_COMMON_TOKEN</code> dbgTokLT (<code>pANTLR3_TOKEN_STREAM</code> ts, <code>ANTLR3_INT32</code> k) [static]</h3>
<p>As per the normal tokLT but sends information to the debugger. </p>
<p> References ANTLR3_TRUE, consumeInitialHiddenTokens(), ANTLR3_TOKEN_STREAM_struct::initialStreamState, ANTLR3_TOKEN_STREAM_struct::istream, and tokLT(). </p>
<p> Referenced by antlr3CommonTokenDebugStreamSourceNew(), and setDebugListener().</p>
<h3>static void discardOffChannel (<code>pANTLR3_COMMON_TOKEN_STREAM</code> cts, <code>ANTLR3_BOOLEAN</code> discard) [static]</h3>
<p>References ANTLR3_COMMON_TOKEN_STREAM_struct::discardOffChannel. </p>
<p> Referenced by antlr3CommonTokenStreamNew().</p>
<h3>static void discardTokenType (<code>pANTLR3_COMMON_TOKEN_STREAM</code> cts, <code>ANTLR3_INT32</code> ttype) [static]</h3>
<p>References ANTLR3_FUNC_PTR, antlr3ListNew(), ANTLR3_COMMON_TOKEN_STREAM_struct::discardSet, and ANTLR3_LIST_struct::put. </p>
<p> Referenced by antlr3CommonTokenStreamNew().</p>
<h3>static void fillBuffer (<code>pANTLR3_COMMON_TOKEN_STREAM</code> tokenStream) [static]</h3>
<p>Referenced by getTokens(), getTokensSet(), LB(), tokLT(), toString(), and toStringSS().</p>
<h3>static <code>pANTLR3_COMMON_TOKEN</code> get (<code>pANTLR3_TOKEN_STREAM</code> ts, <code>ANTLR3_UINT32</code> i) [static]</h3>
<p>References ANTLR3_VECTOR_struct::get, ANTLR3_TOKEN_STREAM_struct::super, and ANTLR3_COMMON_TOKEN_STREAM_struct::tokens.</p>
<h3>static <code>pANTLR3_STRING</code> getSourceName (<code>pANTLR3_INT_STREAM</code> is) [static]</h3>
<p>Referenced by antlr3CommonTokenStreamNew().</p>
<h3>static <code>pANTLR3_LIST</code> getTokenRange (<code>pANTLR3_COMMON_TOKEN_STREAM</code> cts, <code>ANTLR3_UINT32</code> start, <code>ANTLR3_UINT32</code> stop) [static]</h3>
<p>References ANTLR3_COMMON_TOKEN_STREAM_struct::getTokensSet. </p>
<p> Referenced by antlr3CommonTokenStreamNew().</p>
<h3>static <code>pANTLR3_VECTOR</code> getTokens (<code>pANTLR3_COMMON_TOKEN_STREAM</code> cts) [static]</h3>
<p>References fillBuffer(), ANTLR3_COMMON_TOKEN_STREAM_struct::p, and ANTLR3_COMMON_TOKEN_STREAM_struct::tokens. </p>
<p> Referenced by antlr3CommonTokenStreamNew().</p>
<h3>static <code>pANTLR3_LIST</code> getTokensList (<code>pANTLR3_COMMON_TOKEN_STREAM</code> cts, <code>ANTLR3_UINT32</code> start, <code>ANTLR3_UINT32</code> stop, <code>pANTLR3_LIST</code> list) [static]</h3>
<p>References antlr3BitsetList(), ANTLR3_BITSET_struct::free, ANTLR3_COMMON_TOKEN_STREAM_struct::getTokensSet, and ANTLR3_LIST_struct::table. </p>
<p> Referenced by antlr3CommonTokenStreamNew().</p>
<h3>static <code>pANTLR3_TOKEN_SOURCE</code> getTokenSource (<code>pANTLR3_TOKEN_STREAM</code> ts) [static]</h3>
<p>References ANTLR3_TOKEN_STREAM_struct::tokenSource. </p>
<p> Referenced by antlr3CommonTokenStreamNew().</p>
<h3>static <code>pANTLR3_LIST</code> getTokensSet (<code>pANTLR3_COMMON_TOKEN_STREAM</code> tokenStream, <code>ANTLR3_UINT32</code> start, <code>ANTLR3_UINT32</code> stop, <code>pANTLR3_BITSET</code> types) [static]</h3>
<p>Given a start and stop index, return a List of all tokens in the token type BitSet. Return null if no tokens were found. This method looks at both on and off channel tokens. </p>
<p> References ANTLR3_TRUE, antlr3ListNew(), fillBuffer(), ANTLR3_LIST_struct::free, ANTLR3_TOKEN_STREAM_struct::get, ANTLR3_COMMON_TOKEN_struct::getType, ANTLR3_BITSET_struct::isMember, ANTLR3_TOKEN_STREAM_struct::istream, ANTLR3_COMMON_TOKEN_STREAM_struct::p, ANTLR3_LIST_struct::put, ANTLR3_LIST_struct::size, ANTLR3_INT_STREAM_struct::size, and ANTLR3_COMMON_TOKEN_STREAM_struct::tstream. </p>
<p> Referenced by antlr3CommonTokenStreamNew().</p>
<h3>static <code>pANTLR3_LIST</code> getTokensType (<code>pANTLR3_COMMON_TOKEN_STREAM</code> cts, <code>ANTLR3_UINT32</code> start, <code>ANTLR3_UINT32</code> stop, <code>ANTLR3_UINT32</code> type) [static]</h3>
<p>References antlr3BitsetOf(), ANTLR3_BITSET_struct::free, and ANTLR3_COMMON_TOKEN_STREAM_struct::getTokensSet. </p>
<p> Referenced by antlr3CommonTokenStreamNew().</p>
<h3>static <code>pANTLR3_COMMON_TOKEN</code> LB (<code>pANTLR3_COMMON_TOKEN_STREAM</code> tokenStream, <code>ANTLR3_INT32</code> i) [static]</h3>
<p>References ANTLR3_VECTOR_ELEMENT_struct::element, ANTLR3_VECTOR_struct::elements, fillBuffer(), ANTLR3_COMMON_TOKEN_STREAM_struct::p, skipOffTokenChannelsReverse(), and ANTLR3_COMMON_TOKEN_STREAM_struct::tokens. </p>
<p> Referenced by tokLT().</p>
<h3>static <code>ANTLR3_MARKER</code> mark (<code>pANTLR3_INT_STREAM</code> is) [static]</h3>
<p>Referenced by antlr3CommonTokenStreamNew().</p>
<h3>static void release (<code>pANTLR3_INT_STREAM</code> is, <code>ANTLR3_MARKER</code> mark) [static]</h3>
<p>Referenced by antlr3CommonTokenStreamNew().</p>
<h3>static void rewindLast (<code>pANTLR3_INT_STREAM</code> is) [static]</h3>
<p>Referenced by antlr3CommonTokenStreamNew().</p>
<h3>static void rewindStream (<code>pANTLR3_INT_STREAM</code> is, <code>ANTLR3_MARKER</code> marker) [static]</h3>
<p>Referenced by antlr3CommonTokenStreamNew().</p>
<h3>static void seek (<code>pANTLR3_INT_STREAM</code> is, <code>ANTLR3_MARKER</code> index) [static]</h3>
<p>Referenced by antlr3CommonTokenStreamNew().</p>
<h3>static void setDebugListener (<code>pANTLR3_TOKEN_STREAM</code> ts, <code>pANTLR3_DEBUG_EVENT_LISTENER</code> debugger) [static]</h3>
<p>References ANTLR3_INT_STREAM_struct::_LA, ANTLR3_TOKEN_STREAM_struct::_LT, ANTLR3_FALSE, ANTLR3_INT_STREAM_struct::consume, dbgConsume(), dbgLA(), dbgMark(), dbgRewindLast(), dbgRewindStream(), dbgSeek(), dbgTokLT(), ANTLR3_TOKEN_STREAM_struct::debugger, ANTLR3_TOKEN_STREAM_struct::initialStreamState, ANTLR3_TOKEN_STREAM_struct::istream, ANTLR3_INT_STREAM_struct::mark, ANTLR3_INT_STREAM_struct::rewind, ANTLR3_INT_STREAM_struct::rewindLast, and ANTLR3_INT_STREAM_struct::seek. </p>
<p> Referenced by antlr3CommonTokenStreamNew().</p>
<h3>static void setTokenSource (<code>pANTLR3_TOKEN_STREAM</code> ts, <code>pANTLR3_TOKEN_SOURCE</code> tokenSource) [static]</h3>
<p>References ANTLR3_TOKEN_STREAM_struct::tokenSource. </p>
<p> Referenced by antlr3CommonTokenStreamNew().</p>
<h3>static void setTokenTypeChannel (<code>pANTLR3_COMMON_TOKEN_STREAM</code> tokenStream, <code>ANTLR3_UINT32</code> ttype, <code>ANTLR3_UINT32</code> channel) [static]</h3>
<p>A simple filter mechanism whereby you can tell this token stream to force all tokens of type ttype to be on channel. For example, when interpreting, we cannot execute actions so we need to tell the stream to force all WS and NEWLINE to be a different, ignored, channel. </p>
<p> References ANTLR3_FUNC_PTR, antlr3ListNew(), ANTLR3_COMMON_TOKEN_STREAM_struct::channelOverrides, and ANTLR3_LIST_struct::put. </p>
<p> Referenced by antlr3CommonTokenStreamNew().</p>
<h3>static <code>ANTLR3_UINT32</code> size (<code>pANTLR3_INT_STREAM</code> is) [static]</h3>
<p>Referenced by antlr3CommonTokenStreamNew().</p>
<h3>static <code>ANTLR3_UINT32</code> skipOffTokenChannels (<code>pANTLR3_COMMON_TOKEN_STREAM</code> tokenStream, <code>ANTLR3_INT32</code> i) [static]</h3>
<p>Referenced by consume(), and tokLT().</p>
<h3>static <code>ANTLR3_UINT32</code> skipOffTokenChannelsReverse (<code>pANTLR3_COMMON_TOKEN_STREAM</code> tokenStream, <code>ANTLR3_INT32</code> i) [static]</h3>
<p>Referenced by LB().</p>
<h3>static <code>ANTLR3_MARKER</code> tindex (<code>pANTLR3_INT_STREAM</code> is) [static]</h3>
<p>Referenced by antlr3CommonTokenStreamNew().</p>
<h3>static <code>pANTLR3_COMMON_TOKEN</code> tokLT (<code>pANTLR3_TOKEN_STREAM</code> ts, <code>ANTLR3_INT32</code> k) [static]</h3>
<p>Get the ith token from the current position 1..n where k=1 is the first symbol of lookahead. </p>
<p> References ANTLR3_INT_STREAM_struct::cachedSize, ANTLR3_VECTOR_ELEMENT_struct::element, ANTLR3_VECTOR_struct::elements, ANTLR3_TOKEN_SOURCE_struct::eofToken, fillBuffer(), ANTLR3_INT_STREAM_struct::index, ANTLR3_TOKEN_STREAM_struct::istream, LB(), ANTLR3_COMMON_TOKEN_STREAM_struct::p, ANTLR3_COMMON_TOKEN_struct::setStartIndex, ANTLR3_COMMON_TOKEN_struct::setStopIndex, skipOffTokenChannels(), ANTLR3_TOKEN_STREAM_struct::super, ANTLR3_COMMON_TOKEN_STREAM_struct::tokens, and ANTLR3_TOKEN_STREAM_struct::tokenSource. </p>
<p> Referenced by antlr3CommonTokenStreamNew(), and dbgTokLT().</p>
<h3>static <code>pANTLR3_STRING</code> toString (<code>pANTLR3_TOKEN_STREAM</code> ts) [static]</h3>
<p>References fillBuffer(), ANTLR3_TOKEN_STREAM_struct::istream, ANTLR3_COMMON_TOKEN_STREAM_struct::p, ANTLR3_INT_STREAM_struct::size, ANTLR3_TOKEN_STREAM_struct::super, and ANTLR3_TOKEN_STREAM_struct::toStringSS. </p>
<p> Referenced by antlr3CommonTokenStreamNew().</p>
<h3>static <code>pANTLR3_STRING</code> toStringSS (<code>pANTLR3_TOKEN_STREAM</code> ts, <code>ANTLR3_UINT32</code> start, <code>ANTLR3_UINT32</code> stop) [static]</h3>
<p>References fillBuffer(), ANTLR3_TOKEN_STREAM_struct::get, ANTLR3_COMMON_TOKEN_struct::getText, ANTLR3_TOKEN_STREAM_struct::getTokenSource, ANTLR3_TOKEN_STREAM_struct::istream, ANTLR3_STRING_FACTORY_struct::newRaw, ANTLR3_COMMON_TOKEN_STREAM_struct::p, ANTLR3_INT_STREAM_struct::size, ANTLR3_TOKEN_SOURCE_struct::strFactory, ANTLR3_TOKEN_STREAM_struct::super, and ANTLR3_COMMON_TOKEN_STREAM_struct::tokens. </p>
<p> Referenced by antlr3CommonTokenStreamNew().</p>
<h3>static <code>pANTLR3_STRING</code> toStringTT (<code>pANTLR3_TOKEN_STREAM</code> ts, <code>pANTLR3_COMMON_TOKEN</code> start, <code>pANTLR3_COMMON_TOKEN</code> stop) [static]</h3>
<p>References ANTLR3_COMMON_TOKEN_struct::getTokenIndex, and ANTLR3_TOKEN_STREAM_struct::toStringSS. </p>
<p> Referenced by antlr3CommonTokenStreamNew().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
