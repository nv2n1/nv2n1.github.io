---
title: "zproxy_v2(3)"
name: "zproxy_v2"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zproxy_v2/"
description: "zproxy_v2 – run a steerable proxy in the background (deprecated)"
---

<p>zproxy_v2 &#8211; run a steerable proxy in the background (deprecated)</p>
<h2>Synopsis</h2>
<pre>// Constructor
// Create a new zproxy object. You must create the frontend and backend
// sockets, configure them, and connect or bind them, before you pass them
// to the constructor. Do NOT use the sockets again, after passing them to
// this method.
CZMQ_EXPORT zproxy_t *
 zproxy_new (zctx_t *ctx, void *frontend, void *backend);
// Destructor
// Destroy a zproxy object; note this first stops the proxy.
CZMQ_EXPORT void
 zproxy_destroy (zproxy_t **self_p);
// Copy all proxied messages to specified endpoint; if this is NULL, any
// in-progress capturing will be stopped. You must already have bound the
// endpoint to a PULL socket.
CZMQ_EXPORT void
 zproxy_capture (zproxy_t *self, const char *endpoint);
// Pauses a zproxy object; a paused proxy will cease processing messages,
// causing them to be queued up and potentially hit the high-water mark on
// the frontend socket, causing messages to be dropped, or writing
// applications to block.
CZMQ_EXPORT void
 zproxy_pause (zproxy_t *self);
// Resume a zproxy object
CZMQ_EXPORT void
 zproxy_resume (zproxy_t *self);
// Self test of this class
CZMQ_EXPORT void
 zproxy_v2_test (bool verbose);</pre>
<h2>Description</h2>
<p>The zproxy class provides an equivalent to the ZMQ steerable proxy, on all versions of ZeroMQ. </p>
<p> This class is deprecated in CZMQ v3; it works together with zctx, zsocket, and other deprecated V2 classes. New applications should use the V3 zproxy interface, based on zactor, together with the zsock class for sockets.</p>
<h2>Example</h2>
<p><code>From zproxy_v2_test method</code>. </p>
<pre><code>zctx_t *ctx = zctx_new();
assert(ctx);
void *frontend = zsocket_new(ctx, ZMQ_PULL);
assert(frontend);
int rc = zsocket_bind(frontend, &quot;inproc://frontend&quot;);
assert(rc == 0);
void *backend = zsocket_new(ctx, ZMQ_PUSH);
assert(backend);
rc = zsocket_bind(backend, &quot;inproc://backend&quot;);
assert(rc == 0);
zproxy_t *proxy = zproxy_new(ctx, frontend, backend);
assert(proxy);

//  Connect application sockets to proxy
void *faucet = zsocket_new(ctx, ZMQ_PUSH);
assert(faucet);
rc = zsocket_connect(faucet, &quot;inproc://frontend&quot;);
assert(rc == 0);
void *sink = zsocket_new(ctx, ZMQ_PULL);
assert(sink);
rc = zsocket_connect(sink, &quot;inproc://backend&quot;);
assert(rc == 0);

//  Send some messages and check they arrived
zstr_send(faucet, &quot;Hello&quot;);
char *string = zstr_recv(sink);
assert(streq(string, &quot;Hello&quot;));
zstr_free(&amp;string);

//  Check pause/resume functionality
zproxy_pause(proxy);
zstr_send(faucet, &quot;World&quot;);

zproxy_resume(proxy);
string = zstr_recv(sink);
assert(streq(string, &quot;World&quot;));
zstr_free(&amp;string);

//  Create capture socket, must be a PULL socket
void *capture = zsocket_new(ctx, ZMQ_PULL);
assert(capture);
rc = zsocket_bind(capture, &quot;inproc://capture&quot;);
assert(rc == 0);

//  Switch on capturing, check that it works
zproxy_capture(proxy, &quot;inproc://capture&quot;);
zstr_send(faucet, &quot;Hello&quot;);

string = zstr_recv(sink);
assert(streq(string, &quot;Hello&quot;));
zstr_free(&amp;string);

string = zstr_recv(capture);
assert(streq(string, &quot;Hello&quot;));
zstr_free(&amp;string);
zproxy_destroy(&amp;proxy);
zctx_destroy(&amp;ctx);
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
