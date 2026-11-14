---
title: "rasql(1)"
name: "rasql"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rasql/"
description: "rasql – read argus(8) data from mysql database."
---

<h2>NAME</h2>
<p> <code>rasql</code> &#8211; read <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data from mysql database.</p>
<h2>SYNOPSIS</h2>
<p> <code>rasql</code> [<code>-M</code> <i>sql=&#8217;where clause&#8217;</i>] -r <a href="mysql://user@host/db/table">mysql://user@host/db/table</a> [<code>raoptions</code>] [<code>&#8212;</code> <i>filter-expression</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>Rasql</code> reads <code>argus</code> data from an argus-client generated mysql database. </p>
<p> The principal function of rasql is to extract the &#8216;record&#8217; binary blob that is inserted by <i>rasqlinsert.1</i> when adding argus data to a mysql table. </p>
<h2>RASQL SPECIFIC OPTIONS</h2>
<p> Rasql, like all ra based clients, supports a number of <code>ra options</code> including filtering of input argus records through a terminating filter expression. <code><a href="/docs/linux/man/1-rasql/">rasql</a>(1)</code> specific options are:</p>
<dl>
<dt><code>-M</code><i> sql=&#8217;where clause&#8217;</i></p>
<dd> This appends the &#8216;where clause&#8217; to the SELECT mysql database command. providing a means to use SQL select and join strategies when performing queries. </p>
</dl>
<h2>INVOCATION</h2>
<p> This invocation reads <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data from the <i>table</i> table that is contained in the <i>db</i> database, using the <i>user</i> database account, and instructs MySQL to select records where the database attribute &#8216;saddr&#8217; equals to the string &#8216;2.3.4.5&#8217;. </p>
<pre>
 
   <code>rasql</code> -r <a href="mysql://user@localhost/db/table">mysql://user@localhost/db/table</a> -M sql=&quot;saddr='2.3.4.5'&quot;
 
</pre>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2000-2016 QoSient. All rights reserved. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ra/">ra</a>(1),</code> <code><a href="/docs/linux/man/1-rasqlinsert/">rasqlinsert</a>(1),</code> <code><a href="/docs/linux/man/5-rarc/">rarc</a>(5),</code> <code><a href="/docs/linux/man/8-argus/">argus</a>(8),</code> </p>
<h2>AUTHORS</h2>
<pre>
Carter Bullard (carter [at] qosient.com).
</pre>
<h2>Index</h2>
