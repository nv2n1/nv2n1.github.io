---
title: "amstatus(8)"
name: "amstatus"
section: "8"
letter: "a"
url: "/docs/linux/man/8-amstatus/"
description: "amstatus – display the state of an Amanda run"
---

<p>amstatus &#8211; display the state of an Amanda run</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>amstatus</code> [&#8211;file&nbsp;<wbr><i>amdumpfile</i>] [&#8211;summary] [&#8211;dumping] [&#8211;waitdumping] [&#8211;waittaper] [&#8211;dumpingtape] [&#8211;writingtape] [&#8211;finished] [&#8211;failed] [&#8211;estimate] [&#8211;gestimate] [&#8211;stats] [&#8211;locale-independent-date-format] [&#8211;config] <i>config</i></dl>
<h2>Description</h2>
<p><code>Amstatus</code></p>
<dd>gives the current state of the Amanda run specified by the <i>config</i> configuration. If there is no active Amanda running, it summarizes the result of the last run. It may also be used to summarize the results of a previous run. </p>
<p> See the <code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8) man page for more details about Amanda.</p>
<h2>Options</h2>
<p>All options may be abbreviated to the shortest non-ambiguous sub-string. If no options are given, everything is displayed. </p>
<p> <code>[&#8211;config] config</code></p>
<dl>
<dd>Specify the Amanda configuration you want to display the state for.</dl>
<p> <code>&#8211;file amdumpfile</code></p>
<dl>
<dd>Specify an alternate file instead of the <i>amdump</i> or <i>amflush</i> file.</dl>
<p> <code>&#8211;summary</code></p>
<dl>
<dd>Display a summary of the state of the run.</dl>
<p> <code>&#8211;dumping</code></p>
<dl>
<dd>Display all partitions that are dumping.</dl>
<p> <code>&#8211;waitdumping|wdumping</code></p>
<dl>
<dd>Display all partitions that are waiting to be dumped.</dl>
<p> <code>&#8211;waittaper|wtaper</code></p>
<dl>
<dd>Display all partitions dumped that are waiting to be written to tape.</dl>
<p> <code>&#8211;dumpingtape|dtape</code></p>
<dl>
<dd>Display all partitions that are dumping directly to tape.</dl>
<p> <code>&#8211;writingtape|wtape</code></p>
<dl>
<dd>Display all partitions that are writing to tape.</dl>
<p> <code>&#8211;finished</code></p>
<dl>
<dd>Display all partitions that are dumped and written to tape.</dl>
<p> <code>&#8211;failed|error</code></p>
<dl>
<dd>Display all partitions that failed.</dl>
<p> <code>&#8211;estimate</code></p>
<dl>
<dd>Display all partitions whose estimate is finished. Works only during the estimate phase.</dl>
<p> <code>&#8211;gestimate|gettingestimate</code></p>
<dl>
<dd>Display all partitions whose estimate is not finished. Works only during the estimate phase.</dl>
<p> <code>&#8211;stats|statistics</code></p>
<dl>
<dd>Display statistics about active-time of taper and dumpers.</dl>
<p> <code>&#8211;locale-independent-date-format</code></p>
<dl>
<dd>Output the date in a locale independent format. The format is the same executing: date +&#8217;%Y-%m-%d %H:%M:%S %Z&#8217;</dl>
<h2>Exit Code</h2>
<p>The exit code of <code>amstatus</code> is the ORed value of: </p>
<pre> 0 = success
 1 = error
 4 = a dle failed
 8 = Don't know the status of a dle (RESULT_MISSING in the report)
 16 = tape error or no more tape</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/8-amcheck/">amcheck</a></code>(8), <code><a href="/docs/linux/man/8-amdump/">amdump</a></code>(8), <code><a href="/docs/linux/man/8-amrestore/">amrestore</a></code>(8), <code><a href="/docs/linux/man/8-amadmin/">amadmin</a></code>(8) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Author</h2>
<p><code>Stefan G. Weichinger</code> &lt;sgw [at] amanda.org&gt;</p>
