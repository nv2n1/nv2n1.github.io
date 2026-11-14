---
title: "pmfind(1)"
name: "pmfind"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmfind/"
description: "pmfind – find PCP services on the network"
---

<h2>NAME</h2>
<p> <code>pmfind</code> &#8211; find PCP services on the network</p>
<h2>SYNOPSIS</h2>
<p> <code>pmfind</code> [<code>-q</code>] [<code>-m</code> <i>mechanism</i>] [<code>-s</code> <i>service</i>] [<code>-r</code>] [<code>-t</code> <i>timeout</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pmfind</code> searches for instances of the specified PCP service being advertised on the network and prints a list of URLs corresponding to the services discovered. </p>
<p> By default <code>pmfind</code> will search for all supported PCP services, however a specific PCP <i>service</i> to discover can be specified using the <code>-s</code> option. Supported services are <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-pmproxy/">pmproxy</a></code>(1) and <code><a href="/docs/linux/man/1-pmwebd/">pmwebd</a></code>(1)<code>.</code> </p>
<p> The <code>-m</code> option sets the <i>mechanism</i> that <code>pmfind</code> uses when performing service discovery. By default, or if the keyword &quot;all&quot; is specified, every available mechanism will be used (iteratively). Supported mechanisms are:</p>
<dl>
<dt><code>avahi</code></p>
<dd> Searches for services which are broadcasting using mDNS via <code><a href="/docs/linux/man/8-avahi-daemon/">avahi-daemon</a>(8).</code> An optional suffix <code>&quot;,timeout=N&quot;</code> may be added to limit the amount of time waiting for the avahi-daemon. N is a floating point number specifying the number of seconds to wait. The default is 0.5 seconds. This timeout may also be specified by setting the environment variable <code>AVAHI_DISCOVERY_TIMEOUT</code> to the desired number of seconds. If both are specified, then the value specified in the environment variable takes precedence.</p>
<dt><code>probe=&lt;net-address&gt;/&lt;mask-bits&gt;</code></p>
<dd> Actively probes the given subnet for the requested PCP service(s). &lt;net-address&gt; is an inet or ipv6 network address and &lt;mask-bits&gt; is the number of bits used to define the subnet. For example, 192.168.1.0/24 defines an 8 bit subnet consisting of the addresses 192.168.1.0 through 192.168.1.255. An optional suffix <code>&quot;,maxThreads=N&quot;</code> may be added to limit the number of threads used while probing. The default is the value of FD_SETSIZE or the number of addresses in the subnet, whichever is less. An optional suffix <code>&quot;,timeout=N&quot;</code> may be added to limit the amount of time waiting for each connection attempt. N is a floating point number specifying the number of seconds to wait. The default is 20ms.</dl>
<p> The <code>-r</code> option requests that DNS name resolution be attempted for the addresses of any discovered services. The default is to display the network addresses of any discovered services. </p>
<p> The <code>-t</code> option sets the maximum amount of time that <code>pmfind</code> will take before interrupting the service discovery. The argument is a floating point number representing the number of seconds before timing out. The default is to take as much time as is needed to complete the process. </p>
<p> The <code>-q</code> option suppresses all output on the standard output stream.</p>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>DIAGNOSTICS</h2>
<p> The value of the exit status from the command is zero when services were successfully located, one if no services were found, and two if an error occurred. </p>
<p> In the event of an error, a message will be generated on standard error that is intended to be self-explanatory.</p>
<h2>SIGNALS</h2>
<p> <code>pmfind</code> will interrupt the service discovery process when one of the following signals is received: SIGHUP, SIGPIPE, SIGINT, SIGTERM, SIGXFSZ, SIGXCPU. <code>pmfind</code> will report any results which were discovered up to point of the interruption.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-pmproxy/">pmproxy</a></code>(1), <code><a href="/docs/linux/man/1-pmwebd/">pmwebd</a></code>(1), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmdiscoverservices/">pmDiscoverServices</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5). </p>
<h2>Index</h2>
