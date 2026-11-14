---
title: "dnsq(1)"
name: "dnsq"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dnsq/"
---

<h2>SYNOPSIS</h2>
<dl>
<dt><code>dnsq</code> [<code>OPTIONS</code>] &lt;record-type&gt; &lt;domain-name&gt; &lt;name-server&gt;</p>
<dd>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>dnsq</code> lets you query a DNS server for specific type of records about a given domain name. <code>dnsq</code> supports the following options: </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h &#8211;help</code></p>
<dd>
&nbsp;<wbr>print this help</p>
<dt><code>-v &#8211;version</code></p>
<dd>
&nbsp;<wbr>print version information </p>
</dl>
<h2>RECORD TYPES</h2>
<p> A record-type could be any of the following types </p>
<dl>
<dt>A</p>
<dd> Returns an IPv4 host address for the given domain name. </p>
<dt>ANY</p>
<dd> Returns any records that are available for the given domain name. </p>
<dt>NS</p>
<dd> Returns an authoritative name server for the given domain name. </p>
<dt>MX</p>
<dd> Returns the Mail Exchange for the given domain name. </p>
<dt>PTR</p>
<dd> Returns a pointer to another part of the domain name space. </p>
<dt>TXT</p>
<dd> Returns a textual representation of the records for the given domain name. </p>
<dt>CNAME</p>
<dd> Returns a canonical name of the given domain name or for an alias. </p>
<dt>SOA</p>
<dd> Returns the Start of a Zone of Authority. </p>
<dt>HINFO</p>
<dd> Returns information such as CPU and OS used by the host. </p>
<dt>RP</p>
<dd> Returns a responsible person records for the given domain name. </p>
<dt>SIG</p>
<dd> Returns a security signature for the given domain name. </p>
<dt>KEY</p>
<dd> Returns a security key for the given domain name. </p>
<dt>AAAA</p>
<dd> Returns an IPv6 host address for the given domain name. </p>
<dt>AXFR</p>
<dd> Request for a transfer of an entire zone. </p>
</dl>
<h2>BUGS</h2>
<p> Report bugs to &lt;pj.pandit [at] yahoo.co.in&gt; </p>
<h2>AUTHOR</h2>
<p> Prasad J Pandit </p>
<h2>Index</h2>
