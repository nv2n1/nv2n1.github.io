---
title: "zsock(3)"
name: "zsock"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zsock/"
description: "zsock – high-level socket API that hides libzmq contexts and sockets"
---

<p>zsock &#8211; high-level socket API that hides libzmq contexts and sockets</p>
<h2>Synopsis</h2>
<pre><code>//  Create a new socket. Returns the new socket, or NULL if the new socket
//  could not be created. Note that the symbol zsock_new (and other
//  constructors/destructors for zsock) are redirected to the *_checked
//  variant, enabling intelligent socket leak detection. This can have
//  performance implications if you use a LOT of sockets. To turn off this
//  redirection behaviour, define ZSOCK_NOCHECK.
CZMQ_EXPORT zsock_t *
zsock_new(int type);

//  Destroy the socket. You must use this for any socket created via the
//  zsock_new method.
CZMQ_EXPORT void
zsock_destroy(zsock_t **self_p);

//  Create a PUB socket. Default action is bind.
//  The caller is responsible for destroying the return value when finished with it.
CZMQ_EXPORT zsock_t *
zsock_new_pub(const char *endpoint);

//  Create a SUB socket, and optionally subscribe to some prefix string. Default
//  action is connect.
//  The caller is responsible for destroying the return value when finished with it.
CZMQ_EXPORT zsock_t *
zsock_new_sub(const char *endpoint, const char *subscribe);

//  Create a REQ socket. Default action is connect.
//  The caller is responsible for destroying the return value when finished with it.
CZMQ_EXPORT zsock_t *
zsock_new_req(const char *endpoint);

//  Create a REP socket. Default action is bind.
//  The caller is responsible for destroying the return value when finished with it.
CZMQ_EXPORT zsock_t *
zsock_new_rep(const char *endpoint);

//  Create a DEALER socket. Default action is connect.
//  The caller is responsible for destroying the return value when finished with it.
CZMQ_EXPORT zsock_t *
zsock_new_dealer(const char *endpoint);

//  Create a ROUTER socket. Default action is bind.
//  The caller is responsible for destroying the return value when finished with it.
CZMQ_EXPORT zsock_t *
zsock_new_router(const char *endpoint);

//  Create a PUSH socket. Default action is connect.
//  The caller is responsible for destroying the return value when finished with it.
CZMQ_EXPORT zsock_t *
zsock_new_push(const char *endpoint);

//  Create a PULL socket. Default action is bind.
//  The caller is responsible for destroying the return value when finished with it.
CZMQ_EXPORT zsock_t *
zsock_new_pull(const char *endpoint);

//  Create an XPUB socket. Default action is bind.
//  The caller is responsible for destroying the return value when finished with it.
CZMQ_EXPORT zsock_t *
zsock_new_xpub(const char *endpoint);

//  Create an XSUB socket. Default action is connect.
//  The caller is responsible for destroying the return value when finished with it.
CZMQ_EXPORT zsock_t *
zsock_new_xsub(const char *endpoint);

//  Create a PAIR socket. Default action is connect.
//  The caller is responsible for destroying the return value when finished with it.
CZMQ_EXPORT zsock_t *
zsock_new_pair(const char *endpoint);

//  Create a STREAM socket. Default action is connect.
//  The caller is responsible for destroying the return value when finished with it.
CZMQ_EXPORT zsock_t *
zsock_new_stream(const char *endpoint);

//  Bind a socket to a formatted endpoint. For tcp:// endpoints, supports
//  ephemeral ports, if you specify the port number as &quot;*&quot;. By default
//  zsock uses the IANA designated range from C000 (49152) to FFFF (65535).
//  To override this range, follow the &quot;*&quot; with &quot;[first-last]&quot;. Either or
//  both first and last may be empty. To bind to a random port within the
//  range, use &quot;!&quot; in place of &quot;*&quot;.
//
//  Examples:
//      tcp://127.0.0.1:*           bind to first free port from C000 up
//      tcp://127.0.0.1:!           bind to random port from C000 to FFFF
//      tcp://127.0.0.1:*[60000-]   bind to first free port from 60000 up
//      tcp://127.0.0.1:![-60000]   bind to random port from C000 to 60000
//      tcp://127.0.0.1:![55000-55999]
//                                  bind to random port from 55000 to 55999
//
//  On success, returns the actual port number used, for tcp:// endpoints,
//  and 0 for other transports. On failure, returns -1. Note that when using
//  ephemeral ports, a port may be reused by different services without
//  clients being aware. Protocols that run on ephemeral ports should take
//  this into account.
CZMQ_EXPORT int
zsock_bind(zsock_t *self, const char *format, ...) CHECK_PRINTF(2);

