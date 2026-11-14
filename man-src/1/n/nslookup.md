---
title: "nslookup(1)"
name: "nslookup"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nslookup/"
description: "nslookup – query Internet name servers interactively"
---

<h2 class="name">NAME</h2>
<p> nslookup &#8211; query Internet name servers interactively </p>
<h2>SYNOPSIS</h2>
<p> <code>nslookup</code> [-option] [name | -] [server]</p>
<h2>DESCRIPTION</h2>
<p> <code>nslookup</code> is a program to query Internet domain name servers. <code>nslookup</code> has two modes: interactive and non-interactive. Interactive mode allows the user to query name servers for information about various hosts and domains or to print a list of hosts in a domain. Non-interactive mode prints just the name and requested information for a host or domain.</p>
<h2>ARGUMENTS</h2>
<p> Interactive mode is entered in the following cases:</p>
<dl>
<dt>a.</p>
<dd> when no arguments are given (the default name server is used);</p>
<dt>b.</p>
<dd> when the first argument is a hyphen (-) and the second argument is the host name or Internet address of a name server. </p>
<p> Non-interactive mode is used when the name or Internet address of the host to be looked up is given as the first argument. The optional second argument specifies the host name or address of a name server. </p>
<p> Options can also be specified on the command line if they precede the arguments and are prefixed with a hyphen. For example, to change the default query type to host information, with an initial timeout of 10 seconds, type: </p>
<pre>
nslookup -query=hinfo  -timeout=10
</pre>
<p> The <code>-version</code> option causes <code>nslookup</code> to print the version number and immediately exit.</dl>
<h2>INTERACTIVE COMMANDS</h2>
<dl>
<dt><code>host [server]</code></p>
<dd> This command looks up information for <i>host</i> using the current default server or using <code>server</code>, if specified. If <i>host</i> is an Internet address and the query type is A or PTR, the name of the host is returned. If <i>host</i> is a name and does not have a trailing period (<code>.</code>), the search list is used to qualify the name. </p>
<p> To look up a host not in the current domain, append a period to the name.</p>
<dt><code>server domain</code> | <code>lserver domain</code></p>
<dd> These commands change the default server to <code>domain</code>; <code>lserver</code> uses the initial server to look up information about <code>domain</code>, while <code>server</code> uses the current default server. If an authoritative answer cannot be found, the names of servers that might have the answer are returned.</p>
<dt><code>root</code></p>
<dd> This command is not implemented.</p>
<dt><code>finger</code></p>
<dd> This command is not implemented.</p>
<dt><code>ls</code></p>
<dd> This command is not implemented.</p>
<dt><code>view</code></p>
<dd> This command is not implemented.</p>
<dt><code>help</code></p>
<dd> This command is not implemented.</p>
<dt><code>?</code></p>
<dd> This command is not implemented.</p>
<dt><code>exit</code></p>
<dd> This command exits the program.</p>
<dt><code>set keyword[=value]</code></p>
<dd> This command is used to change state information that affects the lookups. Valid keywords are:</p>
<dt><code>all</code></p>
<dd> This keyword prints the current values of the frequently used options to <code>set</code>. Information about the current default server and host is also printed.</p>
<dt><code>class=value</code></p>
<dd> This keyword changes the query class to one of:</p>
<dt><code>IN</code></p>
<dd> the Internet class</p>
<dt><code>CH</code></p>
<dd> the Chaos class</p>
<dt><code>HS</code></p>
<dd> the Hesiod class</p>
<dt><code>ANY</code></p>
<dd> wildcard </p>
<p> The class specifies the protocol group of the information. The default is <code>IN</code>; the abbreviation for this keyword is <code>cl</code>.</p>
<dt><code>nodebug</code></p>
<dd> This keyword turns on or off the display of the full response packet, and any intermediate response packets, when searching. The default for this keyword is <code>nodebug</code>; the abbreviation for this keyword is <code>[no]deb</code>.</p>
<dt><code>nod2</code></p>
<dd> This keyword turns debugging mode on or off. This displays more about what nslookup is doing. The default is <code>nod2</code>.</p>
<dt><code>domain=name</code></p>
<dd> This keyword sets the search list to <code>name</code>.</p>
<dt><code>nosearch</code></p>
<dd> If the lookup request contains at least one period, but does not end with a trailing period, this keyword appends the domain names in the domain search list to the request until an answer is received. The default is <code>search</code>.</p>
<dt><code>port=value</code></p>
<dd> This keyword changes the default TCP/UDP name server port to <code>value</code> from its default, port 53. The abbreviation for this keyword is <code>po</code>.</p>
<dt><code>querytype=value</code> | <code>type=value</code></p>
<dd> This keyword changes the type of the information query to <code>value</code>. The defaults are A and then AAAA; the abbreviations for these keywords are <code>q</code> and <code>ty</code>. </p>
<p> Please note that it is only possible to specify one query type. Only the default behavior looks up both when an alternative is not specified.</p>
<dt><code>norecurse</code></p>
<dd> This keyword tells the name server to query other servers if it does not have the information. The default is <code>recurse</code>; the abbreviation for this keyword is <code>[no]rec</code>.</p>
<dt><code>ndots=number</code></p>
<dd> This keyword sets the number of dots (label separators) in a domain that disables searching. Absolute names always stop searching.</p>
<dt><code>retry=number</code></p>
<dd> This keyword sets the number of retries to <code>number</code>.</p>
<dt><code>timeout=number</code></p>
<dd> This keyword changes the initial timeout interval to wait for a reply to <code>number</code>, in seconds.</p>
<dt><code>novc</code></p>
<dd> This keyword indicates that a virtual circuit should always be used when sending requests to the server. <code>novc</code> is the default.</p>
<dt><code>nofail</code></p>
<dd> This keyword tries the next nameserver if a nameserver responds with SERVFAIL or a referral (nofail), or terminates the query (fail) on such a response. The default is <code>nofail</code>.</dl>
<h2>RETURN VALUES</h2>
<p> <code>nslookup</code> returns with an exit status of 1 if any query failed, and 0 otherwise.</p>
<h2>IDN SUPPORT</h2>
<p> If <code>nslookup</code> has been built with IDN (internationalized domain name) support, it can accept and display non-ASCII domain names. <code>nslookup</code> appropriately converts character encoding of a domain name before sending a request to a DNS server or displaying a reply from the server. To turn off IDN support, define the <code>IDN_DISABLE</code> environment variable. IDN support is disabled if the variable is set when <code>nslookup</code> runs, or when the standard output is not a tty.</p>
<h2>FILES</h2>
<p> <code>/etc/resolv.conf</code></p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-dig/">dig</a>(1)</i>, <i><a href="/docs/linux/man/1-host/">host</a>(1)</i>, <i><a href="/docs/linux/man/8-named/">named</a>(8)</i>.</p>
<h2>AUTHOR</h2>
<p> Internet Systems Consortium</p>
<h2>COPYRIGHT</h2>
<p> 2023, Internet Systems Consortium </p>
<h2>Index</h2>
