---
title: "zsocket(3)"
name: "zsocket"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zsocket/"
description: "zsocket – working with 0MQ sockets (deprecated)"
---

<p>zsocket &#8211; working with 0MQ sockets (deprecated)</p>
<h2>Synopsis</h2>
<pre><code>//  This port range is defined by IANA for dynamic or private ports
//  We use this when choosing a port for dynamic binding.
#define ZSOCKET_DYNFROM 0xc000
#define ZSOCKET_DYNTO 0xffff

//  Callback function for zero-copy methods
typedef void(zsocket_free_fn)(void *data, void *arg);

//  Create a new socket within our CZMQ context, replaces zmq_socket.
//  Use this to get automatic management of the socket at shutdown.
//  Note: SUB sockets do not automatically subscribe to everything; you
//  must set filters explicitly.
CZMQ_EXPORT void *
zsocket_new(zctx_t *self, int type);

//  Destroy a socket within our CZMQ context, replaces zmq_close.
CZMQ_EXPORT void
zsocket_destroy(zctx_t *ctx, void *self);

//  Bind a socket to a formatted endpoint. If the port is specified as
//  '*', binds to any free port from ZSOCKET_DYNFROM to ZSOCKET_DYNTO
//  and returns the actual port number used. Otherwise asserts that the
//  bind succeeded with the specified port number. Always returns the
//  port number if successful.
CZMQ_EXPORT int
zsocket_bind(void *self, const char *format, ...);

//  Unbind a socket from a formatted endpoint.
//  Returns 0 if OK, -1 if the endpoint was invalid or the function
//  isn't supported.
CZMQ_EXPORT int
zsocket_unbind(void *self, const char *format, ...);

//  Connect a socket to a formatted endpoint
//  Returns 0 if OK, -1 if the endpoint was invalid.
CZMQ_EXPORT int
zsocket_connect(void *self, const char *format, ...);

//  Disconnect a socket from a formatted endpoint
//  Returns 0 if OK, -1 if the endpoint was invalid or the function
//  isn't supported.
CZMQ_EXPORT int
zsocket_disconnect(void *self, const char *format, ...);

//  Poll for input events on the socket. Returns TRUE if there is input
//  ready on the socket, else FALSE.
CZMQ_EXPORT bool
zsocket_poll(void *self, int msecs);

//  Returns socket type as printable constant string
CZMQ_EXPORT const char *
zsocket_type_str(void *self);

//  Send data over a socket as a single message frame.
//  Accepts these flags: ZFRAME_MORE and ZFRAME_DONTWAIT.
//  Returns -1 on error, 0 on success
CZMQ_EXPORT int
zsocket_sendmem(void *self, const void *data, size_t size, int flags);

//  Send a signal over a socket. A signal is a zero-byte message.
//  Signals are used primarily between threads, over pipe sockets.
//  Returns -1 if there was an error sending the signal.
CZMQ_EXPORT int
zsocket_signal(void *self);

//  Wait on a signal. Use this to coordinate between threads, over
//  pipe pairs. Returns -1 on error, 0 on success.
CZMQ_EXPORT int
zsocket_wait(void *self);

//  Self test of this class
CZMQ_EXPORT void
zsocket_test(bool verbose);</code></pre>
<h2>Description</h2>
<p>The zsocket class provides helper functions for 0MQ sockets. It doesn&#8217;t wrap the 0MQ socket type, to avoid breaking all libzmq socket-related calls. </p>
<p> Please add @discuss section in ../src/zsocket.c.</p>
<h2>Example</h2>
<p><code>From zsocket_test method</code>. </p>
<pre><code>zctx_t *ctx = zctx_new();
assert(ctx);

//  Create a detached thread, let it run
char *interf = &quot;127.0.0.1&quot;;
char *domain = &quot;localhost&quot;;
int service = 5560;

void *writer = zsocket_new(ctx, ZMQ_PUSH);
assert(writer);
void *reader = zsocket_new(ctx, ZMQ_PULL);
assert(reader);
assert(streq(zsocket_type_str(writer), &quot;PUSH&quot;));
assert(streq(zsocket_type_str(reader), &quot;PULL&quot;));
int rc = zsocket_bind(writer, &quot;tcp://%s:%d&quot;, interf, service);
assert(rc == service);

#if (ZMQ_VERSION &gt;= ZMQ_MAKE_VERSION(3, 2, 0))
//  Check unbind
rc = zsocket_unbind(writer, &quot;tcp://%s:%d&quot;, interf, service);
assert(rc == 0);

//  In some cases and especially when running under Valgrind, doing
//  a bind immediately after an unbind causes an EADDRINUSE error.
//  Even a short sleep allows the OS to release the port for reuse.
zclock_sleep(100);

//  Bind again
rc = zsocket_bind(writer, &quot;tcp://%s:%d&quot;, interf, service);
assert(rc == service);
#endif

rc = zsocket_connect(reader, &quot;tcp://%s:%d&quot;, domain, service);
assert(rc == 0);
zstr_send(writer, &quot;HELLO&quot;);
char *message = zstr_recv(reader);
assert(message);
assert(streq(message, &quot;HELLO&quot;));
free(message);

//  Test binding to ports
int port = zsocket_bind(writer, &quot;tcp://%s:*&quot;, interf);
assert(port &gt;= ZSOCKET_DYNFROM &amp;&amp; port &lt;= ZSOCKET_DYNTO);

assert(zsocket_poll(writer, 100) == false);

//  Test error state when connecting to an invalid socket type
//  ('txp://' instead of 'tcp://', typo intentional)
rc = zsocket_connect(reader, &quot;txp://%s:%d&quot;, domain, service);
assert(rc == -1);

//  Test sending frames to socket
rc = zsocket_sendmem(writer, &quot;ABC&quot;, 3, ZFRAME_MORE);
assert(rc == 0);
rc = zsocket_sendmem(writer, &quot;DEFG&quot;, 4, 0);
assert(rc == 0);

zframe_t *frame = zframe_recv(reader);
assert(frame);
assert(zframe_streq(frame, &quot;ABC&quot;));
assert(zframe_more(frame));
zframe_destroy(&amp;frame);

frame = zframe_recv(reader);
assert(frame);
assert(zframe_streq(frame, &quot;DEFG&quot;));
assert(!zframe_more(frame));
zframe_destroy(&amp;frame);

rc = zsocket_signal(writer);
assert(rc == 0);
rc = zsocket_wait(reader);
assert(rc == 0);

zsocket_destroy(ctx, reader);
zsocket_destroy(ctx, writer);
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
