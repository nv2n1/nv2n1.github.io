---
title: "sasl_errstring(3)"
name: "sasl_errstring"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sasl_errstring/"
description: "sasl_errstring – Translate a SASL return code to a human-readable form"
---

<p>sasl_errstring &#8211; Translate a SASL return code to a human-readable form </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sasl/sasl.h&gt;

const char *sasl_errstring(int saslerr,
                           const char *langlist,
                           const char **outlang);</code></pre>
<h2>Description</h2>
<p><code>sasl_usererr</code> is called to convert a SASL return code (an integer) into a human readable string. At this time the only language available is american english written by programmers (aka gobbledygook). Note that a server should call sasl_usererr on a return code first if the string is going to be sent to the client. <i>saslerr</i> specifies the error number to convert. <i>langlist</i> is currently unused; Use NULL. <i>outlang</i> specifies the desired RFC 1766 language for output. NULL defaults to &quot;en-us,&quot; currently the only supported language. It should be noted that this function is not the recommended means of extracting error code information from SASL, instead application should use <a href="/docs/linux/man/3-sasl_errdetail/">sasl_errdetail</a>(3), which contains this information (and more) </p>
<h2>Return Value</h2>
<p>Returns the string. If langlist is NULL, US-ASCII is used. </p>
<h2>Conforming To</h2>
<p>RFC 4422</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-sasl/">sasl</a>(3), <a href="/docs/linux/man/3-sasl_errdetail/">sasl_errdetail</a>(3), <a href="/docs/linux/man/3-sasl_errors/">sasl_errors</a>(3) </p>
