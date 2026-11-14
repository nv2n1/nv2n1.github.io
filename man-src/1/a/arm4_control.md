---
title: "arm4_control(1)"
name: "arm4_control"
section: "1"
letter: "a"
url: "/docs/linux/man/1-arm4_control/"
description: "arm4_control – ARM 4 agent control program"
---

<h2>NAME</h2>
<p> arm4_control &#8211; ARM 4 agent control program</p>
<h2>SYNOPSIS</h2>
<p> <code>arm4_control</code> <i>&#8211;help|-h</i><br />
 <code>arm4_control</code> <i>&#8211;version|-V</i><br />
 <code>arm4_control</code> [<i>&#8211;config|-C config_file</i>] [<i>commands&#8230;</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>arm4_control</code> program controls the <code>arm4_daemon</code> program.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> display the command line options.</p>
<dt><code>-V</code>, <code>&#8211;Version</code></p>
<dd> display the program version and exit.</p>
<dt><code>-C</code>, <code>&#8211;Config</code> <i>config_file</i></p>
<dd> specifies a configuration file for this instance instead of using the default configuration file. The default configuration file <i>/etc/arm4.conf</i> is used if none is specified.</dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>help</code>, <code>help commands</code></p>
<dd> show all available commands.</p>
<dt><code>help &lt;command&gt;</code></p>
<dd> show options for the command.</p>
<dt><code>archive</code></p>
<dd> backup the current database to the backup directory. Unless specified in the configuration file, the main backup directory is <i>/var/lib/arm4/data/backup</i>.</p>
<dt><code>collect</code>, <code>collect status</code></p>
<dd> show the current collection state.</p>
<dt><code>collect yes</code>, <code>collect on</code></p>
<dd> turn collection on.</p>
<dt><code>collect no</code>, <code>collect off</code></p>
<dd> turn collection off.</p>
<dt><code>checkpoint</code></p>
<dd> perform a database checkpoint operation</p>
<dt><code>remove</code></p>
<dd> remove the shared memory regions and semaphores, but leave the databases intact. This is normally done when recovering from catastrophic failures.</p>
<dt><code>status</code></p>
<dd> show if an instance of the <code>arm4_daemon</code> is running.</p>
<dt><code>stop</code></p>
<dd> stop the current <code>arm4_daemon</code> instance.</p>
<dt><code>wipe</code></p>
<dd> remove the current database, shared memory regions, and semaphores. This is normally done when upgrading versions.</p>
<dt><code>application</code></p>
<dd> display currently defined applications with their application ids.</p>
<dt><code>application </code><i>app_id</i></p>
<dd> display collection parameters for the specified application.</p>
<dt><code>application </code><i>app_id</i><code> transactions</code></p>
<dd> displays the transactions definitions and corresponding transaction ids associated with the specified application.</p>
<dt><code>transaction</code></p>
<dd> displays the current transaction definitions.</p>
<dt><code>transaction </code><i>tran_id</i></p>
<dd> displays the configuration for a specific transaction id.</p>
<dt><code>transaction </code><i>tran_id</i><code> trace all</code></p>
<dd> trace all transaction instances.</p>
<dt><code>transaction </code><i>tran_id</i><code> trace none</code></p>
<dd> turn tracing off.</p>
<dt><code>transaction </code><i>tran_id</i><code> trace </code><i>n</i></p>
<dd> trace every <i>n</i>th transaction instance.</p>
<dt><code>transaction </code><i>tran_id</i><code> trace </code><i>n</i><code>[s|S]</code></p>
<dd> trace one transaction instance every <i>n</i> tenths of seconds.</p>
<dt><code>transaction </code><i>tran_id</i><code> trace application</code></p>
<dd> honor application trace requests.</p>
<dt><code>transaction </code><i>tran_id</i><code> trace noapplication</code></p>
<dd> ignore application trace requests.</p>
<dt><code>transaction </code><i>tran_id</i><code> trace default</code></p>
<dd> use application default settings.</p>
<dt><code>export definitions</code></p>
<dd> exports application, metric, and transaction definitions in xml format to stdout.</p>
<dt><code>export all</code></p>
<dd> exports the full database including definitions and instance data in xml format to stdout.</p>
<dt><code>import </code><i>filename</i></p>
<dd> imports an exported database in xml format from the file.</dl>
<h2>REPORTING BUGS</h2>
<p> Report bugs at &lt;<a rel="nofollow" href="http://www.arm4.org">http://www.arm4.org</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2005-2008 David Carter &lt;dcarter [at] arm4.org&gt; and others. All rights reserved. This program and the accompanying materials are made available under the terms of the Eclipse Public License v1.0 which accompanies this distribution, and is available at <a rel="nofollow" href="http://www.eclipse.org/legal/epl-v10.html">http://www.eclipse.org/legal/epl-v10.html</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-arm4_daemon/">arm4_daemon</a></code>(1), <code><a href="/docs/linux/man/1-arm4_report/">arm4_report</a></code>(1), <code><a href="/docs/linux/man/1-arm4_dump/">arm4_dump</a></code>(1), <code><a href="/docs/linux/man/5-arm4-conf/">arm4.conf</a></code>(5) </p>
<h2>Index</h2>
