---
title: "antlr3-tokenstring(3)"
name: "antlr3-tokenstring"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-tokenstring/"
description: "ANTLR3_DEBUG_EVENT_LISTENER_struct –"
---

<p>ANTLR3_DEBUG_EVENT_LISTENER_struct &#8211; </p>
<p> The ANTLR3 debugging interface for communicating with ANLTR Works.</p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/antlr3debugeventlistener.h">antlr3debugeventlistener.h</a>&gt;</p>
<h3>Data Fields</h3>
<p>void(* <code>ack</code> )(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy)<br />
 <i>Retrieve acknowledge response from the debugger. </i><br />
 <code>pANTLR3_BASE_TREE_ADAPTOR</code> <code>adaptor</code><br />
 <i>Allows the debug event system to access the adapter in use by the recognizer, if this is a tree parser of some sort. </i><br />
 void(* <code>addChild</code> )(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>pANTLR3_BASE_TREE</code> root, <code>pANTLR3_BASE_TREE</code> child)<br />
 <i>Make childID a child of rootID. </i><br />
 void(* <code>becomeRoot</code> )(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>pANTLR3_BASE_TREE</code> newRoot, <code>pANTLR3_BASE_TREE</code> oldRoot)<br />
 <i>Make a node the new root of an existing root. </i><br />
 void(* <code>beginBacktrack</code> )(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, int level) </p>
<p> void(* <code>beginResync</code> )(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy)<br />
 <i>Indicates the recognizer is about to consume tokens to resynchronize the parser. </i><br />
 void(* <code>commence</code> )(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy)<br />
 <i>Announce that parsing has begun. </i><br />
 void(* <code>consumeHiddenToken</code> )(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>pANTLR3_COMMON_TOKEN</code> t)<br />
 <i>An off-channel input token was consumed. </i><br />
 void(* <code>consumeNode</code> )(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>pANTLR3_BASE_TREE</code> t)<br />
 <i>Input for a tree parser is an AST, but we know nothing for sure about a node except its type and text (obtained from the adaptor). </i><br />
 void(* <code>consumeToken</code> )(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>pANTLR3_COMMON_TOKEN</code> t)<br />
 <i>An input token was consumed; matched by any kind of element. </i><br />
 void(* <code>createNode</code> )(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>pANTLR3_BASE_TREE</code> t)<br />
 <i>Announce a new node built from token elements such as type etc. </i><br />
 void(* <code>createNodeTok</code> )(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>pANTLR3_BASE_TREE</code> node, <code>pANTLR3_COMMON_TOKEN</code> token)<br />
 <i>Announce a new node built from an existing token. </i><br />
 void(* <code>endBacktrack</code> )(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, int level, <code>ANTLR3_BOOLEAN</code> successful) </p>
