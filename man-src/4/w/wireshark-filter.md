---
title: "wireshark-filter(4)"
name: "wireshark-filter"
section: "4"
letter: "w"
url: "/docs/linux/man/4-wireshark-filter/"
description: "wireshark-filter – Wireshark filter syntax and reference"
---

<p>wireshark-filter &#8211; Wireshark filter syntax and reference</p>
<h2>Synopsis</h2>
<p><code>wireshark</code> [other options] [&nbsp;<wbr><code>-R</code>&nbsp;<wbr>&#8220;filter expression&#8221;&nbsp;<wbr>] </p>
<p> <code>tshark</code> [other options] [&nbsp;<wbr><code>-R</code>&nbsp;<wbr>&#8220;filter expression&#8221;&nbsp;<wbr>]</p>
<h2>Description</h2>
<p><code>Wireshark</code> and <code>TShark</code> share a powerful filter engine that helps remove the noise from a packet trace and lets you see only the packets that interest you. If a packet meets the requirements expressed in your filter, then it is displayed in the list of packets. Display filters let you compare the fields within a protocol against a specific value, compare fields against fields, and check the existence of specified fields or protocols. </p>
<p> Filters are also used by other features such as statistics generation and packet list colorization (the latter is only available to <code>Wireshark</code>). This manual page describes their syntax. A comprehensive reference of filter fields can be found within Wireshark and in the display filter reference at &lt;<a rel="nofollow" href="http://www.wireshark.org/docs/dfref/">http://www.wireshark.org/docs/dfref/</a>&gt;.</p>
<h2>Filter Syntax</h2>
<h3>Check whether a field or protocol exists</h3>
<p>The simplest filter allows you to check for the existence of a protocol or field. If you want to see all packets which contain the <font SIZE="-1">IP</font> protocol, the filter would be &#8220;ip&#8221; (without the quotation marks). To see all packets that contain a Token-Ring <font SIZE="-1">RIF</font> field, use &#8220;tr.rif&#8221;. </p>
<p> Think of a protocol or field in a filter as implicitly having the &#8220;exists&#8221; operator.</p>
<h3>Comparison operators</h3>
<p>Fields can also be compared against values. The comparison operators can be expressed either through English-like abbreviations or through C-like symbols: </p>
<pre> eq, == Equal
 ne, != Not Equal
 gt, &gt; Greater Than
 lt, &lt; Less Than
 ge, &gt;= Greater than or Equal to
 le, &lt;= Less than or Equal to</pre>
<h3>Search and match operators</h3>
<p>Additional operators exist expressed only in English, not C-like syntax: </p>
<pre> contains Does the protocol, field or slice contain a value
 matches Does the protocol or text string match the given Perl
 regular expression</pre>
<p>The &#8220;contains&#8221; operator allows a filter to search for a sequence of characters, expressed as a string (quoted or unquoted), or bytes, expressed as a byte array. For example, to search for a given <font SIZE="-1">HTTP URL</font> in a capture, the following filter can be used: </p>
<pre> http contains &quot;<a rel="nofollow" href="http://www.wireshark.org">http://www.wireshark.org</a>&quot;</pre>
<p>The &#8220;contains&#8221; operator cannot be used on atomic fields, such as numbers or <font SIZE="-1">IP</font> addresses. </p>
<p> The &#8220;matches&#8221; operator allows a filter to apply to a specified Perl-compatible regular expression (<font SIZE="-1">PCRE</font>). The &#8220;matches&#8221; operator is only implemented for protocols and for protocol fields with a text string representation. For example, to search for a given <font SIZE="-1">WAP WSP</font> User-Agent, you can write: </p>
<pre> wsp.user_agent matches &quot;(?i)cldc&quot;</pre>
<p>This example shows an interesting <font SIZE="-1">PCRE</font> feature: pattern match options have to be specified with the <code>(?</code>option<code>)</code> construct. For instance, <code>(?i)</code> performs a case-insensitive pattern match. More information on <font SIZE="-1">PCRE</font> can be found in the <i><a href="/docs/linux/man/3-pcrepattern/">pcrepattern</a></i>(3) man page (Perl Regular Expressions are explained in &lt;<a rel="nofollow" href="http://perldoc.perl.org/perlre.html">http://perldoc.perl.org/perlre.html</a>&gt;).</p>
<h3>Functions</h3>
<p>The filter language has the following functions: </p>
<pre> upper(string-field) - converts a string field to uppercase
 lower(string-field) - converts a string field to lowercase</pre>
<p><i>upper()</i> and <i>lower()</i> are useful for performing case-insensitive string comparisons. For example: </p>
<pre> upper(ncp.nds_stream_name) contains &quot;MACRO&quot;
 lower(mount.dump.hostname) == &quot;angel&quot;</pre>
<h3>Protocol field types</h3>
<p>Each protocol field is typed. The types are: </p>
<pre> ASN.1 object identifier
 Boolean
 Character string
 Compiled Perl-Compatible Regular Expression (GRegex) object
 Date and time
 Ethernet or other MAC address
 EUI64 address
 Floating point (double-precision)
 Floating point (single-precision)
 Frame number
 Globally Unique Identifier
 IPv4 address
 IPv6 address
 IPX network number
 Label
 Protocol
 Sequence of bytes
 Signed integer, 1, 2, 3, 4, or 8 bytes
 Time offset
 Unsigned integer, 1, 2, 3, 4, or 8 bytes</pre>
<p>An integer may be expressed in decimal, octal, or hexadecimal notation. The following three display filters are equivalent: </p>
<pre> frame.pkt_len &gt; 10
 frame.pkt_len &gt; 012
 frame.pkt_len &gt; 0xa</pre>
<p>Boolean values are either true or false. In a display filter expression testing the value of a Boolean field, &#8220;true&#8221; is expressed as 1 or any other non-zero value, and &#8220;false&#8221; is expressed as zero. For example, a token-ring packet&#8217;s source route field is Boolean. To find any source-routed packets, a display filter would be: </p>
<pre> tr.sr == 1</pre>
<p>Non source-routed packets can be found with: </p>
<pre> tr.sr == 0</pre>
<p>Ethernet addresses and byte arrays are represented by hex digits. The hex digits may be separated by colons, periods, or hyphens: </p>
<pre> eth.dst eq ff:ff:ff:ff:ff:ff
 aim.data == 0.1.0.d
 fddi.src == aa-aa-aa-aa-aa-aa
 echo.data == 7a</pre>
<p>IPv4 addresses can be represented in either dotted decimal notation or by using the hostname: </p>
<pre> ip.dst eq <a rel="nofollow" href="http://www.mit.edu">www.mit.edu</a>
 ip.src == 192.168.1.1</pre>
<p>IPv4 addresses can be compared with the same logical relations as numbers: eq, ne, gt, ge, lt, and le. The IPv4 address is stored in host order, so you do not have to worry about the endianness of an IPv4 address when using it in a display filter. </p>
<p> Classless InterDomain Routing (<font SIZE="-1">CIDR</font>) notation can be used to test if an IPv4 address is in a certain subnet. For example, this display filter will find all packets in the 129.111 Class-B network: </p>
<pre> ip.addr == 129.111.0.0/16</pre>
<p>Remember, the number after the slash represents the number of bits used to represent the network. <font SIZE="-1">CIDR</font> notation can also be used with hostnames, as in this example of finding <font SIZE="-1">IP</font> addresses on the same Class C network as &#8216;sneezy&#8217;: </p>
<pre> ip.addr eq sneezy/24</pre>
<p>The <font SIZE="-1">CIDR</font> notation can only be used on <font SIZE="-1">IP</font> addresses or hostnames, not in variable names. So, a display filter like &#8220;ip.src/24 == ip.dst/24&#8221; is not valid (yet). </p>
<p> <font SIZE="-1">IPX</font> networks are represented by unsigned 32-bit integers. Most likely you will be using hexadecimal when testing <font SIZE="-1">IPX</font> network values: </p>
<pre> ipx.src.net == 0xc0a82c00</pre>
<p>Strings are enclosed in double quotes: </p>
<pre> http.request.method == &quot;POST&quot;</pre>
<p>Inside double quotes, you may use a backslash to embed a double quote or an arbitrary byte represented in either octal or hexadecimal. </p>
<pre> browser.comment == &quot;An embedded \&quot; double-quote&quot;</pre>
<p>Use of hexadecimal to look for &#8220;<font SIZE="-1">HEAD&#8221;:</font> </p>
<pre> http.request.method == &quot;HEAD&quot;</pre>
<p>Use of octal to look for &#8220;<font SIZE="-1">HEAD&#8221;:</font> </p>
<pre> http.request.method == &quot;\110EAD&quot;</pre>
<p>This means that you must escape backslashes with backslashes inside double quotes. </p>
<pre> smb.path contains &quot;\\SERVER\SHARE&quot;</pre>
<p>looks for \SERVER\SHARE in &#8220;smb.path&#8221;.</p>
<h3>The slice operator</h3>
<p>You can take a slice of a field if the field is a text string or a byte array. For example, you can filter on the vendor portion of an ethernet address (the first three bytes) like this: </p>
<pre> eth.src[0:3] == 00:00:83</pre>
<p>Another example is: </p>
<pre> http.content_type[0:4] == &quot;text&quot;</pre>
<p>You can use the slice operator on a protocol name, too. The &#8220;frame&#8221; protocol can be useful, encompassing all the data captured by <code>Wireshark</code> or <code>TShark</code>. </p>
<pre> token[0:5] ne 0.0.0.1.1
 llc[0] eq aa
 frame[100-199] contains &quot;wireshark&quot;</pre>
<p>The following syntax governs slices: </p>
<pre> [i:j] i = start_offset, j = length
 [i-j] i = start_offset, j = end_offset, inclusive.
 [i] i = start_offset, length = 1
 [:j] start_offset = 0, length = j
 [i:] start_offset = i, end_offset = end_of_field</pre>
<p>Offsets can be negative, in which case they indicate the offset from the <code>end</code> of the field. The last byte of the field is at offset -1, the last but one byte is at offset -2, and so on. Here&#8217;s how to check the last four bytes of a frame: </p>
<pre> frame[-4:4] == 0.1.2.3</pre>
<p>or </p>
<pre> frame[-4:] == 0.1.2.3</pre>
<p>A slice is alwasy compared against either a string or a byte sequence. As a special case, when the slice is only 1 byte wide, you can compare it against a hex integer that 0xff or less (which means it fits inside one byte). This is not allowed for byte sequences greater than one byte, because then one would need to specify the endianness of the multi-byte integer. Also, this is not allowed for decimal numbers, since they would be confused with hex numbers that are already allowed as byte strings. Neverthelss, single-byte hex integers can be convienent: </p>
<pre> frame[4] == 0xff</pre>
<p>Slices can be combined. You can concatenate them using the comma operator: </p>
<pre> ftp[1,3-5,9:] == 01:03:04:05:09:0a:0b</pre>
<p>This concatenates offset 1, offsets 3-5, and offset 9 to the end of the ftp data.</p>
<h3>Type conversions</h3>
<p>If a field is a text string or a byte array, it can be expressed in whichever way is most convenient. </p>
<p> So, for instance, the following filters are equivalent: </p>
<pre> http.request.method == &quot;GET&quot;
 http.request.method == 47.45.54</pre>
<p>A range can also be expressed in either way: </p>
<pre> frame[60:2] gt 50.51
 frame[60:2] gt &quot;PQ&quot;</pre>
<h3>Bit field operations</h3>
<p>It is also possible to define tests with bit field operations. Currently the following bit field operation is supported: </p>
<pre> bitwise_and, &amp; Bitwise AND</pre>
<p>The bitwise <font SIZE="-1">AND</font> operation allows testing to see if one or more bits are set. Bitwise <font SIZE="-1">AND</font> operates on integer protocol fields and slices. </p>
<p> When testing for <font SIZE="-1">TCP SYN</font> packets, you can write: </p>
<pre> tcp.flags &amp; 0x02</pre>
<p>That expression will match all packets that contain a &#8220;tcp.flags&#8221; field with the 0x02 bit, i.e. the <font SIZE="-1">SYN</font> bit, set. </p>
<p> Similarly, filtering for all <font SIZE="-1">WSP GET</font> and extended <font SIZE="-1">GET</font> methods is achieved with: </p>
<pre> wsp.pdu_type &amp; 0x40</pre>
<p>When using slices, the bit mask must be specified as a byte string, and it must have the same number of bytes as the slice itself, as in: </p>
<pre> ip[42:2] &amp; 40:ff</pre>
<h3>Logical expressions</h3>
<p>Tests can be combined using logical expressions. These too are expressible in C-like syntax or with English-like abbreviations: </p>
<pre> and, &amp;&amp; Logical AND
 or, || Logical OR
 not, ! Logical NOT</pre>
<p>Expressions can be grouped by parentheses as well. The following are all valid display filter expressions: </p>
<pre> tcp.port == 80 and ip.src == 192.168.2.1
 not llc
 http and frame[100-199] contains &quot;wireshark&quot;
 (ipx.src.net == 0xbad &amp;&amp; ipx.src.node == 0.0.0.0.0.1) || ip</pre>
<p>Remember that whenever a protocol or field name occurs in an expression, the &#8220;exists&#8221; operator is implicitly called. The &#8220;exists&#8221; operator has the highest priority. This means that the first filter expression must be read as &#8220;show me the packets for which tcp.port exists and equals 80, and ip.src exists and equals 192.168.2.1&#8221;. The second filter expression means &#8220;show me the packets where not (llc exists)&#8221;, or in other words &#8220;where llc does not exist&#8221; and hence will match all packets that do not contain the llc protocol. The third filter expression includes the constraint that offset 199 in the frame exists, in other words the length of the frame is at least 200. </p>
<p> A special caveat must be given regarding fields that occur more than once per packet. &#8220;ip.addr&#8221; occurs twice per <font SIZE="-1">IP</font> packet, once for the source address, and once for the destination address. Likewise, &#8220;tr.rif.ring&#8221; fields can occur more than once per packet. The following two expressions are not equivalent: </p>
<pre> ip.addr ne 192.168.4.1
 not ip.addr eq 192.168.4.1</pre>
<p>The first filter says &#8220;show me packets where an ip.addr exists that does not equal 192.168.4.1&#8221;. That is, as long as one ip.addr in the packet does not equal 192.168.4.1, the packet passes the display filter. The other ip.addr could equal 192.168.4.1 and the packet would still be displayed. The second filter says &#8220;don&#8217;t show me any packets that have an ip.addr field equal to 192.168.4.1&#8221;. If one ip.addr is 192.168.4.1, the packet does not pass. If <code>neither</code> ip.addr field is 192.168.4.1, then the packet is displayed. </p>
<p> It is easy to think of the &#8216;ne&#8217; and &#8216;eq&#8217; operators as having an implicit &#8220;exists&#8221; modifier when dealing with multiply-recurring fields. &#8220;ip.addr ne 192.168.4.1&#8221; can be thought of as &#8220;there exists an ip.addr that does not equal 192.168.4.1&#8221;. &#8220;not ip.addr eq 192.168.4.1&#8221; can be thought of as &#8220;there does not exist an ip.addr equal to 192.168.4.1&#8221;. </p>
<p> Be careful with multiply-recurring fields; they can be confusing. </p>
<p> Care must also be taken when using the display filter to remove noise from the packet trace. If, for example, you want to filter out all <font SIZE="-1">IP</font> multicast packets to address 224.1.2.3, then using: </p>
<pre> ip.dst ne 224.1.2.3</pre>
<p>may be too restrictive. Filtering with &#8220;ip.dst&#8221; selects only those <font SIZE="-1"><code>IP</code></font> packets that satisfy the rule. Any other packets, including all non-IP packets, will not be displayed. To display the non-IP packets as well, you can use one of the following two expressions: </p>
<pre> not ip or ip.dst ne 224.1.2.3
 not ip.addr eq 224.1.2.3</pre>
<p>The first filter uses &#8220;not ip&#8221; to include all non-IP packets and then lets &#8220;ip.dst ne 224.1.2.3&#8221; filter out the unwanted <font SIZE="-1">IP</font> packets. The second filter has already been explained above where filtering with multiply occurring fields was discussed.</p>
<h2>Filter Field Reference</h2>
<p>The entire list of display filters is too large to list here. You can can find references and examples at the following locations:</p>
<dl>
<dt>&bull;</p>
<dd>The online Display Filter Reference: &lt;<a rel="nofollow" href="http://www.wireshark.org/docs/dfref/">http://www.wireshark.org/docs/dfref/</a>&gt;</p>
<dt>&bull;</p>
<dd><i>Help:Supported Protocols</i> in Wireshark</p>
<dt>&bull;</p>
<dd><tt>&quot;tshark -G fields&quot;</tt> on the command line</p>
<dt>&bull;</p>
<dd>The Wireshark wiki: &lt;<a rel="nofollow" href="http://wiki.wireshark.org/DisplayFilters">http://wiki.wireshark.org/DisplayFilters</a>&gt;</dl>
<h2>Notes</h2>
<p>The <code>wireshark-filters</code> manpage is part of the <code>Wireshark</code> distribution. The latest version of <code>Wireshark</code> can be found at &lt;<a rel="nofollow" href="http://www.wireshark.org">http://www.wireshark.org</a>&gt;. </p>
<p> Regular expressions in the &#8220;matches&#8221; operator are provided by GRegex in GLib. See &lt;<a rel="nofollow" href="http://developer.gnome.org/glib/2.32/glib-regex-syntax.html/">http://developer.gnome.org/glib/2.32/glib-regex-syntax.html/</a>&gt; or &lt;<a href="http://www.pcre.org/">http://www.pcre.org/</a>&gt; for more information. </p>
<p> This manpage does not describe the capture filter syntax, which is different. See the manual page of <i><a href="/docs/linux/man/7-pcap-filter/">pcap-filter</a></i>(7) or, if that doesn&#8217;t exist, <i><a href="/docs/linux/man/8-tcpdump/">tcpdump</a></i>(8), or, if that doesn&#8217;t exist, &lt;<a rel="nofollow" href="http://wiki.wireshark.org/CaptureFilters">http://wiki.wireshark.org/CaptureFilters</a>&gt; for a description of capture filters.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-wireshark/">wireshark</a></i>(1), <i><a href="/docs/linux/man/1-tshark/">tshark</a></i>(1), <i><a href="/docs/linux/man/1-editcap/">editcap</a></i>(1), <i><a href="/docs/linux/man/3-pcap/">pcap</a></i>(3), <i><a href="/docs/linux/man/7-pcap-filter/">pcap-filter</a></i>(7) or <i><a href="/docs/linux/man/8-tcpdump/">tcpdump</a></i>(8) if it doesn&#8217;t exist.</p>
<h2>Authors</h2>
<p>See the list of authors in the <code>Wireshark</code> man page for a list of authors of that code.</p>
