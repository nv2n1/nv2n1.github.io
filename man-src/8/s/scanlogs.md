---
title: "scanlogs(8)"
name: "scanlogs"
section: "8"
letter: "s"
url: "/docs/linux/man/8-scanlogs/"
description: "scanlogs – Summarize and rotate INN log files"
---

<p>scanlogs &#8211; Summarize and rotate INN log files</p>
<h2>Synopsis</h2>
<p><code>scanlogs</code> [<code>norotate</code>]</p>
<h2>Description</h2>
<p><code>scanlogs</code> summarizes the information recorded in the <font SIZE="-1">INN</font> log files which reside in the <i>pathlog</i> directory set in <i>inn.conf</i> (see <i><a href="/docs/linux/man/5-newslog/">newslog</a></i>(5) for further details about these log files). It is normally invoked by the <i><a href="/docs/linux/man/8-news-daily/">news.daily</a></i>(8) script which performs daily server maintenance tasks. </p>
<p> It invokes <tt>&quot;ctlinnd flushlogs&quot;</tt> to close the news and error log files, rename them to add <tt>&quot;.old&quot;</tt> to the file names and open fresh news and error logs; the <i>active</i> file is also flushed to disk, along with the history database. </p>
<p> By default, <code>scanlogs</code> rotates and cleans out the logs. It keeps up to <i>logcycles</i> old compressed log files in <i>pathlog</i>/OLD (the <i>logcycles</i> parameter can be set in <i>inn.conf</i>). <code>scanlogs</code> also keeps archives of the <i>active</i> file in this directory. </p>
<p> It invokes <code>tally.control</code> if <i>newgroup.log</i> or <i>rmgroup.log</i> exists in <i>pathlog</i> (see the <i>control.log</i> entry of <i><a href="/docs/linux/man/5-newslog/">newslog</a></i>(5) for more information about that). </p>
<p> <code>scanlogs</code> displays the contents of <i>errlog</i> and <i>news.crit</i>, if non-empty, and runs <code>innreport</code> to summarize the contents of <i>news</i> and <i>news.notice</i>, and to update the <i>unwanted.log</i> file amongst other things (see more information about that in <i><a href="/docs/linux/man/8-innreport/">innreport</a></i>(8)).</p>
<h2>Options</h2>
<p>Only one option is currently accepted:</p>
<dl>
<dt><code>norotate</code></p>
<dd>Using this option disables the rotating and cleaning aspect of the log processing: the logs files are only scanned for information and no contents are altered. If <code>scanlogs</code> is invoked more than once a day, the <code>norotate</code> option should be used to prevent premature log cleaning.</dl>
<h2>Files</h2>
<p>See <i><a href="/docs/linux/man/5-newslog/">newslog</a></i>(5) for the list of log files processed by <code>scanlogs</code>.</p>
<h2>History</h2>
<p>Written by Landon Curt Noll &lt;chongo [at] toad.com&gt; and Rich <tt>$alz</tt> &lt;rsalz [at] uunet.uu.net&gt; for InterNetNews. Converted to <font SIZE="-1">POD</font> by Julien Elie. </p>
<p> <tt>$Id:</tt> scanlogs.pod 8357 2009-02-27 17:56:00Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5), <i><a href="/docs/linux/man/8-innreport/">innreport</a></i>(8), <i><a href="/docs/linux/man/8-news-daily/">news.daily</a></i>(8), <i><a href="/docs/linux/man/5-newslog/">newslog</a></i>(5), <i><a href="/docs/linux/man/1-shlock/">shlock</a></i>(1), <i><a href="/docs/linux/man/8-tally-control/">tally.control</a></i>(8). </p>
