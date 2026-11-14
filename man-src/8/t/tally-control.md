---
title: "tally-control(8)"
name: "tally-control"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tally-control/"
description: "tally.control – Keep track of newsgroup creations and deletions"
---

<p>tally.control &#8211; Keep track of newsgroup creations and deletions</p>
<h2>Synopsis</h2>
<p><code>tally.control</code> &lt; <i>logfile</i></p>
<h2>Description</h2>
<p><code>tally.control</code> is normally daily invoked by <code>scanlogs</code>. It reads its standard input, which should be the <i>newgroup.log</i> and <i>rmgroup.log</i> control log files. They contain a summary line describing the control message and the action taken by <code>controlchan</code>, followed by the article indented by four spaces, and a blank line. Then, <code>tally.control</code> updates the cumulative list of newsgroup creations and deletions which is kept in <i>control.log</i>. </p>
<p> All these log files reside in the <i>pathlog</i> directory set in <i>inn.conf</i>. In order to generate them, you need to enable control articles logging in <i><a href="/docs/linux/man/5-control-ctl/">control.ctl</a></i>(5), as explained in the <i>control.log</i> entry of <i><a href="/docs/linux/man/5-newslog/">newslog</a></i>(5).</p>
<h2>Files</h2>
<dl>
<dt><i>pathbin</i>/tally.control</p>
<dd>The Shell script itself used to tally newsgroup creations and deletions up.</p>
<dt><i>pathlog</i>/control.log</p>
<dd>This file maintains a count of the number of newgroup and rmgroup control messages seen for each newsgroup. The count is of the number of control messages with the indicated arguments, regardless if they were actually processed. All control arguments, including invalid ones, are counted. An example of lines which can be found in that log file is: </p>
<pre> 3 Control: newgroup foo.bar moderated
 3 Control: rmgroup misc.removed
 1 Control: newgroup misc.created</pre>
</dl>
<h2>History</h2>
<p>Written by Landon Curt Noll &lt;chongo [at] toad.com&gt; and Rich <tt>$alz</tt> &lt;rsalz [at] uunet.uu.net&gt; for InterNetNews. Rewritten and converted to <font SIZE="-1">POD</font> by Julien Elie. </p>
<p> <tt>$Id:</tt> tally.control.pod 8357 2009-02-27 17:56:00Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-control-ctl/">control.ctl</a></i>(5), <i><a href="/docs/linux/man/8-news-daily/">news.daily</a></i>(8), <i><a href="/docs/linux/man/5-newslog/">newslog</a></i>(5), <i><a href="/docs/linux/man/8-scanlogs/">scanlogs</a></i>(8). </p>
