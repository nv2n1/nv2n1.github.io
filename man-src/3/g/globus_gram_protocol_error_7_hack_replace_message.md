---
title: "globus_gram_protocol_error_7_hack_replace_message(3)"
name: "globus_gram_protocol_error_7_hack_replace_message"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gram_protocol_error_7_hack_replace_message/"
description: "Error Messages –"
---

<h2 class="name">NAME</h2>
<p> Error Messages &#8211; </p>
<p> GRAM Error Messages Functions in this section handle converting GRAM error codes to strings which can help the user diagnose GRAM problems.</p>
<h3>Functions</h3>
<p> const char * <code>globus_gram_protocol_error_string</code> (int error_code)<br />
 <i>Get a description of a a GRAM error code. </i><br />
 void <code>globus_gram_protocol_error_7_hack_replace_message</code> (const char *message)<br />
 <i>Replace the error message associated with error 7 with a custom message. </i><br />
 void <code>globus_gram_protocol_error_10_hack_replace_message</code> (const char *message)<br />
 <i>Replace the error message associated with error 10 with a custom message. </i></p>
<h2>Detailed Description</h2>
<p> GRAM Error Messages Functions in this section handle converting GRAM error codes to strings which can help the user diagnose GRAM problems. </p>
<h2>Function Documentation</h2>
<h3>void globus_gram_protocol_error_10_hack_replace_message (const char *message)</h3>
<p> Replace the error message associated with error 10 with a custom message. The <code>globus_gram_protocol_error_10_hack_replace_message()</code> function creates a custom version of the error message for the error <i>GLOBUS_GRAM_PROTOCOL_ERROR_PROTOCOL_FAILED</i>. The string pointed to by the <i>message</i> parameter is copied to thread-local storage, and subsequent calls to <code>globus_gram_protocol_error_string()</code> with this error number will return this copy of the string. Each time <code>globus_gram_protocol_error_10_hack_replace_message()</code> is called for a particular thread, the previous message is freed. </p>
<p> The purpose of this function is to allow more meaningful error messages to be generated when protocol errors occur. In particular, the specific XIO error reason can be used in place of a generic protocol failure message. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>message</i> The new message to be associated with the GLOBUS_GRAM_PROTOCOL_ERROR_PROTOCOL_FAILED error code.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Since Globus 5.0.0, this function uses thread-specific storage, so that the value returned by <code>globus_gram_protocol_error_string()</code> for GLOBUS_GRAM_PROTOCOL_ERROR_PROTOCOL_FAILED is that for the last authorization error where <code>globus_gram_protocol_error_10_hack_replace_message()</code> was called from this thread.</dl>
<h3>void globus_gram_protocol_error_7_hack_replace_message (const char *message)</h3>
<p> Replace the error message associated with error 7 with a custom message. The <code>globus_gram_protocol_error_7_hack_replace_message()</code> function creates a custom version of the error message for the error <i>GLOBUS_GRAM_PROTOCOL_ERROR_AUTHORIZATION</i>. The string pointed to by the <i>message</i> parameter is copied to thread-local storage, and subsequent calls to <code>globus_gram_protocol_error_string()</code> with this error number will return this copy of the string. Each time <code>globus_gram_protocol_error_7_hack_replace_message()</code> is called for a particular thread, the previous message is freed. </p>
<p> The purpose of this function is to allow more meaningful error messages to be generated when authentication failures occur. In particular, the specific GSSAPI error reason can be used in place of a generic authorization failure message. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>message</i> The new message to be associated with the GLOBUS_GRAM_PROTOCOL_ERROR_AUTHORIZATION error code.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Since Globus 5.0.0, this function uses thread-specific storage, so that the value returned by <code>globus_gram_protocol_error_string()</code> for GLOBUS_GRAM_PROTOCOL_ERROR_AUTHORIZATION is that for the last authorization error where <code>globus_gram_protocol_error_7_hack_replace_message()</code> was called from this thread.</dl>
<h3>const char* globus_gram_protocol_error_string (interror_code)</h3>
<p> Get a description of a a GRAM error code. The <code>globus_gram_protocol_error_string()</code> function takes a GRAM error code value and returns the associated error code string for the message. The string is statically allocated by the GRAM Protocol library and should not be modified or freed by the caller. The string is intended to complete a sentence of the form &#8216;[operation] failed because &#8230;&#8217; </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>error_code</i> The error code to translate into a string.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The <code>globus_gram_protocol_error_string()</code> function returns a static string containing an explanation of the error.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gram_protocol from the source code. </p>
<h2>Index</h2>
