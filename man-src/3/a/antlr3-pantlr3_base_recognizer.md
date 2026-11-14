---
title: "antlr3-pantlr3_base_recognizer(3)"
name: "antlr3-pantlr3_base_recognizer"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-pantlr3_base_recognizer/"
description: "pANTLR3_BASE_RECOGNIZER Base Recognizer Implementation –"
---

<p>pANTLR3_BASE_RECOGNIZER Base Recognizer Implementation &#8211; </p>
<p> The base recognizer interface is implemented by all higher level recognizers such as <code>pANTLR3_PARSER</code> and provides methods common to all recognizers.</p>
<h3>Functions</h3>
<p>static <code>ANTLR3_BOOLEAN</code> <code>alreadyParsedRule</code> (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>ANTLR3_MARKER</code> ruleIndex)<br />
 <i>Has this rule already parsed input at the current index in the input stream? Return ANTLR3_TRUE if we have and ANTLR3_FALSE if we have not. </i><br />
 ANTLR3_API <code>pANTLR3_BASE_RECOGNIZER</code> <code>antlr3BaseRecognizerNew</code> (<code>ANTLR3_UINT32</code> type, <code>ANTLR3_UINT32</code> sizeHint, <code>pANTLR3_RECOGNIZER_SHARED_STATE</code> state) </p>
<p> ANTLR3_API void <code>antlr3MTExceptionNew</code> (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer)<br />
 <i>Creates a new Mismatched Token Exception and inserts in the recognizer exception stack. </i><br />
 ANTLR3_API void <code>antlr3RecognitionExceptionNew</code> (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer) </p>
<p> static void <code>beginBacktrack</code> (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>ANTLR3_UINT32</code> level) </p>
<p> static void <code>beginResync</code> (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer) </p>
<p> static <code>pANTLR3_BITSET</code> <code>combineFollows</code> (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>ANTLR3_BOOLEAN</code> exact)<br />
 <i>Compute the current followset for the input stream. </i><br />
 static <code>pANTLR3_BITSET</code> <code>computeCSRuleFollow</code> (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer)<br />
 <i>Compute the context-sensitive FOLLOW set for current rule. </i><br />
 static <code>pANTLR3_BITSET</code> <code>computeErrorRecoverySet</code> (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer)<br />
 <i>Compute the error recovery set for the current rule. </i><br />
 static void <code>consumeUntil</code> (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>ANTLR3_UINT32</code> tokenType)<br />
 <i>Eat tokens from the input stream until we get one of JUST the right type. </i><br />
 static void <code>consumeUntilSet</code> (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>pANTLR3_BITSET</code> set)<br />
 <i>Eat tokens from the input stream until we find one that belongs to the supplied set. </i><br />
 static void <code>displayRecognitionError</code> (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>pANTLR3_UINT8</code> *tokenNames)<br />
 <i>Standard/Example error display method. </i><br />
 static void <code>endBacktrack</code> (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>ANTLR3_UINT32</code> level, <code>ANTLR3_BOOLEAN</code> successful) </p>
