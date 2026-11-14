---
title: "zuuid(3)"
name: "zuuid"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zuuid/"
description: "zuuid – UUID support class"
---

<p>zuuid &#8211; UUID support class</p>
<h2>Synopsis</h2>
<pre>// Constructor
CZMQ_EXPORT zuuid_t *
 zuuid_new (void);
// Destructor
CZMQ_EXPORT void
 zuuid_destroy (zuuid_t **self_p);
// Create UUID object from supplied ZUUID_LEN-octet value
CZMQ_EXPORT zuuid_t *
 zuuid_new_from (const byte *source);
// Set UUID to new supplied ZUUID_LEN-octet value
CZMQ_EXPORT void
 zuuid_set (zuuid_t *self, const byte *source);
// Set UUID to new supplied string value skipping '-' and '{' '}'
// optional delimiters. Return 0 if OK, else returns -1.
CZMQ_EXPORT int
 zuuid_set_str (zuuid_t *self, const char *source);
// Return UUID binary data
CZMQ_EXPORT const byte *
 zuuid_data (zuuid_t *self);
// Return UUID binary size
CZMQ_EXPORT size_t
 zuuid_size (zuuid_t *self);
// Returns UUID as string
CZMQ_EXPORT const char *
 zuuid_str (zuuid_t *self);
// Return UUID in the canonical string format: 8-4-4-4-12, in lower
// case. Caller does not modify or free returned value. See
// <a rel="nofollow" href="http://en.wikipedia.org/wiki/Universally_unique_identifier">http://en.wikipedia.org/wiki/Universally_unique_identifier</a>
CZMQ_EXPORT const char *
 zuuid_str_canonical (zuuid_t *self);
// Store UUID blob in target array
CZMQ_EXPORT void
 zuuid_export (zuuid_t *self, byte *target);
// Check if UUID is same as supplied value
CZMQ_EXPORT bool
 zuuid_eq (zuuid_t *self, const byte *compare);
// Check if UUID is different from supplied value
CZMQ_EXPORT bool
 zuuid_neq (zuuid_t *self, const byte *compare);
// Make copy of UUID object; if uuid is null, or memory was exhausted,
// returns null.
CZMQ_EXPORT zuuid_t *
 zuuid_dup (zuuid_t *self);
// Self test of this class
CZMQ_EXPORT void
 zuuid_test (bool verbose);</pre>
<h2>Description</h2>
<p>The zuuid class generates UUIDs and provides methods for working with them. If you build CZMQ with libuuid, on Unix/Linux, it will use that library. On Windows it will use UuidCreate(). Otherwise it will use a random number generator to produce convincing imitations of uuids. </p>
<p> Please add @discuss section in ../src/zuuid.c.</p>
<h2>Example</h2>
<p><code>From zuuid_test method</code>. </p>
<pre><code>//  Simple create/destroy test
assert(ZUUID_LEN == 16);
assert(ZUUID_STR_LEN == 32);

zuuid_t *uuid = zuuid_new();
assert(uuid);
assert(zuuid_size(uuid) == ZUUID_LEN);
assert(strlen(zuuid_str(uuid)) == ZUUID_STR_LEN);
zuuid_t *copy = zuuid_dup(uuid);
assert(streq(zuuid_str(uuid), zuuid_str(copy)));

//  Check set/set_str/export methods
const char *myuuid = &quot;8CB3E9A9649B4BEF8DE225E9C2CEBB38&quot;;
const char *myuuid2 = &quot;8CB3E9A9-649B-4BEF-8DE2-25E9C2CEBB38&quot;;
const char *myuuid3 = &quot;{8CB3E9A9-649B-4BEF-8DE2-25E9C2CEBB38}&quot;;
const char *myuuid4 = &quot;8CB3E9A9649B4BEF8DE225E9C2CEBB3838&quot;;
int rc = zuuid_set_str(uuid, myuuid);
assert(rc == 0);
assert(streq(zuuid_str(uuid), myuuid));
rc = zuuid_set_str(uuid, myuuid2);
assert(rc == 0);
assert(streq(zuuid_str(uuid), myuuid));
rc = zuuid_set_str(uuid, myuuid3);
assert(rc == 0);
assert(streq(zuuid_str(uuid), myuuid));
rc = zuuid_set_str(uuid, myuuid4);
assert(rc == -1);
byte copy_uuid[ZUUID_LEN];
zuuid_export(uuid, copy_uuid);
zuuid_set(uuid, copy_uuid);
assert(streq(zuuid_str(uuid), myuuid));

//  Check the canonical string format
assert(streq(zuuid_str_canonical(uuid),
             &quot;8cb3e9a9-649b-4bef-8de2-25e9c2cebb38&quot;));

zuuid_destroy(&amp;uuid);
zuuid_destroy(&amp;copy);
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
