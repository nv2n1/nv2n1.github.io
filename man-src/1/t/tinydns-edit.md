---
title: "tinydns-edit(1)"
name: "tinydns-edit"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tinydns-edit/"
description: "tinydns-edit"
---

<h2 class="name">NAME</h2>
<p> <code>tinydns-edit</code></p>
<h2>SYNOPSIS</h2>
<p> <code>tinydns-edit</code> [<code>OPTIONS</code>] DATA DATA.TMP add TYPE NAME ADDRESS </p>
<h2>DESCRIPTION</h2>
<p> <code>tinydns-edit</code> write the DNS records to the `data&#8217; file, which in turn is used by <code>tinydns-data</code> to generate the binary .cdb file used by <code>tinydns</code> or <code>axfrdns</code> server. The command line parameters required by <code>tinydns-edit</code> are </p>
<dl>
<dt>DATA</dt>
<dd> is a path of the `data&#8217; file to be written. </dd>
<dt>DATA.TMP</dt>
<dd> is a path of the temporary file to be used by tinydns-edit for creating the DATA file. </dd>
<dt>add</dt>
<dd> is a mandatory command. </dd>
<dt>TYPE</dt>
<dd> is the DNS record type, and could be any of the following </dd>
<p> ns: name server record, specifies that the NAME is published by a DNS server at ADDRESS. </p>
<p> childns: specifies that requests for the domain NAME should be referred to a child DNS server at ADDRESS. </p>
<p> mx: this record says, mail to names in the domain NAME should be sent to an SMTP server at ADDRESS. </p>
<p> host: this record says that the domain NAME maps to an address ADDRESS and vice versa. </p>
<p> alias: this record says that the domain NAME maps to the address ADDRESS but the reverse is not true. </p>
<dt>NAME</dt>
<dd> is the domain name to be appended to the DATA file. </dd>
<dt>ADDRESS</dt>
<dd> is the respective address for the domain NAME. </dd>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h &#8211;help</code></dt>
<dd>
&nbsp;<wbr>print this help.</dd>
<dt><code>-v &#8211;version</code></dt>
<dd>
&nbsp;<wbr>print version information. </dd>
</dl>
<h2>BUGS</h2>
<p> Report bugs to &lt;pj.pandit [at] yahoo.co.in&gt; </p>
<h2>AUTHOR</h2>
<p> Prasad J Pandit </p>
<h2>Index</h2>
