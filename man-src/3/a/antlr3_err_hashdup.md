---
title: "antlr3_err_hashdup(3)"
name: "antlr3_err_hashdup"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3_err_hashdup/"
description: "include/antlr3errors.h –"
---

<p>include/antlr3errors.h &#8211; </p>
<h2>Synopsis</h2>
<h3>Defines</h3>
<p>#define <code>ANTLR3_CHARSTREAM_EOF</code> 0xFFFFFFFF<br />
 <i>Indicates end of character stream and is an invalid Unicode code point. </i><br />
 #define <code>ANTLR3_ERR_BASE</code> 0 </p>
<p> #define <code>ANTLR3_ERR_HASHDUP</code> (ANTLR3_ERR_BASE + 3) </p>
<p> #define <code>ANTLR3_ERR_NOFILE</code> (ANTLR3_ERR_BASE + 2) </p>
<p> #define <code>ANTLR3_ERR_NOMEM</code> (ANTLR3_ERR_BASE + 1) </p>
<p> #define <code>ANTLR3_FAIL</code> 1 </p>
<p> #define <code>ANTLR3_FALSE</code> 0 </p>
<p> #define <code>ANTLR3_SUCCESS</code> 0 </p>
<p> #define <code>ANTLR3_TRUE</code> 1 </p>
<p> #define <code>MEMO_RULE_FAILED</code> 0xFFFFFFFE<br />
 <i>Indicates memoizing on a rule failed. </i><br />
 #define <code>MEMO_RULE_UNKNOWN</code> 0xFFFFFFFF </p>
<h2>Define Documentation</h2>
<h3>#define ANTLR3_CHARSTREAM_EOF 0xFFFFFFFF</h3>
<p>Indicates end of character stream and is an invalid Unicode code point. </p>
<p> Referenced by antlr3AsciiLA(), antlr3AsciiLA_ucase(), antlr3UCS2LA(), and nextTokenStr().</p>
<h3>#define ANTLR3_ERR_BASE 0</h3>
<h3>#define ANTLR3_ERR_HASHDUP (ANTLR3_ERR_BASE + 3)</h3>
<p>Referenced by antlr3HashPut(), and antlr3HashPutI().</p>
<h3>#define ANTLR3_ERR_NOFILE (ANTLR3_ERR_BASE + 2)</h3>
<p>Referenced by antlr3readAscii().</p>
<h3>#define ANTLR3_ERR_NOMEM (ANTLR3_ERR_BASE + 1)</h3>
<p>Referenced by antlr3EnumNew(), antlr3HashPut(), antlr3HashPutI(), antlr3IntTrieNew(), antlr3ListNew(), antlr3readAscii(), antlr3StackNew(), and antlr3VectorNew().</p>
<h3>#define ANTLR3_FAIL 1</h3>
<p>Referenced by antlr3EnumNext().</p>
<h3>#define ANTLR3_FALSE 0</h3>
<p>Referenced by alreadyParsedRule(), antlr3BaseRecognizerNew(), antlr3BitsetEquals(), antlr3BitsetIsNil(), antlr3BitsetMember(), antlr3CommonTokenDebugStreamSourceNew(), antlr3CommonTokenStreamSourceNew(), antlr3CommonTreeNodeStreamNew(), antlr3CommonTreeNodeStreamNewStream(), antlr3HashPut(), antlr3HashPutI(), antlr3HashTableNew(), antlr3NewAsciiStringInPlaceStream(), antlr3NewUCS2StringInPlaceStream(), antlr3RecognitionExceptionNew(), antlr3RewriteRuleElementStreamNewAE(), antlr3RewriteRuleElementStreamNewAEV(), antlr3SetVectorApi(), antlr3TopoNew(), antlr3VectorFree(), antlr3VectorSwap(), combineFollows(), computeCSRuleFollow(), computeErrorRecoverySet(), consumeInitialHiddenTokens(), consumeUntilSet(), DFS(), fillBuffer(), freeNodeRS(), freeRS(), handshake(), hasNext(), intTrieAdd(), intTrieDel(), isNilNode(), match(), matchAny(), matchc(), matchRange(), matchs(), mismatchIsMissingToken(), mismatchIsUnwantedToken(), newToken(), nextTokenStr(), recover(), recoverFromMismatchedElement(), recoverFromMismatchedSet(), recoverFromMismatchedToken(), replaceChildren(), reset(), setChild(), setDebugListener(), sockSend(), sortToArray(), synpred(), toInt32_16(), and toStringTree().</p>
<h3>#define ANTLR3_SUCCESS 0</h3>
<p>Referenced by antlr3AsciiFileStreamNew(), antlr3BitsetList(), antlr3EnumNext(), antlr3HashPut(), antlr3HashPutI(), and antlr3readAscii().</p>
<h3>#define ANTLR3_TRUE 1</h3>
<p>Referenced by add(), addChild(), alreadyParsedRule(), antlr3BitsetEquals(), antlr3BitsetIsNil(), antlr3BitsetMember(), antlr3BitsetToIntList(), antlr3CommonTreeNodeStreamFree(), antlr3CommonTreeNodeStreamNewStream(), antlr3dfapredict(), antlr3ExceptionFree(), antlr3HashPut(), antlr3HashRemove(), antlr3HashTableNew(), antlr3LexerNew(), antlr3NewAsciiStringCopyStream(), antlr3readAscii(), antlr3RecognitionExceptionNew(), antlr3RewriteRuleElementStreamNewAEV(), antlr3TokenFactoryNew(), antlr3VectorFactoryNew(), antlr3VectorSwap(), closeVectorFactory(), combineFollows(), dbgConsume(), dbgTokLT(), DFS(), expungeRS(), freeNodeRS(), freeRS(), getTokensSet(), handshake(), hasNext(), intTrieAdd(), isNilNode(), match(), matchc(), matchRange(), matchs(), memoize(), mismatchIsMissingToken(), mismatchIsUnwantedToken(), newPoolToken(), newRaw16(), newRaw8(), newVector(), nextNode(), nextTokenStr(), noViableAlt(), recoverFromMismatchedElement(), recoverFromMismatchedSet(), recoverFromMismatchedToken(), replaceChildren(), reportError(), reset(), sockSend(), sortToArray(), sortVector(), synpred(), toInt32_16(), and toString().</p>
<h3>#define MEMO_RULE_FAILED 0xFFFFFFFE</h3>
<p>Indicates memoizing on a rule failed. </p>
<p> Referenced by alreadyParsedRule(), and memoize().</p>
<h3>#define MEMO_RULE_UNKNOWN 0xFFFFFFFF</h3>
<p>Referenced by alreadyParsedRule(), and getRuleMemoization().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