<p> void(* <code>endResync</code> )(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy)<br />
 <i>Indicates that the recognizer has finished consuming tokens in order to resynchronize. </i><br />
 void(* <code>enterAlt</code> )(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, int alt)<br />
 <i>Because rules can have lots of alternatives, it is very useful to know which alt you are entering. </i><br />
 void(* <code>enterDecision</code> )(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, int decisionNumber)<br />
 <i>Every decision, fixed k or arbitrary, has an enter/exit event so that a GUI can easily track what LT/consume events are associated with prediction. </i><br />
 void(* <code>enterRule</code> )(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, const char *<code>grammarFileName</code>, const char *ruleName)<br />
 <i>The parser has just entered a rule. </i><br />
 void(* <code>enterSubRule</code> )(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, int decisionNumber)<br />
 <i>Track entry into any (. </i><br />
 void(* <code>errorNode</code> )(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>pANTLR3_BASE_TREE</code> t)<br />
 <i>If a syntax error occurs, recognizers bracket the error with an error node if they are building ASTs. </i><br />
 void(* <code>exitDecision</code> )(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, int decisionNumber) </p>
<p> void(* <code>exitRule</code> )(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, const char *<code>grammarFileName</code>, const char *ruleName)<br />
 <i>This is the last thing executed before leaving a rule. </i><br />
 void(* <code>exitSubRule</code> )(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, int decisionNumber) </p>
<p> void(* <code>free</code> )(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy)<br />
 <i>Free up the resources allocated to this structure. </i><br />
 <code>pANTLR3_STRING</code> <code>grammarFileName</code><br />
 <i>The name of the grammar file that we are debugging. </i><br />
 <code>ANTLR3_BOOLEAN</code>(* <code>handshake</code> )(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy)<br />
 <i>Wait for a connection from the debugger and initiate the debugging session. </i><br />
 <code>ANTLR3_BOOLEAN</code> <code>initialized</code><br />
 <i>Indicates whether we have already connected or not. </i><br />
 void(* <code>location</code> )(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, int line, int pos)<br />
 <i>To watch a parser move through the grammar, the parser needs to inform the debugger what line/charPos it is passing in the grammar. </i><br />
 void(* <code>LT</code> )(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, int i, <code>pANTLR3_COMMON_TOKEN</code> t)<br />
 <i>Somebody (anybody) looked ahead. </i><br />
 void(* <code>LTT</code> )(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, int i, <code>pANTLR3_BASE_TREE</code> t)<br />
 <i>The tree parser looked ahead. </i><br />
 void(* <code>mark</code> )(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>ANTLR3_MARKER</code> marker)<br />
 <i>The parser is going to look arbitrarily ahead; mark this location, the token stream&#8217;s marker is sent in case you need it. </i><br />
 void(* <code>nilNode</code> )(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>pANTLR3_BASE_TREE</code> t)<br />
 <i>A nil was created (even nil nodes have a unique ID. </i><br />
 <code>ANTLR3_UINT32</code> <code>port</code><br />
 <i>The port number which the debug listener should listen on for a connection. </i><br />
 int <code>PROTOCOL_VERSION</code><br />
 <i>The version of the debugging protocol supported by the providing instance of the debug event listener. </i><br />
 void(* <code>recognitionException</code> )(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>pANTLR3_EXCEPTION</code> e)<br />
 <i>A recognition exception occurred such as NoViableAltException. </i><br />
 void(* <code>rewind</code> )(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>ANTLR3_MARKER</code> marker)<br />
 <i>After an arbitrarily long lookahead as with a cyclic DFA (or with any backtrack), this informs the debugger that stream should be rewound to the position associated with marker. </i><br />
 void(* <code>rewindLast</code> )(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy)<br />
 <i>Rewind to the input position of the last marker. </i><br />
 void(* <code>semanticPredicate</code> )(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>ANTLR3_BOOLEAN</code> result, const char *predicate)<br />
 <i>A semantic predicate was evaluate with this result and action text. </i><br />
 void(* <code>setTokenBoundaries</code> )(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>pANTLR3_BASE_TREE</code> t, <code>ANTLR3_MARKER</code> tokenStartIndex, <code>ANTLR3_MARKER</code> tokenStopIndex)<br />
 <i>Set the token start/stop token index for a subtree root or node. </i><br />
 <code>SOCKET</code> <code>socket</code><br />
 <i>The socket structure we receive after a successful accept on the serverSocket. </i><br />
 void(* <code>terminate</code> )(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy)<br />
 <i>Parsing is over; successfully or not. </i><br />
 <code>pANTLR3_STRING</code> <code>tokenString</code><br />
 <i>Used to serialize the values of any particular token we need to send back to the debugger. </i></p>
<h2>Detailed Description</h2>
<p>The ANTLR3 debugging interface for communicating with ANLTR Works. </p>
<p> Function comments mostly taken from the Java version.</p>
<h2>Field Documentation</h2>
<h3>void(* <code>ANTLR3_DEBUG_EVENT_LISTENER_struct::ack</code>)(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy)</h3>
<p>Retrieve acknowledge response from the debugger. in fact this response is never used at the moment. So we just read whatever is in the socket buffer and throw it away.</p>
<h3><code>pANTLR3_BASE_TREE_ADAPTOR</code> <code>ANTLR3_DEBUG_EVENT_LISTENER_struct::adaptor</code></h3>
<p>Allows the debug event system to access the adapter in use by the recognizer, if this is a tree parser of some sort. </p>
<p> Referenced by antlr3BaseTreeAdaptorInit(), and serializeNode().</p>
<h3>void(* <code>ANTLR3_DEBUG_EVENT_LISTENER_struct::addChild</code>)(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>pANTLR3_BASE_TREE</code> root, <code>pANTLR3_BASE_TREE</code> child)</h3>
<p>Make childID a child of rootID. If you are receiving this event over a socket via RemoteDebugEventSocketListener then only IDs are set. </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>org.antlr.runtime.tree.TreeAdaptor.addChild()</code></dl>
<p> Referenced by antlr3DebugListenerNew(), dbgAddChild(), dbgAddChildToken(), and simulateTreeConstruction().</p>
<h3>void(* <code>ANTLR3_DEBUG_EVENT_LISTENER_struct::becomeRoot</code>)(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>pANTLR3_BASE_TREE</code> newRoot, <code>pANTLR3_BASE_TREE</code> oldRoot)</h3>
<p>Make a node the new root of an existing root. See </p>
<p> Note: the newRootID parameter is possibly different than the <code>TreeAdaptor.becomeRoot()</code> newRoot parameter. In our case, it will always be the result of calling <code>TreeAdaptor.becomeRoot()</code> and not root_n or whatever. </p>
<p> The listener should assume that this event occurs only when the current subrule (or rule) subtree is being reset to newRootID. </p>
<p> If you are receiving this event over a socket via RemoteDebugEventSocketListener then only IDs are set. </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>org.antlr.runtime.tree.TreeAdaptor.becomeRoot()</code></dl>
<p> Referenced by antlr3DebugListenerNew(), dbgBecomeRoot(), and dbgBecomeRootToken().</p>
<h3>void(* <code>ANTLR3_DEBUG_EVENT_LISTENER_struct::beginBacktrack</code>)(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, int level)</h3>
<p>Referenced by antlr3DebugListenerNew(), and beginBacktrack().</p>
<h3>void(* <code>ANTLR3_DEBUG_EVENT_LISTENER_struct::beginResync</code>)(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy)</h3>
<p>Indicates the recognizer is about to consume tokens to resynchronize the parser. Any consume events from here until the recovered event are not part of the parse&#8211;they are dead tokens. </p>
<p> Referenced by antlr3DebugListenerNew(), beginResync(), and recoverFromMismatchedToken().</p>
<h3>void(* <code>ANTLR3_DEBUG_EVENT_LISTENER_struct::commence</code>)(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy)</h3>
<p>Announce that parsing has begun. Not technically useful except for sending events over a socket. A GUI for example will launch a thread to connect and communicate with a remote parser. The thread will want to notify the GUI when a connection is made. ANTLR parsers trigger this upon entry to the first rule (the ruleLevel is used to figure this out). </p>
<p> Referenced by antlr3DebugListenerNew().</p>
<h3>void(* <code>ANTLR3_DEBUG_EVENT_LISTENER_struct::consumeHiddenToken</code>)(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>pANTLR3_COMMON_TOKEN</code> t)</h3>
<p>An off-channel input token was consumed. Trigger after the token was matched by things like <code>match()</code>, <code>matchAny()</code>. (unless of course the hidden token is first stuff in the input stream). </p>
<p> Referenced by antlr3DebugListenerNew(), consumeInitialHiddenTokens(), and dbgConsume().</p>
<h3>void(* <code>ANTLR3_DEBUG_EVENT_LISTENER_struct::consumeNode</code>)(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>pANTLR3_BASE_TREE</code> t)</h3>
<p>Input for a tree parser is an AST, but we know nothing for sure about a node except its type and text (obtained from the adaptor). This is the analog of the consumeToken method. The ID is usually the memory address of the node. If the type is UP or DOWN, then the ID is not really meaningful as it&#8217;s fixed&#8211;there is just one UP node and one DOWN navigation node. </p>
<p> Note that unlike the Java version, the node type of the C parsers is always fixed as pANTLR3_BASE_TREE because all such structures contain a super pointer to their parent, which is generally COMMON_TREE and within that there is a super pointer that can point to a user type that encapsulates it. Almost akin to saying that it is an interface pointer except we don&#8217;t need to know what the interface is in full, just those bits that are the base. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>t</i></dl>
<p> Referenced by antlr3DebugListenerNew().</p>
<h3>void(* <code>ANTLR3_DEBUG_EVENT_LISTENER_struct::consumeToken</code>)(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>pANTLR3_COMMON_TOKEN</code> t)</h3>
<p>An input token was consumed; matched by any kind of element. Trigger after the token was matched by things like <code>match()</code>, <code>matchAny()</code>. </p>
<p> Referenced by antlr3DebugListenerNew(), and dbgConsume().</p>
<h3>void(* <code>ANTLR3_DEBUG_EVENT_LISTENER_struct::createNode</code>)(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>pANTLR3_BASE_TREE</code> t)</h3>
<p>Announce a new node built from token elements such as type etc. .. </p>
<p> If you are receiving this event over a socket via RemoteDebugEventSocketListener then only t.ID, type, text are set. </p>
<p> Referenced by antlr3DebugListenerNew(), dbgCreate(), dbgCreateTypeText(), dbgCreateTypeToken(), dbgCreateTypeTokenText(), dbgNil(), and simulateTreeConstruction().</p>
<h3>void(* <code>ANTLR3_DEBUG_EVENT_LISTENER_struct::createNodeTok</code>)(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>pANTLR3_BASE_TREE</code> node, <code>pANTLR3_COMMON_TOKEN</code> token)</h3>
<p>Announce a new node built from an existing token. If you are receiving this event over a socket via RemoteDebugEventSocketListener then only node.ID and token.tokenIndex are set. </p>
<p> Referenced by antlr3DebugListenerNew().</p>
<h3>void(* <code>ANTLR3_DEBUG_EVENT_LISTENER_struct::endBacktrack</code>)(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, int level, <code>ANTLR3_BOOLEAN</code> successful)</h3>
<p>Referenced by antlr3DebugListenerNew(), and endBacktrack().</p>
<h3>void(* <code>ANTLR3_DEBUG_EVENT_LISTENER_struct::endResync</code>)(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy)</h3>
<p>Indicates that the recognizer has finished consuming tokens in order to resynchronize. There may be multiple beginResync/endResync pairs before the recognizer comes out of errorRecovery mode (in which multiple errors are suppressed). This will be useful in a gui where you want to probably grey out tokens that are consumed but not matched to anything in grammar. Anything between a beginResync/endResync pair was tossed out by the parser. </p>
<p> Referenced by antlr3DebugListenerNew(), endResync(), and recoverFromMismatchedToken().</p>
<h3>void(* <code>ANTLR3_DEBUG_EVENT_LISTENER_struct::enterAlt</code>)(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, int alt)</h3>
<p>Because rules can have lots of alternatives, it is very useful to know which alt you are entering. This is 1..n for n alts. </p>
<p> Referenced by antlr3DebugListenerNew().</p>
<h3>void(* <code>ANTLR3_DEBUG_EVENT_LISTENER_struct::enterDecision</code>)(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, int decisionNumber)</h3>
<p>Every decision, fixed k or arbitrary, has an enter/exit event so that a GUI can easily track what LT/consume events are associated with prediction. You will see a single enter/exit subrule but multiple enter/exit decision events, one for each loop iteration. </p>
<p> Referenced by antlr3DebugListenerNew().</p>
<h3>void(* <code>ANTLR3_DEBUG_EVENT_LISTENER_struct::enterRule</code>)(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, const char *<code>grammarFileName</code>, const char *ruleName)</h3>
<p>The parser has just entered a rule. No decision has been made about which alt is predicted. This is fired AFTER init actions have been executed. Attributes are defined and available etc&#8230; </p>
<p> Referenced by antlr3DebugListenerNew().</p>
<h3>void(* <code>ANTLR3_DEBUG_EVENT_LISTENER_struct::enterSubRule</code>)(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, int decisionNumber)</h3>
<p>Track entry into any (. ..) subrule other EBNF construct </p>
<p> Referenced by antlr3DebugListenerNew().</p>
<h3>void(* <code>ANTLR3_DEBUG_EVENT_LISTENER_struct::errorNode</code>)(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>pANTLR3_BASE_TREE</code> t)</h3>
<p>If a syntax error occurs, recognizers bracket the error with an error node if they are building ASTs. This event notifies the listener that this is the case </p>
<p> Referenced by antlr3DebugListenerNew().</p>
<h3>void(* <code>ANTLR3_DEBUG_EVENT_LISTENER_struct::exitDecision</code>)(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, int decisionNumber)</h3>
<p>Referenced by antlr3DebugListenerNew().</p>
<h3>void(* <code>ANTLR3_DEBUG_EVENT_LISTENER_struct::exitRule</code>)(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, const char *<code>grammarFileName</code>, const char *ruleName)</h3>
<p>This is the last thing executed before leaving a rule. It is executed even if an exception is thrown. This is triggered after error reporting and recovery have occurred (unless the exception is not caught in this rule). This implies an &#8216;exitAlt&#8217; event. </p>
<p> Referenced by antlr3DebugListenerNew().</p>
<h3>void(* <code>ANTLR3_DEBUG_EVENT_LISTENER_struct::exitSubRule</code>)(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, int decisionNumber)</h3>
<p>Referenced by antlr3DebugListenerNew().</p>
<h3>void(* <code>ANTLR3_DEBUG_EVENT_LISTENER_struct::free</code>)(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy)</h3>
<p>Free up the resources allocated to this structure.</p>
<h3><code>pANTLR3_STRING</code> <code>ANTLR3_DEBUG_EVENT_LISTENER_struct::grammarFileName</code></h3>
<p>The name of the grammar file that we are debugging. </p>
<p> Referenced by handshake(), serializeNode(), and serializeToken().</p>
<h3><code>ANTLR3_BOOLEAN</code>(* <code>ANTLR3_DEBUG_EVENT_LISTENER_struct::handshake</code>)(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy)</h3>
<p>Wait for a connection from the debugger and initiate the debugging session. </p>
<p> Referenced by antlr3DebugListenerNew().</p>
<h3><code>ANTLR3_BOOLEAN</code> <code>ANTLR3_DEBUG_EVENT_LISTENER_struct::initialized</code></h3>
<p>Indicates whether we have already connected or not. </p>
<p> Referenced by handshake().</p>
<h3>void(* <code>ANTLR3_DEBUG_EVENT_LISTENER_struct::location</code>)(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, int line, int pos)</h3>
<p>To watch a parser move through the grammar, the parser needs to inform the debugger what line/charPos it is passing in the grammar. For now, this does not know how to switch from one grammar to the other and back for island grammars etc&#8230; </p>
<p> This should also allow breakpoints because the debugger can stop the parser whenever it hits this line/pos. </p>
<p> Referenced by antlr3DebugListenerNew().</p>
<h3>void(* <code>ANTLR3_DEBUG_EVENT_LISTENER_struct::LT</code>)(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, int i, <code>pANTLR3_COMMON_TOKEN</code> t)</h3>
<p>Somebody (anybody) looked ahead. Note that this actually gets triggered by both LA and LT calls. The debugger will want to know which Token object was examined. Like consumeToken, this indicates what token was seen at that depth. A remote debugger cannot look ahead into a file it doesn&#8217;t have so LT events must pass the token even if the info is redundant. </p>
<p> Referenced by antlr3DebugListenerNew().</p>
<h3>void(* <code>ANTLR3_DEBUG_EVENT_LISTENER_struct::LTT</code>)(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, int i, <code>pANTLR3_BASE_TREE</code> t)</h3>
<p>The tree parser looked ahead. If the type is UP or DOWN, then the ID is not really meaningful as it&#8217;s fixed&#8211;there is just one UP node and one DOWN navigation node. </p>
<p> Referenced by antlr3DebugListenerNew().</p>
<h3>void(* <code>ANTLR3_DEBUG_EVENT_LISTENER_struct::mark</code>)(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>ANTLR3_MARKER</code> marker)</h3>
<p>The parser is going to look arbitrarily ahead; mark this location, the token stream&#8217;s marker is sent in case you need it. </p>
<p> Referenced by antlr3DebugListenerNew().</p>
<h3>void(* <code>ANTLR3_DEBUG_EVENT_LISTENER_struct::nilNode</code>)(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>pANTLR3_BASE_TREE</code> t)</h3>
<p>A nil was created (even nil nodes have a unique ID. .. they are not &#8216;null&#8217; per se). As of 4/28/2006, this seems to be uniquely triggered when starting a new subtree such as when entering a subrule in automatic mode and when building a tree in rewrite mode. </p>
<p> If you are receiving this event over a socket via RemoteDebugEventSocketListener then only t.ID is set. </p>
<p> Referenced by antlr3DebugListenerNew().</p>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_DEBUG_EVENT_LISTENER_struct::port</code></h3>
<p>The port number which the debug listener should listen on for a connection. </p>
<p> Referenced by antlr3DebugListenerNew(), antlr3DebugListenerNewPort(), and handshake().</p>
<h3>int <code>ANTLR3_DEBUG_EVENT_LISTENER_struct::PROTOCOL_VERSION</code></h3>
<p>The version of the debugging protocol supported by the providing instance of the debug event listener. </p>
<p> Referenced by antlr3DebugListenerNew(), and handshake().</p>
<h3>void(* <code>ANTLR3_DEBUG_EVENT_LISTENER_struct::recognitionException</code>)(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>pANTLR3_EXCEPTION</code> e)</h3>
<p>A recognition exception occurred such as NoViableAltException. I made this a generic event so that I can alter the exception hierarchy later without having to alter all the debug objects. </p>
<p> Upon error, the stack of enter rule/subrule must be properly unwound. If no viable alt occurs it is within an enter/exit decision, which also must be rewound. Even the rewind for each mark must be unwound. In the Java target this is pretty easy using try/finally, if a bit ugly in the generated code. The rewind is generated in DFA.predict() actually so no code needs to be generated for that. For languages w/o this &#8216;finally&#8217; feature (C++?), the target implementor will have to build an event stack or something. </p>
<p> Across a socket for remote debugging, only the RecognitionException data fields are transmitted. The token object or whatever that caused the problem was the last object referenced by LT. The immediately preceding LT event should hold the unexpected Token or char. </p>
<p> Here is a sample event trace for grammar: </p>
<p> b : C ({;}A|B) // {;} is there to prevent A|B becoming a set | D ; </p>
<p> The sequence for this rule (with no viable alt in the subrule) for input &#8216;c c&#8217; (there are 3 tokens) is: </p>
<p> commence <a href="/docs/linux/man/1-lt/">LT</a>(1) enterRule b location 7 1 enter decision 3 <a href="/docs/linux/man/1-lt/">LT</a>(1) exit decision 3 enterAlt1 location 7 5 <a href="/docs/linux/man/1-lt/">LT</a>(1) consumeToken [c/&lt;4&gt;,1:0] location 7 7 enterSubRule 2 enter decision 2 <a href="/docs/linux/man/1-lt/">LT</a>(1) <a href="/docs/linux/man/1-lt/">LT</a>(1) recognitionException NoViableAltException 2 1 2 exit decision 2 exitSubRule 2 beginResync <a href="/docs/linux/man/1-lt/">LT</a>(1) consumeToken [c/&lt;4&gt;,1:1] <a href="/docs/linux/man/1-lt/">LT</a>(1) endResync LT(-1) exitRule b terminate </p>
<p> Referenced by antlr3DebugListenerNew(), and recoverFromMismatchedToken().</p>
<h3>void(* <code>ANTLR3_DEBUG_EVENT_LISTENER_struct::rewind</code>)(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>ANTLR3_MARKER</code> marker)</h3>
<p>After an arbitrarily long lookahead as with a cyclic DFA (or with any backtrack), this informs the debugger that stream should be rewound to the position associated with marker. </p>
<p> Referenced by antlr3DebugListenerNew().</p>
<h3>void(* <code>ANTLR3_DEBUG_EVENT_LISTENER_struct::rewindLast</code>)(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy)</h3>
<p>Rewind to the input position of the last marker. Used currently only after a cyclic DFA and just before starting a sem/syn predicate to get the input position back to the start of the decision. Do not &#8216;pop&#8217; the marker off the state. mark(i) and rewind(i) should balance still. </p>
<p> Referenced by antlr3DebugListenerNew().</p>
<h3>void(* <code>ANTLR3_DEBUG_EVENT_LISTENER_struct::semanticPredicate</code>)(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>ANTLR3_BOOLEAN</code> result, const char *predicate)</h3>
<p>A semantic predicate was evaluate with this result and action text. </p>
<p> Referenced by antlr3DebugListenerNew().</p>
<h3>void(* <code>ANTLR3_DEBUG_EVENT_LISTENER_struct::setTokenBoundaries</code>)(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy, <code>pANTLR3_BASE_TREE</code> t, <code>ANTLR3_MARKER</code> tokenStartIndex, <code>ANTLR3_MARKER</code> tokenStopIndex)</h3>
<p>Set the token start/stop token index for a subtree root or node. If you are receiving this event over a socket via RemoteDebugEventSocketListener then only t.ID is set. </p>
<p> Referenced by antlr3DebugListenerNew(), and dbgSetTokenBoundaries().</p>
<h3><code>SOCKET</code> <code>ANTLR3_DEBUG_EVENT_LISTENER_struct::socket</code></h3>
<p>The socket structure we receive after a successful accept on the serverSocket. </p>
<p> Referenced by ack(), handshake(), and transmit().</p>
<h3>void(* <code>ANTLR3_DEBUG_EVENT_LISTENER_struct::terminate</code>)(<code>pANTLR3_DEBUG_EVENT_LISTENER</code> delboy)</h3>
<p>Parsing is over; successfully or not. Mostly useful for telling remote debugging listeners that it&#8217;s time to quit. When the rule invocation level goes to zero at the end of a rule, we are done parsing. </p>
<p> Referenced by antlr3DebugListenerNew().</p>
<h3><code>pANTLR3_STRING</code> <code>ANTLR3_DEBUG_EVENT_LISTENER_struct::tokenString</code></h3>
<p>Used to serialize the values of any particular token we need to send back to the debugger. </p>
<p> Referenced by serializeNode(), and serializeToken(). </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
