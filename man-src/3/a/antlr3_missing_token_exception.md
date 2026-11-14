---
title: "antlr3_missing_token_exception(3)"
name: "antlr3_missing_token_exception"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3_missing_token_exception/"
description: "include/antlr3exception.h –"
---

<p>include/antlr3exception.h &#8211; </p>
<p> Contains the definition of a basic ANTLR3 exception structure created by a recognizer when errors are found/predicted.</p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/antlr3defs.h">antlr3defs.h</a>&gt; </p>
<h3>Data Structures</h3>
<p>struct <code>ANTLR3_EXCEPTION_struct</code><br />
 <i>Base structure for an ANTLR3 exception tracker. </i></p>
<h3>Defines</h3>
<p>#define <code>ANTLR3_EARLY_EXIT_EXCEPTION</code> 5 </p>
<p> #define <code>ANTLR3_EARLY_EXIT_NAME</code> &#8216;Early exit&#8217; </p>
<p> #define <code>ANTLR3_FAILED_PREDICATE_EXCEPTION</code> 6 </p>
<p> #define <code>ANTLR3_FAILED_PREDICATE_NAME</code> &#8216;Predicate failed!&#8217; </p>
<p> #define <code>ANTLR3_MISMATCHED_EX_NAME</code> &#8216;Mismatched Token Exception&#8217;<br />
 <i>Name of </i><code>ANTLR3_MISMATCHED_TOKEN_EXCEPTION</code>.<br />
 #define <code>ANTLR3_MISMATCHED_SET_EXCEPTION</code> 4 </p>
<p> #define <code>ANTLR3_MISMATCHED_SET_NAME</code> &#8216;Mismatched set&#8217; </p>
<p> #define <code>ANTLR3_MISMATCHED_TOKEN_EXCEPTION</code> 2<br />
 <i>Indicates that the recognizer was expecting one token and found a a different one. </i><br />
 #define <code>ANTLR3_MISMATCHED_TREE_NODE_EXCEPTION</code> 7 </p>
<p> #define <code>ANTLR3_MISMATCHED_TREE_NODE_NAME</code> &#8216;Mismatched tree node!&#8217; </p>
<p> #define <code>ANTLR3_MISSING_TOKEN_EXCEPTION</code> 10 </p>
<p> #define <code>ANTLR3_MISSING_TOKEN_EXCEPTION_NAME</code> &#8216;Missing token&#8217; </p>
<p> #define <code>ANTLR3_NO_VIABLE_ALT_EXCEPTION</code> 3<br />
 <i>Recognizer could not find a valid alternative from the input. </i><br />
 #define <code>ANTLR3_NO_VIABLE_ALT_NAME</code> &#8216;No Viable Alt&#8217;<br />
 <i>Name of </i><code>ANTLR3_NO_VIABLE_ALT_EXCEPTION</code>.<br />
 #define <code>ANTLR3_RECOGNITION_EX_NAME</code> &#8216;Recognition Exception&#8217;<br />
 <i>Name of exception </i><code>ANTLR3_RECOGNITION_EXCEPTION</code>.<br />
 #define <code>ANTLR3_RECOGNITION_EXCEPTION</code> 1<br />
 <i>Indicates that the recognizer received a token in the input that was not predicted. </i><br />
 #define <code>ANTLR3_REWRITE_EARLY_EXCEPTION</code> 8 </p>
<p> #define <code>ANTLR3_REWRITE_EARLY_EXCEPTION_NAME</code> &#8216;Mismatched tree node!&#8217; </p>
<p> #define <code>ANTLR3_UNWANTED_TOKEN_EXCEPTION</code> 9 </p>
<p> #define <code>ANTLR3_UNWANTED_TOKEN_EXCEPTION_NAME</code> &#8216;Extraneous token&#8217; </p>
<h3>Typedefs</h3>
<p>typedef struct <code>ANTLR3_EXCEPTION_struct</code> <code>ANTLR3_EXCEPTION</code><br />
 <i>Base structure for an ANTLR3 exception tracker. </i></p>