//  Returns last bound endpoint, if any.
CZMQ_EXPORT const char *
zsock_endpoint(zsock_t *self);

//  Unbind a socket from a formatted endpoint.
//  Returns 0 if OK, -1 if the endpoint was invalid or the function
//  isn't supported.
CZMQ_EXPORT int
zsock_unbind(zsock_t *self, const char *format, ...) CHECK_PRINTF(2);

//  Connect a socket to a formatted endpoint
//  Returns 0 if OK, -1 if the endpoint was invalid.
CZMQ_EXPORT int
zsock_connect(zsock_t *self, const char *format, ...) CHECK_PRINTF(2);

//  Disconnect a socket from a formatted endpoint
//  Returns 0 if OK, -1 if the endpoint was invalid or the function
//  isn't supported.
CZMQ_EXPORT int
zsock_disconnect(zsock_t *self, const char *format, ...) CHECK_PRINTF(2);

//  Attach a socket to zero or more endpoints. If endpoints is not null,
//  parses as list of ZeroMQ endpoints, separated by commas, and prefixed by
//  '@' (to bind the socket) or '&gt;' (to connect the socket). Returns 0 if all
//  endpoints were valid, or -1 if there was a syntax error. If the endpoint
//  does not start with '@' or '&gt;', the serverish argument defines whether
//  it is used to bind (serverish = true) or connect (serverish = false).
CZMQ_EXPORT int
zsock_attach(zsock_t *self, const char *endpoints, bool serverish);

//  Returns socket type as printable constant string.
CZMQ_EXPORT const char *
zsock_type_str(zsock_t *self);

//  Send a 'picture' message to the socket (or actor). The picture is a
//  string that defines the type of each frame. This makes it easy to send
//  a complex multiframe message in one call. The picture can contain any
//  of these characters, each corresponding to one or two arguments:
//
//      i = int (signed)
//      1 = uint8_t
//      2 = uint16_t
//      4 = uint32_t
//      8 = uint64_t
//      s = char *
//      b = byte *, size_t (2 arguments)
//      c = zchunk_t *
//      f = zframe_t *
//      h = zhashx_t *
//      U = zuuid_t *
//      p = void * (sends the pointer value, only meaningful over inproc)
//      m = zmsg_t * (sends all frames in the zmsg)
//      z = sends zero-sized frame (0 arguments)
//      u = uint (deprecated)
//
//  Note that s, b, c, and f are encoded the same way and the choice is
//  offered as a convenience to the sender, which may or may not already
//  have data in a zchunk or zframe. Does not change or take ownership of
//  any arguments. Returns 0 if successful, -1 if sending failed for any
//  reason.
CZMQ_EXPORT int
zsock_send(void *self, const char *picture, ...);

//  Send a 'picture' message to the socket (or actor). This is a va_list
//  version of zsock_send (), so please consult its documentation for the
//  details.
CZMQ_EXPORT int
zsock_vsend(void *self, const char *picture, va_list argptr);

//  Receive a 'picture' message to the socket (or actor). See zsock_send for
//  the format and meaning of the picture. Returns the picture elements into
//  a series of pointers as provided by the caller:
//
//      i = int * (stores signed integer)
//      4 = uint32_t * (stores 32-bit unsigned integer)
//      8 = uint64_t * (stores 64-bit unsigned integer)
//      s = char ** (allocates new string)
//      b = byte **, size_t * (2 arguments) (allocates memory)
//      c = zchunk_t ** (creates zchunk)
//      f = zframe_t ** (creates zframe)
//      U = zuuid_t * (creates a zuuid with the data)
//      h = zhashx_t ** (creates zhashx)
//      p = void ** (stores pointer)
//      m = zmsg_t ** (creates a zmsg with the remaing frames)
//      z = null, asserts empty frame (0 arguments)
//      u = uint * (stores unsigned integer, deprecated)
//
//  Note that zsock_recv creates the returned objects, and the caller must
//  destroy them when finished with them. The supplied pointers do not need
//  to be initialized. Returns 0 if successful, or -1 if it failed to recv
//  a message, in which case the pointers are not modified. When message
//  frames are truncated (a short message), sets return values to zero/null.
//  If an argument pointer is NULL, does not store any value (skips it).
//  An 'n' picture matches an empty frame; if the message does not match,
//  the method will return -1.
CZMQ_EXPORT int
zsock_recv(void *self, const char *picture, ...);

