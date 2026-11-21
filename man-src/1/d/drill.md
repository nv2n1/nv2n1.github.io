---
title: "drill(1)"
name: "drill"
section: "1"
letter: "d"
url: "/docs/linux/man/1-drill/"
description: "drill – get (debug) information out of DNS(SEC)"
---

<h2>NAME</h2>
<p> drill &#8211; get (debug) information out of DNS(SEC)</p>
<h2>SYNOPSIS</h2>
<p> <code>drill</code> [ <i>OPTIONS</i> ] <i>name</i> [ <i>@server</i> ] [ <i>type</i> ] [ <i>class</i> ] </p>
<h2>DESCRIPTION</h2>
<p> <code>drill</code> is a tool to designed to get all sorts of information out of the DNS. It is specificly designed to be used with DNSSEC. </p>
<p> The name <code>drill</code> is a pun on <code>dig</code>. With <code>drill</code> you should be able get even more information than with <code>dig</code>. </p>
<p> If no arguments are given class defaults to &#8216;IN&#8217; and type to &#8216;A&#8217;. The server(s) specified in /etc/resolv.conf are used to query against. </p>
<p> <i>name</i> Ask for this name. </p>
<p> <i>@server</i> Send to query to this server. If not specified use the nameservers from <i>/etc/resolv.conf</i>. </p>
<p> <i>type</i> Ask for this RR type. If type is not given on the command line it defaults to &#8216;A&#8217;. Except when doing to reverse lookup when it defaults to &#8216;PTR&#8217;. </p>
<p> <i>class</i> Use this class when querying. </p>
<h2>SAMPLE USAGE</h2>
<p> <code>drill mx miek.nl</code> Show the MX records of the domain miek.nl </p>
<dl>
<dt><code>drill -S jelte.nlnetlabs.nl</code></dt>
<dd> Chase any signatures in the jelte.nlnetlab.nl domain. This option is only available when ldns has been compiled with openssl-support. </dd>
<dt><code>drill -TD <a rel="nofollow" href="http://www.example.com">www.example.com</a></code></dt>
<dd> Do a DNSSEC (-D) trace (-T) from the rootservers down to <a rel="nofollow" href="http://www.example.com">www.example.com</a>. This option only works when ldns has been compiled with openssl support. </dd>
<dt><code>drill -s dnskey jelte.nlnetlabs.nl</code></dt>
<dd> Show the DNSKEY record(s) for jelte.nlnetlabs.nl. For each found DNSKEY record also print the DS record. </dd>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-D</dt>
<dd> Enable DNSSEC in the query. When querying for DNSSEC types (DNSKEY, RRSIG, DS and NSEC) this is </code><i>not</i> automaticly enabled. </dd>
<dt><code>-T</dt>
<dd> Trace </code><i>name</i> from the root down. When using this option the @server and the type arguments are not used. </dd>
<dt><code>-S</dt>
<dd> Chase the signature(s) of &#8216;name&#8217; to a known key or as high up in the tree as possible. </dd>
<dt>-V </code><i>level</i></dt>
<dd> Be more verbose. Set level to 5 to see the actual query that is sent. </dd>
<dt><code>-Q</dt>
<dd> Quiet mode, this overrules -V. </dd>
<dt>-f </code><i>file</i></dt>
<dd> Read the query from a file. The query must be dumped with -w. </dd>
<dt><code>-i </code><i>file</i></dt>
<dd> read the answer from the file instead from the network. This aids in debugging and can be used to check if a query on disk is valid. If the file contains binary data it is assumed to be a query in network order. </dd>
<dt><code>-w </code><i>file</i></dt>
<dd> Write an answer packet to file. </dd>
<dt><code>-q </code><i>file</i></dt>
<dd> Write the query packet to file. </dd>
<dt><code>-v</dt>
<dd> Show drill&#8217;s version. </dd>
<dt>-h</dt>
<dd> Show a short help message. </dd>
</dl>
<p> </code></p>
<h3>QUERY OPTIONS</h3>
<dl>
<dt><code>-4</dt>
<dd> Stay on ip4. Only send queries to ip4 enabled nameservers. </dd>
<dt>-6</dt>
<dd> Stay on ip6. Only send queries to ip6 enabled nameservers. </dd>
<dt>-a</dt>
<dd> Use the resolver structure&#8217;s fallback mechanism if the answer is truncated (TC=1). If a truncated packet is received and this option is set, drill will first send a new query with EDNS0 buffer size 4096. </dd>
<p> If the EDNS0 buffer size was already set to 512+ bytes, or the above retry also results in a truncated answer, the resolver structure will fall back to TCP. </p>
<dt>-b </code><i>size</i></dt>
<dd> Use size as the buffer size in the EDNS0 pseudo RR. </dd>
<dt><code>-c </code><i>file</i></dt>
<dd> Use file instead of /etc/resolv.conf for nameserver configuration. </dd>
<dt><code>-d </code><i>domain</i></dt>
<dd> When tracing (-T), start from this domain instead of the root. </dd>
<dt><code>-t</dt>
<dd> Use TCP/IP when querying a server </dd>
<dt>-k </code><i>keyfile</i></dt>
<dd> Use this file to read a (trusted) key from. When this options is given <code>drill</code> tries to validate the current answer with this key. No chasing is done. When <code>drill</code> is doing a secure trace, this key will be used as trust anchor. Can contain a DNSKEY or a DS record. </dd>
<p> Alternatively, when DNSSEC enabled tracing (<code>-TD</code>) or signature chasing (<code>-S</code>), if <code>-k</code> is not specified, and a default trust anchor (/var/lib/unbound/root.key) exists and contains a valid DNSKEY or DS record, it will be used as the trust anchor. </p>
<dt><code>-o </code><i>mnemonic</i></dt>
<dd> Use this option to set or unset specific header bits. A bit is set by using the bit mnemonic in CAPITAL letters. A bit is unset when the mnemonic is given in lowercase. The following mnemonics are understood by <code>drill</code>: </dd>
<p>&nbsp;<wbr>&nbsp;<wbr>QR, qr: set, unset QueRy&nbsp;<wbr>(default: on)<br />
&nbsp;<wbr>&nbsp;<wbr>AA, aa: set, unset Authoritative Answer&nbsp;<wbr>(default: off)<br />
&nbsp;<wbr>&nbsp;<wbr>TC, tc: set, unset TrunCated&nbsp;<wbr>(default: off)<br />
&nbsp;<wbr>&nbsp;<wbr>RD, rd: set, unset Recursion Desired&nbsp;<wbr>(default: on)<br />
&nbsp;<wbr>&nbsp;<wbr>CD, cd: set, unset Checking Disabled&nbsp;<wbr>&nbsp;<wbr>(default: off)<br />
&nbsp;<wbr>&nbsp;<wbr>RA, ra: set, unset Recursion Available&nbsp;<wbr>&nbsp;<wbr>(default: off)<br />
&nbsp;<wbr>&nbsp;<wbr>AD, ad: set, unset Authenticated Data&nbsp;<wbr>(default: off) </p>
<p> Thus: <code>-o CD</code>, will enable Checking Disabled, which instructs the cache to not validate the answers it gives out. </p>
<dt><code>-p </code><i>port</i></dt>
<dd> Use this port instead of the default of 53. </dd>
<dt><code>-r </code><i>file</i></dt>
<dd> When tracing (-T), use file as a root servers hint file. </dd>
<dt><code>-s</dt>
<dd> When encountering a DNSKEY print the equivalent DS also. </dd>
<dt>-u</dt>
<dd> Use UDP when querying a server. This is the default. </dd>
<dt>-w </code><i>file</i></dt>
<dd> write the answer to a file. The file will contain a hexadecimal dump of the query. This can be used in conjunction with -f. </dd>
<dt><code>-x</dt>
<dd> Do a reverse loopup. The type argument is not used, it is preset to PTR. </dd>
<dt>-y </code><i>&lt;name:key[:algo]&gt;</i></dt>
<dd> specify named base64 tsig key, and optional an algorithm (defaults to hmac-md5.sig-alg.reg.int) </dd>
<dt><code>-z </code></dt>
<dd> don&#8217;t randomize the nameserver list before sending queries. </dd>
</dl>
<h2>FILES</h2>
<dl>
<dt>/var/lib/unbound/root.key</dt>
<dd> The file from which trusted keys are loaded when no <code>-k</code> option is given.</dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/8-unbound-anchor/">unbound-anchor</a>(8) </p>
<h2>AUTHOR</h2>
<p> Jelte Jansen and Miek Gieben. Both of NLnet Labs. </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;ldns-team [at] nlnetlabs.nl&gt;. </p>
<h2>BUGS</h2>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004-2008 NLnet Labs. Licensed under the revised BSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dig/">dig</a></code>(1), <i>RFC403{3,4,5}</i>. </p>
