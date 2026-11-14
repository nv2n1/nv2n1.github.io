---
title: "reposdump(1)"
name: "reposdump"
section: "1"
letter: "r"
url: "/docs/linux/man/1-reposdump/"
description: "reposdump – utility for dumping SBLIM Data Gatherer online metric repository"
---

<h2 class="name">NAME</h2>
<p> reposdump &#8211; utility for dumping SBLIM Data Gatherer online metric repository </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>reposdump</code> [<i>age</i>] [<i>interval</i>] [<i>directory</i>]</dl>
<h2>DESCRIPTION</h2>
<dd>The <code>reposdump</code> program is used to dump the metrics from the <code><a href="/docs/linux/man/8-reposd/">reposd</a></code>(8) daemons online repository. The metric data is exported into a flat text file. The file contains sections seperated by lines with the following format. </p>
<dl>
<dt>
<dd>
<pre>
===metricdefs &lt;pluginname&gt;===
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
===metricvals &lt;pluginname&gt;===
</pre>
</dl>
<p> Each section contains a list of comma seperated records containing the defined metric or metric values. A sample perl script /usr/share/reposd2csv.pl is included which demonstrates converting the dump data into a comma seperated value list (CSV) suitable for import into a spreadsheet.</p>
<h2>OPTIONS</h2>
<p> <i>age</i></p>
<dl>
<dt>
<dd> Maximum sample age in seconds to be dumped.</dl>
<p> <i>interval</i></p>
<dl>
<dt>
<dd> Sample interval granularity in seconds to be dumped.</dl>
<p> <i>directory</i></p>
<dl>
<dt>
<dd> Directory in which to dump metric file.</dl>
<h2>BUGS</h2>
<p> The SBLIM project maintains a mailing list to which you should direct all questions regarding sfcb, sfcc, wbemcli, the metric data gatherer, or any of the SBLIM providers. To subscribe to this list visit: </p>
<dl>
<dt>
<dd>
<pre>
<a rel="nofollow" href="https://lists.sourceforge.net/lists/listinfo/sblim-issues">https://lists.sourceforge.net/lists/listinfo/sblim-issues</a>
</pre>
</dl>
<p> Please report bugs you discover to the bug tracker. The SBLIM project bug tracking page can be found at: </p>
<dl>
<dt>
<dd>
<pre>
<a rel="nofollow" href="https://sourceforge.net/tracker/?group_id=128809">https://sourceforge.net/tracker/?group_id=128809</a>&amp;atid=712784
</pre>
</dl>
<h2>AUTHORS</h2>
<p> Please refer to the AUTHORS file distributed with sblim-gather.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2003-2012 IBM Corp.</p>
<h2>LICENSE</h2>
<p> <code>reposdump</code> is distributed under the terms of the Eclipse Public License (&quot;Agreement&quot;). Any use, reproduction or distribution of this program constitutes recipeients acceptance of the agreement. </p>
<p> You can obtain a current copy of the Eclipse Public License from <a rel="nofollow" href="http://www.opensource.org/licenses/eclipse-1.0.php">http://www.opensource.org/licenses/eclipse-1.0.php</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-reposd/">reposd</a></code>(8) </p>
<h2>Index</h2>
