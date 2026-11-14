---
title: "dsniff(8)"
name: "dsniff"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dsniff/"
description: "dsniff – password sniffer"
---

<p>dsniff &#8211; password sniffer</p>
<h2>Synopsis</h2>
<p><code>dsniff</code> [<code>-c</code>] [<code>-d</code>] [<code>-m</code>] [<code>-n</code>] [<code>-i </code><i>interface</i> | <code>-p </code><i>pcapfile</i>] [<code>-s </code><i>snaplen</i>] [<code>-f </code><i>services</i>] [<code>-t </code><i>trigger[,&#8230;]</i>]] [<code>-r</code>|<code>-w</code> <i>savefile</i>] [<i>expression</i>]</p>
<h2>Description</h2>
<p><code>dsniff</code> is a password sniffer which handles FTP, Telnet, SMTP, HTTP, POP, poppass, NNTP, IMAP, SNMP, LDAP, Rlogin, RIP, OSPF, PPTP MS-CHAP, NFS, VRRP, YP/NIS, SOCKS, X11, CVS, IRC, AIM, ICQ, Napster, PostgreSQL, Meeting Maker, Citrix ICA, Symantec pcAnywhere, NAI Sniffer, Microsoft SMB, Oracle SQL*Net, Sybase and Microsoft SQL protocols. </p>
<p> <code>dsniff</code> automatically detects and minimally parses each application protocol, only saving the interesting bits, and uses Berkeley DB as its output file format, only logging unique authentication attempts. Full TCP/IP reassembly is provided by <a href="/docs/linux/man/3-libnids/">libnids</a>(3). </p>
<p> I wrote <code>dsniff</code> with honest intentions &#8211; to audit my own network, and to demonstrate the insecurity of cleartext network protocols. Please do not abuse this software.</p>
<h2>Options</h2>
<dl>
<dt><code>-c</code></p>
<dd>Perform half-duplex TCP stream reassembly, to handle asymmetrically routed traffic (such as when using <a href="/docs/linux/man/8-arpspoof/">arpspoof</a>(8) to intercept client traffic bound for the local gateway).</p>
<dt><code>-d</code></p>
<dd>Enable debugging mode.</p>
<dt><code>-m</code></p>
<dd>Enable automatic protocol detection.</p>
<dt><code>-n</code></p>
<dd>Do not resolve IP addresses to hostnames.</p>
<dt><code>-i </code><i>interface</i></p>
<dd>Specify the interface to listen on.</p>
<dt><code>-p </code><i>pcapfile</i></p>
<dd>Rather than processing the contents of packets observed upon the network process the given PCAP capture file.</p>
<dt><code>-s </code><i>snaplen</i></p>
<dd>Analyze at most the first <i>snaplen</i> bytes of each TCP connection, rather than the default of 1024.</p>
<dt><code>-f </code><i>services</i></p>
<dd>Load triggers from a <i>services</i> file.</p>
<dt><code> -t </code><i>trigger</i>[,&#8230;]</p>
<dd>Load triggers from a comma-separated list, specified as <i>port</i>/<i>proto</i>=<i>service</i> (e.g. 80/tcp=http).</p>
<dt><code>-r </code><i>savefile</i></p>
<dd>Read sniffed sessions from a <i>savefile</i> created with the <code>-w</code> option.</p>
<dt><code>-w </code><i>file</i></p>
<dd>Write sniffed sessions to <i>savefile</i> rather than parsing and printing them out.</p>
<dt><i>expression</i></p>
<dd>Specify a <a href="/docs/linux/man/8-tcpdump/">tcpdump</a>(8) filter expression to select traffic to sniff.</dl>
<p> On a hangup signal <code>dsniff</code> will dump its current trigger table to <i>dsniff.services</i>.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/dsniff/dsniff.services</i></p>
<dd>Default trigger table</p>
<dt><i>/etc/dsniff/dsniff.magic</i></p>
<dd>Network protocol magic</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-arpspoof/">arpspoof</a>(8), <a href="/docs/linux/man/3-libnids/">libnids</a>(3), <a href="/docs/linux/man/5-services/">services</a>(5), <a href="/docs/linux/man/5-magic/">magic</a>(5)</p>
<h2>Author</h2>
<pre>Dug Song &lt;dugsong [at] monkey.org&gt;</pre>
<h2>Bugs</h2>
<p><code>dsniff</code>&#8216;s automatic protocol detection feature is based on the classic <a href="/docs/linux/man/1-file/">file</a>(1) command by Ian Darwin, and shares its historical limitations and bugs. </p>
