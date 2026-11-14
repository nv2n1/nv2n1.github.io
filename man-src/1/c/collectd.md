---
title: "collectd(1)"
name: "collectd"
section: "1"
letter: "c"
url: "/docs/linux/man/1-collectd/"
description: "collectd – System statistics collection daemon"
---

<h2 class="name">NAME</h2>
<p> collectd &#8211; System statistics collection daemon </p>
<h2>SYNOPSIS</h2>
<p> collectd <i>[options]</i></p>
<h2>DESCRIPTION</h2>
<p> collectd is a daemon that receives system statistics and makes them available in a number of ways. The main daemon itself doesn&#8217;t have any real functionality apart from loading, querying and submitting to plugins. For a description of available plugins please see &#8220;<font SIZE="-1">PLUGINS&#8221;</font> below.</p>
<h2>OPTIONS</h2>
<p> Most of collectd&#8217;s configuration is done using using a configfile. See <i><a href="/docs/linux/man/5-collectd-conf/">collectd.conf</a></i>(5) for an in-depth description of all options.</p>
<dl>
<dt><code>-C</code> <i>&lt;config-file&gt;</i></p>
<dd> Specify an alternative config file. This is the place to go when you wish to change <code>collectd</code>&#8216;s behavior. The path may be relative to the current working directory.</p>
<dt><code>-t</code></p>
<dd> Test the configuration only. The program immediately exits after parsing the config file. A return code not equal to zero indicates an error.</p>
<dt><code>-T</code></p>
<dd> Test the plugin read callbacks only. The program immediately exits after invoking the read callbacks once. A return code not equal to zero indicates an error.</p>
<dt><code>-P</code> <i>&lt;pid-file&gt;</i></p>
<dd> Specify an alternative pid file. This overwrites any settings in the config file. This is thought for init-scripts that require the PID-file in a certain directory to work correctly. For everyday-usage use the <code>PIDFile</code> config-option.</p>
<dt><code>-f</code></p>
<dd> Don&#8217;t fork to the background. <i>collectd</i> will also <code>not</code> close standard file descriptors, detach from the session nor write a pid file. This is mainly thought for &#8216;supervising&#8217; init replacements such as <i>runit</i>. If using <i>upstart</i> or <i>systemd</i> though, starting with version 5.5.0 <i>collectd</i> is able to notify these two init replacements, and <code>does</code> require forking to the background for process supervision. The <i>contrib/</i> directory has sample <i>upstart</i> and <i>systemd</i> configuration files.</p>
<dt><code>-h</code></p>
<dd> Output usage information and exit.</dl>
<h2>PLUGINS</h2>
<p> As noted above, the real power of collectd lies within it&#8217;s plugins. A (hopefully complete) list of plugins and short descriptions can be found in the <i></i><font SIZE="-1"><i>README</i></font><i></i> file that is distributed with the sourcecode. If you&#8217;re using a package it&#8217;s a good bet to search somewhere near <i>/usr/share/doc/collectd</i>. </p>
<p> There are two big groups of plugins, <code>input</code> and <code>output</code> plugins:</p>
<dl>
<dt>&bull;</p>
<dd> Input plugins are queried periodically. They somehow acquire the current value of whatever they where designed to work with and submit these values back to the daemon, i. e. they &#8220;dispatch&#8221; the values. As an example, the <tt>&quot;cpu plugin&quot;</tt> reads the current cpu-counters of time spent in the various modes (user, system, nice, &#8230;) and dispatches these counters to the daemon.</p>
<dt>&bull;</p>
<dd> Output plugins get the dispatched values from the daemon and does something with them. Common applications are writing to RRD-files, CSV-files or sending the data over a network link to a remote box.</dl>
<p> Of course not all plugins fit neatly into one of the two above categories. The <tt>&quot;network plugin&quot;</tt>, for example, is able to send (i. e. &#8220;write&#8221;) <code>and</code> receive (i. e. &#8220;dispatch&#8221;) values. Also, it opens a socket upon initialization and dispatches the values when it receives them and isn&#8217;t triggered at the same time the input plugins are being read. You can think of the network receive part as working asynchronous if it helps. </p>
<p> In addition to the above, there are &#8220;logging plugins&#8221;. Right now those are the <tt>&quot;logfile plugin&quot;</tt> and the <tt>&quot;syslog plugin&quot;</tt>. With these plugins collectd can provide information about issues and significant situations to the user. Several loglevels let you suppress uninteresting messages. </p>
<p> Starting with version <tt>4.3.0</tt> collectd has support for <code>monitoring</code>. This is done by checking thresholds defined by the user. If a value is out of range, a notification will be dispatched to &#8220;notification plugins&#8221;. See <i><a href="/docs/linux/man/5-collectd-conf/">collectd.conf</a></i>(5) for more detailed information about threshold checking. </p>
<p> Please note that some plugins, that provide other means of communicating with the daemon, have manpages of their own to describe their functionality in more detail. In particular those are <i><a href="/docs/linux/man/5-collectd-email/">collectd-email</a></i>(5), <i><a href="/docs/linux/man/5-collectd-exec/">collectd-exec</a></i>(5), <i><a href="/docs/linux/man/5-collectd-perl/">collectd-perl</a></i>(5), <i><a href="/docs/linux/man/5-collectd-snmp/">collectd-snmp</a></i>(5), and <i><a href="/docs/linux/man/5-collectd-unixsock/">collectd-unixsock</a></i>(5)</p>
<h2>SIGNALS</h2>
<p> <code>collectd</code> accepts the following signals:</p>
<dl>
<dt><font SIZE="-1"><code>SIGINT</code></font>, <font SIZE="-1"><code>SIGTERM</code></font></p>
<dd> These signals cause <code>collectd</code> to shut down all plugins and terminate.</p>
<dt><font SIZE="-1"><code>SIGUSR1</code></font></p>
<dd> This signal causes <code>collectd</code> to signal all plugins to flush data from internal caches. E. g. the <tt>&quot;rrdtool plugin&quot;</tt> will write all pending data to the <font SIZE="-1">RRD</font> files. This is the same as using the <tt>&quot;FLUSH -1&quot;</tt> command of the <tt>&quot;unixsock plugin&quot;</tt>.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/5-collectd-conf/">collectd.conf</a></i>(5), <i><a href="/docs/linux/man/5-collectd-email/">collectd-email</a></i>(5), <i><a href="/docs/linux/man/5-collectd-exec/">collectd-exec</a></i>(5), <i><a href="/docs/linux/man/5-collectd-perl/">collectd-perl</a></i>(5), <i><a href="/docs/linux/man/5-collectd-snmp/">collectd-snmp</a></i>(5), <i><a href="/docs/linux/man/5-collectd-unixsock/">collectd-unixsock</a></i>(5), <i><a href="/docs/linux/man/5-types-db/">types.db</a></i>(5), &lt;<a rel="nofollow" href="http://collectd.org/">http://collectd.org/</a>&gt;</p>
<h2>AUTHOR</h2>
<p> Florian Forster &lt;octo [at] collectd.org&gt; </p>
<h2>Index</h2>
