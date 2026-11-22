---

title: "newsx-newsq(1)"
name: "newsx-newsq"
section: "1"
letter: "n"
url: "/docs/linux/man/1-newsx-newsq/"
description: "newsq – list news server outgoing queue"
---

<p> newsq &#8211; list news server outgoing queue </p>
<h2>SYNOPSIS</h2>
<p> <code>newsq</code> [ <i>options</i> ] [ <i>hostname&#8230;</i> ] </p>
<h2>DESCRIPTION</h2>
<p> Unless options dictate otherwise, <code>newsq</code> lists the current outgoing queue for the specified hosts. If no name is given, the queues of all external news hosts are shown. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></dt>
<dd> List all entries, also those without any outgoing messages.</dd>
<dt><code>&#8211;batch</code><i> batchdir</i></dt>
<dd> Use <i>batchdir</i> as the outgoing news article spool directory instead of the default .</dd>
<dt><code>&#8211;cnews</code></dt>
<dd> Set to C News mode.</dd>
<dt><code>-c</code></dt>
<dd> Continuously lists state of currently active newsx processes.</dd>
<dt><code>&#8211;inn</code></dt>
<dd> Set to INN mode.</dd>
<dt><code>-n</code></dt>
<dd> Show the size of the outgoing quene.</dd>
<dt><code>-q</code></dt>
<dd> Quiet operation, useful for getting outgoing queue empty vs. non-empty status.</dd>
<dt><code>-s</code></dt>
<dd> List state of currently active newsx processes.</dd>
<dt><code>-w</code><i> secs</i></dt>
<dd> Continuously lists state, pause <i>secs</i> seconds between displays. </dd>
</dl>
<h2>DIAGNOSTICS</h2>
<p> newsq returns error codes as follows:</p>
<dl>
<dt>
</dt><dd> 0 &#8211; Successful completion<br/>
 1 &#8211; Outgoing queue is empty<br/>
 2 &#8211; Incorrect arguments supplied.</dd></dl>
<h2>BUGS</h2>
<p> Report any bugs to <a rel="nofollow" href="http://www.kvaleberg.com/bug/">http://www.kvaleberg.com/bug/</a> </p>
<h2>FILES</h2>
<p> For C News:</p>
<dl>
<dt>/var/spool/news/outgoing/<i>spoolname</i>/togo</dt>
<dd> Spool file </dd>
</dl>
<h2>AUTHOR</h2>
<p> Egil Kvaleberg &lt;egil [at] kvaleberg.no&gt; </p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/8-newsx/">newsx</a></i>(8) </p>
