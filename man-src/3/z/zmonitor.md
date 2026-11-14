---
title: "zmonitor(3)"
name: "zmonitor"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zmonitor/"
description: "zmonitor – socket event monitor"
---

<p>zmonitor &#8211; socket event monitor</p>
<h2>Synopsis</h2>
<pre><code>//  Create new zmonitor actor instance to monitor a zsock_t socket:
//
//      zactor_t *monitor = zactor_new (zmonitor, mysocket);
//
//  Destroy zmonitor instance.
//
//      zactor_destroy (&amp;monitor);
//
//  Enable verbose logging of commands and activity.
//
//      zstr_send (monitor, &quot;VERBOSE&quot;);
//
//  Listen to monitor event type (zero or types, ending in NULL):
//      zstr_sendx (monitor, &quot;LISTEN&quot;, type, ..., NULL);
//
//      Events:
//      CONNECTED
//      CONNECT_DELAYED
//      CONNECT_RETRIED
//      LISTENING
//      BIND_FAILED
//      ACCEPTED
//      ACCEPT_FAILED
//      CLOSED
//      CLOSE_FAILED
//      DISCONNECTED
//      MONITOR_STOPPED
//      ALL
//
//  Start monitor; after this, any further LISTEN commands are ignored.
//
//      zstr_send (monitor, &quot;START&quot;);
//      zsock_wait (monitor);
//
//  Receive next monitor event:
//
//      zmsg_t *msg = zmsg_recv (monitor);
//
//  This is the zmonitor constructor as a zactor_fn; the argument can be
//  a zactor_t, zsock_t, or libzmq void * socket:
CZMQ_EXPORT void
zmonitor(zsock_t *pipe, void *sock);

//  Selftest
CZMQ_EXPORT void
zmonitor_test(bool verbose);</code></pre>
<h2>Description</h2>
<p>The zmonitor actor provides an API for obtaining socket events such as connected, listen, disconnected, etc. Socket events are only available for sockets connecting or bound to ipc:// and tcp:// endpoints. </p>
<p> This class wraps the ZMQ socket monitor API, see zmq_socket_monitor for details. Works on all versions of libzmq from 3.2 onwards. This class replaces zproxy_v2, and is meant for applications that use the CZMQ v3 API (meaning, zsock).</p>
<h2>Example</h2>
<p><code>From zmonitor_test method</code>. </p>
<pre><code>zsock_t *client = zsock_new(ZMQ_DEALER);
assert(client);
zactor_t *clientmon = zactor_new(zmonitor, client);
assert(clientmon);
if (verbose)
    zstr_sendx(clientmon, &quot;VERBOSE&quot;, NULL);
zstr_sendx(clientmon, &quot;LISTEN&quot;, &quot;LISTENING&quot;, &quot;ACCEPTED&quot;, NULL);
zstr_sendx(clientmon, &quot;START&quot;, NULL);
zsock_wait(clientmon);

zsock_t *server = zsock_new(ZMQ_DEALER);
assert(server);
zactor_t *servermon = zactor_new(zmonitor, server);
assert(servermon);
if (verbose)
    zstr_sendx(servermon, &quot;VERBOSE&quot;, NULL);
zstr_sendx(servermon, &quot;LISTEN&quot;, &quot;CONNECTED&quot;, &quot;DISCONNECTED&quot;, NULL);
zstr_sendx(servermon, &quot;START&quot;, NULL);
zsock_wait(servermon);

//  Allow a brief time for the message to get there...
zmq_poll(NULL, 0, 200);

//  Check client is now listening
int port_nbr = zsock_bind(client, &quot;tcp://127.0.0.1:*&quot;);
assert(port_nbr != -1);
s_assert_event(clientmon, &quot;LISTENING&quot;);

//  Check server connected to client
zsock_connect(server, &quot;tcp://127.0.0.1:%d&quot;, port_nbr);
s_assert_event(servermon, &quot;CONNECTED&quot;);

//  Check client accepted connection
s_assert_event(clientmon, &quot;ACCEPTED&quot;);

zactor_destroy(&amp;clientmon);
zactor_destroy(&amp;servermon);
zsock_destroy(&amp;client);
zsock_destroy(&amp;server);
#endif
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
