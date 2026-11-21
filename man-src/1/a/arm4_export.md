---

title: "arm4_export(1)"
name: "arm4_export"
section: "1"
letter: "a"
url: "/docs/linux/man/1-arm4_export/"
description: "arm4_export – export the ARM 4 database in XML format"
---

<h2>NAME</h2>
<p> arm4_export &#8211; export the ARM 4 database in XML format</p>
<p> <code>arm4_export</code> <i>&#8211;help|-h</i><br />
 <code>arm4_export</code> <i>&#8211;version|-V</i><br />
 <code>arm4_export</code> [<i>&#8211;config|-C config_file</i>] [<i>&#8211;archive|-a archive_directory</i>]</p>
<p> The <code>arm4_export</code> program exports the <i>ARM 4</i> agent database to XML. This can then be used to archive the data or to facilitate conversion from one database type to another, or for upgrading agent versions. </p>
<p> This is functionally equivalent to running the command <code>arm4_control export all</code>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> display the command line options.</dd>
<dt><code>-V</code>, <code>&#8211;Version</code></dt>
<dd> display the program version and exit.</dd>
<dt><code>-C</code>, <code>&#8211;Config</code> <i>config_file</i></dt>
<dd> specifies a configuration file for this instance instead of using the default configuration file. The default configuration file <i>/etc/arm4.conf</i> is used if none is specified.</dd>
<dt><code>-a</code>, <code>&#8211;archive</code> <i>archive_directory</i></dt>
<dd> read an archive created using the <code>arm4_control</code> <i>&#8211;archive</i> command.</dd></dl>
<h2>REPORTING BUGS</h2>
<p> Report bugs at &lt;<a rel="nofollow" href="http://www.arm4.org">http://www.arm4.org</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2005-2008 David Carter &lt;dcarter [at] arm4.org&gt; and others. All rights reserved. This program and the accompanying materials are made available under the terms of the Eclipse Public License v1.0 which accompanies this distribution, and is available at <a rel="nofollow" href="http://www.eclipse.org/legal/epl-v10.html">http://www.eclipse.org/legal/epl-v10.html</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-arm4_control/">arm4_control</a></code>(1), <code><a href="/docs/linux/man/1-arm4_daemon/">arm4_daemon</a></code>(1), <code><a href="/docs/linux/man/1-arm4_dump/">arm4_dump</a></code>(1), <code><a href="/docs/linux/man/1-arm4_report/">arm4_report</a></code>(1), <code>arm4.conf</code>(5) </p>
