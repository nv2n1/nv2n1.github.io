---
title: "antlr3-enteralt(3)"
name: "antlr3-enteralt"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-enteralt/"
description: "src/antlr3debughandlers.c –"
---

<p>src/antlr3debughandlers.c &#8211; </p>
<p> Provides the debugging functions invoked by a recognizer built using the debug generator mode of the antlr tool.</p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/antlr3.h">antlr3.h</a>&gt; </p>
<h3>Functions</h3>
<p>static void <code>ack</code> (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy) </p>
<p> static void <code>addChild</code> (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>pANTLR3_BASE_TREE</code> root, <code>pANTLR3_BASE_TREE</code> child) </p>
<p> ANTLR3_API <code>pANTLR3_DEBUG_EVENT_LISTENER</code> <code>antlr3DebugListenerNew</code> ()<br />
 <i>Create and initialize a new debug event listener that can be connected to by ANTLRWorks and any other debugger via a socket. </i><br />
 <code>pANTLR3_DEBUG_EVENT_LISTENER</code> <code>antlr3DebugListenerNewPort</code> (<code>ANTLR3_UINT32</code> port) </p>
<p> static void <code>becomeRoot</code> (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>pANTLR3_BASE_TREE</code> newRoot, <code>pANTLR3_BASE_TREE</code> oldRoot) </p>
<p> static void <code>beginBacktrack</code> (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, int level) </p>
<p> static void <code>beginResync</code> (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy) </p>
<p> static void <code>commence</code> (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy) </p>
<p> static void <code>consumeHiddenToken</code> (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>pANTLR3_COMMON_TOKEN</code> t) </p>
<p> static void <code>consumeNode</code> (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>pANTLR3_BASE_TREE</code> t) </p>
<p> static void <code>consumeToken</code> (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>pANTLR3_COMMON_TOKEN</code> t) </p>
<p> static void <code>createNode</code> (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>pANTLR3_BASE_TREE</code> t) </p>
<p> static void <code>createNodeTok</code> (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>pANTLR3_BASE_TREE</code> node, <code>pANTLR3_COMMON_TOKEN</code> token) </p>
<p> static void <code>endBacktrack</code> (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, int level, <code>ANTLR3_BOOLEAN</code> successful) </p>
<p> static void <code>endResync</code> (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy) </p>
<p> static void <code>enterAlt</code> (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, int alt) </p>
<p> static void <code>enterDecision</code> (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, int decisionNumber) </p>
<p> static void <code>enterRule</code> (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, const char *grammarFileName, const char *ruleName) </p>
<p> static void <code>enterSubRule</code> (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, int decisionNumber) </p>
<p> static void <code>errorNode</code> (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>pANTLR3_BASE_TREE</code> t) </p>
<p> static void <code>exitDecision</code> (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, int decisionNumber) </p>
<p> static void <code>exitRule</code> (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, const char *grammarFileName, const char *ruleName) </p>
<p> static void <code>exitSubRule</code> (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, int decisionNumber) </p>
<p> static <code>ANTLR3_BOOLEAN</code> <code>handshake</code> (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy) </p>
<p> static void <code>location</code> (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, int line, int pos) </p>
<p> static void <code>LT</code> (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, int i, <code>pANTLR3_COMMON_TOKEN</code> t) </p>
<p> static void <code>LTT</code> (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, int i, <code>pANTLR3_BASE_TREE</code> t) </p>
<p> static void <code>mark</code> (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>ANTLR3_MARKER</code> marker) </p>
<p> static void <code>nilNode</code> (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>pANTLR3_BASE_TREE</code> t) </p>
<p> static void <code>recognitionException</code> (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>pANTLR3_EXCEPTION</code> e) </p>
<p> static void <code>rewindLast</code> (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy) </p>
<p> static void <code>rewindMark</code> (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>ANTLR3_MARKER</code> marker) </p>
<p> static void <code>semanticPredicate</code> (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>ANTLR3_BOOLEAN</code> result, const char *predicate) </p>
<p> <code>pANTLR3_STRING</code> <code>serializeNode</code> (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>pANTLR3_BASE_TREE</code> node) </p>
<p> void <code>serializeText</code> (<code>pANTLR3_STRING</code> buffer, <code>pANTLR3_STRING</code> text) </p>
<p> <code>pANTLR3_STRING</code> <code>serializeToken</code> (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>pANTLR3_COMMON_TOKEN</code> t) </p>
<p> static void <code>setTokenBoundaries</code> (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>pANTLR3_BASE_TREE</code> t, <code>ANTLR3_MARKER</code> tokenStartIndex, <code>ANTLR3_MARKER</code> tokenStopIndex) </p>
<p> static int <code>sockSend</code> (<code>SOCKET</code> sock, const char *ptr, int len) </p>
<p> static void <code>terminate</code> (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy) </p>
<p> static void <code>transmit</code> (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, const char *ptr) </p>
<h2>Detailed Description</h2>
<p>Provides the debugging functions invoked by a recognizer built using the debug generator mode of the antlr tool. </p>
<p> See <code>antlr3debugeventlistener.h</code> for documentation.</p>
<h2>Function Documentation</h2>
<h3>static void ack (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy) [static]</h3>
<p>References ANTLR3_PRINTF, and ANTLR3_DEBUG_EVENT_LISTENER_struct::socket. </p>
<p> Referenced by handshake(), and transmit().</p>
<h3>static void addChild (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>pANTLR3_BASE_TREE</code> root, <code>pANTLR3_BASE_TREE</code> child) [static]</h3>
<p>Referenced by antlr3DebugListenerNew().</p>
<h3>ANTLR3_API <code>pANTLR3_DEBUG_EVENT_LISTENER</code> antlr3DebugListenerNew ()</h3>
<p>Create and initialize a new debug event listener that can be connected to by ANTLRWorks and any other debugger via a socket. </p>
<p> References addChild(), ANTLR3_DEBUG_EVENT_LISTENER_struct::addChild, ANTLR3_CALLOC, becomeRoot(), ANTLR3_DEBUG_EVENT_LISTENER_struct::becomeRoot, beginBacktrack(), ANTLR3_DEBUG_EVENT_LISTENER_struct::beginBacktrack, beginResync(), ANTLR3_DEBUG_EVENT_LISTENER_struct::beginResync, commence(), ANTLR3_DEBUG_EVENT_LISTENER_struct::commence, consumeHiddenToken(), ANTLR3_DEBUG_EVENT_LISTENER_struct::consumeHiddenToken, consumeNode(), ANTLR3_DEBUG_EVENT_LISTENER_struct::consumeNode, consumeToken(), ANTLR3_DEBUG_EVENT_LISTENER_struct::consumeToken, createNode(), ANTLR3_DEBUG_EVENT_LISTENER_struct::createNode, createNodeTok(), ANTLR3_DEBUG_EVENT_LISTENER_struct::createNodeTok, DEFAULT_DEBUGGER_PORT, endBacktrack(), ANTLR3_DEBUG_EVENT_LISTENER_struct::endBacktrack, endResync(), ANTLR3_DEBUG_EVENT_LISTENER_struct::endResync, enterAlt(), ANTLR3_DEBUG_EVENT_LISTENER_struct::enterAlt, enterDecision(), ANTLR3_DEBUG_EVENT_LISTENER_struct::enterDecision, enterRule(), ANTLR3_DEBUG_EVENT_LISTENER_struct::enterRule, enterSubRule(), ANTLR3_DEBUG_EVENT_LISTENER_struct::enterSubRule, errorNode(), ANTLR3_DEBUG_EVENT_LISTENER_struct::errorNode, exitDecision(), ANTLR3_DEBUG_EVENT_LISTENER_struct::exitDecision, exitRule(), ANTLR3_DEBUG_EVENT_LISTENER_struct::exitRule, exitSubRule(), ANTLR3_DEBUG_EVENT_LISTENER_struct::exitSubRule, handshake(), ANTLR3_DEBUG_EVENT_LISTENER_struct::handshake, location(), ANTLR3_DEBUG_EVENT_LISTENER_struct::location, LT(), ANTLR3_DEBUG_EVENT_LISTENER_struct::LT, LTT(), ANTLR3_DEBUG_EVENT_LISTENER_struct::LTT, mark(), ANTLR3_DEBUG_EVENT_LISTENER_struct::mark, nilNode(), ANTLR3_DEBUG_EVENT_LISTENER_struct::nilNode, ANTLR3_DEBUG_EVENT_LISTENER_struct::port, ANTLR3_DEBUG_EVENT_LISTENER_struct::PROTOCOL_VERSION, recognitionException(), ANTLR3_DEBUG_EVENT_LISTENER_struct::recognitionException, ANTLR3_DEBUG_EVENT_LISTENER_struct::rewind, rewindLast(), ANTLR3_DEBUG_EVENT_LISTENER_struct::rewindLast, rewindMark(), semanticPredicate(), ANTLR3_DEBUG_EVENT_LISTENER_struct::semanticPredicate, setTokenBoundaries(), ANTLR3_DEBUG_EVENT_LISTENER_struct::setTokenBoundaries, terminate(), and ANTLR3_DEBUG_EVENT_LISTENER_struct::terminate. </p>
<p> Referenced by antlr3DebugListenerNewPort().</p>
<h3><code>pANTLR3_DEBUG_EVENT_LISTENER</code> antlr3DebugListenerNewPort (<code>ANTLR3_UINT32</code> port)</h3>
<p>References antlr3DebugListenerNew(), and ANTLR3_DEBUG_EVENT_LISTENER_struct::port.</p>
<h3>static void becomeRoot (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>pANTLR3_BASE_TREE</code> newRoot, <code>pANTLR3_BASE_TREE</code> oldRoot) [static]</h3>
<p>Referenced by antlr3DebugListenerNew().</p>
<h3>static void beginBacktrack (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, int level) [static]</h3>
<p>Referenced by antlr3DebugListenerNew().</p>
<h3>static void beginResync (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy) [static]</h3>
<p>Referenced by antlr3DebugListenerNew().</p>
<h3>static void commence (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy) [static]</h3>
<p>Referenced by antlr3DebugListenerNew().</p>
<h3>static void consumeHiddenToken (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>pANTLR3_COMMON_TOKEN</code> t) [static]</h3>
<p>References ANTLR3_STRING_struct::addc, ANTLR3_STRING_struct::chars, ANTLR3_STRING_struct::insert8, serializeToken(), and transmit(). </p>
<p> Referenced by antlr3DebugListenerNew().</p>
<h3>static void consumeNode (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>pANTLR3_BASE_TREE</code> t) [static]</h3>
<p>Referenced by antlr3DebugListenerNew().</p>
<h3>static void consumeToken (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>pANTLR3_COMMON_TOKEN</code> t) [static]</h3>
<p>References ANTLR3_STRING_struct::addc, ANTLR3_STRING_struct::chars, ANTLR3_STRING_struct::insert8, serializeToken(), and transmit(). </p>
<p> Referenced by antlr3DebugListenerNew().</p>
<h3>static void createNode (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>pANTLR3_BASE_TREE</code> t) [static]</h3>
<p>Referenced by antlr3DebugListenerNew().</p>
<h3>static void createNodeTok (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>pANTLR3_BASE_TREE</code> node, <code>pANTLR3_COMMON_TOKEN</code> token) [static]</h3>
<p>Referenced by antlr3DebugListenerNew().</p>
<h3>static void endBacktrack (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, int level, <code>ANTLR3_BOOLEAN</code> successful) [static]</h3>
<p>Referenced by antlr3DebugListenerNew().</p>
<h3>static void endResync (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy) [static]</h3>
<p>Referenced by antlr3DebugListenerNew().</p>
<h3>static void enterAlt (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, int alt) [static]</h3>
<p>References transmit(). </p>
<p> Referenced by antlr3DebugListenerNew().</p>
<h3>static void enterDecision (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, int decisionNumber) [static]</h3>
<p>References transmit(). </p>
<p> Referenced by antlr3DebugListenerNew().</p>
<h3>static void enterRule (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, const char * grammarFileName, const char * ruleName) [static]</h3>
<p>References transmit(). </p>
<p> Referenced by antlr3DebugListenerNew().</p>
<h3>static void enterSubRule (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, int decisionNumber) [static]</h3>
<p>References transmit(). </p>
<p> Referenced by antlr3DebugListenerNew().</p>
<h3>static void errorNode (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>pANTLR3_BASE_TREE</code> t) [static]</h3>
<p>Referenced by antlr3DebugListenerNew().</p>
<h3>static void exitDecision (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, int decisionNumber) [static]</h3>
<p>References transmit(). </p>
<p> Referenced by antlr3DebugListenerNew().</p>
<h3>static void exitRule (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, const char * grammarFileName, const char * ruleName) [static]</h3>
<p>References transmit(). </p>
<p> Referenced by antlr3DebugListenerNew().</p>
<h3>static void exitSubRule (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, int decisionNumber) [static]</h3>
<p>References transmit(). </p>
<p> Referenced by antlr3DebugListenerNew().</p>
<h3>static <code>ANTLR3_BOOLEAN</code> handshake (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy) [static]</h3>
<p>Connection structure with which to wait and accept a connection from a debugger. </p>
<p> References ack(), ANTLR3_CLOSESOCKET, ANTLR3_FALSE, ANTLR3_TRUE, ANTLR3_STRING_struct::chars, ANTLR3_DEBUG_EVENT_LISTENER_struct::grammarFileName, ANTLR3_DEBUG_EVENT_LISTENER_struct::initialized, INVALID_SOCKET, ANTLR3_DEBUG_EVENT_LISTENER_struct::port, ANTLR3_DEBUG_EVENT_LISTENER_struct::PROTOCOL_VERSION, ANTLR3_DEBUG_EVENT_LISTENER_struct::socket, and sockSend(). </p>
<p> Referenced by antlr3DebugListenerNew().</p>
<h3>static void location (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, int line, int pos) [static]</h3>
<p>Referenced by antlr3DebugListenerNew().</p>
<h3>static void LT (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, int i, <code>pANTLR3_COMMON_TOKEN</code> t) [static]</h3>
<p>Referenced by antlr3DebugListenerNew().</p>
<h3>static void LTT (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, int i, <code>pANTLR3_BASE_TREE</code> t) [static]</h3>
<p>Referenced by antlr3DebugListenerNew().</p>
<h3>static void mark (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>ANTLR3_MARKER</code> marker) [static]</h3>
<p>Referenced by antlr3DebugListenerNew().</p>
<h3>static void nilNode (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>pANTLR3_BASE_TREE</code> t) [static]</h3>
<p>Referenced by antlr3DebugListenerNew().</p>
<h3>static void recognitionException (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>pANTLR3_EXCEPTION</code> e) [static]</h3>
<p>Referenced by antlr3DebugListenerNew().</p>
<h3>static void rewindLast (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy) [static]</h3>
<p>Referenced by antlr3DebugListenerNew().</p>
<h3>static void rewindMark (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>ANTLR3_MARKER</code> marker) [static]</h3>
<p>Referenced by antlr3DebugListenerNew().</p>
<h3>static void semanticPredicate (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>ANTLR3_BOOLEAN</code> result, const char * predicate) [static]</h3>
<p>Referenced by antlr3DebugListenerNew().</p>
<h3><code>pANTLR3_STRING</code> serializeNode (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>pANTLR3_BASE_TREE</code> node)</h3>
<p>References ANTLR3_DEBUG_EVENT_LISTENER_struct::adaptor, ANTLR3_STRING_struct::addc, ANTLR3_STRING_struct::addi, ANTLR3_STRING_struct::factory, ANTLR3_COMMON_TOKEN_struct::getCharPositionInLine, ANTLR3_COMMON_TOKEN_struct::getLine, ANTLR3_BASE_TREE_ADAPTOR_struct::getText, ANTLR3_BASE_TREE_ADAPTOR_struct::getToken, ANTLR3_BASE_TREE_ADAPTOR_struct::getTokenStartIndex, ANTLR3_BASE_TREE_ADAPTOR_struct::getType, ANTLR3_BASE_TREE_ADAPTOR_struct::getUniqueID, ANTLR3_DEBUG_EVENT_LISTENER_struct::grammarFileName, ANTLR3_STRING_FACTORY_struct::newSize, serializeText(), ANTLR3_STRING_struct::set, ANTLR3_DEBUG_EVENT_LISTENER_struct::tokenString, and ANTLR3_STRING_struct::toUTF8.</p>
<h3>void serializeText (<code>pANTLR3_STRING</code> buffer, <code>pANTLR3_STRING</code> text)</h3>
<p>References ANTLR3_STRING_struct::addc, ANTLR3_STRING_struct::append, ANTLR3_STRING_struct::charAt, and ANTLR3_STRING_struct::len. </p>
<p> Referenced by serializeNode(), and serializeToken().</p>
<h3><code>pANTLR3_STRING</code> serializeToken (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>pANTLR3_COMMON_TOKEN</code> t)</h3>
<p>References ANTLR3_STRING_struct::addc, ANTLR3_STRING_struct::addi, ANTLR3_STRING_struct::factory, ANTLR3_COMMON_TOKEN_struct::getChannel, ANTLR3_COMMON_TOKEN_struct::getCharPositionInLine, ANTLR3_COMMON_TOKEN_struct::getLine, ANTLR3_COMMON_TOKEN_struct::getText, ANTLR3_COMMON_TOKEN_struct::getTokenIndex, ANTLR3_COMMON_TOKEN_struct::getType, ANTLR3_DEBUG_EVENT_LISTENER_struct::grammarFileName, ANTLR3_STRING_FACTORY_struct::newSize, serializeText(), ANTLR3_STRING_struct::set, ANTLR3_DEBUG_EVENT_LISTENER_struct::tokenString, and ANTLR3_STRING_struct::toUTF8. </p>
<p> Referenced by consumeHiddenToken(), and consumeToken().</p>
<h3>static void setTokenBoundaries (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>pANTLR3_BASE_TREE</code> t, <code>ANTLR3_MARKER</code> tokenStartIndex, <code>ANTLR3_MARKER</code> tokenStopIndex) [static]</h3>
<p>Referenced by antlr3DebugListenerNew().</p>
<h3>static int sockSend (<code>SOCKET</code> sock, const char * ptr, int len) [static]</h3>
<p>References ANTLR3_FALSE, and ANTLR3_TRUE. </p>
<p> Referenced by handshake(), and transmit().</p>
<h3>static void terminate (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy) [static]</h3>
<p>Referenced by antlr3DebugListenerNew().</p>
<h3>static void transmit (<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, const char * ptr) [static]</h3>
<p>References ack(), ANTLR3_DEBUG_EVENT_LISTENER_struct::socket, and sockSend(). </p>
<p> Referenced by consumeHiddenToken(), consumeToken(), enterAlt(), enterDecision(), enterRule(), enterSubRule(), exitDecision(), exitRule(), and exitSubRule().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
