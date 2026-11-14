---
title: "libssh2_session_supported_algs(3)"
name: "libssh2_session_supported_algs"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_session_supported_algs/"
description: "libssh2_session_supported_algs – get list of supported algorithms"
---

<h2>NAME</h2>
<p> libssh2_session_supported_algs &#8211; get list of supported algorithms</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;libssh2.h&gt;
int libssh2_session_supported_algs(LIBSSH2_SESSION *session,
                                   int method_type,
                                   const char ***algs);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <i>session</i> &#8211; An instance of initialized LIBSSH2_SESSION (the function will use its pointer to the memory allocation function). <i>method_type</i> &#8211; Method type. See .BR <i><a href="/docs/linux/man/3-libssh2_session_method_pref/">libssh2_session_method_pref</a>(3)</i>. <i>algs</i> &#8211; Address of a pointer that will point to an array af returned algorithms </p>
<p> Get a list of supported algorithms for the given <i>method_type</i>. The method_type parameter is equivalent to method_type in <i><a href="/docs/linux/man/3-libssh2_session_method_pref/">libssh2_session_method_pref</a>(3)</i>. If successful, the function will allocate the appropriate amount of memory. When not needed anymore, it must be deallocated by calling <i><a href="/docs/linux/man/3-libssh2_free/">libssh2_free</a>(3)</i>. When this function is unsuccessful, this must not be done. </p>
<p> In order to get a list of all supported compression algorithms, libssh2_session_flag(session, LIBSSH2_FLAG_COMPRESS, 1) must be called before calling this function, otherwise only &quot;none&quot; will be returned. </p>
<p> If successful, the function will allocate and fill the array with supported algorithms (the same names as defined in RFC 4253). The array is not NULL terminated.</p>
<h2>EXAMPLE</h2>
<pre><code>
#include "libssh2.h"
const char **algorithms;
int rc, i;
LIBSSH2_SESSION *session;
/* initilize session */
session = libssh2_session_init();
rc = libssh2_session_supported_algs(session,
                                    LIBSSH2_METHOD_CRYPT_CS,
                                    &amp;algorithms);
if (rc &gt; 0) {
    /* the call succeeded, do sth. with the list of algorithms
       (e.g. list them)... */
    printf("Supported symmetric algorithms:);
    for ( i=0; i&lt;rc; i++ )
        printf("	%s, algorithms[i]);
    /* ... and free the allocated memory when not needed anymore */
    libssh2_free(session, algorithms);
} else {
    /* call failed, error handling */
}
</code></pre>
<h2>RETURN VALUE</h2>
<p> On success, a number of returned algorithms (i.e a positive number will be returned). In case of a failure, an error code (a negative number, see below) is returned. 0 should never be returned.</p>
<h2>ERRORS</h2>
<p> <i>LIBSSH2_ERROR_BAD_USE</i> &#8211; Invalid address of algs. </p>
<p> <i>LIBSSH2_ERROR_METHOD_NOT_SUPPORTED</i> &#8211; Unknown method type. </p>
<p> <i>LIBSSH2_ERROR_INVAL</i> &#8211; Internal error (normally should not occur). </p>
<p> <i>LIBSSH2_ERROR_ALLOC</i> &#8211; Allocation of memory failed.</p>
<h2>AVAILABILITY</h2>
<p> Added in 1.4.0</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_session_methods/">libssh2_session_methods</a>(3),</code> <code><a href="/docs/linux/man/3-libssh2_session_method_pref/">libssh2_session_method_pref</a>(3)</code> <code><a href="/docs/linux/man/3-libssh2_free/">libssh2_free</a>(3)</code> </p>
<h2>Index</h2>
