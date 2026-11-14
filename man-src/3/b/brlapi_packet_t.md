---
title: "brlapi_packet_t(3)"
name: "brlapi_packet_t"
section: "3"
letter: "b"
url: "/docs/linux/man/3-brlapi_packet_t/"
description: "brlapi_packet_t –"
---

<h2 class="name">NAME</h2>
<p> brlapi_packet_t &#8211; </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;brlapi_protocol.h&gt;</p>
<h3>Data Fields</h3>
<p> unsigned char <code>data</code> [<code>BRLAPI_MAXPACKETSIZE</code>] </p>
<p> <code>brlapi_versionPacket_t</code> <code>version</code> </p>
<p> <code>brlapi_authClientPacket_t</code> <code>authClient</code> </p>
<p> <code>brlapi_authServerPacket_t</code> <code>authServer</code> </p>
<p> <code>brlapi_errorPacket_t</code> <code>error</code> </p>
<p> <code>brlapi_getDriverSpecificModePacket_t</code> <code>getDriverSpecificMode</code> </p>
<p> <code>brlapi_writeArgumentsPacket_t</code> <code>writeArguments</code> </p>
<p> uint32_t <code>uint32</code> </p>
<h2>Detailed Description</h2>
<p> Type for packets. Should be used instead of a mere char[], since it has correct alignment requirements.</p>
<h2>Field Documentation</h2>
<h3><code>brlapi_authClientPacket_t</code> brlapi_packet_t::authClient</h3>
<h3><code>brlapi_authServerPacket_t</code> brlapi_packet_t::authServer</h3>
<h3>unsigned char brlapi_packet_t::data[<code>BRLAPI_MAXPACKETSIZE</code>]</h3>
<h3><code>brlapi_errorPacket_t</code> brlapi_packet_t::error</h3>
<h3><code>brlapi_getDriverSpecificModePacket_t</code> brlapi_packet_t::getDriverSpecificMode</h3>
<h3>uint32_t brlapi_packet_t::uint32</h3>
<h3><code>brlapi_versionPacket_t</code> brlapi_packet_t::version</h3>
<h3><code>brlapi_writeArgumentsPacket_t</code> brlapi_packet_t::writeArguments</h3>
<h2>Author</h2>
<p> Generated automatically by Doxygen for BrlAPI from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAO">Author</a></p>
<dd></dl>
