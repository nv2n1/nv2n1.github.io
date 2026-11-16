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
<dt><code>-f &lt;function&gt;</code></dt>
<dd> Function name to use for jobs (can give many)</dd>
<dt><code>-h &lt;host&gt;</code></dt>
<dd> Job server host</dd>
<dt><code>-H</code></dt>
<dd> Print this help menu</dd>
<dt><code>-p &lt;port&gt;</code></dt>
<dd> Gearman server port</dd>
<dt><code>-t &lt;timeout&gt;</code></dt>
<dd> Timeout in milliseconds</dd>
<dt><code>-i &lt;pidfile&gt;</code></dt>
<dd> Create a pidfile for the process</dd>
<dt><code>-n</code></dt>
<dd> In client mode run one job per line, in worker mode send data packet for each line</dd>
<dt><code>-N</code></dt>
<dd> Same as -n, but strip off the newline </dd>
<p> <code>Client options</code></p>
<dt><code>-b</code></dt>
<dd> Run jobs in the background</dd>
<dt><code>-I</code></dt>
<dd> Run jobs as high priority</dd>
<dt><code>-L</code></dt>
<dd> Run jobs as low priority</dd>
<dt><code>-P</code></dt>
<dd> Prefix all output lines with functions names</dd>
<dt><code>-s</code></dt>
<dd> Send job without reading from standard input</dd>
<dt><code>-u &lt;unique&gt;</code></dt>
<dd> Unique key to use for job </dd>
<p> <i>Worker options*</i></p>
<dt><code>-c &lt;count&gt;</code></dt>
<dd> Number of jobs for worker to run before exiting</dd>
<dt><code>-w</code></dt>
<dd> Run in worker mode</dd></dl>
<h2>DESCRIPTION</h2>
<p> With gearman you can run client and worker functions from the command line. </p>
<p> The environmental variable GEARMAN_SERVER can be used to specify multiple gearmand servers. Please see the c:func:&#8217;gearman_client_add_servers&#8217; for an explanation of the required syntax.</p>
<h2>HOME</h2>
<p> To find out more information please check: <i><a rel="nofollow" href="http://gearman.info/">http://gearman.info/</a></i></p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/8-gearmand/">gearmand</a>(8)</i> <i>libgearman(3)</i></p>
<h2>AUTHOR</h2>
<p> Data Differential <a rel="nofollow" href="http://www.datadifferential.com/">http://www.datadifferential.com/</a></p>
<h2>COPYRIGHT</h2>
<p> 2011-2013, Data Differential, <a rel="nofollow" href="http://www.datadifferential.com/">http://www.datadifferential.com/</a> </p>
<h2>Index</h2>
