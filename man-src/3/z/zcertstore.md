---
title: "zcertstore(3)"
name: "zcertstore"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zcertstore/"
description: "zcertstore – work with CURVE security certificate stores"
---

<p>zcertstore &#8211; work with CURVE security certificate stores</p>
<h2>Synopsis</h2>
<pre>// Create a new certificate store from a disk directory, loading and
// indexing all certificates in that location. The directory itself may be
// absent, and created later, or modified at any time. The certificate store
// is automatically refreshed on any zcertstore_lookup() call. If the
// location is specified as NULL, creates a pure-memory store, which you
// can work with by inserting certificates at runtime.
CZMQ_EXPORT zcertstore_t *
 zcertstore_new (const char *location);
// Destroy a certificate store object in memory. Does not affect anything
// stored on disk.
CZMQ_EXPORT void
 zcertstore_destroy (zcertstore_t **self_p);
// Look up certificate by public key, returns zcert_t object if found,
// else returns NULL. The public key is provided in Z85 text format.
CZMQ_EXPORT zcert_t *
 zcertstore_lookup (zcertstore_t *self, const char *public_key);
// Insert certificate into certificate store in memory. Note that this
// does not save the certificate to disk. To do that, use zcert_save()
// directly on the certificate. Takes ownership of zcert_t object.
CZMQ_EXPORT void
 zcertstore_insert (zcertstore_t *self, zcert_t **cert_p);
// Print list of certificates in store to logging facility
CZMQ_EXPORT void
 zcertstore_print (zcertstore_t *self);
// DEPRECATED as incompatible with centralized logging
// Print list of certificates in store to open stream
CZMQ_EXPORT void
 zcertstore_fprint (zcertstore_t *self, FILE *file);
// Self test of this class
CZMQ_EXPORT void
 zcertstore_test (bool verbose);</pre>
<h2>Description</h2>
<p>To authenticate new clients using the ZeroMQ CURVE security mechanism, we have to check that the client&#8217;s public key matches a key we know and accept. There are numerous ways to store accepted client public keys. The mechanism CZMQ implements is &quot;certificates&quot; (plain text files) held in a &quot;certificate store&quot; (a disk directory). This class works with such certificate stores, and lets you easily load them from disk, and check if a given client public key is known or not. The zcert class does the work of managing a single certificate. </p>
<p> The certificate store can be memory-only, in which case you can load it yourself by inserting certificate objects one by one, or it can be loaded from disk, in which case you can add, modify, or remove certificates on disk at any time, and the store will detect such changes and refresh itself automatically. In most applications you won&#8217;t use this class directly but through the zauth class, which provides a high-level API for authentication (and manages certificate stores for you). To actually create certificates on disk, use the zcert class in code, or the tools/makecert.c command line tool, or any text editor. The format of a certificate file is defined in the zcert man page.</p>
<h2>Example</h2>
<p><code>From zcertstore_test method</code>. </p>
<pre><code>//  Create temporary directory for test files
#define TESTDIR &quot;.test_zcertstore&quot;
zsys_dir_create(TESTDIR);

//  Load certificate store from disk; it will be empty
zcertstore_t *certstore = zcertstore_new(TESTDIR);
assert(certstore);

//  Create a single new certificate and save to disk
zcert_t *cert = zcert_new();
assert(cert);
char *client_key = strdup(zcert_public_txt(cert));
assert(client_key);
zcert_set_meta(cert, &quot;name&quot;, &quot;John Doe&quot;);
zcert_save(cert, TESTDIR &quot;/mycert.txt&quot;);
zcert_destroy(&amp;cert);

//  Check that certificate store refreshes as expected
cert = zcertstore_lookup(certstore, client_key);
assert(cert);
assert(streq(zcert_meta(cert, &quot;name&quot;), &quot;John Doe&quot;));
free(client_key);

if (verbose)
    zcertstore_print(certstore);
zcertstore_destroy(&amp;certstore);

//  Delete all test files
zdir_t *dir = zdir_new(TESTDIR, NULL);
assert(dir);
zdir_remove(dir, true);
zdir_destroy(&amp;dir);
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
