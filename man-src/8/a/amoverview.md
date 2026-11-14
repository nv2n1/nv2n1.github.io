---
title: "amoverview(8)"
name: "amoverview"
section: "8"
letter: "a"
url: "/docs/linux/man/8-amoverview/"
description: "amoverview – display file systems processed by Amanda over time"
---

<p>amoverview &#8211; display file systems processed by Amanda over time</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>amoverview</code> [&#8211;hostwidth&nbsp;<wbr><i>width</i>] [&#8211;diskwidth&nbsp;<wbr><i>width</i>] [&#8211;skipmissed] [&#8211;last] [&#8211;num0] [&#8211;togo0] [&#8211;verbose] [&#8211;config&nbsp;<wbr>]&nbsp;<wbr><i>config</i></dl>
<h2>Description</h2>
<p><code>Amoverview</code></p>
<dd>displays a chart showing hosts and file systems processed by Amanda along with the backup level performed each day. </p>
<p> See the <code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8) man page for more details about Amanda.</p>
<h2>Options</h2>
<p><code>&#8211;config</code> <i>config</i></p>
<dl>
<dd>Use configuration <i>config</i>.</dl>
<p> <code>&#8211;hostwidth</code> <i>width</i></p>
<dl>
<dd>Set <code>host</code> field column width to <i>width</i> characters instead of 8.</dl>
<p> <code>&#8211;diskwidth</code> <i>width</i></p>
<dl>
<dd>Set <code>disk</code> field column width to <i>width</i> characters instead of 20.</dl>
<p> <code>&#8211;skipmissed</code></p>
<dl>
<dd>Compacts the output by only printing stats for the days Amanda actually ran.</dl>
<p> <code>&#8211;last</code></p>
<dl>
<dd>Outputs the last status of each disk at the start. Useful for long tapecycles and/or sparse reports.</dl>
<p> <code>&#8211;num0</code></p>
<dl>
<dd>Outputs the number of level 0 dumps for each disk.</dl>
<p> <code>&#8211;togo0</code></p>
<dl>
<dd>Outputs the number of runs until the last level 0 dump is overwritten.</dl>
<p> <code>&#8211;verbose</code></p>
<dl>
<dd><code>Amoverview</code> can take a long while on large systems. This option reports intermediate steps while it is working.</dl>
<h2>Results</h2>
<p><code>amoverview</code> is a summary of the output of &quot; <code>amadmin &lt;config&gt; find</code> &quot;. When the last column of <code>amadmin find</code> contains anything other than &quot;OK&quot;, amoverview translates this into &quot;E&quot; for that day. </p>
<p> A number indicates the level of backup and it succeeded. An &quot;E&quot; indicates an error for that day. You get an &quot;E&quot; for all errors, like failed to connect, datatimeout, computer crashed, etc, but also for failing to write to tape. </p>
<p> You can have an &quot;E&quot; followed by a number if a filesystem ran into end-of-tape once (gives an &quot;E&quot;, and later that day, you flush it to a second tape (a number: the level, indicating success). If the flush failed too, you get a double &quot;EE&quot; for that day. </p>
<p> You can also have a double code if you have two tapes in the changer and Amanda failed to write to tape the first time because it hit end of tape (resulting in &quot;E0&quot;, for a full, &quot;E1&quot; for an incremental etc.) or twice with error (&quot;EE&quot;), and may a successful flush afterwards giving maybe &quot;EE0&quot;. (Only the latest 2 characters are printed).</p>
<h2>Example</h2>
<p>This shows the /home file system on <i>host2</i> was backed up at level 3 on the 8th, 9th and 10th of December, had a full backup on the 11th, a level 1 on the 12th and a level 2 on the 13th. </p>
<pre># amoverview
 date 12 12 12 12 12 12
host disk 08 09 10 11 12 13
 
host1 / 0 1 1 1 1 1
host1 /var 0 1 1 1 1 1
host2 / 1 1 1 1 1 0
host2 /home 3 3 3 0 1 2
host2 /opt 1 1 1 1 1 1
host2 /var 1 1 0 1 1 1 </pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/8-amadmin/">amadmin</a></code>(8) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Author</h2>
<p><code>Stefan G. Weichinger</code> &lt;sgw [at] amanda.org&gt;</p>
