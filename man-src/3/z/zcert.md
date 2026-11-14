---
title: "zcert(3)"
name: "zcert"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zcert/"
description: "zcert – work with CURVE security certificates"
---

<p>zcert &#8211; work with CURVE security certificates</p>
<h2>Synopsis</h2>
<pre>// Create and initialize a new certificate in memory
CZMQ_EXPORT zcert_t *
 zcert_new (void);
// Constructor, accepts public/secret key pair from caller
CZMQ_EXPORT zcert_t *
 zcert_new_from (byte *public_key, byte *secret_key);
// Destroy a certificate in memory
CZMQ_EXPORT void
 zcert_destroy (zcert_t **self_p);
// Return public part of key pair as 32-byte binary string
CZMQ_EXPORT byte *
 zcert_public_key (zcert_t *self);
// Return secret part of key pair as 32-byte binary string
CZMQ_EXPORT byte *
 zcert_secret_key (zcert_t *self);
// Return public part of key pair as Z85 armored string
CZMQ_EXPORT char *
 zcert_public_txt (zcert_t *self);
// Return secret part of key pair as Z85 armored string
CZMQ_EXPORT char *
 zcert_secret_txt (zcert_t *self);
// Set certificate metadata from formatted string.
CZMQ_EXPORT void
 zcert_set_meta (zcert_t *self, const char *name, const char *format, ...);
// Get metadata value from certificate; if the metadata value doesn't
// exist, returns NULL.
CZMQ_EXPORT char *
 zcert_meta (zcert_t *self, const char *name);
// Get list of metadata fields from certificate. Caller is responsible for
// destroying list. Caller should not modify the values of list items.
CZMQ_EXPORT zlist_t *
 zcert_meta_keys (zcert_t *self);
// Load certificate from file (constructor)
CZMQ_EXPORT zcert_t *
 zcert_load (const char *filename);
// Save full certificate (public + secret) to file for persistent storage
// This creates one public file and one secret file (filename + &quot;_secret&quot;).
CZMQ_EXPORT int
 zcert_save (zcert_t *self, const char *filename);
// Save public certificate only to file for persistent storage
CZMQ_EXPORT int
 zcert_save_public (zcert_t *self, const char *filename);
// Save secret certificate only to file for persistent storage
CZMQ_EXPORT int
 zcert_save_secret (zcert_t *self, const char *filename);
// Apply certificate to socket, i.e. use for CURVE security on socket.
// If certificate was loaded from public file, the secret key will be
// undefined, and this certificate will not work successfully.
CZMQ_EXPORT void
 zcert_apply (zcert_t *self, void *zocket);
// Return copy of certificate; if certificate is null or we exhausted
// heap memory, returns null.
CZMQ_EXPORT zcert_t *
 zcert_dup (zcert_t *self);
// Return true if two certificates have the same keys
CZMQ_EXPORT bool
 zcert_eq (zcert_t *self, zcert_t *compare);
// Print certificate contents to stdout
CZMQ_EXPORT void
 zcert_print (zcert_t *self);
// DEPRECATED as incompatible with centralized logging
// Print certificate contents to open stream
CZMQ_EXPORT void
 zcert_fprint (zcert_t *self, FILE *file);
// Self test of this class
CZMQ_EXPORT void
 zcert_test (bool verbose);</pre>
<h2>Description</h2>
<p>The zcert class provides a way to create and work with security certificates for the ZMQ CURVE mechanism. A certificate contains a public + secret key pair, plus metadata. It can be used as a temporary object in memory, or persisted to disk. On disk, a certificate is stored as two files. One is public and contains only the public key. The second is secret and contains both keys. The two have the same filename, with the secret file adding &quot;_secret&quot;. To exchange certificates, send the public file via some secure route. Certificates are not signed but are text files that can be verified by eye. </p>
<p> Certificates are stored in the ZPL (ZMQ RFC 4) format. They have two sections, &quot;metadata&quot; and &quot;curve&quot;. The first contains a list of <i>name = value</i> pairs, one per line. Values may be enclosed in quotes. The curve section has a <i>public-key = keyvalue</i> and, for secret certificates, a <i>secret-key = keyvalue</i> line. The keyvalue is a Z85-encoded CURVE key.</p>
<h2>Example</h2>
<p><code>From zcert_test method</code>. </p>
<pre><code>//  Create temporary directory for test files
#define TESTDIR &quot;.test_zcert&quot;
zsys_dir_create(TESTDIR);

//  Create a simple certificate with metadata
zcert_t *cert = zcert_new();
assert(cert);
zcert_set_meta(cert, &quot;email&quot;, &quot;ph [at] imatix.com&quot;);
zcert_set_meta(cert, &quot;name&quot;, &quot;Pieter Hintjens&quot;);
zcert_set_meta(cert, &quot;organization&quot;, &quot;iMatix Corporation&quot;);
zcert_set_meta(cert, &quot;version&quot;, &quot;%d&quot;, 1);
assert(streq(zcert_meta(cert, &quot;email&quot;), &quot;ph [at] imatix.com&quot;));
zlist_t *keys = zcert_meta_keys(cert);
assert(zlist_size(keys) == 4);
zlist_destroy(&amp;keys);

//  Check the dup and eq methods
zcert_t *shadow = zcert_dup(cert);
assert(zcert_eq(cert, shadow));
zcert_destroy(&amp;shadow);

//  Check we can save and load certificate
zcert_save(cert, TESTDIR &quot;/mycert.txt&quot;);
assert(zsys_file_exists(TESTDIR &quot;/mycert.txt&quot;));
assert(zsys_file_exists(TESTDIR &quot;/mycert.txt_secret&quot;));

//  Load certificate, will in fact load secret one
shadow = zcert_load(TESTDIR &quot;/mycert.txt&quot;);
assert(shadow);
assert(zcert_eq(cert, shadow));
zcert_destroy(&amp;shadow);

//  Delete secret certificate, load public one
int rc = zsys_file_delete(TESTDIR &quot;/mycert.txt_secret&quot;);
assert(rc == 0);
shadow = zcert_load(TESTDIR &quot;/mycert.txt&quot;);

//  32-byte null key encodes as 40 '0' characters
assert(streq(zcert_secret_txt(shadow), FORTY_ZEROES));

zcert_destroy(&amp;shadow);
zcert_destroy(&amp;cert);

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
