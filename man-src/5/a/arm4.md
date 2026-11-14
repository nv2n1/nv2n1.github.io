---
title: "arm4(5)"
name: "arm4"
section: "5"
letter: "a"
url: "/docs/linux/man/5-arm4/"
description: "arm4.conf – ARM 4 agent configuration file"
---

<p>arm4.conf &#8211; ARM 4 agent configuration file</p>
<h2>Synopsis</h2>
<p><i>/etc/arm4.conf</i></p>
<h2>Description</h2>
<p>The agent has a number of configurable options that are controlled through the configuration file. The agent and it&#8217;s utilities can use either the default file at <i>/etc/arm4.conf</i>, or a file passed in as a command line argument. While the options are passed to the programs as they start, they generally affect persistent global objects shuch as the shared memory regions that remain after the program exits. Because of this, many options will only be changed when the shared memory objects are recreated.</p>
<dl>
<dt>Options may be set in one of two ways:</p>
<dd>&lt;<i>option</i>&gt; &lt;<i>value</i>&gt;<br />
 &lt;<i>option</i>&gt; = &lt;<i>value</i>&gt; Blank lines and lines starting with <i>#</i> are considered to be comment lines. The different configuration options are:</p>
<dt><code>hostname</code></p>
<dd>overrides the default hostname. The default value is the same as returned by running the command <code>uname -n</code>.</p>
<dt><code>user</code></p>
<dd>the user name or UID for the daemon. The defaults is to run as the current user.</p>
<dt><code>group</code></p>
<dd>the group name or GID for the daemon. The defaults is to run as the current group.</p>
<dt><code>umask</code></p>
<dd>the umask used for the creation of shared objects.</p>
<dt><code>instance</code></p>
<dd>specify the <i>ARM 4</i> instance number. Refer to user guide for more information on running multiple instances. The default instance is 0.</p>
<dt><code>log_filename</code></p>
<dd>specify a file that will log all error messags from the the <code>arm4_daemon</code> process.</p>
<dt><code>schema_location</code></p>
<dd>specify a location for the schema files. This may be a local directory or a URL. This does not include the name of the schema file itself.</p>
<dt><code>db</code></p>
<dd>specify the database to use as the back end. The supported back ends are <code>bdb</code> for Berkeley databases, and <code>sqlite</code> for Sqlite3 databases.</p>
<dt><code>db_home_dir</code></p>
<dd>the home directory for the <i>ARM 4</i> instance databases. The default is <i>/var/lib/arm4/data</i>.</p>
<dt><code>db_backup_dir</code></p>
<dd>the parent directory for the database archives. When a new archive is created, a time stamped directory is created as a child of this directory. The default is <i>/var/lib/arm4/data/backup</i>.</p>
<dt></dl>
<h2>Berkeley DB Specific Configuration Options</h2>
<dd>
<dl>
<dt><code>db_log_file_size</code></p>
<dd>sets the transaction file size for the Berkeley DB. This should be large enough that no single transaction can span multiple files or memory allocation errors will occur. The <code>db_file_size</code> parameter must always be smaller than the <code>db_buffer_size</code>. Refer to the Berkeley DB documentation for more information.</p>
<dt><code>db_buffer_size</code></p>
<dd>sets the size of memory allocated for transactions. It should be large enough to hold all active transactions or memory allocation errors will occur. the <code>db_buffer_size</code> parameter should always be larger than <code>db_file_size</code>. Refer to the Berkeley DB documentation for more information.</p>
<dt><code>db_key</code></p>
<dd>multiple instances of the Berkeley database share common memory regions. In cases where this is undesireable, the <code>db_key</code> can be set explicitly. Refer to the Berkeley DB documentation for more information.</p>
<dt><code>checkpoint</code></p>
<dd>specifies the database checkpoint interval in seconds. A value less than or equal to zero disables checkpointing, except on database close. It is also possible to initiate a checkpoint operation using <i><a href="/docs/linux/man/1-arm4_control/">arm4_control</a>(1)</i>.</dl>
<h2>Files</h2>
<p><i>/etc/arm4.conf</i></p>
<h2>Reporting Bugs</h2>
<p>Report bugs at &lt;<a rel="nofollow" href="http://www.arm4.org">http://www.arm4.org</a>&gt;</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2005-2008 David Carter &lt;dcarter [at] arm4.org&gt; and others. All rights reserved. This program and the accompanying materials are made available under the terms of the Eclipse Public License v1.0 which accompanies this distribution, and is available at <a rel="nofollow" href="http://www.eclipse.org/legal/epl-v10.html">http://www.eclipse.org/legal/epl-v10.html</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-arm4_daemon/">arm4_daemon</a></code>(1), <code><a href="/docs/linux/man/1-arm4_control/">arm4_control</a></code>(1), <code><a href="/docs/linux/man/1-arm4_dump/">arm4_dump</a></code>(1), <code><a href="/docs/linux/man/1-arm4_export/">arm4_export</a></code>(1) <code><a href="/docs/linux/man/1-arm4_report/">arm4_report</a></code>(1) </p>
