---
title: "remctl_set_ccache(3)"
name: "remctl_set_ccache"
section: "3"
letter: "r"
url: "/docs/linux/man/3-remctl_set_ccache/"
---

remctl_set_ccache - Set credential cache for remctl client connections

<h2>Synopsis</h2>

<pre><code>#include &lt;remctl.h&gt;
int remctl_set_ccache(struct remctl *r, const char *ccache);</code></pre>

<h2>Description</h2>

<i>remctl_set_ccache()</i> tells the the remctl client library to use <i>ccache</i> as the credential cache for authentication to a remctl server. It will affect any subsequent <i>remctl_open()</i> calls on the same struct remctl object (and may have broader effects; see <font SIZE="-1">WARNINGS</font> below). <i>ccache</i> is normally a path to a file in the file system that holds Kerberos credentials, but may take other values depending on the underlying Kerberos implementation used by GSS-API. 

 Calling this function will normally override any <font SIZE="-1">KRB5CCNAME</font> environment setting. If the caller wishes to honor that setting, it should either not call this function or check whether that environment variable is set first.

<h2>Return Value</h2>

<i>remctl_set_ccache()</i> returns true on success and false on failure. On failure, the caller should call <i>remctl_error()</i> to retrieve the error message. 

 This function will always return failure if the underlying GSS-API implementation against which the remctl client library was compiled does not support setting the Kerberos credential cache. The caller should be prepared for that. Falling back on setting the <font SIZE="-1">KRB5CCNAME</font> environment variable is often a reasonable choice.

<h2>Examples</h2>

Here's an example of attempting to use this function to set a ticket cache location and falling back on setting <font SIZE="-1">KRB5CCNAME</font> in the environment if this function is not supported. <pre><code>struct remctl r;

r = remctl_new();
if (r != NULL)
    if (!remctl_set_ccache(r, &quot;/tmp/krb5cc_example&quot;))
        putenv(&quot;KRB5CCNAME=/tmp/krb5cc_example&quot;);</code></pre> This assumes that any failure is due to lack of support from the underlying library rather than some other cause.

<h2>Compatibility</h2>

This interface was added in version 3.0, but that version would always change the ticket cache used by all GSS-API calls in the same process. Support for the <i>gss_krb5_import_cred()</i> method of isolating the changed ticket cache to only this remctl client object was added in version 3.5.

<h2>Warnings</h2>

The effect of this function is only localized to this specific remctl client context if the remctl client library was built against a Kerberos as well as GSS-API library and the GSS-API library supported <i>gss_krb5_import_cred()</i>. Otherwise, it falls back to calling <i>gss_krb5_ccache_name()</i>, which sets the credential cache used by the underlying GSS-API library for every GSS-API operation in the current execution context (process or thread), not just for this remctl object or even just for remctl operations. This function may therefore change global execution state and may affect other GSS-API operations done elsewhere in the same process.

<h2>Author</h2>

Russ Allbery &lt;eagle [at] eyrie.org&gt;

<h2>Copyright And License</h2>

Copyright 2011, 2013, 2014 The Board of Trustees of the Leland Stanford Junior University 

 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved. This file is offered as-is, without any warranty.

<h2>See Also</h2>

<i><a HREF="/docs/linux/man/3-remctl_new/">remctl_new</a></i>(3), <i><a HREF="/docs/linux/man/3-remctl_open/">remctl_open</a></i>(3), <i><a HREF="/docs/linux/man/3-remctl_error/">remctl_error</a></i>(3) The current version of the remctl library and complete details of the remctl protocol are available from its web page at &lt;<a rel="nofollow" HREF="http://www.eyrie.org/~eagle/software/remctl/">http://www.eyrie.org/~eagle/software/remctl/</a>&gt;. 
