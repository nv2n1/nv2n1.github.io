---
title: "zgossip(3)"
name: "zgossip"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zgossip/"
description: "zgossip – decentralized configuration management"
---

<p>zgossip &#8211; decentralized configuration management</p>
<h2>Synopsis</h2>
<pre><code>//  To work with zgossip, use the CZMQ zactor API:
//
//  Create new zgossip instance, passing logging prefix:
//
//      zactor_t *zgossip = zactor_new (zgossip, &quot;myname&quot;);
//
//  Destroy zgossip instance
//
//      zactor_destroy (&amp;zgossip);
//
//  Enable verbose logging of commands and activity:
//
//      zstr_send (zgossip, &quot;VERBOSE&quot;);
//
//  Bind zgossip to specified endpoint. TCP endpoints may specify
//  the port number as &quot;*&quot; to aquire an ephemeral port:
//
//      zstr_sendx (zgossip, &quot;BIND&quot;, endpoint, NULL);
//
//  Return assigned port number, specifically when BIND was done using an
//  an ephemeral port:
//
//      zstr_sendx (zgossip, &quot;PORT&quot;, NULL);
//      char *command, *port_str;
//      zstr_recvx (zgossip, &amp;command, &amp;port_str, NULL);
//      assert (streq (command, &quot;PORT&quot;));
//
//  Specify configuration file to load, overwriting any previous loaded
//  configuration file or options:
//
//      zstr_sendx (zgossip, &quot;LOAD&quot;, filename, NULL);
//
//  Set configuration path value:
//
//      zstr_sendx (zgossip, &quot;SET&quot;, path, value, NULL);
//
//  Save configuration data to config file on disk:
//
//      zstr_sendx (zgossip, &quot;SAVE&quot;, filename, NULL);
//
//  Send zmsg_t instance to zgossip:
//
//      zactor_send (zgossip, &amp;msg);
//
//  Receive zmsg_t instance from zgossip:
//
//      zmsg_t *msg = zactor_recv (zgossip);
//
//  This is the zgossip constructor as a zactor_fn:
//
CZMQ_EXPORT void
zgossip(zsock_t *pipe, void *args);

//  Self test of this class
CZMQ_EXPORT void
zgossip_test(bool verbose);</code></pre>
<h2>Description</h2>
<p>Implements a gossip protocol for decentralized configuration management. Your applications nodes form a loosely connected network (which can have cycles), and publish name/value tuples. Each node re-distributes the new tuples it receives, so that the entire network eventually achieves a consistent state. The current design does not expire tuples. </p>
<p> Provides these commands (sent as multipart strings to the actor): </p>
<dl>
<dd>&bull; BIND endpoint &#8212; binds the gossip service to specified endpoint</dl>
<dl>
<dd>&bull; PORT &#8212; returns the last TCP port, if any, used for binding</dl>
<dl>
<dd>&bull; LOAD configfile &#8212; load configuration from specified file</dl>
<dl>
<dd>&bull; SET configpath value &#8212; set configuration path = value</dl>
<dl>
<dd>&bull; SAVE configfile &#8212; save configuration to specified file</dl>
<dl>
<dd>&bull; CONNECT endpoint &#8212; connect the gossip service to the specified peer</dl>
<dl>
<dd>&bull; PUBLISH key value &#8212; publish a key/value pair to the gossip cluster</dl>
<dl>
<dd>&bull; STATUS &#8212; return number of key/value pairs held by gossip service</dl>
<p> Returns these messages: </p>
<dl>
<dd>&bull; PORT number &#8212; reply to PORT command</dl>
<dl>
<dd>&bull; STATUS number &#8212; reply to STATUS command</dl>
<dl>
<dd>&bull; DELIVER key value &#8212; new tuple delivered from network</dl>
<p> The gossip protocol distributes information around a loosely-connected network of gossip services. The information consists of name/value pairs published by applications at any point in the network. The goal of the gossip protocol is to create eventual consistency between all the using applications. </p>
<p> The name/value pairs (tuples) can be used for configuration data, for status updates, for presence, or for discovery. When used for discovery, the gossip protocol works as an alternative to e.g. UDP beaconing. </p>
<p> The gossip network consists of a set of loosely-coupled nodes that exchange tuples. Nodes can be connected across arbitrary transports, so the gossip network can have nodes that communicate over inproc, over IPC, and/or over TCP, at the same time. </p>
<p> Each node runs the same stack, which is a server-client hybrid using a modified Harmony pattern (from Chapter 8 of the Guide): m[blue]<code><a rel="nofollow" href="http://zguide.zeromq.org/page:all#True-Peer-Connectivity-Harmony-Pattern">http://zguide.zeromq.org/page:all#True-Peer-Connectivity-Harmony-Pattern</a></code>m[] </p>
<p> Each node provides a ROUTER socket that accepts client connections on an key defined by the application via a BIND command. The state machine for these connections is in zgossip.xml, and the generated code is in zgossip_engine.inc. </p>
<p> Each node additionally creates outbound connections via DEALER sockets to a set of servers (&quot;remotes&quot;), and under control of the calling app, which sends CONNECT commands for each configured remote. </p>
<p> The messages between client and server are defined in zgossip_msg.xml. We built this stack using the zeromq/zproto toolkit. </p>
<p> To join the gossip network, a node connects to one or more peers. Each peer acts as a forwarder. This loosely-coupled network can scale to thousands of nodes. However the gossip protocol is NOT designed to be efficient, and should not be used for application data, as the same tuples may be sent many times across the network. </p>
<p> The basic logic of the gossip service is to accept PUBLISH messages from its owning application, and to forward these to every remote, and every client it talks to. When a node gets a duplicate tuple, it throws it away. When a node gets a new tuple, it stores it, and fowards it as just described. At any point the application can access the node&#8217;s set of tuples. </p>
<p> At present there is no way to expire tuples from the network. </p>
<p> The assumptions in this design are: </p>
<dl>
<dd>&bull; The data set is slow-changing. Thus, the cost of the gossip protocol is irrelevant with respect to other traffic.</dl>
<h2>Example</h2>
<p><code>From zgossip_test method</code>. </p>
<pre><code>//  Test basic client-to-server operation of the protocol
zactor_t *server = zactor_new(zgossip, &quot;server&quot;);
assert(server);
if (verbose)
    zstr_send(server, &quot;VERBOSE&quot;);
