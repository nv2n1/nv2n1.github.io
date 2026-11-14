---
title: "host(1)"
name: "host"
section: "1"
letter: "h"
url: "/docs/linux/man/1-host/"
description: "host – DNS lookup utility"
---

<h2 class="name">NAME</h2>
<p> host &#8211; DNS lookup utility </p>
<h2>SYNOPSIS</h2>
<p> <code>host</code> [<code>-aACdlnrsTUwv</code>] [<code>-c</code> class] [<code>-N</code> ndots] [<code>-p</code> port] [<code>-R</code> number] [<code>-t</code> type] [<code>-W</code> wait] [<code>-m</code> flag] [ [<code>-4</code>] | [<code>-6</code>] ] [<code>-v</code>] [<code>-V</code>] {name} [server]</p>
<h2>DESCRIPTION</h2>
<p> <code>host</code> is a simple utility for performing DNS lookups. It is normally used to convert names to IP addresses and vice versa. When no arguments or options are given, <code>host</code> prints a short summary of its command-line arguments and options. </p>
<p> <code>name</code> is the domain name that is to be looked up. It can also be a dotted-decimal IPv4 address or a colon-delimited IPv6 address, in which case <code>host</code> by default performs a reverse lookup for that address. <code>server</code> is an optional argument which is either the name or IP address of the name server that <code>host</code> should query instead of the server or servers listed in <code>/etc/resolv.conf</code>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-4</code></p>
<dd> This option specifies that only IPv4 should be used for query transport. See also the <i>-6</i> option.</p>
<dt><code>-6</code></p>
<dd> This option specifies that only IPv6 should be used for query transport. See also the <i>-4</i> option.</p>
<dt><code>-a</code></p>
<dd> The <i>-a</i> (&quot;all&quot;) option is normally equivalent to <i>-v</i> <i>-t ANY</i>. It also affects the behavior of the <i>-l</i> list zone option.</p>
<dt><code>-A</code></p>
<dd> The <i>-A</i> (&quot;almost all&quot;) option is equivalent to <i>-a</i>, except that RRSIG, NSEC, and NSEC3 records are omitted from the output.</p>
<dt><code>-c class</code></p>
<dd> This option specifies the query class, which can be used to lookup HS (Hesiod) or CH (Chaosnet) class resource records. The default class is IN (Internet).</p>
<dt><code>-C</code></p>
<dd> This option indicates that <i>named</i> should check consistency, meaning that <code>host</code> queries the SOA records for zone <code>name</code> from all the listed authoritative name servers for that zone. The list of name servers is defined by the NS records that are found for the zone.</p>
<dt><code>-d</code></p>
<dd> This option prints debugging traces, and is equivalent to the <i>-v</i> verbose option.</p>
<dt><code>-l</code></p>
<dd> This option tells <i>named</i> to list the zone, meaning the <code>host</code> command performs a zone transfer of zone <code>name</code> and prints out the NS, PTR, and address records (A/AAAA). </p>
<p> Together, the <i>-l</i> <i>-a</i> options print all records in the zone.</p>
<dt><code>-N ndots</code></p>
<dd> This option specifies the number of dots (<code>ndots</code>) that have to be in <code>name</code> for it to be considered absolute. The default value is that defined using the <code>ndots</code> statement in <code>/etc/resolv.conf</code>, or 1 if no <code>ndots</code> statement is present. Names with fewer dots are interpreted as relative names, and are searched for in the domains listed in the <code>search</code> or <code>domain</code> directive in <code>/etc/resolv.conf</code>.</p>
<dt><code>-p port</code></p>
<dd> This option specifies the port to query on the server. The default is 53.</p>
<dt><code>-r</code></p>
<dd> This option specifies a non-recursive query; setting this option clears the RD (recursion desired) bit in the query. This means that the name server receiving the query does not attempt to resolve <code>name</code>. The <i>-r</i> option enables <code>host</code> to mimic the behavior of a name server by making non-recursive queries, and expecting to receive answers to those queries that can be referrals to other name servers.</p>
<dt><code>-R number</code></p>
<dd> This option specifies the number of retries for UDP queries. If <code>number</code> is negative or zero, the number of retries is silently set to 1. The default value is 1, or the value of the <code>attempts</code> option in <code>/etc/resolv.conf</code>, if set.</p>
<dt><code>-s</code></p>
<dd> This option tells <i>named</i> <i>not</i> to send the query to the next nameserver if any server responds with a SERVFAIL response, which is the reverse of normal stub resolver behavior.</p>
<dt><code>-t type</code></p>
<dd> This option specifies the query type. The <code>type</code> argument can be any recognized query type: CNAME, NS, SOA, TXT, DNSKEY, AXFR, etc. </p>
<p> When no query type is specified, <code>host</code> automatically selects an appropriate query type. By default, it looks for A, AAAA, and MX records. If the <i>-C</i> option is given, queries are made for SOA records. If <code>name</code> is a dotted-decimal IPv4 address or colon-delimited IPv6 address, <code>host</code> queries for PTR records. </p>
<p> If a query type of IXFR is chosen, the starting serial number can be specified by appending an equals sign (=), followed by the starting serial number, e.g., <i>-t IXFR=12345678</i>.</p>
<dt><code>-T, -U</code></p>
<dd> This option specifies TCP or UDP. By default, <code>host</code> uses UDP when making queries; the <i>-T</i> option makes it use a TCP connection when querying the name server. TCP is automatically selected for queries that require it, such as zone transfer (AXFR) requests. Type <code>ANY</code> queries default to TCP, but can be forced to use UDP initially via <i>-U</i>.</p>
<dt><code>-m flag</code></p>
<dd> This option sets memory usage debugging: the flag can be <code>record</code>, <code>usage</code>, or <code>trace</code>. The <i>-m</i> option can be specified more than once to set multiple flags.</p>
<dt><code>-v</code></p>
<dd> This option sets verbose output, and is equivalent to the <i>-d</i> debug option. Verbose output can also be enabled by setting the <code>debug</code> option in <code>/etc/resolv.conf</code>.</p>
<dt><code>-V</code></p>
<dd> This option prints the version number and exits.</p>
<dt><code>-w</code></p>
<dd> This option sets &quot;wait forever&quot;: the query timeout is set to the maximum possible. See also the <i>-W</i> option.</p>
<dt><code>-W wait</code></p>
<dd> This options sets the length of the wait timeout, indicating that <i>named</i> should wait for up to <code>wait</code> seconds for a reply. If <code>wait</code> is less than 1, the wait interval is set to 1 second. </p>
<p> By default, <code>host</code> waits for 5 seconds for UDP responses and 10 seconds for TCP connections. These defaults can be overridden by the <code>timeout</code> option in <code>/etc/resolv.conf</code>. </p>
<p> See also the <i>-w</i> option.</dl>
<h2>IDN SUPPORT</h2>
<p> If <code>host</code> has been built with IDN (internationalized domain name) support, it can accept and display non-ASCII domain names. <code>host</code> appropriately converts character encoding of a domain name before sending a request to a DNS server or displaying a reply from the server. To turn off IDN support, define the <code>IDN_DISABLE</code> environment variable. IDN support is disabled if the variable is set when <code>host</code> runs.</p>
<h2>FILES</h2>
<p> <code>/etc/resolv.conf</code></p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-dig/">dig</a>(1)</i>, <i><a href="/docs/linux/man/8-named/">named</a>(8)</i>.</p>
<h2>AUTHOR</h2>
<p> Internet Systems Consortium</p>
<h2>COPYRIGHT</h2>
<p> 2023, Internet Systems Consortium </p>
<h2>Index</h2>
