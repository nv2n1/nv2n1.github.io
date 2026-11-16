---
title: "salt-master(1)"
name: "salt-master"
section: "1"
letter: "s"
url: "/docs/linux/man/1-salt-master/"
description: "salt-master – salt-master Documentation"
---

<h2>NAME</h2>
<p> salt-master &#8211; salt-master Documentation </p>
<p> The Salt master daemon, used to control the Salt minions</p>
<h2>SYNOPSIS</h2>
<pre>
salt-master [ options ]
</pre>
<h2>DESCRIPTION</h2>
<p> The master daemon controls the Salt minions</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></dt>
<dd> Print the version of Salt that is running.</dd>
<dt><code>&#8211;versions-report</code></dt>
<dd> Show program&#8217;s dependencies and version number, and then exit</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> Show the help message and exit</dd>
<dt><code>-c CONFIG_DIR, &#8211;config-dir=CONFIG_dir</code></dt>
<dd> The location of the Salt configuration directory. This directory contains the configuration files for Salt master and minions. The default location on most systems is <code>/etc/salt</code>.</dd>
<dt><code>-u USER, &#8211;user=USER</code></dt>
<dd> Specify user to run salt-master</dd>
<dt><code>-d, &#8211;daemon</code></dt>
<dd> Run salt-master as a daemon</dd>
<dt><code>&#8211;pid-file PIDFILE</code></dt>
<dd> Specify the location of the pidfile. Default: /var/run/salt-master.pid</dd></dl>
<h3>Logging Options</h3>
<p> Logging options which override any settings defined on the configuration files.</p>
<dl>
<dt><code>-l LOG_LEVEL, &#8211;log-level=LOG_LEVEL</code></dt>
<dd> Console logging log level. One of <code>all</code>, <code>garbage</code>, <code>trace</code>, <code>debug</code>, <code>info</code>, <code>warning</code>, <code>error</code>, <code>quiet</code>. Default: <code>warning</code>.</dd>
<dt><code>&#8211;log-file=LOG_FILE</code></dt>
<dd> Log file path. Default: /var/log/salt/master.</dd>
<dt><code>&#8211;log-file-level=LOG_LEVEL_LOGFILE</code></dt>
<dd> Logfile logging log level. One of <code>all</code>, <code>garbage</code>, <code>trace</code>, <code>debug</code>, <code>info</code>, <code>warning</code>, <code>error</code>, <code>quiet</code>. Default: <code>warning</code>.</dd></dl>
<h2>SEE ALSO</h2>
<p> <i>salt(1)</i> <i><a href="/docs/linux/man/7-salt/">salt</a>(7)</i> <i><a href="/docs/linux/man/1-salt-minion/">salt-minion</a>(1)</i></p>
<h2>AUTHOR</h2>
<p> Thomas S. Hatch &lt;thatch45 [at] gmail.com&gt; and many others, please see the Authors file</p>
<h2>COPYRIGHT</h2>
<p> 2016 SaltStack, Inc. </p>
<h2>Index</h2>