zstr_sendx(server, &quot;BIND&quot;, &quot;inproc://zgossip&quot;, NULL);

zsock_t *client = zsock_new(ZMQ_DEALER);
assert(client);
zsock_set_rcvtimeo(client, 2000);
int rc = zsock_connect(client, &quot;inproc://zgossip&quot;);
assert(rc == 0);

//  Send HELLO, which gets no message
zgossip_msg_t *message = zgossip_msg_new();
zgossip_msg_set_id(message, ZGOSSIP_MSG_HELLO);
zgossip_msg_send(message, client);

//  Send PING, expect PONG back
zgossip_msg_set_id(message, ZGOSSIP_MSG_PING);
zgossip_msg_send(message, client);
zgossip_msg_recv(message, client);
assert(zgossip_msg_id(message) == ZGOSSIP_MSG_PONG);
zgossip_msg_destroy(&amp;message);

zactor_destroy(&amp;server);
zsock_destroy(&amp;client);

//  Test peer-to-peer operations
zactor_t *base = zactor_new(zgossip, &quot;base&quot;);
assert(base);
if (verbose)
    zstr_send(base, &quot;VERBOSE&quot;);
//  Set a 100msec timeout on clients so we can test expiry
zstr_sendx(base, &quot;SET&quot;, &quot;server/timeout&quot;, &quot;100&quot;, NULL);
zstr_sendx(base, &quot;BIND&quot;, &quot;inproc://base&quot;, NULL);

zactor_t *alpha = zactor_new(zgossip, &quot;alpha&quot;);
assert(alpha);
zstr_sendx(alpha, &quot;CONNECT&quot;, &quot;inproc://base&quot;, NULL);
zstr_sendx(alpha, &quot;PUBLISH&quot;, &quot;inproc://alpha-1&quot;, &quot;service1&quot;, NULL);
zstr_sendx(alpha, &quot;PUBLISH&quot;, &quot;inproc://alpha-2&quot;, &quot;service2&quot;, NULL);

zactor_t *beta = zactor_new(zgossip, &quot;beta&quot;);
assert(beta);
zstr_sendx(beta, &quot;CONNECT&quot;, &quot;inproc://base&quot;, NULL);
zstr_sendx(beta, &quot;PUBLISH&quot;, &quot;inproc://beta-1&quot;, &quot;service1&quot;, NULL);
zstr_sendx(beta, &quot;PUBLISH&quot;, &quot;inproc://beta-2&quot;, &quot;service2&quot;, NULL);

//  got nothing
zclock_sleep(200);

zactor_destroy(&amp;base);
zactor_destroy(&amp;alpha);
zactor_destroy(&amp;beta);
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
