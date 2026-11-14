---
title: "brlapi_protocol-h(3)"
name: "brlapi_protocol-h"
section: "3"
letter: "b"
url: "/docs/linux/man/3-brlapi_protocol-h/"
description: "brlapi_protocol.h –"
---

<p>brlapi_protocol.h &#8211; </p>
<p> types and constants for <i>BrlAPI&#8217;s</i> protocol</p>
<h2>Synopsis</h2>
<p>#include &#8216;brlapi.h&#8217;<br />
 #include &lt;inttypes.h&gt;<br />
 #include &lt;unistd.h&gt;<br />
 #include &lt;pthread.h&gt; </p>
<h3>Data Structures</h3>
<p>struct <code>brlapi_header_t</code> </p>
<p> struct <code>brlapi_versionPacket_t</code> </p>
<p> struct <code>brlapi_authClientPacket_t</code> </p>
<p> struct <code>brlapi_authServerPacket_t</code> </p>
<p> struct <code>brlapi_errorPacket_t</code> </p>
<p> struct <code>brlapi_getDriverSpecificModePacket_t</code> </p>
<p> struct <code>brlapi_writeArgumentsPacket_t</code> </p>
<p> union <code>brlapi_packet_t</code> </p>
<h3>Macros</h3>
<p>#define <code>UINT32_MAX</code> (4294967295U) </p>
<p> #define <code>BRLAPI_PROTOCOL_VERSION</code> ((uint32_t) 8) /** Communication protocol version */ </p>
<p> #define <code>BRLAPI_MAXPACKETSIZE</code> 512 </p>
<p> #define <code>BRLAPI_PACKET_VERSION</code> &#8216;v&#8217; </p>
<p> #define <code>BRLAPI_PACKET_AUTH</code> &#8216;a&#8217; </p>
<p> #define <code>BRLAPI_PACKET_GETDRIVERNAME</code> &#8216;n&#8217; </p>
<p> #define <code>BRLAPI_PACKET_GETDISPLAYSIZE</code> &#8216;s&#8217; </p>
<p> #define <code>BRLAPI_PACKET_ENTERTTYMODE</code> &#8216;t&#8217; </p>
<p> #define <code>BRLAPI_PACKET_SETFOCUS</code> &#8216;F&#8217; </p>
<p> #define <code>BRLAPI_PACKET_LEAVETTYMODE</code> &#8216;L&#8217; </p>
<p> #define <code>BRLAPI_PACKET_KEY</code> &#8216;k&#8217; </p>
<p> #define <code>BRLAPI_PACKET_IGNOREKEYRANGES</code> &#8216;m&#8217; </p>
<p> #define <code>BRLAPI_PACKET_ACCEPTKEYRANGES</code> &#8216;u&#8217; </p>
<p> #define <code>BRLAPI_PACKET_WRITE</code> &#8216;w&#8217; </p>
<p> #define <code>BRLAPI_PACKET_ENTERRAWMODE</code> &#8216;*&#8217; </p>
<p> #define <code>BRLAPI_PACKET_LEAVERAWMODE</code> &#8216;#&#8217; </p>
<p> #define <code>BRLAPI_PACKET_PACKET</code> &#8216;p&#8217; </p>
<p> #define <code>BRLAPI_PACKET_ACK</code> &#8216;A&#8217; </p>
<p> #define <code>BRLAPI_PACKET_ERROR</code> &#8216;e&#8217; </p>
<p> #define <code>BRLAPI_PACKET_EXCEPTION</code> &#8216;E&#8217; </p>
<p> #define <code>BRLAPI_PACKET_SUSPENDDRIVER</code> &#8216;S&#8217; </p>
<p> #define <code>BRLAPI_PACKET_RESUMEDRIVER</code> &#8216;R&#8217; </p>
<p> #define <code>BRLAPI_DEVICE_MAGIC</code> (0xdeadbeefL) </p>
<p> #define <code>BRLAPI_HEADERSIZE</code> sizeof(<code>brlapi_header_t</code>) </p>
<p> #define <code>BRLAPI_AUTH_NONE</code> &#8216;N&#8217; </p>
<p> #define <code>BRLAPI_AUTH_KEY</code> &#8216;K&#8217; </p>
<p> #define <code>BRLAPI_AUTH_CRED</code> &#8216;C&#8217; </p>
<p> #define <code>BRLAPI_WF_DISPLAYNUMBER</code> 0X01 </p>
<p> #define <code>BRLAPI_WF_REGION</code> 0X02 </p>
<p> #define <code>BRLAPI_WF_TEXT</code> 0X04 </p>
<p> #define <code>BRLAPI_WF_ATTR_AND</code> 0X08 </p>
<p> #define <code>BRLAPI_WF_ATTR_OR</code> 0X10 </p>
<p> #define <code>BRLAPI_WF_CURSOR</code> 0X20 </p>
<p> #define <code>BRLAPI_WF_CHARSET</code> 0X40 </p>
<h3>Functions</h3>
<p>ssize_t <code>brlapi_writePacket</code> (<code>brlapi_fileDescriptor</code> fd, <code>brlapi_packetType_t</code> type, const void *buf, size_t size) </p>
<p> ssize_t <code>brlapi_readPacketHeader</code> (<code>brlapi_fileDescriptor</code> fd, <code>brlapi_packetType_t</code> *packetType) </p>
<p> ssize_t <code>brlapi_readPacketContent</code> (<code>brlapi_fileDescriptor</code> fd, size_t packetSize, void *buf, size_t bufSize) </p>
<p> ssize_t <code>brlapi_readPacket</code> (<code>brlapi_fileDescriptor</code> fd, <code>brlapi_packetType_t</code> *type, void *buf, size_t size) </p>
<h3>Variables</h3>
<p>pthread_mutex_t <code>brlapi_fd_mutex</code> </p>
<h2>Macro Definition Documentation</h2>
<h3>#define UINT32_MAX (4294967295U)</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for BrlAPI from the source code.</p>
