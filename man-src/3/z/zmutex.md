---
title: "zmutex(3)"
name: "zmutex"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zmutex/"
description: "zmutex – working with mutexes (deprecated)"
---

<p>zmutex &#8211; working with mutexes (deprecated)</p>
<h2>Synopsis</h2>
<pre>// Create a new mutex container
CZMQ_EXPORT zmutex_t *
 zmutex_new (void);
// Destroy a mutex container
CZMQ_EXPORT void
 zmutex_destroy (zmutex_t **self_p);
// Lock mutex
CZMQ_EXPORT void
 zmutex_lock (zmutex_t *self);
// Unlock mutex
CZMQ_EXPORT void
 zmutex_unlock (zmutex_t *self);
// Try to lock mutex
CZMQ_EXPORT int
 zmutex_try_lock (zmutex_t *self);
// Self test of this class
CZMQ_EXPORT void
 zmutex_test (bool verbose);</pre>
<h2>Description</h2>
<p>The zmutex class provides a portable wrapper for mutexes. Please do not use this class to do multi-threading. It is for the rare case where you absolutely need thread-safe global state. This should happen in system code only. DO NOT USE THIS TO SHARE SOCKETS BETWEEN THREADS, OR DARK THINGS WILL HAPPEN TO YOUR CODE. </p>
<p> Please add @discuss section in ../src/zmutex.c.</p>
<h2>Example</h2>
<p><code>From zmutex_test method</code>. </p>
<pre><code>zmutex_t *mutex = zmutex_new ();
assert (mutex);
zmutex_lock (mutex);
zmutex_unlock (mutex);
zmutex_destroy (&amp;mutex);
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
