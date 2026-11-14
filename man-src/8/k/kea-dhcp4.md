---
title: "kea-dhcp4(8)"
name: "kea-dhcp4"
section: "8"
letter: "k"
url: "/docs/linux/man/8-kea-dhcp4/"
description: "kea-dhcp4 – DHCPv4 server in Kea"
---

<p>kea-dhcp4 &#8211; DHCPv4 server in Kea</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>kea-dhcp4</code> [<code>-v</code>] [<code>-V</code>] [<code>-W</code>] [<code>-d</code>] [<code>-c</code><i>config-file</i>] [<code>-p</code><i>port-number</i>]</dl>
<h2>Description</h2>
<dd>The <code>kea-dhcp4</code> daemon provides the DHCPv4 server implementation.</p>
<h2>Arguments</h2>
<p>The arguments are as follows: </p>
<p> <code>-v</code></p>
<dl>
<dd>Display the version.</dl>
<p> <code>-V</code></p>
<dl>
<dd>Display the extended version.</dl>
<p> <code>-W</code></p>
<dl>
<dd>Display the configuration report.</dl>
<p> <code>-d</code></p>
<dl>
<dd>Enable the debug mode with extra verbosity.</dl>
<p> <code>-c</code></p>
<dl>
<dd>Configuration file including the configuration for DHCPv4 server. It may also contain configuration entries for other Kea services.</dl>
<p> <code>-p</code></p>
<dl>
<dd>Port number (1-65535) on which the server listens. This is useful for testing purposes only.</dl>
<h2>Documentation</h2>
<p>Kea comes with an extensive Kea User&#8217;s Guide documentation that covers all aspects of running the Kea software &#8211; compilation, installation, configuration, configuration examples and many more. Kea also features a Kea Messages Manual, which lists all possible messages Kea can print with a brief description for each of them. Both documents are typically available in various formats (txt, html, pdf) with your Kea distribution. The on-line version is available at <a rel="nofollow" href="http://kea.isc.org/docs/.">http://kea.isc.org/docs/.</a> </p>
<p> Kea source code is documented in the Kea Developer&#8217;s Guide. It&#8217;s on-line version is available at <a rel="nofollow" href="http://kea.isc.org.">http://kea.isc.org.</a> Please follow Developer&#8217;s Guide link. </p>
<p> Kea project website is available at: <a rel="nofollow" href="http://kea.isc.org.">http://kea.isc.org.</a></p>
<h2>Mailing Lists And Support</h2>
<p>There are two mailing lists available for Kea project. kea-users (kea-users at lists.isc.org) is intended for Kea users, while kea-dev (kea-dev at lists.isc.org) is intended for Kea developers, prospective contributors and other advanced users. Both lists are available at <a rel="nofollow" href="http://lists.isc.org.">http://lists.isc.org.</a> The community provides best effort type of support on both of those lists. </p>
<p> ISC provides professional support for Kea services. See <a rel="nofollow" href="https://www.isc.org/kea/">https://www.isc.org/kea/</a> for details.</p>
<h2>History</h2>
<p>The <code>b10-dhcp4</code> daemon was first coded in November 2011 by Tomek Mrugalski. </p>
<p> In the mid 2014 Kea was decoupled from the BIND10 framework and became a standalone DHCP server. The DHCPv4 server binary was renamed to kea-dhcp4. Kea 1.0.0 was released in December 2015.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-kea-dhcp6/">kea-dhcp6</a></code>(8), <code><a href="/docs/linux/man/8-kea-dhcp-ddns/">kea-dhcp-ddns</a></code>(8), <code><a href="/docs/linux/man/8-kea-admin/">kea-admin</a></code>(8), <code><a href="/docs/linux/man/8-keactrl/">keactrl</a></code>(8), <code><a href="/docs/linux/man/8-perfdhcp/">perfdhcp</a></code>(8), <code><a href="/docs/linux/man/8-kea-lfc/">kea-lfc</a></code>(8), Kea Administrator&#8217;s Guide.</p>
<h2>Author</h2>
<p>The Kea software has been written by a number of engineers working for ISC: Tomek Mrugalski, Stephen Morris, Marcin Siodelski, Thomas Markwalder, Francis Dupont, Jeremy C. Reed, Wlodek Wencel and Shawn Routhier. That list is roughly in the chronological order in which the authors made their first contribution. For a complete list of authors and contributors, see AUTHORS file.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2011-2016 Internet Systems Consortium, Inc. (&quot;ISC&quot;)</p>
