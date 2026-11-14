---
title: "kea-lfc(8)"
name: "kea-lfc"
section: "8"
letter: "k"
url: "/docs/linux/man/8-kea-lfc/"
description: "kea-lfc – Lease File Cleanup process in Kea"
---

<p>kea-lfc &#8211; Lease File Cleanup process in Kea</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>kea-lfc</code> [<code>-4|-6</code>] [<code>-c&nbsp;<wbr></code><i>config-file</i>] [<code>-p&nbsp;<wbr></code><i>pid-file</i>] [<code>-x&nbsp;<wbr></code><i>previous-file</i>] [<code>-i&nbsp;<wbr></code><i>copy-file</i>] [<code>-o&nbsp;<wbr></code><i>output-file</i>] [<code>-f&nbsp;<wbr></code><i>finish-file</i>] [<code>-v</code>] [<code>-V</code>] [<code>-W</code>] [<code>-d</code>] [<code>-h</code>]</dl>
<h2>Description</h2>
<dd>The <code>kea-lfc</code> service process removes redundant information from the files used to provide persistent storage for the memfile data base backend. The service is written to run as a stand alone process. While it can be started externally, there is usually no need to do this. It will be run on a periodic basis by the Kea DHCP servers.</p>
<h2>Arguments</h2>
<p>The arguments are as follows: </p>
<p> <code>-d</code></p>
<dl>
<dd>Verbose mode sets the logging level to debug. This is primarily for development purposes in stand-alone mode.</dl>
<p> <code>-v</code></p>
<dl>
<dd>version causes the version stamp to be printed.</dl>
<p> <code>-V</code></p>
<dl>
<dd>Version causes a longer form of the version stamp to be printed.</dl>
<p> <code>-W</code></p>
<dl>
<dd>Display the configuration report.</dl>
<p> <code>-h</code></p>
<dl>
<dd>Help causes the usage string to be printed.</dl>
<p> <code>-4 | -6</code></p>
<dl>
<dd>The protocol version of the lease files, must be one of 4 or 6.</dl>
<p> <code>-c</code></p>
<dl>
<dd>Configuration file including the configuration for <code>kea-lfc</code> process. It may also contain configuration entries for other Kea services. Currently <code>kea-lfc</code> gets all of its arguments from the command line, in the future it will be extended to get some arguments from the config file.</dl>
<p> <code>-p</code></p>
<dl>
<dd>PID file &#8211; When the <code>kea-lfc</code> process starts it attempts to determine if another instance of the process is already running by examining the pid file. If one is already running the new process is terminated. If one isn&#8217;t running it writes its pid into the pid file.</dl>
<p> <code>-x</code></p>
<dl>
<dd>Previous or ex lease file &#8211; When <code>kea-lfc</code> starts this is the result of any previous run of <code>kea-lfc</code>. When <code>kea-lfc</code> finishes it is the result of this run. If <code>kea-lfc</code> is interrupted before completing, this file may not exist.</dl>
<p> <code>-i</code></p>
<dl>
<dd>Input or copy of lease file &#8211; Before the DHCP server invokes <code>kea-lfc</code> it will move the current lease file here and then call <code>kea-lfc</code> with this file.</dl>
<p> <code>-o</code></p>
<dl>
<dd>Output lease file &#8211; The temporary file <code>kea-lfc</code> should use to write the leases. Upon completion of writing this this file it will be moved to the finish file (see below).</dl>
<p> <code>-f</code></p>
<dl>
<dd>Finish or completion file &#8211; Another temporary file <code>kea-lfc</code> uses for bookkeeping. When <code>kea-lfc</code> completes writing the output file it moves it to this file name. After <code>kea-lfc</code> finishes deleting the other files (previous and input) it moves this file to previous lease file. By moving the files in this fashion the <code>kea-lfc</code> and the DHCP server processes can determine the correct file to use even if one of the processes was interrupted before completing its task.</dl>
<h2>Documentation</h2>
<p>Kea comes with an extensive Kea User&#8217;s Guide documentation that covers all aspects of running the Kea software &#8211; compilation, installation, configuration, configuration examples and many more. Kea also features a Kea Messages Manual, which lists all possible messages Kea can print with a brief description for each of them. Both documents are typically available in various formats (txt, html, pdf) with your Kea distribution. The on-line version is available at <a rel="nofollow" href="http://kea.isc.org/docs/.">http://kea.isc.org/docs/.</a> </p>
<p> Kea source code is documented in the Kea Developer&#8217;s Guide. It&#8217;s on-line version is available at <a rel="nofollow" href="http://kea.isc.org.">http://kea.isc.org.</a> Please follow Developer&#8217;s Guide link. </p>
<p> Kea project website is available at: <a rel="nofollow" href="http://kea.isc.org.">http://kea.isc.org.</a></p>
<h2>Mailing Lists And Support</h2>
<p>There are two mailing lists available for Kea project. kea-users (kea-users at lists.isc.org) is intended for Kea users, while kea-dev (kea-dev at lists.isc.org) is intended for Kea developers, prospective contributors and other advanced users. Both lists are available at <a rel="nofollow" href="http://lists.isc.org.">http://lists.isc.org.</a> The community provides best effort type of support on both of those lists. </p>
<p> ISC provides professional support for Kea services. See <a rel="nofollow" href="https://www.isc.org/kea/">https://www.isc.org/kea/</a> for details.</p>
<h2>History</h2>
<p>The <code>kea-lfc</code> process was first coded in January 2015 by the ISC Kea/DHCP team.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-kea-dhcp4/">kea-dhcp4</a></code>(8), <code><a href="/docs/linux/man/8-kea-dhcp6/">kea-dhcp6</a></code>(8), <code><a href="/docs/linux/man/8-kea-dhcp-ddns/">kea-dhcp-ddns</a></code>(8), <code><a href="/docs/linux/man/8-kea-admin/">kea-admin</a></code>(8), <code><a href="/docs/linux/man/8-keactrl/">keactrl</a></code>(8), <code><a href="/docs/linux/man/8-perfdhcp/">perfdhcp</a></code>(8), Kea Administrator&#8217;s Guide.</p>
<h2>Author</h2>
<p>The Kea software has been written by a number of engineers working for ISC: Tomek Mrugalski, Stephen Morris, Marcin Siodelski, Thomas Markwalder, Francis Dupont, Jeremy C. Reed, Wlodek Wencel and Shawn Routhier. That list is roughly in the chronological order in which the authors made their first contribution. For a complete list of authors and contributors, see AUTHORS file.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2015 Internet Systems Consortium, Inc. (&quot;ISC&quot;)</p>