<p> static void <code>endResync</code> (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer) </p>
<p> static void <code>freeBR</code> (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer) </p>
<p> static void ANTLR3_CDECL <code>freeIntTrie</code> (void *trie) </p>
<p> static void * <code>getCurrentInputSymbol</code> (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>pANTLR3_INT_STREAM</code> istream) </p>
<p> static void * <code>getMissingSymbol</code> (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>pANTLR3_INT_STREAM</code> istream, <code>pANTLR3_EXCEPTION</code> e, <code>ANTLR3_UINT32</code> expectedTokenType, <code>pANTLR3_BITSET_LIST</code> follow) </p>
<p> static <code>ANTLR3_UINT32</code> <code>getNumberOfSyntaxErrors</code> (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer)<br />
 <i>Return how many syntax errors were detected by this recognizer. </i><br />
 static <code>pANTLR3_STACK</code> <code>getRuleInvocationStack</code> (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer)<br />
 <i>Return the rule invocation stack (how we got here in the parse. </i><br />
 static <code>pANTLR3_STACK</code> <code>getRuleInvocationStackNamed</code> (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>pANTLR3_UINT8</code> name) </p>
<p> static <code>ANTLR3_MARKER</code> <code>getRuleMemoization</code> (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>ANTLR3_INTKEY</code> ruleIndex, <code>ANTLR3_MARKER</code> ruleParseStart)<br />
 <i>Pointer to a function to return whether the rule has parsed input starting at the supplied start index before. </i><br />
 static void * <code>match</code> (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>ANTLR3_UINT32</code> ttype, <code>pANTLR3_BITSET_LIST</code> follow)<br />
 <i>Match current input symbol against ttype. </i><br />
 static void <code>matchAny</code> (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer)<br />
 <i>Consumes the next token, whatever it is, and resets the recognizer state so that it is not in error. </i><br />
 static void <code>memoize</code> (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>ANTLR3_MARKER</code> ruleIndex, <code>ANTLR3_MARKER</code> ruleParseStart)<br />
 <i>Record whether or not this rule parsed the input at this position successfully. </i><br />
 static void <code>mismatch</code> (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>ANTLR3_UINT32</code> ttype, <code>pANTLR3_BITSET_LIST</code> follow)<br />
 <i>Factor out what to do upon token mismatch so tree parsers can behave differently. </i><br />
 static <code>ANTLR3_BOOLEAN</code> <code>mismatchIsMissingToken</code> (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>pANTLR3_INT_STREAM</code> is, <code>pANTLR3_BITSET_LIST</code> follow) </p>
<p> static <code>ANTLR3_BOOLEAN</code> <code>mismatchIsUnwantedToken</code> (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>pANTLR3_INT_STREAM</code> is, <code>ANTLR3_UINT32</code> ttype) </p>
<p> static void <code>recover</code> (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer)<br />
 <i>Recover from an error found on the input stream. </i><br />
 static <code>ANTLR3_BOOLEAN</code> <code>recoverFromMismatchedElement</code> (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>pANTLR3_BITSET_LIST</code> followBits)<br />
 <i>This code is factored out from mismatched token and mismatched set recovery. </i><br />
 static void * <code>recoverFromMismatchedSet</code> (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>pANTLR3_BITSET_LIST</code> follow) </p>
<p> static void * <code>recoverFromMismatchedToken</code> (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>ANTLR3_UINT32</code> ttype, <code>pANTLR3_BITSET_LIST</code> follow)<br />
 <i>Attempt to recover from a single missing or extra token. </i><br />
 static void <code>reportError</code> (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer)<br />
 <i>Report a recognition problem. </i><br />
 static void <code>reset</code> (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer) </p>
<p> static <code>ANTLR3_BOOLEAN</code> <code>synpred</code> (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, void *ctx, void(*predicate)(void *ctx))<br />
 <i>A syntactic predicate. </i><br />
 static <code>pANTLR3_HASH_TABLE</code> <code>toStrings</code> (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>pANTLR3_HASH_TABLE</code> tokens)<br />
 <i>Convenience method for template rewrites &#8211; NYI. </i></p>
<h2>Detailed Description</h2>
<p>The base recognizer interface is implemented by all higher level recognizers such as <code>pANTLR3_PARSER</code> and provides methods common to all recognizers.</p>
<h2>Function Documentation</h2>
<h3>static <code>ANTLR3_BOOLEAN</code> alreadyParsedRule (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>ANTLR3_MARKER</code> ruleIndex) [static]</h3>
<p>Has this rule already parsed input at the current index in the input stream? Return ANTLR3_TRUE if we have and ANTLR3_FALSE if we have not. This method has a side-effect: if we have seen this input for this rule and successfully parsed before, then seek ahead to 1 past the stop token matched for this rule last time. </p>
<p> References ANTLR3_FALSE, ANTLR3_FPRINTF, ANTLR3_TRUE, ANTLR3_TYPE_LEXER, ANTLR3_TYPE_PARSER, ANTLR3_TYPE_TREE_PARSER, ANTLR3_TREE_PARSER_struct::ctnstream, ANTLR3_RECOGNIZER_SHARED_STATE_struct::failed, ANTLR3_BASE_RECOGNIZER_struct::getRuleMemoization, ANTLR3_INT_STREAM_struct::index, ANTLR3_LEXER_struct::input, ANTLR3_INPUT_STREAM_struct::istream, ANTLR3_TREE_NODE_STREAM_struct::istream, ANTLR3_TOKEN_STREAM_struct::istream, MEMO_RULE_FAILED, MEMO_RULE_UNKNOWN, ANTLR3_INT_STREAM_struct::seek, ANTLR3_BASE_RECOGNIZER_struct::state, ANTLR3_BASE_RECOGNIZER_struct::super, ANTLR3_COMMON_TREE_NODE_STREAM_struct::tnstream, ANTLR3_PARSER_struct::tstream, and ANTLR3_BASE_RECOGNIZER_struct::type. </p>
<p> Referenced by antlr3BaseRecognizerNew().</p>
<h3>ANTLR3_API <code>pANTLR3_BASE_RECOGNIZER</code> antlr3BaseRecognizerNew (<code>ANTLR3_UINT32</code> type, <code>ANTLR3_UINT32</code> sizeHint, <code>pANTLR3_RECOGNIZER_SHARED_STATE</code> state)</h3>
<p>References alreadyParsedRule(), ANTLR3_BASE_RECOGNIZER_struct::alreadyParsedRule, ANTLR3_CALLOC, ANTLR3_FALSE, ANTLR3_FREE, ANTLR3_MALLOC, antlr3MTExceptionNew(), antlr3VectorNew(), ANTLR3_RECOGNIZER_SHARED_STATE_struct::backtracking, beginBacktrack(), ANTLR3_BASE_RECOGNIZER_struct::beginBacktrack, beginResync(), ANTLR3_BASE_RECOGNIZER_struct::beginResync, combineFollows(), ANTLR3_BASE_RECOGNIZER_struct::combineFollows, computeCSRuleFollow(), ANTLR3_BASE_RECOGNIZER_struct::computeCSRuleFollow, computeErrorRecoverySet(), ANTLR3_BASE_RECOGNIZER_struct::computeErrorRecoverySet, consumeUntil(), ANTLR3_BASE_RECOGNIZER_struct::consumeUntil, consumeUntilSet(), ANTLR3_BASE_RECOGNIZER_struct::consumeUntilSet, ANTLR3_BASE_RECOGNIZER_struct::debugger, displayRecognitionError(), ANTLR3_BASE_RECOGNIZER_struct::displayRecognitionError, endBacktrack(), ANTLR3_BASE_RECOGNIZER_struct::endBacktrack, endResync(), ANTLR3_BASE_RECOGNIZER_struct::endResync, ANTLR3_RECOGNIZER_SHARED_STATE_struct::errorCount, ANTLR3_RECOGNIZER_SHARED_STATE_struct::errorRecovery, ANTLR3_BASE_RECOGNIZER_struct::exConstruct, ANTLR3_RECOGNIZER_SHARED_STATE_struct::failed, ANTLR3_RECOGNIZER_SHARED_STATE_struct::following, ANTLR3_BASE_RECOGNIZER_struct::free, freeBR(), getCurrentInputSymbol(), ANTLR3_BASE_RECOGNIZER_struct::getCurrentInputSymbol, getMissingSymbol(), ANTLR3_BASE_RECOGNIZER_struct::getMissingSymbol, getNumberOfSyntaxErrors(), ANTLR3_BASE_RECOGNIZER_struct::getNumberOfSyntaxErrors, getRuleInvocationStack(), ANTLR3_BASE_RECOGNIZER_struct::getRuleInvocationStack, getRuleInvocationStackNamed(), ANTLR3_BASE_RECOGNIZER_struct::getRuleInvocationStackNamed, getRuleMemoization(), ANTLR3_BASE_RECOGNIZER_struct::getRuleMemoization, ANTLR3_RECOGNIZER_SHARED_STATE_struct::lastErrorIndex, match(), ANTLR3_BASE_RECOGNIZER_struct::match, matchAny(), ANTLR3_BASE_RECOGNIZER_struct::matchAny, memoize(), ANTLR3_BASE_RECOGNIZER_struct::memoize, mismatch(), ANTLR3_BASE_RECOGNIZER_struct::mismatch, mismatchIsMissingToken(), ANTLR3_BASE_RECOGNIZER_struct::mismatchIsMissingToken, mismatchIsUnwantedToken(), ANTLR3_BASE_RECOGNIZER_struct::mismatchIsUnwantedToken, recover(), ANTLR3_BASE_RECOGNIZER_struct::recover, recoverFromMismatchedElement(), recoverFromMismatchedSet(), ANTLR3_BASE_RECOGNIZER_struct::recoverFromMismatchedSet, recoverFromMismatchedToken(), ANTLR3_BASE_RECOGNIZER_struct::recoverFromMismatchedToken, reportError(), ANTLR3_BASE_RECOGNIZER_struct::reportError, reset(), ANTLR3_BASE_RECOGNIZER_struct::reset, ANTLR3_RECOGNIZER_SHARED_STATE_struct::rStreams, ANTLR3_RECOGNIZER_SHARED_STATE_struct::ruleMemo, ANTLR3_RECOGNIZER_SHARED_STATE_struct::sizeHint, ANTLR3_BASE_RECOGNIZER_struct::state, synpred(), ANTLR3_BASE_RECOGNIZER_struct::synpred, ANTLR3_RECOGNIZER_SHARED_STATE_struct::tokenNames, ANTLR3_RECOGNIZER_SHARED_STATE_struct::tokFactory, ANTLR3_RECOGNIZER_SHARED_STATE_struct::tokSource, toStrings(), ANTLR3_BASE_RECOGNIZER_struct::toStrings, and ANTLR3_BASE_RECOGNIZER_struct::type. </p>
<p> Referenced by antlr3LexerNew(), antlr3ParserNew(), and antlr3TreeParserNewStream().</p>
<h3>ANTLR3_API void antlr3MTExceptionNew (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer)</h3>
<p>Creates a new Mismatched Token Exception and inserts in the recognizer exception stack. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>recognizer</i> Context pointer for this recognizer</dl>
<p> References ANTLR3_MISMATCHED_EX_NAME, ANTLR3_MISMATCHED_TOKEN_EXCEPTION, antlr3RecognitionExceptionNew(), ANTLR3_RECOGNIZER_SHARED_STATE_struct::exception, ANTLR3_EXCEPTION_struct::name, ANTLR3_BASE_RECOGNIZER_struct::state, and ANTLR3_EXCEPTION_struct::type. </p>
<p> Referenced by antlr3BaseRecognizerNew(), antlr3ParserNew(), and mismatch().</p>
<h3>ANTLR3_API void antlr3RecognitionExceptionNew (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer)</h3>
<p>References ANTLR3_INT_STREAM_struct::_LA, ANTLR3_TREE_NODE_STREAM_struct::_LT, ANTLR3_TOKEN_STREAM_struct::_LT, ANTLR3_CHARSTREAM, ANTLR3_COMMONTREENODE, ANTLR3_FALSE, ANTLR3_FPRINTF, ANTLR3_INPUT_MASK, ANTLR3_RECOGNITION_EX_NAME, ANTLR3_RECOGNITION_EXCEPTION, ANTLR3_TOKEN_EOF, ANTLR3_TOKENSTREAM, ANTLR3_TRUE, ANTLR3_TYPE_LEXER, ANTLR3_TYPE_PARSER, ANTLR3_TYPE_TREE_PARSER, antlr3ExceptionNew(), ANTLR3_EXCEPTION_struct::c, ANTLR3_EXCEPTION_struct::charPositionInLine, ANTLR3_TREE_PARSER_struct::ctnstream, ANTLR3_RECOGNIZER_SHARED_STATE_struct::error, ANTLR3_RECOGNIZER_SHARED_STATE_struct::exception, ANTLR3_INPUT_STREAM_struct::fileName, getCharPositionInLine(), ANTLR3_INPUT_STREAM_struct::getCharPositionInLine, getLine(), ANTLR3_INPUT_STREAM_struct::getLine, ANTLR3_INT_STREAM_struct::index, ANTLR3_EXCEPTION_struct::index, ANTLR3_EXCEPTION_struct::input, ANTLR3_COMMON_TOKEN_struct::input, ANTLR3_LEXER_struct::input, ANTLR3_TREE_NODE_STREAM_struct::istream, ANTLR3_TOKEN_STREAM_struct::istream, ANTLR3_INPUT_STREAM_struct::istream, ANTLR3_EXCEPTION_struct::line, ANTLR3_EXCEPTION_struct::message, ANTLR3_EXCEPTION_struct::nextException, ANTLR3_BASE_RECOGNIZER_struct::state, ANTLR3_EXCEPTION_struct::streamName, ANTLR3_TOKEN_STREAM_struct::super, ANTLR3_BASE_RECOGNIZER_struct::super, ANTLR3_COMMON_TREE_NODE_STREAM_struct::tnstream, ANTLR3_COMMON_TREE_struct::token, ANTLR3_EXCEPTION_struct::token, ANTLR3_COMMON_TOKEN_STREAM_struct::tstream, ANTLR3_PARSER_struct::tstream, ANTLR3_INT_STREAM_struct::type, and ANTLR3_BASE_RECOGNIZER_struct::type. </p>
<p> Referenced by antlr3MTExceptionNew(), antlr3MTNExceptionNew(), mismatch(), recoverFromMismatchedToken(), and setCharStream().</p>
<h3>static void beginBacktrack (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>ANTLR3_UINT32</code> level) [static]</h3>
<p>References ANTLR3_DEBUG_EVENT_LISTENER_struct::beginBacktrack, and ANTLR3_BASE_RECOGNIZER_struct::debugger. </p>
<p> Referenced by antlr3BaseRecognizerNew().</p>
<h3>static void beginResync (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer) [static]</h3>
<p>References ANTLR3_DEBUG_EVENT_LISTENER_struct::beginResync, and ANTLR3_BASE_RECOGNIZER_struct::debugger. </p>
<p> Referenced by antlr3BaseRecognizerNew().</p>
<h3>static <code>pANTLR3_BITSET</code> combineFollows (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>ANTLR3_BOOLEAN</code> exact) [static]</h3>
<p>Compute the current followset for the input stream. </p>
<p> References ANTLR3_EOR_TOKEN_TYPE, ANTLR3_FALSE, ANTLR3_TRUE, antlr3BitsetLoad(), antlr3BitsetNew(), ANTLR3_BITSET_struct::borInPlace, ANTLR3_RECOGNIZER_SHARED_STATE_struct::following, ANTLR3_BITSET_struct::free, ANTLR3_STACK_struct::get, ANTLR3_BITSET_struct::isMember, ANTLR3_BITSET_struct::remove, ANTLR3_STACK_struct::size, and ANTLR3_BASE_RECOGNIZER_struct::state. </p>
<p> Referenced by antlr3BaseRecognizerNew().</p>
<h3>static <code>pANTLR3_BITSET</code> computeCSRuleFollow (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer) [static]</h3>
<p>Compute the context-sensitive FOLLOW set for current rule. Documentation below is from the Java runtime. </p>
<p> This is the set of token types that can follow a specific rule reference given a specific call chain. You get the set of viable tokens that can possibly come next (look ahead depth 1) given the current call chain. Contrast this with the definition of plain FOLLOW for rule r: </p>
<p> FOLLOW(r)={x | S=&gt;*alpha r beta in G and x in FIRST(beta)} </p>
<p> where x in T* and alpha, beta in V*; T is set of terminals and V is the set of terminals and non terminals. In other words, FOLLOW(r) is the set of all tokens that can possibly follow references to r in///any* sentential form (context). At runtime, however, we know precisely which context applies as we have the call chain. We may compute the exact (rather than covering superset) set of following tokens. </p>
<p> For example, consider grammar: </p>
<p> stat : ID &#8216;=&#8217; expr &#8216;;&#8217; // FOLLOW(stat)=={EOF} | &#8216;return&#8217; expr &#8216;.&#8217; ; expr : atom (&#8216;+&#8217; atom)* ; // FOLLOW(expr)=={&#8216;;&#8217;,&#8217;.&#8217;,&#8217;)&#8217;} atom : INT // FOLLOW(atom)=={&#8216;+&#8217;,&#8217;)&#8217;,&#8217;;&#8217;,&#8217;.&#8217;} | &#8216;(&#8216; expr &#8216;)&#8217; ; </p>
<p> The FOLLOW sets are all inclusive whereas context-sensitive FOLLOW sets are precisely what could follow a rule reference. For input input &#8216;i=(3);&#8217;, here is the derivation: </p>
<p> stat =&gt; ID &#8216;=&#8217; expr &#8216;;&#8217; =&gt; ID &#8216;=&#8217; atom (&#8216;+&#8217; atom)* &#8216;;&#8217; =&gt; ID &#8216;=&#8217; &#8216;(&#8216; expr &#8216;)&#8217; (&#8216;+&#8217; atom)* &#8216;;&#8217; =&gt; ID &#8216;=&#8217; &#8216;(&#8216; atom &#8216;)&#8217; (&#8216;+&#8217; atom)* &#8216;;&#8217; =&gt; ID &#8216;=&#8217; &#8216;(&#8216; INT &#8216;)&#8217; (&#8216;+&#8217; atom)* &#8216;;&#8217; =&gt; ID &#8216;=&#8217; &#8216;(&#8216; INT &#8216;)&#8217; &#8216;;&#8217; </p>
<p> At the &#8216;3&#8217; token, you&#8217;d have a call chain of </p>
<p> stat -&gt; expr -&gt; atom -&gt; expr -&gt; atom </p>
<p> What can follow that specific nested ref to atom? Exactly &#8216;)&#8217; as you can see by looking at the derivation of this specific input. Contrast this with the FOLLOW(atom)={&#8216;+&#8217;,&#8217;)&#8217;,&#8217;;&#8217;,&#8217;.&#8217;}. </p>
<p> You want the exact viable token set when recovering from a token mismatch. Upon token mismatch, if <a href="/docs/linux/man/1-la/">LA</a>(1) is member of the viable next token set, then you know there is most likely a missing token in the input stream. &#8216;Insert&#8217; one by just not throwing an exception. </p>
<p> References ANTLR3_FALSE, and ANTLR3_BASE_RECOGNIZER_struct::combineFollows. </p>
<p> Referenced by antlr3BaseRecognizerNew().</p>
<h3>static <code>pANTLR3_BITSET</code> computeErrorRecoverySet (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer) [static]</h3>
<p>Compute the error recovery set for the current rule. Documentation below is from the Java implementation. </p>
<p> During rule invocation, the parser pushes the set of tokens that can follow that rule reference on the stack; this amounts to computing FIRST of what follows the rule reference in the enclosing rule. This local follow set only includes tokens from within the rule; i.e., the FIRST computation done by ANTLR stops at the end of a rule. EXAMPLE When you find a &#8216;no viable alt exception&#8217;, the input is not consistent with any of the alternatives for rule r. The best thing to do is to consume tokens until you see something that can legally follow a call to r *or* any rule that called r. You don&#8217;t want the exact set of viable next tokens because the input might just be missing a token&#8211;you might consume the rest of the input looking for one of the missing tokens. </p>
<p> Consider grammar: </p>
<p> a : &#8216;[&#8216; b &#8216;]&#8217; | &#8216;(&#8216; b &#8216;)&#8217; ; b : c &#8216;^&#8217; INT ; c : ID | INT ; </p>
<p> At each rule invocation, the set of tokens that could follow that rule is pushed on a stack. Here are the various &#8216;local&#8217; follow sets: </p>
<p> FOLLOW(b1_in_a) = FIRST(&#8216;]&#8217;) = &#8216;]&#8217; FOLLOW(b2_in_a) = FIRST(&#8216;)&#8217;) = &#8216;)&#8217; FOLLOW(c_in_b) = FIRST(&#8216;^&#8217;) = &#8216;^&#8217; </p>
<p> Upon erroneous input &#8216;[]&#8217;, the call chain is </p>
<p> a -&gt; b -&gt; c </p>
<p> and, hence, the follow context stack is: </p>
<p> depth local follow set after call to rule 0 &lt;EOF&gt; a (from main()) 1 &#8216;]&#8217; b 3 &#8216;^&#8217; c </p>
<p> Notice that &#8216;)&#8217; is not included, because b would have to have been called from a different context in rule a for &#8216;)&#8217; to be included. </p>
<p> For error recovery, we cannot consider FOLLOW(c) (context-sensitive or otherwise). We need the combined set of all context-sensitive FOLLOW sets&#8211;the set of all tokens that could follow any reference in the call chain. We need to resync to one of those tokens. Note that FOLLOW(c)=&#8217;^&#8217; and if we resync&#8217;d to that token, we&#8217;d consume until EOF. We need to sync to context-sensitive FOLLOWs for a, b, and c: {&#8216;]&#8217;,&#8217;^&#8217;}. In this case, for input &#8216;[]&#8217;, <a href="/docs/linux/man/1-la/">LA</a>(1) is in this set so we would not consume anything and after printing an error rule c would return normally. It would not find the required &#8216;^&#8217; though. At this point, it gets a mismatched token error and throws an exception (since <a href="/docs/linux/man/1-la/">LA</a>(1) is not in the viable following token set). The rule exception handler tries to recover, but finds the same recovery set and doesn&#8217;t consume anything. Rule b exits normally returning to rule a. Now it finds the &#8216;]&#8217; (and with the successful match exits errorRecovery mode). </p>
<p> So, you can see that the parser walks up call chain looking for the token that was a member of the recovery set. </p>
<p> Errors are not generated in errorRecovery mode. </p>
<p> ANTLR&#8217;s error recovery mechanism is based upon original ideas: </p>
<p> and </p>
<p> Later, Josef Grosch had some good ideas: </p>
<p>&nbsp;<wbr>Parsers&#8217;:&nbsp;<wbr><a href="ftp://www.cocolab.com/products/cocktail/doca4.ps/ell.ps.zip">ftp://www.cocolab.com/products/cocktail/doca4.ps/ell.ps.zip</a> </p>
<p> Like Grosch I implemented local FOLLOW sets that are combined at run-time upon error to avoid overhead during parsing. </p>
<p> References ANTLR3_FALSE, and ANTLR3_BASE_RECOGNIZER_struct::combineFollows. </p>
<p> Referenced by antlr3BaseRecognizerNew().</p>
<h3>static void consumeUntil (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>ANTLR3_UINT32</code> tokenType) [static]</h3>
<p>Eat tokens from the input stream until we get one of JUST the right type. </p>
<p> References ANTLR3_INT_STREAM_struct::_LA, ANTLR3_FPRINTF, ANTLR3_TOKEN_EOF, ANTLR3_TYPE_PARSER, ANTLR3_TYPE_TREE_PARSER, ANTLR3_INT_STREAM_struct::consume, ANTLR3_TREE_PARSER_struct::ctnstream, ANTLR3_TREE_NODE_STREAM_struct::istream, ANTLR3_TOKEN_STREAM_struct::istream, ANTLR3_BASE_RECOGNIZER_struct::super, ANTLR3_COMMON_TREE_NODE_STREAM_struct::tnstream, ANTLR3_PARSER_struct::tstream, and ANTLR3_BASE_RECOGNIZER_struct::type. </p>
<p> Referenced by antlr3BaseRecognizerNew().</p>
<h3>static void consumeUntilSet (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>pANTLR3_BITSET</code> set) [static]</h3>
<p>Eat tokens from the input stream until we find one that belongs to the supplied set. </p>
<p> References ANTLR3_INT_STREAM_struct::_LA, ANTLR3_FALSE, ANTLR3_FPRINTF, ANTLR3_TOKEN_EOF, ANTLR3_TYPE_PARSER, ANTLR3_TYPE_TREE_PARSER, ANTLR3_INT_STREAM_struct::consume, ANTLR3_TREE_PARSER_struct::ctnstream, ANTLR3_TREE_NODE_STREAM_struct::istream, ANTLR3_TOKEN_STREAM_struct::istream, ANTLR3_BASE_RECOGNIZER_struct::super, ANTLR3_COMMON_TREE_NODE_STREAM_struct::tnstream, ANTLR3_PARSER_struct::tstream, and ANTLR3_BASE_RECOGNIZER_struct::type. </p>
<p> Referenced by antlr3BaseRecognizerNew().</p>
<h3>static void displayRecognitionError (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>pANTLR3_UINT8</code> * tokenNames) [static]</h3>
<p>Standard/Example error display method. No generic error message display funciton coudl possibly do everything correctly for all possible parsers. Hence you are provided with this example routine, which you should override in your parser/tree parser to do as you will. </p>
<p> Here we depart somewhat from the Java runtime as that has now split up a lot of the error display routines into spearate units. However, ther is little advantage to this in the C version as you will probably implement all such routines as a separate translation unit, rather than install them all as pointers to functions in the base recognizer. </p>
<p> References ANTLR3_EARLY_EXIT_EXCEPTION, ANTLR3_FPRINTF, ANTLR3_MISMATCHED_SET_EXCEPTION, ANTLR3_MISMATCHED_TOKEN_EXCEPTION, ANTLR3_MISSING_TOKEN_EXCEPTION, ANTLR3_NO_VIABLE_ALT_EXCEPTION, ANTLR3_RECOGNITION_EXCEPTION, ANTLR3_TOKEN_EOF, ANTLR3_TYPE_PARSER, ANTLR3_TYPE_TREE_PARSER, ANTLR3_UNWANTED_TOKEN_EXCEPTION, antlr3BitsetLoad(), ANTLR3_EXCEPTION_struct::charPositionInLine, ANTLR3_STRING_struct::chars, ANTLR3_TREE_PARSER_struct::ctnstream, ANTLR3_RECOGNIZER_SHARED_STATE_struct::exception, ANTLR3_EXCEPTION_struct::expecting, ANTLR3_EXCEPTION_struct::expectingSet, ANTLR3_BASE_TREE_struct::getCharPositionInLine, ANTLR3_BASE_TREE_struct::getToken, ANTLR3_TREE_NODE_STREAM_struct::istream, ANTLR3_TOKEN_STREAM_struct::istream, ANTLR3_EXCEPTION_struct::line, ANTLR3_EXCEPTION_struct::message, ANTLR3_BITSET_struct::numBits, ANTLR3_BITSET_struct::size, size(), ANTLR3_BASE_RECOGNIZER_struct::state, ANTLR3_EXCEPTION_struct::streamName, ANTLR3_BASE_TREE_struct::super, ANTLR3_BASE_RECOGNIZER_struct::super, ANTLR3_COMMON_TREE_NODE_STREAM_struct::tnstream, ANTLR3_STRING_struct::to8, ANTLR3_EXCEPTION_struct::token, ANTLR3_COMMON_TOKEN_struct::toString, ANTLR3_BASE_TREE_struct::toStringTree, ANTLR3_PARSER_struct::tstream, ANTLR3_COMMON_TOKEN_struct::type, ANTLR3_BASE_RECOGNIZER_struct::type, and ANTLR3_EXCEPTION_struct::type. </p>
<p> Referenced by antlr3BaseRecognizerNew().</p>
<h3>static void endBacktrack (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>ANTLR3_UINT32</code> level, <code>ANTLR3_BOOLEAN</code> successful) [static]</h3>
<p>References ANTLR3_BASE_RECOGNIZER_struct::debugger, and ANTLR3_DEBUG_EVENT_LISTENER_struct::endBacktrack. </p>
<p> Referenced by antlr3BaseRecognizerNew().</p>
<h3>static void endResync (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer) [static]</h3>
<p>References ANTLR3_BASE_RECOGNIZER_struct::debugger, and ANTLR3_DEBUG_EVENT_LISTENER_struct::endResync. </p>
<p> Referenced by antlr3BaseRecognizerNew().</p>
<h3>static void freeBR (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer) [static]</h3>
<p>References ANTLR3_FREE, ANTLR3_TOKEN_FACTORY_struct::close, ANTLR3_RECOGNIZER_SHARED_STATE_struct::exception, ANTLR3_INT_TRIE_struct::free, ANTLR3_EXCEPTION_struct::freeEx, ANTLR3_RECOGNIZER_SHARED_STATE_struct::rStreams, ANTLR3_RECOGNIZER_SHARED_STATE_struct::ruleMemo, ANTLR3_BASE_RECOGNIZER_struct::state, and ANTLR3_RECOGNIZER_SHARED_STATE_struct::tokFactory. </p>
<p> Referenced by antlr3BaseRecognizerNew().</p>
<h3>static void ANTLR3_CDECL freeIntTrie (void * trie) [static]</h3>
<p>Referenced by getRuleMemoization().</p>
<h3>static void * getCurrentInputSymbol (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>pANTLR3_INT_STREAM</code> istream) [static]</h3>
<p>References ANTLR3_INT_STREAM_struct::super. </p>
<p> Referenced by antlr3BaseRecognizerNew().</p>
<h3>static void * getMissingSymbol (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>pANTLR3_INT_STREAM</code> istream, <code>pANTLR3_EXCEPTION</code> e, <code>ANTLR3_UINT32</code> expectedTokenType, <code>pANTLR3_BITSET_LIST</code> follow) [static]</h3>
<p>References ANTLR3_TOKEN_STREAM_struct::_LT, ANTLR3_TOKEN_DEFAULT_CHANNEL, ANTLR3_TOKEN_EOF, antlr3TokenFactoryNew(), ANTLR3_STRING_struct::append8, ANTLR3_COMMON_TOKEN_struct::custom, ANTLR3_COMMON_TOKEN_struct::getCharPositionInLine, ANTLR3_COMMON_TOKEN_struct::getLine, ANTLR3_COMMON_TOKEN_struct::getText, ANTLR3_COMMON_TOKEN_struct::getType, ANTLR3_COMMON_TOKEN_struct::input, ANTLR3_COMMON_TOKEN_struct::lineStart, ANTLR3_TOKEN_FACTORY_struct::newToken, ANTLR3_COMMON_TOKEN_struct::setChannel, ANTLR3_COMMON_TOKEN_struct::setCharPositionInLine, ANTLR3_COMMON_TOKEN_struct::setLine, ANTLR3_COMMON_TOKEN_struct::setText8, ANTLR3_COMMON_TOKEN_struct::setType, ANTLR3_BASE_RECOGNIZER_struct::state, ANTLR3_TOKEN_STREAM_struct::super, ANTLR3_INT_STREAM_struct::super, ANTLR3_RECOGNIZER_SHARED_STATE_struct::tokenNames, ANTLR3_RECOGNIZER_SHARED_STATE_struct::tokFactory, ANTLR3_COMMON_TOKEN_struct::user1, ANTLR3_COMMON_TOKEN_struct::user2, and ANTLR3_COMMON_TOKEN_struct::user3. </p>
<p> Referenced by antlr3BaseRecognizerNew().</p>
<h3>static <code>ANTLR3_UINT32</code> getNumberOfSyntaxErrors (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer) [static]</h3>
<p>Return how many syntax errors were detected by this recognizer. </p>
<p> References ANTLR3_RECOGNIZER_SHARED_STATE_struct::errorCount, and ANTLR3_BASE_RECOGNIZER_struct::state. </p>
<p> Referenced by antlr3BaseRecognizerNew().</p>
<h3>static <code>pANTLR3_STACK</code> getRuleInvocationStack (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer) [static]</h3>
<p>Return the rule invocation stack (how we got here in the parse. In the java version Ter just asks the JVM for all the information but in C we don&#8217;t get this information, so I am going to do nothing right now. </p>
<p> Referenced by antlr3BaseRecognizerNew().</p>
<h3>static <code>pANTLR3_STACK</code> getRuleInvocationStackNamed (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>pANTLR3_UINT8</code> name) [static]</h3>
<p>Referenced by antlr3BaseRecognizerNew().</p>
<h3>static <code>ANTLR3_MARKER</code> getRuleMemoization (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>ANTLR3_INTKEY</code> ruleIndex, <code>ANTLR3_MARKER</code> ruleParseStart) [static]</h3>
<p>Pointer to a function to return whether the rule has parsed input starting at the supplied start index before. If the rule has not parsed input starting from the supplied start index, then it will return ANTLR3_MEMO_RULE_UNKNOWN. If it has parsed from the suppled start point then it will return the point where it last stopped parsing after that start point. </p>
<p> <code>Remarks:</code></p>
<dl COMPACT>
<dd>The rule memos are an ANTLR3_LIST of ANTLR3_LISTS, however if this becomes any kind of performance issue (it probably won&#8217;t, the hash tables are pretty quick) then we could make a special int only version of the table.</dl>
<p> References ANTLR3_INT_TRIE_struct::add, ANTLR3_FUNC_PTR, ANTLR3_HASH_TYPE_STR, antlr3IntTrieNew(), ANTLR3_TRIE_ENTRY_struct::data, freeIntTrie(), ANTLR3_INT_TRIE_struct::get, ANTLR3_TRIE_ENTRY_struct::intVal, MEMO_RULE_UNKNOWN, ANTLR3_TRIE_ENTRY_struct::ptr, ANTLR3_RECOGNIZER_SHARED_STATE_struct::ruleMemo, and ANTLR3_BASE_RECOGNIZER_struct::state. </p>
<p> Referenced by antlr3BaseRecognizerNew().</p>
<h3>static void * match (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>ANTLR3_UINT32</code> ttype, <code>pANTLR3_BITSET_LIST</code> follow) [static]</h3>
<p>Match current input symbol against ttype. Upon error, do one token insertion or deletion if possible. To turn off single token insertion or deletion error recovery, override mismatchRecover() and have it call plain <code>mismatch()</code>, which does not recover. Then any error in a rule will cause an exception and immediate exit from rule. Rule would recover by resynchronizing to the set of symbols that can follow rule ref. </p>
<p> References ANTLR3_INT_STREAM_struct::_LA, ANTLR3_FALSE, ANTLR3_FPRINTF, ANTLR3_TRUE, ANTLR3_TYPE_PARSER, ANTLR3_TYPE_TREE_PARSER, ANTLR3_RECOGNIZER_SHARED_STATE_struct::backtracking, ANTLR3_INT_STREAM_struct::consume, ANTLR3_TREE_PARSER_struct::ctnstream, ANTLR3_RECOGNIZER_SHARED_STATE_struct::errorRecovery, ANTLR3_RECOGNIZER_SHARED_STATE_struct::failed, ANTLR3_BASE_RECOGNIZER_struct::getCurrentInputSymbol, ANTLR3_TREE_NODE_STREAM_struct::istream, ANTLR3_TOKEN_STREAM_struct::istream, ANTLR3_BASE_RECOGNIZER_struct::recoverFromMismatchedToken, ANTLR3_BASE_RECOGNIZER_struct::state, ANTLR3_BASE_RECOGNIZER_struct::super, ANTLR3_COMMON_TREE_NODE_STREAM_struct::tnstream, ANTLR3_PARSER_struct::tstream, and ANTLR3_BASE_RECOGNIZER_struct::type. </p>
<p> Referenced by antlr3BaseRecognizerNew().</p>
<h3>static void matchAny (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer) [static]</h3>
<p>Consumes the next token, whatever it is, and resets the recognizer state so that it is not in error. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>recognizer</i> Recognizer context pointer</dl>
<p> References ANTLR3_FALSE, ANTLR3_FPRINTF, ANTLR3_TYPE_PARSER, ANTLR3_TYPE_TREE_PARSER, ANTLR3_INT_STREAM_struct::consume, ANTLR3_TREE_PARSER_struct::ctnstream, ANTLR3_RECOGNIZER_SHARED_STATE_struct::errorRecovery, ANTLR3_RECOGNIZER_SHARED_STATE_struct::failed, ANTLR3_TREE_NODE_STREAM_struct::istream, ANTLR3_TOKEN_STREAM_struct::istream, ANTLR3_BASE_RECOGNIZER_struct::state, ANTLR3_BASE_RECOGNIZER_struct::super, ANTLR3_COMMON_TREE_NODE_STREAM_struct::tnstream, ANTLR3_PARSER_struct::tstream, and ANTLR3_BASE_RECOGNIZER_struct::type. </p>
<p> Referenced by antlr3BaseRecognizerNew().</p>
<h3>static void memoize (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>ANTLR3_MARKER</code> ruleIndex, <code>ANTLR3_MARKER</code> ruleParseStart) [static]</h3>
<p>Record whether or not this rule parsed the input at this position successfully. </p>
<p> References ANTLR3_INT_TRIE_struct::add, ANTLR3_FPRINTF, ANTLR3_HASH_TYPE_INT, ANTLR3_TRUE, ANTLR3_TYPE_LEXER, ANTLR3_TYPE_PARSER, ANTLR3_TYPE_TREE_PARSER, ANTLR3_TREE_PARSER_struct::ctnstream, ANTLR3_TRIE_ENTRY_struct::data, ANTLR3_RECOGNIZER_SHARED_STATE_struct::failed, ANTLR3_INT_TRIE_struct::get, ANTLR3_INT_STREAM_struct::index, ANTLR3_LEXER_struct::input, ANTLR3_INPUT_STREAM_struct::istream, ANTLR3_TREE_NODE_STREAM_struct::istream, ANTLR3_TOKEN_STREAM_struct::istream, MEMO_RULE_FAILED, ANTLR3_TRIE_ENTRY_struct::ptr, ANTLR3_RECOGNIZER_SHARED_STATE_struct::ruleMemo, ANTLR3_BASE_RECOGNIZER_struct::state, ANTLR3_BASE_RECOGNIZER_struct::super, ANTLR3_COMMON_TREE_NODE_STREAM_struct::tnstream, ANTLR3_PARSER_struct::tstream, and ANTLR3_BASE_RECOGNIZER_struct::type. </p>
<p> Referenced by antlr3BaseRecognizerNew().</p>
<h3>static void mismatch (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>ANTLR3_UINT32</code> ttype, <code>pANTLR3_BITSET_LIST</code> follow) [static]</h3>
<p>Factor out what to do upon token mismatch so tree parsers can behave differently. Override and call mismatchRecover(input, ttype, follow) to get single token insertion and deletion. Use this to turn off single token insertion and deletion. Override mismatchRecover to call this instead. </p>
<p> <code>Remarks:</code></p>
<dl COMPACT>
<dd>mismatch only works for parsers and must be overridden for anything else.</dl>
<p> References ANTLR3_FPRINTF, ANTLR3_MISSING_TOKEN_EXCEPTION, ANTLR3_MISSING_TOKEN_EXCEPTION_NAME, ANTLR3_TYPE_PARSER, ANTLR3_UNWANTED_TOKEN_EXCEPTION, ANTLR3_UNWANTED_TOKEN_EXCEPTION_NAME, antlr3MTExceptionNew(), antlr3RecognitionExceptionNew(), ANTLR3_RECOGNIZER_SHARED_STATE_struct::exception, ANTLR3_EXCEPTION_struct::expecting, ANTLR3_TOKEN_STREAM_struct::istream, mismatchIsMissingToken(), mismatchIsUnwantedToken(), ANTLR3_EXCEPTION_struct::name, ANTLR3_BASE_RECOGNIZER_struct::state, ANTLR3_BASE_RECOGNIZER_struct::super, ANTLR3_PARSER_struct::tstream, ANTLR3_EXCEPTION_struct::type, and ANTLR3_BASE_RECOGNIZER_struct::type. </p>
<p> Referenced by antlr3BaseRecognizerNew().</p>
<h3>static <code>ANTLR3_BOOLEAN</code> mismatchIsMissingToken (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>pANTLR3_INT_STREAM</code> is, <code>pANTLR3_BITSET_LIST</code> follow) [static]</h3>
<p>if current token is consistent with what could come after set then we know we&#8217;re missing a token; error recovery is free to &#8216;insert&#8217; the missing token </p>
<p> BitSet cannot handle negative numbers like -1 (EOF) so I leave EOR in follow set to indicate that the fall of the start symbol is in the set (EOF can follow). </p>
<p> References ANTLR3_INT_STREAM_struct::_LA, ANTLR3_EOR_TOKEN_TYPE, ANTLR3_FALSE, ANTLR3_TRUE, antlr3BitsetLoad(), ANTLR3_BITSET_struct::borInPlace, ANTLR3_BASE_RECOGNIZER_struct::computeCSRuleFollow, ANTLR3_VECTOR_struct::count, ANTLR3_RECOGNIZER_SHARED_STATE_struct::following, ANTLR3_BITSET_struct::free, ANTLR3_BITSET_struct::isMember, ANTLR3_BITSET_struct::remove, ANTLR3_BASE_RECOGNIZER_struct::state, and ANTLR3_STACK_struct::vector. </p>
<p> Referenced by antlr3BaseRecognizerNew(), mismatch(), and recoverFromMismatchedToken().</p>
<h3>static <code>ANTLR3_BOOLEAN</code> mismatchIsUnwantedToken (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>pANTLR3_INT_STREAM</code> is, <code>ANTLR3_UINT32</code> ttype) [static]</h3>
<p>References ANTLR3_INT_STREAM_struct::_LA, ANTLR3_FALSE, ANTLR3_TRUE, ANTLR3_RECOGNIZER_SHARED_STATE_struct::exception, ANTLR3_EXCEPTION_struct::expecting, and ANTLR3_BASE_RECOGNIZER_struct::state. </p>
<p> Referenced by antlr3BaseRecognizerNew(), and mismatch().</p>
<h3>static void recover (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer) [static]</h3>
<p>Recover from an error found on the input stream. Mostly this is NoViableAlt exceptions, but could be a mismatched token that the <code>match()</code> routine could not recover from. </p>
<p> References ANTLR3_FALSE, ANTLR3_FPRINTF, ANTLR3_TYPE_PARSER, ANTLR3_TYPE_TREE_PARSER, ANTLR3_BASE_RECOGNIZER_struct::beginResync, ANTLR3_BASE_RECOGNIZER_struct::computeErrorRecoverySet, ANTLR3_INT_STREAM_struct::consume, ANTLR3_BASE_RECOGNIZER_struct::consumeUntilSet, ANTLR3_TREE_PARSER_struct::ctnstream, ANTLR3_BASE_RECOGNIZER_struct::endResync, ANTLR3_RECOGNIZER_SHARED_STATE_struct::error, ANTLR3_RECOGNIZER_SHARED_STATE_struct::failed, ANTLR3_BITSET_struct::free, ANTLR3_INT_STREAM_struct::index, ANTLR3_TREE_NODE_STREAM_struct::istream, ANTLR3_TOKEN_STREAM_struct::istream, ANTLR3_RECOGNIZER_SHARED_STATE_struct::lastErrorIndex, ANTLR3_BASE_RECOGNIZER_struct::state, ANTLR3_BASE_RECOGNIZER_struct::super, ANTLR3_COMMON_TREE_NODE_STREAM_struct::tnstream, ANTLR3_PARSER_struct::tstream, and ANTLR3_BASE_RECOGNIZER_struct::type. </p>
<p> Referenced by antlr3BaseRecognizerNew().</p>
<h3>static <code>ANTLR3_BOOLEAN</code> recoverFromMismatchedElement (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>pANTLR3_BITSET_LIST</code> followBits) [static]</h3>
<p>This code is factored out from mismatched token and mismatched set recovery. It handles &#8216;single token insertion&#8217; error recovery for both. No tokens are consumed to recover from insertions. Return true if recovery was possible else return false. </p>
<p> References ANTLR3_INT_STREAM_struct::_LA, ANTLR3_EOR_TOKEN_TYPE, ANTLR3_FALSE, ANTLR3_FPRINTF, ANTLR3_TRUE, ANTLR3_TYPE_PARSER, ANTLR3_TYPE_TREE_PARSER, antlr3BitsetLoad(), ANTLR3_BASE_RECOGNIZER_struct::computeCSRuleFollow, ANTLR3_TREE_PARSER_struct::ctnstream, ANTLR3_RECOGNIZER_SHARED_STATE_struct::error, ANTLR3_RECOGNIZER_SHARED_STATE_struct::failed, ANTLR3_BITSET_struct::free, ANTLR3_BITSET_struct::isMember, ANTLR3_TREE_NODE_STREAM_struct::istream, ANTLR3_TOKEN_STREAM_struct::istream, ANTLR3_BITSET_struct::remove, ANTLR3_BASE_RECOGNIZER_struct::reportError, ANTLR3_BASE_RECOGNIZER_struct::state, ANTLR3_BASE_RECOGNIZER_struct::super, ANTLR3_COMMON_TREE_NODE_STREAM_struct::tnstream, ANTLR3_PARSER_struct::tstream, and ANTLR3_BASE_RECOGNIZER_struct::type. </p>
<p> Referenced by antlr3BaseRecognizerNew().</p>
<h3>static void * recoverFromMismatchedSet (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>pANTLR3_BITSET_LIST</code> follow) [static]</h3>
<p>References ANTLR3_FALSE, ANTLR3_FPRINTF, ANTLR3_MISSING_TOKEN_EXCEPTION, ANTLR3_TOKEN_INVALID, ANTLR3_TRUE, ANTLR3_TYPE_PARSER, ANTLR3_TYPE_TREE_PARSER, ANTLR3_TREE_PARSER_struct::ctnstream, ANTLR3_RECOGNIZER_SHARED_STATE_struct::error, ANTLR3_RECOGNIZER_SHARED_STATE_struct::exception, ANTLR3_RECOGNIZER_SHARED_STATE_struct::failed, ANTLR3_BASE_RECOGNIZER_struct::getMissingSymbol, ANTLR3_TREE_NODE_STREAM_struct::istream, ANTLR3_TOKEN_STREAM_struct::istream, ANTLR3_BASE_RECOGNIZER_struct::mismatchIsMissingToken, ANTLR3_BASE_RECOGNIZER_struct::reportError, ANTLR3_BASE_RECOGNIZER_struct::state, ANTLR3_BASE_RECOGNIZER_struct::super, ANTLR3_COMMON_TREE_NODE_STREAM_struct::tnstream, ANTLR3_EXCEPTION_struct::token, ANTLR3_PARSER_struct::tstream, ANTLR3_EXCEPTION_struct::type, and ANTLR3_BASE_RECOGNIZER_struct::type. </p>
<p> Referenced by antlr3BaseRecognizerNew().</p>
<h3>static void * recoverFromMismatchedToken (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>ANTLR3_UINT32</code> ttype, <code>pANTLR3_BITSET_LIST</code> follow) [static]</h3>
<p>Attempt to recover from a single missing or extra token. EXTRA TOKEN </p>
<p> <a href="/docs/linux/man/1-la/">LA</a>(1) is not what we are looking for. If <a href="/docs/linux/man/2-la/">LA</a>(2) has the right token, however, then assume <a href="/docs/linux/man/1-la/">LA</a>(1) is some extra spurious token. Delete it and <a href="/docs/linux/man/2-la/">LA</a>(2) as if we were doing a normal <code>match()</code>, which advances the input. </p>
<p> MISSING TOKEN </p>
<p> If current token is consistent with what could come after ttype then it is ok to &#8216;insert&#8217; the missing token, else throw exception For example, Input &#8216;i=(3;&#8217; is clearly missing the &#8216;)&#8217;. When the parser returns from the nested call to expr, it will have call chain: </p>
<p> stat -&gt; expr -&gt; atom </p>
<p> and it will be trying to match the &#8216;)&#8217; at this point in the derivation: </p>
<p> =&gt; ID &#8216;=&#8217; &#8216;(&#8216; INT &#8216;)&#8217; (&#8216;+&#8217; atom)* &#8216;;&#8217; ^ <code>match()</code> will see that &#8216;;&#8217; doesn&#8217;t match &#8216;)&#8217; and report a mismatched token error. To recover, it sees that <a href="/docs/linux/man/1-la/">LA</a>(1)==&#8217;;&#8217; is in the set of tokens that can follow the &#8216;)&#8217; token reference in rule atom. It can assume that you forgot the &#8216;)&#8217;. </p>
<p> The exception that was passed in, in the java implementation is sorted in the recognizer exception stack in the C version. To &#8216;throw&#8217; it we set the error flag and rules cascade back when this is set. </p>
<p> References ANTLR3_FALSE, ANTLR3_FPRINTF, ANTLR3_MISSING_TOKEN_EXCEPTION, ANTLR3_MISSING_TOKEN_EXCEPTION_NAME, ANTLR3_TRUE, ANTLR3_TYPE_PARSER, ANTLR3_TYPE_TREE_PARSER, ANTLR3_UNWANTED_TOKEN_EXCEPTION, ANTLR3_UNWANTED_TOKEN_EXCEPTION_NAME, antlr3RecognitionExceptionNew(), ANTLR3_BASE_RECOGNIZER_struct::beginResync, ANTLR3_DEBUG_EVENT_LISTENER_struct::beginResync, ANTLR3_INT_STREAM_struct::consume, ANTLR3_TREE_PARSER_struct::ctnstream, ANTLR3_BASE_RECOGNIZER_struct::debugger, ANTLR3_DEBUG_EVENT_LISTENER_struct::endResync, ANTLR3_BASE_RECOGNIZER_struct::endResync, ANTLR3_RECOGNIZER_SHARED_STATE_struct::error, ANTLR3_RECOGNIZER_SHARED_STATE_struct::exception, ANTLR3_EXCEPTION_struct::expecting, ANTLR3_BASE_RECOGNIZER_struct::getCurrentInputSymbol, ANTLR3_BASE_RECOGNIZER_struct::getMissingSymbol, ANTLR3_TREE_NODE_STREAM_struct::istream, ANTLR3_TOKEN_STREAM_struct::istream, ANTLR3_EXCEPTION_struct::message, mismatchIsMissingToken(), ANTLR3_BASE_RECOGNIZER_struct::mismatchIsUnwantedToken, ANTLR3_DEBUG_EVENT_LISTENER_struct::recognitionException, ANTLR3_BASE_RECOGNIZER_struct::reportError, ANTLR3_BASE_RECOGNIZER_struct::state, ANTLR3_BASE_RECOGNIZER_struct::super, ANTLR3_COMMON_TREE_NODE_STREAM_struct::tnstream, ANTLR3_EXCEPTION_struct::token, ANTLR3_PARSER_struct::tstream, ANTLR3_EXCEPTION_struct::type, and ANTLR3_BASE_RECOGNIZER_struct::type. </p>
<p> Referenced by antlr3BaseRecognizerNew().</p>
<h3>static void reportError (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer) [static]</h3>
<p>Report a recognition problem. This method sets errorRecovery to indicate the parser is recovering not parsing. Once in recovery mode, no errors are generated. To get out of recovery mode, the parser must successfully match a token (after a resync). So it will go: </p>
<p> 1. error occurs 2. enter recovery mode, report error 3. consume until token found in resynch set 4. try to resume parsing 5. next <code>match()</code> will reset errorRecovery mode </p>
<p> If you override, make sure to update errorCount if you care about that. </p>
<p> References ANTLR3_TRUE, ANTLR3_BASE_RECOGNIZER_struct::displayRecognitionError, ANTLR3_RECOGNIZER_SHARED_STATE_struct::errorCount, ANTLR3_RECOGNIZER_SHARED_STATE_struct::errorRecovery, ANTLR3_BASE_RECOGNIZER_struct::state, and ANTLR3_RECOGNIZER_SHARED_STATE_struct::tokenNames. </p>
<p> Referenced by antlr3BaseRecognizerNew().</p>
<h3>static void reset (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer) [static]</h3>
<p>References ANTLR3_FALSE, antlr3IntTrieNew(), antlr3StackNew(), ANTLR3_RECOGNIZER_SHARED_STATE_struct::backtracking, ANTLR3_RECOGNIZER_SHARED_STATE_struct::errorCount, ANTLR3_RECOGNIZER_SHARED_STATE_struct::errorRecovery, ANTLR3_RECOGNIZER_SHARED_STATE_struct::failed, ANTLR3_RECOGNIZER_SHARED_STATE_struct::following, ANTLR3_INT_TRIE_struct::free, ANTLR3_STACK_struct::free, ANTLR3_RECOGNIZER_SHARED_STATE_struct::lastErrorIndex, ANTLR3_RECOGNIZER_SHARED_STATE_struct::ruleMemo, and ANTLR3_BASE_RECOGNIZER_struct::state. </p>
<p> Referenced by antlr3BaseRecognizerNew().</p>
<h3>static <code>ANTLR3_BOOLEAN</code> synpred (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, void * ctx, void(*)(void *ctx) predicate) [static]</h3>
<p>A syntactic predicate. Returns true/false depending on whether the specified grammar fragment matches the current input stream. This resets the failed instance var afterwards. </p>
<p> References ANTLR3_FALSE, ANTLR3_FPRINTF, ANTLR3_TRUE, ANTLR3_TYPE_PARSER, ANTLR3_TYPE_TREE_PARSER, ANTLR3_RECOGNIZER_SHARED_STATE_struct::backtracking, ANTLR3_TREE_PARSER_struct::ctnstream, ANTLR3_RECOGNIZER_SHARED_STATE_struct::failed, ANTLR3_TREE_NODE_STREAM_struct::istream, ANTLR3_TOKEN_STREAM_struct::istream, ANTLR3_INT_STREAM_struct::mark, ANTLR3_INT_STREAM_struct::rewind, ANTLR3_BASE_RECOGNIZER_struct::state, ANTLR3_BASE_RECOGNIZER_struct::super, ANTLR3_COMMON_TREE_NODE_STREAM_struct::tnstream, ANTLR3_PARSER_struct::tstream, and ANTLR3_BASE_RECOGNIZER_struct::type. </p>
<p> Referenced by antlr3BaseRecognizerNew().</p>
<h3>static <code>pANTLR3_HASH_TABLE</code> toStrings (<code>pANTLR3_BASE_RECOGNIZER</code> recognizer, <code>pANTLR3_HASH_TABLE</code> tokens) [static]</h3>
<p>Convenience method for template rewrites &#8211; NYI. </p>
<p> Referenced by antlr3BaseRecognizerNew().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
