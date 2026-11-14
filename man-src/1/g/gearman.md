---
title: "gearman(1)"
name: "gearman"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gearman/"
description: "gearman – Gearmand Documentation, http://gearman.info/"
---

<h2>NAME</h2>
<p> gearman &#8211; Gearmand Documentation, <a rel="nofollow" href="http://gearman.info/">http://gearman.info/</a> </p>
<p> Command line client for Gearmand</p>
<h2>SYNOPSIS</h2>
<p> <code>Common options</code></p>
<dl>
<dt><code>-f &lt;function&gt;</code></p>
<dd> Function name to use for jobs (can give many)</p>
<dt><code>-h &lt;host&gt;</code></p>
<dd> Job server host</p>
<dt><code>-H</code></p>
<dd> Print this help menu</p>
<dt><code>-p &lt;port&gt;</code></p>
<dd> Gearman server port</p>
<dt><code>-t &lt;timeout&gt;</code></p>
<dd> Timeout in milliseconds</p>
<dt><code>-i &lt;pidfile&gt;</code></p>
<dd> Create a pidfile for the process</p>
<dt><code>-n</code></p>
<dd> In client mode run one job per line, in worker mode send data packet for each line</p>
<dt><code>-N</code></p>
<dd> Same as -n, but strip off the newline </p>
<p> <code>Client options</code></p>
<dt><code>-b</code></p>
<dd> Run jobs in the background</p>
<dt><code>-I</code></p>
<dd> Run jobs as high priority</p>
<dt><code>-L</code></p>
<dd> Run jobs as low priority</p>
<dt><code>-P</code></p>
<dd> Prefix all output lines with functions names</p>
<dt><code>-s</code></p>
<dd> Send job without reading from standard input</p>
<dt><code>-u &lt;unique&gt;</code></p>
<dd> Unique key to use for job </p>
<p> <i>Worker options*</i></p>
<dt><code>-c &lt;count&gt;</code></p>
<dd> Number of jobs for worker to run before exiting</p>
<dt><code>-w</code></p>
<dd> Run in worker mode</dl>
<h2>DESCRIPTION</h2>
<p> With gearman you can run client and worker functions from the command line. </p>
<p> The environmental variable GEARMAN_SERVER can be used to specify multiple gearmand servers. Please see the c:func:&#8217;gearman_client_add_servers&#8217; for an explanation of the required syntax.</p>
<h2>HOME</h2>
<p> To find out more information please check: <i><a rel="nofollow" href="http://gearman.info/">http://gearman.info/</a></i></p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/8-gearmand/">gearmand</a>(8)</i> <i><a href="/docs/linux/man/3-libgearman/">libgearman</a>(3)</i></p>
<h2>AUTHOR</h2>
<p> Data Differential <a rel="nofollow" href="http://www.datadifferential.com/">http://www.datadifferential.com/</a></p>
<h2>COPYRIGHT</h2>
<p> 2011-2013, Data Differential, <a rel="nofollow" href="http://www.datadifferential.com/">http://www.datadifferential.com/</a> </p>
<h2>Index</h2>
