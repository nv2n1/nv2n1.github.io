---
title: "dnsperf(1)"
name: "dnsperf"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dnsperf/"
description: "dnsperf – test the performance of a DNS server"
---

<h2>NAME</h2>
<p> dnsperf &#8211; test the performance of a DNS server</p>
<h2>SYNOPSIS</h2>
<p> <code>dnsperf</code>&nbsp;<wbr>[<code>-a&nbsp;<wbr></code><i>local_addr</i>] [<code>-b&nbsp;<wbr></code><i>bufsize</i>] [<code>-c&nbsp;<wbr></code><i>clients</i>] [<code>-d&nbsp;<wbr></code><i>datafile</i>] [<code>-D</code>] [<code>-e</code>] [<code>-f&nbsp;<wbr></code><i>family</i>] [<code>-h</code>] [<code>-l&nbsp;<wbr></code><i>limit</i>] [<code>-n&nbsp;<wbr></code><i>runs_through_file</i>] [<code>-p&nbsp;<wbr></code><i>port</i>] [<code>-q&nbsp;<wbr></code><i>num_queries</i>] [<code>-Q&nbsp;<wbr></code><i>max_qps</i>] [<code>-s&nbsp;<wbr></code><i>server_addr</i>] [<code>-S&nbsp;<wbr></code><i>stats_interval</i>] [<code>-t&nbsp;<wbr></code><i>timeout</i>] [<code>-T&nbsp;<wbr></code><i>threads</i>] [<code>-u</code>] [<code>-v</code>] [<code>-x&nbsp;<wbr></code><i>local_port</i>] [<code>-y&nbsp;<wbr></code><i>[alg:]name:secret</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>dnsperf</code> is a DNS server performance testing tool. It is primarily intended for measuring the performance of authoritative DNS servers, but it can also be used for measuring caching server performance in a closed laboratory environment. For testing caching servers resolving against the live Internet, the <code>resperf</code> program is preferred. </p>
<p> It is recommended that <code>dnsperf</code> and the name server under test be run on separate machines, so that the CPU usage of <code>dnsperf</code> itself does not slow down the name server. The two machines should be connected with a fast network, preferably a dedicated Gigabit Ethernet segment. Testing through a router or firewall is not advisable.</p>
<h3>Configuring the name server</h3>
<p> If using <code>dnsperf</code> to test an authoritative server, the name server under test should be set up to serve one or more zones similar in size and number to what the server is expected to serve in production. </p>
<p> Also, be sure to turn off recursion in the server&#8217;s configuration (in BIND 8/9, specify &quot;recursion no;&quot; in the options block). In BIND 8, you should also specify &quot;fetch-glue no;&quot;; otherwise the server may attempt to retrieve glue information from the Internet during the test, slowing it down by an unpredictable factor.</p>
<h3>Constructing a query input file</h3>
<p> A <code>dnsperf</code> input file should contain a large and realistic set of queries, on the order of ten thousand to a million. The input file contains one line per query, consisting of a domain name and an RR type name separated by a space. The class of the query is implicitly IN. </p>
<p> When measuring the performance serving non-terminal zones such as the root zone or TLDs, note that such servers spend most of their time providing referral responses, not authoritative answers. Therefore, a realistic input file might consist mostly of queries for type A for names *below*, not at, the delegations present in the zone. For example, when testing the performance of a server configured to be authoritative for the top-level domain &quot;fi.&quot;, which contains delegations for domains like &quot;helsinki.fi&quot; and &quot;turku.fi&quot;, the input file could contain lines like</p>
<dl>
<dt>
<dd>
<pre>
<a rel="nofollow" href="http://www.turku.fi">www.turku.fi</a> A
<a rel="nofollow" href="http://www.helsinki.fi">www.helsinki.fi</a> A
</pre>
</dl>
<p> where the &quot;www&quot; prefix ensures that the server will respond with a referral. Ideally, a realistic proportion of queries for nonexistent domains should be mixed in with those for existing ones, and the lines of the input file should be in a random order.</p>
<h3>Constructing a dynamic update input file</h3>
<p> To test dynamic update performance, <code>dnsperf</code> is run with the <code>-u</code> option, and the input file is constructed of blocks of lines describing dynamic update messages. The first line in a block contains the zone name:</p>
<dl>
<dt>
<dd>
<pre>
example.com
</pre>
</dl>
<p> Subsequent lines contain prerequisites, if there are any. Prerequisites can specify that a name may or may not exist, an rrset may or may not exist, or an rrset exists and its rdata matches all specified rdata for that name and type. The keywords &quot;require&quot; and &quot;prohibit&quot; are followed by the appropriate information. All relative names are considered to be relative to the zone name. The following lines show the 5 types of prerequisites.</p>
<dl>
<dt>
<dd>
<pre>
require a
require a A
require a A 1.2.3.4
prohibit x
prohibit x A
</pre>
</dl>
<p> Subsequent lines contain records to be added, records to be deleted, rrsets to be deleted, or names to be deleted. The keywords &quot;add&quot; or &quot;delete&quot; are followed by the appropriate information. All relative names are considered to be relative to the zone name. The following lines show the 4 types of updates.</p>
<dl>
<dt>
<dd>
<pre>
add x 3600 A 10.1.2.3
delete y A 10.1.2.3
delete z A
delete w
</pre>
</dl>
<p> Each update message is terminated by a line containing the command:</p>
<dl>
<dt>
<dd>
<pre>
send
</pre>
</dl>
<h3>Running the tests</h3>
<p> When running <code>dnsperf</code>, a data file (the <code>-d</code> option) and server (the <code>-s</code> option) will normally be specified. The output of dnsperf is mostly self-explanatory. Pay attention to the number of dropped packets reported &#8211; when running the test over a local Ethernet connection, it should be zero. If one or more packets has been dropped, there may be a problem with the network connection. In that case, the results should be considered suspect and the test repeated.</p>
<h2>OPTIONS</h2>
<p> <code>-a </code><i>local_addr</i> </p>
<dl>
<dt>
<dd> Specifies the local address from which to send requests. The default is the wildcard address.</dl>
<p> <code>-b </code><i>bufsize</i> </p>
<dl>
<dt>
<dd> Sets the size of the socket&#8217;s send and receive buffers, in kilobytes. If not specified, the operating system&#8217;s default is used.</dl>
<p> <code>-c </code><i>clients</i> </p>
<dl>
<dt>
<dd> Act as multiple clients. Requests are sent from multiple sockets. The default is to act as 1 client.</dl>
<p> <code>-d </code><i>datafile</i> </p>
<dl>
<dt>
<dd> Specifies the input data file. If not specified, <code>dnsperf</code> will read from standard input.</dl>
<p> <code>-D</code> </p>
<dl>
<dt>
<dd> Sets the DO (DNSSEC OK) bit [RFC3225] in all packets sent. This also enables EDNS0, which is required for DNSSEC.</dl>
<p> <code>-e</code> </p>
<dl>
<dt>
<dd> Enables EDNS0 [RFC2671], by adding an OPT record to all packets sent.</dl>
<p> <code>-f </code><i>family</i> </p>
<dl>
<dt>
<dd> Specifies the address family used for sending DNS packets. The possible values are &quot;inet&quot;, &quot;inet6&quot;, or &quot;any&quot;. If &quot;any&quot; (the default value) is specified, <code>dnsperf</code> will use whichever address family is appropriate for the server it is sending packets to.</dl>
<p> <code>-h</code> </p>
<dl>
<dt>
<dd> Print a usage statement and exit.</dl>
<p> <code>-l </code><i>limit</i> </p>
<dl>
<dt>
<dd> Specifies a time limit for the run, in seconds. This may cause the input to be read multiple times, or only some of the input to be read. The default behavior is to read the input once, and have no specific time limit.</dl>
<p> <code>-n </code><i>runs_through_file</i> </p>
<dl>
<dt>
<dd> Run through the input file at most this many times. If no time limit is set, the file will be read exactly this number of times; if a time limit is set, the file may be read fewer times.</dl>
<p> <code>-p </code><i>port</i> </p>
<dl>
<dt>
<dd> Sets the port on which the DNS packets are sent. If not specified, the standard DNS port (53) is used.</dl>
<p> <code>-q </code><i>num_queries</i> </p>
<dl>
<dt>
<dd> Sets the maximum number of outstanding requests. When this value is reached, <code>dnsperf</code> will not send any more requests until either responses are received or requests time out. The default value is 100.</dl>
<p> <code>-Q </code><i>max_qps</i> </p>
<dl>
<dt>
<dd> Limits the number of requests per second. There is no default limit.</dl>
<p> <code>-s </code><i>server_addr</i> </p>
<dl>
<dt>
<dd> Specifies the name or address of the server to which requests will be sent. The default is the loopback address, 127.0.0.1.</dl>
<p> <code>-S </code><i>stats_interval</i> </p>
<dl>
<dt>
<dd> If this parameter is specified, a count of the number of queries per second during the interval will be printed out every stats_interval seconds.</dl>
<p> <code>-t </code><i>timeout</i> </p>
<dl>
<dt>
<dd> Specifies the request timeout value, in seconds. <code>dnsperf</code> will no longer wait for a response to a particular request after this many seconds have elapsed. The default is 5 seconds.</dl>
<p> <code>-T </code><i>threads</i> </p>
<dl>
<dt>
<dd> Run multiple client threads. By default, <code>dnsperf</code> uses one thread for sending requests and one thread for receiving responses. If this option is specified, <code>dnsperf</code> will instead use N pairs of send/receive threads.</dl>
<p> <code>-u</code> </p>
<dl>
<dt>
<dd> Instructs <code>dnsperf</code> to send DNS dynamic update messages, rather than queries. The format of the input file is different in this case; see the &quot;Constructing a dynamic update input file&quot; section for more details.</dl>
<p> <code>-v</code> </p>
<dl>
<dt>
<dd> Enables verbose mode. The DNS RCODE of each response will be reported to standard output when the response is received, as will the latency. If a query times out, it will be reported with the special string &quot;T&quot; instead of a normal DNS RCODE. If a query is interrupted, it will be reported with the special string &quot;I&quot;.</dl>
<p> <code>-x </code><i>local_port</i> </p>
<dl>
<dt>
<dd> Specifies the local port from which to send requests. The default is the wildcard port (0). </p>
<p> If acting as multiple clients and the wildcard port is used, each client will use a different random port. If a port is specified, the clients will use a range of ports starting with the specified one.</dl>
<p> <code>-y </code><i>[alg:]name:secret</i> </p>
<dl>
<dt>
<dd> Add a TSIG record [RFC2845] to all packets sent, using the specified TSIG key algorithm, name and secret, where the algorithm defaults to hmac-md5 and the secret is expressed as a base-64 encoded string.</dl>
<h2>AUTHOR</h2>
<p> Nominum, Inc.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-resperf/">resperf</a></code>(1) </p>
<h2>Index</h2>
