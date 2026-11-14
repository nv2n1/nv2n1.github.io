---
title: "salt-cp(1)"
name: "salt-cp"
section: "1"
letter: "s"
url: "/docs/linux/man/1-salt-cp/"
description: "salt-cp – salt-cp Documentation"
---

<h2>NAME</h2>
<p> salt-cp &#8211; salt-cp Documentation </p>
<p> Copy a file to a set of systems</p>
<h2>SYNOPSIS</h2>
<pre><code>
salt - cp '*'[options] SOURCE DEST salt - cp - E '.*'[options] SOURCE DEST salt - cp - G 'os:Arch.*'[options] SOURCE DEST
</code></pre>
<h2>DESCRIPTION</h2>
<p> Salt copy copies a local file out to all of the Salt minions matched by the given target.</p>
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
<dt><code>-t TIMEOUT, &#8211;timeout=TIMEOUT</code></p>
<dd> The timeout in seconds to wait for replies from the Salt minions. The timeout number specifies how long the command line client will wait to query the minions and check on running jobs. Default: 5</dl>
<h3>Logging Options</h3>
<p> Logging options which override any settings defined on the configuration files.</p>
<dl>
<dt><code>-l LOG_LEVEL, &#8211;log-level=LOG_LEVEL</code></p>
<dd> Console logging log level. One of <code>all</code>, <code>garbage</code>, <code>trace</code>, <code>debug</code>, <code>info</code>, <code>warning</code>, <code>error</code>, <code>quiet</code>. Default: <code>warning</code>.</p>
<dt><code>&#8211;log-file=LOG_FILE</code></p>
<dd> Log file path. Default: /var/log/salt/master.</p>
<dt><code>&#8211;log-file-level=LOG_LEVEL_LOGFILE</code></p>
<dd> Logfile logging log level. One of <code>all</code>, <code>garbage</code>, <code>trace</code>, <code>debug</code>, <code>info</code>, <code>warning</code>, <code>error</code>, <code>quiet</code>. Default: <code>warning</code>.</dl>
<h3>Target Selection</h3>
<dl>
<dt><code>-E, &#8211;pcre</code></p>
<dd> The target expression will be interpreted as a PCRE regular expression rather than a shell glob.</p>
<dt><code>-L, &#8211;list</code></p>
<dd> The target expression will be interpreted as a comma-delimited list; example: server1.foo.bar,server2.foo.bar,example7.quo.qux</p>
<dt><code>-G, &#8211;grain</code></p>
<dd> The target expression matches values returned by the Salt grains system on the minions. The target expression is in the format of &#8216;&lt;grain value&gt;:&lt;glob expression&gt;&#8217;; example: &#8216;os:Arch*&#8217; </p>
<p> This was changed in version 0.9.8 to accept glob expressions instead of regular expression. To use regular expression matching with grains, use the &#8211;grain-pcre option.</p>
<dt><code>&#8211;grain-pcre</code></p>
<dd> The target expression matches values returned by the Salt grains system on the minions. The target expression is in the format of &#8216;&lt;grain value&gt;:&lt; regular expression&gt;&#8217;; example: &#8216;os:Arch.*&#8217;</p>
<dt><code>-N, &#8211;nodegroup</code></p>
<dd> Use a predefined compound target defined in the Salt master configuration file.</p>
<dt><code>-R, &#8211;range</code></p>
<dd> Instead of using shell globs to evaluate the target, use a range expression to identify targets. Range expressions look like %cluster. </p>
<p> Using the Range option requires that a range server is set up and the location of the range server is referenced in the master configuration file.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-salt/">salt</a>(1)</i> <i><a href="/docs/linux/man/1-salt-master/">salt-master</a>(1)</i> <i><a href="/docs/linux/man/1-salt-minion/">salt-minion</a>(1)</i></p>
<h2>AUTHOR</h2>
<p> Thomas S. Hatch &lt;thatch45 [at] gmail.com&gt; and many others, please see the Authors file</p>
<h2>COPYRIGHT</h2>
<p> 2016 SaltStack, Inc. </p>
<h2>Index</h2>
