---
title: "brlapi_fd_mutex(3)"
name: "brlapi_fd_mutex"
section: "3"
letter: "b"
url: "/docs/linux/man/3-brlapi_fd_mutex/"
description: "BrlAPI’s protocol –"
---

<h2 class="name">NAME</h2>
<p> BrlAPI&#8217;s protocol &#8211; </p>
<p> Instructions and constants for <i>BrlAPI</i> &#8216;s protocol.</p>
<h3>Data Structures</h3>
<p> struct <code>brlapi_header_t</code> </p>
<p> struct <code>brlapi_versionPacket_t</code> </p>
<p> struct <code>brlapi_authClientPacket_t</code> </p>
<p> struct <code>brlapi_authServerPacket_t</code> </p>
<p> struct <code>brlapi_errorPacket_t</code> </p>
<p> struct <code>brlapi_getDriverSpecificModePacket_t</code> </p>
<p> struct <code>brlapi_writeArgumentsPacket_t</code> </p>
<p> union <code>brlapi_packet_t</code> </p>
<h3>Macros</h3>
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
<p> ssize_t <code>brlapi_writePacket</code> (<code>brlapi_fileDescriptor</code> fd, <code>brlapi_packetType_t</code> type, const void *buf, size_t size) </p>
<p> ssize_t <code>brlapi_readPacketHeader</code> (<code>brlapi_fileDescriptor</code> fd, <code>brlapi_packetType_t</code> *packetType) </p>
<p> ssize_t <code>brlapi_readPacketContent</code> (<code>brlapi_fileDescriptor</code> fd, size_t packetSize, void *buf, size_t bufSize) </p>
<p> ssize_t <code>brlapi_readPacket</code> (<code>brlapi_fileDescriptor</code> fd, <code>brlapi_packetType_t</code> *type, void *buf, size_t size) </p>
<h3>Variables</h3>
<p> pthread_mutex_t <code>brlapi_fd_mutex</code> </p>
<h2>Detailed Description</h2>
<p> These are defines for the protocol between <i>BrlAPI</i> &#8216;s server and clients. Understanding is not needed to use the <i>BrlAPI</i> library, so reading this is not needed unless really wanting to connect to <i>BrlAPI</i> without <i>BrlAPI</i> &#8216;s library.</p>
<h2>Macro Definition Documentation</h2>
<h3>#define BRLAPI_AUTH_CRED &#8216;C&#8217;</h3>
<p> Explicit socket credentials authorization</p>
<h3>#define BRLAPI_AUTH_KEY &#8216;K&#8217;</h3>
<p> Key authorization</p>
<h3>#define BRLAPI_AUTH_NONE &#8216;N&#8217;</h3>
<p> No or implicit authorization</p>
<h3>#define BRLAPI_DEVICE_MAGIC (0xdeadbeefL)</h3>
<p> Magic number to give when sending a BRLPACKET_ENTERRAWMODE or BRLPACKET_SUSPEND packet</p>
<h3>#define BRLAPI_HEADERSIZE sizeof(<code>brlapi_header_t</code>)</h3>
<p> Size of packet headers</p>
<h3>#define BRLAPI_MAXPACKETSIZE 512</h3>
<p> Maximum packet size for packets exchanged on sockets and with braille terminal</p>
<h3>#define BRLAPI_PACKET_ACCEPTKEYRANGES &#8216;u&#8217;</h3>
<p> Unmask key ranges</p>
<h3>#define BRLAPI_PACKET_ACK &#8216;A&#8217;</h3>
<p> Acknowledgement</p>
<h3>#define BRLAPI_PACKET_AUTH &#8216;a&#8217;</h3>
<p> Authorization</p>
<h3>#define BRLAPI_PACKET_ENTERRAWMODE &#8216;*&#8217;</h3>
<p> Enter in raw mode</p>
<h3>#define BRLAPI_PACKET_ENTERTTYMODE &#8216;t&#8217;</h3>
<p> Asks for a specified tty</p>
<h3>#define BRLAPI_PACKET_ERROR &#8216;e&#8217;</h3>
<p> non-fatal error</p>
<h3>#define BRLAPI_PACKET_EXCEPTION &#8216;E&#8217;</h3>
<p> Exception</p>
<h3>#define BRLAPI_PACKET_GETDISPLAYSIZE &#8216;s&#8217;</h3>
<p> Dimensions of brl display</p>
<h3>#define BRLAPI_PACKET_GETDRIVERNAME &#8216;n&#8217;</h3>
<p> Ask which driver is used</p>
<h3>#define BRLAPI_PACKET_IGNOREKEYRANGES &#8216;m&#8217;</h3>
<p> Mask key ranges</p>
<h3>#define BRLAPI_PACKET_KEY &#8216;k&#8217;</h3>
<p> Braille key</p>
<h3>#define BRLAPI_PACKET_LEAVERAWMODE &#8216;#&#8217;</h3>
<p> Leave raw mode</p>
<h3>#define BRLAPI_PACKET_LEAVETTYMODE &#8216;L&#8217;</h3>
<p> Release the tty</p>
<h3>#define BRLAPI_PACKET_PACKET &#8216;p&#8217;</h3>
<p> Raw packets</p>
<h3>#define BRLAPI_PACKET_RESUMEDRIVER &#8216;R&#8217;</h3>
<p> Resume driver</p>
<h3>#define BRLAPI_PACKET_SETFOCUS &#8216;F&#8217;</h3>
<p> Set current tty focus</p>
<h3>#define BRLAPI_PACKET_SUSPENDDRIVER &#8216;S&#8217;</h3>
<p> Suspend driver</p>
<h3>#define BRLAPI_PACKET_VERSION &#8216;v&#8217;</h3>
<p> Version</p>
<h3>#define BRLAPI_PACKET_WRITE &#8216;w&#8217;</h3>
<p> Write</p>
<h3>#define BRLAPI_PROTOCOL_VERSION ((uint32_t) 8) /** Communication protocol version */</h3>
<h3>#define BRLAPI_WF_ATTR_AND 0X08</h3>
<p> And attributes</p>
<h3>#define BRLAPI_WF_ATTR_OR 0X10</h3>
<p> Or attributes</p>
<h3>#define BRLAPI_WF_CHARSET 0X40</h3>
<p> Charset</p>
<h3>#define BRLAPI_WF_CURSOR 0X20</h3>
<p> Cursor position</p>
<h3>#define BRLAPI_WF_DISPLAYNUMBER 0X01</h3>
<p> Flags for writing Display number</p>
<h3>#define BRLAPI_WF_REGION 0X02</h3>
<p> Region parameter</p>
<h3>#define BRLAPI_WF_TEXT 0X04</h3>
<p> Contains some text</p>
<h2>Function Documentation</h2>
<h3>ssize_t brlapi_readPacket (<code>brlapi_fileDescriptor</code>fd, <code>brlapi_packetType_t</code> *type, void *buf, size_tsize)</h3>
<p> Read a packet from <i>BrlAPI</i> server </p>
<p> This function is for internal use, but one might use it if one really knows what one is doing&#8230; </p>
<p> <i>type</i> is where the function will store the packet type; it should always be one of the above defined BRLPACKET_* (or else something very nasty must have happened :/). </p>
<p> The syntax is the same as read()&#8217;s. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> packet&#8217;s size, -2 if EOF occurred, -1 on error or signal interruption.</dl>
<p> If the packet is larger than the supplied buffer, the buffer will be filled with the beginning of the packet, the rest of the packet being discarded. This follows the semantics of the recv system call when the MSG_TRUNC option is given. </p>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>brlapi_writePacket()</code></dl>
<h3>ssize_t brlapi_readPacketContent (<code>brlapi_fileDescriptor</code>fd, size_tpacketSize, void *buf, size_tbufSize)</h3>
<p> Read the content of a packet from <i>BrlAPI</i> server </p>
<p> This function is for internal use, but one might use it if one really knows what one is doing&#8230; </p>
<p> <i>packetSize</i> is the size announced by <i></i><code>brlapi_readPacketHeader()</code> </p>
<p> <i>bufSize</i> is the size of <i>buf</i> </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> packetSize, -2 if EOF occurred, -1 on error.</dl>
<p> If the packet is larger than the supplied buffer, the buffer will be filled with the beginning of the packet, the rest of the packet being discarded. This follows the semantics of the recv system call when the MSG_TRUNC option is given. </p>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>brlapi_writePacket()</code> <code>brlapi_readPacketHeader()</code> <code>brlapi_readPacket()</code></dl>
<h3>ssize_t brlapi_readPacketHeader (<code>brlapi_fileDescriptor</code>fd, <code>brlapi_packetType_t</code> *packetType)</h3>
<p> Read the header (type+size) of a packet from <i>BrlAPI</i> server </p>
<p> This function is for internal use, but one might use it if one really knows what one is doing&#8230; </p>
<p> <i>type</i> is where the function will store the packet type; it should always be one of the above defined BRLPACKET_* (or else something very nasty must have happened :/). </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> packet&#8217;s size, -2 if EOF occurred, -1 on error or signal interruption.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>brlapi_writePacket()</code> <code>brlapi_readPacketContent</code> <code>brlapi_readPacket</code></dl>
<h3>ssize_t brlapi_writePacket (<code>brlapi_fileDescriptor</code>fd, <code>brlapi_packetType_t</code>type, const void *buf, size_tsize)</h3>
<p> Send a packet to <i>BrlAPI</i> server </p>
<p> This function is for internal use, but one might use it if one really knows what one is doing&#8230; </p>
<p> <i>type</i> should only be one of the above defined BRLPACKET_*. </p>
<p> The syntax is the same as write()&#8217;s. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success, -1 on failure.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>brlapi_readPacketHeader()</code> <code>brlapi_readPacketContent()</code> <code>brlapi_readPacket()</code></dl>
<h2>Variable Documentation</h2>
<h3>pthread_mutex_t brlapi_fd_mutex</h3>
<p> Mutex for protecting concurrent fd access </p>
<p> In order to regulate concurrent access to the library&#8217;s file descriptor and requests to / answers from <i>BrlAPI</i> server, every function of the library locks this mutex, namely </p>
<dl>
<dt>&bull;</p>
<dd> <code>brlapi_openConnection()</code></p>
<dt>&bull;</p>
<dd> <code>brlapi_closeConnection()</code></p>
<dt>&bull;</p>
<dd> <code>brlapi_enterRawMode()</code></p>
<dt>&bull;</p>
<dd> <code>brlapi_leaveRawMode()</code></p>
<dt>&bull;</p>
<dd> <code>brlapi_sendRaw()</code></p>
<dt>&bull;</p>
<dd> <code>brlapi_recvRaw()</code></p>
<dt>&bull;</p>
<dd> brlapi_getDriverId()</p>
<dt>&bull;</p>
<dd> <code>brlapi_getDriverName()</code></p>
<dt>&bull;</p>
<dd> <code>brlapi_getDisplaySize()</code></p>
<dt>&bull;</p>
<dd> <code>brlapi_enterTtyMode()</code></p>
<dt>&bull;</p>
<dd> <code>brlapi_enterTtyModeWithPath()</code></p>
<dt>&bull;</p>
<dd> <code>brlapi_leaveTtyMode()</code></p>
<dt>&bull;</p>
<dd> brlapi_*write*()</p>
<dt>&bull;</p>
<dd> brlapi_(un)?ignorekey(Range|Set)()</p>
<dt>&bull;</p>
<dd> <code>brlapi_readKey()</code></dl>
<p> If both these functions and <code>brlapi_writePacket()</code> or <code>brlapi_readPacket()</code> are used in a multithreaded application, this mutex must be locked before calling <code>brlapi_writePacket()</code> or <code>brlapi_readPacket()</code>, and unlocked afterwards.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for BrlAPI from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbBP">Function Documentation</a></p>
<dd>
<dt><a href="#lbBU">Variable Documentation</a></p>
<dd>
<dt><a href="#lbBW">Author</a></p>
<dd></dl>