<h2>Detailed Description</h2>
<p>Contains the definition of a basic ANTLR3 exception structure created by a recognizer when errors are found/predicted. </p>
<h2>Define Documentation</h2>
<h3>#define ANTLR3_EARLY_EXIT_EXCEPTION 5</h3>
<p>Referenced by displayRecognitionError().</p>
<h3>#define ANTLR3_EARLY_EXIT_NAME &#8216;Early exit&#8217;</h3>
<h3>#define ANTLR3_FAILED_PREDICATE_EXCEPTION 6</h3>
<h3>#define ANTLR3_FAILED_PREDICATE_NAME &#8216;Predicate failed!&#8217;</h3>
<h3>#define ANTLR3_MISMATCHED_EX_NAME &#8216;Mismatched Token Exception&#8217;</h3>
<p>Name of <code>ANTLR3_MISMATCHED_TOKEN_EXCEPTION</code>. </p>
<p> Referenced by antlr3MTExceptionNew().</p>
<h3>#define ANTLR3_MISMATCHED_SET_EXCEPTION 4</h3>
<p>Referenced by displayRecognitionError().</p>
<h3>#define ANTLR3_MISMATCHED_SET_NAME &#8216;Mismatched set&#8217;</h3>
<h3>#define ANTLR3_MISMATCHED_TOKEN_EXCEPTION 2</h3>
<p>Indicates that the recognizer was expecting one token and found a a different one. </p>
<p> Referenced by antlr3MTExceptionNew(), and displayRecognitionError().</p>
<h3>#define ANTLR3_MISMATCHED_TREE_NODE_EXCEPTION 7</h3>
<p>Referenced by antlr3MTNExceptionNew().</p>
<h3>#define ANTLR3_MISMATCHED_TREE_NODE_NAME &#8216;Mismatched tree node!&#8217;</h3>
<p>Referenced by antlr3MTNExceptionNew().</p>
<h3>#define ANTLR3_MISSING_TOKEN_EXCEPTION 10</h3>
<p>Referenced by displayRecognitionError(), mismatch(), recoverFromMismatchedSet(), and recoverFromMismatchedToken().</p>
<h3>#define ANTLR3_MISSING_TOKEN_EXCEPTION_NAME &#8216;Missing token&#8217;</h3>
<p>Referenced by mismatch(), and recoverFromMismatchedToken().</p>
<h3>#define ANTLR3_NO_VIABLE_ALT_EXCEPTION 3</h3>
<p>Recognizer could not find a valid alternative from the input. </p>
<p> Referenced by displayRecognitionError(), and noViableAlt().</p>
<h3>#define ANTLR3_NO_VIABLE_ALT_NAME &#8216;No Viable Alt&#8217;</h3>
<p>Name of <code>ANTLR3_NO_VIABLE_ALT_EXCEPTION</code>.</p>
<h3>#define ANTLR3_RECOGNITION_EX_NAME &#8216;Recognition Exception&#8217;</h3>
<p>Name of exception <code>ANTLR3_RECOGNITION_EXCEPTION</code>. </p>
<p> Referenced by antlr3RecognitionExceptionNew().</p>
<h3>#define ANTLR3_RECOGNITION_EXCEPTION 1</h3>
<p>Indicates that the recognizer received a token in the input that was not predicted. </p>
<p> Referenced by antlr3RecognitionExceptionNew(), and displayRecognitionError().</p>
<h3>#define ANTLR3_REWRITE_EARLY_EXCEPTION 8</h3>
<h3>#define ANTLR3_REWRITE_EARLY_EXCEPTION_NAME &#8216;Mismatched tree node!&#8217;</h3>
<h3>#define ANTLR3_UNWANTED_TOKEN_EXCEPTION 9</h3>
<p>Referenced by displayRecognitionError(), mismatch(), and recoverFromMismatchedToken().</p>
<h3>#define ANTLR3_UNWANTED_TOKEN_EXCEPTION_NAME &#8216;Extraneous token&#8217;</h3>
<p>Referenced by mismatch(), and recoverFromMismatchedToken().</p>
<h2>Typedef Documentation</h2>
<h3>typedef struct <code>ANTLR3_EXCEPTION_struct</code></h3>
<p>&nbsp;<wbr>&nbsp;<wbr><code>ANTLR3_EXCEPTION</code>&quot; </p>
<p> Base structure for an ANTLR3 exception tracker.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
