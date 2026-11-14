---
title: "antlr3-expectingset(3)"
name: "antlr3-expectingset"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-expectingset/"
description: "ANTLR3_EXCEPTION_struct –"
---

<p>ANTLR3_EXCEPTION_struct &#8211; </p>
<p> Base structure for an ANTLR3 exception tracker.</p>
<h2>Synopsis</h2>
<p> #include &lt;<a href="file:/usr/include/antlr3exception.h">antlr3exception.h</a>&gt;</p>
<h3>Data Fields</h3>
<p> <code>ANTLR3_UCHAR</code> <code>c</code><br />
 <i>The current character when an error occurred &#8211; for lexers. </i><br />
 <code>ANTLR3_INT32</code> <code>charPositionInLine</code><br />
 <i>Character position in the line where the error occurred. </i><br />
 void * <code>custom</code><br />
 <i>Pointer for you, the programmer to add anything you like to an exception. </i><br />
 <code>ANTLR3_UINT32</code> <code>decisionNum</code><br />
 <i>decision number for NVE </i><br />
 <code>ANTLR3_UINT32</code> <code>expecting</code><br />
 <i>Indicates the token we were expecting to see next when the error occurred. </i><br />
 <code>pANTLR3_BITSET_LIST</code> <code>expectingSet</code><br />
 <i>Indicates a set of tokens that we were expecting to see one of when the error occurred. </i><br />
 void(* <code>freeCustom</code> )(void *<code>custom</code>)<br />
 <i>Pointer to a routine that is called to free the custom exception structure when the exception is destroyed. </i><br />
 void(* <code>freeEx</code> )(struct <code>ANTLR3_EXCEPTION_struct</code> *ex) </p>
<p> <code>ANTLR3_BOOLEAN</code> <code>freeMessage</code><br />
 <i>If set to ANTLR3_TRUE, this indicates that the message element of this structure should be freed by calling </i><code>ANTLR3_FREE()</code> when the exception is destroyed.<br />
 <code>ANTLR3_MARKER</code> <code>index</code><br />
 <i>Indicates the index of the &#8216;token&#8217; we were looking at when the exception occurred. </i><br />
 <code>pANTLR3_INT_STREAM</code> <code>input</code><br />
 <i>Pointer to the input stream that this exception occurred in. </i><br />
 <code>ANTLR3_UINT32</code> <code>line</code><br />
 <i>Track the line at which the error occurred in case this is generated from a lexer. </i><br />
 void * <code>message</code><br />
 <i>The printable message that goes with this exception, in your preferred encoding format. </i><br />
 void * <code>name</code><br />
 <i>The string name of the exception. </i><br />
 struct <code>ANTLR3_EXCEPTION_struct</code> * <code>nextException</code><br />
 <i>Pointer to the next exception in the chain (if any). </i><br />
 void * <code>node</code><br />
 <i>If this is a tree parser exception then the node is set to point to the node that caused the issue. </i><br />
 void(* <code>print</code> )(struct <code>ANTLR3_EXCEPTION_struct</code> *ex) </p>
<p> void * <code>ruleName</code><br />
 <i>Rule name for failed predicate exception. </i><br />
 <code>ANTLR3_UINT32</code> <code>state</code><br />
 <i>State for NVE. </i><br />
 <code>pANTLR3_STRING</code> <code>streamName</code><br />
 <i>Name of the file/input source for reporting. </i><br />
 void * <code>token</code><br />
 <i>Indicates what the current token/tree was when the error occurred. </i><br />
 <code>ANTLR3_UINT32</code> <code>type</code><br />
 <i>Set to one of the exception type defines:. </i></p>
