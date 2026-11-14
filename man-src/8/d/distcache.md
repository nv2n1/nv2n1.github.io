---
title: "distcache(8)"
name: "distcache"
section: "8"
letter: "d"
url: "/docs/linux/man/8-distcache/"
description: "distcache – Distributed session caching"
---

<p>distcache &#8211; Distributed session caching</p>
<h2>Description</h2>
<p>The distcache architecture provides a protocol and set of accompanying tools to allow applications, and indeed machines, to share session state between them by way of a network service. </p>
<p> The primary use of distcache right now is <font SIZE="-1">SSL/TLS</font> session caching. This allows <font SIZE="-1">SSL/TLS</font> servers (eg. a secure Apache web server providing <font SIZE="-1">HTTPS</font> support) to use a centralised session cache, i.e any server may resume <font SIZE="-1">SSL/TLS</font> sessions negotiated by any other server on the network. The advantages to this approach include increased freedom of mechanisms for load-balancing.</p>
<h2>Existing <font SIZE="-1">SSL/TLS</font> load-balancing solutions</h2>
<p>Many load-balancers attempt to route incoming connections to servers based on remembering the last mapping from the same source network address. Others, called &#8220;<font SIZE="-1">SSL</font> sticky&#8221; load-balancers, attempt to parse <font SIZE="-1">SSL/TLS</font> session ids from handshake messages and so map future session-resume attempts. Both methods have serious weaknesses &#8211; the former is generally confused by any form of network address translation (eg. when clients are behind masquerading gateways), and the latter is confused by any <font SIZE="-1">SSL/TLS</font> renegotiations. Moreover both are stateful and a potential bottleneck, because there is no obvious way to scale the architecture to multiple load-balancers.</p>
<h2>Arbitrary <font SIZE="-1">SSL/TLS</font> load-balancing with distcache</h2>
<p>There is no need nor motivation to route incoming connections to &#8220;the same server&#8221; to improve the chances for <font SIZE="-1">SSL/TLS</font> session resumption, and indeed doing so defeats the point of load-balancing (which is to balance according load or availability). The use of distcache is to ensure that all servers share the same &#8220;cache&#8221; and so can respond to <font SIZE="-1">SSL/TLS</font> session resume requests irrespective of where the previous <font SIZE="-1">SSL/TLS</font> connection from the same client was mapped to.</p>
<h2> ain&#8217;t just for <font SIZE="-1">SSL/TLS</font> &#8230;</h2>
<p>Future versions of distcache will expand on the protocol and should provide for a variety of &#8220;shared-state&#8221; uses besides <font SIZE="-1">SSL/TLS</font> session caching. The possibilities include application state caching, network-based shared virtual memory, etc.</p>
<h2>Tools</h2>
<dl>
<dt><code>dc_server</code></p>
<dd>Runs a cache server listening on a configurable network address. See <i><a href="/docs/linux/man/1-dc_server/">dc_server</a></i>(1).</p>
<dt><code>dc_client</code></p>
<dd>Runs a local client proxy. From the point of view of applications this behaves like <code>dc_server</code>, but manages multiplexing application requests to/from a cache server over a single persistent connection. See <i><a href="/docs/linux/man/1-dc_client/">dc_client</a></i>(1).</p>
<dt><code>dc_test</code></p>
<dd>Sends a (configurable) barrage of session caching requests to a given network address using the distcache protocol. Useful for testing correctness of an installation as well as benchmarking. Can be used directly against an instance of <code>dc_server</code> or against a <code>dc_client</code> proxy. See <i><a href="/docs/linux/man/1-dc_test/">dc_test</a></i>(1).</p>
<dt><code>dc_snoop</code></p>
<dd>A transparent proxy tool supporting the distcache protocol that can be used to monitor cache operation requests and responses between any two end-points (eg. between an application and <code>dc_client</code>, or between <code>dc_client</code> and <code>dc_server</code>). See <i><a href="/docs/linux/man/1-dc_snoop/">dc_snoop</a></i>(1).</dl>
<h2>Apis</h2>
<p>The comments below provide a short summary of the APIs available in distcache. To view more details, consult the section 2 man pages these summaries refer to. If you are using a packaged version of distcache, you may need to ensure that a corresponding &#8220;devel&#8221; package is installed as the libraries, headers, and <font SIZE="-1">API</font> documentation is often packaged independantly of the user tools.</p>
<h2>libnal</h2>
<p>This is the underlying Network Abstraction Library (hence &#8220;<font SIZE="-1">NAL</font>&#8221;) used by the distcache libraries and tools. libnal uses non-blocking sockets, with an addressing abstraction that allows tools to transparently work over unix domain sockets or TCP/IPv4 sockets by a change of address text. For this reason, all the distcache tools can have their &#8220;-listen&#8221; and &#8220;-connect&#8221; switches set to work over either kind of transport. </p>
<p> libnal defines various object types;</p>
<dl>
<dt><font SIZE="-1">NAL_ADDRESS</font> (see <i><a href="/docs/linux/man/2-nal_address_new/">NAL_ADDRESS_new</a></i>(2))</p>
<dd>The addressing abstraction converts to and from text representations, indicates whether given addresses are valid for listening on, connecting to, or both.</p>
<dt><font SIZE="-1">NAL_CONNECTION</font> (see <i><a href="/docs/linux/man/2-nal_connection_new/">NAL_CONNECTION_new</a></i>(2))</p>
<dd>This encapsulates a network connection that can be used for sending and receiving arbitrary binary data.</p>
<dt><font SIZE="-1">NAL_LISTENER</font> (see <i><a href="/docs/linux/man/2-nal_listener_new/">NAL_LISTENER_new</a></i>(2))</p>
<dd>This encapsulates a listening socket that can be used to accept incoming connection requests on a configured address, creating a <font SIZE="-1">NAL_CONNECTION</font> wrapper for each accepted connection.</p>
<dt><font SIZE="-1">NAL_SELECTOR</font> (see <i><a href="/docs/linux/man/2-nal_selector_new/">NAL_SELECTOR_new</a></i>(2))</p>
<dd>This provides an object that can be prepared with various <font SIZE="-1">NAL_LISTENER</font> and <font SIZE="-1">NAL_CONNECTION</font> objects, and then can block waiting for network activity up to some configurable limit of time. This is the basis of non-blocking I/O and is an encapsulation of the traditional <i><a href="/docs/linux/man/2-select/">select</a></i>(2) function.</p>
<dt><font SIZE="-1">NAL_BUFFER</font> (see <i><a href="/docs/linux/man/2-nal_buffer_new/">NAL_BUFFER_new</a></i>(2))</p>
<dd>This abstraction implements a <font SIZE="-1">FIFO</font> data array and is used primarily for representing the read and send parts of a <font SIZE="-1">NAL_CONNECTION</font> object.</dl>
<p> There are also some helper functions to assist in serialising data, particularly with respect to putting integral data into network byte order (allowing interoperability between platforms with differing byte-order). These functions are documented in <i><a href="/docs/linux/man/2-nal_decode_uint32/">NAL_decode_uint32</a></i>(2).</p>
<h2>libdistcache</h2>
<p>There are two APIs implemented by the <code>libdistcache</code> library;</p>
<dl>
<dt>distcache/dc_plug.h</p>
<dd>This header provides the <font SIZE="-1">DC_PLUG</font> abstraction. This encapsulates a connection and implements the distcache protocol and various functions for manipulating the reading and writing of distcache messages (requests or responses). This abstraction can support client and server implementations of the distcache protocol and supports asynchronous behaviour by interacting with <i>libnal</i>&#8216;s <font SIZE="-1">NAL_SELECTOR</font> type. For more information, see <i><a href="/docs/linux/man/2-dc_plug_new/">DC_PLUG_new</a></i>(2).</p>
<dt>distcache/dc_client.h</p>
<dd>This header declares a higher-level (and much simpler) <font SIZE="-1">API</font> than dc_plug.h, and is useful in applications that want <font SIZE="-1">API</font> functions that &#8220;do cache operations&#8221;. The <font SIZE="-1">API</font> is blocking, and provides simplistic &#8220;add&#8221;, &#8220;remove&#8221;, and &#8220;get&#8221; functions that only return once the full request/response cycle is complete or an error has occured. This is the <font SIZE="-1">API</font> used to add distcache support to applications like Apache, stunnel, etc. For more information, see <i><a href="/docs/linux/man/2-dc_ctx_new/">DC_CTX_new</a></i>(2).</dl>
<h2>libdistcacheserver</h2>
<p>This header declares an <font SIZE="-1">API</font> for implementing a session cache supporting the distcache protocol. It is primarily intended for environments that wish to implement an alternative method for session storage. As with elements of <i>libdistcache</i>, this <font SIZE="-1">API</font> is likely to be undergoing some important restructuring and enhancements. Please consider subscribing to the distcache mail list and/or monitoring <font SIZE="-1">CVS</font>, this gives you an opportunity to influence ongoing development and be less surprised at changes the turn up in future versions. For more information, see <i><a href="/docs/linux/man/2-dc_server_new/">DC_SERVER_new</a></i>(2).</p>
<h2>License</h2>
<p>The <i>distcache</i> toolkit, including the <i>libnal</i> network abstraction library that comes bundled with it, is distributed under the <font SIZE="-1">LGPL</font> license (&#8220;Library <font SIZE="-1">GNU</font> Public License&#8221;) and you should have received a copy of this license with this software and its documents.</p>
<h2>Bugs</h2>
<p>Quite possibly. In particular, portability has not been tested under many platforms as the current developers have limited <font SIZE="-1">OS</font> resources. Feedback, access to alternative platforms, bug-reports, and questions are all welcome &#8211; please go to the distcache website and subscribe to the distcache-users mail list.</p>
<h2>See Also</h2>
<dl>
<dt><i><a href="/docs/linux/man/1-dc_server/">dc_server</a></i>(1)</p>
<dd>Distributed caching server.</p>
<dt><i><a href="/docs/linux/man/1-dc_client/">dc_client</a></i>(1)</p>
<dd>Distributed caching client proxy</p>
<dt><i><a href="/docs/linux/man/1-dc_snoop/">dc_snoop</a></i>(1)</p>
<dd>Distcache protocol analyser and debugging tool.</p>
<dt><i><a rel="nofollow" href="http://www.distcache.org/">http://www.distcache.org/</a></i></p>
<dd>Distcache home page.</dl>
<h2>Author</h2>
<p>This toolkit was designed and implemented by Geoff Thorpe for Cryptographic Appliances Incorporated. Since the project was released into open source, it has a home page and a project environment where development, mailing lists, and releases are organised. For problems with the software or this man page please check for new releases at the project web-site below, mail the users mailing list described there, or contact the author at <i>geoff [at] geoffthorpe.net</i>. </p>
<p> Home Page: <i><a rel="nofollow" href="http://www.distcache.org">http://www.distcache.org</a></i></p>
