---
title: "munge_ctx(3)"
name: "munge_ctx"
section: "3"
letter: "m"
url: "/docs/linux/man/3-munge_ctx/"
description: "munge_ctx_create, munge_ctx_copy, munge_ctx_destroy, munge_ctx_strerror, munge_ctx_get, munge_ctx_set – MUNGE context functions"
---

<p>munge_ctx_create, munge_ctx_copy, munge_ctx_destroy, munge_ctx_strerror, munge_ctx_get, munge_ctx_set &#8211; MUNGE context functions</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;munge.h&gt;</code>
<code>munge_ctx_t munge_ctx_create (void);</code>
<code>munge_ctx_t munge_ctx_copy (munge_ctx_t </code><i>ctx</i><code>);</code>
<code>void munge_ctx_destroy (munge_ctx_t </code><i>ctx</i><code>);</code>
<code>const char * munge_ctx_strerror (munge_ctx_t </code><i>ctx</i><code>);</code>
<code>munge_err_t munge_ctx_get (munge_ctx_t </code><i>ctx</i><code>, munge_opt_t </code><i>opt</i><code>, ...);</code>
<code>munge_err_t munge_ctx_set (munge_ctx_t </code><i>ctx</i><code>, munge_opt_t </code><i>opt</i><code>, ...);</code>
<code>cc `pkg-config --cflags --libs munge` -o foo foo.c</code></pre>
<h2>Description</h2>
<p>The <code>munge_ctx_create</code>() function creates and returns a new MUNGE context, or NULL on error. </p>
<p> The <code>munge_ctx_copy</code>() function copies the context <i>ctx</i> and returns a new MUNGE context, or NULL on error. </p>
<p> The <code>munge_ctx_destroy</code>() function destroys the context <i>ctx</i>. </p>
<p> The <code>munge_ctx_strerror</code>() function returns a descriptive text string describing the MUNGE error number according to the context <i>ctx</i>, or NULL if no error condition exists. This may provide a more detailed error message than that returned by <code>munge_strerror</code>(). </p>
<p> The <code>munge_ctx_get</code>() function gets the value for the option <i>opt</i> associated with the MUNGE context <i>ctx</i>, storing the result in the subsequent pointer argument. If the result is a string, that string should not be freed or modified by the caller. </p>
<p> The <code>munge_ctx_set</code>() function sets the value for the option <i>opt</i> associated with the MUNGE context <i>ctx</i>, using the value of the subsequent argument. </p>
<h2>Return Value</h2>
<p>The <code>munge_ctx_create</code>() and <code>munge_ctx_copy</code>() functions return a newly allocated MUNGE context, or NULL on error. </p>
<p> The <code>munge_ctx_strerror</code>() function returns a pointer to a NUL-terminated constant text string, or NULL if no error condition exists. This string should not be freed or modified by the caller. </p>
<p> The <code>munge_ctx_get</code>() and <code>munge_ctx_set</code>() functions return <code>EMUNGE_SUCCESS</code> on success, or a MUNGE error number otherwise. </p>
<h2>Context Options</h2>
<p>The following context options can be queried via <code>munge_ctx_get</code>() or specified via <code>munge_ctx_set</code>(). The type following each enumeration is the variable type used for the subsequent argument in <code>munge_ctx_set</code>(), or the variable type of a pointer used for the subsequent argument in <code>munge_ctx_get</code>().</p>
<dl COMPACT>
<dt><code>MUNGE_OPT_CIPHER_TYPE</code> , <i>int</i></p>
<dd>Get or set the cipher type (cf., <code>CIPHER TYPES</code>).</p>
<dt><code>MUNGE_OPT_MAC_TYPE</code> , <i>int</i></p>
<dd>Get or set the MAC type (cf., <code>MAC TYPES</code>).</p>
<dt><code>MUNGE_OPT_ZIP_TYPE</code> , <i>int</i></p>
<dd>Get or set the compression type (cf., <code>COMPRESSION TYPES</code>).</p>
<dt><code>MUNGE_OPT_REALM</code> , <i>char *</i></p>
<dd>Get or set the security realm, where the <i>char *</i> type is a NUL-terminated character string. The string returned by <code>munge_ctx_get</code>() should not be freed or modified by the caller. <code>NOT CURRENTLY SUPPORTED</code>.</p>
<dt><code>MUNGE_OPT_TTL</code> , <i>int</i></p>
<dd>Get or set the time-to-live (in seconds) (cf., <code>TTL TYPES</code>). This value controls how long the credential is valid once it has been encoded.</p>
<dt><code>MUNGE_OPT_ADDR4</code> , <i>struct in_addr</i></p>
<dd>Get the IPv4 address of the host where the credential was encoded. This option cannot be explicitly set.</p>
<dt><code>MUNGE_OPT_ENCODE_TIME</code> , <i>time_t</i></p>
<dd>Get the time (in seconds since the epoch) at which the credential was encoded. This option cannot be explicitly set.</p>
<dt><code>MUNGE_OPT_DECODE_TIME</code> , <i>time_t</i></p>
<dd>Get the time (in seconds since the epoch) at which the credential was decoded. This option cannot be explicitly set.</p>
<dt><code>MUNGE_OPT_SOCKET</code> , <i>char *</i></p>
<dd>Get or set the local domain socket for connecting with <code>munged</code>, where the <i>char *</i> type is a NUL-terminated character string. The string returned by <code>munge_ctx_get</code>() should not be freed or modified by the caller.</p>
<dt><code>MUNGE_OPT_UID_RESTRICTION</code> , <i>uid_t</i></p>
<dd>Get or set the UID allowed to decode the credential (cf., <code>UID &amp; GID TYPES</code>). This value will be matched against the effective user ID of the process requesting the credential decode.</p>
<dt><code>MUNGE_OPT_GID_RESTRICTION</code> , <i>gid_t</i></p>
<dd>Get or set the GID allowed to decode the credential (cf., <code>UID &amp; GID TYPES</code>). This value will be matched against the effective group ID of the process requesting the credential decode, as well as each supplementary group of which the effective user ID of that process is a member. </p>
</dl>
<h2>Cipher Types</h2>
<p>Credentials can be encrypted using the secret key shared by all <code>munged</code> daemons within a security realm. Anyone having access to this key can use it to decrypt a credential, thereby bypassing any restrictions being imposed by <code>munged</code>.</p>
<dl COMPACT>
<dt><code>MUNGE_CIPHER_NONE</code></p>
<dd>Specify that encryption is to be disabled.</p>
<dt><code>MUNGE_CIPHER_DEFAULT</code></p>
<dd>Specify the default according to the <code>munged</code> configuration.</p>
<dt><code>MUNGE_CIPHER_BLOWFISH</code></p>
<dd>Specify the Blowfish cipher designed by Bruce Schneier. This cipher has a 64-bit block-size and a variable key length. MUNGE uses it with a 128-bit key in CBC mode. It is a fast block cipher but suffers from a slow key setup time. Consequently, it underperforms when generating small credentials.</p>
<dt><code>MUNGE_CIPHER_CAST5</code></p>
<dd>Specify the CAST5 cipher designed by Carlisle Adams and Stafford Tavares. This cipher has a 64-bit block-size and a variable key length. MUNGE uses it with a 128-bit key in CBC mode.</p>
<dt><code>MUNGE_CIPHER_AES128</code></p>
<dd>Specify the AES (Advanced Encryption Standard) cipher, also known as Rijndael. It was designed by Joan Daemen and Vincent Rijmen. This cipher has a 128-bit block-size and a key length of 128, 192, or 256 bits. MUNGE uses it here with a 128-bit key in CBC mode.</p>
<dt><code>MUNGE_CIPHER_AES256</code></p>
<dd>Specify the AES (Advanced Encryption Standard) cipher, also known as Rijndael. It was designed by Joan Daemen and Vincent Rijmen. This cipher has a 128-bit block-size and a key length of 128, 192, or 256 bits. MUNGE uses it here with a 256-bit key in CBC mode. Currently, <code>MUNGE_CIPHER_AES256</code> requires the use of <code>MUNGE_MAC_SHA256</code>. </p>
</dl>
<h2>Mac Types</h2>
<p>The message authentication code (MAC) is a required component of the credential; consequently, it cannot be disabled.</p>
<dl COMPACT>
<dt><code>MUNGE_MAC_DEFAULT</code></p>
<dd>Specify the default according to the <code>munged</code> configuration.</p>
<dt><code>MUNGE_MAC_MD5</code></p>
<dd>Specify the MD5 algorithm designed by Ron Rivest and published in 1991. This algorithm has a 128-bit message digest. In 2004, a successful collision attack against MD5 was demonstrated. In 2009, a theoretical pre-image attack against MD5 was published. Consequently, use of MD5 is not recommended due to its lower security margin.</p>
<dt><code>MUNGE_MAC_SHA1</code></p>
<dd>Specify the SHA-1 algorithm designed by the National Security Agency and published in 1995; this is the successor to the original Secure Hash Algorithm (now called SHA-0) published in 1993. This algorithm has a 160-bit message digest. In 2005, successful collision attacks were demonstrated against SHA-1. But since a pre-image attack has not yet been demonstrated, SHA-1 should still be safe to use within MUNGE.</p>
<dt><code>MUNGE_MAC_RIPEMD160</code></p>
<dd>Specify the RIPEMD-160 (RACE Integrity Primitives Evaluation Message Digest) algorithm designed in Europe by Hans Dobbertin, Antoon Bosselaers, and Bart Preneel, and published in 1996. This algorithm has a 160-bit message digest. It is somewhat less popular than SHA-1 and correspondingly less well studied. While slower than SHA-1, it is believed to have a slightly better security margin.</p>
<dt><code>MUNGE_MAC_SHA256</code></p>
<dd>Specify the SHA-256 algorithm designed by the National Security Agency and published in 2002; this is one of the SHA-2 variants in the Secure Hash Algorithm family. This algorithm has a 256-bit message digest. In 2006, NIST began encouraging the use of the SHA-2 family of hash functions for all new applications and protocols.</p>
<dt><code>MUNGE_MAC_SHA512</code></p>
<dd>Specify the SHA-512 algorithm designed by the National Security Agency and published in 2002; this is one of the SHA-2 variants in the Secure Hash Algorithm family. This algorithm has a 512-bit message digest. In 2006, NIST began encouraging the use of the SHA-2 family of hash functions for all new applications and protocols. </p>
</dl>
<h2>Compression Types</h2>
<p>If a compression type is specified, a payload-bearing credential will be compressed accordingly. However, if the resulting compressed data is larger than the original uncompressed data, the uncompressed data will be restored and compression will be disabled for that credential.</p>
<dl COMPACT>
<dt><code>MUNGE_ZIP_NONE</code></p>
<dd>Specify that compression is to be disabled. This is the recommended setting unless there is a payload of sufficient size to compress.</p>
<dt><code>MUNGE_ZIP_DEFAULT</code></p>
<dd>Specify the default according to the <code>munged</code> configuration.</p>
<dt><code>MUNGE_ZIP_BZLIB</code></p>
<dd>Specify the bzip2 library developed by Julian Seward. This is slower and uses more memory, but generally gets better compression on larger payloads.</p>
<dt><code>MUNGE_ZIP_ZLIB</code></p>
<dd>Specify the zlib library developed by Jean-loup Gailly and Mark Adler. This is faster and uses less memory, but gets pretty good compression nonetheless. </p>
</dl>
<h2>Ttl Types</h2>
<p>The time-to-live value specifies the number of seconds after the encode-time that the credential is considered valid. In addition to specifying an integer value, the following types are available.</p>
<dl COMPACT>
<dt><code>MUNGE_TTL_MAXIMUM</code></p>
<dd>Specify the maximum allowed by the <code>munged</code> configuration.</p>
<dt><code>MUNGE_TTL_DEFAULT</code></p>
<dd>Specify the default according to the <code>munged</code> configuration. </p>
</dl>
<h2>UID &amp; GID TYPES</h2>
<p>The UID and GID restrictions can be used to restrict the decoding of the credential based on the effective user and group ID of the requesting process. In addition to specifying an integer value, the following types are available.</p>
<dl COMPACT>
<dt><code>MUNGE_UID_ANY</code></p>
<dd>Specify that no UID restriction is to take effect; this is the default behavior.</p>
<dt><code>MUNGE_GID_ANY</code></p>
<dd>Specify that no GID restriction is to take effect; this is the default behavior. </p>
</dl>
<h2>Errors</h2>
<p>Refer to <code><a href="/docs/linux/man/3-munge/">munge</a></code>(3) for a complete list of errors. </p>
<h2>Example</h2>
<p>The following example program illustrates the use of the MUNGE context to query the location of the <code>munged</code> domain socket. </p>
<pre>#include &lt;stdio.h&gt; /* for printf() */
#include &lt;stdlib.h&gt; /* for exit() */
#include &lt;munge.h&gt;
int
main (int argc, char *argv[])
{
 munge_ctx_t ctx;
 munge_err_t err;
 char *str;
 if (!(ctx = munge_ctx_create ())) {
 fprintf (stderr, &quot;ERROR: Unable to create MUNGE context
&quot;);
 exit (1);
 }
 err = munge_ctx_get (ctx, MUNGE_OPT_SOCKET, &amp;str);
 if (err != EMUNGE_SUCCESS) {
 fprintf (stderr, &quot;ERROR: %s
&quot;, munge_ctx_strerror (ctx));
 exit (1);
 }
 printf (&quot;socket=%s
&quot;, str);
 /*
 * Note that 'str' is not to be free()d since
 * it points to a string within the 'ctx'.
 */
 munge_ctx_destroy (ctx);
 exit (0);
}</pre>
<h2>Notes</h2>
<p>Abandoning a new or copied MUNGE context without destroying it will result in a memory leak. </p>
<p> The context passed to <code>munge_encode</code>() is treated read-only except for the error message that is set when an error is returned. The context passed to <code>munge_decode</code>() is set according to the context used to encode the credential; however, on error, its settings may be in a state which is invalid for encoding. Consequently, separate contexts should be used for encoding and decoding. </p>
<p> A context should not be shared between threads unless it is protected by a mutex; however, a better alternative is to use a separate context (or two) for each thread, either by creating a new one via <code>munge_ctx_create</code>() or copying an existing one via <code>munge_ctx_copy</code>(). </p>
<h2>Author</h2>
<p>Chris Dunlap &lt;cdunlap [at] llnl.gov&gt; </p>
<h2>Copyright</h2>
<p>Copyright (C) 2007-2013 Lawrence Livermore National Security, LLC.<br />
 Copyright (C) 2002-2007 The Regents of the University of California. </p>
<p> MUNGE is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. </p>
<p> Additionally for the MUNGE library (libmunge), you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-munge/">munge</a></code>(1), <code><a href="/docs/linux/man/1-remunge/">remunge</a></code>(1), <code><a href="/docs/linux/man/1-unmunge/">unmunge</a></code>(1), <code><a href="/docs/linux/man/3-munge/">munge</a></code>(3), <code><a href="/docs/linux/man/3-munge_enum/">munge_enum</a></code>(3), <code><a href="/docs/linux/man/7-munge/">munge</a></code>(7), <code><a href="/docs/linux/man/8-munged/">munged</a></code>(8). </p>
<p> <code><a rel="nofollow" href="https://munge.googlecode.com/">https://munge.googlecode.com/</a></code></p>