<h2>Detailed Description</h2>
<p> Base structure for an ANTLR3 exception tracker.</p>
<h2>Field Documentation</h2>
<h3><code>ANTLR3_UCHAR</code> <code>ANTLR3_EXCEPTION_struct::c</code></h3>
<p> The current character when an error occurred &#8211; for lexers. </p>
<p> Referenced by antlr3RecognitionExceptionNew(), and displayRecognitionError().</p>
<h3><code>ANTLR3_INT32</code> <code>ANTLR3_EXCEPTION_struct::charPositionInLine</code></h3>
<p> Character position in the line where the error occurred. </p>
<p> Referenced by antlr3RecognitionExceptionNew(), and displayRecognitionError().</p>
<h3>void* <code>ANTLR3_EXCEPTION_struct::custom</code></h3>
<p> Pointer for you, the programmer to add anything you like to an exception. </p>
<p> Referenced by antlr3ExceptionFree().</p>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_EXCEPTION_struct::decisionNum</code></h3>
<p> decision number for NVE </p>
<p> Referenced by noViableAlt().</p>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_EXCEPTION_struct::expecting</code></h3>
<p> Indicates the token we were expecting to see next when the error occurred. </p>
<p> Referenced by displayRecognitionError(), mismatch(), mismatchIsUnwantedToken(), and recoverFromMismatchedToken().</p>
<h3><code>pANTLR3_BITSET_LIST</code> <code>ANTLR3_EXCEPTION_struct::expectingSet</code></h3>
<p> Indicates a set of tokens that we were expecting to see one of when the error occurred. It is a following bitset list, so you can use load it and use -&gt;toIntList() on it to generate an array of integer tokens that it represents. </p>
<p> Referenced by displayRecognitionError().</p>
<h3>void(* <code>ANTLR3_EXCEPTION_struct::freeCustom</code>)(void *<code>custom</code>)</h3>
<p> Pointer to a routine that is called to free the custom exception structure when the exception is destroyed. Set to NULL if nothing should be done. </p>
<p> Referenced by antlr3ExceptionFree().</p>
<h3>void(* <code>ANTLR3_EXCEPTION_struct::freeEx</code>)(struct <code>ANTLR3_EXCEPTION_struct</code> *ex)</h3>
<p> Referenced by antlr3ExceptionNew(), and freeBR().</p>
<h3><code>ANTLR3_BOOLEAN</code> <code>ANTLR3_EXCEPTION_struct::freeMessage</code></h3>
<p> If set to ANTLR3_TRUE, this indicates that the message element of this structure should be freed by calling <code>ANTLR3_FREE()</code> when the exception is destroyed. </p>
<p> Referenced by antlr3ExceptionFree(), and antlr3ExceptionNew().</p>
<h3><code>ANTLR3_MARKER</code> <code>ANTLR3_EXCEPTION_struct::index</code></h3>
<p> Indicates the index of the &#8216;token&#8217; we were looking at when the exception occurred. </p>
<p> Referenced by antlr3RecognitionExceptionNew(), and displayRecognitionError().</p>
<h3><code>pANTLR3_INT_STREAM</code> <code>ANTLR3_EXCEPTION_struct::input</code></h3>
<p> Pointer to the input stream that this exception occurred in. </p>
<p> Referenced by antlr3RecognitionExceptionNew().</p>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_EXCEPTION_struct::line</code></h3>
<p> Track the line at which the error occurred in case this is generated from a lexer. We need to track this since the unexpected char doesn&#8217;t carry the line info. </p>
<p> Referenced by antlr3RecognitionExceptionNew(), and displayRecognitionError().</p>
<h3>void* <code>ANTLR3_EXCEPTION_struct::message</code></h3>
<p> The printable message that goes with this exception, in your preferred encoding format. ANTLR just uses ASCII by default but you can ignore these messages or convert them to another format or whatever of course. They are really internal messages that you then decide how to print out in a form that the users of your product will understand, as they are unlikely to know what to do with &#8216;Recognition exception at: [[TOK_GERUND&#8230;.. &#8216; ;-) </p>
<p> Referenced by antlr3ExceptionFree(), antlr3ExceptionNew(), antlr3ExceptionPrint(), antlr3RecognitionExceptionNew(), displayRecognitionError(), noViableAlt(), and recoverFromMismatchedToken().</p>
<h3>void* <code>ANTLR3_EXCEPTION_struct::name</code></h3>
<p> The string name of the exception. </p>
<p> Referenced by antlr3ExceptionNew(), antlr3MTExceptionNew(), antlr3MTNExceptionNew(), displayRecognitionError(), and mismatch().</p>
<h3>struct <code>ANTLR3_EXCEPTION_struct</code>* <code>ANTLR3_EXCEPTION_struct::nextException</code> [read]</h3>
<p> Pointer to the next exception in the chain (if any). </p>
<p> Referenced by antlr3ExceptionFree(), antlr3ExceptionPrint(), and antlr3RecognitionExceptionNew().</p>
<h3>void* <code>ANTLR3_EXCEPTION_struct::node</code></h3>
<p> If this is a tree parser exception then the node is set to point to the node that caused the issue.</p>
<h3>void(* <code>ANTLR3_EXCEPTION_struct::print</code>)(struct <code>ANTLR3_EXCEPTION_struct</code> *ex)</h3>
<p> Referenced by antlr3ExceptionNew().</p>
<h3>void* <code>ANTLR3_EXCEPTION_struct::ruleName</code></h3>
<p> Rule name for failed predicate exception.</p>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_EXCEPTION_struct::state</code></h3>
<p> State for NVE. </p>
<p> Referenced by noViableAlt().</p>
<h3><code>pANTLR3_STRING</code> <code>ANTLR3_EXCEPTION_struct::streamName</code></h3>
<p> Name of the file/input source for reporting. Note that this may be NULL!! </p>
<p> Referenced by antlr3RecognitionExceptionNew(), and displayRecognitionError().</p>
<h3>void* <code>ANTLR3_EXCEPTION_struct::token</code></h3>
<p> Indicates what the current token/tree was when the error occurred. Since not all input streams will be able to retrieve the nth token, we track it here instead. This is for parsers, and even tree parsers may set this. </p>
<p> Referenced by antlr3RecognitionExceptionNew(), displayRecognitionError(), recoverFromMismatchedSet(), and recoverFromMismatchedToken().</p>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_EXCEPTION_struct::type</code></h3>
<p> Set to one of the exception type defines:. .IP &quot;*&quot; 2 <code>ANTLR3_RECOGNITION_EXCEPTION</code></p>
<dl COMPACT>
<dt>*</p>
<dd> <code>ANTLR3_MISMATCHED_TOKEN_EXCEPTION</code></p>
<dt>*</p>
<dd> <code>ANTLR3_NO_VIABLE_ALT_EXCEPTION</code></p>
<dt>*</p>
<dd> <code>ANTLR3_MISMATCHED_SET_EXCEPTION</code></p>
<dt>*</p>
<dd> <code>ANTLR3_EARLY_EXIT_EXCEPTION</code></p>
<dt>*</p>
<dd> <code>ANTLR3_FAILED_PREDICATE_EXCEPTION</code></p>
<dt>*</p>
<dd> <code>ANTLR3_EARLY_EXIT_EXCEPTION</code></dl>
<p> Referenced by antlr3ExceptionNew(), antlr3ExceptionPrint(), antlr3MTExceptionNew(), antlr3MTNExceptionNew(), displayRecognitionError(), mismatch(), noViableAlt(), recoverFromMismatchedSet(), and recoverFromMismatchedToken(). </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for ANTLR3C from the source code.</p>
