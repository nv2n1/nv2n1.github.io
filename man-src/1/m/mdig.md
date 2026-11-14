---
title: "mdig(1)"
name: "mdig"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mdig/"
description: "mdig – DNS pipelined lookup utility"
---

<h2 class="name">NAME</h2>
<p> mdig &#8211; DNS pipelined lookup utility </p>
<h2>SYNOPSIS</h2>
<p> <code>mdig</code> <i>{@server</i>} [<code>-f</code> filename] [<code>-h</code>] [<code>-v</code>] [ [<code>-4</code>] | [<code>-6</code>] ] [<code>-m</code>] [<code>-b</code> address] [<code>-p</code> port#] [<code>-c</code> class] [<code>-t</code> type] [<code>-i</code>] [<code>-x</code> addr] [plusopt&#8230;] </p>
<p> <code>mdig</code> {<code>-h</code>} </p>
<p> <code>mdig</code> [@server] {global-opt&#8230;} { {local-opt&#8230;} {query} &#8230;}</p>
<h2>DESCRIPTION</h2>
<p> <code>mdig</code> is a multiple/pipelined query version of <i>dig</i>: instead of waiting for a response after sending each query, it begins by sending all queries. Responses are displayed in the order in which they are received, not in the order the corresponding queries were sent. </p>
<p> <code>mdig</code> options are a subset of the <i>dig</i> options, and are divided into &quot;anywhere options,&quot; which can occur anywhere, &quot;global options,&quot; which must occur before the query name (or they are ignored with a warning), and &quot;local options,&quot; which apply to the next query on the command line. </p>
<p> The <code>@server</code> option is a mandatory global option. It is the name or IP address of the name server to query. (Unlike <i>dig</i>, this value is not retrieved from <code>/etc/resolv.conf</code>.) It can be an IPv4 address in dotted-decimal notation, an IPv6 address in colon-delimited notation, or a hostname. When the supplied <code>server</code> argument is a hostname, <code>mdig</code> resolves that name before querying the name server. </p>
<p> <code>mdig</code> provides a number of query options which affect the way in which lookups are made and the results displayed. Some of these set or reset flag bits in the query header, some determine which sections of the answer get printed, and others determine the timeout and retry strategies. </p>
<p> Each query option is identified by a keyword preceded by a plus sign (<code>+</code>). Some keywords set or reset an option. These may be preceded by the string <code>no</code> to negate the meaning of that keyword. Other keywords assign values to options like the timeout interval. They have the form <code>+keyword=value</code>.</p>
<h2>ANYWHERE OPTIONS</h2>
<dl>
<dt><code>-f</code></p>
<dd> This option makes <code>mdig</code> operate in batch mode by reading a list of lookup requests to process from the file <code>filename</code>. The file contains a number of queries, one per line. Each entry in the file should be organized in the same way they would be presented as queries to <code>mdig</code> using the command-line interface.</p>
<dt><code>-h</code></p>
<dd> This option causes <code>mdig</code> to print detailed help information, with the full list of options, and exit.</p>
<dt><code>-v</code></p>
<dd> This option causes <code>mdig</code> to print the version number and exit.</dl>
<h2>GLOBAL OPTIONS</h2>
<dl>
<dt><code>-4</code></p>
<dd> This option forces <code>mdig</code> to only use IPv4 query transport.</p>
<dt><code>-6</code></p>
<dd> This option forces <code>mdig</code> to only use IPv6 query transport.</p>
<dt><code>-b address</code></p>
<dd> This option sets the source IP address of the query to <code>address</code>. This must be a valid address on one of the host&#8217;s network interfaces or &quot;0.0.0.0&quot; or &quot;::&quot;. An optional port may be specified by appending &quot;#&lt;port&gt;&quot;</p>
<dt><code>-m</code></p>
<dd> This option enables memory usage debugging.</p>
<dt><code>-p port#</code></p>
<dd> This option is used when a non-standard port number is to be queried. <code>port#</code> is the port number that <code>mdig</code> sends its queries to, instead of the standard DNS port number 53. This option is used to test a name server that has been configured to listen for queries on a non-standard port number. </p>
<p> The global query options are:</p>
<dt><code>+additional, +noadditional</code></p>
<dd> This option displays [or does not display] the additional section of a reply. The default is to display it.</p>
<dt><code>+all, +noall</code></p>
<dd> This option sets or clears all display flags.</p>
<dt><code>+answer, +noanswer</code></p>
<dd> This option displays [or does not display] the answer section of a reply. The default is to display it.</p>
<dt><code>+authority, +noauthority</code></p>
<dd> This option displays [or does not display] the authority section of a reply. The default is to display it.</p>
<dt><code>+besteffort, +nobesteffort</code></p>
<dd> This option attempts to display [or does not display] the contents of messages which are malformed. The default is to not display malformed answers.</p>
<dt><code>+burst</code></p>
<dd> This option delays queries until the start of the next second.</p>
<dt><code>+cl, +nocl</code></p>
<dd> This option displays [or does not display] the CLASS when printing the record.</p>
<dt><code>+comments, +nocomments</code></p>
<dd> This option toggles the display of comment lines in the output. The default is to print comments.</p>
<dt><code>+continue, +nocontinue</code></p>
<dd> This option toggles continuation on errors (e.g. timeouts).</p>
<dt><code>+crypto, +nocrypto</code></p>
<dd> This option toggles the display of cryptographic fields in DNSSEC records. The contents of these fields are unnecessary to debug most DNSSEC validation failures and removing them makes it easier to see the common failures. The default is to display the fields. When omitted, they are replaced by the string &quot;[omitted]&quot;; in the DNSKEY case, the key ID is displayed as the replacement, e.g., <code>[ key id = value ]</code>.</p>
<dt><code>+dscp=value</code></p>
<dd> This option formerly set the DSCP value used when sending a query. It is now obsolete, and has no effect.</p>
<dt><code>+multiline, +nomultiline</code></p>
<dd> This option toggles printing of records, like the SOA records, in a verbose multi-line format with human-readable comments. The default is to print each record on a single line, to facilitate machine parsing of the <code>mdig</code> output.</p>
<dt><code>+question, +noquestion</code></p>
<dd> This option prints [or does not print] the question section of a query when an answer is returned. The default is to print the question section as a comment.</p>
<dt><code>+rrcomments, +norrcomments</code></p>
<dd> This option toggles the display of per-record comments in the output (for example, human-readable key information about DNSKEY records). The default is not to print record comments unless multiline mode is active.</p>
<dt><code>+short, +noshort</code></p>
<dd> This option provides [or does not provide] a terse answer. The default is to print the answer in a verbose form.</p>
<dt><code>+split=W</code></p>
<dd> This option splits long hex- or base64-formatted fields in resource records into chunks of <code>W</code> characters (where <code>W</code> is rounded up to the nearest multiple of 4). <code>+nosplit</code> or <code>+split=0</code> causes fields not to be split. The default is 56 characters, or 44 characters when multiline mode is active.</p>
<dt><code>+tcp, +notcp</code></p>
<dd> This option uses [or does not use] TCP when querying name servers. The default behavior is to use UDP.</p>
<dt><code>+ttlid, +nottlid</code></p>
<dd> This option displays [or does not display] the TTL when printing the record.</p>
<dt><code>+ttlunits, +nottlunits</code></p>
<dd> This option displays [or does not display] the TTL in friendly human-readable time units of &quot;s&quot;, &quot;m&quot;, &quot;h&quot;, &quot;d&quot;, and &quot;w&quot;, representing seconds, minutes, hours, days, and weeks. This implies +ttlid.</p>
<dt><code>+vc, +novc</code></p>
<dd> This option uses [or does not use] TCP when querying name servers. This alternate syntax to <i>+tcp</i> is provided for backwards compatibility. The <code>vc</code> stands for &quot;virtual circuit&quot;.</dl>
<h2>LOCAL OPTIONS</h2>
<dl>
<dt><code>-c class</code></p>
<dd> This option sets the query class to <code>class</code>. It can be any valid query class which is supported in BIND 9. The default query class is &quot;IN&quot;.</p>
<dt><code>-t type</code></p>
<dd> This option sets the query type to <code>type</code>. It can be any valid query type which is supported in BIND 9. The default query type is &quot;A&quot;, unless the <i>-x</i> option is supplied to indicate a reverse lookup with the &quot;PTR&quot; query type.</p>
<dt><code>-x addr</code></p>
<dd> Reverse lookups &#8211; mapping addresses to names &#8211; are simplified by this option. <code>addr</code> is an IPv4 address in dotted-decimal notation, or a colon-delimited IPv6 address. <code>mdig</code> automatically performs a lookup for a query name like <code>11.12.13.10.in-addr.arpa</code> and sets the query type and class to PTR and IN respectively. By default, IPv6 addresses are looked up using nibble format under the IP6.ARPA domain. </p>
<p> The local query options are:</p>
<dt><code>+aaflag, +noaaflag</code></p>
<dd> This is a synonym for <i>+aaonly</i>, <i>+noaaonly</i>.</p>
<dt><code>+aaonly, +noaaonly</code></p>
<dd> This sets the <code>aa</code> flag in the query.</p>
<dt><code>+adflag, +noadflag</code></p>
<dd> This sets [or does not set] the AD (authentic data) bit in the query. This requests the server to return whether all of the answer and authority sections have all been validated as secure, according to the security policy of the server. AD=1 indicates that all records have been validated as secure and the answer is not from a OPT-OUT range. AD=0 indicates that some part of the answer was insecure or not validated. This bit is set by default.</p>
<dt><code>+bufsize=B</code></p>
<dd> This sets the UDP message buffer size advertised using EDNS0 to <code>B</code> bytes. The maximum and minimum sizes of this buffer are 65535 and 0 respectively. Values outside this range are rounded up or down appropriately. Values other than zero cause a EDNS query to be sent.</p>
<dt><code>+cdflag, +nocdflag</code></p>
<dd> This sets [or does not set] the CD (checking disabled) bit in the query. This requests the server to not perform DNSSEC validation of responses.</p>
<dt><code>+cookie=####, +nocookie</code></p>
<dd> This sends [or does not send] a COOKIE EDNS option, with an optional value. Replaying a COOKIE from a previous response allows the server to identify a previous client. The default is <code>+nocookie</code>.</p>
<dt><code>+dnssec, +nodnssec</code></p>
<dd> This requests that DNSSEC records be sent by setting the DNSSEC OK (DO) bit in the OPT record in the additional section of the query.</p>
<dt><code>+edns[=#], +noedns</code></p>
<dd> This specifies [or does not specify] the EDNS version to query with. Valid values are 0 to 255. Setting the EDNS version causes an EDNS query to be sent. <code>+noedns</code> clears the remembered EDNS version. EDNS is set to 0 by default.</p>
<dt><code>+ednsflags[=#], +noednsflags</code></p>
<dd> This sets the must-be-zero EDNS flag bits (Z bits) to the specified value. Decimal, hex, and octal encodings are accepted. Setting a named flag (e.g. DO) is silently ignored. By default, no Z bits are set.</p>
<dt><code>+ednsopt[=code[:value]], +noednsopt</code></p>
<dd> This specifies [or does not specify] an EDNS option with code point <code>code</code> and an optional payload of <code>value</code> as a hexadecimal string. <code>+noednsopt</code> clears the EDNS options to be sent.</p>
<dt><code>+expire, +noexpire</code></p>
<dd> This toggles sending of an EDNS Expire option.</p>
<dt><code>+nsid, +nonsid</code></p>
<dd> This toggles inclusion of an EDNS name server ID request when sending a query.</p>
<dt><code>+recurse, +norecurse</code></p>
<dd> This toggles the setting of the RD (recursion desired) bit in the query. This bit is set by default, which means <code>mdig</code> normally sends recursive queries.</p>
<dt><code>+retry=T</code></p>
<dd> This sets the number of times to retry UDP queries to server to <code>T</code> instead of the default, 2. Unlike <i>+tries</i>, this does not include the initial query.</p>
<dt><code>+subnet=addr[/prefix-length], +nosubnet</code></p>
<dd> This sends [or does not send] an EDNS Client Subnet option with the specified IP address or network prefix.</p>
<dt><code>mdig +subnet=0.0.0.0/0</code>, or simply <code>mdig +subnet=0</code></p>
<dd> This sends an EDNS client-subnet option with an empty address and a source prefix-length of zero, which signals a resolver that the client&#8217;s address information must <i>not</i> be used when resolving this query.</p>
<dt><code>+timeout=T</code></p>
<dd> This sets the timeout for a query to <code>T</code> seconds. The default timeout is 5 seconds for UDP transport and 10 for TCP. An attempt to set <code>T</code> to less than 1 results in a query timeout of 1 second being applied.</p>
<dt><code>+tries=T</code></p>
<dd> This sets the number of times to try UDP queries to server to <code>T</code> instead of the default, 3. If <code>T</code> is less than or equal to zero, the number of tries is silently rounded up to 1.</p>
<dt><code>+udptimeout=T</code></p>
<dd> This sets the timeout between UDP query retries to <code>T</code>.</p>
<dt><code>+unknownformat, +nounknownformat</code></p>
<dd> This prints [or does not print] all RDATA in unknown RR-type presentation format (see <i>RFC 3597</i>). The default is to print RDATA for known types in the type&#8217;s presentation format.</p>
<dt><code>+yaml, +noyaml</code></p>
<dd> This toggles printing of the responses in a detailed YAML format.</p>
<dt><code>+zflag, +nozflag</code></p>
<dd> This sets [or does not set] the last unassigned DNS header flag in a DNS query. This flag is off by default.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-dig/">dig</a>(1)</i>, <i>RFC 1035</i>.</p>
<h2>AUTHOR</h2>
<p> Internet Systems Consortium</p>
<h2>COPYRIGHT</h2>
<p> 2023, Internet Systems Consortium </p>
<h2>Index</h2>
