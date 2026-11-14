---
title: "ngrep(8)"
name: "ngrep"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ngrep/"
description: "ngrep – network grep"
---

<p>ngrep &#8211; network grep</p>
<h2>Synopsis</h2>
<p><code>ngrep &lt;-hNXViwqpevxlDtTRM&gt; &lt;-IO</code> <i>pcap_dump</i> <code>&gt; &lt; -n</code> <i>num</i> <code>&gt; &lt; -d</code> <i>dev</i> <code>&gt; &lt; -A</code> <i>num</i> <code>&gt; &lt; -s</code> <i>snaplen</i> <code>&gt; &lt; -S</code> <i>limitlen</i> <code>&gt; &lt; -W</code> <i>normal|byline|single|none</i> <code>&gt; &lt; -c</code> <i>cols</i> <code>&gt; &lt; -P</code> <i>char</i> <code>&gt; &lt; -F</code> <i>file</i> <code>&gt; &lt;</code> <i>match expression</i> <code>&gt; &lt;</code> <i>bpf filter</i> <code>&gt;</code> </p>
<h2>Description</h2>
<p>ngrep strives to provide most of GNU grep&#8217;s common features, applying them to the network layer. ngrep is a pcap-aware tool that will allow you to specify extended regular expressions to match against data payloads of packets. It currently recognizes TCP, UDP and ICMP across Ethernet, PPP, SLIP, FDDI and null interfaces, and understands bpf filter logic in the same fashion as more common packet sniffing tools, such as <code><a href="/docs/linux/man/8-tcpdump/">tcpdump</a></code>(8) and <code><a href="/docs/linux/man/1-snoop/">snoop</a></code>(1). </p>
<h2>Options</h2>
<dl>
<dt>-h</p>
<dd>Display help/usage information. </p>
<dt>-N</p>
<dd>Show sub-protocol number along with single-character identifier (useful when observing raw or unknown protocols). </p>
<dt>-X</p>
<dd>Treat the match expression as a hexadecimal string. See the explanation of <i>match expression</i> below. </p>
<dt>-V</p>
<dd>Display version information. </p>
<dt>-i</p>
<dd>Ignore case for the regex expression. </p>
<dt>-w</p>
<dd>Match the regex expression as a word. </p>
<dt>-q</p>
<dd>Be quiet; don&#8217;t output any information other than packet headers and their payloads (if relevant). </p>
<dt>-p</p>
<dd>Don&#8217;t put the interface into promiscuous mode. </p>
<dt>-e</p>
<dd>Show empty packets. Normally empty packets are discarded because they have no payload to search. If specified, empty packets will be shown, regardless of the specified regex expression. </p>
<dt>-v</p>
<dd>Invert the match; only display packets that don&#8217;t match. </p>
<dt>-x</p>
<dd>Dump packet contents as hexadecimal as well as ASCII. </p>
<dt>-l</p>
<dd>Make stdout line buffered. </p>
<dt>-D</p>
<dd>When reading pcap_dump files, replay them at their recorded time intervals (mimic realtime). </p>
<dt>-t</p>
<dd>Print a timestamp in the form of YYYY/MM/DD HH:MM:SS.UUUUUU everytime a packet is matched. </p>
<dt>-T</p>
<dd>Print a timestamp in the form of +S.UUUUUU, indicating the delta between packet matches. Specify a second time to indicate the delta since the first packet match. </p>
<dt>-R</p>
<dd>Do not try to drop privileges to the DROPPRIVS_USER. </p>
<p> ngrep makes no effort to validate input from live or offline sources as it is focused more on performance and handling large amounts of data than protocol correctness, which is most often a fair assumption to make. However, sometimes it matters and thus as a rule ngrep will try to be defensive and drop any root privileges it might have. </p>
<p> There exist scenarios where this behaviour can become an obstacle, so this option is provided to end-users who want to disable this feature, but must do so with an understanding of the risks. Packets can be randomly malformed or even specifically designed to overflow sniffers and take control of them, and revoking root privileges is currently the only risk mitigation ngrep employs against such an attack. Use this option and turn it off at your own risk. </p>
<dt>-c cols</p>
<dd>Explicitly set the console width to &#8220;cols&#8221;. Note that this is the console width, and not the full width of what ngrep prints out as payloads; depending on the output mode ngrep may print less than &#8220;cols&#8221; bytes per line (indentation). </p>
<dt>-F file</p>
<dd>Read in the bpf filter from the specified filename. This is a compatibility option for users familiar with tcpdump. Please note that specifying &#8220;-F&#8221; will override any bpf filter specified on the command-line. </p>
<dt>-P char</p>
<dd>Specify an alternate character to signify non-printable characters when displayed. The default is &#8220;.&#8221;. </p>
<dt>-K num</p>
<dd>Kill matching TCP connections (like tcpkill). The numeric argument controls how many RST segments are sent. </p>
<dt>-W normal|byline|single|none</p>
<dd>Specify an alternate manner for displaying packets, when not in hexadecimal mode. The &#8220;byline&#8221; mode honors embedded linefeeds, wrapping text only when a linefeed is encountered. The &#8220;none&#8221; mode doesn&#8217;t wrap under any circumstance (entire payload is displayed on one line). The &#8220;single&#8221; mode is conceptually the same as &#8220;none&#8221;, except that everything including IP and source/destination header information is all on one line. &#8220;normal&#8221; is the default mode and is only included for completeness. This option is incompatible with &#8220;-x&#8221;. </p>
<dt>-s snaplen</p>
<dd>Set the bpf caplen to snaplen (default 65536). </p>
<dt>-S limitlen</p>
<dd>Set the upper limit on the size of packets that ngrep will look at. Useful for looking at only the first N bytes of packets without changing the BPF snaplen. </p>
<dt>-I pcap_dump</p>
<dd>Input file pcap_dump into ngrep. Works with any pcap-compatible dump file format. This option is useful for searching for a wide range of different patterns over the same packet stream. </p>
<dt>-O pcap_dump</p>
<dd>Output matched packets to a pcap-compatible dump file. This feature does not interfere with normal output to stdout. </p>
<dt>-n num</p>
<dd>Match only <i>num</i> packets total, then exit. </p>
<dt>-d dev</p>
<dd>By default ngrep will select a default interface to listen on. Use this option to force ngrep to listen on interface <i>dev</i>. </p>
<dt>-A num</p>
<dd>Dump <i>num</i> packets of trailing context after matching a packet. </p>
<dt><i> match expression</i></p>
<dd>A match expression is either an extended regular expression, or if the <i>-X</i> option is specified, a string signifying a hexadecimal value. An extended regular expression follows the rules as implemented by the <code>GNU regex</code> <code>library</code>. Hexadecimal expressions can optionally be preceded by `0x&#8217;. E.g., `DEADBEEF&#8217;, `0xDEADBEEF&#8217;. </p>
<dt><i> bpf filter</i></p>
<dd>Selects a filter that specifies what packets will be dumped. If no <i>bpf filter</i> is given, all IP packets seen on the selected interface will be dumped. Otherwise, only packets for which <i>bpf filter</i> is `true&#8217; will be dumped.</dl>
<p> The <i>bpf filter</i> consists of one or more <i>primitives.</i> Primitives usually consist of an <i>id</i> (name or number) preceded by one or more qualifiers. There are three different kinds of qualifier:</p>
<dl>
<dt><i>type</i></p>
<dd>qualifiers say what kind of thing the id name or number refers to. Possible types are <code>host</code>, <code>net</code> and <code>port</code>. E.g., `host blort&#8217;, `net 1.2.3&#8242;, `port 80&#8242;. If there is no type qualifier, <code>host</code> is assumed.</p>
<dt><i>dir</i></p>
<dd>qualifiers specify a particular transfer direction to and/or from <i>id.</i> Possible directions are <code>src</code>, <code>dst</code>, <code>src or dst</code> and <code>src and</code> <code>dst</code>. E.g., `src foo&#8217;, `dst net 1.2.3&#8242;, `src or dst port ftp-data&#8217;. If there is no dir qualifier, <code>src or dst</code> is assumed. For `null&#8217; link layers (i.e. point to point protocols such as slip) the <code>inbound</code> and <code>outbound</code> qualifiers can be used to specify a desired direction.</p>
<dt><i>proto</i></p>
<dd>qualifiers are restricted to ip-only protocols. Possible protos are: <code>tcp ,</code> <code>udp</code> and <code>icmp</code>. e.g., `udp src foo&#8217; or `tcp port 21&#8242;. If there is no proto qualifier, all protocols consistent with the type are assumed. E.g., `src foo&#8217; means `ip and ((tcp or udp) src foo)&#8217;, `net bar&#8217; means `ip and (net bar)&#8217;, and `port 53&#8242; means `ip and ((tcp or udp) port 53)&#8217;.</dl>
<p> In addition to the above, there are some special `primitive&#8217; keywords that don&#8217;t follow the pattern: <code>gateway</code>, <code>broadcast</code>, <code>less</code>, <code>greater</code> and arithmetic expressions. All of these are described below. </p>
<p> More complex filter expressions are built up by using the words <code>and</code>, <code>or</code> and <code>not</code> to combine primitives. E.g., `host blort and not port ftp and not port ftp-data&#8217;. To save typing, identical qualifier lists can be omitted. E.g., `tcp dst port ftp or ftp-data or domain&#8217; is exactly the same as `tcp dst port ftp or tcp dst port ftp-data or tcp dst port domain&#8217;. </p>
<p> Allowable primitives are: </p>
<dl>
<dt><code>dst host </code><i>host</i></p>
<dd>True if the IP destination field of the packet is <i>host</i>, which may be either an address or a name. </p>
<dt><code>src host </code><i>host</i></p>
<dd>True if the IP source field of the packet is <i>host</i>. </p>
<dt><code>host </code><i>host</i></p>
<dd>True if either the IP source or destination of the packet is <i>host</i>. Any of the above host expressions can be prepended with the keywords, <code>ip</code>, <code>arp</code>, or <code>rarp</code> as in: </p>
<pre><code>ip host </code><i>host</i></pre>
<p>which is equivalent to: </p>
<dt><code>ether dst </code><i>ehost</i></p>
<dd>True if the ethernet destination address is <i>ehost</i>. <i>Ehost</i> may be either a name from /etc/ethers or a number (see <i><a href="//www.systutorials.com/docs/linux/man/3N-ethers/">ethers</a></i>(3N) for numeric format).</p>
<dt><code>ether src </code><i>ehost</i></p>
<dd>True if the ethernet source address is <i>ehost</i>.</p>
<dt><code>ether host </code><i>ehost</i></p>
<dd>True if either the ethernet source or destination address is <i>ehost</i>. </p>
<dt><code>gateway</code> <i>host</i></p>
<dd>True if the packet used <i>host</i> as a gateway. I.e., the ethernet source or destination address was <i>host</i> but neither the IP source nor the IP destination was <i>host</i>. <i>Host</i> must be a name and must be found in both /etc/hosts and /etc/ethers. (An equivalent expression is </p>
<pre><code>ether host </code><i>ehost </i><code>and not host </code><i>host</i></pre>
<p>which can be used with either names or numbers for <i>host / ehost</i>.) </p>
<dt><code>dst net </code><i>net</i></p>
<dd>True if the IP destination address of the packet has a network number of <i>net</i>. <i>Net</i> may be either a name from /etc/networks or a network number (see <i><a href="/docs/linux/man/4-networks/">networks</a>(4)</i> for details). </p>
<dt><code>src net </code><i>net</i></p>
<dd>True if the IP source address of the packet has a network number of <i>net</i>. </p>
<dt><code>net </code><i>net</i></p>
<dd>True if either the IP source or destination address of the packet has a network number of <i>net</i>. </p>
<dt><code>net </code><i>net</i> <code>mask </code><i>mask</i></p>
<dd>True if the IP address matches <i>net</i> with the specific netmask. May be qualified with <code>src</code> or <code>dst</code>. </p>
<dt><code>net </code><i>net</i>/<i>len</i></p>
<dd>True if the IP address matches <i>net</i> a netmask <i>len</i> bits wide. May be qualified with <code>src</code> or <code>dst</code>. </p>
<dt><code>dst port </code><i>port</i></p>
<dd>True if the packet is ip/tcp or ip/udp and has a destination port value of <i>port</i>. The <i>port</i> can be a number or a name used in /etc/services (see <i><a href="//www.systutorials.com/docs/linux/man/4P-tcp/">tcp</a></i>(4P) and <i><a href="//www.systutorials.com/docs/linux/man/4P-udp/">udp</a></i>(4P)). If a name is used, both the port number and protocol are checked. If a number or ambiguous name is used, only the port number is checked (e.g., <code>dst port 513</code> will print both tcp/login traffic and udp/who traffic, and <code>port domain</code> will print both tcp/domain and udp/domain traffic). </p>
<dt><code>src port </code><i>port</i></p>
<dd>True if the packet has a source port value of <i>port</i>. </p>
<dt><code>port </code><i>port</i></p>
<dd>True if either the source or destination port of the packet is <i>port</i>. Any of the above port expressions can be prepended with the keywords, <code>tcp</code> or <code>udp</code>, as in: </p>
<pre><code>tcp src port </code><i>port</i></pre>
<p>which matches only tcp packets whose source port is <i>port</i>. </p>
<dt><code>less </code><i>length</i></p>
<dd>True if the packet has a length less than or equal to <i>length</i>. This is equivalent to: </p>
<pre><code>len &lt;= </code><i>length</i>.</pre>
<dt><code>greater </code><i>length</i></p>
<dd>True if the packet has a length greater than or equal to <i>length</i>. This is equivalent to: </p>
<pre><code>len &gt;= </code><i>length</i>.</pre>
<dt><code>ip proto </code><i>protocol</i></p>
<dd>True if the packet is an ip packet (see <i><a href="//www.systutorials.com/docs/linux/man/4P-ip/">ip</a></i>(4P)) of protocol type <i>protocol</i>. <i>Protocol</i> can be a number or one of the names <i>tcp</i>, <i>udp</i> or <i>icmp</i>. Note that the identifiers <i>tcp</i> and <i>udp</i> are also keywords and must be escaped via backslash (\), which is \ in the C-shell. </p>
<dt><code>ip broadcast</code></p>
<dd>True if the packet is an IP broadcast packet. It checks for both the all-zeroes and all-ones broadcast conventions, and looks up the local subnet mask. </p>
<dt><code>ip multicast</code></p>
<dd>True if the packet is an IP multicast packet. </p>
<dt><code>ip</code></p>
<dd>Abbreviation for: </p>
<pre><code>ether proto ip</code></pre>
<dt><code>tcp</code>, <code>udp</code>, <code>icmp</code></p>
<dd>Abbreviations for: </p>
<pre><code>ip proto </code><i>p</i></pre>
<p>where <i>p</i> is one of the above protocols.</p>
<dt><i>expr relop expr</i></p>
<dd>True if the relation holds, where <i>relop</i> is one of &gt;, &lt;, &gt;=, &lt;=, =, !=, and <i>expr</i> is an arithmetic expression composed of integer constants (expressed in standard C syntax), the normal binary operators [+, -, *, /, &amp;, |], a length operator, and special packet data accessors. To access data inside the packet, use the following syntax: </p>
<pre><i>proto</i><code> [ </code><i>expr</i><code> : </code><i>size</i><code> ]</code></pre>
<p><i>Proto</i> is one of <code>ip, tcp, udp </code>or <code>icmp</code>, and indicates the protocol layer for the index operation. The byte offset, relative to the indicated protocol layer, is given by <i>expr</i>. <i>Size</i> is optional and indicates the number of bytes in the field of interest; it can be either one, two, or four, and defaults to one. The length operator, indicated by the keyword <code>len</code>, gives the length of the packet. </p>
<p> For example, `<code>ether[0] &amp; 1 != 0</code>&#8216; catches all multicast traffic. The expression `<code>ip[0] &amp; 0xf != 5</code>&#8216; catches all IP packets with options. The expression `<code>ip[6:2] &amp; 0x1fff = 0</code>&#8216; catches only unfragmented datagrams and frag zero of fragmented datagrams. This check is implicitly applied to the <code>tcp</code> and <code>udp</code> index operations. For instance, <code>tcp[0]</code> always means the first byte of the TCP <i>header</i>, and never means the first byte of an intervening fragment.</dl>
<p> Primitives may be combined using:</p>
<dl>
<dd>A parenthesized group of primitives and operators (parentheses are special to the Shell and must be escaped).</p>
<dd>Negation (`<code>!</code>&#8216; or `<code>not</code>&#8216;).</p>
<dd>Concatenation (`<code>&amp;&amp;</code>&#8216; or `<code>and</code>&#8216;).</p>
<dd>Alternation (`<code>||</code>&#8216; or `<code>or</code>&#8216;).</dl>
<p> Negation has highest precedence. Alternation and concatenation have equal precedence and associate left to right. Note that explicit <code>and</code> tokens, not juxtaposition, are now required for concatenation. </p>
<p> If an identifier is given without a keyword, the most recent keyword is assumed. For example, </p>
<pre><code>not host vs and ace</code></pre>
<p>is short for </p>
<pre><code>not host vs and host ace</code></pre>
<p>which should not be confused with </p>
<pre><code>not ( host vs or ace )</code></pre>
<p>Expression arguments can be passed to ngrep as either a single argument or as multiple arguments, whichever is more convenient. Generally, if the expression contains Shell metacharacters, it is easier to pass it as a single, quoted argument. Multiple arguments are concatenated with spaces before being parsed.</p>
<h2>Diagnostics</h2>
<p>Errors from <code>ngrep, libpcap,</code> and the <code>GNU regex library</code> are all output to stderr.</p>
<h2>Author</h2>
<p>Written by Jordan Ritter &lt;jpr5 [at] darkridge.com&gt;.</p>
<h2>Reporting Bugs</h2>
<p>Please report bugs to the ngrep&#8217;s GitHub Issue Tracker, located at </p>
<p>&nbsp;<wbr><a rel="nofollow" href="http://github.com/jpr5/ngrep/issues">http://github.com/jpr5/ngrep/issues</a> </p>
<p> Non-bug, non-feature-request general feedback should be sent to the author directly by email.</p>
<h2>Notes</h2>
<p>ALL YOUR BASE ARE BELONG TO US. </p>
