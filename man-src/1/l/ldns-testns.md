---
title: "ldns-testns(1)"
name: "ldns-testns"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldns-testns/"
description: "ldns-testns – simple fake nameserver tool"
---

<h2>NAME</h2>
<p> ldns-testns &#8211; simple fake nameserver tool</p>
<h2>SYNOPSYS</h2>
<p> <code>ldns-testns</code> [ <i>OPTION</i> ] <i>datafile</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>ldns-testns</code> can be used to provide answers to DNS queries for testing. The answers are premade, and can be tailored to testing needs. The answers can be wildly invalid or unparseable. </p>
<p> This program is a debugging aid. It is not efficient, especially with a long config file, but it can give any reply to any query. This can help the developer pre-script replies for queries. </p>
<p> It listens to IP4 UDP and TCP by default. You can specify a packet RR by RR with header flags to return. </p>
<p> ldns-testns is not meant for production use. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-r</code></p>
<dd> Listens to a random port. The port number is printed to stdout. </p>
<dt><code>-p</code> <i>port</i></p>
<dd> Listens to the specified port. </p>
<dt><code>-f</code> <i>num</i></p>
<dd> Forks this number of additional instances that serve the same ports and same datafile. They do not exit; printed is &#8216;forked pid: &lt;num&gt;&#8217; and you have to kill them yourself. </p>
<dt><code>-v</code></p>
<dd> Outputs more debug information. It is possible to give this option multiple times to increase verbosity level. </p>
<dt><code>-6</code></p>
<dd> Bind to IP6 address instead of IP4. Use together with -p. </p>
<dt><code>datafile</code></p>
<dd> The data file is read on start up. It contains queries and the packets that should be sent in answer to those queries. The data file format is explained below. </p>
</dl>
<h2>DATA FILE FORMAT</h2>
<p> The data file format has &#8216;;&#8217; to denote comment. A number of entries are processed first to last. The first matching entry is used to answer the query with. This is a line based format. DNS resource records are entered in zone-file format. </p>
<p> You can use $ORIGIN and $TTL directives. Zone file &#8216;(&#8216; and &#8216;)&#8217; to span multiple lines are not allowed. </p>
<p> $ORIGIN origin $TTL default_ttl </p>
<p> ENTRY_BEGIN </p>
<p> ; first give MATCH lines, that say what queries are matched ; by this entry. ; &#8216;opcode&#8217; makes the query match the opcode from the reply ; if you leave it out, any opcode matches this entry. ; &#8216;qtype&#8217; makes the query match the qtype from the reply ; &#8216;qname&#8217; makes the query match the qname from the reply ; &#8216;serial=1023&#8217; makes the query match if ixfr serial is 1023. </p>
<p> MATCH [opcode] [qtype] [qname] [serial=&lt;value&gt;] MATCH [UDP|TCP] MATCH &#8230; </p>
<p> ; Then the REPLY header is specified. </p>
<p> REPLY opcode, rcode or flags.<br />
&nbsp;<wbr>&nbsp;<wbr>(opcode)&nbsp;<wbr>&nbsp;<wbr>QUERY IQUERY STATUS NOTIFY UPDATE<br />
&nbsp;<wbr>&nbsp;<wbr>(rcode)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>NOERROR FORMERR SERVFAIL NXDOMAIN NOTIMPL YXDOMAIN<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>YXRRSET NXRRSET NOTAUTH NOTZONE<br />
&nbsp;<wbr>&nbsp;<wbr>(flags)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>QR AA TC RD CD RA AD </p>
<p> REPLY &#8230; </p>
<p> ; any additional actions to do. </p>
<p> ADJUST copy_id ; &#8216;copy_id&#8217; copies the ID from the query to the answer. </p>
<p> ; &#8216;sleep=10&#8217; sleeps for 10 seconds before giving the answer (TCP is open) </p>
<p> ADJUST [sleep=&lt;num&gt;] ; sleep before giving any reply ADJUST [packet_sleep=&lt;num&gt;] ; sleep before this packet in sequence </p>
<p> SECTION QUESTION &lt;RRs, one per line&gt; ; the RRcount is determined automatically. </p>
<p> SECTION ANSWER &lt;RRs, one per line&gt; </p>
<p> SECTION AUTHORITY &lt;RRs, one per line&gt; </p>
<p> SECTION ADDITIONAL &lt;RRs, one per line&gt; </p>
<p> EXTRA_PACKET ; follow with SECTION, REPLY for more packets. HEX_ANSWER_BEGIN ; follow with hex data<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>;&nbsp;<wbr>this replaces any answer packet constructed<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>;&nbsp;<wbr>with the SECTION keywords&nbsp;<wbr>(only SECTION QUERY<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>;&nbsp;<wbr>is used to match queries). If the data cannot<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>;&nbsp;<wbr>be parsed, ADJUST rules for the answer packet<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>;&nbsp;<wbr>are ignored </p>
<p> HEX_ANSWER_END </p>
<p> ENTRY_END </p>
<h2>AUTHOR</h2>
<p> Written by the ldns team as an example for ldns usage, and for testing purposes.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;ldns-team [at] nlnetlabs.nl&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2006-2008 NLnet Labs. This is free software. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>Index</h2>
