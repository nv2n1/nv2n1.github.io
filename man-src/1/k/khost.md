---
title: "khost(1)"
name: "khost"
section: "1"
letter: "k"
url: "/docs/linux/man/1-khost/"
---

<h2>NAME</h2>
<dl>
<dt><code>khost</code></p>
<dd> &#8211; Simple DNS lookup utility (libknot equivalent of ISC host)</dl>
<h2>SYNOPSIS</h2>
<p> <code>khost</code> [<i>options</i>] <i>name</i> [<i>server</i>]</p>
<h2>DESCRIPTION</h2>
<p> This utility sends a DNS query for the <i>name</i> to the <i>server</i> and prints a reply in more user-readable form. For more advanced DNS queries use <code>kdig</code> instead.</p>
<dl>
<dt><i>name</i></p>
<dd> Is a domain name that is to be looked up. If the <i>name</i> is IPv4 or IPv6 address the <i>PTR</i> query type is used.</p>
<dt><i>server</i></p>
<dd> Is a name or an address of the nameserver to send a query to. The address can be specified using [address]:port notation. If no server is specified the servers from <code>/etc/resolv.conf</code> are used.</p>
<dt>If no arguments are provided, <code>khost</code> prints short help.</p>
<dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-4</code></p>
<dd> Use IPv4 protocol only.</p>
<dt><code>-6</code></p>
<dd> Use IPv6 protocol only.</p>
<dt><code>-a</code></p>
<dd> Send ANY query with verbose mode.</p>
<dt><code>-d</code></p>
<dd> Enable debug messages if any.</p>
<dt><code>-h</code>,&nbsp;<wbr><code>&#8211;help</code></p>
<dd> Print help.</p>
<dt><code>-r</code></p>
<dd> Disable recursion.</p>
<dt><code>-s</code></p>
<dd> Stop querying next nameserver if SERVFAIL response is received.</p>
<dt><code>-T</code></p>
<dd> Use TCP protocol.</p>
<dt><code>-v</code></p>
<dd> Enable verbose output.</p>
<dt><code>-V</code>,&nbsp;<wbr><code>&#8211;version</code></p>
<dd> Print program version.</p>
<dt><code>-w</code></p>
<dd> Wait forever for the reply.</p>
<dt><code>-c</code><i>&nbsp;<wbr>class</i></p>
<dd> Set query class (e.g. <i>CH</i>, <i>CLASS4</i>). The default class is <i>IN</i>.</p>
<dt><code>-t</code><i>&nbsp;<wbr>type</i></p>
<dd> Set query type (e.g. <i>NS</i>, <i>IXFR=12345</i>, <i>TYPE65535</i>). The default is to send 3 queries (<i>A</i>, <i>AAAA</i> and <i>MX</i>).</p>
<dt><code>-R</code><i>&nbsp;<wbr>retries</i></p>
<dd> The number (&gt;=0) of UDP retries to query a nameserver. The default is <i>1</i>.</p>
<dt><code>-W</code><i>&nbsp;<wbr>wait</i></p>
<dd> The time to wait for a reply in seconds. This timeout applies to each query try. The default is <i>2</i> seconds.</dl>
<h2>NOTES</h2>
<h3>Missing features with regard to ISC host</h3>
<p> Options <code>-C, -i, -l, -m, -N</code>.</p>
<h3>Differences with regard to ISC host</h3>
<p> Option <code>-d</code> is not equivalent to <code>-v</code>, but enables debug messages.</p>
<dl>
<dt>The number of retries can be set to zero.</p>
<dd>
<dt>Verbose mode has slightly different format (same as <code>kdig</code>).</p>
<dd></dl>
<h2>EXAMPLES</h2>
<p> <code>Example 1. Get A, AAAA and MX records for example.com:</code></p>
<dl>
<dt># khost example.com</p>
<dd>
<dt><code>Example 2. Get reverse record for address 192.0.2.1:</code></p>
<dd>
<dt># khost 192.0.2.1</p>
<dd>
<dt><code>Example 3. Perform verbose zone transfer for zone example.com:</code></p>
<dd>
<dt># khost -t AXFR -v example.com</p>
<dd></dl>
<h2>FILES</h2>
<p> <i>/etc/resolv.conf</i></p>
<h2>AUTHOR</h2>
<p> Daniel Salzman (<code><a rel="nofollow" href="http://www.knot-dns.cz">www.knot-dns.cz</a></code>)</p>
<dl>
<dt>Please send any bug reports or comments to <code>knot-dns [at] labs.nic.cz</code></p>
<dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-kdig/">kdig</a></code>(1), <code><a href="/docs/linux/man/1-knsupdate/">knsupdate</a></code>(1). </p>
<h2>Index</h2>
