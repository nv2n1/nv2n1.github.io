---
title: "arm4_report(1)"
name: "arm4_report"
section: "1"
letter: "a"
url: "/docs/linux/man/1-arm4_report/"
description: "arm4_report – report on ARM 4 transactions"
---

<h2>NAME</h2>
<p> arm4_report &#8211; report on ARM 4 transactions</p>
<h2>SYNOPSIS</h2>
<p> <code>arm4_report</code> <i>&#8211;help|-h</i><br />
 <code>arm4_report</code> <i>&#8211;version|-V</i><br />
 <code>arm4_report</code> [[<i>&#8211;summary|-s</i>] | [<i>&#8211;detailed|-d</i>]]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<i>&#8211;config|-C config_file</i>]&nbsp;<wbr>[<i>&#8211;archive|-a archive_directory</i>]</p>
<h2>WARNING</h2>
<p> <code>This program is deprecated and may not exist in a future release</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>arm4_report</code> program is a simple reporting interface to the <i>ARM 4</i> transaction database. Two types of reports are available. The summary report shows response time statistics for all instances of a transaction instead of individual instances. The detailed report shows the results of individual transactions.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> display the command line options.</p>
<dt><code>-V</code>, <code>&#8211;Version</code></p>
<dd> display the program version and exit.</p>
<dt><code>-s</code>, <code>&#8211;summary</code></p>
<dd> display summary information for each of the transaction types in the database. This is the default if neither summary nor detailed reports are specified.</p>
<dt><code>-d</code>, <code>&#8211;detailed</code></p>
<dd> show detailed information for each transaction instance.</p>
<dt><code>-C</code>, <code>&#8211;Config</code> <i>config_file</i></p>
<dd> specifies a configuration file for this instance instead of using the default configuration file. The default configuration file <i>/etc/arm4.conf</i> is used if none is specified.</p>
<dt><code>-a</code>, <code>&#8211;archive</code> <i>archive_directory</i></p>
<dd> read an archive created using the <code>arm4_control</code> <i>&#8211;archive</i> command.</dl>
<h2>KNOWN BUGS</h2>
<p> Although intended to be used as a user space program, the current implementation accesses the database directly. This means that the program must be run by the database owner or as root.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs at &lt;<a rel="nofollow" href="http://www.arm4.org">http://www.arm4.org</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2005-2008 David Carter &lt;dcarter [at] arm4.org&gt; and others. All rights reserved. This program and the accompanying materials are made available under the terms of the Eclipse Public License v1.0 which accompanies this distribution, and is available at <a rel="nofollow" href="http://www.eclipse.org/legal/epl-v10.html">http://www.eclipse.org/legal/epl-v10.html</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-arm4_control/">arm4_control</a></code>(1), <code><a href="/docs/linux/man/1-arm4_daemon/">arm4_daemon</a></code>(1), <code><a href="/docs/linux/man/1-arm4_dump/">arm4_dump</a></code>(1), <code><a href="/docs/linux/man/1-arm4_export/">arm4_export</a></code>(1), <code><a href="/docs/linux/man/5-arm4_conf/">arm4_conf</a></code>(5) </p>
<h2>Index</h2>
