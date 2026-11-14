---
title: "mrtg-ipv6(1)"
name: "mrtg-ipv6"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mrtg-ipv6/"
description: "mrtg-ipv6 – IPv6 support in MRTG"
---

<h2 class="name">NAME</h2>
<p> mrtg-ipv6 &#8211; IPv6 support in MRTG </p>
<h2>OVERVIEW</h2>
<p> <font SIZE="-1">MRTG</font> and cfgmaker support <font SIZE="-1">SNMP</font> over IPv6. IPv6 targets can be specified by hostname or IPv6 address, and if the required libraries are present (see below), queries will use IPv6.</p>
<h2>USAGE</h2>
<h3>Enabling IPv6</h3>
<p> IPv6 is currently disabled by default and must be explicitly enabled. In <font SIZE="-1">MRTG</font> this is done by turning on the <code>EnableIPv6</code> global option in the configuration file. In cfgmaker, it is enabled with the <code>&#8211;enable-ipv6</code> command-line option. </p>
<p> If IPv6 is disabled, <font SIZE="-1">MRTG</font> and cfgmaker should behave in exactly the same way as previous versions. So the addition of IPv6 support should have no effect on existing <font SIZE="-1">MRTG</font> setups unless IPv6 is enabled. </p>
<p> IPv6 support requires the Socket6 and <font SIZE="-1">INET6</font> libraries (see below). If <font SIZE="-1">MRTG</font> can&#8217;t find them, IPv6 is disabled.</p>
<h3>Specifying IPv6 targets</h3>
<p> IPv6 targets may be specified by name or IPv6 address. Numeric IPv6 addresses may be used with both cfgmaker and <font SIZE="-1">MRTG</font>, but they must be enclosed in square brackets. </p>
<p> For example, a target could be specified as: </p>
<pre>
 public@[2001:760:4::]:161
</pre>
<p> Hostnames work as expected: first an IPv6 name lookup is tried, then an IPv4 lookup.</p>
<h3>Targets that do not support <font SIZE="-1">SNMP</font> over IPv6</h3>
<p> Many targets (this currently includes all Cisco routers) do not yet support <font SIZE="-1">SNMP</font> over IPv6 and must be monitored over IPv4. This can cause problems if you specify a target through its <font SIZE="-1">DNS</font> name and the name maps to both the IPv6 address and the IPv4 address of the target: <font SIZE="-1">MRTG</font> will only try IPv6, and will fail. </p>
<p> To query these targets, use the <code>IPv4Only</code> per-target option, which tells <font SIZE="-1">MRTG</font> not to use <font SIZE="-1">SNMP</font> over IPv6 for the target. </p>
<p> <font SIZE="-1">MRTG</font> does not fall back to IPv4 for performance and correctness reasons. If there are many routers to query, a timeout for every router would make <font SIZE="-1">MRTG</font> take too long to query them all. And if, for some reason, IPv6 connectivity to the target is lost, <font SIZE="-1">MRTG</font>&#8216;s error messages can help figure out what is wrong. </p>
<p> cfgmaker does fall back from IPv6 to IPv4. If IPv6 is enabled and cfgmaker is given a hostname that resolves to both an IPv6 and an IPv4 address, it first tries to query the target over IPv6. If it receives no answer, it tries again using IPv4. If the target answers, cfgmaker sets the IPv4Only option in the generated config file.</p>
<h2>IPv6 LIBRARIES</h2>
<h3>Libraries required</h3>
<p> IPv6 support requires the <code>Socket6</code> and <font SIZE="-1"><code>INET6</code></font> Perl modules. Both can be downloaded from <font SIZE="-1">CPAN:</font> </p>
<p> <a rel="nofollow" href="http://search.cpan.org/author/UMEMOTO/Socket6/">http://search.cpan.org/author/UMEMOTO/Socket6/</a> </p>
<p> <a rel="nofollow" href="http://search.cpan.org/author/MONDEJAR/INET6/">http://search.cpan.org/author/MONDEJAR/INET6/</a> </p>
<p> If you use Debian, you will need the packages <code>libsocket6-perl</code> and <code>libio-socket-inet6-perl</code>, which are (or should soon be) in unstable. </p>
<p> So far, IPv6 support has been tested on Linux only, and only with Socket6 version 0.12. Also note that IPv6 won&#8217;t work at all if you don&#8217;t have <font SIZE="-1">INET6</font>.pm version 2.00 or newer.</p>
<h3>Installing the libraries</h3>
<p> Building and installing Socket6 and <font SIZE="-1">INET6</font> is very simple. For each module, just unpack the archive and then do: </p>
<pre>
 perl Makefile.PL
 make
</pre>
<p> and then: </p>
<pre>
 su
 make install
</pre>
<p> If you have installed the libraries successfully, cfgmaker and mrtg should automatically detect them and allow IPv6 support to be enabled.</p>
<h2>AUTHOR</h2>
<p> Lorenzo Colitti &lt;lorenzo location colitti.com&gt; </p>
<h2>Index</h2>
<dt><a href="#lbAH">IPv6 LIBRARIES</a></p>
<dd>
<dt><a href="#lbAK">AUTHOR</a></p>
<dd></dl>
