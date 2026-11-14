---
title: "unbound-host(1)"
name: "unbound-host"
section: "1"
letter: "u"
url: "/docs/linux/man/1-unbound-host/"
description: "unbound-host – unbound DNS lookup utility"
---

<h2 class="name">NAME</h2>
<p> <code>unbound-host</code> &#8211; unbound DNS lookup utility </p>
<h2>SYNOPSIS</h2>
<p> <code>unbound-host</code> [<code>-vdhr46</code>] [<code>-c</code> <i>class</i>] [<code>-t</code> <i>type</i>] <i>hostname</i> [<code>-y</code> <i>key</i>] [<code>-f</code> <i>keyfile</i>] [<code>-F</code> <i>namedkeyfile</i>] [<code>-C</code> <i>configfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>Unbound-host</code> uses the unbound validating resolver to query for the hostname and display results. With the <code>-v</code> option it displays validation status: secure, insecure, bogus (security failure). </p>
<p> By default it reads no configuration file whatsoever. It attempts to reach the internet root servers. With <code>-C</code> an unbound config file and with <code>-r</code> resolv.conf can be read. </p>
<p> The available options are:</p>
<dl>
<dt><i>hostname</i></p>
<dd> This name is resolved (looked up in the DNS). If a IPv4 or IPv6 address is given, a reverse lookup is performed.</p>
<dt><code>-h</code></p>
<dd> Show the version and commandline option help.</p>
<dt><code>-v</code></p>
<dd> Enable verbose output and it shows validation results, on every line. Secure means that the NXDOMAIN (no such domain name), nodata (no such data) or positive data response validated correctly with one of the keys. Insecure means that that domain name has no security set up for it. Bogus (security failure) means that the response failed one or more checks, it is likely wrong, outdated, tampered with, or broken.</p>
<dt><code>-d</code></p>
<dd> Enable debug output to stderr. One -d shows what the resolver and validator are doing and may tell you what is going on. More times, -d -d, gives a lot of output, with every packet sent and received.</p>
<dt><code>-c </code><i>class</i></p>
<dd> Specify the class to lookup for, the default is IN the internet class.</p>
<dt><code>-t </code><i>type</i></p>
<dd> Specify the type of data to lookup. The default looks for IPv4, IPv6 and mail handler data, or domain name pointers for reverse queries.</p>
<dt><code>-y </code><i>key</i></p>
<dd> Specify a public key to use as trust anchor. This is the base for a chain of trust that is built up from the trust anchor to the response, in order to validate the response message. Can be given as a DS or DNSKEY record. For example -y &quot;example.com DS 31560 5 1 1CFED84787E6E19CCF9372C1187325972FE546CD&quot;.</p>
<dt><code>-f </code><i>keyfile</i></p>
<dd> Reads keys from a file. Every line has a DS or DNSKEY record, in the format as for -y. The zone file format, the same as dig and drill produce.</p>
<dt><code>-F </code><i>namedkeyfile</i></p>
<dd> Reads keys from a BIND-style named.conf file. Only the trusted-key {}; entries are read.</p>
<dt><code>-C </code><i>configfile</i></p>
<dd> Uses the specified unbound.conf to prime <i><a href="/docs/linux/man/3-libunbound/">libunbound</a></i>(3).</p>
<dt><code>-r</code></p>
<dd> Read /etc/resolv.conf, and use the forward DNS servers from there (those could have been set by DHCP). More info in <i><a href="/docs/linux/man/5-resolv-conf/">resolv.conf</a></i>(5). Breaks validation if those servers do not support DNSSEC.</p>
<dt><code>-4</code></p>
<dd> Use solely the IPv4 network for sending packets.</p>
<dt><code>-6</code></p>
<dd> Use solely the IPv6 network for sending packets.</dl>
<h2>EXAMPLES</h2>
<p> Some examples of use. The keys shown below are fakes, thus a security failure is encountered. </p>
<p> $ unbound-host <a rel="nofollow" href="http://www.example.com">www.example.com</a> </p>
<p> $ unbound-host -v -y &quot;example.com DS 31560 5 1 1CFED84787E6E19CCF9372C1187325972FE546CD&quot; <a rel="nofollow" href="http://www.example.com">www.example.com</a> </p>
<p> $ unbound-host -v -y &quot;example.com DS 31560 5 1 1CFED84787E6E19CCF9372C1187325972FE546CD&quot; 192.0.2.153</p>
<h2>EXIT CODE</h2>
<p> The unbound-host program exits with status code 1 on error, 0 on no error. The data may not be available on exit code 0, exit code 1 means the lookup encountered a fatal error.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/5-unbound-conf/">unbound.conf</a></i>(5), <i><a href="/docs/linux/man/8-unbound/">unbound</a></i>(8). </p>
<h2>Index</h2>
