---
title: "pcap-savefile(5)"
name: "pcap-savefile"
section: "5"
letter: "p"
url: "/docs/linux/man/5-pcap-savefile/"
description: "pcap-savefile – libpcap savefile format"
---

<p>pcap-savefile &#8211; libpcap savefile format</p>
<h2>Description</h2>
<p>NOTE: applications and libraries should, if possible, use libpcap to read savefiles, rather than having their own code to read savefiles. If, in the future, a new file format is supported by libpcap, applications and libraries using libpcap to read savefiles will be able to read the new format of savefiles, but applications and libraries using their own code to read savefiles will have to be changed to support the new file format. </p>
<p> &#8220;Savefiles&#8221; read and written by libpcap and applications using libpcap start with a per-file header. The format of the per-file header is:</p>
<dl>
<dd>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=2>Magic number
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>Major version</td>
<td ALIGN=center>Minor version
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=2>Time zone offset
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=2>Time stamp accuracy
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=2>Snapshot length
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=2>Link-layer header type
</td>
</tr>
</table>
</table>
</dl>
<p> All fields in the per-file header are in the byte order of the host writing the file. Normally, the first field in the per-file header is a 4-byte magic number, with the value 0xa1b2c3d4. The magic number, when read by a host with the same byte order as the host that wrote the file, will have the value 0xa1b2c3d4, and, when read by a host with the opposite byte order as the host that wrote the file, will have the value 0xd4c3b2a1. That allows software reading the file to determine whether the byte order of the host that wrote the file is the same as the byte order of the host on which the file is being read, and thus whether the values in the per-file and per-packet headers need to be byte-swapped. </p>
<p> If the magic number has the value 0xa1b23c4d (with the two nibbles of the two lower-order bytes of the magic number swapped), which would be read as 0xa1b23c4d by a host with the same byte order as the host that wrote the file and as 0x4d3cb2a1 by a host with the opposite byte order as the host that wrote the file, the file format is the same as for regular files, except that the time stamps for packets are given in seconds and nanoseconds rather than seconds and microseconds. </p>
<p> Following this are:</p>
<dl>
<dd>A 2-byte file format major version number; the current version number is 2.</p>
<dd>A 2-byte file format minor version number; the current version number is 4.</p>
<dd>A 4-byte time zone offset; this is always 0.</p>
<dd>A 4-byte number giving the accuracy of time stamps in the file; this is always 0.</p>
<dd>A 4-byte number giving the &quot;snapshot length&quot; of the capture; packets longer than the snapshot length are truncated to the snapshot length, so that, if the snapshot length is <i>N</i>, only the first <i>N</i> bytes of a packet longer than <i>N</i> bytes will be saved in the capture.</p>
<dd>a 4-byte number giving the link-layer header type for packets in the capture; see <code><a href="/docs/linux/man/7-pcap-linktype/">pcap-linktype</a></code>(7) for the <code>LINKTYPE_</code> values that can appear in this field.</dl>
<p> Following the per-file header are zero or more packets; each packet begins with a per-packet header, which is immediately followed by the raw packet data. The format of the per-packet header is:</p>
<dl>
<dd>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center>Time stamp, seconds value
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>Time stamp, microseconds or nanoseconds value
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>Length of captured packet data
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>Un-truncated length of the packet data
</td>
</tr>
</table>
</table>
</dl>
<p> All fields in the per-packet header are in the byte order of the host writing the file. The per-packet header begins with a time stamp giving the approximate time the packet was captured; the time stamp consists of a 4-byte value, giving the time in seconds since January 1, 1970, 00:00:00 UTC, followed by a 4-byte value, giving the time in microseconds or nanoseconds since that second, depending on the magic number in the file header. Following that are a 4-byte value giving the number of bytes of captured data that follow the per-packet header and a 4-byte value giving the number of bytes that would have been present had the packet not been truncated by the snapshot length. The two lengths will be equal if the number of bytes of packet data are less than or equal to the snapshot length.</p>
<h2>See Also</h2>
<p><a href="//www.systutorials.com/docs/linux/man/3PCAP-pcap/">pcap</a>(3PCAP), <a href="/docs/linux/man/7-pcap-linktype/">pcap-linktype</a>(7) </p>
