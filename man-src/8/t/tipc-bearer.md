---
title: "tipc-bearer(8)"
name: "tipc-bearer"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tipc-bearer/"
description: "tipc-bearer – show or modify TIPC bearers"
---

<p>tipc-bearer &#8211; show or modify TIPC bearers</p>
<h2>Synopsis</h2>
<p><code>tipc bearer add media udp name</code> <i>NAME </i><code>remoteip </code><i>REMOTEIP</i> </p>
<pre><code>tipc bearer enable

[ domain

DOMAIN ]

[ priority

PRIORITY ]

media


{ { eth | ib } device

    DEVICE }

|


{ udp

    name

    NAME

    localip

    LOCALIP

    [ localport

    LOCALPORT ]

    [ remoteip

    REMOTEIP ]

    [ remoteport

    REMOTEPORT ] }
tipc bearer disable media


{ { eth | ib } device

    DEVICE }

|


{ udp

    name

    NAME }
tipc bearer set

{ priority

    PRIORITY

    | tolerance

    TOLERANCE

    | window

    WINDOW

} media


{ { eth | ib } device

    DEVICE }

|


{ udp

    name

    NAME }
tipc bearer get

[ priority | tolerance | window ] media


{ { eth | ib } device

    DEVICE }

|


{ udp

    name

    NAME

    [ localip | localport | remoteip | remoteport ] }</code></pre>
<p> <code>tipc bearer list</code> </p>
<h2>Options</h2>
<p>Options (flags) that can be passed anywhere in the command chain.</p>
<dl>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd>Show help about last valid command. For example <code>tipc bearer &#8211;help</code> will show bearer help and <code>tipc &#8211;help</code> will show general help. The position of the option in the string is irrelevant.</dl>
<h2>Description</h2>
<h3>Bearer identification</h3>
<dl>
<dt><code>media </code><i>MEDIA</i></p>
<dd>Specifies the TIPC media type for a particular bearer to operate on. Different media types have different ways of identifying a unique bearer. For example, <code>ib </code>and <code>eth</code> identify a bearer with a <i>DEVICE</i> while <code>udp</code> identify a bearer with a <i>LOCALIP </i>and a <i>NAME</i> <code>ib</code> &#8211; Infiniband <code>eth</code> &#8211; Ethernet <code>udp</code> &#8211; User Datagram Protocol (UDP)</p>
<dt><code>name </code><i>NAME</i></p>
<dd>Logical bearer identifier valid for bearers on <code>udp</code> media.</p>
<dt><code>device </code><i>DEVICE</i></p>
<dd>Physical bearer device valid for bearers on <code>eth</code> and <code>ib</code> media.</dl>
<h3>Bearer properties</h3>
<dl>
<dt><code>domain</code></p>
<dd>The addressing domain (region) in which a bearer will establish links and accept link establish requests.</p>
<dt><code>priority</code></p>
<dd>Default link priority inherited by all links subsequently established over a bearer. A single bearer can only host one link to a particular node. This means the default link priority for a bearer typically affects which bearer to use when communicating with a particular node in an multi bearer setup. For more info about link priority see <code><a href="/docs/linux/man/8-tipc-link/">tipc-link</a></code>(8)</p>
<dt><code>tolerance</code></p>
<dd>Default link tolerance inherited by all links subsequently established over a bearer. For more info about link tolerance see <code><a href="/docs/linux/man/8-tipc-link/">tipc-link</a></code>(8)</p>
<dt><code>window</code></p>
<dd>Default link window inherited by all links subsequently established over a bearer. For more info about the link window size see <code><a href="/docs/linux/man/8-tipc-link/">tipc-link</a></code>(8)</dl>
<h3>UDP bearer options</h3>
<dl>
<dt><code>localip </code><i>LOCALIP</i></p>
<dd>Specify a local IP v4/v6 address for a <code>udp</code> bearer.</p>
<dt><code>localport </code><i>LOCALPORT</i></p>
<dd>Specify the local port for a <code>udp</code> bearer. The default port 6118 is used if no port is specified.</p>
<dt><code>remoteip </code><i>REMOTEIP</i></p>
<dd>Specify a remote IP for a <code>udp</code> bearer. If no remote IP is specified a <code>udp</code> bearer runs in multicast mode and tries to auto-discover its neighbours. The multicast IP address is generated based on the TIPC network ID. If a remote IP is specified the <code>udp</code> bearer runs in point-to-point mode. Multiple <code>remoteip</code> addresses can be added via the <code>bearer add</code> command. Adding one or more unicast <code>remoteip</code> addresses to an existing <code>udp</code> bearer puts the bearer in replicast mode where IP multicast is emulated by sending multiple unicast messages to each configured <code>remoteip.</code> When a peer sees a TIPC discovery message from an unknown peer the peer address is automatically added to the <code>remoteip</code> (replicast) list, thus only one side of a link needs to be manually configured. A <code>remoteip</code> address cannot be added to a multicast bearer.</p>
<dt><code>remoteport </code><i>REMOTEPORT</i></p>
<dd>Specify the remote port for a <code>udp</code> bearer. The default port 6118 is used if no port is specified. </p>
<h2>Exit Status</h2>
<p>Exit status is 0 if command was successful or a positive integer upon failure.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tipc/">tipc</a></code>(8), <code><a href="/docs/linux/man/8-tipc-link/">tipc-link</a></code>(8), <code><a href="/docs/linux/man/8-tipc-media/">tipc-media</a></code>(8), <code><a href="/docs/linux/man/8-tipc-nametable/">tipc-nametable</a></code>(8), <code><a href="/docs/linux/man/8-tipc-node/">tipc-node</a></code>(8), <code><a href="/docs/linux/man/8-tipc-peer/">tipc-peer</a></code>(8), <code><a href="/docs/linux/man/8-tipc-socket/">tipc-socket</a></code>(8)</p>
<h2>Reporting Bugs</h2>
<p>Report any bugs to the Network Developers mailing list <code>&lt;netdev [at] vger.kernel.org&gt;</code> where the development and maintenance is primarily done. You do not have to be subscribed to the list to send a message there.</p>
<h2>Author</h2>
<p>Richard Alpe &lt;richard.alpe [at] ericsson.com&gt;</p>
