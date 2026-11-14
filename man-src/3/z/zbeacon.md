---
title: "zbeacon(3)"
name: "zbeacon"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zbeacon/"
description: "zbeacon – LAN discovery and presence"
---

<p>zbeacon &#8211; LAN discovery and presence</p>
<h2>Synopsis</h2>
<pre><code>//  Create new zbeacon actor instance:
//
//      zactor_t *beacon = zactor_new (zbeacon, NULL);
//
//  Destroy zbeacon instance:
//
//      zactor_destroy (&amp;beacon);
//
//  Enable verbose logging of commands and activity:
//
//      zstr_send (beacon, &quot;VERBOSE&quot;);
//
//  Configure beacon to run on specified UDP port, and return the name of
//  the host, which can be used as endpoint for incoming connections. To
//  force the beacon to operate on a given interface, set the environment
//  variable ZSYS_INTERFACE, or call zsys_set_interface() before creating
//  the beacon. If the system does not support UDP broadcasts (lacking a
//  workable interface), returns an empty hostname:
//
//      //  Pictures: 's' = C string, 'i' = int
//      zsock_send (beacon, &quot;si&quot;, &quot;CONFIGURE&quot;, port_number);
//      char *hostname = zstr_recv (beacon);
//
//  Start broadcasting a beacon at a specified interval in msec. The beacon
//  data can be at most UDP_FRAME_MAX bytes; this constant is defined in
//  zsys.h to be 255:
//
//      //  Pictures: 'b' = byte * data + size_t size
//      zsock_send (beacon, &quot;sbi&quot;, &quot;PUBLISH&quot;, data, size, interval);
//
//  Stop broadcasting the beacon:
//
//      zstr_sendx (beacon, &quot;SILENCE&quot;, NULL);
//
//  Start listening to beacons from peers. The filter is used to do a prefix
//  match on received beacons, to remove junk. Note that any received data
//  that is identical to our broadcast beacon_data is discarded in any case.
//  If the filter size is zero, we get all peer beacons:
//
//      zsock_send (beacon, &quot;sb&quot;, &quot;SUBSCRIBE&quot;, filter_data, filter_size);
//
//  Stop listening to other peers
//
//      zstr_sendx (beacon, &quot;UNSUBSCRIBE&quot;, NULL);
//
//  Receive next beacon from a peer. Received beacons are always a 2-frame
//  message containing the ipaddress of the sender, and then the binary
//  beacon data as published by the sender:
//
//      zmsg_t *msg = zmsg_recv (beacon);
//
//  This is the zbeacon constructor as a zactor_fn:
CZMQ_EXPORT void
zbeacon(zsock_t *pipe, void *unused);

//  Self test of this class
CZMQ_EXPORT void
zbeacon_test(bool verbose);</code></pre>
<h2>Description</h2>
<p>The zbeacon class implements a peer-to-peer discovery service for local networks. A beacon can broadcast and/or capture service announcements using UDP messages on the local area network. This implementation uses IPv4 UDP broadcasts. You can define the format of your outgoing beacons, and set a filter that validates incoming beacons. Beacons are sent and received asynchronously in the background. </p>
<p> This class replaces zbeacon_v2, and is meant for applications that use the CZMQ v3 API (meaning, zsock).</p>
<h2>Example</h2>
<p><code>From zbeacon_test method</code>. </p>
<pre><code>//  Test 1 - two beacons, one speaking, one listening
//  Create speaker beacon to broadcast our service
zactor_t *speaker = zactor_new(zbeacon, NULL);
assert(speaker);
if (verbose)
    zstr_sendx(speaker, &quot;VERBOSE&quot;, NULL);

zsock_send(speaker, &quot;si&quot;, &quot;CONFIGURE&quot;, 9999);
char *hostname = zstr_recv(speaker);
if (!*hostname) {
    printf(&quot;OK (skipping test, no UDP broadcasting)
&quot;);
    zactor_destroy(&amp;speaker);
    free(hostname);
    return;
}
free(hostname);

