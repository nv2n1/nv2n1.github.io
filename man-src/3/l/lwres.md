---
title: "lwres(3)"
name: "lwres"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lwres/"
description: "lwres – introduction to the lightweight resolver library"
---

<h2 class="name">NAME</h2>
<p> lwres &#8211; introduction to the lightweight resolver library </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;lwres/lwres.h&gt;
</code></pre>
<h2>DESCRIPTION</h2>
<p> The BIND 9 lightweight resolver library is a simple, name service independent stub resolver library. It provides hostname-to-address and address-to-hostname lookup services to applications by transmitting lookup requests to a resolver daemon <code>lwresd</code> running on the local host. The resover daemon performs the lookup using the DNS or possibly other name service protocols, and returns the results to the application through the library. The library and resolver daemon communicate using a simple UDP-based protocol.</p>
<h2>OVERVIEW</h2>
<p> The lwresd library implements multiple name service APIs. The standard <code>gethostbyname()</code>, <code>gethostbyaddr()</code>, <code>gethostbyname_r()</code>, <code>gethostbyaddr_r()</code>, <code>getaddrinfo()</code>, <code>getipnodebyname()</code>, and <code>getipnodebyaddr()</code> functions are all supported. To allow the lwres library to coexist with system libraries that define functions of the same name, the library defines these functions with names prefixed by lwres_. To define the standard names, applications must include the header file <i>&lt;lwres/netdb.h&gt;</i> which contains macro definitions mapping the standard function names into lwres_ prefixed ones. Operating system vendors who integrate the lwres library into their base distributions should rename the functions in the library proper so that the renaming macros are not needed. </p>
<p> The library also provides a native API consisting of the functions <code>lwres_getaddrsbyname()</code> and <code>lwres_getnamebyaddr()</code>. These may be called by applications that require more detailed control over the lookup process than the standard functions provide. </p>
<p> In addition to these name service independent address lookup functions, the library implements a new, experimental API for looking up arbitrary DNS resource records, using the <code>lwres_getaddrsbyname()</code> function. </p>
<p> Finally, there is a low-level API for converting lookup requests and responses to and from raw lwres protocol packets. This API can be used by clients requiring nonblocking operation, and is also used when implementing the server side of the lwres protocol, for example in the <code>lwresd</code> resolver daemon. The use of this low-level API in clients and servers is outlined in the following sections.</p>
<h2>CLIENT-SIDE LOW-LEVEL API CALL FLOW</h2>
<p> When a client program wishes to make an lwres request using the native low-level API, it typically performs the following sequence of actions. </p>
<p> (1) Allocate or use an existing <code>lwres_packet_t</code>, called <i>pkt</i> below. </p>
<p> (2) Set pkt.recvlength to the maximum length we will accept. This is done so the receiver of our packets knows how large our receive buffer is. The &quot;default&quot; is a constant in <i>lwres.h</i>: <code>LWRES_RECVLENGTH = 4096</code>. </p>
<p> (3) Set pkt.serial to a unique serial number. This value is echoed back to the application by the remote server. </p>
<p> (4) Set pkt.pktflags. Usually this is set to 0. </p>
<p> (5) Set pkt.result to 0. </p>
<p> (6) Call <code>lwres_*request_render()</code>, or marshall in the data using the primitives such as <code>lwres_packet_render()</code> and storing the packet data. </p>
<p> (7) Transmit the resulting buffer. </p>
<p> (8) Call <code>lwres_*response_parse()</code> to parse any packets received. </p>
<p> (9) Verify that the opcode and serial match a request, and process the packet specific information contained in the body.</p>
<h2>SERVER-SIDE LOW-LEVEL API CALL FLOW</h2>
<p> When implementing the server side of the lightweight resolver protocol using the lwres library, a sequence of actions like the following is typically involved in processing each request packet. </p>
<p> Note that the same <code>lwres_packet_t</code> is used in both the <code>_parse()</code> and <code>_render()</code> calls, with only a few modifications made to the packet header&#8217;s contents between uses. This method is recommended as it keeps the serial, opcode, and other fields correct. </p>
<p> (1) When a packet is received, call <code>lwres_*request_parse()</code> to unmarshall it. This returns a <code>lwres_packet_t</code> (also called <i>pkt</i>, below) as well as a data specific type, such as <code>lwres_gabnrequest_t</code>. </p>
<p> (2) Process the request in the data specific type. </p>
<p> (3) Set the pkt.result, pkt.recvlength as above. All other fields can be left untouched since they were filled in by the <code>*_parse()</code> call above. If using <code>lwres_*response_render()</code>, pkt.pktflags will be set up properly. Otherwise, the <code>LWRES_LWPACKETFLAG_RESPONSE</code> bit should be set. </p>
<p> (4) Call the data specific rendering function, such as <code>lwres_gabnresponse_render()</code>. </p>
<p> (5) Send the resulting packet to the client. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-lwres_gethostent/">lwres_gethostent</a></code>(3), <code><a href="/docs/linux/man/3-lwres_getipnode/">lwres_getipnode</a></code>(3), <code><a href="/docs/linux/man/3-lwres_getnameinfo/">lwres_getnameinfo</a></code>(3), <code><a href="/docs/linux/man/3-lwres_noop/">lwres_noop</a></code>(3), <code><a href="/docs/linux/man/3-lwres_gabn/">lwres_gabn</a></code>(3), <code><a href="/docs/linux/man/3-lwres_gnba/">lwres_gnba</a></code>(3), <code><a href="/docs/linux/man/3-lwres_context/">lwres_context</a></code>(3), <code><a href="/docs/linux/man/3-lwres_config/">lwres_config</a></code>(3), <code><a href="/docs/linux/man/5-resolver/">resolver</a></code>(5), <code><a href="/docs/linux/man/8-lwresd/">lwresd</a></code>(8).</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2004, 2005, 2007 Internet Systems Consortium, Inc. (&quot;ISC&quot;)<br />
 Copyright &#169; 2000, 2001 Internet Software Consortium. </p>
<h2>Index</h2>
