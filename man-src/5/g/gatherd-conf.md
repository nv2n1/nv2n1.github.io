---
title: "gatherd-conf(5)"
name: "gatherd-conf"
section: "5"
letter: "g"
url: "/docs/linux/man/5-gatherd-conf/"
description: "gatherd.conf – SBLIM metric repository daemon configuration file"
---

<p>gatherd.conf &#8211; SBLIM metric repository daemon configuration file</p>
<h2>Description</h2>
<p>The file <i>gatherd.conf</i> is read by <code><a href="/docs/linux/man/8-gatherd/">gatherd</a></code>(8) at startup. Each line consists of a configuration option value pair delimited by an &#8216;=&#8217; character. A &#8216;#&#8217; (number sign) indicates the beginning of a comment.</p>
<h2>Options</h2>
<p><code>RepositoryHost</code>=<i>addr</i></p>
<dl>
<dd>The ip address of the remote repository daemon to which metric values will be sent. Default is <code>localhost</code>.</dl>
<p> <code>RepositoryPort</code>=<i>port</i></p>
<dl>
<dd>TCP port of remote repository daemon. Default is <code>6363</code>.</dl>
<p> <code>TraceLevel</code>=<i>level</i></p>
<dl>
<dd>Trace level for the <code>gatherd</code> process. Default is <code>0</code>.</dl>
<p> <code>TraceFile</code>=<i>file</i></p>
<dl>
<dd>Name of file to write tracing information. Default is <code>stderr</code>.</dl>
<p> <code>TraceComponents</code>=<i>comps[:comps&#8230;]</i></p>
<dl>
<dd>Gatherer components to be traced seperated by a colon (:). Valid components are: comm, util, gather, rrepos. Default is <code>none</code>.</dl>
<p> <code>PluginDirectory</code>=<i>dir</i></p>
<dl>
<dd>Directory where metric collection plugins are located. Default is <code>/usr/lib/gather/mplug</code> (<code>/usr/lib64/gather/mplug</code>).</dl>
<p> <code>AutoLoad</code>=<i>plugin[:plugin&#8230;]</i></p>
<dl>
<dd>Plugins to automatically load, initalize and start sampling. Valid values are: * or colon-seperated list. Default is <code>none</code>.</dl>
<p> <code>SampleInterval</code>=<i>secs</i></p>
<dl>
<dd>If specified this interval will override the plugin defined individual sampling intervals. Unit is in seconds. </p>
<p> <code>WARNING:</code> This config option should only be used for debugging purposes. It overrides the per metric defined sample interval of all plugins, and really short intervals can introduce skew in the data due to seconds not being a high enough sample resolution.</dl>
<p> <code>Synchronization</code>=<i>0|1</i></p>
<dl>
<dd>Specifies whether the metric plugins are invoked in a time-synchronized manner. Synchronized metrics with the same sample interval will be scheduled together. Possible values are: </p>
<dl>
<dd>
<pre>1 synchronized relative to Jan, 1st, 1970, 00:00</pre>
</dl>
<dl>
<dd>
<pre>0 unsynchronized, will be scheduled asap</pre>
</dl>
<p> Default is <code>1</code>.</dl>
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
<p><code>gatherd.conf</code> is distributed under the terms of the Eclipse Public License (&quot;Agreement&quot;). Any use, reproduction or distribution of this program constitutes recipeients acceptance of the agreement. </p>
<p> You can obtain a current copy of the Eclipse Public License from <a rel="nofollow" href="http://www.opensource.org/licenses/eclipse-1.0.php">http://www.opensource.org/licenses/eclipse-1.0.php</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-gatherd/">gatherd</a></code>(8) </p>
