---
title: "sasl_verifyfile_t(3)"
name: "sasl_verifyfile_t"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sasl_verifyfile_t/"
description: "sasl_verifyfile_t – The SASL file verification"
---

<p>sasl_verifyfile_t &#8211; The SASL file verification </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sasl/sasl.h&gt;

typedef enum {
    SASL_VRFY_PLUGIN, /* a DLL/shared library plugin */
    SASL_VRFY_CONF,   /* a configuration file */
    SASL_VRFY_PASSWD, /* a password storage file */
    SASL_VRFY_OTHER   /* some other file type */
} sasl_verify_type_t

    int
    sasl_verifyfile_t(void *context,
                      const char *file,
                      sasl_verify_type_t type)</code></pre>
<h2>Description</h2>
<p><code>sasl_verifyfile_t</code> is used to check whether a given file is okay for use by the SASL library. this is intended to allow applications to sanity check the environment to ensure that plugins or the config file cannot be written to, etc. <i>context</i> context from the callback record <i>file</i> full path of the file to verify <i>type</i> type of the file. </p>
<h2>Return Value</h2>
<p>SASL callback functions should return SASL return codes. See sasl.h for a complete list. SASL_OK indicates success. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-sasl/">sasl</a>(3), <a href="/docs/linux/man/3-sasl_callbacks/">sasl_callbacks</a>(3) </p>
