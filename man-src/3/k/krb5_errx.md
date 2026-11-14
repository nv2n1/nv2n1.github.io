---
title: "krb5_errx(3)"
name: "krb5_errx"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5_errx/"
description: "Heimdal Kerberos 5 error reporting functions –"
---

<h2 class="name">NAME</h2>
<p> Heimdal Kerberos 5 error reporting functions &#8211; </p>
<h3>Functions</h3>
<p> KRB5_LIB_FUNCTION char<br />
 *KRB5_LIB_CALL <code>KRB5_DEPRECATED_FUNCTION</code> (&#8216;Use <code>krb5_get_error_message</code> instead&#8217;)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_eai_to_heim_errno</code> (int eai_errno, int system_error)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_h_errno_to_heim_errno</code> (int eai_errno)&quot; </p>
<p> KRB5_LIB_FUNCTION void<br />
 KRB5_LIB_CALL <code>krb5_clear_error_message</code> (krb5_context context)&quot; </p>
<p> KRB5_LIB_FUNCTION void<br />
 KRB5_LIB_CALL <code>krb5_set_error_message</code> (krb5_context context, krb5_error_code ret, const char *fmt,&#8230;) <code>__attribute__</code>((format(printf&quot; </p>
<p> KRB5_LIB_FUNCTION void<br />
 KRB5_LIB_CALL <code>krb5_vset_error_message</code> (krb5_context context, krb5_error_code ret, const char *fmt, va_list args) <code>__attribute__</code>((format(printf&quot; </p>
<p> KRB5_LIB_FUNCTION void<br />
 KRB5_LIB_CALL <code>krb5_prepend_error_message</code> (krb5_context context, krb5_error_code ret, const char *fmt,&#8230;) <code>__attribute__</code>((format(printf&quot; </p>
<p> KRB5_LIB_FUNCTION void<br />
 KRB5_LIB_CALL <code>krb5_vprepend_error_message</code> (krb5_context context, krb5_error_code ret, const char *fmt, va_list args) <code>__attribute__</code>((format(printf&quot; </p>
<p> KRB5_LIB_FUNCTION const char<br />
 *KRB5_LIB_CALL <code>krb5_get_error_message</code> (krb5_context context, krb5_error_code code)&quot; </p>
<p> KRB5_LIB_FUNCTION void<br />
 KRB5_LIB_CALL <code>krb5_free_error_message</code> (krb5_context context, const char *msg)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_abort</code> (krb5_context, krb5_error_code, const char *,&#8230;) <code>__attribute__</code>((noreturn&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_abortx</code> (krb5_context, const char *,&#8230;) <code>__attribute__</code>((noreturn&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_err</code> (krb5_context, int, krb5_error_code, const char *,&#8230;) <code>__attribute__</code>((noreturn&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_errx</code> (krb5_context, int, const char *,&#8230;) <code>__attribute__</code>((noreturn&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_log_facility<br />
 *KRB5_LIB_CALL <code>krb5_get_warn_dest</code> (krb5_context)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_set_warn_dest</code> (krb5_context, krb5_log_facility *)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_vabort</code> (krb5_context, krb5_error_code, const char *, va_list) <code>__attribute__</code>((noreturn&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_verr</code> (krb5_context, int, krb5_error_code, const char *, va_list) <code>__attribute__</code>((noreturn&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_verrx</code> (krb5_context, int, const char *, va_list) <code>__attribute__</code>((noreturn&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_vwarn</code> (krb5_context, krb5_error_code, const char *, va_list) <code>__attribute__</code>((format(printf&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL<br />
 KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_vwarnx</code> (krb5_context, const char *, va_list) <code>__attribute__</code>((format(printf&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL<br />
 KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL<br />
 KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_warn</code> (krb5_context, krb5_error_code, const char *,&#8230;) <code>__attribute__</code>((format(printf&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL<br />
 KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL<br />
 KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL<br />
 KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_warnx</code> (krb5_context, const char *,&#8230;) <code>__attribute__</code>((format(printf&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL<br />
 KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>__attribute__</code> ((format(printf, 3, 4)))&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>__attribute__</code> ((format(printf, 2, 0)))&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>__attribute__</code> ((format(printf, 2, 3)))&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>__attribute__</code> ((noreturn, format(printf, 3, 0)))&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>__attribute__</code> ((noreturn, format(printf, 3, 4)))&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>__attribute__</code> ((noreturn, format(printf, 2, 3)))&quot; </p>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL __attribute__ ((format(printf, 3, 4)))</h3>
<p> Log a warning to the log, default stderr, include the error from the last failure. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context.<br />
 <i>code</i> error code of the last error<br />
 <i>fmt</i> message to print</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL __attribute__ ((format(printf, 2, 0)))</h3>
<p> Log a warning to the log, default stderr. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context.<br />
 <i>fmt</i> message to print<br />
 <i>ap</i> arguments</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL __attribute__ ((format(printf, 2, 3)))</h3>
<p> Log a warning to the log, default stderr. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context.<br />
 <i>fmt</i> message to print</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL __attribute__ ((noreturn, format(printf, 3, 0)))</h3>
<p> Log a warning to the log, default stderr, and then exit. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context<br />
 <i>eval</i> the exit code to exit with<br />
 <i>fmt</i> message to print<br />
 <i>ap</i> arguments</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL __attribute__ ((noreturn, format(printf, 3, 4)))</h3>
<p> Log a warning to the log, default stderr, and then exit. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context<br />
 <i>eval</i> the exit code to exit with<br />
 <i>fmt</i> message to print</dl>
<p> Log a warning to the log, default stderr, include the error from the last failure and then abort. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context<br />
 <i>code</i> error code of the last error<br />
 <i>fmt</i> message to print</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL __attribute__ ((noreturn, format(printf, 2, 3)))</h3>
<p> Log a warning to the log, default stderr, and then abort. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context<br />
 <i>code</i> error code of the last error<br />
 <i>fmt</i> message to print</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_abort (krb5_context, krb5_error_code, const char *, &#8230;)</h3>
<p> Log a warning to the log, default stderr, include the error from the last failure and then abort. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context<br />
 <i>code</i> error code of the last error<br />
 <i>fmt</i> message to print</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_abortx (krb5_context, const char *, &#8230;)</h3>
<p> Log a warning to the log, default stderr, and then abort. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context<br />
 <i>code</i> error code of the last error<br />
 <i>fmt</i> message to print</dl>
<h3>KRB5_LIB_FUNCTION void KRB5_LIB_CALL krb5_clear_error_message (krb5_contextcontext)</h3>
<p> Clears the error message from the Kerberos 5 context. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> The Kerberos 5 context to clear</dl>
<h3>KRB5_LIB_FUNCTION char *KRB5_LIB_CALL KRB5_DEPRECATED_FUNCTION (&#8216;Use <code>krb5_get_error_message</code> instead&#8217;)</h3>
<p> Return the error message in context. On error or no error string, the function returns NULL. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> an error string, needs to be freed with <code>krb5_free_error_message()</code>. The functions return NULL on error.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_eai_to_heim_errno (inteai_errno, intsystem_error)</h3>
<p> Convert the getaddrinfo() error code to a Kerberos et error code. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>eai_errno</i> contains the error code from getaddrinfo().<br />
 <i>system_error</i> should have the value of errno after the failed getaddrinfo().</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Kerberos error code representing the EAI errors.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_err (krb5_contextcontext, inteval, krb5_error_codecode, const char *fmt, &#8230;)</h3>
<p> Log a warning to the log, default stderr, include bthe error from the last failure and then exit. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context<br />
 <i>eval</i> the exit code to exit with<br />
 <i>code</i> error code of the last error<br />
 <i>fmt</i> message to print</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_errx (krb5_context, int, const char *, &#8230;)</h3>
<p> Log a warning to the log, default stderr, and then exit. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context<br />
 <i>eval</i> the exit code to exit with<br />
 <i>fmt</i> message to print</dl>
<h3>KRB5_LIB_FUNCTION void KRB5_LIB_CALL krb5_free_error_message (krb5_contextcontext, const char *msg)</h3>
<p> Free the error message returned by <code>krb5_get_error_message()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos context<br />
 <i>msg</i> error message to free, returned byg <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION const char *KRB5_LIB_CALL krb5_get_error_message (krb5_contextcontext, krb5_error_codecode)</h3>
<p> Return the error message for `code&#8217; in context. On memory allocation error the function returns NULL. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context<br />
 <i>code</i> Error code related to the error</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> an error string, needs to be freed with <code>krb5_free_error_message()</code>. The functions return NULL on error.</dl>
<h3>KRB5_LIB_FUNCTION krb5_log_facility *KRB5_LIB_CALL krb5_get_warn_dest (krb5_contextcontext)</h3>
<p> Get the default logging facility. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_h_errno_to_heim_errno (inteai_errno)</h3>
<p> Convert the gethostname() error code (h_error) to a Kerberos et error code. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>eai_errno</i> contains the error code from gethostname().</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Kerberos error code representing the gethostname errors.</dl>
<h3>KRB5_LIB_FUNCTION void KRB5_LIB_CALL krb5_prepend_error_message (krb5_contextcontext, krb5_error_coderet, const char *fmt, &#8230;)</h3>
<p> Prepend the context full error string for a specific error code. The error that is stored should be internationalized. </p>
<p> The if context is NULL, no error string is stored. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context<br />
 <i>ret</i> The error code<br />
 <i>fmt</i> Error string for the error code<br />
 <i>&#8230;</i> <a href="/docs/linux/man/3-printf/">printf</a>(3) style parameters.</dl>
<h3>KRB5_LIB_FUNCTION void KRB5_LIB_CALL krb5_set_error_message (krb5_contextcontext, krb5_error_coderet, const char *fmt, &#8230;)</h3>
<p> Set the context full error string for a specific error code. The error that is stored should be internationalized. </p>
<p> The if context is NULL, no error string is stored. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context<br />
 <i>ret</i> The error code<br />
 <i>fmt</i> Error string for the error code<br />
 <i>&#8230;</i> <a href="/docs/linux/man/3-printf/">printf</a>(3) style parameters.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_set_warn_dest (krb5_contextcontext, krb5_log_facility *fac)</h3>
<p> Set the default logging facility. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context<br />
 <i>fac</i> Facility to use for logging.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_vabort (krb5_contextcontext, krb5_error_codecode, const char *fmt, va_listap)</h3>
<p> Log a warning to the log, default stderr, include bthe error from the last failure and then abort. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context<br />
 <i>code</i> error code of the last error<br />
 <i>fmt</i> message to print<br />
 <i>ap</i> arguments</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_verr (krb5_contextcontext, inteval, krb5_error_codecode, const char *fmt, va_listap)</h3>
<p> Log a warning to the log, default stderr, include bthe error from the last failure and then exit. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context<br />
 <i>eval</i> the exit code to exit with<br />
 <i>code</i> error code of the last error<br />
 <i>fmt</i> message to print<br />
 <i>ap</i> arguments</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_verrx (krb5_context, int, const char *, va_list)</h3>
<p> Log a warning to the log, default stderr, and then exit. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context<br />
 <i>eval</i> the exit code to exit with<br />
 <i>fmt</i> message to print<br />
 <i>ap</i> arguments</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL KRB5_LIB_FUNCTION void KRB5_LIB_CALL krb5_vprepend_error_message (krb5_contextcontext, krb5_error_coderet, const char *fmt, va_listargs)</h3>
<p> Prepend the contexts&#8217;s full error string for a specific error code. </p>
<p> The if context is NULL, no error string is stored. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context<br />
 <i>ret</i> The error code<br />
 <i>fmt</i> Error string for the error code<br />
 <i>args</i> <a href="/docs/linux/man/3-printf/">printf</a>(3) style parameters.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL KRB5_LIB_FUNCTION void KRB5_LIB_CALL KRB5_LIB_FUNCTION void KRB5_LIB_CALL krb5_vset_error_message (krb5_contextcontext, krb5_error_coderet, const char *fmt, va_listargs)</h3>
<p> Set the context full error string for a specific error code. </p>
<p> The if context is NULL, no error string is stored. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context<br />
 <i>ret</i> The error code<br />
 <i>fmt</i> Error string for the error code<br />
 <i>args</i> <a href="/docs/linux/man/3-printf/">printf</a>(3) style parameters.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_vwarn (krb5_contextcontext, krb5_error_codecode, const char *fmt, va_listap)</h3>
<p> Log a warning to the log, default stderr, include the error from the last failure. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context.<br />
 <i>code</i> error code of the last error<br />
 <i>fmt</i> message to print<br />
 <i>ap</i> arguments</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_vwarnx (krb5_context, const char *, va_list)</h3>
<p> Log a warning to the log, default stderr. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context.<br />
 <i>fmt</i> message to print<br />
 <i>ap</i> arguments</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_warn (krb5_context, krb5_error_code, const char *, &#8230;)</h3>
<p> Log a warning to the log, default stderr, include the error from the last failure. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context.<br />
 <i>code</i> error code of the last error<br />
 <i>fmt</i> message to print</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_warnx (krb5_context, const char *, &#8230;)</h3>
<p> Log a warning to the log, default stderr. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context.<br />
 <i>fmt</i> message to print</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for HeimdalKerberos5library from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbBI">Author</a></p>
<dd></dl>
