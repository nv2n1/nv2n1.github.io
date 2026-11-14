---
title: "hx509_set_error_string(3)"
name: "hx509_set_error_string"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hx509_set_error_string/"
description: "hx509 error functions –"
---

<h2 class="name">NAME</h2>
<p> hx509 error functions &#8211; </p>
<h3>Functions</h3>
<p> void <code>hx509_clear_error_string</code> (hx509_context context) </p>
<p> void <code>hx509_set_error_stringv</code> (hx509_context context, int flags, int code, const char *fmt, va_list ap) </p>
<p> void <code>hx509_set_error_string</code> (hx509_context context, int flags, int code, const char *fmt,&#8230;) </p>
<p> char * <code>hx509_get_error_string</code> (hx509_context context, int error_code) </p>
<p> void <code>hx509_free_error_string</code> (char *str) </p>
<p> void <code>hx509_err</code> (hx509_context context, int exit_code, int error_code, const char *fmt,&#8230;) </p>
<h2>Detailed Description</h2>
<p> See the <code>Hx509 error reporting functions</code> for description and examples.</p>
<h2>Function Documentation</h2>
<h3>void hx509_clear_error_string (hx509_contextcontext)</h3>
<p> Resets the error strings the hx509 context. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A hx509 context.</dl>
<h3>void hx509_err (hx509_contextcontext, intexit_code, interror_code, const char *fmt, &#8230;)</h3>
<p> Print error message and fatally exit from error code </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A hx509 context.<br />
 <i>exit_code</i> exit() code from process.<br />
 <i>error_code</i> Error code for the reason to exit.<br />
 <i>fmt</i> format string with the exit message.<br />
 <i>&#8230;</i> argument to format string.</dl>
<h3>void hx509_free_error_string (char *str)</h3>
<p> Free error string returned by <code>hx509_get_error_string()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>str</i> error string to free.</dl>
<h3>char * hx509_get_error_string (hx509_contextcontext, interror_code)</h3>
<p> Get an error string from context associated with error_code. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A hx509 context.<br />
 <i>error_code</i> Get error message for this error code.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> error string, free with <code>hx509_free_error_string()</code>.</dl>
<h3>void hx509_set_error_string (hx509_contextcontext, intflags, intcode, const char *fmt, &#8230;)</h3>
<p> See <code>hx509_set_error_stringv()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A hx509 context.<br />
 <i>flags</i></p>
<dl>
<dt>&bull;</p>
<dd> HX509_ERROR_APPEND appends the error string to the old messages (code is updated).</dl>
<p> <i>code</i> error code related to error message<br />
 <i>fmt</i> error message format<br />
 <i>&#8230;</i> arguments to error message format</dl>
<h3>void hx509_set_error_stringv (hx509_contextcontext, intflags, intcode, const char *fmt, va_listap)</h3>
<p> Add an error message to the hx509 context. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A hx509 context.<br />
 <i>flags</i></p>
<dl>
<dt>&bull;</p>
<dd> HX509_ERROR_APPEND appends the error string to the old messages (code is updated).</dl>
<p> <i>code</i> error code related to error message<br />
 <i>fmt</i> error message format<br />
 <i>ap</i> arguments to error message format</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Heimdalx509library from the source code. </p>
<h2>Index</h2>
