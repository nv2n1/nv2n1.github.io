---
title: "ssldump(1)"
name: "ssldump"
section: "1"
letter: "s"
url: "/docs/linux/man/1-ssldump/"
description: "ssldump – dump SSL traffic on a network"
---

<h2>NAME</h2>
<p> ssldump &#8211; dump SSL traffic on a network</p>
<h2>SYNOPSIS</h2>
<p> <code>ssldump</code> [ <code>-vTshVq</code> <code>-aAdeHnNqTxXvy</code> ] [ <code>-i</code> <i>interface</i> ] </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [ <code>-k</code> <i>keyfile</i> ] [ <code>-p</code> <i>password</i> ] [ <code>-r</code> <i>dumpfile</i> ] </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [ <code>-S</code> [<i>crypto</i>|<i>d</i>|<i>ht</i>|<i>H</i>|<i>nroff</i>] ] [ <i>expression</i> ] </p>
<h2>DESCRIPTION</h2>
<p> <i>ssldump</i> is an SSL/TLS network protocol analyzer. It identifies TCP connections on the chosen network interface and attempts to interpret them as SSL/TLS traffic. When it identifies SSL/TLS traffic, it decodes the records and displays them in a textual form to stdout. If provided with the appropriate keying material, it will also decrypt the connections and display the application data traffic. </p>
<p> ssldump has been tested on FreeBSD, Linux, Solaris, and HP/UX. Since it&#8217;s based on PCAP, it should work on most platforms. However, unlike tcpdump, ssldump needs to be able to see both sides of the data transmission so you may have trouble using it with network taps such as SunOS nit that don&#8217;t permit you to see transmitted data. <code>Under SunOS with nit or bpf:</code> To run <i>tcpdump</i> you must have read access to <i>/dev/nit</i> or <i>/dev/bpf*</i>. <code>Under Solaris with dlpi:</code> You must have read access to the network pseudo device, e.g. <i>/dev/le</i>. <code>Under HP-UX with dlpi:</code> You must be root or it must be installed setuid to root. <code>Under IRIX with snoop:</code> You must be root or it must be installed setuid to root. <code>Under Linux:</code> You must be root or it must be installed setuid to root. <code>Under Ultrix and Digital UNIX:</code> Once the super-user has enabled promiscuous-mode operation using <i><a href="/docs/linux/man/8-pfconfig/">pfconfig</a></i>(8), any user may run <code>ssldump</code> <code>Under BSD:</code> You must have read access to <i>/dev/bpf*</i>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></p>
<dd> Print bare TCP ACKs (useful for observing Nagle behavior)</p>
<dt><code>-A</code></p>
<dd> Print all record fields (by default ssldump chooses the most interesting fields)</p>
<dt><code>-d</code></p>
<dd> Display the application data traffic. This usually means decrypting it, but when -d is used ssldump will also decode application data traffic <i>before</i> the SSL session initiates. This allows you to see HTTPS CONNECT behavior as well as SMTP STARTTLS. As a side effect, since ssldump can&#8217;t tell whether plaintext is traffic before the initiation of an SSL connection or just a regular TCP connection, this allows you to use ssldump to sniff any TCP connection. ssldump will automatically detect ASCII data and display it directly to the screen. non-ASCII data is displayed as hex dumps. See also -X.</p>
<dt><code>-e</code></p>
<dd> Print absolute timestamps instead of relative timestamps</p>
<dt><code>-H</code></p>
<dd> Print the full SSL packet header.</p>
<dt><code>-n </code></p>
<dd> Don&#8217;t try to resolve host names from IP addresses</p>
<dt><code>-N</code></p>
<dd> Attempt to parse ASN.1 when it appears, such as in certificates and DNs.</p>
<dt><code>-p</code></p>
<dd> Use <i>password</i> as the SSL keyfile password.</p>
<dt><code>-P</code></p>
<dd> Don&#8217;t put the interface into promiscuous mode.</p>
<dt><code>-q</code></p>
<dd> Don&#8217;t decode any record fields beyond a single summary line. (quiet mode).</p>
<dt><code>-T</code></p>
<dd> Print the TCP headers.</p>
<dt><code>-v</code></p>
<dd> Display version and copyright information.</p>
<dt><code>-x</code></p>
<dd> Print each record in hex, as well as decoding it.</p>
<dt><code>-X</code></p>
<dd> When the -d option is used, binary data is automatically printed in two columns with a hex dump on the left and the printable characters on the right. -X suppresses the display of the printable characters, thus making it easier to cut and paste the hex data into some other program.</p>
<dt><code>-y</code></p>
<dd> Decorate the output for processing with nroff/troff. Not very useful for the average user.</p>
<dt><code>-i</code><i> interface</i></p>
<dd> Use <i>interface</i> as the network interface on which to sniff SSL/TLS traffic.</p>
<dt><code>-k</code><i> keyfile</i></p>
<dd> Use <i>keyfile</i> as the location of the SSL keyfile (OpenSSL format) Previous versions of ssldump automatically looked in ./server.pem. Now you must specify your keyfile every time.</p>
<dt><code>-p</code><i> password</i></p>
<dd> Use <i>password</i> as the SSL keyfile password.</p>
<dt><code>-r</code><i> file</i></p>
<dd> Read data from <i>file</i> instead of from the network. The old -f option still works but is deprecated and will probably be removed with the next version.</p>
<dt><code>-S</code><i> [ </i><code>crypto</code><i> | </i><code>d</code><i> | </i><code>ht</code><i> | </i><code>H</code><i> ]</i></p>
<dd> Specify SSL flags to ssldump. These flags include:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>crypto</i></p>
<dd> Print cryptographic information.</p>
<dt><i>d</i></p>
<dd> Print fields as decoded.</p>
<dt><i>ht</i></p>
<dd> Print the handshake type.</p>
<dt><i>H</i></p>
<dd> Print handshake type and highlights.</dl>
</dl>
<dt><i>expression</i></p>
<dd>
<dl>
<dt>
<dd> Selects what packets ssldump will examine. Technically speaking, ssldump supports the full expression syntax from PCAP and tcpdump. In fact, the description here is cribbed from the tcpdump man page. However, since ssldump needs to examine full TCP streams, most of the tcpdump expressions will select traffic mixes that ssldump will simply ignore. Only the expressions which don&#8217;t result in incomplete TCP streams are listed here. </p>
<p> The <i>expression</i> consists of one or more <i>primitives</i>. Primitives usually consist of an <i>id</i> (name or number) preceded by one or more qualifiers. There are three different kinds of qualifier:</p>
<dl>
<dt><i>type</i></p>
<dd> qualifiers say what kind of thing the id name or number refers to. Possible types are <code>host</code>, <code>net</code> and <code>port</code>. E.g., `host foo&#8217;, `net 128.3&#8242;, `port 20&#8242;. If there is no type qualifier, <code>host</code> is assumed.</p>
<dt><i>dir</i></p>
<dd> qualifiers specify a particular transfer direction to and/or from <i>id.</i> Possible directions are <code>src</code>, <code>dst</code>, <code>src or dst</code> and <code>src and</code> <code>dst</code>. E.g., `src foo&#8217;, `dst net 128.3&#8242;, `src or dst port ftp-data&#8217;. If there is no dir qualifier, <code>src or dst</code> is assumed. For `null&#8217; link layers (i.e. point to point protocols such as slip) the <code>inbound</code> and <code>outbound</code> qualifiers can be used to specify a desired direction.</dl>
<p> More complex filter expressions are built up by using the words <code>and</code>, <code>or</code> and <code>not</code> to combine primitives. E.g., `host foo and not port ftp and not port ftp-data&#8217;. To save typing, identical qualifier lists can be omitted. E.g., `tcp dst port ftp or ftp-data or domain&#8217; is exactly the same as `tcp dst port ftp or tcp dst port ftp-data or tcp dst port domain&#8217;. </p>
<p> Allowable primitives are:</p>
<dl>
<dt><code>dst host </code><i>host</i></p>
<dd> True if the IPv4/v6 destination field of the packet is <i>host</i>, which may be either an address or a name.</p>
<dt><code>src host </code><i>host</i></p>
<dd> True if the IPv4/v6 source field of the packet is <i>host</i>.</p>
<dt><code>host </code><i>host</i></p>
<dd> True if either the IPv4/v6 source or destination of the packet is <i>host</i>. Any of the above host expressions can be prepended with the keywords, <code>ip</code>, <code>arp</code>, <code>rarp</code>, or <code>ip6</code> as in: </p>
<pre>
<code>ip host </code><i>host</i>
</pre>
<p> which is equivalent to: </p>
<pre>
<code>ether proto </code><i>\ip</i><code> and host </code><i>host</i>
</pre>
<p> If <i>host</i> is a name with multiple IP addresses, each address will be checked for a match.</p>
<dt><code>ether dst </code><i>ehost</i></p>
<dd> True if the ethernet destination address is <i>ehost</i>. <i>Ehost</i> may be either a name from /etc/ethers or a number (see <i><a href="//www.systutorials.com/docs/linux/man/3N-ethers/">ethers</a></i>(3N) for numeric format).</p>
<dt><code>ether src </code><i>ehost</i></p>
<dd> True if the ethernet source address is <i>ehost</i>.</p>
<dt><code>ether host </code><i>ehost</i></p>
<dd> True if either the ethernet source or destination address is <i>ehost</i>.</p>
<dt><code>gateway</code> <i>host</i></p>
<dd> True if the packet used <i>host</i> as a gateway. I.e., the ethernet source or destination address was <i>host</i> but neither the IP source nor the IP destination was <i>host</i>. <i>Host</i> must be a name and must be found in both /etc/hosts and /etc/ethers. (An equivalent expression is </p>
<pre>
<code>ether host </code><i>ehost </i><code>and not host </code><i>host</i>
</pre>
<p> which can be used with either names or numbers for <i>host / ehost</i>.) This syntax does not work in IPv6-enabled configuration at this moment.</p>
<dt><code>dst net </code><i>net</i></p>
<dd> True if the IPv4/v6 destination address of the packet has a network number of <i>net</i>. <i>Net</i> may be either a name from /etc/networks or a network number (see <i><a href="/docs/linux/man/4-networks/">networks</a>(4)</i> for details).</p>
<dt><code>src net </code><i>net</i></p>
<dd> True if the IPv4/v6 source address of the packet has a network number of <i>net</i>.</p>
<dt><code>net </code><i>net</i></p>
<dd> True if either the IPv4/v6 source or destination address of the packet has a network number of <i>net</i>.</p>
<dt><code>net </code><i>net</i> <code>mask </code><i>mask</i></p>
<dd> True if the IP address matches <i>net</i> with the specific netmask. May be qualified with <code>src</code> or <code>dst</code>. Note that this syntax is not valid for IPv6 <i>net</i>.</p>
<dt><code>net </code><i>net</i>/<i>len</i></p>
<dd> True if the IPv4/v6 address matches <i>net</i> a netmask <i>len</i> bits wide. May be qualified with <code>src</code> or <code>dst</code>.</p>
<dt><code>dst port </code><i>port</i></p>
<dd> True if the packet is ip/tcp, ip/udp, ip6/tcp or ip6/udp and has a destination port value of <i>port</i>. The <i>port</i> can be a number or a name used in /etc/services (see <i><a href="//www.systutorials.com/docs/linux/man/4P-tcp/">tcp</a></i>(4P) and <i><a href="//www.systutorials.com/docs/linux/man/4P-udp/">udp</a></i>(4P)). If a name is used, both the port number and protocol are checked. If a number or ambiguous name is used, only the port number is checked (e.g., <code>dst port 513</code> will print both tcp/login traffic and udp/who traffic, and <code>port domain</code> will print both tcp/domain and udp/domain traffic).</p>
<dt><code>src port </code><i>port</i></p>
<dd> True if the packet has a source port value of <i>port</i>.</p>
<dt><code>port </code><i>port</i></p>
<dd> True if either the source or destination port of the packet is <i>port</i>. Any of the above port expressions can be prepended with the keywords, <code>tcp</code> or <code>udp</code>, as in: </p>
<pre>
<code>tcp src port </code><i>port</i>
</pre>
<p> which matches only tcp packets whose source port is <i>port</i>.</dl>
<p> Primitives may be combined using:</p>
<dl>
<dt>
<dd> A parenthesized group of primitives and operators (parentheses are special to the Shell and must be escaped).</p>
<dt>
<dd> Negation (`<code>!</code>&#8216; or `<code>not</code>&#8216;).</p>
<dt>
<dd> Concatenation (`<code>&amp;&amp;</code>&#8216; or `<code>and</code>&#8216;).</p>
<dt>
<dd> Alternation (`<code>||</code>&#8216; or `<code>or</code>&#8216;).</dl>
<p> Negation has highest precedence. Alternation and concatenation have equal precedence and associate left to right. Note that explicit <code>and</code> tokens, not juxtaposition, are now required for concatenation. </p>
<p> If an identifier is given without a keyword, the most recent keyword is assumed. For example, </p>
<pre>
<code>not host vs and ace</code>
</pre>
<p> is short for </p>
<pre>
<code>not host vs and host ace</code>
</pre>
<p> which should not be confused with </p>
<pre>
<code>not ( host vs or ace )</code>
</pre>
<p> Expression arguments can be passed to ssldump as either a single argument or as multiple arguments, whichever is more convenient. Generally, if the expression contains Shell metacharacters, it is easier to pass it as a single, quoted argument. Multiple arguments are concatenated with spaces before being parsed.</dl>
</dl>
<h2>EXAMPLES</h2>
<p> To listen to traffic on interface <i>le0</i> port <i>443</i></p>
<dl>
<dt>
<dd>
<pre>
<code>ssldump -i le0 port 443</code>
</pre>
</dl>
<p> To listen to traffic to the server <i>romeo</i> on port <i>443</i>.</p>
<dl>
<dt>
<dd>
<pre>
<code>ssldump -i le0 port 443 and host romeo</code>
</pre>
</dl>
<p> To decrypt traffic to to host <i>romeo</i> <i>server.pem</i> and the password <i>foobar</i></p>
<dl>
<dt>
<dd>
<pre>
<code>ssldump -Ad -k ~/server.pem -p foobar -i le0 host romeo
</code></pre>
</dl>
<h2>OUTPUT FORMAT</h2>
<p> All output is printed to standard out. </p>
<p> ssldump prints an indication of every new TCP connection using a line like the following </p>
<pre>
<code>New TCP connection #2: iromeo.rtfm.com(2302) &lt;-&gt; sr1.rtfm.com(4433)</code>
</pre>
<p> The host which send the first SYN is printed on the left and the host which responded is printed on the right. Ordinarily, this means that the SSL client will be printed on the left with the SSL server on the right. In this case we have a connection from <i>iromeo.rtfm.com</i> (port <i>2303</i>) to <i>sr1.rtfm.com</i> (port <i>4433</i>). To allow the user to disentangle traffic from different connections, each connection is numbered. This is connection <i>2</i>. </p>
<p> The printout of each SSL record begins with a record line. This line contains the connection and record number, a timestamp, and the record type, as in the following: </p>
<pre>
<code>2 3  0.2001 (0.0749)  S&gt;C  Handshake      Certificate</code>
</pre>
<p> This is record <i>3</i> on connection <i>2</i>. The first timestamp is the time since the beginning of the connection. The second is the time since the previous record. Both are in seconds. </p>
<p> The next field in the record line is the direction that the record was going. <i>C&gt;S</i> indicates records transmitted from client to server and <i>S&gt;C</i> indicates records transmitted from server to client. ssldump assumes that the host to transmit the first SYN is the SSL client (this is nearly always correct). </p>
<p> The next field is the record type, one of <i>Handshake</i>, <i>IAlert</i>, <i>ChangeCipherSpec</i>, or <i>application_data</i>. Finally, ssldump may print record-specific data on the rest of the line. For <i>Handshake</i> records, it prints the handshake message. Thus, this record is a <i>Certificate</i> message. </p>
<p> ssldump chooses certain record types for further decoding. These are the ones that have proven to be most useful for debugging: </p>
<pre>
<i>ClientHello</i> - version, offered cipher suites, session id
                     if provided)
<i>ServerHello</i> - version, session_id, chosen cipher suite,
                     compression method
<i>Alert</i> - type and level (if obtainable)
</pre>
<p> Fuller decoding of the various records can be obtained by using the <code>-A</code> , <code>-d</code> , <code>-k</code> and <code>-p</code> flags. </p>
<h2>DECRYPTION</h2>
<p> ssldump can decrypt traffic between two hosts if the following two conditions are met:</p>
<dl>
<dt>
<dd>
<pre>
1. ssldump has the keys.
2. Static RSA was used.
</pre>
</dl>
<p> In any other case, once encryption starts, ssldump will only be able to determine the record type. Consider the following section of a trace. </p>
<pre>
<code>1 5  0.4129 (0.1983)  C&gt;S  Handshake      ClientKeyExchange
1 6  0.4129 (0.0000)  C&gt;S  ChangeCipherSpec
1 7  0.4129 (0.0000)  C&gt;S  Handshake
1 8  0.5585 (0.1456)  S&gt;C  ChangeCipherSpec
1 9  0.6135 (0.0550)  S&gt;C  Handshake
1 10 2.3121 (1.6986)  C&gt;S  application_data
1 11 2.5336 (0.2214)  C&gt;S  application_data
1 12 2.5545 (0.0209)  S&gt;C  application_data
1 13 2.5592 (0.0046)  S&gt;C  application_data
1 14 2.5592 (0.0000)  S&gt;C  Alert</code>
</pre>
<p> Note that the <i>ClientKeyExchange</i> message type is printed but the rest of the <i>Handshake</i> messages do not have types. These are the <i>Finished</i> messages, but because they are encrypted ssldump only knows that they are of type <i>Handshake</i>. Similarly, had the <i>Alert</i> in record 14 happened during the handshake, it&#8217;s type and level would have been printed. However, since it is encrypted we can only tell that it is an alert. </p>
<h2>BUGS</h2>
<p> Please send bug reports to ssldump [at] rtfm.com. </p>
<p> The TCP reassembler is not perfect. No attempt is made to reassemble IP fragments and the 3-way handshake and close handshake are imperfectly implemented. In practice, this turns out not to be much of a problem. </p>
<p> Support is provided for only for Ethernet and loopback interfaces because that&#8217;s all that I have. If you have another kind of network you will need to modify pcap_cb in base/pcap-snoop.c. If you have direct experience with ssldump on other networks, please send me patches. </p>
<p> ssldump doesn&#8217;t implement session caching and therefore can&#8217;t decrypt resumed sessions. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tcpdump/">tcpdump</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> ssldump was written by Eric Rescorla &lt;ekr [at] rtfm.com&gt;. </p>
<h2>Index</h2>
