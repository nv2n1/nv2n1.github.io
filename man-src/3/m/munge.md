---
title: "munge(3)"
name: "munge"
section: "3"
letter: "m"
url: "/docs/linux/man/3-munge/"
description: "munge_encode, munge_decode, munge_strerror – MUNGE core functions"
---

<p>munge_encode, munge_decode, munge_strerror &#8211; MUNGE core functions</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;munge.h&gt;</code>
<code>munge_err_t munge_encode (char **</code><i>cred</i><code>, munge_ctx_t </code><i>ctx</i><code>,</code>
<code> const void *</code><i>buf</i><code>, int </code><i>len</i><code>);</code>
<code>munge_err_t munge_decode (const char *</code><i>cred</i><code>, munge_ctx_t </code><i>ctx</i><code>,</code>
<code> void **</code><i>buf</i><code>, int *</code><i>len</i><code>, uid_t *</code><i>uid</i><code>, gid_t *</code><i>gid</i><code>);</code>
<code>const char * munge_strerror (munge_err_t </code><i>e</i><code>);</code>
<code>cc `pkg-config --cflags --libs munge` -o foo foo.c</code></pre>
<h2>Description</h2>
<p>The <code>munge_encode</code>() function creates a credential contained in a NUL-terminated base64 string. A payload specified by a buffer <i>buf</i> of length <i>len</i> can be encapsulated in as well. If the MUNGE context <i>ctx</i> is NULL, the default context will be used. A pointer to the resulting credential is returned via <i>cred</i>; on error, it is set to NULL. The caller is responsible for freeing the memory referenced by <i>cred</i>. </p>
<p> The <code>munge_decode</code>() function validates the NUL-terminated credential <i>cred</i>. If the MUNGE context <i>ctx</i> is not NULL, it will be set to that used to encode the credential. If <i>buf</i> and <i>len</i> are not NULL, memory will be allocated for the encapsulated payload, <i>buf</i> will be set to point to this data, and <i>len</i> will be set to its length. An additional NUL character will be appended to this payload data but not included in its length. If no payload exists, <i>buf</i> will be set to NULL and <i>len</i> will be set to 0. For certain errors (i.e., <code>EMUNGE_CRED_EXPIRED</code>, <code>EMUNGE_CRED_REWOUND</code>, <code>EMUNGE_CRED_REPLAYED</code>), payload memory will still be allocated if necessary. The caller is responsible for freeing the memory referenced by <i>buf</i>. If <i>uid</i> or <i>gid</i> is not NULL, they will be set to the UID/GID of the process that created the credential. </p>
<p> The <code>munge_strerror</code>() function returns a descriptive text string describing the MUNGE error number <i>e</i>. </p>
<h2>Return Value</h2>
<p>The <code>munge_encode</code>() and <code>munge_decode</code>() functions return <code>EMUNGE_SUCCESS</code> on success, or a MUNGE error otherwise. If a MUNGE context was used, it may contain a more detailed error message accessible via <code>munge_ctx_strerror</code>(). </p>
<p> The <code>munge_strerror</code>() function returns a pointer to a NUL-terminated constant text string; this string should not be freed or modified by the caller. </p>
<h2>Errors</h2>
<dl COMPACT>
<dt><code>EMUNGE_SUCCESS</code></p>
<dd>Success.</p>
<dt><code>EMUNGE_SNAFU</code></p>
<dd>Internal error.</p>
<dt><code>EMUNGE_BAD_ARG</code></p>
<dd>Invalid argument.</p>
<dt><code>EMUNGE_BAD_LENGTH</code></p>
<dd>Exceeded the maximum message length as specified by the <code>munged</code> configuration.</p>
<dt><code>EMUNGE_OVERFLOW</code></p>
<dd>Exceeded the maximum length of a buffer.</p>
<dt><code>EMUNGE_NO_MEMORY</code></p>
<dd>Unable to allocate the requisite memory.</p>
<dt><code>EMUNGE_SOCKET</code></p>
<dd>Unable to communicate with the daemon on the domain socket.</p>
<dt><code>EMUNGE_BAD_CRED</code></p>
<dd>The credential does not match the specified format.</p>
<dt><code>EMUNGE_BAD_VERSION</code></p>
<dd>The credential contains an unsupported version number.</p>
<dt><code>EMUNGE_BAD_CIPHER</code></p>
<dd>The credential contains an unsupported cipher type.</p>
<dt><code>EMUNGE_BAD_MAC</code></p>
<dd>The credential contains an unsupported MAC type.</p>
<dt><code>EMUNGE_BAD_ZIP</code></p>
<dd>The credential contains an unsupported compression type.</p>
<dt><code>EMUNGE_BAD_REALM</code></p>
<dd>The credential contains an unrecognized security realm.</p>
<dt><code>EMUNGE_CRED_INVALID</code></p>
<dd>The credential is invalid. This means the credential could not be successfully decoded. More than likely, the secret keys on the encoding and decoding hosts do not match. Another possibility is that the credential has been altered since it was encoded.</p>
<dt><code>EMUNGE_CRED_EXPIRED</code></p>
<dd>The credential has expired. This means more than TTL seconds have elapsed since the credential was encoded. Another possibility is that the clocks on the encoding and decoding hosts are out of sync.</p>
<dt><code>EMUNGE_CRED_REWOUND</code></p>
<dd>The credential appears to have been encoded at some point in the future. This means the clock on the decoding host is slower than that of the encoding host by more than the allowable clock skew. More than likely, the clocks on the encoding and decoding hosts are out of sync.</p>
<dt><code>EMUNGE_CRED_REPLAYED</code></p>
<dd>The credential has been previously decoded on this host.</p>
<dt><code>EMUNGE_CRED_UNAUTHORIZED</code></p>
<dd>The client is not authorized to decode the credential based upon the effective user and/or group ID of the process. </p>
</dl>
<h2>Example</h2>
<p>The following example program illustrates the use of a MUNGE credential to ascertain the effective user and group ID of the encoding process. </p>
<pre>#include &lt;stdio.h&gt; /* for printf() */
#include &lt;stdlib.h&gt; /* for exit() &amp; free() */
#include &lt;unistd.h&gt; /* for uid_t &amp; gid_t */
#include &lt;munge.h&gt;
int
main (int argc, char *argv[])
{
 char *cred;
 munge_err_t err;
 uid_t uid;
 gid_t gid;
 err = munge_encode (&amp;cred, NULL, NULL, 0);
 if (err != EMUNGE_SUCCESS) {
 fprintf (stderr, &quot;ERROR: %s
&quot;, munge_strerror (err));
 exit (1);
 }
 err = munge_decode (cred, NULL, NULL, NULL, &amp;uid, &amp;gid);
 if (err != EMUNGE_SUCCESS) {
 fprintf (stderr, &quot;ERROR: %s
&quot;, munge_strerror (err));
 exit (1);
 }
 printf (&quot;uid=%d gid=%d
&quot;, uid, gid);
 free (cred);
 exit (0);
}</pre>
<h2>Notes</h2>
<p>Both <code>munge_encode</code>() and <code>munge_decode</code>() may allocate memory that the caller is responsible for freeing. Failure to do so will result in a memory leak. </p>
<h2>Author</h2>
<p>Chris Dunlap &lt;cdunlap [at] llnl.gov&gt; </p>
<h2>Copyright</h2>
<p>Copyright (C) 2007-2013 Lawrence Livermore National Security, LLC.<br />
 Copyright (C) 2002-2007 The Regents of the University of California. </p>
<p> MUNGE is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. </p>
<p> Additionally for the MUNGE library (libmunge), you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-munge/">munge</a></code>(1), <code><a href="/docs/linux/man/1-remunge/">remunge</a></code>(1), <code><a href="/docs/linux/man/1-unmunge/">unmunge</a></code>(1), <code><a href="/docs/linux/man/3-munge_ctx/">munge_ctx</a></code>(3), <code><a href="/docs/linux/man/3-munge_enum/">munge_enum</a></code>(3), <code><a href="/docs/linux/man/7-munge/">munge</a></code>(7), <code><a href="/docs/linux/man/8-munged/">munged</a></code>(8). </p>
<p> <code><a rel="nofollow" href="https://munge.googlecode.com/">https://munge.googlecode.com/</a></code></p>
