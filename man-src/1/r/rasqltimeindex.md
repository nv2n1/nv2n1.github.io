---
title: "rasqltimeindex(1)"
name: "rasqltimeindex"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rasqltimeindex/"
description: "rasqltimeindex – read argus(8) data from mysql database."
---

<h2>NAME</h2>
<p> <code>rasqltimeindex</code> &#8211; read <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data from mysql database.</p>
<h2>SYNOPSIS</h2>
<p> <code>rasqltimeindex -r argus.data.file -w <a href="mysql://user@host/db">mysql://user@host/db</a></code></p>
<h2>DESCRIPTION</h2>
<p> <code>Rasqltimeindex</code> index <code>argus</code> data files by time. </p>
<p> The principal function of rasqltimeindex is to provide fast access to indexed argus data files based on time. </p>
<p> Rasqltimeindex, like all ra based clients, supports a number of <code>ra options</code> <code><a href="/docs/linux/man/1-rasqltimeindex/">rasqltimeindex</a>(1)</code> specific options are: </p>
<h2>RASQLTIMEINDEX SPECIFIC OPTIONS</h2>
<dl>
<dt><code>-w &lt;<a href="mysql://[user[:pass]@]host[:port]/db">mysql://[user[:pass]@]host[:port]/db</a>&gt;</code></p>
<dd> Specify the mysql database to use in maintaining the &#8216;Seconds&#8217;, &#8216;Probe&#8217;, and &#8216;Filename&#8217; database index tables. </p>
</dl>
<h2>INVOCATION</h2>
<p> This invocation reads <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data from the <i>file</i> argus.file and creates an index of every second in the file in the <i>db</i> database, using the <i>user</i> database account. </p>
<pre>
 
   <code>rasqltimeindex</code> -r argus.file -w <a href="mysql://user@localhost/db">mysql://user@localhost/db</a>
 
</pre>
<p> To take advantage of the speedup provided by the time indexing, use <code>rasql</code> to read the mysql database, with a time filter. This example will read from the database that contains the &#8216;Seconds&#8217;, &#8216;Probe&#8217;, and &#8216;Filename&#8217; database index tables, and search for all flow records from 00:00:00 &#8211; 00:00:25, 20 days ago. </p>
<pre>
   <code>rasql</code> -r <a href="mysql://user@localhost/db">mysql://user@localhost/db</a> -t -20d+25s
</pre>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2000-2016 QoSient. All rights reserved. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ra/">ra</a>(1),</code> <code><a href="/docs/linux/man/1-rasql/">rasql</a>(1),</code> <code><a href="/docs/linux/man/5-rarc/">rarc</a>(5),</code> <code><a href="/docs/linux/man/8-argus/">argus</a>(8),</code> </p>
<h2>AUTHORS</h2>
<pre>
Carter Bullard (carter [at] qosient.com).
</pre>
<h2>Index</h2>
