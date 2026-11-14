---
title: "reposd-conf(5)"
name: "reposd-conf"
section: "5"
letter: "r"
url: "/docs/linux/man/5-reposd-conf/"
description: "reposd.conf – SBLIM metric repository daemon configuration file"
---

<p>reposd.conf &#8211; SBLIM metric repository daemon configuration file</p>
<h2>Description</h2>
<p>The file <i>reposd.conf</i> is read by <code><a href="/docs/linux/man/8-reposd/">reposd</a></code>(8) at startup. Each line consists of a configuration option value pair delimited by an &#8216;=&#8217; character. A &#8216;#&#8217; (number sign) indicates the beginning of a comment.</p>
<h2>Options</h2>
<p><code>RepositoryPort</code>=<i>port</i></p>
<dl>
<dd>TCP port repository daemon will listen. Default is <code>6363</code>.</dl>
<p> <code>RepositoryMaxConnections</code>=<i>conns</i></p>
<dl>
<dd>Number of parallel client connections the repository daemon is able to handle. Default is <code>100</code>.</dl>
<p> <code>TraceLevel</code>=<i>level</i></p>
<dl>
<dd>Trace level for the <code>reposd</code> process. Default is <code>0</code>.</dl>
<p> <code>TraceFile</code>=<i>file</i></p>
<dl>
<dd>Name of file to write tracing information. Default is <code>stderr</code>.</dl>
<p> <code>TraceComponents</code>=<i>comps[:comps&#8230;]</i></p>
<dl>
<dd>Repository components to be traced seperated by a colon (:). Valid components are: comm, util, repos. Default is <code>none</code>.</dl>
<p> <code>PluginDirectory</code>=<i>dir</i></p>
<dl>
<dd>Directory where repository metric plugins are located. Default is <code>/usr/lib/gather/rplug</code> (<code>/usr/lib64/gather/rplug</code>).</dl>
<p> <code>AutoLoad</code>=<i>plugin[:plugin&#8230;]</i></p>
<dl>
<dd>Plugins to be automatically load, initalize and start sampling. Valid values are: * or colon-seperated list. Default is <code>none</code>.</dl>
<p> <code>ExpirationInterval</code>=<i>secs</i></p>
<dl>
<dd>Specifies how many seconds metric values are kept in the in-core repository. Note that the longer the interval is the more memory that will be consumed by <code>reposd</code>. Valid values are: and integer between 60 and 86400. Default is <code>1200</code>.</dl>
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
<p><code>reposd.conf</code> is distributed under the terms of the Eclipse Public License (&quot;Agreement&quot;). Any use, reproduction or distribution of this program constitutes recipeients acceptance of the agreement. </p>
<p> You can obtain a current copy of the Eclipse Public License from <a rel="nofollow" href="http://www.opensource.org/licenses/eclipse-1.0.php">http://www.opensource.org/licenses/eclipse-1.0.php</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-reposd/">reposd</a></code>(8) </p>
