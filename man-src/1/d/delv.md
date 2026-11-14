---
title: "delv(1)"
name: "delv"
section: "1"
letter: "d"
url: "/docs/linux/man/1-delv/"
description: "delv – DNS lookup and validation utility"
---

<h2 class="name">NAME</h2>
<p> delv &#8211; DNS lookup and validation utility </p>
<h2>SYNOPSIS</h2>
<p> <code>delv</code> [@server] [ [<code>-4</code>] | [<code>-6</code>] ] [<code>-a</code> anchor-file] [<code>-b</code> address] [<code>-c</code> class] [<code>-d</code> level] [<code>-i</code>] [<code>-m</code>] [<code>-p</code> port#] [<code>-q</code> name] [<code>-t</code> type] [<code>-x</code> addr] [name] [type] [class] [queryopt&#8230;] </p>
<p> <code>delv</code> [<code>-h</code>] </p>
<p> <code>delv</code> [<code>-v</code>] </p>
<p> <code>delv</code> [queryopt&#8230;] [query&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>delv</code> is a tool for sending DNS queries and validating the results, using the same internal resolver and validator logic as <i>named</i>. </p>
<p> <code>delv</code> sends to a specified name server all queries needed to fetch and validate the requested data; this includes the original requested query, subsequent queries to follow CNAME or DNAME chains, queries for DNSKEY, and DS records to establish a chain of trust for DNSSEC validation. It does not perform iterative resolution, but simulates the behavior of a name server configured for DNSSEC validating and forwarding. </p>
<p> By default, responses are validated using the built-in DNSSEC trust anchor for the root zone (&quot;.&quot;). Records returned by <code>delv</code> are either fully validated or were not signed. If validation fails, an explanation of the failure is included in the output; the validation process can be traced in detail. Because <code>delv</code> does not rely on an external server to carry out validation, it can be used to check the validity of DNS responses in environments where local name servers may not be trustworthy. </p>
<p> Unless it is told to query a specific name server, <code>delv</code> tries each of the servers listed in <code>/etc/resolv.conf</code>. If no usable server addresses are found, <code>delv</code> sends queries to the localhost addresses (127.0.0.1 for IPv4, ::1 for IPv6). </p>
<p> When no command-line arguments or options are given, <code>delv</code> performs an NS query for &quot;.&quot; (the root zone).</p>
<h2>SIMPLE USAGE</h2>
<p> A typical invocation of <code>delv</code> looks like: </p>
<pre>
delv @server name type
</pre>
<p> where:</p>
<dl>
<dt><code>server</code></p>
<dd> is the name or IP address of the name server to query. This can be an IPv4 address in dotted-decimal notation or an IPv6 address in colon-delimited notation. When the supplied <code>server</code> argument is a hostname, <code>delv</code> resolves that name before querying that name server (note, however, that this initial lookup is <i>not</i> validated by DNSSEC). </p>
<p> If no <code>server</code> argument is provided, <code>delv</code> consults <code>/etc/resolv.conf</code>; if an address is found there, it queries the name server at that address. If either of the <i>-4</i> or <i>-6</i> options is in use, then only addresses for the corresponding transport are tried. If no usable addresses are found, <code>delv</code> sends queries to the localhost addresses (127.0.0.1 for IPv4, ::1 for IPv6).</p>
<dt><code>name</code></p>
<dd> is the domain name to be looked up.</p>
<dt><code>type</code></p>
<dd> indicates what type of query is required &#8211; ANY, A, MX, etc. <code>type</code> can be any valid query type. If no <code>type</code> argument is supplied, <code>delv</code> performs a lookup for an A record.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a anchor-file</code></p>
<dd> This option specifies a file from which to read DNSSEC trust anchors. The default is <code>/etc/bind/bind.keys</code>, which is included with BIND 9 and contains one or more trust anchors for the root zone (&quot;.&quot;). </p>
<p> Keys that do not match the root zone name are ignored. An alternate key name can be specified using the <i>+root</i> option. </p>
<p> Note: When reading the trust anchor file, <code>delv</code> treats <code>trust-anchors</code>, <code>initial-key</code>, and <code>static-key</code> identically. That is, for a managed key, it is the <i>initial</i> key that is trusted; <i>RFC 5011</i> key management is not supported. <code>delv</code> does not consult the managed-keys database maintained by <i>named</i>, which means that if either of the keys in <code>/etc/bind/bind.keys</code> is revoked and rolled over, <code>/etc/bind/bind.keys</code> must be updated to use DNSSEC validation in <code>delv</code>.</p>
<dt><code>-b address</code></p>
<dd> This option sets the source IP address of the query to <code>address</code>. This must be a valid address on one of the host&#8217;s network interfaces, or <code>0.0.0.0</code>, or <code>::</code>. An optional source port may be specified by appending <code>#&lt;port&gt;</code></p>
<dt><code>-c class</code></p>
<dd> This option sets the query class for the requested data. Currently, only class &quot;IN&quot; is supported in <code>delv</code> and any other value is ignored.</p>
<dt><code>-d level</code></p>
<dd> This option sets the systemwide debug level to <code>level</code>. The allowed range is from 0 to 99. The default is 0 (no debugging). Debugging traces from <code>delv</code> become more verbose as the debug level increases. See the <i>+mtrace</i>, <i>+rtrace</i>, and <i>+vtrace</i> options below for additional debugging details.</p>
<dt><code>-h</code></p>
<dd> This option displays the <code>delv</code> help usage output and exits.</p>
<dt><code>-i</code></p>
<dd> This option sets insecure mode, which disables internal DNSSEC validation. (Note, however, that this does not set the CD bit on upstream queries. If the server being queried is performing DNSSEC validation, then it does not return invalid data; this can cause <code>delv</code> to time out. When it is necessary to examine invalid data to debug a DNSSEC problem, use <i>dig +cd</i>.)</p>
<dt><code>-m</code></p>
<dd> This option enables memory usage debugging.</p>
<dt><code>-p port#</code></p>
<dd> This option specifies a destination port to use for queries, instead of the standard DNS port number 53. This option is used with a name server that has been configured to listen for queries on a non-standard port number.</p>
<dt><code>-q name</code></p>
<dd> This option sets the query name to <code>name</code>. While the query name can be specified without using the <i>-q</i> option, it is sometimes necessary to disambiguate names from types or classes (for example, when looking up the name &quot;ns&quot;, which could be misinterpreted as the type NS, or &quot;ch&quot;, which could be misinterpreted as class CH).</p>
<dt><code>-t type</code></p>
<dd> This option sets the query type to <code>type</code>, which can be any valid query type supported in BIND 9 except for zone transfer types AXFR and IXFR. As with <i>-q</i>, this is useful to distinguish query-name types or classes when they are ambiguous. It is sometimes necessary to disambiguate names from types. </p>
<p> The default query type is &quot;A&quot;, unless the <i>-x</i> option is supplied to indicate a reverse lookup, in which case it is &quot;PTR&quot;.</p>
<dt><code>-v</code></p>
<dd> This option prints the <code>delv</code> version and exits.</p>
<dt><code>-x addr</code></p>
<dd> This option performs a reverse lookup, mapping an address to a name. <code>addr</code> is an IPv4 address in dotted-decimal notation, or a colon-delimited IPv6 address. When <i>-x</i> is used, there is no need to provide the <code>name</code> or <code>type</code> arguments; <code>delv</code> automatically performs a lookup for a name like <code>11.12.13.10.in-addr.arpa</code> and sets the query type to PTR. IPv6 addresses are looked up using nibble format under the IP6.ARPA domain.</p>
<dt><code>-4</code></p>
<dd> This option forces <code>delv</code> to only use IPv4.</p>
<dt><code>-6</code></p>
<dd> This option forces <code>delv</code> to only use IPv6.</dl>
<h2>QUERY OPTIONS</h2>
<p> <code>delv</code> provides a number of query options which affect the way results are displayed, and in some cases the way lookups are performed. </p>
<p> Each query option is identified by a keyword preceded by a plus sign (<code>+</code>). Some keywords set or reset an option. These may be preceded by the string <code>no</code> to negate the meaning of that keyword. Other keywords assign values to options like the timeout interval. They have the form <code>+keyword=value</code>. The query options are:</p>
<dl>
<dt><code>+cdflag, +nocdflag</code></p>
<dd> This option controls whether to set the CD (checking disabled) bit in queries sent by <code>delv</code>. This may be useful when troubleshooting DNSSEC problems from behind a validating resolver. A validating resolver blocks invalid responses, making it difficult to retrieve them for analysis. Setting the CD flag on queries causes the resolver to return invalid responses, which <code>delv</code> can then validate internally and report the errors in detail.</p>
<dt><code>+class, +noclass</code></p>
<dd> This option controls whether to display the CLASS when printing a record. The default is to display the CLASS.</p>
<dt><code>+ttl, +nottl</code></p>
<dd> This option controls whether to display the TTL when printing a record. The default is to display the TTL.</p>
<dt><code>+rtrace, +nortrace</code></p>
<dd> This option toggles resolver fetch logging. This reports the name and type of each query sent by <code>delv</code> in the process of carrying out the resolution and validation process, including the original query and all subsequent queries to follow CNAMEs and to establish a chain of trust for DNSSEC validation. </p>
<p> This is equivalent to setting the debug level to 1 in the &quot;resolver&quot; logging category. Setting the systemwide debug level to 1 using the <i>-d</i> option produces the same output, but affects other logging categories as well.</p>
<dt><code>+mtrace, +nomtrace</code></p>
<dd> This option toggles message logging. This produces a detailed dump of the responses received by <code>delv</code> in the process of carrying out the resolution and validation process. </p>
<p> This is equivalent to setting the debug level to 10 for the &quot;packets&quot; module of the &quot;resolver&quot; logging category. Setting the systemwide debug level to 10 using the <i>-d</i> option produces the same output, but affects other logging categories as well.</p>
<dt><code>+vtrace, +novtrace</code></p>
<dd> This option toggles validation logging. This shows the internal process of the validator as it determines whether an answer is validly signed, unsigned, or invalid. </p>
<p> This is equivalent to setting the debug level to 3 for the &quot;validator&quot; module of the &quot;dnssec&quot; logging category. Setting the systemwide debug level to 3 using the <i>-d</i> option produces the same output, but affects other logging categories as well.</p>
<dt><code>+short, +noshort</code></p>
<dd> This option toggles between verbose and terse answers. The default is to print the answer in a verbose form.</p>
<dt><code>+comments, +nocomments</code></p>
<dd> This option toggles the display of comment lines in the output. The default is to print comments.</p>
<dt><code>+rrcomments, +norrcomments</code></p>
<dd> This option toggles the display of per-record comments in the output (for example, human-readable key information about DNSKEY records). The default is to print per-record comments.</p>
<dt><code>+crypto, +nocrypto</code></p>
<dd> This option toggles the display of cryptographic fields in DNSSEC records. The contents of these fields are unnecessary to debug most DNSSEC validation failures and removing them makes it easier to see the common failures. The default is to display the fields. When omitted, they are replaced by the string <code>[omitted]</code> or, in the DNSKEY case, the key ID is displayed as the replacement, e.g. <code>[ key id = value ]</code>.</p>
<dt><code>+trust, +notrust</code></p>
<dd> This option controls whether to display the trust level when printing a record. The default is to display the trust level.</p>
<dt><code>+split[=W], +nosplit</code></p>
<dd> This option splits long hex- or base64-formatted fields in resource records into chunks of <code>W</code> characters (where <code>W</code> is rounded up to the nearest multiple of 4). <code>+nosplit</code> or <code>+split=0</code> causes fields not to be split at all. The default is 56 characters, or 44 characters when multiline mode is active.</p>
<dt><code>+all, +noall</code></p>
<dd> This option sets or clears the display options <i>+comments</i>, <i>+rrcomments</i>, and <i>+trust</i> as a group.</p>
<dt><code>+multiline, +nomultiline</code></p>
<dd> This option prints long records (such as RRSIG, DNSKEY, and SOA records) in a verbose multi-line format with human-readable comments. The default is to print each record on a single line, to facilitate machine parsing of the <code>delv</code> output.</p>
<dt><code>+dnssec, +nodnssec</code></p>
<dd> This option indicates whether to display RRSIG records in the <code>delv</code> output. The default is to do so. Note that (unlike in <i>dig</i>) this does <i>not</i> control whether to request DNSSEC records or to validate them. DNSSEC records are always requested, and validation always occurs unless suppressed by the use of <i>-i</i> or <i>+noroot</i>.</p>
<dt><code>+root[=ROOT], +noroot</code></p>
<dd> This option indicates whether to perform conventional DNSSEC validation, and if so, specifies the name of a trust anchor. The default is to validate using a trust anchor of &quot;.&quot; (the root zone), for which there is a built-in key. If specifying a different trust anchor, then <i>-a</i> must be used to specify a file containing the key.</p>
<dt><code>+tcp, +notcp</code></p>
<dd> This option controls whether to use TCP when sending queries. The default is to use UDP unless a truncated response has been received.</p>
<dt><code>+unknownformat, +nounknownformat</code></p>
<dd> This option prints all RDATA in unknown RR-type presentation format (<i>RFC 3597</i>). The default is to print RDATA for known types in the type&#8217;s presentation format.</p>
<dt><code>+yaml, +noyaml</code></p>
<dd> This option prints response data in YAML format.</dl>
<h2>FILES</h2>
<p> <code>/etc/bind/bind.keys</code> </p>
<p> <code>/etc/resolv.conf</code></p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-dig/">dig</a>(1)</i>, <i><a href="/docs/linux/man/8-named/">named</a>(8)</i>, <i>RFC 4034</i>, <i>RFC 4035</i>, <i>RFC 4431</i>, <i>RFC 5074</i>, <i>RFC 5155</i>.</p>
<h2>AUTHOR</h2>
<p> Internet Systems Consortium</p>
<h2>COPYRIGHT</h2>
<p> 2023, Internet Systems Consortium </p>
<h2>Index</h2>
