---
title: "cups-lpd(8)"
name: "cups-lpd"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cups-lpd/"
description: "cups-lpd – receive print jobs and report printer status to lpd clients (deprecated)"
---

<p>cups-lpd &#8211; receive print jobs and report printer status to lpd clients (deprecated)</p>
<h2>Synopsis</h2>
<p><code>cups-lpd</code> [ <code>-h </code><i>hostname</i>[<code>:</code><i>port</i>] ] [ <code>-n</code> ] [ <code>-o</code> <i>option=value</i> ]</p>
<h2>Description</h2>
<p><code>cups-lpd</code> is the CUPS Line Printer Daemon (&quot;LPD&quot;) mini-server that supports legacy client systems that use the LPD protocol. <code>cups-lpd</code> does not act as a standalone network daemon but instead operates using any of the Internet &quot;super-servers&quot; such as <code><a href="/docs/linux/man/8-inetd/">inetd</a></code>(8), <code><a href="/docs/linux/man/8-launchd/">launchd</a></code>(8), and <code><a href="/docs/linux/man/8-systemd/">systemd</a></code>(8).</p>
<h2>Options</h2>
<dl>
<dt><code>-h </code><i>hostname</i>[<code>:</code><i>port</i>]</p>
<dd>Sets the CUPS server (and port) to use.</p>
<dt><code>-n</code></p>
<dd>Disables reverse address lookups; normally <code>cups-lpd</code> will try to discover the hostname of the client via a reverse DNS lookup.</p>
<dt><code>-o </code><i>name=value</i></p>
<dd>Inserts options for all print queues. Most often this is used to disable the &quot;l&quot; filter so that remote print jobs are filtered as needed for printing; the <code><a href="/docs/linux/man/8-inetd/">inetd</a></code>(8) example below sets the &quot;document-format&quot; option to &quot;application/octet-stream&quot; which forces autodetection of the print file format.</dl>
<h2>Conforming To</h2>
<p><code>cups-lpd</code> does not enforce the restricted source port number specified in RFC 1179, as using restricted ports does not prevent users from submitting print jobs. While this behavior is different than standard Berkeley LPD implementations, it should not affect normal client operations. </p>
<p> The output of the status requests follows RFC 2569, Mapping between LPD and IPP Protocols. Since many LPD implementations stray from this definition, remote status reporting to LPD clients may be unreliable.</p>
<h2>Errors</h2>
<p>Errors are sent to the system log.</p>
<h2>Files</h2>
<pre><i>/etc/inetd.conf</i>
<i>/etc/xinetd.d/cups-lpd</i>
<i>/System/Library/LaunchDaemons/org.cups.cups-lpd.plist</i></pre>
<h2>Notes</h2>
<p>The <code>cups-lpd</code> program is deprecated and will no longer be supported in a future feature release of CUPS.</p>
<h3>Performance</h3>
<p><code>cups-lpd</code> performs well with small numbers of clients and printers. However, since a new process is created for each connection and since each process must query the printing system before each job submission, it does not scale to larger configurations. We highly recommend that large configurations use the native IPP support provided by CUPS instead.</p>
<h3>Security</h3>
<p><code>cups-lpd</code> currently does not perform any access control based on the settings in <i><a href="/docs/linux/man/5-cupsd-conf/">cupsd.conf</a>(5)</i> or in the <i><a href="/docs/linux/man/5-hosts-allow/">hosts.allow</a>(5)</i> or <i><a href="/docs/linux/man/5-hosts-deny/">hosts.deny</a>(5)</i> files used by TCP wrappers. Therefore, running <code>cups-lpd</code> on your server will allow any computer on your network (and perhaps the entire Internet) to print to your server. </p>
<p> While <code><a href="/docs/linux/man/8-xinetd/">xinetd</a></code>(8) has built-in access control support, you should use the TCP wrappers package with <code><a href="/docs/linux/man/8-inetd/">inetd</a></code>(8) to limit access to only those computers that should be able to print through your server. </p>
<p> <code>cups-lpd</code> is not enabled by the standard CUPS distribution. Please consult with your operating system vendor to determine whether it is enabled by default on your system.</p>
<h2>Example</h2>
<p>If you are using <code><a href="/docs/linux/man/8-inetd/">inetd</a></code>(8), add the following line to the <i>inetd.conf</i> file to enable the <code>cups-lpd</code> mini-server: </p>
<pre> printer stream tcp nowait lp /usr/lib/cups/daemon/cups-lpd cups-lpd \
 -o document-format=application/octet-stream</pre>
<p>CUPS includes configuration files for <code><a href="/docs/linux/man/8-launchd/">launchd</a></code>(8), <code><a href="/docs/linux/man/8-systemd/">systemd</a></code>(8), and <code><a href="/docs/linux/man/8-xinetd/">xinetd</a></code>(8). Simply enable the <code>cups-lpd</code> service using the corresponding control program.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-cups/">cups</a></code>(1), <code><a href="/docs/linux/man/8-cupsd/">cupsd</a></code>(8), <code><a href="/docs/linux/man/8-inetd/">inetd</a></code>(8), <code><a href="/docs/linux/man/8-launchd/">launchd</a></code>(8), <code><a href="/docs/linux/man/8-xinetd/">xinetd</a></code>(8), CUPS Online Help (<a rel="nofollow" href="http://localhost:631/help">http://localhost:631/help</a>), RFC 2569</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2020-2022 by OpenPrinting.</p>
