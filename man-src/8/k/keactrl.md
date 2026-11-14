---
title: "keactrl(8)"
name: "keactrl"
section: "8"
letter: "k"
url: "/docs/linux/man/8-keactrl/"
description: "keactrl – Shell script for managing Kea"
---

<p>keactrl &#8211; Shell script for managing Kea</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>keactrl</code> [command] [<code>-c&nbsp;<wbr></code><i>keactrl-config-file</i>] [<code>-s&nbsp;<wbr></code><i>server[,server,&#8230;]</i>]</dl>
<h2>Description</h2>
<dd>keactrl is a shell script which controls the startup, shutdown and reconfiguration of the Kea servers (<code>kea-dhcp4</code>, <code>kea-dhcp6</code> and <code>kea-dhcp-ddns</code>). It also provides the means for checking the current status of the servers and determining the configuration files in use.</p>
<h2>Configuration File</h2>
<p>Depending on requirements, not all of the available servers need be run. The keactrl configuration file sets which servers are enabled and which are disabled. By default the configuration file is [kea-install-dir]/etc/kea/keactrl.conf. </p>
<p> See the Kea Administrator&#8217;s Guide for the documentation of the parameters in the <code>keactrl</code> configuration file.</p>
<h2>Options</h2>
<p><i>command</i></p>
<dl>
<dd>Command to be issued to the servers. It can be one of the following: </p>
<p> start</p>
<dl>
<dd>Start the servers.</dl>
<p> stop</p>
<dl>
<dd>Stop the servers.</dl>
<p> reload</p>
<dl>
<dd>Instructs the servers to re-read the kea configuration file.</dl>
<p> status</p>
<dl>
<dd>Print the status of the servers.</dl>
</dl>
<p> <code>-c|&#8211;ctrl-config </code><i>keactrl-config-file</i></p>
<dl>
<dd>Specify the <code>keactrl</code> configuration file. Without this switch, the <code>keactrl</code> will attempt to use the file [kea-install-dir]/etc/kea/keactrl.conf.</dl>
<p> <code>-s|&#8211;server </code><i>server[,server,&#8230;]</i></p>
<dl>
<dd>Specifies a subset of the enabled servers to which the command should be issued. The list of servers should be separated by commas with no intervening spaces. Acceptable values are: </p>
<p> dhcp4</p>
<dl>
<dd>DHCPv4 server (<code>kea-dhcp4</code>).</dl>
<p> dhcp6</p>
<dl>
<dd>DHCPv6 server (<code>kea-dhcp6</code>).</dl>
<p> dhcp_ddns</p>
<dl>
<dd>DHCP DDNS server (<code>kea-dhcp-ddns</code>).</dl>
<p> all</p>
<dl>
<dd>All servers (default).</dl>
</dl>
<h2>Documentation</h2>
<p>Kea comes with an extensive Kea User&#8217;s Guide documentation that covers all aspects of running the Kea software &#8211; compilation, installation, configuration, configuration examples and many more. Kea also features a Kea Messages Manual, which lists all possible messages Kea can print with a brief description for each of them. Both documents are typically available in various formats (txt, html, pdf) with your Kea distribution. The on-line version is available at <a rel="nofollow" href="http://kea.isc.org/docs/.">http://kea.isc.org/docs/.</a> </p>
<p> Kea source code is documented in the Kea Developer&#8217;s Guide. It&#8217;s on-line version is available at <a rel="nofollow" href="http://kea.isc.org.">http://kea.isc.org.</a> Please follow Developer&#8217;s Guide link. </p>
<p> Kea project website is available at: <a rel="nofollow" href="http://kea.isc.org.">http://kea.isc.org.</a></p>
<h2>Mailing Lists And Support</h2>
<p>There are two mailing lists available for Kea project. kea-users (kea-users at lists.isc.org) is intended for Kea users, while kea-dev (kea-dev at lists.isc.org) is intended for Kea developers, prospective contributors and other advanced users. Both lists are available at <a rel="nofollow" href="http://lists.isc.org.">http://lists.isc.org.</a> The community provides best effort type of support on both of those lists. </p>
<p> ISC provides professional support for Kea services. See <a rel="nofollow" href="https://www.isc.org/kea/">https://www.isc.org/kea/</a> for details.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-kea-dhcp4/">kea-dhcp4</a></code>(8), <code><a href="/docs/linux/man/8-kea-dhcp6/">kea-dhcp6</a></code>(8), <code><a href="/docs/linux/man/8-kea-dhcp-ddns/">kea-dhcp-ddns</a></code>(8), <code><a href="/docs/linux/man/8-kea-admin/">kea-admin</a></code>(8), <code><a href="/docs/linux/man/8-perfdhcp/">perfdhcp</a></code>(8), <code><a href="/docs/linux/man/8-kea-lfc/">kea-lfc</a></code>(8), Kea Administrator&#8217;s Guide.</p>
<h2>Author</h2>
<p>The Kea software has been written by a number of engineers working for ISC: Tomek Mrugalski, Stephen Morris, Marcin Siodelski, Thomas Markwalder, Francis Dupont, Jeremy C. Reed, Wlodek Wencel and Shawn Routhier. That list is roughly in the chronological order in which the authors made their first contribution. For a complete list of authors and contributors, see AUTHORS file.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2014-2016 Internet Systems Consortium, Inc. (&quot;ISC&quot;)</p>