//  Receive a 'picture' message from the socket (or actor). This is a
//  va_list version of zsock_recv (), so please consult its documentation
//  for the details.
CZMQ_EXPORT int
zsock_vrecv(void *self, const char *picture, va_list argptr);

//  Send a binary encoded 'picture' message to the socket (or actor). This
//  method is similar to zsock_send, except the arguments are encoded in a
//  binary format that is compatible with zproto, and is designed to reduce
//  memory allocations. The pattern argument is a string that defines the
//  type of each argument. Supports these argument types:
//
//   pattern    C type                  zproto type:
//      1       uint8_t                 type = &quot;number&quot; size = &quot;1&quot;
//      2       uint16_t                type = &quot;number&quot; size = &quot;2&quot;
//      4       uint32_t                type = &quot;number&quot; size = &quot;3&quot;
//      8       uint64_t                type = &quot;number&quot; size = &quot;4&quot;
//      s       char *, 0-255 chars     type = &quot;string&quot;
//      S       char *, 0-2^32-1 chars  type = &quot;longstr&quot;
//      c       zchunk_t *              type = &quot;chunk&quot;
//      f       zframe_t *              type = &quot;frame&quot;
//      u       zuuid_t *               type = &quot;uuid&quot;
//      m       zmsg_t *                type = &quot;msg&quot;
//      p       void *, sends pointer value, only over inproc
//
//  Does not change or take ownership of any arguments. Returns 0 if
//  successful, -1 if sending failed for any reason.
CZMQ_EXPORT int
zsock_bsend(void *self, const char *picture, ...);

//  Receive a binary encoded 'picture' message from the socket (or actor).
//  This method is similar to zsock_recv, except the arguments are encoded
//  in a binary format that is compatible with zproto, and is designed to
//  reduce memory allocations. The pattern argument is a string that defines
//  the type of each argument. See zsock_bsend for the supported argument
//  types. All arguments must be pointers; this call sets them to point to
//  values held on a per-socket basis. Do not modify or destroy the returned
//  values. Returns 0 if successful, or -1 if it failed to read a message.
CZMQ_EXPORT int
zsock_brecv(void *self, const char *picture, ...);

//  Set socket to use unbounded pipes (HWM=0); use this in cases when you are
//  totally certain the message volume can fit in memory. This method works
//  across all versions of ZeroMQ. Takes a polymorphic socket reference.
CZMQ_EXPORT void
zsock_set_unbounded(void *self);

//  Send a signal over a socket. A signal is a short message carrying a
//  success/failure code (by convention, 0 means OK). Signals are encoded
//  to be distinguishable from &quot;normal&quot; messages. Accepts a zock_t or a
//  zactor_t argument, and returns 0 if successful, -1 if the signal could
//  not be sent. Takes a polymorphic socket reference.
CZMQ_EXPORT int
zsock_signal(void *self, byte status);

//  Wait on a signal. Use this to coordinate between threads, over pipe
//  pairs. Blocks until the signal is received. Returns -1 on error, 0 or
//  greater on success. Accepts a zsock_t or a zactor_t as argument.
//  Takes a polymorphic socket reference.
CZMQ_EXPORT int
zsock_wait(void *self);

//  If there is a partial message still waiting on the socket, remove and
//  discard it. This is useful when reading partial messages, to get specific
//  message types.
CZMQ_EXPORT void
zsock_flush(void *self);

//  Probe the supplied object, and report if it looks like a zsock_t.
//  Takes a polymorphic socket reference.
CZMQ_EXPORT bool
zsock_is(void *self);

