---
title: "arm4_daemon(1)"
name: "arm4_daemon"
section: "1"
letter: "a"
url: "/docs/linux/man/1-arm4_daemon/"
description: "arm4_daemon – ARM 4 collection agent"
---

<h2>NAME</h2>
<p> arm4_daemon &#8211; ARM 4 collection agent</p>
<h2>SYNOPSIS</h2>
<p> <code>arm4_daemon</code> <i>&#8211;help|-h</i><br />
 <code>arm4_daemon</code> <i>&#8211;version|-V</i><br />
 <code>arm4_daemon</code> [<i>&#8211;verbose|-v</i>] [<i>&#8211;debug|-d</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<i>&#8211;config|-C config_file</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<i>&#8211;stats|-s</i>]&nbsp;<wbr>[<i>&#8211;off|-o</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>arm4_daemon</code> program collects <i>ARM 4</i> measurement data from the <i>ARM 4</i> libraries and saves the measurements in a local database. While there will normally be many instances of the instrumented applications, there will typically be only one instance of the <code>arm4_daemon</code> running at a time.</p>
<h2>CONFIGURATION</h2>
<p> Configuration options are set in the configuration file. The default configuration is <i>/etc/arm4.conf</i>, although this can be overridden using the <i>&#8211;config</i> command line option. See <code><a href="/docs/linux/man/5-arm4-conf/">arm4.conf</a></code>(5) for more information.</p>
<h2>DATAFILES</h2>
<p> The <code>arm4_daemon</code> program uses the Berkeley database to store transaction information. Rather than a single file, this database uses separate files fore each database table. For simplicity, all database files are stored in a single directory. Therefore specifying a database or database archive location is really specifying the directory in which the files are stored. The default location for the database files is <i>/var/lib/arm4/data</i>. For backup files, a time stamped directory is created under <i>/var/lib/arm4/data/backup</i>. Each of these directories can be changed using the <i>arm4.conf</i> configuration file.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> display the command line options</p>
<dt><code>-V</code>, <code>&#8211;Version</code></p>
<dd> display the program version and exit</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> output diagnostic information as the program is run. This may not be suitable when running in the background as a true daemon but can be useful for debugging.</p>
<dt><code>-C</code>, <code>&#8211;Config</code> <i>config_file</i></p>
<dd> specifies a configuration file for this instance instead of using the default configuration file. The default configuration file <i>/etc/arm4.conf</i> is used if none is specified.</p>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd> run the daemon as a foreground process. This is primarily used for debugging.</p>
<dt><code>-s</code>, <code>&#8211;stats</code></p>
<dd> periodically display statistics on the message queues and database processes.</p>
<dt><code>-o</code>, <code>&#8211;off</code></p>
<dd> Start the agent as a &quot;null&quot; collector. Although the collector is active, no data is actually collected. This can be controlled using the <code>arm4_control</code> utility.</dl>
<h2>REPORTING BUGS</h2>
<p> Report bugs at &lt;<a rel="nofollow" href="http://www.arm4.org">http://www.arm4.org</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2005-2008 David Carter &lt;dcarter [at] arm4.org&gt; and others. All rights reserved. This program and the accompanying materials are made available under the terms of the Eclipse Public License v1.0 which accompanies this distribution, and is available at <a rel="nofollow" href="http://www.eclipse.org/legal/epl-v10.html">http://www.eclipse.org/legal/epl-v10.html</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-arm4_control/">arm4_control</a></code>(1), <code><a href="/docs/linux/man/1-arm4_dump/">arm4_dump</a></code>(1), <code><a href="/docs/linux/man/1-arm4_export/">arm4_export</a></code>(1), <code><a href="/docs/linux/man/1-arm4_report/">arm4_report</a></code>(1), <code><a href="/docs/linux/man/5-arm4_conf/">arm4_conf</a></code>(5) </p>
<h2>Index</h2>
