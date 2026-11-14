---
title: "zbeacon_v2(3)"
name: "zbeacon_v2"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zbeacon_v2/"
description: "zbeacon_v2 – LAN discovery and presence (deprecated)"
---

<p>zbeacon_v2 &#8211; LAN discovery and presence (deprecated)</p>
<h2>Synopsis</h2>
<pre>// Create a new beacon on a certain UDP port. If the system does not
// support UDP broadcasts (lacking a useful interface), returns NULL.
// To force the beacon to operate on a given port, set the environment
// variable ZSYS_INTERFACE, or call zsys_set_interface() beforehand.
// If you are using the new zsock API then pass NULL as the ctx here.
CZMQ_EXPORT zbeacon_t *
 zbeacon_new (zctx_t *ctx, int port_nbr);
// Destroy a beacon
CZMQ_EXPORT void
 zbeacon_destroy (zbeacon_t **self_p);
// Return our own IP address as printable string
CZMQ_EXPORT char *
 zbeacon_hostname (zbeacon_t *self);
// Set broadcast interval in milliseconds (default is 1000 msec)
CZMQ_EXPORT void
 zbeacon_set_interval (zbeacon_t *self, int interval);
// Filter out any beacon that looks exactly like ours
CZMQ_EXPORT void
 zbeacon_noecho (zbeacon_t *self);
// Start broadcasting beacon to peers at the specified interval
CZMQ_EXPORT void
 zbeacon_publish (zbeacon_t *self, byte *transmit, size_t size);
// Stop broadcasting beacons
CZMQ_EXPORT void
 zbeacon_silence (zbeacon_t *self);
// Start listening to other peers; zero-sized filter means get everything
CZMQ_EXPORT void
 zbeacon_subscribe (zbeacon_t *self, byte *filter, size_t size);
// Stop listening to other peers
CZMQ_EXPORT void
 zbeacon_unsubscribe (zbeacon_t *self);
// Get beacon ZeroMQ socket, for polling or receiving messages
CZMQ_EXPORT void *
 zbeacon_socket (zbeacon_t *self);
// Self test of this class
CZMQ_EXPORT void
 zbeacon_v2_test (bool verbose);</pre>
<h2>Description</h2>
<p>The zbeacon class implements a peer-to-peer discovery service for local networks. A beacon can broadcast and/or capture service announcements using UDP messages on the local area network. This implementation uses IPv4 UDP broadcasts. You can define the format of your outgoing beacons, and set a filter that validates incoming beacons. Beacons are sent and received asynchronously in the background. The zbeacon API provides a incoming beacons on a ZeroMQ socket (the pipe) that you can configure, poll on, and receive messages on. Incoming beacons are always delivered as two frames: the ipaddress of the sender (a string), and the beacon data itself (binary, as published). </p>
<p> This class is deprecated in CZMQ v3; it works together with zctx, zsocket, and other deprecated V2 classes. New applications should use the V3 zauth interface, based on zactor, together with the zsock class for sockets.</p>
<h2>Example</h2>
<p><code>From zbeacon_v2_test method</code>. </p>
<pre><code>//  Create beacon to broadcast our service
zctx_t *ctx = zctx_new();
assert(ctx);
zbeacon_t *service_beacon = zbeacon_new(ctx, 9999);
if (service_beacon == NULL) {
    printf(&quot;OK (skipping test, no UDP discovery)
&quot;);
    return;
}
//  Create a service socket and bind to an ephemeral port
zsock_t *service = zsock_new(ZMQ_PUB);
assert(service);
int port_nbr = zsock_bind(service, &quot;tcp://127.0.0.1:*&quot;);
byte announcement[2] = {(port_nbr &gt;&gt; 8) &amp; 0xFF, port_nbr &amp; 0xFF};
zbeacon_set_interval(service_beacon, 100);
zbeacon_publish(service_beacon, announcement, 2);

//  Create beacon to lookup service
zbeacon_t *client_beacon = zbeacon_new(ctx, 9999);
assert(client_beacon);
zbeacon_subscribe(client_beacon, NULL, 0);

//  Wait for at most 1/2 second if there's no broadcast networking
zsocket_set_rcvtimeo(zbeacon_socket(client_beacon), 500);

char *ipaddress = zstr_recv(zbeacon_socket(client_beacon));
if (ipaddress) {
    zframe_t *content = zframe_recv(zbeacon_socket(client_beacon));
    int received_port = (zframe_data(content)[0] &lt;&lt; 8) + zframe_data(content)[1];
    assert(received_port == port_nbr);
    zframe_destroy(&amp;content);
    zbeacon_silence(service_beacon);
    zstr_free(&amp;ipaddress);
}
zbeacon_destroy(&amp;client_beacon);
zbeacon_destroy(&amp;service_beacon);

zbeacon_t *node1 = zbeacon_new(ctx, 5670);
assert(node1);
zbeacon_t *node2 = zbeacon_new(ctx, 5670);
assert(node2);
zbeacon_t *node3 = zbeacon_new(ctx, 5670);
assert(node3);

assert(*zbeacon_hostname(node1));
assert(*zbeacon_hostname(node2));
assert(*zbeacon_hostname(node3));

zbeacon_set_interval(node1, 250);
zbeacon_set_interval(node2, 250);
zbeacon_set_interval(node3, 250);
zbeacon_noecho(node1);
zbeacon_publish(node1, (byte *)&quot;NODE/1&quot;, 6);
zbeacon_publish(node2, (byte *)&quot;NODE/2&quot;, 6);
zbeacon_publish(node3, (byte *)&quot;GARBAGE&quot;, 7);
zbeacon_subscribe(node1, (byte *)&quot;NODE&quot;, 4);

//  Poll on three API sockets at once
zpoller_t *poller = zpoller_new(
    zbeacon_socket(node1),
    zbeacon_socket(node2),
    zbeacon_socket(node3), NULL);
assert(poller);

int64_t stop_at = zclock_mono() + 1000;
while (zclock_mono() &lt; stop_at) {
    long timeout = (long)(stop_at - zclock_mono());
    if (timeout &lt; 0)
        timeout = 0;
    void *which = zpoller_wait(poller, timeout * ZMQ_POLL_MSEC);
    if (which) {
        assert(which == zbeacon_socket(node1));
        char *ipaddress, *beacon;
        zstr_recvx(zbeacon_socket(node1), &amp;ipaddress, &amp;beacon, NULL);
        assert(streq(beacon, &quot;NODE/2&quot;));
        zstr_free(&amp;ipaddress);
        zstr_free(&amp;beacon);
    }
}
zpoller_destroy(&amp;poller);

//  Stop listening
zbeacon_unsubscribe(node1);

//  Stop all node broadcasts
zbeacon_silence(node1);
zbeacon_silence(node2);
zbeacon_silence(node3);

//  Destroy the test nodes
zbeacon_destroy(&amp;node1);
zbeacon_destroy(&amp;node2);
zbeacon_destroy(&amp;node3);

zsock_destroy(&amp;service);
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