//  Probe the supplied reference. If it looks like a zsock_t instance, return
//  the underlying libzmq socket handle; else if it looks like a file
//  descriptor, return NULL; else if it looks like a libzmq socket handle,
//  return the supplied value. Takes a polymorphic socket reference.
CZMQ_EXPORT void *
zsock_resolve(void *self);

//  Self test of this class
CZMQ_EXPORT void
zsock_test(bool verbose);</code></pre>
<h2>Description</h2>
<p>The zsock class wraps the libzmq socket handle (a void *) with a proper structure that follows the CLASS rules for construction and destruction. Some zsock methods take a void * &quot;polymorphic&quot; reference, which can be either a zsock_t or a zactor_t reference, or a libzmq void *. </p>
<p> Please add @discuss section in ../src/zsock.c.</p>
<h2>Example</h2>
<p><code>From zsock_test method</code>. </p>
<pre><code>zsock_t *writer = zsock_new_push(&quot;@tcp://127.0.0.1:5560&quot;);
assert(writer);
assert(zsock_resolve(writer) != writer);
assert(streq(zsock_type_str(writer), &quot;PUSH&quot;));

int rc;
#if (ZMQ_VERSION &gt;= ZMQ_MAKE_VERSION(3, 2, 0))
//  Check unbind
rc = zsock_unbind(writer, &quot;tcp://127.0.0.1:%d&quot;, 5560);
assert(rc == 0);

//  In some cases and especially when running under Valgrind, doing
//  a bind immediately after an unbind causes an EADDRINUSE error.
//  Even a short sleep allows the OS to release the port for reuse.
zclock_sleep(100);

//  Bind again
rc = zsock_bind(writer, &quot;tcp://127.0.0.1:%d&quot;, 5560);
assert(rc == 5560);
assert(streq(zsock_endpoint(writer), &quot;tcp://127.0.0.1:5560&quot;));
#endif

zsock_t *reader = zsock_new_pull(&quot;&gt;tcp://127.0.0.1:5560&quot;);
assert(reader);
assert(zsock_resolve(reader) != reader);
assert(streq(zsock_type_str(reader), &quot;PULL&quot;));

//  Basic Hello, World
zstr_send(writer, &quot;Hello, World&quot;);
zmsg_t *msg = zmsg_recv(reader);
assert(msg);
char *string = zmsg_popstr(msg);
assert(streq(string, &quot;Hello, World&quot;));
free(string);
zmsg_destroy(&amp;msg);

//  Test resolve FD
SOCKET fd = zsock_fd(reader);
assert(zsock_resolve((void *)&amp;fd) == NULL);

//  Test binding to ephemeral ports, sequential and random
int port = zsock_bind(writer, &quot;tcp://127.0.0.1:*&quot;);
assert(port &gt;= DYNAMIC_FIRST &amp;&amp; port &lt;= DYNAMIC_LAST);
port = zsock_bind(writer, &quot;tcp://127.0.0.1:*[50000-]&quot;);
assert(port &gt;= 50000 &amp;&amp; port &lt;= DYNAMIC_LAST);
port = zsock_bind(writer, &quot;tcp://127.0.0.1:*[-50001]&quot;);
assert(port &gt;= DYNAMIC_FIRST &amp;&amp; port &lt;= 50001);
port = zsock_bind(writer, &quot;tcp://127.0.0.1:*[60000-60050]&quot;);
assert(port &gt;= 60000 &amp;&amp; port &lt;= 60050);

port = zsock_bind(writer, &quot;tcp://127.0.0.1:!&quot;);
assert(port &gt;= DYNAMIC_FIRST &amp;&amp; port &lt;= DYNAMIC_LAST);
port = zsock_bind(writer, &quot;tcp://127.0.0.1:![50000-]&quot;);
assert(port &gt;= 50000 &amp;&amp; port &lt;= DYNAMIC_LAST);
port = zsock_bind(writer, &quot;tcp://127.0.0.1:![-50001]&quot;);
assert(port &gt;= DYNAMIC_FIRST &amp;&amp; port &lt;= 50001);
port = zsock_bind(writer, &quot;tcp://127.0.0.1:![60000-60050]&quot;);
assert(port &gt;= 60000 &amp;&amp; port &lt;= 60050);

//  Test zsock_attach method
zsock_t *server = zsock_new(ZMQ_DEALER);
assert(server);
rc = zsock_attach(server, &quot;@inproc://myendpoint,tcp://127.0.0.1:5556,inproc://others&quot;, true);
assert(rc == 0);
rc = zsock_attach(server, &quot;&quot;, false);
assert(rc == 0);
rc = zsock_attach(server, NULL, true);
assert(rc == 0);
rc = zsock_attach(server, &quot;&gt;a,@b, c,, &quot;, false);
assert(rc == -1);
zsock_destroy(&amp;server);

//  Test zsock_endpoint method
rc = zsock_bind(writer, &quot;inproc://test.%s&quot;, &quot;writer&quot;);
assert(rc == 0);
assert(streq(zsock_endpoint(writer), &quot;inproc://test.writer&quot;));

//  Test error state when connecting to an invalid socket type
//  ('txp://' instead of 'tcp://', typo intentional)
rc = zsock_connect(reader, &quot;txp://127.0.0.1:5560&quot;);
assert(rc == -1);

//  Test signal/wait methods
rc = zsock_signal(writer, 123);
assert(rc == 0);
rc = zsock_wait(reader);
assert(rc == 123);

//  Test zsock_send/recv pictures
uint8_t number1 = 123;
uint16_t number2 = 123 * 123;
uint32_t number4 = 123 * 123 * 123;
uint64_t number8 = 123 * 123 * 123 * 123;

zchunk_t *chunk = zchunk_new(&quot;HELLO&quot;, 5);
assert(chunk);
zframe_t *frame = zframe_new(&quot;WORLD&quot;, 5);
assert(frame);
zhashx_t *hash = zhashx_new();
assert(hash);
zuuid_t *uuid = zuuid_new();
assert(uuid);
zhashx_autofree(hash);
zhashx_insert(hash, &quot;1&quot;, &quot;value A&quot;);
zhashx_insert(hash, &quot;2&quot;, &quot;value B&quot;);
char *original = &quot;pointer&quot;;

//  Test zsock_recv into each supported type
zsock_send(writer, &quot;i1248zsbcfUhp&quot;,
           -12345, number1, number2, number4, number8,
           &quot;This is a string&quot;, &quot;ABCDE&quot;, 5,
           chunk, frame, uuid, hash, original);
char *uuid_str = strdup(zuuid_str(uuid));
zchunk_destroy(&amp;chunk);
zframe_destroy(&amp;frame);
zuuid_destroy(&amp;uuid);
zhashx_destroy(&amp;hash);

int integer;
byte *data;
size_t size;
char *pointer;
number8 = number4 = number2 = number1 = 0;
rc = zsock_recv(reader, &quot;i1248zsbcfUhp&quot;,
                &amp;integer, &amp;number1, &amp;number2, &amp;number4, &amp;number8,
                &amp;string, &amp;data, &amp;size, &amp;chunk, &amp;frame, &amp;uuid, &amp;hash, &amp;pointer);
assert(rc == 0);
assert(integer == -12345);
assert(number1 == 123);
assert(number2 == 123 * 123);
assert(number4 == 123 * 123 * 123);
assert(number8 == 123 * 123 * 123 * 123);
assert(streq(string, &quot;This is a string&quot;));
assert(memcmp(data, &quot;ABCDE&quot;, 5) == 0);
assert(size == 5);
assert(memcmp(zchunk_data(chunk), &quot;HELLO&quot;, 5) == 0);
assert(zchunk_size(chunk) == 5);
assert(streq(uuid_str, zuuid_str(uuid)));
assert(memcmp(zframe_data(frame), &quot;WORLD&quot;, 5) == 0);
assert(zframe_size(frame) == 5);
char *value = (char *)zhashx_lookup(hash, &quot;1&quot;);
assert(streq(value, &quot;value A&quot;));
value = (char *)zhashx_lookup(hash, &quot;2&quot;);
assert(streq(value, &quot;value B&quot;));
assert(original == pointer);
free(string);
free(data);
free(uuid_str);
zframe_destroy(&amp;frame);
zchunk_destroy(&amp;chunk);
zhashx_destroy(&amp;hash);

//  Test zsock_recv of short message; this lets us return a failure
//  with a status code and then nothing else; the receiver will get
//  the status code and NULL/zero for all other values
zsock_send(writer, &quot;i&quot;, -1);
zsock_recv(reader, &quot;izsbcfp&quot;,
           &amp;integer, &amp;string, &amp;data, &amp;size, &amp;chunk, &amp;frame, &amp;pointer);
assert(integer == -1);
assert(string == NULL);
assert(data == NULL);
assert(size == 0);
assert(chunk == NULL);
assert(frame == NULL);
assert(pointer == NULL);

msg = zmsg_new();
zmsg_addstr(msg, &quot;frame 1&quot;);
zmsg_addstr(msg, &quot;frame 2&quot;);
zsock_send(writer, &quot;szm&quot;, &quot;header&quot;, msg);
zmsg_destroy(&amp;msg);

zsock_recv(reader, &quot;szm&quot;, &amp;string, &amp;msg);

assert(streq(&quot;header&quot;, string));
assert(zmsg_size(msg) == 2);
assert(zframe_streq(zmsg_first(msg), &quot;frame 1&quot;));
assert(zframe_streq(zmsg_next(msg), &quot;frame 2&quot;));
zstr_free(&amp;string);
zmsg_destroy(&amp;msg);

//  Test zsock_recv with null arguments
chunk = zchunk_new(&quot;HELLO&quot;, 5);
assert(chunk);
frame = zframe_new(&quot;WORLD&quot;, 5);
assert(frame);
zsock_send(writer, &quot;izsbcfp&quot;,
           -12345, &quot;This is a string&quot;, &quot;ABCDE&quot;, 5, chunk, frame, original);
zframe_destroy(&amp;frame);
zchunk_destroy(&amp;chunk);
zsock_recv(reader, &quot;izsbcfp&quot;, &amp;integer, NULL, NULL, NULL, &amp;chunk, NULL, NULL);
assert(integer == -12345);
assert(memcmp(zchunk_data(chunk), &quot;HELLO&quot;, 5) == 0);
assert(zchunk_size(chunk) == 5);
zchunk_destroy(&amp;chunk);

//  Test zsock_bsend/brecv pictures with binary encoding
frame = zframe_new(&quot;Hello&quot;, 5);
chunk = zchunk_new(&quot;World&quot;, 5);

msg = zmsg_new();
zmsg_addstr(msg, &quot;Hello&quot;);
zmsg_addstr(msg, &quot;World&quot;);

zsock_bsend(writer, &quot;1248sSpcfm&quot;,
            number1, number2, number4, number8,
            &quot;Hello, World&quot;,
            &quot;Goodbye cruel World!&quot;,
            original,
            chunk, frame, msg);
zchunk_destroy(&amp;chunk);
zframe_destroy(&amp;frame);
zmsg_destroy(&amp;msg);

number8 = number4 = number2 = number1 = 0;
char *longstr;
zsock_brecv(reader, &quot;1248sSpcfm&quot;,
            &amp;number1, &amp;number2, &amp;number4, &amp;number8,
            &amp;string, &amp;longstr,
            &amp;pointer,
            &amp;chunk, &amp;frame, &amp;msg);
assert(number1 == 123);
assert(number2 == 123 * 123);
assert(number4 == 123 * 123 * 123);
assert(number8 == 123 * 123 * 123 * 123);
assert(streq(string, &quot;Hello, World&quot;));
assert(streq(longstr, &quot;Goodbye cruel World!&quot;));
assert(pointer == original);
zstr_free(&amp;longstr);
zchunk_destroy(&amp;chunk);
zframe_destroy(&amp;frame);
zmsg_destroy(&amp;msg);

//  Check that we can send a zproto format message
zsock_bsend(writer, &quot;1111sS4&quot;, 0xAA, 0xA0, 0x02, 0x01, &quot;key&quot;, &quot;value&quot;, 1234);
zgossip_msg_t *gossip = zgossip_msg_new();
zgossip_msg_recv(gossip, reader);
assert(zgossip_msg_id(gossip) == ZGOSSIP_MSG_PUBLISH);
zgossip_msg_destroy(&amp;gossip);

zsock_destroy(&amp;reader);
zsock_destroy(&amp;writer);
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
