---
title: "glite-lb-mon-db(1)"
name: "glite-lb-mon-db"
section: "1"
letter: "g"
url: "/docs/linux/man/1-glite-lb-mon-db/"
description: "glite-lb-mon-db – program for monitoring the number of jobs in the LB system"
---

<h2 class="name">NAME</h2>
<p> glite-lb-mon-db &#8211; program for monitoring the number of jobs in the LB system</p>
<h2>SYNOPSIS</h2>
<p> <code>glite-lb-mon-db</code> <code>[-m dbstring -d -v -h]</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>glite-lb-mon-db</code> is a low-level program for monitoring the the number of jobs in the LB system. Using the LB internals, it connects directly to the underlying MySQL database and reads the number of jobs in each state. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-m dbstring, &#8211;mysql=dbstring</code></p>
<dd> Use non-default database connection string. </p>
<dt><code>-d, &#8211;debug</code></p>
<dd> Print debug info (if any). </p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Be verbose. </p>
<dt><code>-h, &#8211;help</code></p>
<dd> Display help and exit. </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>glite-lb-mon-db</code></p>
<dd> this is the default usage</p>
<dt><code>glite-lb-mon-db</code><i>&nbsp;<wbr>-m</i><code>&nbsp;<wbr>lbserver/@localhost:lbproxy</code></p>
<dd> use this dbstring to query the LB Proxy database. WARNING: the data in the LB Proxy may be incomplete! </p>
</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>MYSQL_UNIX_PORT</code></p>
<dd> set this environment variable to specify the path to the non-default MySQL socket path</p>
<dt><code>LBDB</code></p>
<dd> you can set this environment variable as an alternative to specify the non-default database connection string </p>
</dl>
<h2>BUGS</h2>
<p> Please report all bugs to CESNET gLite L&amp;B issue tracker available at <i><a rel="nofollow" href="https://github.com/CESNET/glite-lb/issues">https://github.com/CESNET/glite-lb/issues</a></i> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-glite-lb-mon/">glite-lb-mon</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> EU EGEE JRA1, CESNET group. </p>
<h2>Index</h2>
