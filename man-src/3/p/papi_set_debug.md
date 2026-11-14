---
title: "papi_set_debug(3)"
name: "papi_set_debug"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_set_debug/"
description: "PAPI_set_debug –"
---

<p>PAPI_set_debug &#8211; </p>
<p> Set the current debug level for error output from PAPI.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<p><code>C Prototype:</code></p>
<dl COMPACT>
<dd>#include &lt;<code>papi.h</code>&gt; </p>
<p>&nbsp;<wbr>int&nbsp;<wbr><code>PAPI_set_debug(&nbsp;<wbr>int level&nbsp;<wbr>)</code>;</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>level</i> one of the constants shown in the table below and defined in the <code>papi.h</code> header file. </p>
<p>&nbsp;<wbr>The possible debug levels for debugging are shown below.&nbsp;<wbr> </p>
<dl COMPACT>
<dt>&bull;</p>
<dd>PAPI_QUIET Do not print anything, just return the error code</p>
<dt>&bull;</p>
<dd>PAPI_VERB_ECONT Print error message and continue</p>
<dt>&bull;</p>
<dd>PAPI_VERB_ESTOP Print error message and exit </p>
<p>&nbsp;<wbr></dl>
</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>PAPI_OK</i><br />
 <i>PAPI_EINVAL</i> The debug level is invalid. </p>
<p>&nbsp;<wbr>The current debug level is used by both the internal error and debug message handler subroutines.&nbsp;<wbr> </p>
<p>&nbsp;<wbr>The debug handler is only used if the library was compiled with -DDEBUG.&nbsp;<wbr> </p>
<p>&nbsp;<wbr>The debug handler is called when there is an error upon a call to the PAPI API. </p>
<p>&nbsp;<wbr>The error handler is always active and its behavior cannot be modified except for whether or not it prints anything.</dl>
<p> The default PAPI debug handler prints out messages in the following form: </p>
<p>&nbsp;<wbr>PAPI Error: Error Code code, symbol, description </p>
<p> If the error was caused from a system call and the return code is PAPI_ESYS, the message will have a colon space and the error string as reported by strerror() appended to the end. </p>
<p> The PAPI error handler prints out messages in the following form: </p>
<p>&nbsp;<wbr>PAPI Error: message.&nbsp;<wbr> </p>
<p>&nbsp;<wbr> </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>This is the ONLY function that may be called BEFORE <code>PAPI_library_init()</code>. </p>
<p>&nbsp;<wbr></dl>
<p> <code>Example:</code></p>
<dl COMPACT>
<dd>
<pre>int ret;
ret = PAPI_set_debug(PAPI_VERB_ECONT);
if ( ret != PAPI_OK ) handle_error();
* </pre>
</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_library_init</code> </p>
<p> <code>PAPI_get_opt</code> </p>
<p> <code>PAPI_set_opt</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
