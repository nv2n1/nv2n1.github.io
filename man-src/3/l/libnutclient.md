---
title: "libnutclient(3)"
name: "libnutclient"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libnutclient/"
description: "libnutclient – Network UPS Tools high-level client access library"
---

<h2 class="name">NAME</h2>
<p> libnutclient &#8211; Network UPS Tools high-level client access library </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;nutclient.h&gt;
</code></pre>
<pre>
Refer to this file for more information.
</pre>
<h2>DESCRIPTION</h2>
<p> The Network UPS Tools (NUT) <code>nutclient</code> library provides a number of useful functions for programs to use when communicating with <code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8). It provides high-level representation of NUT data through client connection, devices, variables and commands. Unlike <code><a href="/docs/linux/man/3-upsclient/">upsclient</a></code>(3), all low-level protocol details are hidden. </p>
<p> State is maintained across calls in an opaque structure called NUTCLIENT_t. Callers are expected to create one per client connection. These will be provided to most of the <code>nutclient</code> functions. The format of this structure is subject to change, and client programs must not reference elements within it directly. </p>
<p> NUTCLIENT_t represents the common connection information. Derived versions exist for each connection type (NUTCLIENT_TCP_t for TCP connection; actually the unique connection type, NUTCLIENT_TCP_t can be passed as NUTCLIENT_t parameter). </p>
<p> See the nutclient.h header for more information.</p>
<h2>ERROR HANDLING</h2>
<p> There is currently no specific mechanism around error handling.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libnutclient_devices/">libnutclient_devices</a></code>(3) <code><a href="/docs/linux/man/3-libnutclient_commands/">libnutclient_commands</a></code>(3) <code><a href="/docs/linux/man/3-libnutclient_general/">libnutclient_general</a></code>(3) <code><a href="/docs/linux/man/3-libnutclient_misc/">libnutclient_misc</a></code>(3) <code><a href="/docs/linux/man/3-libnutclient_tcp/">libnutclient_tcp</a></code>(3) <code><a href="/docs/linux/man/3-libnutclient_variables/">libnutclient_variables</a></code>(3) </p>
<h2>Index</h2>
