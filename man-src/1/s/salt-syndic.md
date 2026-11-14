---
title: "salt-syndic(1)"
name: "salt-syndic"
section: "1"
letter: "s"
url: "/docs/linux/man/1-salt-syndic/"
description: "salt-syndic – salt-syndic Documentation"
---

<h2>NAME</h2>
<p> salt-syndic &#8211; salt-syndic Documentation </p>
<p> The Salt syndic daemon, a special minion that passes through commands from a higher master</p>
<h2>SYNOPSIS</h2>
<pre>
salt-syndic [ options ]
</pre>
<h2>DESCRIPTION</h2>
<p> The Salt syndic daemon, a special minion that passes through commands from a higher master.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd> Print the version of Salt that is running.</p>
<dt><code>&#8211;versions-report</code></p>
<dd> Show program&#8217;s dependencies and version number, and then exit</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Show the help message and exit</p>
<dt><code>-c CONFIG_DIR, &#8211;config-dir=CONFIG_dir</code></p>
<dd> The location of the Salt configuration directory. This directory contains the configuration files for Salt master and minions. The default location on most systems is <code>/etc/salt</code>.</p>
<dt><code>-u USER, &#8211;user=USER</code></p>
<dd> Specify user to run salt-syndic</p>
<dt><code>-d, &#8211;daemon</code></p>
<dd> Run salt-syndic as a daemon</p>
<dt><code>&#8211;pid-file PIDFILE</code></p>
<dd> Specify the location of the pidfile. Default: /var/run/salt-syndic.pid</dl>
<h3>Logging Options</h3>
<p> Logging options which override any settings defined on the configuration files.</p>
<dl>
<dt><code>-l LOG_LEVEL, &#8211;log-level=LOG_LEVEL</code></p>
<dd> Console logging log level. One of <code>all</code>, <code>garbage</code>, <code>trace</code>, <code>debug</code>, <code>info</code>, <code>warning</code>, <code>error</code>, <code>quiet</code>. Default: <code>warning</code>.</p>
<dt><code>&#8211;log-file=LOG_FILE</code></p>
<dd> Log file path. Default: /var/log/salt/master.</p>
<dt><code>&#8211;log-file-level=LOG_LEVEL_LOGFILE</code></p>
<dd> Logfile logging log level. One of <code>all</code>, <code>garbage</code>, <code>trace</code>, <code>debug</code>, <code>info</code>, <code>warning</code>, <code>error</code>, <code>quiet</code>. Default: <code>warning</code>.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-salt/">salt</a>(1)</i> <i><a href="/docs/linux/man/1-salt-master/">salt-master</a>(1)</i> <i><a href="/docs/linux/man/1-salt-minion/">salt-minion</a>(1)</i></p>
<h2>AUTHOR</h2>
<p> Thomas S. Hatch &lt;thatch45 [at] gmail.com&gt; and many others, please see the Authors file</p>
<h2>COPYRIGHT</h2>
<p> 2016 SaltStack, Inc. </p>
<h2>Index</h2>
