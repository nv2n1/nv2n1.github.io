---
title: "collectdmon(1)"
name: "collectdmon"
section: "1"
letter: "c"
url: "/docs/linux/man/1-collectdmon/"
description: "collectdmon – Monitoring daemon for collectd"
---

<h2 class="name">NAME</h2>
<p> collectdmon &#8211; Monitoring daemon for collectd </p>
<h2>SYNOPSIS</h2>
<p> collectdmon <i>[options]</i> [&#8211; <i>collectd options</i>]</p>
<h2>DESCRIPTION</h2>
<p> collectdmon is a small &#8220;wrapper&#8221; daemon which starts and monitors the collectd daemon. If collectd terminates it will automatically be restarted, unless collectdmon was told to shut it down.</p>
<h2>OPTIONS</h2>
<p> collectdmon supports the following options:</p>
<dl>
<dt><code>-c</code> <i>&lt;path&gt;</i></p>
<dd> Specify the pathname of the collectd binary. You may either specify an absolute path or simply the name of the binary in which case the <font SIZE="-1"><code>PATH</code></font> variable will be searched for it. The default is &quot;<code>collectd</code>&quot;.</p>
<dt><code>-P</code> <i>&lt;pid-file&gt;</i></p>
<dd> Specify the pid file. The default is &quot;<i>/var/run/collectdmon.pid</i>&quot;.</p>
<dt><code>-h</code></p>
<dd> Output usage information and exit.</p>
<dt><i>collectd options</i></p>
<dd> Specify options that are passed on to collectd. If it is not already included, <code>-f</code> will be added to these options. See <i><a href="/docs/linux/man/1-collectd/">collectd</a></i>(1).</dl>
<h2>SIGNALS</h2>
<p> <code>collectdmon</code> accepts the following signals:</p>
<dl>
<dt><font SIZE="-1"><code>SIGINT</code></font>, <font SIZE="-1"><code>SIGTERM</code></font></p>
<dd> These signals cause <code>collectdmon</code> to terminate <code>collectd</code>, wait for its termination and then shut down.</p>
<dt><font SIZE="-1"><code>SIGHUP</code></font></p>
<dd> This signal causes <code>collectdmon</code> to terminate <code>collectd</code>, wait for its termination and then restart it.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-collectd/">collectd</a></i>(1), <i><a href="/docs/linux/man/5-collectd-conf/">collectd.conf</a></i>(5), &lt;<a rel="nofollow" href="http://collectd.org/">http://collectd.org/</a>&gt;</p>
<h2>AUTHOR</h2>
<p> collectd has been written by Florian Forster &lt;octo at collectd.org&gt; and many contributors (see `<font SIZE="-1">AUTHORS</font>&#8216;). </p>
<p> collectdmon has been written by Sebastian Harl &lt;sh [at] tokkee.org&gt;. </p>
<h2>Index</h2>
