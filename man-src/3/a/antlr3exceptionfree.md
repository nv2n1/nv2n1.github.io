---
title: "antlr3exceptionfree(3)"
name: "antlr3exceptionfree"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3exceptionfree/"
description: "src/antlr3exception.c –"
---

<p>src/antlr3exception.c &#8211; </p>
<p> Contains default functions for creating and destroying as well as otherwise handling ANTLR3 standard exception structures.</p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/antlr3exception.h">antlr3exception.h</a>&gt; </p>
<h3>Functions</h3>
<p>static void <code>antlr3ExceptionFree</code> (<code>pANTLR3_EXCEPTION</code> ex)<br />
 <i>Frees up a chain of ANTLR3 exceptions. </i><br />
 <code>pANTLR3_EXCEPTION</code> <code>antlr3ExceptionNew</code> (<code>ANTLR3_UINT32</code> exception, void *name, void *message, <code>ANTLR3_BOOLEAN</code> freeMessage)<br />
 <i>Creates a new ANTLR3 exception structure. </i><br />
 static void <code>antlr3ExceptionPrint</code> (<code>pANTLR3_EXCEPTION</code> ex)<br />
 <i>Prints out the message in all the exceptions in the supplied chain. </i></p>
<h2>Detailed Description</h2>
<p>Contains default functions for creating and destroying as well as otherwise handling ANTLR3 standard exception structures. </p>
<h2>Function Documentation</h2>
<h3>static void antlr3ExceptionFree (<code>pANTLR3_EXCEPTION</code> ex) [static]</h3>
<p>Frees up a chain of ANTLR3 exceptions. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ex</i> Pointer to the first exception in the chain to free.</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>ANTLR3_EXCEPTION</code></dl>
<p> References ANTLR3_FREE, ANTLR3_TRUE, ANTLR3_EXCEPTION_struct::custom, ANTLR3_EXCEPTION_struct::freeCustom, ANTLR3_EXCEPTION_struct::freeMessage, ANTLR3_EXCEPTION_struct::message, next(), and ANTLR3_EXCEPTION_struct::nextException. </p>
<p> Referenced by antlr3ExceptionNew().</p>
<h3><code>pANTLR3_EXCEPTION</code> antlr3ExceptionNew (<code>ANTLR3_UINT32</code> exception, void * name, void * message, <code>ANTLR3_BOOLEAN</code> freeMessage)</h3>
<p>Creates a new ANTLR3 exception structure. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>exception</i> One of the ANTLR3_xxx_EXCEPTION indicators such as <code>ANTLR3_RECOGNITION_EXCEPTION</code><br />
 <i>message</i> Pointer to message string<br />
 <i>freeMessage</i> Set to ANTLR3_TRUE if the message parameter should be freed by a call to <code>ANTLR3_FREE()</code> when the exception is destroyed.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Pointer to newly initialized exception structure, or an ANTLR3_ERR_xx defined value upon failure.</dl>
<p> An exception is &#8216;thrown&#8217; by a recognizer when input is seen that is not predicted by the grammar productions or when some other error condition occurs. In C we do not have the luxury of try and catch blocks, so exceptions are added in the order they occur to a list in the baserecognizer structure. The last one to be thrown is inserted at the head of the list and the one currently installed is pointed to by the newly installed exception. </p>
<p> <code>Remarks:</code></p>
<dl COMPACT>
<dd>After an exception is created, you may add a pointer to your own structure and a pointer to a function to free this structure when the exception is destroyed.</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>ANTLR3_EXCEPTION</code></dl>
<p> References ANTLR3_CALLOC, antlr3ExceptionFree(), antlr3ExceptionPrint(), ANTLR3_EXCEPTION_struct::freeEx, ANTLR3_EXCEPTION_struct::freeMessage, ANTLR3_EXCEPTION_struct::message, ANTLR3_EXCEPTION_struct::name, ANTLR3_EXCEPTION_struct::print, and ANTLR3_EXCEPTION_struct::type. </p>
<p> Referenced by antlr3RecognitionExceptionNew().</p>
<h3>static void antlr3ExceptionPrint (<code>pANTLR3_EXCEPTION</code> ex) [static]</h3>
<p>Prints out the message in all the exceptions in the supplied chain. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ex</i> Pointer to the exception structure to print.</dl>
<p> <code>Remarks:</code></p>
<dl COMPACT>
<dd>You may wish to override this function by installing a pointer to a new function in the base recognizer context structure.</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>ANTLR3_BASE_RECOGNIZER</code></dl>
<p> References ANTLR3_FPRINTF, ANTLR3_EXCEPTION_struct::message, ANTLR3_EXCEPTION_struct::nextException, and ANTLR3_EXCEPTION_struct::type. </p>
<p> Referenced by antlr3ExceptionNew().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
