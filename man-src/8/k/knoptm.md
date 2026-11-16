---
title: "knoptm(8)"
name: "knoptm"
section: "8"
letter: "k"
url: "/docs/linux/man/8-knoptm/"
description: "knoptm – Daemon in charge to remove firewall rules."
---

<p><code>knoptm</code> &#8211; Daemon in charge to remove firewall rules. </p>
<h2>Description</h2>
<p><code>knoptm</code> is a daemon that removes rule entries from the iptables or ipfw policies to which fwknop has added access rules for legitimate fwknop PK/SPA clients. This daemon runs in all authentication modes supported by fwknopd (both port knocking and SPA), and enforces rule timeouts that defined by the <i>/etc/fwknop/access.conf</i> file. </p>
<h2>Options</h2>
<dl>
<dt><code>-c</code>, <code>&#8211;config&nbsp;<wbr>&lt;config-file&gt;</code></dt>
<dd>When run as a daemon <code>knoptm</code> references the file <code>/etc/fwknop/fwknop.conf</code> for various run-time configuration variables. The path to this file can be changed through the use of the <code>&#8211;config</code> command line option.</dd>
<dt><code>-i</code>, <code>&#8211;interface</code></dt>
<dd>Specify the interface that <code>fwknopd</code> sniffs to acquire packet data. This is used for running interface checks, such as checking whether the interface has been deleted and recreated (e.g. ppp restart for a VPN connection). The <code>fwknopd</code> daemon passes this argument on the <code>knoptm</code> command line.</dd>
<dt><code>&#8211;Debug-to-file&nbsp;<wbr>&lt;file&gt;</code></dt>
<dd>Allow the user to collect outputs from the knoptm daemon by writing debug informations to a specific file.</dd>
<dt><code>&#8211;firewall-type&nbsp;<wbr>&lt;firewall&gt;</code></dt>
<dd>Manually specify the firewall type from the command line.</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd>Display usage information and exit.</dd>
<dt><code>-V</code>, <code>&#8211;Version</code></dt>
<dd>Display version information and exit.</dd>
<dt><code>&#8211;Lib-dir&nbsp;<wbr>&lt;directory&gt;</code></dt>
<dd>Path to the perl modules directory (not usually necessary).</dd>
<dt><code>-l</code>, <code> &#8211;locale&nbsp;<wbr>&lt;locale&gt;</code></dt>
<dd>Provide a locale setting other than the default &quot;C&quot; locale.</dd>
<dt><code>&#8211;no-locale</code></dt>
<dd>Do not set the locale at all so that the default system locale will apply.</dd>
<dt><code>&#8211;no-logs</code></dt>
<dd>Do not generate any log output or emails (fwknop_test.pl uses this).</dd>
<dt><code>&#8211;no-voluntary-exits</code></dt>
<dd>Disregard ENABLE_VOLUNTARY_EXITS setting. This way fwknopd/knoptm is not allowed to be restarted periodically according to EXIT_INTERVAL.</dd>
<dt><code>-O</code>, <code>&#8211;Override-config&nbsp;<wbr>&lt;file&gt;</code></dt>
<dd>Override config variable values that are normally read from the /etc/fwknop/fwknop.conf file with values from the specified file. Multiple override config files can be given as a comma separated list. </dd>
</dl>
<h2>Diagnostics</h2>
<p><code>knoptm</code> can be run in debug mode with the &#8211;debug command line option. This will disable daemon mode execution, and print verbose information to the screen on STDERR.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-fwknopd/">fwknopd</a></code>(8), </p>
<h2>Author</h2>
<p>Michael Rash &lt;mbr [at] cipherdyne.org&gt;</p>
<h2>Distribution</h2>
<p><code>knoptm</code> is distributed under the GNU General Public License (GPL), and the latest version may be downloaded from <code><a rel="nofollow" href="http://www.cipherdyne.org/">http://www.cipherdyne.org/</a></code></p>
