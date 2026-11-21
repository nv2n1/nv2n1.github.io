---
title: "dnsqr(1)"
name: "dnsqr"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dnsqr/"
---

<h2>SYNOPSIS</h2>
<dl>
<dt><code>dnsqr</code> [<code>OPTIONS</code>] &lt;record-type&gt; &lt;domain-name&gt;</dt>
<dd>
</dd></dl>
<h2>DESCRIPTION</h2>
<p> <code>dnsqr</code> lets you query for specific type of records about a given domain name. <code>dnsqr</code> supports the following options: </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h &#8211;help</code></dt>
<dd>
&nbsp;<wbr>print this help</dd>
<dt><code>-v &#8211;version</code></dt>
<dd>
&nbsp;<wbr>print version information </dd>
</dl>
<h2>RECORD TYPES</h2>
<p> A record-type could be any of the following types </p>
<dl>
<dt>A</dt>
<dd> Returns an IPv4 host address for the given domain name. </dd>
<dt>ANY</dt>
<dd> Returns any records that are available for the given domain name. </dd>
<dt>NS</dt>
<dd> Returns an authoritative name server for the given domain name. </dd>
<dt>MX</dt>
<dd> Returns the Mail Exchange for the given domain name. </dd>
<dt>PTR</dt>
<dd> Returns a pointer to another part of the domain name space. </dd>
<dt>TXT</dt>
<dd> Returns a textual representation of the records for the given domain name. </dd>
<dt>CNAME</dt>
<dd> Returns a canonical name of the given domain name or for an alias. </dd>
<dt>SOA</dt>
<dd> Returns the Start of a Zone of Authority. </dd>
<dt>HINFO</dt>
<dd> Returns information such as CPU and OS used by the host. </dd>
<dt>RP</dt>
<dd> Returns a responsible person records for the given domain name. </dd>
<dt>SIG</dt>
<dd> Returns a security signature for the given domain name. </dd>
<dt>KEY</dt>
<dd> Returns a security key for the given domain name. </dd>
<dt>AAAA</dt>
<dd> Returns an IPv6 host address for the given domain name. </dd>
<dt>AXFR</dt>
<dd> Request for a transfer of an entire zone. </dd>
</dl>
<h2>BUGS</h2>
<p> Report bugs to &lt;pj.pandit [at] yahoo.co.in&gt; </p>
<h2>Manual Author</h2>
<p> Prasad J Pandit </p>
