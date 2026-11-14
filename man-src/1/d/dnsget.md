---
title: "dnsget(1)"
name: "dnsget"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dnsget/"
description: "dnsget – DNS lookup utility"
---

<h2 class="name">NAME</h2>
<p> dnsget &#8211; DNS lookup utility</p>
<h2>SYNOPSYS</h2>
<p> <code>dnsget</code> [<code>-v</code>|<code>-q</code>] [<code>-c</code> <i>class</i>] [<code>-t</code> <i>type</i>] [<code>-o</code> <i>opt</i>,<i>opt</i>,&#8230;] <i>name</i>&#8230; </p>
<h2>DESCRIPTION</h2>
<p> <code>dnsget</code> is a simple command-line to perform DNS lookups, similar to <code><a href="/docs/linux/man/1-host/">host</a></code>(1) and <code><a href="/docs/linux/man/1-dig/">dig</a></code>(1). It is useable for both interactive/debugging scenarious and in scripts. The program is implemented using <code><a href="/docs/linux/man/3-udns/">udns</a></code>(3) library. </p>
<p> By default, <code>dnsget</code> produces a human-readable output, similar to</p>
<dl>
<dt>
<dd>
<pre>
alias.example.com. CNAME <a rel="nofollow" href="http://www.example.com">www.example.com</a>.
<a rel="nofollow" href="http://www.example.com">www.example.com</a>. A 192.168.1.1
<a rel="nofollow" href="http://www.example.com">www.example.com</a>. MX 10 mx.example.com.
</pre>
</dl>
<p> which is just sufficient to see how a given name resolves. Output format is controllable with <code>-v</code> and <code>-q</code> options &#8212; the former increases verbosity level up to printing the whole DNS contents of all packets sent and received, which is suitable for debugging DNS problems, while the latter reduces the level, making output more quiet, up to bare result with no error messages, which is good for scripts. </p>
<h2>OPTIONS</h2>
<p> The following options are recognized by <code>dnsget</code>: </p>
<dl>
<dt><code>-v</code></p>
<dd> produce more detailed output. More <code>-v</code>&#8216;s means more details will be produced. With single <code>-v</code>,<code>dnsget</code> will print contents of all received DNS packets (in a readable format), while with <code>-vv</code>, it will output all outgoing DNS packets too. </p>
<dt><code>-q</code></p>
<dd> the opposite for <code>-v</code> &#8212; produce less detailed output. With single <code>-q</code>,<code>dnsget</code> will only show (decoded) data from final DNS resource records (RR), while <code>-qq</code> also suppresses error messages. </p>
<dt><code>-t </code><i>type</i></p>
<dd> request record(s) of the given type <i>type</i>. By default, <code>dnsget</code> will ask for IPv4 address (A) record, or for PTR record if the argument in question is an IPv4 or IPv6 address. Recognized types include A, AAAA, MX, TXT, CNAME, PTR, NS, SOA, ANY and others. </p>
<dt><code>-c </code><i>class</i></p>
<dd> request DNS record(s) of the given class <i>class</i>. By default <code>dnsget</code> uses IN class. Valid classes include IN, CH, HS, ANY. </p>
<dt><code>-a</code></p>
<dd> (compatibility option). Equivalent to setting query type to <code>ANY</code> and increasing verbosity level (<code>-v</code>). </p>
<dt><code>-C</code></p>
<dd> (planned) </p>
<dt><code>-x</code></p>
<dd> (planned) </p>
<dt><code>-o </code><i>opt</i>,<i>opt</i>,&#8230;</p>
<dd> (may be specified several times). Set resolver options (in a form <i>option</i>:<i>value</i>) as if they were set in $<code>RES_OPTIONS</code> environment variable, or set query flags:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>timeout</code>:<i>sec</i></p>
<dd> Set initial query timeout to <i>sec</i>.</p>
<dt><code>attempts</code>:<i>num</i></p>
<dd> (re)try every query <i>num</i> times before failing.</p>
<dt><code>udpbuf</code>:<i>bytes</i></p>
<dd> set DNS UDP buffer size to <i>bytes</i> bytes. Valid values are from 512 to 65535. If <i>bytes</i> is greather than 512, EDNS0 (RFC 2671) extensions will be used.</p>
<dt><code>port</code>:<i>num</i></p>
<dd> Use given UDP port number <i>num</i> instead of the default port 53 (domain).</p>
<dt><code>aa</code></p>
<dd> set AA (auth only) query bit.</p>
<dt><code>nord</code></p>
<dd> do not set RD (recursion desired) query bit (set by default).</p>
<dt><code>dnssec</code> or <code>do</code></p>
<dd> set DNSSEC OK (DO) query flag (<code>dnsget</code> does not verify DNSSEC signatures, only displays them; this is set in EDNS RR).</p>
<dt><code>cd</code></p>
<dd> set CD (checking disabled) query bit.</dl>
</dl>
<dt><code>-n </code><i>nameserver</i></p>
<dd> Use the given nameserver(s) (may be specified more than once) instead of the default. Using this option has the same same effect as $<code>NSCACHEIP</code> or $<code>NAMESERVERS</code> environment variables, with the only difference that only IPv4 addresses are recognized for now, and it is possible to specify names (which will be resolved using default settings) instead of IP addresses. </p>
<dt><code>-h</code></p>
<dd> print short help and exit. </p>
</dl>
<h2>RETURN VALUE</h2>
<p> When all names where resovled successefully, <code>dnsget</code> exits with zero exit status. If at least one name was not found, <code>dnsget</code> will exit with return code 100. If some other error occured during name resolution, it will exit with code 99. In case of usage or initialization error, <code>dnsget</code> will return 1. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-host/">host</a></code>(1) <code><a href="/docs/linux/man/1-dig/">dig</a></code>(1) <code><a href="/docs/linux/man/5-resolv-conf/">resolv.conf</a></code>(5) <code><a href="/docs/linux/man/3-udns/">udns</a></code>(3). </p>
<h2>Index</h2>
