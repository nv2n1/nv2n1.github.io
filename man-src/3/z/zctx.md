---
title: "zctx(3)"
name: "zctx"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zctx/"
description: "zctx – working with 0MQ contexts (deprecated)"
---

<p>zctx &#8211; working with 0MQ contexts (deprecated)</p>
<h2>Synopsis</h2>
<pre>// Create new context, returns context object, replaces zmq_init
CZMQ_EXPORT zctx_t *
 zctx_new (void);
// Destroy context and all sockets in it, replaces zmq_term
CZMQ_EXPORT void
 zctx_destroy (zctx_t **self_p);
// Create new shadow context, returns context object
CZMQ_EXPORT zctx_t *
 zctx_shadow (zctx_t *self);
// Raise default I/O threads from 1, for crazy heavy applications
// The rule of thumb is one I/O thread per gigabyte of traffic in
// or out. Call this method before creating any sockets on the context,
// or calling zctx_shadow, or the setting will have no effect.
CZMQ_EXPORT void
 zctx_set_iothreads (zctx_t *self, int iothreads);
// Set msecs to flush sockets when closing them, see the ZMQ_LINGER
// man page section for more details. By default, set to zero, so
// any in-transit messages are discarded when you destroy a socket or
// a context.
CZMQ_EXPORT void
 zctx_set_linger (zctx_t *self, int linger);
// Set initial high-water mark for inter-thread pipe sockets. Note that
// this setting is separate from the default for normal sockets. You
// should change the default for pipe sockets *with care*. Too low values
// will cause blocked threads, and an infinite setting can cause memory
// exhaustion. The default, no matter the underlying ZeroMQ version, is
// 1,000.
CZMQ_EXPORT void
 zctx_set_pipehwm (zctx_t *self, int pipehwm);
// Set initial send HWM for all new normal sockets created in context.
// You can set this per-socket after the socket is created.
// The default, no matter the underlying ZeroMQ version, is 1,000.
CZMQ_EXPORT void
 zctx_set_sndhwm (zctx_t *self, int sndhwm);
// Set initial receive HWM for all new normal sockets created in context.
// You can set this per-socket after the socket is created.
// The default, no matter the underlying ZeroMQ version, is 1,000.
CZMQ_EXPORT void
 zctx_set_rcvhwm (zctx_t *self, int rcvhwm);
// Return low-level 0MQ context object, will be NULL before first socket
// is created. Use with care.
CZMQ_EXPORT void *
 zctx_underlying (zctx_t *self);
// Self test of this class
CZMQ_EXPORT void
 zctx_test (bool verbose);</pre>
<h2>Description</h2>
<p>The zctx class wraps 0MQ contexts. It manages open sockets in the context and automatically closes these before terminating the context. It provides a simple way to set the linger timeout on sockets, and configure contexts for number of I/O threads. Sets-up signal (interrupt) handling for the process. The zctx class has these main features:</p>
<dl>
<dd>&bull; Tracks all open sockets and automatically closes them before calling zmq_term(). This avoids an infinite wait on open sockets.</dl>
<dl>
<dd>&bull; Automatically configures sockets with a ZMQ_LINGER timeout you can define, and which defaults to zero. The default behavior of zctx is therefore like 0MQ/2.0, immediate termination with loss of any pending messages. You can set any linger timeout you like by calling the zctx_set_linger() method.</dl>
<dl>
<dd>&bull; Moves the iothreads configuration to a separate method, so that default usage is 1 I/O thread. Lets you configure this value.</dl>
<dl>
<dd>&bull; Sets up signal (SIGINT and SIGTERM) handling so that blocking calls such as zmq_recv() and zmq_poll() will return when the user presses Ctrl-C.</dl>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 this class is deprecated in favor of zsock, which does not expose contexts in the API at all. All zsock instances use the same global context. </p>
<h2>Example</h2>
<p><code>From zctx_test method</code>. </p>
<pre><code>//  Create and destroy a context without using it
zctx_t *ctx = zctx_new();
assert(ctx);
zctx_destroy(&amp;ctx);
assert(ctx == NULL);

//  Create a context with many busy sockets, destroy it
ctx = zctx_new();
assert(ctx);
zctx_set_iothreads(ctx, 1);
zctx_set_linger(ctx, 5); //  5 msecs
void *s1 = zctx__socket_new(ctx, ZMQ_PAIR);
assert(s1);
void *s2 = zctx__socket_new(ctx, ZMQ_XREQ);
assert(s2);
void *s3 = zctx__socket_new(ctx, ZMQ_REQ);
assert(s3);
void *s4 = zctx__socket_new(ctx, ZMQ_REP);
assert(s4);
void *s5 = zctx__socket_new(ctx, ZMQ_PUB);
assert(s5);
void *s6 = zctx__socket_new(ctx, ZMQ_SUB);
assert(s6);
int rc = zsocket_connect(s1, &quot;tcp://127.0.0.1:5555&quot;);
assert(rc == 0);
rc = zsocket_connect(s2, &quot;tcp://127.0.0.1:5555&quot;);
assert(rc == 0);
rc = zsocket_connect(s3, &quot;tcp://127.0.0.1:5555&quot;);
assert(rc == 0);
rc = zsocket_connect(s4, &quot;tcp://127.0.0.1:5555&quot;);
assert(rc == 0);
rc = zsocket_connect(s5, &quot;tcp://127.0.0.1:5555&quot;);
assert(rc == 0);
rc = zsocket_connect(s6, &quot;tcp://127.0.0.1:5555&quot;);
assert(rc == 0);
assert(zctx_underlying(ctx));
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
