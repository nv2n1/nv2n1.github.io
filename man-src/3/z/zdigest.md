---
title: "zdigest(3)"
name: "zdigest"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zdigest/"
description: "zdigest – provides hashing functions (SHA-1 at present)"
---

<p>zdigest &#8211; provides hashing functions (SHA-1 at present)</p>
<h2>Synopsis</h2>
<pre>// Constructor - creates new digest object, which you use to build up a
// digest by repeatedly calling zdigest_update() on chunks of data.
CZMQ_EXPORT zdigest_t *
 zdigest_new (void);
// Destroy a digest object
CZMQ_EXPORT void
 zdigest_destroy (zdigest_t **self_p);
// Add buffer into digest calculation
CZMQ_EXPORT void
 zdigest_update (zdigest_t *self, byte *buffer, size_t length);
// Return final digest hash data. If built without crypto support, returns
// NULL.
CZMQ_EXPORT byte *
 zdigest_data (zdigest_t *self);
// Return final digest hash size
CZMQ_EXPORT size_t
 zdigest_size (zdigest_t *self);
// Return digest as printable hex string; caller should not modify nor
// free this string. After calling this, you may not use zdigest_update()
// on the same digest. If built without crypto support, returns NULL.
CZMQ_EXPORT char *
 zdigest_string (zdigest_t *self);
// Self test of this class
CZMQ_EXPORT void
 zdigest_test (bool verbose);</pre>
<h2>Description</h2>
<p>The zdigest class generates a hash from zchunks of data. The current algorithm is SHA-1, chosen for speed. We are aiming to generate a unique digest for a file, and there are no security issues in this use case. </p>
<p> The current code depends on OpenSSL, which might be replaced by hard coded SHA-1 implementation to reduce build dependencies.</p>
<h2>Example</h2>
<p><code>From zdigest_test method</code>. </p>
<pre><code>byte *buffer = (byte *) zmalloc (1024);
memset (buffer, 0xAA, 1024);

zdigest_t *digest = zdigest_new ();
assert (digest);
zdigest_update (digest, buffer, 1024);
byte *data = zdigest_data (digest);
assert (data [0] == 0xDE);
assert (data [1] == 0xB2);
assert (data [2] == 0x38);
assert (data [3] == 0x07);
assert (streq (zdigest_string (digest),
&quot;DEB23807D4FE025E900FE9A9C7D8410C3DDE9671&quot;));
zdigest_destroy (&amp;digest);
free (buffer);
</code></pre>
<h2>Authors</h2>
<p>The czmq manual was written by the authors in the AUTHORS file.</p>
<h2>Resources</h2>
<p>Main web site: m[blue]m[] </p>
<p> Report bugs to the email &lt;m[blue]<code>zeromq-dev [at] lists.zeromq.org</code>m[]<font SIZE="-2">[1]</font>&gt;</p>
<h2>Copyright</h2>
<p>Copyright (c) 1991-2012 iMatix Corporation &#8212; <a rel="nofollow" href="http://www.imatix.com">http://www.imatix.com</a> Copyright other contributors as noted in the AUTHORS file. This file is part of CZMQ, the high-level C binding for 0MQ: <a href="http://czmq.zeromq.org">http://czmq.zeromq.org</a> This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at <a href="http://mozilla.org/MPL/2.0/.">http://mozilla.org/MPL/2.0/.</a> LICENSE included with the czmq distribution.</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>zeromq-dev [at] lists.zeromq.org</p>
<dl>
<dd>mailto:zeromq-dev [at] lists.zeromq.org</dl>
