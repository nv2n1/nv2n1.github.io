---
title: "reposctl(8)"
name: "reposctl"
section: "8"
letter: "r"
url: "/docs/linux/man/8-reposctl/"
description: "reposctl – control utility for reposd"
---

<p>reposctl &#8211; control utility for reposd</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>reposctl</code></dl>
<h2>Description</h2>
<p><code>reposctl</code></p>
<dd>is a simple shell program for controling the <code><a href="/docs/linux/man/8-reposd/">reposd</a></code>(8) metric repository daemon. It provides the ability to manipulate the state of the daemon as well as online loading and unloading of metric repository plugins.</p>
<h2>Commands</h2>
<p><code>h</code></p>
<dl>
<dd>print help message</dl>
<p> <code>s</code></p>
<dl>
<dd>print status of daemon</dl>
<p> <code>i</code></p>
<dl>
<dd>initialize repository service</dl>
<p> <code>t</code></p>
<dl>
<dd>terminate repository service</dl>
<p> <code>l</code> <i>pluginlib</i></p>
<dl>
<dd>load plugin library</dl>
<p> <code>u</code> <i>pluginlib</i></p>
<dl>
<dd>unload plugin library</dl>
<p> <code>v</code> <i>pluginlib</i></p>
<dl>
<dd>view/list metrics supported by plugin library</dl>
<p> <code>q</code></p>
<dl>
<dd>quit/exit control utility</dl>
<p> <code>g</code> <i>id</i></p>
<dl>
<dd>retrieve values for given metric id</dl>
<p> <code>f</code> <i>id</i> <i>num</i></p>
<dl>
<dd>retrieve filtered (top-n, sorted) values for given metric id</dl>
<p> <code>r</code> <i>id</i></p>
<dl>
<dd>list system and type of resource for given metrid id</dl>
<p> <code>G</code></p>
<dl>
<dd>list current global metric filter</dl>
<p> <code>F</code> <i>num</i></p>
<dl>
<dd>set the global metric filter</dl>
<p> <code>k</code></p>
<dl>
<dd>kill gathering daemon</dl>
<p> <code>d</code></p>
<dl>
<dd>start gathering daemon</dl>
<h2>Files</h2>
<p><i>/etc/reposd.conf</i></p>
<dl>
<dd>This file contains the daemon configuration settings. See <code><a href="/docs/linux/man/5-reposd-conf/">reposd.conf</a></code>(5) for more information.</dl>
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
<p><code>reposctl</code> is distributed under the terms of the Eclipse Public License (&quot;Agreement&quot;). Any use, reproduction or distribution of this program constitutes recipeients acceptance of the agreement. </p>
<p> You can obtain a current copy of the Eclipse Public License from <a rel="nofollow" href="http://www.opensource.org/licenses/eclipse-1.0.php">http://www.opensource.org/licenses/eclipse-1.0.php</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-reposd/">reposd</a></code>(8), <code><a href="/docs/linux/man/5-reposd-conf/">reposd.conf</a></code>(5), </p>
