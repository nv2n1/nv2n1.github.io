---
title: "gatherd(8)"
name: "gatherd"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gatherd/"
description: "gatherd – SBLIM metric collection daemon"
---

<p>gatherd &#8211; SBLIM metric collection daemon</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>gatherd</code> [<i>argument</i>]</dl>
<h2>Description</h2>
<dd>The <code>gatherd</code> program is a system daemon that collects performance metrics for various components via a set of metric plugins. Raw metric data is forwarded to a seperate repository daemon that is located either locally or remotely (see <code><a href="/docs/linux/man/8-reposd/">reposd</a></code>(8)). The repository destination, location of plugin directory, and other controllable configuration options are described in the configuration file man page (see <code><a href="/docs/linux/man/5-gatherd-conf/">gatherd.conf</a></code>(5)). </p>
<p> The <code>gatherd</code> daemon can be controlled at runtime by way of the <code><a href="/docs/linux/man/8-gatherctl/">gatherctl</a></code>(8) command. This provides the ability to load and unload metric plugins online without the need to restart <code>gatherd</code>. </p>
<p> The primary goal of the the sblim-gather package is to implement the DMTF&#8217;s Base Metric Model (DSP1053). While, <code>gatherd</code>, <code><a href="/docs/linux/man/8-reposd/">reposd</a></code>(8), and their plugins can be used standalone, the greatest benefit comes from using their CIM provider layer in conjuction with a CIM Object Manager (see <code><a href="/docs/linux/man/1-cimserver/">cimserver</a></code>(1)). For more information about CIM and the Base Metric Model refer to the Distrubuted Management Task Force (DMTF) at <a rel="nofollow" href="http://www.dmtf.org.">http://www.dmtf.org.</a></p>
<h2>Options</h2>
<p><i>argument</i></p>
<dl>
<dd><code>gatherd</code> daemonizes by default. Passing any value on the command line will cause it to run in the terminal.</dl>
<h2>Files</h2>
<p><i>/etc/gatherd.conf</i></p>
<dl>
<dd>This file contains the daemon configuration settings. See <code><a href="/docs/linux/man/5-gatherd-conf/">gatherd.conf</a></code>(5) for more information.</dl>
<h2>Bugs</h2>
<p>The SBLIM project maintains a mailing list to which you should direct all questions regarding sfcb, sfcc, wbemcli, the metric data gatherer, or any of the SBLIM providers. To subscribe to this list visit:</p>
<dl>
<dd>
<pre><a rel="nofollow" href="https://lists.sourceforge.net/lists/listinfo/sblim-issues">https://lists.sourceforge.net/lists/listinfo/sblim-issues</a></pre>
</dl>
<p> Please report bugs you discover to the bug tracker. The SBLIM project bug tracking page can be found at:</p>
<dl>
<dd>
<pre><a rel="nofollow" href="https://sourceforge.net/tracker/?group_id=128809">https://sourceforge.net/tracker/?group_id=128809</a>&amp;atid=712784</pre>
</dl>
<h2>Authors</h2>
<p>Please refer to the AUTHORS file distributed with sblim-gather.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2003-2012 IBM Corp.</p>
<h2>License</h2>
<p><code>gatherd</code> is distributed under the terms of the Eclipse Public License (&quot;Agreement&quot;). Any use, reproduction or distribution of this program constitutes recipeients acceptance of the agreement. </p>
<p> You can obtain a current copy of the Eclipse Public License from <a rel="nofollow" href="http://www.opensource.org/licenses/eclipse-1.0.php">http://www.opensource.org/licenses/eclipse-1.0.php</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-gatherctl/">gatherctl</a></code>(8), <code><a href="/docs/linux/man/5-gatherd-conf/">gatherd.conf</a></code>(5), <code><a href="/docs/linux/man/8-reposd/">reposd</a></code>(8), <code><a href="/docs/linux/man/1-cimserver/">cimserver</a></code>(1) </p>
