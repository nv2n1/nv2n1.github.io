---
title: "dig(1)"
name: "dig"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dig/"
description: "dig – DNS lookup utility"
---

<h2 class="name">NAME</h2>
<p> dig &#8211; DNS lookup utility </p>
<h2>SYNOPSIS</h2>
<p> <code>dig</code> [@server] [<code>-b</code> address] [<code>-c</code> class] [<code>-f</code> filename] [<code>-k</code> filename] [<code>-m</code>] [<code>-p</code> port#] [<code>-q</code> name] [<code>-t</code> type] [<code>-v</code>] [<code>-x</code> addr] [<code>-y</code> [hmac:]name:key] [ [<code>-4</code>] | [<code>-6</code>] ] [name] [type] [class] [queryopt&#8230;] </p>
<p> <code>dig</code> [<code>-h</code>] </p>
<p> <code>dig</code> [global-queryopt&#8230;] [query&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>dig</code> is a flexible tool for interrogating DNS name servers. It performs DNS lookups and displays the answers that are returned from the name server(s) that were queried. Most DNS administrators use <code>dig</code> to troubleshoot DNS problems because of its flexibility, ease of use, and clarity of output. Other lookup tools tend to have less functionality than <code>dig</code>. </p>
<p> Although <code>dig</code> is normally used with command-line arguments, it also has a batch mode of operation for reading lookup requests from a file. A brief summary of its command-line arguments and options is printed when the <i>-h</i> option is given. The BIND 9 implementation of <code>dig</code> allows multiple lookups to be issued from the command line. </p>
<p> Unless it is told to query a specific name server, <code>dig</code> tries each of the servers listed in <code>/etc/resolv.conf</code>. If no usable server addresses are found, <code>dig</code> sends the query to the local host. </p>
<p> When no command-line arguments or options are given, <code>dig</code> performs an NS query for &quot;.&quot; (the root). </p>
<p> It is possible to set per-user defaults for <code>dig</code> via <code>${HOME}/.digrc</code>. This file is read and any options in it are applied before the command-line arguments. The <i>-r</i> option disables this feature, for scripts that need predictable behavior. </p>
<p> The IN and CH class names overlap with the IN and CH top-level domain names. Either use the <i>-t</i> and <i>-c</i> options to specify the type and class, use the <i>-q</i> to specify the domain name, or use &quot;IN.&quot; and &quot;CH.&quot; when looking up these top-level domains.</p>
<h2>SIMPLE USAGE</h2>
<p> A typical invocation of <code>dig</code> looks like: </p>
<pre>
dig @server name type
</pre>
<p> where:</p>
<dl>
<dt><code>server</code></p>
<dd> is the name or IP address of the name server to query. This can be an IPv4 address in dotted-decimal notation or an IPv6 address in colon-delimited notation. When the supplied <code>server</code> argument is a hostname, <code>dig</code> resolves that name before querying that name server. </p>
<p> If no <code>server</code> argument is provided, <code>dig</code> consults <code>/etc/resolv.conf</code>; if an address is found there, it queries the name server at that address. If either of the <i>-4</i> or <i>-6</i> options are in use, then only addresses for the corresponding transport are tried. If no usable addresses are found, <code>dig</code> sends the query to the local host. The reply from the name server that responds is displayed.</p>
<dt><code>name</code></p>
<dd> is the name of the resource record that is to be looked up.</p>
<dt><code>type</code></p>
<dd> indicates what type of query is required &#8211; ANY, A, MX, SIG, etc. <code>type</code> can be any valid query type. If no <code>type</code> argument is supplied, <code>dig</code> performs a lookup for an A record.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-4</code></p>
<dd> This option indicates that only IPv4 should be used.</p>
<dt><code>-6</code></p>
<dd> This option indicates that only IPv6 should be used.</p>
<dt><code>-b address[#port]</code></p>
<dd> This option sets the source IP address of the query. The <code>address</code> must be a valid address on one of the host&#8217;s network interfaces, or &quot;0.0.0.0&quot; or &quot;::&quot;. An optional port may be specified by appending <code>#port</code>.</p>
<dt><code>-c class</code></p>
<dd> This option sets the query class. The default <code>class</code> is IN; other classes are HS for Hesiod records or CH for Chaosnet records.</p>
<dt><code>-f file</code></p>
<dd> This option sets batch mode, in which <code>dig</code> reads a list of lookup requests to process from the given <code>file</code>. Each line in the file should be organized in the same way it would be presented as a query to <code>dig</code> using the command-line interface.</p>
<dt><code>-h</code></p>
<dd> Print a usage summary.</p>
<dt><code>-k keyfile</code></p>
<dd> This option tells <code>dig</code> to sign queries using TSIG or SIG(0) using a key read from the given file. Key files can be generated using <i>tsig-keygen</i>. When using TSIG authentication with <code>dig</code>, the name server that is queried needs to know the key and algorithm that is being used. In BIND, this is done by providing appropriate <code>key</code> and <code>server</code> statements in <i>named.conf</i> for TSIG and by looking up the KEY record in zone data for SIG(0).</p>
<dt><code>-m</code></p>
<dd> This option enables memory usage debugging.</p>
<dt><code>-p port</code></p>
<dd> This option sends the query to a non-standard port on the server, instead of the default port 53. This option is used to test a name server that has been configured to listen for queries on a non-standard port number.</p>
<dt><code>-q name</code></p>
<dd> This option specifies the domain name to query. This is useful to distinguish the <code>name</code> from other arguments.</p>
<dt><code>-r</code></p>
<dd> This option indicates that options from <code>${HOME}/.digrc</code> should not be read. This is useful for scripts that need predictable behavior.</p>
<dt><code>-t type</code></p>
<dd> This option indicates the resource record type to query, which can be any valid query type. If it is a resource record type supported in BIND 9, it can be given by the type mnemonic (such as <code>NS</code> or <code>AAAA</code>). The default query type is <code>A</code>, unless the <i>-x</i> option is supplied to indicate a reverse lookup. A zone transfer can be requested by specifying a type of AXFR. When an incremental zone transfer (IXFR) is required, set the <code>type</code> to <code>ixfr=N</code>. The incremental zone transfer contains all changes made to the zone since the serial number in the zone&#8217;s SOA record was <code>N</code>. </p>
<p> All resource record types can be expressed as <code>TYPEnn</code>, where <code>nn</code> is the number of the type. If the resource record type is not supported in BIND 9, the result is displayed as described in <i>RFC 3597</i>.</p>
<dt><code>-u</code></p>
<dd> This option indicates that print query times should be provided in microseconds instead of milliseconds.</p>
<dt><code>-v</code></p>
<dd> This option prints the version number and exits.</p>
<dt><code>-x addr</code></p>
<dd> This option sets simplified reverse lookups, for mapping addresses to names. The <code>addr</code> is an IPv4 address in dotted-decimal notation, or a colon-delimited IPv6 address. When the <i>-x</i> option is used, there is no need to provide the <code>name</code>, <code>class</code>, and <code>type</code> arguments. <code>dig</code> automatically performs a lookup for a name like <code>94.2.0.192.in-addr.arpa</code> and sets the query type and class to PTR and IN respectively. IPv6 addresses are looked up using nibble format under the IP6.ARPA domain.</p>
<dt><code>-y [hmac:]keyname:secret</code></p>
<dd> This option signs queries using TSIG with the given authentication key. <code>keyname</code> is the name of the key, and <code>secret</code> is the base64-encoded shared secret. <code>hmac</code> is the name of the key algorithm; valid choices are <code>hmac-md5</code>, <code>hmac-sha1</code>, <code>hmac-sha224</code>, <code>hmac-sha256</code>, <code>hmac-sha384</code>, or <code>hmac-sha512</code>. If <code>hmac</code> is not specified, the default is <code>hmac-md5</code>; if MD5 was disabled, the default is <code>hmac-sha256</code>. </p>
<p> <code>NOTE:</code> Only the <i>-k</i> option should be used, rather than the <i>-y</i> option, because with <i>-y</i> the shared secret is supplied as a command-line argument in clear text. This may be visible in the output from <code>ps1</code> or in a history file maintained by the user&#8217;s shell.</dl>
<h2>QUERY OPTIONS</h2>
<p> <code>dig</code> provides a number of query options which affect the way in which lookups are made and the results displayed. Some of these set or reset flag bits in the query header, some determine which sections of the answer get printed, and others determine the timeout and retry strategies. </p>
<p> Each query option is identified by a keyword preceded by a plus sign (<code>+</code>). Some keywords set or reset an option; these may be preceded by the string <code>no</code> to negate the meaning of that keyword. Other keywords assign values to options, like the timeout interval. They have the form <code>+keyword=value</code>. Keywords may be abbreviated, provided the abbreviation is unambiguous; for example, <i>+cd</i> is equivalent to <i>+cdflag</i>. The query options are:</p>
<dl>
<dt><code>+aaflag, +noaaflag</code></p>
<dd> This option is a synonym for <i>+aaonly</i>, <i>+noaaonly</i>.</p>
<dt><code>+aaonly, +noaaonly</code></p>
<dd> This option sets the <code>aa</code> flag in the query.</p>
<dt><code>+additional, +noadditional</code></p>
<dd> This option displays [or does not display] the additional section of a reply. The default is to display it.</p>
<dt><code>+adflag, +noadflag</code></p>
<dd> This option sets [or does not set] the AD (authentic data) bit in the query. This requests the server to return whether all of the answer and authority sections have been validated as secure, according to the security policy of the server. <code>AD=1</code> indicates that all records have been validated as secure and the answer is not from a OPT-OUT range. <code>AD=0</code> indicates that some part of the answer was insecure or not validated. This bit is set by default.</p>
<dt><code>+all, +noall</code></p>
<dd> This option sets or clears all display flags.</p>
<dt><code>+answer, +noanswer</code></p>
<dd> This option displays [or does not display] the answer section of a reply. The default is to display it.</p>
<dt><code>+authority, +noauthority</code></p>
<dd> This option displays [or does not display] the authority section of a reply. The default is to display it.</p>
<dt><code>+badcookie, +nobadcookie</code></p>
<dd> This option retries the lookup with a new server cookie if a BADCOOKIE response is received.</p>
<dt><code>+besteffort, +nobesteffort</code></p>
<dd> This option attempts to display the contents of messages which are malformed. The default is to not display malformed answers.</p>
<dt><code>+bufsize[=B]</code></p>
<dd> This option sets the UDP message buffer size advertised using EDNS0 to <code>B</code> bytes. The maximum and minimum sizes of this buffer are 65535 and 0, respectively. <code>+bufsize</code> restores the default buffer size.</p>
<dt><code>+cd, +cdflag, +nocdflag</code></p>
<dd> This option sets [or does not set] the CD (checking disabled) bit in the query. This requests the server to not perform DNSSEC validation of responses.</p>
<dt><code>+class, +noclass</code></p>
<dd> This option displays [or does not display] the CLASS when printing the record.</p>
<dt><code>+cmd, +nocmd</code></p>
<dd> This option toggles the printing of the initial comment in the output, identifying the version of <code>dig</code> and the query options that have been applied. This option always has a global effect; it cannot be set globally and then overridden on a per-lookup basis. The default is to print this comment.</p>
<dt><code>+comments, +nocomments</code></p>
<dd> This option toggles the display of some comment lines in the output, with information about the packet header and OPT pseudosection, and the names of the response section. The default is to print these comments. </p>
<p> Other types of comments in the output are not affected by this option, but can be controlled using other command-line switches. These include <i>+cmd</i>, <i>+question</i>, <i>+stats</i>, and <i>+rrcomments</i>.</p>
<dt><code>+cookie=####, +nocookie</code></p>
<dd> This option sends [or does not send] a COOKIE EDNS option, with an optional value. Replaying a COOKIE from a previous response allows the server to identify a previous client. The default is <code>+cookie</code>. </p>
<p> <code>+cookie</code> is also set when <i>+trace</i> is set to better emulate the default queries from a nameserver.</p>
<dt><code>+crypto, +nocrypto</code></p>
<dd> This option toggles the display of cryptographic fields in DNSSEC records. The contents of these fields are unnecessary for debugging most DNSSEC validation failures and removing them makes it easier to see the common failures. The default is to display the fields. When omitted, they are replaced by the string <code>[omitted]</code> or, in the DNSKEY case, the key ID is displayed as the replacement, e.g. <code>[ key id = value ]</code>.</p>
<dt><code>+defname, +nodefname</code></p>
<dd> This option, which is deprecated, is treated as a synonym for <i>+search</i>, <i>+nosearch</i>.</p>
<dt><code>+dns64prefix, +nodns64prefix</code></p>
<dd> Lookup IPV4ONLY.ARPA AAAA and print any DNS64 prefixes found.</p>
<dt><code>+dnssec, +do, +nodnssec, +nodo</code></p>
<dd> This option requests that DNSSEC records be sent by setting the DNSSEC OK (DO) bit in the OPT record in the additional section of the query.</p>
<dt><code>+domain=somename</code></p>
<dd> This option sets the search list to contain the single domain <code>somename</code>, as if specified in a <code>domain</code> directive in <code>/etc/resolv.conf</code>, and enables search list processing as if the <i>+search</i> option were given.</p>
<dt><code>+dscp=value</code></p>
<dd> This option formerly set the DSCP value used when sending a query. It is now obsolete, and has no effect.</p>
<dt><code>+edns[=#], +noedns</code></p>
<dd> This option specifies the EDNS version to query with. Valid values are 0 to 255. Setting the EDNS version causes an EDNS query to be sent. <code>+noedns</code> clears the remembered EDNS version. EDNS is set to 0 by default.</p>
<dt><code>+ednsflags[=#], +noednsflags</code></p>
<dd> This option sets the must-be-zero EDNS flags bits (Z bits) to the specified value. Decimal, hex, and octal encodings are accepted. Setting a named flag (e.g., DO) is silently ignored. By default, no Z bits are set.</p>
<dt><code>+ednsnegotiation, +noednsnegotiation</code></p>
<dd> This option enables/disables EDNS version negotiation. By default, EDNS version negotiation is enabled.</p>
<dt><code>+ednsopt[=code[:value]], +noednsopt</code></p>
<dd> This option specifies the EDNS option with code point <code>code</code> and an optional payload of <code>value</code> as a hexadecimal string. <code>code</code> can be either an EDNS option name (for example, <code>NSID</code> or <code>ECS</code>) or an arbitrary numeric value. <code>+noednsopt</code> clears the EDNS options to be sent.</p>
<dt><code>+expire, +noexpire</code></p>
<dd> This option sends an EDNS Expire option.</p>
<dt><code>+fail, +nofail</code></p>
<dd> This option indicates that <i>named</i> should try [or not try] the next server if a SERVFAIL is received. The default is to not try the next server, which is the reverse of normal stub resolver behavior.</p>
<dt><code>+fuzztime[=value], +nofuzztime</code></p>
<dd> This option allows the signing time to be specified when generating signed messages. If a value is specified it is the seconds since 00:00:00 January 1, 1970 UTC ignoring leap seconds. If no value is specified 1646972129 (Fri 11 Mar 2022 04:15:29 UTC) is used. The default is <code>+nofuzztime</code> and the current time is used.</p>
<dt><code>+header-only, +noheader-only</code></p>
<dd> This option sends a query with a DNS header without a question section. The default is to add a question section. The query type and query name are ignored when this is set.</p>
<dt><code>+https[=value], +nohttps</code></p>
<dd> This option indicates whether to use DNS over HTTPS (DoH) when querying name servers. When this option is in use, the port number defaults to 443. The HTTP POST request mode is used when sending the query. </p>
<p> If <code>value</code> is specified, it will be used as the HTTP endpoint in the query URI; the default is <code>/dns-query</code>. So, for example, <code>dig @example.com +https</code> will use the URI <code><a rel="nofollow" href="https://example.com/dns-query">https://example.com/dns-query</a></code>.</p>
<dt><code>+https-get[=value], +nohttps-get</code></p>
<dd> Similar to <i>+https</i>, except that the HTTP GET request mode is used when sending the query.</p>
<dt><code>+https-post[=value], +nohttps-post</code></p>
<dd> Same as <i>+https</i>.</p>
<dt><code>+http-plain[=value], +nohttp-plain</code></p>
<dd> Similar to <i>+https</i>, except that HTTP queries will be sent over a non-encrypted channel. When this option is in use, the port number defaults to 80 and the HTTP request mode is POST.</p>
<dt><code>+http-plain-get[=value], +nohttp-plain-get</code></p>
<dd> Similar to <i>+http-plain</i>, except that the HTTP request mode is GET.</p>
<dt><code>+http-plain-post[=value], +nohttp-plain-post</code></p>
<dd> Same as <i>+http-plain</i>.</p>
<dt><code>+identify, +noidentify</code></p>
<dd> This option shows [or does not show] the IP address and port number that supplied the answer, when the <i>+short</i> option is enabled. If short form answers are requested, the default is not to show the source address and port number of the server that provided the answer.</p>
<dt><code>+idnin, +noidnin</code></p>
<dd> This option processes [or does not process] IDN domain names on input. This requires <code>IDN SUPPORT</code> to have been enabled at compile time. </p>
<p> The default is to process IDN input when standard output is a tty. The IDN processing on input is disabled when <code>dig</code> output is redirected to files, pipes, and other non-tty file descriptors.</p>
<dt><code>+idnout, +noidnout</code></p>
<dd> This option converts [or does not convert] puny code on output. This requires <code>IDN SUPPORT</code> to have been enabled at compile time. </p>
<p> The default is to process puny code on output when standard output is a tty. The puny code processing on output is disabled when <code>dig</code> output is redirected to files, pipes, and other non-tty file descriptors.</p>
<dt><code>+ignore, +noignore</code></p>
<dd> This option ignores [or does not ignore] truncation in UDP responses instead of retrying with TCP. By default, TCP retries are performed.</p>
<dt><code>+keepalive, +nokeepalive</code></p>
<dd> This option sends [or does not send] an EDNS Keepalive option.</p>
<dt><code>+keepopen, +nokeepopen</code></p>
<dd> This option keeps [or does not keep] the TCP socket open between queries, and reuses it rather than creating a new TCP socket for each lookup. The default is <code>+nokeepopen</code>.</p>
<dt><code>+multiline, +nomultiline</code></p>
<dd> This option prints [or does not print] records, like the SOA records, in a verbose multi-line format with human-readable comments. The default is to print each record on a single line to facilitate machine parsing of the <code>dig</code> output.</p>
<dt><code>+ndots=D</code></p>
<dd> This option sets the number of dots (<code>D</code>) that must appear in <code>name</code> for it to be considered absolute. The default value is that defined using the <code>ndots</code> statement in <code>/etc/resolv.conf</code>, or 1 if no <code>ndots</code> statement is present. Names with fewer dots are interpreted as relative names, and are searched for in the domains listed in the <code>search</code> or <code>domain</code> directive in <code>/etc/resolv.conf</code> if <i>+search</i> is set.</p>
<dt><code>+nsid, +nonsid</code></p>
<dd> When enabled, this option includes an EDNS name server ID request when sending a query.</p>
<dt><code>+nssearch, +nonssearch</code></p>
<dd> When this option is set, <code>dig</code> attempts to find the authoritative name servers for the zone containing the name being looked up, and display the SOA record that each name server has for the zone. Addresses of servers that did not respond are also printed.</p>
<dt><code>+onesoa, +noonesoa</code></p>
<dd> When enabled, this option prints only one (starting) SOA record when performing an AXFR. The default is to print both the starting and ending SOA records.</p>
<dt><code>+opcode=value, +noopcode</code></p>
<dd> When enabled, this option sets (restores) the DNS message opcode to the specified value. The default value is QUERY (0).</p>
<dt><code>+padding=value</code></p>
<dd> This option pads the size of the query packet using the EDNS Padding option to blocks of <code>value</code> bytes. For example, <code>+padding=32</code> causes a 48-byte query to be padded to 64 bytes. The default block size is 0, which disables padding; the maximum is 512. Values are ordinarily expected to be powers of two, such as 128; however, this is not mandatory. Responses to padded queries may also be padded, but only if the query uses TCP or DNS COOKIE.</p>
<dt><code>+qid=value</code></p>
<dd> This option specifies the query ID to use when sending queries.</p>
<dt><code>+qr, +noqr</code></p>
<dd> This option toggles the display of the query message as it is sent. By default, the query is not printed.</p>
<dt><code>+question, +noquestion</code></p>
<dd> This option toggles the display of the question section of a query when an answer is returned. The default is to print the question section as a comment.</p>
<dt><code>+raflag, +noraflag</code></p>
<dd> This option sets [or does not set] the RA (Recursion Available) bit in the query. The default is <code>+noraflag</code>. This bit is ignored by the server for QUERY.</p>
<dt><code>+rdflag, +nordflag</code></p>
<dd> This option is a synonym for <i>+recurse</i>, <i>+norecurse</i>.</p>
<dt><code>+recurse, +norecurse</code></p>
<dd> This option toggles the setting of the RD (recursion desired) bit in the query. This bit is set by default, which means <code>dig</code> normally sends recursive queries. Recursion is automatically disabled when the <i>+nssearch</i> or <i>+trace</i> query option is used.</p>
<dt><code>+retry=T</code></p>
<dd> This option sets the number of times to retry UDP and TCP queries to server to <code>T</code> instead of the default, 2. Unlike <i>+tries</i>, this does not include the initial query.</p>
<dt><code>+rrcomments, +norrcomments</code></p>
<dd> This option toggles the display of per-record comments in the output (for example, human-readable key information about DNSKEY records). The default is not to print record comments unless multiline mode is active.</p>
<dt><code>+search, +nosearch</code></p>
<dd> This option uses [or does not use] the search list defined by the searchlist or domain directive in <code>resolv.conf</code>, if any. The search list is not used by default. </p>
<p> <code>ndots</code> from <code>resolv.conf</code> (default 1), which may be overridden by <i>+ndots</i>, determines whether the name is treated as relative and hence whether a search is eventually performed.</p>
<dt><code>+short, +noshort</code></p>
<dd> This option toggles whether a terse answer is provided. The default is to print the answer in a verbose form. This option always has a global effect; it cannot be set globally and then overridden on a per-lookup basis.</p>
<dt><code>+showbadcookie, +noshowbadcookie</code></p>
<dd> This option toggles whether to show the message containing the BADCOOKIE rcode before retrying the request or not. The default is to not show the messages.</p>
<dt><code>+showsearch, +noshowsearch</code></p>
<dd> This option performs [or does not perform] a search showing intermediate results.</p>
<dt><code>+sigchase, +nosigchase</code></p>
<dd> This feature is now obsolete and has been removed; use <i>delv</i> instead.</p>
<dt><code>+split=W</code></p>
<dd> This option splits long hex- or base64-formatted fields in resource records into chunks of <code>W</code> characters (where <code>W</code> is rounded up to the nearest multiple of 4). <code>+nosplit</code> or <code>+split=0</code> causes fields not to be split at all. The default is 56 characters, or 44 characters when multiline mode is active.</p>
<dt><code>+stats, +nostats</code></p>
<dd> This option toggles the printing of statistics: when the query was made, the size of the reply, etc. The default behavior is to print the query statistics as a comment after each lookup.</p>
<dt><code>+subnet=addr[/prefix-length], +nosubnet</code></p>
<dd> This option sends [or does not send] an EDNS CLIENT-SUBNET option with the specified IP address or network prefix. </p>
<p> <code>dig +subnet=0.0.0.0/0</code>, or simply <code>dig +subnet=0</code> for short, sends an EDNS CLIENT-SUBNET option with an empty address and a source prefix-length of zero, which signals a resolver that the client&#8217;s address information must <i>not</i> be used when resolving this query.</p>
<dt><code>+tcflag, +notcflag</code></p>
<dd> This option sets [or does not set] the TC (TrunCation) bit in the query. The default is <code>+notcflag</code>. This bit is ignored by the server for QUERY.</p>
<dt><code>+tcp, +notcp</code></p>
<dd> This option indicates whether to use TCP when querying name servers. The default behavior is to use UDP unless a type <code>any</code> or <code>ixfr=N</code> query is requested, in which case the default is TCP. AXFR queries always use TCP. To prevent retry over TCP when TC=1 is returned from a UDP query, use <code>+ignore</code>.</p>
<dt><code>+timeout=T</code></p>
<dd> This option sets the timeout for a query to <code>T</code> seconds. The default timeout is 5 seconds. An attempt to set <code>T</code> to less than 1 is silently set to 1.</p>
<dt><code>+tls, +notls</code></p>
<dd> This option indicates whether to use DNS over TLS (DoT) when querying name servers. When this option is in use, the port number defaults to 853.</p>
<dt><code>+tls-ca[=file-name], +notls-ca</code></p>
<dd> This option enables remote server TLS certificate validation for DNS transports, relying on TLS. Certificate authorities certificates are loaded from the specified PEM file (<code>file-name</code>). If the file is not specified, the default certificates from the global certificates store are used.</p>
<dt><code>+tls-certfile=file-name, +tls-keyfile=file-name, +notls-certfile, +notls-keyfile</code></p>
<dd> These options set the state of certificate-based client authentication for DNS transports, relying on TLS. Both certificate chain file and private key file are expected to be in PEM format. Both options must be specified at the same time.</p>
<dt><code>+tls-hostname=hostname, +notls-hostname</code></p>
<dd> This option makes <code>dig</code> use the provided hostname during remote server TLS certificate verification. Otherwise, the DNS server name is used. This option has no effect if <i>+tls-ca</i> is not specified.</p>
<dt><code>+topdown, +notopdown</code></p>
<dd> This feature is related to <i>dig +sigchase</i>, which is obsolete and has been removed. Use <i>delv</i> instead.</p>
<dt><code>+trace, +notrace</code></p>
<dd> This option toggles tracing of the delegation path from the root name servers for the name being looked up. Tracing is disabled by default. When tracing is enabled, <code>dig</code> makes iterative queries to resolve the name being looked up. It follows referrals from the root servers, showing the answer from each server that was used to resolve the lookup. </p>
<p> If <code>@server</code> is also specified, it affects only the initial query for the root zone name servers. </p>
<p> <i>+dnssec</i> is also set when <i>+trace</i> is set, to better emulate the default queries from a name server.</p>
<dt><code>+tries=T</code></p>
<dd> This option sets the number of times to try UDP and TCP queries to server to <code>T</code> instead of the default, 3. If <code>T</code> is less than or equal to zero, the number of tries is silently rounded up to 1.</p>
<dt><code>+trusted-key=####</code></p>
<dd> This option formerly specified trusted keys for use with <i>dig +sigchase</i>. This feature is now obsolete and has been removed; use <i>delv</i> instead.</p>
<dt><code>+ttlid, +nottlid</code></p>
<dd> This option displays [or does not display] the TTL when printing the record.</p>
<dt><code>+ttlunits, +nottlunits</code></p>
<dd> This option displays [or does not display] the TTL in friendly human-readable time units of <code>s</code>, <code>m</code>, <code>h</code>, <code>d</code>, and <code>w</code>, representing seconds, minutes, hours, days, and weeks. This implies <i>+ttlid</i>.</p>
<dt><code>+unknownformat, +nounknownformat</code></p>
<dd> This option prints all RDATA in unknown RR type presentation format (<i>RFC 3597</i>). The default is to print RDATA for known types in the type&#8217;s presentation format.</p>
<dt><code>+vc, +novc</code></p>
<dd> This option uses [or does not use] TCP when querying name servers. This alternate syntax to <i>+tcp</i> is provided for backwards compatibility. The <code>vc</code> stands for &quot;virtual circuit.&quot;</p>
<dt><code>+yaml, +noyaml</code></p>
<dd> When enabled, this option prints the responses (and, if <i>+qr</i> is in use, also the outgoing queries) in a detailed YAML format.</p>
<dt><code>+zflag, +nozflag</code></p>
<dd> This option sets [or does not set] the last unassigned DNS header flag in a DNS query. This flag is off by default.</dl>
<h2>MULTIPLE QUERIES</h2>
<p> The BIND 9 implementation of <code>dig</code> supports specifying multiple queries on the command line (in addition to supporting the <i>-f</i> batch file option). Each of those queries can be supplied with its own set of flags, options, and query options. </p>
<p> In this case, each <code>query</code> argument represents an individual query in the command-line syntax described above. Each consists of any of the standard options and flags, the name to be looked up, an optional query type and class, and any query options that should be applied to that query. </p>
<p> A global set of query options, which should be applied to all queries, can also be supplied. These global query options must precede the first tuple of name, class, type, options, flags, and query options supplied on the command line. Any global query options (except <i>+cmd</i> and <i>+short</i> options) can be overridden by a query-specific set of query options. For example: </p>
<pre>
dig +qr <a rel="nofollow" href="http://www.isc.org">www.isc.org</a> any -x 127.0.0.1 isc.org ns +noqr
</pre>
<p> shows how <code>dig</code> can be used from the command line to make three lookups: an ANY query for <code><a rel="nofollow" href="http://www.isc.org">www.isc.org</a></code>, a reverse lookup of 127.0.0.1, and a query for the NS records of <code>isc.org</code>. A global query option of <i>+qr</i> is applied, so that <code>dig</code> shows the initial query it made for each lookup. The final query has a local query option of <i>+noqr</i> which means that <code>dig</code> does not print the initial query when it looks up the NS records for <code>isc.org</code>.</p>
<h2>IDN SUPPORT</h2>
<p> If <code>dig</code> has been built with IDN (internationalized domain name) support, it can accept and display non-ASCII domain names. <code>dig</code> appropriately converts character encoding of a domain name before sending a request to a DNS server or displaying a reply from the server. To turn off IDN support, use the parameters <i>+idnin</i> and <i>+idnout</i>, or define the <code>IDN_DISABLE</code> environment variable.</p>
<h2>RETURN CODES</h2>
<p> <code>dig</code> return codes are:</p>
<dl>
<dt><code>0</code></p>
<dd> DNS response received, including NXDOMAIN status</p>
<dt><code>1</code></p>
<dd> Usage error</p>
<dt><code>8</code></p>
<dd> Couldn&#8217;t open batch file</p>
<dt><code>9</code></p>
<dd> No reply from server</p>
<dt><code>10</code></p>
<dd> Internal error</dl>
<h2>FILES</h2>
<p> <code>/etc/resolv.conf</code> </p>
<p> <code>${HOME}/.digrc</code></p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-delv/">delv</a>(1)</i>, <i><a href="/docs/linux/man/1-host/">host</a>(1)</i>, <i><a href="/docs/linux/man/8-named/">named</a>(8)</i>, <i><a href="/docs/linux/man/8-dnssec-keygen/">dnssec-keygen</a>(8)</i>, <i>RFC 1035</i>.</p>
<h2>BUGS</h2>
<p> There are probably too many query options.</p>
<h2>AUTHOR</h2>
<p> Internet Systems Consortium</p>
<h2>COPYRIGHT</h2>
<p> 2023, Internet Systems Consortium </p>
<h2>Index</h2>
