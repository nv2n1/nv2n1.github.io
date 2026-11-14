---
title: "cnfsstat(8)"
name: "cnfsstat"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cnfsstat/"
description: "cnfsstat – Show usage of CNFS buffers"
---

<p>cnfsstat &#8211; Show usage of CNFS buffers</p>
<h2>Synopsis</h2>
<p><code>cnfsstat</code> [<code>-ahpPsv</code>] [<code>-c</code> <i>class</i>] [<code>-i</code> <i>seconds</i>] [<code>-l</code> [<i>seconds</i>]] [<code>-m</code> <i>buffer</i>]</p>
<h2>Description</h2>
<p><code>cnfsstat</code> reads <i>pathetc</i>/cycbuff.conf and <i>pathetc</i>/storage.conf to determine which <font SIZE="-1">CNFS</font> buffers are available. It then reads the specified cyclic buffers and shows their usage status. <code>cnfsstat</code> can be invoked from <code>rc.news</code> if <i>docnfsstat</i> is set to true in <i>inn.conf</i>, and the result is written to <i><a href="/docs/linux/man/3-syslog/">syslog</a></i>(3).</p>
<h2>Options</h2>
<dl>
<dt><code>-a</code></p>
<dd>Besides its usual output, <code>cnfsstat</code> prints the age of the oldest article in the cycbuff. You may also want to use the <code>-v</code> flag to see extended consistency checks.</p>
<dt><code>-c</code> <i>class</i></p>
<dd>Only information for the specified class is printed.</p>
<dt><code>-h</code></p>
<dd>Print usage information and exit.</p>
<dt><code>-i</code> <i>seconds</i></p>
<dd>With this option, <code>cnfsstat</code> has an initial sleep of <i>seconds</i> seconds at startup. This is useful when <code>cnfsstat</code> is started at the same time as <font SIZE="-1">INN</font>, so that it can wait a little before beginning performing its checks.</p>
<dt><code>-l</code> [<i>seconds</i>]</p>
<dd>With this option, <code>cnfsstat</code> prints a status snapshot every <i>seconds</i> seconds, and only exits if an error occurs. When unspecified, the default interval is <tt>600</tt> seconds. </p>
<p> At each iteration, <code>cnfsstat</code> checks whether the <i>cycbuff.conf</i> and <i>storage.conf</i> files have been modified, and loads the new configuration if needed.</p>
<dt><code>-m</code> <i>buffer</i></p>
<dd>Print information about the specified buffer in a format suitable for <font SIZE="-1">MRTG</font>.</p>
<dt><code>-p</code></p>
<dd>Print an <font SIZE="-1">MRTG</font> config file.</p>
<dt><code>-P</code></p>
<dd>Write <font SIZE="-1">PID</font> into <i>pathrun</i>/cnfsstat.pid.</p>
<dt><code>-s</code></p>
<dd>Write output to <i><a href="/docs/linux/man/3-syslog/">syslog</a></i>(3) instead of standard output.</p>
<dt><code>-v</code></p>
<dd>Write additional information, especially about consistency checks for article storage and the <i>history</i> file.</dl>
<h2>History</h2>
<p>Written by Katsuhiro Kondou &lt;kondou [at] nec.co.jp&gt; for InterNetNews. Converted to <font SIZE="-1">POD</font> by Julien Elie. </p>
<p> <tt>$Id:</tt> cnfsstat.pod 9725 2014-09-24 18:01:11Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-cycbuff-conf/">cycbuff.conf</a></i>(5), <i><a href="/docs/linux/man/5-history/">history</a></i>(5), <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5), <i><a href="/docs/linux/man/8-rc-news/">rc.news</a></i>(8), <i><a href="/docs/linux/man/5-storage-conf/">storage.conf</a></i>(5). </p>
