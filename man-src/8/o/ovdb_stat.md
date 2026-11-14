---
title: "ovdb_stat(8)"
name: "ovdb_stat"
section: "8"
letter: "o"
url: "/docs/linux/man/8-ovdb_stat/"
description: "ovdb_stat – Display information from the ovdb database"
---

<p>ovdb_stat &#8211; Display information from the ovdb database</p>
<h2>Synopsis</h2>
<p><code>ovdb_stat</code> <code>-Hgci</code> [<code>-r</code> <i>artnumrange</i>] newsgroup [newsgroup &#8230;] </p>
<p> <code>ovdb_stat</code> <code>-Hklmtv</code> [<code>-d</code> <i>database</i>]</p>
<h2>Description</h2>
<p><code>ovdb_stat</code> displays information from the ovdb database: Berkeley&nbsp;<wbr><font SIZE="-1">DB</font> statistics, newsgroup data, and overview records; and optionally outputs in <font SIZE="-1">HTML</font> format.</p>
<h2>Options</h2>
<dl>
<dt><code>-g</code></p>
<dd>Newsgroup himark, lowmark, article count, and flag for the given newsgroups (as stored in the ovdb &#8220;groupinfo&#8221; database) are displayed.</p>
<dt><code>-c</code></p>
<dd>Similar to <code>-g</code>, except the himark, lowmark, and count are calculated by actually scanning the overview records and counting them. This can be a lengthy operation on groups with lots of articles.</p>
<dt><code>-i</code></p>
<dd>Internal data regarding the given newsgroups are displayed.</p>
<dt><code>-r</code> <i>artnumrange</i></p>
<dd>Overview records are retrieved. The <i>artnumrange</i> parameter may be a single article number, or a range of articles in the format <tt>&quot;low-hi&quot;</tt>.</p>
<dt><code>-H</code></p>
<dd>Output is presented in <font SIZE="-1">HTML</font> format.</p>
<dt><code>-k</code></p>
<dd>Displays lock region statistics, as returned by the Berkeley&nbsp;<wbr><font SIZE="-1">DB</font> <i>lock_stat()</i> call.</p>
<dt><code>-l</code></p>
<dd>Displays log region statistics, as returned by the Berkeley&nbsp;<wbr><font SIZE="-1">DB</font> <i>log_stat()</i> call.</p>
<dt><code>-m</code></p>
<dd>Displays global memory pool statistics, as returned by the Berkeley&nbsp;<wbr><font SIZE="-1">DB</font> <i>memp_stat()</i> call.</p>
<dt><code>-M</code></p>
<dd>Same as <code>-m</code>, and also displays memory pool statistics for each database file.</p>
<dt><code>-t</code></p>
<dd>Displays log region statistics, as returned by the Berkeley&nbsp;<wbr><font SIZE="-1">DB</font> <i>txn_stat()</i> call.</p>
<dt><code>-v</code></p>
<dd>Displays ovdb version, and Berkeley&nbsp;<wbr><font SIZE="-1">DB</font> version.</p>
<dt><code>-d</code> <i>database</i></p>
<dd>Displays information about the given database, as returned by the Berkeley&nbsp;<wbr><font SIZE="-1">DB</font> db-&gt;<i>stat()</i> call. This operation may take a long time on busy systems (several minutes or more).</dl>
<h2>Warnings</h2>
<p>ovdb_stat may be safely killed with the <font SIZE="-1">INT</font>, <font SIZE="-1">TERM</font>, or <font SIZE="-1">HUP</font> signals. It catches those signals and exits cleanly. Do not kill ovdb_stat with other signals, unless absolutely necessary, because it may leave stale locks in the <font SIZE="-1">DB</font> environment.</p>
<h2>History</h2>
<p>Written by Heath Kehoe &lt;hakehoe [at] avalon.net&gt; for InterNetNews. </p>
<p> <tt>$Id:</tt> ovdb_stat.pod 9766 2014-12-07 21:08:08Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-ovdb/">ovdb</a></i>(5) </p>
