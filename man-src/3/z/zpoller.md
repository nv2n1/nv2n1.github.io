---
title: "zpoller(3)"
name: "zpoller"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zpoller/"
description: "zpoller – trivial socket poller class"
---

<p>zpoller &#8211; trivial socket poller class</p>
<h2>Synopsis</h2>
<pre><code>//  Create new poller; the reader can be a libzmq socket (void *), a zsock_t
//  instance, or a zactor_t instance.
CZMQ_EXPORT zpoller_t *
zpoller_new(void *reader, ...);

//  Destroy a poller
CZMQ_EXPORT void
zpoller_destroy(zpoller_t **self_p);

//  Add a reader to be polled. Returns 0 if OK, -1 on failure. The reader may
//  be a libzmq void * socket, a zsock_t instance, or a zactor_t instance.
CZMQ_EXPORT int
zpoller_add(zpoller_t *self, void *reader);

//  Remove a reader from the poller; returns 0 if OK, -1 on failure. The
//  reader may be a libzmq void * socket, a zsock_t instance, or a zactor_t
//  instance.
CZMQ_EXPORT int
zpoller_remove(zpoller_t *self, void *reader);

//  Poll the registered readers for I/O, return first reader that has input.
//  The reader will be a libzmq void * socket, or a zsock_t or zactor_t
//  instance as specified in zpoller_new/zpoller_add. The timeout should be
//  zero or greater, or -1 to wait indefinitely. Socket priority is defined
//  by their order in the poll list. If you need a balanced poll, use the low
//  level zmq_poll method directly. If the poll call was interrupted (SIGINT),
//  or the ZMQ context was destroyed, or the timeout expired, returns NULL.
//  You can test the actual exit condition by calling zpoller_expired () and
//  zpoller_terminated (). The timeout is in msec.
CZMQ_EXPORT void *
zpoller_wait(zpoller_t *self, int timeout);

//  Return true if the last zpoller_wait () call ended because the timeout
//  expired, without any error.
CZMQ_EXPORT bool
zpoller_expired(zpoller_t *self);

//  Return true if the last zpoller_wait () call ended because the process
//  was interrupted, or the parent context was destroyed.
CZMQ_EXPORT bool
zpoller_terminated(zpoller_t *self);

//  Ignore zsys_interrupted flag in this poller. By default, a zpoller_wait will
//  return immediately if detects zsys_interrupted is set to something other than
//  zero. Calling zpoller_ignore_interrupts will supress this behavior.

CZMQ_EXPORT void
zpoller_ignore_interrupts(zpoller_t *self);

//  Self test of this class
CZMQ_EXPORT void
zpoller_test(bool verbose);</code></pre>
<h2>Description</h2>
<p>The zpoller class provides a minimalist interface to ZeroMQ&#8217;s zmq_poll API, for the very common case of reading from a number of sockets. It does not provide polling for output, nor polling on file handles. If you need either of these, use the zmq_poll API directly. </p>
<p> Please add @discuss section in ../src/zpoller.c.</p>
<h2>Example</h2>
<p><code>From zpoller_test method</code>. </p>
<pre><code>//  Create a few sockets
zsock_t *vent = zsock_new(ZMQ_PUSH);
assert(vent);
int port_nbr = zsock_bind(vent, &quot;tcp://127.0.0.1:*&quot;);
assert(port_nbr != -1);
zsock_t *sink = zsock_new(ZMQ_PULL);
assert(sink);
int rc = zsock_connect(sink, &quot;tcp://127.0.0.1:%d&quot;, port_nbr);
assert(rc != -1);
zsock_t *bowl = zsock_new(ZMQ_PULL);
assert(bowl);
zsock_t *dish = zsock_new(ZMQ_PULL);
assert(dish);

//  Set-up poller
zpoller_t *poller = zpoller_new(bowl, dish, NULL);
assert(poller);

// Add a reader to the existing poller
rc = zpoller_add(poller, sink);
assert(rc == 0);

zstr_send(vent, &quot;Hello, World&quot;);

//  We expect a message only on the sink
zsock_t *which = (zsock_t *)zpoller_wait(poller, -1);
assert(which == sink);
assert(zpoller_expired(poller) == false);
assert(zpoller_terminated(poller) == false);
char *message = zstr_recv(which);
assert(streq(message, &quot;Hello, World&quot;));
zstr_free(&amp;message);

//  Stop polling reader
rc = zpoller_remove(poller, sink);
assert(rc == 0);

//  Check we can poll an FD
rc = zsock_connect(bowl, &quot;tcp://127.0.0.1:%d&quot;, port_nbr);
assert(rc != -1);
SOCKET fd = zsock_fd(bowl);
rc = zpoller_add(poller, (void *)&amp;fd);
assert(rc != -1);
zstr_send(vent, &quot;Hello again, world&quot;);
assert(zpoller_wait(poller, 500) == &amp;fd);

// Check whether poller properly ignores zsys_interrupted flag
// when asked to
zsys_interrupted = 1;
zpoller_wait(poller, 0);
assert(zpoller_terminated(poller));
zpoller_ignore_interrupts(poller);
zpoller_wait(poller, 0);
assert(!zpoller_terminated(poller));
zsys_interrupted = 0;

//  Destroy poller and sockets
zpoller_destroy(&amp;poller);

zsock_destroy(&amp;vent);
zsock_destroy(&amp;sink);
zsock_destroy(&amp;bowl);
zsock_destroy(&amp;dish);
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
