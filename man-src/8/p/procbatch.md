---
title: "procbatch(8)"
name: "procbatch"
section: "8"
letter: "p"
url: "/docs/linux/man/8-procbatch/"
description: "procbatch – Process an INN funnel file or innfeed-dropped file"
---

<p>procbatch &#8211; Process an INN funnel file or innfeed-dropped file</p>
<h2>Synopsis</h2>
<p><code>procbatch</code> [<code>-hquv</code>] [<code>-c</code> [<code>-s</code> <i>spooldir</i>]] [<code>-d</code> <i>outdir</i>] [<code>-e</code> <i>peer</i>] [<code>-m</code> [<code>-t</code> <i>backlogdir</i>]] <i>batchfile</i></p>
<h2>Description</h2>
<p><code>procbatch</code> will take an <font SIZE="-1">INN</font> funnel or <i>innfeed-dropped</i> file and split it up by host for direct processing with <code>innfeed</code> or <code>innxmit</code>. </p>
<p> While funnel files will normally only be of interest after a crash, <code>innfeed</code> may drop articles for a variety of reasons, not all of which indicate a fundamental problem. For example, <code>innfeed</code> may drop articles when started and stopped in quick succession while <font SIZE="-1">INN</font> processes a large number of control messages (a temporary indisposition), or when <font SIZE="-1">INN</font> feeds it articles for a site that isn&#8217;t in <i>innfeed.conf</i> (a misconfiguration). </p>
<p> Every running <code>innfeed</code> opens a file named <i>innfeed-dropped.&lt;id&gt;</i>, which should normally always be zero length and deleted on exit. If there are non-zero length files, <code>innfeed</code> has dropped some articles, and those dropped article files have to be processed or those articles will never be sent to peers. Though <code>news.daily</code> automatically process these files (invoking <code>procbatch</code>), it is also possible to do that manually. First make sure that the file doesn&#8217;t correspond to a currently running <code>innfeed</code>, for example by calling <tt>&quot;ctlinnd flush innfeed!&quot;</tt>. </p>
<p> An <font SIZE="-1">INN</font> funnel file, or an <i>innfeed-dropped</i> file, will usually be of the format: </p>
<pre> pathname message-id peer1 peer2 peer3 ...</pre>
<p>where <i>pathname</i> can alternatively be a storage <font SIZE="-1">API</font> token. </p>
<p> <code>procbatch</code> will break this file up into files named <i>peer1.tmp</i>, <i>peer2.tmp</i>, <i>peer3.tmp</i>, etc. of the format: </p>
<pre> pathname message-id</pre>
<p>These tape files will be sorted and stripped of duplicate entries. Simply renaming them to <i>peer1</i>, <i>peer2</i>, <i>peer3</i>, etc. in a running <code>innfeed</code>&#8216;s backlog directory will cause them to be picked up automatically by <code>innfeed</code> every <i>backlog-newfile-period</i> seconds (as set in in <i>innfeed.conf</i>). Use the <code>-m</code> flag to have <code>procbatch</code> rename and move them into place automatically. </p>
<p> After running <code>procbatch</code>, you may want to make sure that every generated backlog file has a corresponding <tt>&quot;.lock&quot;</tt> file. Otherwise, <code>innfeed</code> doesn&#8217;t have that site configured as a peer, meaning your <i>innfeed.conf</i> may need fixing.</p>
<h2>Options</h2>
<dl>
<dt><code>-c</code></p>
<dd>Check for the existence of an article before writing references to it to the tape files. Currently, this option can only be used with a tradspool article store. Using it with any other spool format will lead to all articles being dropped.</p>
<dt><code>-d</code> <i>outdir</i></p>
<dd>Put the output file(s) into the directory <i>outdir</i> (defaults to <i>pathtmp</i> as set in <i>inn.conf</i>). When also specifying <code>-m</code>, the temporary output files will still be put here before being moved into their final location.</p>
<dt><code>-e</code> <i>peer</i></p>
<dd>Only process entries for <i>peer</i>.</p>
<dt><code>-h</code></p>
<dd>Display a short help screen.</p>
<dt><code>-m</code></p>
<dd>Directly append to tape files in <code>innfeed</code>&#8216;s backlog directory.</p>
<dt><code>-q</code></p>
<dd>Quiet mode: only display error messages.</p>
<dt><code>-s</code> <i>spooldir</i></p>
<dd>Use <i>spooldir</i> as the location of the article spool (defaults to <i>patharticles</i> as set in <i>inn.conf</i>). This option has an effect only on a tradspool storage system when also specifying <code>-c</code>.</p>
<dt><code>-t</code> <i>backlogdir</i></p>
<dd>Use <i>backlogdir</i> as the location of the <code>innfeed</code> backlog directory (the directory where the created tape files will be put). Defaults to <i>pathspool</i>/innfeed. This option has an effect only when also specifying <code>-m</code>.</p>
<dt><code>-u</code></p>
<dd>Unlink the input batchfile after processing.</p>
<dt><code>-v</code></p>
<dd>Add verbosity.</dl>
<h2>Examples</h2>
<p>Take the file <i>innfeed-dropped.B012345</i>, process its lines appending to tapefiles in <code>innfeed</code>&#8216;s backlog directory, and remove it when done. Be verbose while doing so: </p>
<pre> procbatch -umv innfeed-dropped.B012345</pre>
<p>Go through <i>innfeed-dropped.B012345</i> saving entries for <tt>&quot;peer1&quot;</tt> in <i>/tmp/peer1.tmp</i>, but only if the articles are still available in the local tradspool: </p>
<pre> procbatch -e peer1 -d /tmp -c innfeed-dropped.B012345</pre>
<h2>Bugs</h2>
<p><code>procbatch</code> should be able to check for the existence of articles with any kind of article store, possibly using <code>grephistory</code>.</p>
<h2>History</h2>
<p><code>procbatch</code> was written by James Brister and improved for speed by Clayton O&#8217;Neill. </p>
<p> This manual page was written by Florian Schlichting, with the help of a memo by Russ Allbery. </p>
<p> <tt>$Id:</tt> procbatch.pod 9372 2011-09-04 09:22:23Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-filechan/">filechan</a></i>(8), <i><a href="/docs/linux/man/8-innfeed/">innfeed</a></i>(8), <i><a href="/docs/linux/man/8-innxmit/">innxmit</a></i>(8), <i><a href="/docs/linux/man/8-news-daily/">news.daily</a></i>(8). </p>
