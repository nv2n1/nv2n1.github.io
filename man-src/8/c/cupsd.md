---
title: "cupsd(8)"
name: "cupsd"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cupsd/"
description: "cupsd – cups scheduler"
---

<p>cupsd &#8211; cups scheduler</p>
<h2>Synopsis</h2>
<p><code>cupsd</code> [ <code>-c</code> <i>cupsd.conf</i> ] [ <code>-f</code> ] [ <code>-F</code> ] [ <code>-h</code> ] [ <code>-l</code> ] [ <code>-s</code> <i>cups-files.conf</i> ] [ <code>-t</code> ]</p>
<h2>Description</h2>
<p><code>cupsd</code> is the scheduler for CUPS. It implements a printing system based upon the Internet Printing Protocol, version 2.1, and supports most of the requirements for IPP Everywhere. If no options are specified on the command-line then the default configuration file <i>/etc/cups/cupsd.conf</i> will be used.</p>
<h2>Options</h2>
<dl>
<dt><code>-c</code><i>&nbsp;cupsd.conf</i></p>
<dd>Uses the named cupsd.conf configuration file.</p>
<dt><code>-f</code></p>
<dd>Run <code>cupsd</code> in the foreground; the default is to run in the background as a &quot;daemon&quot;.</p>
<dt><code>-F</code></p>
<dd>Run <code>cupsd</code> in the foreground but detach the process from the controlling terminal and current directory. This is useful for running <code>cupsd</code> from <code><a href="/docs/linux/man/8-init/">init</a></code>(8).</p>
<dt><code>-h</code></p>
<dd>Shows the program usage.</p>
<dt><code>-l</code></p>
<dd>This option is passed to <code>cupsd</code> when it is run from <code><a href="/docs/linux/man/8-launchd/">launchd</a></code>(8) or <code><a href="/docs/linux/man/8-systemd/">systemd</a></code>(8).</p>
<dt><code>-s</code><i>&nbsp;cups-files.conf</i></p>
<dd>Uses the named cups-files.conf configuration file.</p>
<dt><code>-t</code></p>
<dd>Test the configuration file for syntax errors.</dl>
<h2>Files</h2>
<pre><i>/etc/cups/classes.conf</i>
<i>/etc/cups/cups-files.conf</i>
<i>/etc/cups/cupsd.conf</i>
<i>/usr/share/cups/mime/mime.convs</i>
<i>/usr/share/cups/mime/mime.types</i>
<i>/etc/cups/printers.conf</i>
<i>/etc/cups/subscriptions.conf</i></pre>
<h2>Conforming To</h2>
<p><code>cupsd</code> implements all of the required IPP/2.1 attributes and operations. It also implements several CUPS-specific administrative operations.</p>
<h2>Examples</h2>
<p>Run <code>cupsd</code> in the background with the default configuration file: </p>
<pre> cupsd</pre>
<p>Test a configuration file called <i>test.conf</i>: </p>
<pre> cupsd -t -c test.conf</pre>
<p>Run <code>cupsd</code> in the foreground with a test configuration file called <i>test.conf</i>: </p>
<pre> cupsd -f -c test.conf</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-backend/">backend</a></code>(7), <code><a href="/docs/linux/man/5-classes-conf/">classes.conf</a></code>(5), <code><a href="/docs/linux/man/1-cups/">cups</a></code>(1), <code><a href="/docs/linux/man/5-cups-files-conf/">cups-files.conf</a></code>(5), <code><a href="/docs/linux/man/8-cups-lpd/">cups-lpd</a></code>(8), <code><a href="/docs/linux/man/5-cupsd-conf/">cupsd.conf</a></code>(5), <code><a href="/docs/linux/man/8-cupsd-helper/">cupsd-helper</a></code>(8), <code><a href="/docs/linux/man/8-cupsd-logs/">cupsd-logs</a></code>(8), <code><a href="/docs/linux/man/7-filter/">filter</a></code>(7), <code><a href="/docs/linux/man/8-launchd/">launchd</a></code>(8), <code><a href="/docs/linux/man/5-mime-convs/">mime.convs</a></code>(5), <code><a href="/docs/linux/man/5-mime-types/">mime.types</a></code>(5), <code><a href="/docs/linux/man/5-printers-conf/">printers.conf</a></code>(5), <code><a href="/docs/linux/man/8-systemd/">systemd</a></code>(8), CUPS Online Help (<a rel="nofollow" href="http://localhost:631/help)">http://localhost:631/help)</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2021-2022 by OpenPrinting.</p>