//  Create listener beacon on port 9999 to lookup service
zactor_t *listener = zactor_new(zbeacon, NULL);
assert(listener);
if (verbose)
    zstr_sendx(listener, &quot;VERBOSE&quot;, NULL);
zsock_send(listener, &quot;si&quot;, &quot;CONFIGURE&quot;, 9999);
hostname = zstr_recv(listener);
assert(*hostname);
free(hostname);

//  We will broadcast the magic value 0xCAFE
byte announcement[2] = {0xCA, 0xFE};
zsock_send(speaker, &quot;sbi&quot;, &quot;PUBLISH&quot;, announcement, 2, 100);
//  We will listen to anything (empty subscription)
zsock_send(listener, &quot;sb&quot;, &quot;SUBSCRIBE&quot;, &quot;&quot;, 0);

//  Wait for at most 1/2 second if there's no broadcasting
zsock_set_rcvtimeo(listener, 500);
char *ipaddress = zstr_recv(listener);
if (ipaddress) {
    zframe_t *content = zframe_recv(listener);
    assert(zframe_size(content) == 2);
    assert(zframe_data(content)[0] == 0xCA);
    assert(zframe_data(content)[1] == 0xFE);
    zframe_destroy(&amp;content);
    zstr_free(&amp;ipaddress);
    zstr_sendx(speaker, &quot;SILENCE&quot;, NULL);
}
zactor_destroy(&amp;listener);
zactor_destroy(&amp;speaker);

//  Test subscription filter using a 3-node setup
zactor_t *node1 = zactor_new(zbeacon, NULL);
assert(node1);
zsock_send(node1, &quot;si&quot;, &quot;CONFIGURE&quot;, 5670);
hostname = zstr_recv(node1);
assert(*hostname);
free(hostname);

zactor_t *node2 = zactor_new(zbeacon, NULL);
assert(node2);
zsock_send(node2, &quot;si&quot;, &quot;CONFIGURE&quot;, 5670);
hostname = zstr_recv(node2);
assert(*hostname);
free(hostname);

zactor_t *node3 = zactor_new(zbeacon, NULL);
assert(node3);
zsock_send(node3, &quot;si&quot;, &quot;CONFIGURE&quot;, 5670);
hostname = zstr_recv(node3);
assert(*hostname);
free(hostname);

zsock_send(node1, &quot;sbi&quot;, &quot;PUBLISH&quot;, &quot;NODE/1&quot;, 6, 250);
zsock_send(node2, &quot;sbi&quot;, &quot;PUBLISH&quot;, &quot;NODE/2&quot;, 6, 250);
zsock_send(node3, &quot;sbi&quot;, &quot;PUBLISH&quot;, &quot;RANDOM&quot;, 6, 250);
zsock_send(node1, &quot;sb&quot;, &quot;SUBSCRIBE&quot;, &quot;NODE&quot;, 4);

//  Poll on three API sockets at once
zpoller_t *poller = zpoller_new(node1, node2, node3, NULL);
assert(poller);
int64_t stop_at = zclock_mono() + 1000;
while (zclock_mono() &lt; stop_at) {
    long timeout = (long)(stop_at - zclock_mono());
    if (timeout &lt; 0)
        timeout = 0;
    void *which = zpoller_wait(poller, timeout * ZMQ_POLL_MSEC);
    if (which) {
        assert(which == node1);
        char *ipaddress, *received;
        zstr_recvx(node1, &amp;ipaddress, &amp;received, NULL);
        assert(streq(received, &quot;NODE/2&quot;));
        zstr_free(&amp;ipaddress);
        zstr_free(&amp;received);
    }
}
zpoller_destroy(&amp;poller);

//  Stop listening
zstr_sendx(node1, &quot;UNSUBSCRIBE&quot;, NULL);

//  Stop all node broadcasts
zstr_sendx(node1, &quot;SILENCE&quot;, NULL);
zstr_sendx(node2, &quot;SILENCE&quot;, NULL);
zstr_sendx(node3, &quot;SILENCE&quot;, NULL);

//  Destroy the test nodes
zactor_destroy(&amp;node1);
zactor_destroy(&amp;node2);
zactor_destroy(&amp;node3);
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
