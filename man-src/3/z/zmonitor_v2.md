---
title: "zmonitor_v2(3)"
name: "zmonitor_v2"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zmonitor_v2/"
description: "zmonitor_v2 – socket event monitor (deprecated)"
---

<p>zmonitor_v2 &#8211; socket event monitor (deprecated)</p>
<h2>Synopsis</h2>
<pre><code>//  This code needs backporting to work with ZMQ v3.2
#if (ZMQ_VERSION_MAJOR == 4)

//  Create a new socket monitor
CZMQ_EXPORT zmonitor_t *
zmonitor_new(zctx_t *ctx, void *socket, int events);

//  Destroy a socket monitor
CZMQ_EXPORT void
zmonitor_destroy(zmonitor_t **self_p);

//  Receive a status message from the monitor; if no message arrives within
//  500 msec, or the call was interrupted, returns NULL.
CZMQ_EXPORT zmsg_t *
zmonitor_recv(zmonitor_t *self);

//  Get the ZeroMQ socket, for polling
CZMQ_EXPORT void *
zmonitor_socket(zmonitor_t *self);

//  Enable verbose tracing of commands and activity
CZMQ_EXPORT void
zmonitor_set_verbose(zmonitor_t *self, bool verbose);
#endif //  ZeroMQ 4.0 or later

// Self test of this class
CZMQ_EXPORT void
zmonitor_v2_test(bool verbose);</code></pre>
<h2>Description</h2>
<p>The zmonitor class provides an API for obtaining socket events such as connected, listen, disconnected, etc. Socket events are only available for sockets connecting or bound to ipc:// and tcp:// endpoints. This class wraps the ZMQ socket monitor API, see zmq_socket_monitor for details. Currently this class requires libzmq v4.0 or later and is empty on older versions of libzmq. </p>
<p> This class is deprecated in CZMQ v3; it works together with zctx, zsocket, and other deprecated V2 classes. New applications should use the V3 zmonitor interface, based on zactor, together with the zsock class for sockets.</p>
<h2>Example</h2>
<p><code>From zmonitor_v2_test method</code>. </p>
<pre><code>zctx_t *ctx = zctx_new();
assert(ctx);
bool result;

void *sink = zsocket_new(ctx, ZMQ_PULL);
assert(sink);
zmonitor_t *sinkmon = zmonitor_new(ctx,
                                   sink, ZMQ_EVENT_LISTENING | ZMQ_EVENT_ACCEPTED);
assert(sinkmon);
zmonitor_set_verbose(sinkmon, verbose);

//  Check sink is now listening
int port_nbr = zsocket_bind(sink, &quot;tcp://127.0.0.1:*&quot;);
assert(port_nbr != -1);
result = s_check_event(sinkmon, ZMQ_EVENT_LISTENING);
assert(result);

void *source = zsocket_new(ctx, ZMQ_PUSH);
assert(source);
zmonitor_t *sourcemon = zmonitor_new(ctx,
                                     source, ZMQ_EVENT_CONNECTED | ZMQ_EVENT_DISCONNECTED);
assert(sourcemon);
zmonitor_set_verbose(sourcemon, verbose);
zsocket_connect(source, &quot;tcp://127.0.0.1:%d&quot;, port_nbr);

//  Check source connected to sink
result = s_check_event(sourcemon, ZMQ_EVENT_CONNECTED);
assert(result);

//  Check sink accepted connection
result = s_check_event(sinkmon, ZMQ_EVENT_ACCEPTED);
assert(result);

zmonitor_destroy(&amp;sinkmon);
zmonitor_destroy(&amp;sourcemon);
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
