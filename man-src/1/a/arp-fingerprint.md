---
title: "arp-fingerprint(1)"
name: "arp-fingerprint"
section: "1"
letter: "a"
url: "/docs/linux/man/1-arp-fingerprint/"
description: "arp-fingerprint – Fingerprint a system using ARP"
---

<h2 class="name">NAME</h2>
<p> arp-fingerprint &#8211; Fingerprint a system using ARP </p>
<h2>SYNOPSIS</h2>
<p> <code>arp-fingerprint</code> [<i>options</i>] <i>target</i> </p>
<p> The target should be specified as a single IP address or hostname. You cannot specify multiple targets, IP networks or ranges. </p>
<p> If you use an IP address for the target, you can use the <code>-o</code> option to pass the <code>&#8211;numeric</code> option to <code>arp-scan</code>, which will prevent it from attempting DNS lookups. This can speed up the fingerprinting process, especially on systems with a slow or faulty DNS configuration.</p>
<h2>DESCRIPTION</h2>
<p> <code>arp-fingerprint</code> fingerprints the specified target host using the ARP protocol. </p>
<p> It sends various different types of ARP request to the target, and records which types it responds to. From this, it constructs a fingerprint string consisting of &quot;1&quot; where the target responded and &quot;0&quot; where it did not. An example of a fingerprint string is <i>01000100000</i>. This fingerprint string is then used to lookup the likely target operating system. </p>
<p> Many of the fingerprint strings are shared by several operating systems, so there is not always a one-to-one mapping between fingerprint strings and operating systems. Also the fact that a system&#8217;s fingerprint matches a certain operating system (or list of operating systems) does not necessarily mean that the system being fingerprinted is that operating system, although it is quite likely. This is because the list of operating systems is not exhaustive; it is just what I have discovered to date, and there are bound to be operating systems that are not listed. </p>
<p> The ARP fingerprint of a system is generally a function of that system&#8217;s kernel (although it is possible for the ARP function to be implemented in user space, it almost never is). </p>
<p> Sometimes, an operating system can give different fingerprints depending on the configuration. An example is Linux, which will respond to a non-local source IP address if that IP is routed through the interface being tested. This is both good and bad: on one hand it makes the fingerprinting task more complex; but on the other, it can allow some aspects of the system configuration to be determined. </p>
<p> Sometimes the fact that two different operating systems share a common ARP fingerprint string points to a re-use of networking code. One example of this is Windows NT and FreeBSD. </p>
<p> <code>arp-fingerprint</code> uses <code>arp-scan</code> to send the ARP requests and receive the replies. </p>
<p> There are other methods that can be used to fingerprint a system using <code>arp-scan</code> which can be used in addition to <code>arp-fingerprint</code>. These additional methods are not included in <code>arp-fingerprint</code> either because they are likely to cause disruption to the target system, or because they require knowledge of the target&#8217;s configuration that may not always be available. </p>
<p> <code>arp-fingerprint</code> is still being developed, and the results should not be relied on. As most of the ARP requests that it sends are non-standard, it is possible that it may disrupt some systems, so caution is advised. </p>
<p> If you find a system that <code>arp-fingerprint</code> reports as <i>UNKNOWN</i>, and you know what operating system it is running, could you please send details of the operating system and fingerprint to <i>arp-scan [at] nta-monitor.com</i> so I can include it in future versions. Please include the exact version of the operating system if you know it, as fingerprints sometimes change between versions.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> Display a brief usage message and exit.</p>
<dt><code>-v</code></p>
<dd> Display verbose progress messages.</p>
<dt><code>-o &lt;option-string&gt;</code></p>
<dd> Pass specified options to arp-scan. You need to enclose the options string in quotes if it contains spaces. e.g. -o &quot;-I eth1&quot;. The commonly used options are &#8211;interface (-I) and &#8211;numeric (-N).</dl>
<h2>EXAMPLES</h2>
<pre>
$ arp-fingerprint 192.168.0.1
192.168.0.1   01000100000     Linux 2.2, 2.4, 2.6
</pre>
<pre>
$ arp-fingerprint -o &quot;-N -I eth1&quot; 192.168.0.202
192.168.0.202 11110100000     FreeBSD 5.3, Win98, WinME, NT4, 2000, XP, 2003
</pre>
<h2>NOTES</h2>
<p> <code>arp-fingerprint</code> is implemented in Perl, so you need to have the Perl interpreter installed on your system to use it.</p>
<h2>AUTHOR</h2>
<p> Roy Hills &lt;Roy.Hills [at] nta-monitor.com&gt;</p>
<h2>SEE ALSO</h2>
<dl>
<dt><code><a href="/docs/linux/man/1-arp-scan/">arp-scan</a></code>(1)</p>
<dd></dl>
<p> <i><a rel="nofollow" href="http://www.nta-monitor.com/wiki/">http://www.nta-monitor.com/wiki/</a></i> The arp-scan wiki page. </p>
<h2>Index</h2>
