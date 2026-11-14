---
title: "antlr3-channeloverrides(3)"
name: "antlr3-channeloverrides"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-channeloverrides/"
description: "ANTLR3_COMMON_TOKEN_STREAM_struct –"
---

<p>ANTLR3_COMMON_TOKEN_STREAM_struct &#8211; </p>
<p> Common token stream is an implementation of ANTLR_TOKEN_STREAM for the default parsers and recognizers.</p>
<h2>Synopsis</h2>
<p> #include &lt;<a href="file:/usr/include/antlr3tokenstream.h">antlr3tokenstream.h</a>&gt;</p>
<h3>Data Fields</h3>
<p> <code>ANTLR3_UINT32</code> <code>channel</code> </p>
<p> <code>pANTLR3_LIST</code> <code>channelOverrides</code><br />
 <i>Override map of tokens. </i><br />
 <code>ANTLR3_BOOLEAN</code> <code>discardOffChannel</code><br />
 <i>If this flag is set to ANTLR3_TRUE, then tokens that the stream sees that are not in the channel that this stream is tuned to, are not tracked in the tokens table. </i><br />
 void(* <code>discardOffChannelToks</code> )(struct <code>ANTLR3_COMMON_TOKEN_STREAM_struct</code> *tokenStream, <code>ANTLR3_BOOLEAN</code> discard)<br />
 <i>Signal to discard off channel tokens from here on in. </i><br />
 <code>pANTLR3_LIST</code> <code>discardSet</code><br />
 <i>Discared set. </i><br />
 void(* <code>discardTokenType</code> )(struct <code>ANTLR3_COMMON_TOKEN_STREAM_struct</code> *tokenStream, <code>ANTLR3_INT32</code> ttype)<br />
 <i>Add a particular token type to the discard set. </i><br />
 void(* <code>free</code> )(struct <code>ANTLR3_COMMON_TOKEN_STREAM_struct</code> *tokenStream)<br />
 <i>Function that knows how to free an ANTLR3_COMMON_TOKEN_STREAM. </i><br />
 <code>pANTLR3_LIST</code>(* <code>getTokenRange</code> )(struct <code>ANTLR3_COMMON_TOKEN_STREAM_struct</code> *tokenStream, <code>ANTLR3_UINT32</code> start, <code>ANTLR3_UINT32</code> stop)<br />
 <i>Function that returns all the tokens between a start and a stop index. </i><br />
 <code>pANTLR3_VECTOR</code>(* <code>getTokens</code> )(struct <code>ANTLR3_COMMON_TOKEN_STREAM_struct</code> *tokenStream)<br />
 <i>Function that returns a pointer to the ANTLR3_LIST of all tokens in the stream (this causes the buffer to fill if we have not get any yet). </i><br />
 <code>pANTLR3_LIST</code>(* <code>getTokensList</code> )(struct <code>ANTLR3_COMMON_TOKEN_STREAM_struct</code> *tokenStream, <code>ANTLR3_UINT32</code> start, <code>ANTLR3_UINT32</code> stop, <code>pANTLR3_LIST</code> list)<br />
 <i>Function that returns all the tokens indicated by being a member of the supplied List. </i><br />
 <code>pANTLR3_LIST</code>(* <code>getTokensSet</code> )(struct <code>ANTLR3_COMMON_TOKEN_STREAM_struct</code> *tokenStream, <code>ANTLR3_UINT32</code> start, <code>ANTLR3_UINT32</code> stop, <code>pANTLR3_BITSET</code> types)<br />
 <i>Function that returns all the tokens indicated by the specified bitset, within a range of tokens. </i><br />
 <code>pANTLR3_LIST</code>(* <code>getTokensType</code> )(struct <code>ANTLR3_COMMON_TOKEN_STREAM_struct</code> *tokenStream, <code>ANTLR3_UINT32</code> start, <code>ANTLR3_UINT32</code> stop, <code>ANTLR3_UINT32</code> type)<br />
 <i>Function that returns all tokens of a certain type within a range. </i><br />
 <code>ANTLR3_INT32</code> <code>p</code><br />
 <i>The index into the tokens list of the current token (the next one that will be consumed. </i><br />
 void(* <code>setTokenTypeChannel</code> )(struct <code>ANTLR3_COMMON_TOKEN_STREAM_struct</code> *tokenStream, <code>ANTLR3_UINT32</code> ttype, <code>ANTLR3_UINT32</code> <code>channel</code>)<br />
 <i>A simple filter mechanism whereby you can tell this token stream to force all tokens of type ttype to be on channel. </i><br />
 void * <code>super</code><br />
 <i>Whatever is supplying the COMMON_TOKEN_STREAM needs a pointer to itself so that this can be accessed by any of the API functions which it implements. </i><br />
 <code>pANTLR3_VECTOR</code> <code>tokens</code><br />
 <i>Records every single token pulled from the source indexed by the token index. </i><br />
 <code>pANTLR3_TOKEN_STREAM</code> <code>tstream</code><br />
 <i>The ANTLR3_TOKEN_STREAM interface implementation, which also includes the intstream implementation. </i></p>
<h2>Detailed Description</h2>
<p> Common token stream is an implementation of ANTLR_TOKEN_STREAM for the default parsers and recognizers. </p>
<p> You may of course build your own implementation if you are so inclined.</p>
<h2>Field Documentation</h2>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_COMMON_TOKEN_STREAM_struct::channel</code></h3>
<p> Referenced by antlr3CommonTokenStreamSourceNew().</p>
<h3><code>pANTLR3_LIST</code> <code>ANTLR3_COMMON_TOKEN_STREAM_struct::channelOverrides</code></h3>
<p> Override map of tokens. If a token type has an entry in here, then the pointer in the table points to an int, being the override channel number that should always be used for this token type. </p>
<p> Referenced by antlr3CommonTokenStreamSourceNew(), antlr3CTSFree(), and setTokenTypeChannel().</p>
<h3><code>ANTLR3_BOOLEAN</code> <code>ANTLR3_COMMON_TOKEN_STREAM_struct::discardOffChannel</code></h3>
<p> If this flag is set to ANTLR3_TRUE, then tokens that the stream sees that are not in the channel that this stream is tuned to, are not tracked in the tokens table. When set to false, ALL tokens are added to the tracking. </p>
<p> Referenced by antlr3CommonTokenStreamSourceNew(), and discardOffChannel().</p>
<h3>void(* <code>ANTLR3_COMMON_TOKEN_STREAM_struct::discardOffChannelToks</code>)(struct <code>ANTLR3_COMMON_TOKEN_STREAM_struct</code> *tokenStream, <code>ANTLR3_BOOLEAN</code> discard)</h3>
<p> Signal to discard off channel tokens from here on in. </p>
<p> Referenced by antlr3CommonTokenStreamNew().</p>
<h3><code>pANTLR3_LIST</code> <code>ANTLR3_COMMON_TOKEN_STREAM_struct::discardSet</code></h3>
<p> Discared set. If a token has an entry in this table, then it is thrown away (data pointer is always NULL). </p>
<p> Referenced by antlr3CommonTokenStreamSourceNew(), antlr3CTSFree(), and discardTokenType().</p>
<h3>void(* <code>ANTLR3_COMMON_TOKEN_STREAM_struct::discardTokenType</code>)(struct <code>ANTLR3_COMMON_TOKEN_STREAM_struct</code> *tokenStream, <code>ANTLR3_INT32</code> ttype)</h3>
<p> Add a particular token type to the discard set. If a token is found to belong to this set, then it is skipped/thrown away </p>
<p> Referenced by antlr3CommonTokenStreamNew().</p>
<h3>void(* <code>ANTLR3_COMMON_TOKEN_STREAM_struct::free</code>)(struct <code>ANTLR3_COMMON_TOKEN_STREAM_struct</code> *tokenStream)</h3>
<p> Function that knows how to free an ANTLR3_COMMON_TOKEN_STREAM. </p>
<p> Referenced by antlr3CommonTokenStreamSourceNew().</p>
<h3><code>pANTLR3_LIST</code>(* <code>ANTLR3_COMMON_TOKEN_STREAM_struct::getTokenRange</code>)(struct <code>ANTLR3_COMMON_TOKEN_STREAM_struct</code> *tokenStream, <code>ANTLR3_UINT32</code> start, <code>ANTLR3_UINT32</code> stop)</h3>
<p> Function that returns all the tokens between a start and a stop index. TODO: This is a new list (Ack! Maybe this is a reason to have factories for LISTS and HASHTABLES etc :-( come back to this) </p>
<p> Referenced by antlr3CommonTokenStreamNew().</p>
<h3><code>pANTLR3_VECTOR</code>(* <code>ANTLR3_COMMON_TOKEN_STREAM_struct::getTokens</code>)(struct <code>ANTLR3_COMMON_TOKEN_STREAM_struct</code> *tokenStream)</h3>
<p> Function that returns a pointer to the ANTLR3_LIST of all tokens in the stream (this causes the buffer to fill if we have not get any yet). </p>
<p> Referenced by antlr3CommonTokenStreamNew().</p>
<h3><code>pANTLR3_LIST</code>(* <code>ANTLR3_COMMON_TOKEN_STREAM_struct::getTokensList</code>)(struct <code>ANTLR3_COMMON_TOKEN_STREAM_struct</code> *tokenStream, <code>ANTLR3_UINT32</code> start, <code>ANTLR3_UINT32</code> stop, <code>pANTLR3_LIST</code> list)</h3>
<p> Function that returns all the tokens indicated by being a member of the supplied List. </p>
<p> Referenced by antlr3CommonTokenStreamNew().</p>
<h3><code>pANTLR3_LIST</code>(* <code>ANTLR3_COMMON_TOKEN_STREAM_struct::getTokensSet</code>)(struct <code>ANTLR3_COMMON_TOKEN_STREAM_struct</code> *tokenStream, <code>ANTLR3_UINT32</code> start, <code>ANTLR3_UINT32</code> stop, <code>pANTLR3_BITSET</code> types)</h3>
<p> Function that returns all the tokens indicated by the specified bitset, within a range of tokens. </p>
<p> Referenced by antlr3CommonTokenStreamNew(), getTokenRange(), getTokensList(), and getTokensType().</p>
<h3><code>pANTLR3_LIST</code>(* <code>ANTLR3_COMMON_TOKEN_STREAM_struct::getTokensType</code>)(struct <code>ANTLR3_COMMON_TOKEN_STREAM_struct</code> *tokenStream, <code>ANTLR3_UINT32</code> start, <code>ANTLR3_UINT32</code> stop, <code>ANTLR3_UINT32</code> type)</h3>
<p> Function that returns all tokens of a certain type within a range. </p>
<p> Referenced by antlr3CommonTokenStreamNew().</p>
<h3><code>ANTLR3_INT32</code> <code>ANTLR3_COMMON_TOKEN_STREAM_struct::p</code></h3>
<p> The index into the tokens list of the current token (the next one that will be consumed. p = -1 indicates that the token list is empty. </p>
<p> Referenced by antlr3CommonTokenStreamNew(), consume(), getTokens(), getTokensSet(), LB(), tokLT(), toString(), and toStringSS().</p>
<h3>void(* <code>ANTLR3_COMMON_TOKEN_STREAM_struct::setTokenTypeChannel</code>)(struct <code>ANTLR3_COMMON_TOKEN_STREAM_struct</code> *tokenStream, <code>ANTLR3_UINT32</code> ttype, <code>ANTLR3_UINT32</code> <code>channel</code>)</h3>
<p> A simple filter mechanism whereby you can tell this token stream to force all tokens of type ttype to be on channel. For example, when interpreting, we cannot exec actions so we need to tell the stream to force all WS and NEWLINE to be a different, ignored channel. </p>
<p> Referenced by antlr3CommonTokenStreamNew().</p>
<h3>void* <code>ANTLR3_COMMON_TOKEN_STREAM_struct::super</code></h3>
<p> Whatever is supplying the COMMON_TOKEN_STREAM needs a pointer to itself so that this can be accessed by any of the API functions which it implements.</p>
<h3><code>pANTLR3_VECTOR</code> <code>ANTLR3_COMMON_TOKEN_STREAM_struct::tokens</code></h3>
<p> Records every single token pulled from the source indexed by the token index. There might be more efficient ways to do this, such as referencing directly in to the token factory pools, but for now this is convenient and the ANTLR3_LIST is not a huge overhead as it only stores pointers anyway, but allows for iterations and so on. </p>
<p> Referenced by antlr3CommonTokenStreamNew(), antlr3CTSFree(), consume(), get(), getTokens(), LB(), tokLT(), and toStringSS().</p>
<h3><code>pANTLR3_TOKEN_STREAM</code> <code>ANTLR3_COMMON_TOKEN_STREAM_struct::tstream</code></h3>
<p> The ANTLR3_TOKEN_STREAM interface implementation, which also includes the intstream implementation. We could duplicate the pANTLR_INT_STREAM in this interface and initialize it to a copy, but this could be confusing it just results in one more level of indirection and I think that with judicial use of &#8216;const&#8217; later, the optimizer will do decent job. </p>
<p> Referenced by antlr3CommonTokenDebugStreamSourceNew(), antlr3CommonTokenStreamNew(), antlr3CommonTokenStreamSourceNew(), antlr3CTSFree(), antlr3RecognitionExceptionNew(), and getTokensSet(). </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for ANTLR3C from the source code.</p>
