---
title: "mongod(1)"
name: "mongod"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mongod/"
description: "mongod – MongoDB Server"
---

<h2>NAME</h2>
<p> mongod &#8211; MongoDB Server</p>
<h2>SYNOPSIS</h2>
<p> <code>mongod</code> is the primary daemon process for the MongoDB system. It handles data requests, manages data format, and performs background management operations. </p>
<p> This document provides a complete overview of all command line options for <code>mongod</code>. These options are primarily useful for testing purposes. In common operation, use the <code>configuration file options</code> to control the behavior of your database, which is fully capable of all operations described below.</p>
<h2>OPTIONS</h2>
<h3>Core Options</h3>
<dl>
<dt><code>mongod</code></p>
<dd>
<dt><code>&#8211;help, -h</code></p>
<dd> Returns information on <code>mongod</code> options and usage.</p>
<dt><code>&#8211;version</code></p>
<dd> Returns the <code>mongod</code> release number.</p>
<dt><code>&#8211;config &lt;filename&gt;, -f</code></p>
<dd> Specifies a configuration file for runtime configuration options. The configuration file is the preferred method for runtime configuration of <code>mongod</code>. The options are equivalent to the command-line configuration options. See <a rel="nofollow" href="http://docs.mongodb.org/manual/reference/configuration-options">http://docs.mongodb.org/manual/reference/configuration-options</a> for more information. </p>
<p> Ensure the configuration file uses ASCII encoding. <code>mongod</code> does not support configuration files with non-ASCII encoding, including UTF-8.</p>
<dt><code>&#8211;verbose, -v</code></p>
<dd> Increases the amount of internal reporting returned on standard output or in log files. Increase the verbosity with the <code>-v</code> form by including the option multiple times, (e.g. <code>-vvvvv</code>.)</p>
<dt><code>&#8211;quiet</code></p>
<dd> Runs <code>mongod</code> in a quiet mode that attempts to limit the amount of output. This option suppresses:</p>
<dt>&bull;</p>
<dd> output from <i>database commands</i></p>
<dt>&bull;</p>
<dd> replication activity</p>
<dt>&bull;</p>
<dd> connection accepted events</p>
<dt>&bull;</p>
<dd> connection closed events</p>
<dt><code>&#8211;port &lt;port&gt;</code></p>
<dd> Specifies the port number when the MongoDB instance is not running on the standard port of <code>27017</code>. You may also specify the port number using the <code>&#8211;host</code> option.</p>
<dt><code>&#8211;bind_ip &lt;ip address&gt;</code></p>
<dd> Specifies the IP address that the <code>mongod</code> process binds to and listens for connections on. By default <code>mongod</code> listens for connections for all interfaces. You may attach <code>mongod</code> to any interface. When attaching <code>mongod</code> to a publicly accessible interface, ensure that you have implemented proper authentication and firewall restrictions to protect the integrity of your database.</p>
<dt><code>&#8211;maxConns &lt;number&gt;</code></p>
<dd> Specifies the maximum number of simultaneous connections that <code>mongod</code> will accept. This setting has no effect if it is higher than your operating system&#8217;s configured maximum connection tracking threshold. </p>
<p> Changed in version 2.6: MongoDB removed the upward limit on the <code>maxConns</code> setting. </p>
<dt><code>&#8211;syslog</code></p>
<dd> Sends all logging output to the host&#8217;s <i>syslog</i> system rather than to standard output or a log file as with <i>&#8211;logpath</i>. </p>
<p> <i>&#8211;syslog</i> is not supported on Windows.</p>
<dt><code>&#8211;syslogFacility &lt;string&gt;</code></p>
<dd> Specifies the facility level used when logging messages to syslog. The default is <code>user</code>. The value you specify must be supported by your operating system&#8217;s implementation of syslog. To use this option, you must enable the <i>&#8211;syslog</i> option.</p>
<dt><code>&#8211;logpath &lt;path&gt;</code></p>
<dd> Specifies the path for the log file that holds all diagnostic logging information. </p>
<p> Unless specified, <code>mongod</code> will output all log information to the standard output. Additionally, unless you also specify <i>&#8211;logappend</i>, the logfile will be overwritten when the process restarts. </p>
<p> <code>NOTE:</code> The behavior of the logging system may change in the near future in response to the <i>SERVER-4499</i> case.</p>
<dt><code>&#8211;logappend</code></p>
<dd> Appends new entries to the end of the logfile when the <code>mongod</code> restarts instead of overwriting the content of the log.</p>
<dt><code>&#8211;timeStampFormat &lt;string&gt;</code></p>
<dd> Specifies the time format for timestamps in log messages. Specify one of the following values: <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Value </td>
<td> Description
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>ctime</code> </td>
<td> Displays timestamps as <code>Wed Dec 31 18:17:54.811</code>.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>iso8601-utc</code> </td>
<td> Displays timestamps in Coordinated Universal Time (UTC) in the ISO-8601 format. For example, for New York at the start of the Epoch: <code>1970-01-01T00:00:00.000Z</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>iso8601-local</code> </td>
<td> Default value. Displays timestamps in local time in the ISO-8601 format. For example, for New York at the start of the Epoch: <code>1969-12-31T19:00:00.000+0500</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center></p>
<dt><code>&#8211;diaglog &lt;value&gt;</code></p>
<dd> Deprecated since version 2.6. </p>
<p> <i>&#8211;diaglog</i> is for internal use and not intended for most users. </p>
<p> Creates a very verbose, <i>diagnostic log</i> for troubleshooting and recording various errors. MongoDB writes these log files in the <code>dbpath</code> directory in a series of files that begin with the string <code>diaglog</code> and end with the initiation time of the logging as a hex string. </p>
<p> The specified value configures the level of verbosity. Possible values, and their impact are as follows. <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>Value</code> </td>
<td> <code>Setting</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 0 </td>
<td> off. No logging.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 1 </td>
<td> Log write operations.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 2 </td>
<td> Log read operations.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 3 </td>
<td> Log both read and write operations.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 7 </td>
<td> Log write and some read operations.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center> </p>
<p> You can use the <code>mongosniff</code> tool to replay this output for investigation. Given a typical diaglog file, located at <code>/data/db/diaglog.4f76a58c</code>, you might use a command in the following form to read these files: </p>
<pre>
mongosniff --source DIAGLOG /data/db/diaglog.4f76a58c
</pre>
<p> <code>WARNING:</code> Setting the diagnostic level to <code>0</code> will cause <code>mongod</code> to stop writing data to the <i>diagnostic log</i> file. However, the <code>mongod</code> instance will continue to keep the file open, even if it is no longer writing data to the file. If you want to rename, move, or delete the diagnostic log you must cleanly shut down the <code>mongod</code> instance before doing so.</p>
<dt><code>&#8211;traceExceptions</code></p>
<dd> For internal diagnostic use only.</p>
<dt><code>&#8211;pidfilepath &lt;path&gt;</code></p>
<dd> Specifies a file location to hold the &quot;<i>PID</i>&quot; or process ID of the <code>mongod</code> process. Useful for tracking the <code>mongod</code> process in combination with the <i>&#8211;fork</i> option. </p>
<p> Without a specified <i>&#8211;pidfilepath</i> option, <code>mongod</code> creates no PID file.</p>
<dt><code>&#8211;keyFile &lt;file&gt;</code></p>
<dd> Specifies the path to a key file to store authentication information. This option is used for interprocess authentication among the <code>mongos</code> and <code>mongod</code> instances of a <i>sharded cluster</i> or <i>replica set</i>.</p>
<dt><code>&#8211;setParameter &lt;options&gt;</code></p>
<dd> New in version 2.4. </p>
<p> Specifies an option to configure on startup. Specify multiple options with multiple <i>&#8211;setParameter</i> options. See <a rel="nofollow" href="http://docs.mongodb.org/manual/reference/parameters">http://docs.mongodb.org/manual/reference/parameters</a> for full documentation of these parameters. The <code>setParameter</code> database command provides access to many of these parameters. <i>&#8211;setParameter</i> supports the following options:</p>
<dt>&bull;</p>
<dd> <code>enableLocalhostAuthBypass</code></p>
<dt>&bull;</p>
<dd> <code>enableTestCommands</code></p>
<dt>&bull;</p>
<dd> <code>journalCommitInterval</code></p>
<dt>&bull;</p>
<dd> <code>logLevel</code></p>
<dt>&bull;</p>
<dd> <code>logUserIds</code></p>
<dt>&bull;</p>
<dd> <code>notablescan</code></p>
<dt>&bull;</p>
<dd> <code>quiet</code></p>
<dt>&bull;</p>
<dd> <code>replApplyBatchSize</code></p>
<dt>&bull;</p>
<dd> <code>replIndexPrefetch</code></p>
<dt>&bull;</p>
<dd> <code>supportCompatibilityFormPrivilegeDocuments</code></p>
<dt>&bull;</p>
<dd> <code>syncdelay</code></p>
<dt>&bull;</p>
<dd> <code>textSearchEnabled</code></p>
<dt>&bull;</p>
<dd> <code>traceExceptions</code></p>
<dt>&bull;</p>
<dd> <code>saslauthdPath</code></p>
<dt>&bull;</p>
<dd> <code>authenticationMechanisms</code></p>
<dt>&bull;</p>
<dd> <code>sslMode</code></p>
<dt>&bull;</p>
<dd> <code>clusterAuthMode</code></p>
<dt><code>&#8211;httpinterface</code></p>
<dd> New in version 2.6. </p>
<p> Enables the HTTP interface. Enabling the interface can increase network exposure. </p>
<p> Leave the HTTP interface <i>disabled</i> for production deployments. If you <i>do</i> enable this interface, you should only allow trusted clients to access this port. See <i>security-firewalls</i>. </p>
<p> <code>NOTE:</code> In MongoDB Enterprise, the HTTP Console does not support Kerberos Authentication.</p>
<dt><code>&#8211;nohttpinterface</code></p>
<dd> Deprecated since version 2.6: MongoDB disables the HTTP interface by default. </p>
<p> Disables the HTTP interface. </p>
<p> Do not use in conjunction with <i>&#8211;rest</i> or <i>&#8211;jsonp</i>. </p>
<p> <code>NOTE:</code> In MongoDB Enterprise, the HTTP Console does not support Kerberos Authentication.</p>
<dt><code>&#8211;clusterAuthMode &lt;option&gt;</code></p>
<dd> New in version 2.6. </p>
<p> Enables <i>internal x.509 authentication</i> for membership to the cluster or replica set. The <i>&#8211;clusterAuthMode</i> option can have one of the following values: <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Value </td>
<td> Description
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>keyFile</code> </td>
<td> Default value. Use keyfile for authentication.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>sendKeyFile</code> </td>
<td> For rolling upgrade purposes. Send the keyfile for authentication but can accept either keyfile or x.509 certificate.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>sendX509</code> </td>
<td> For rolling upgrade purposes. Send the x.509 certificate for authentication but can accept either keyfile or x.509 certificate.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>x509</code> </td>
<td> Recommended. Send the x.509 certificate for authentication and accept <code>only</code> x.509 certificate.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center> </p>
<p> The default distribution of MongoDB does not contain support for SSL. For more information on MongoDB and SSL, see <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/configure-ssl.">http://docs.mongodb.org/manual/tutorial/configure-ssl.</a></p>
<dt><code>&#8211;nounixsocket</code></p>
<dd> Disables listening on the UNIX socket. <code>mongod</code> always listens on the UNIX socket, unless either: <i>&#8211;nounixsocket</i> is set, <code>bind_ip</code> is not set, or <code>bind_ip</code> does not specify <code>127.0.0.1</code>. </p>
<p> New in version 2.6: <code>mongod</code> installed from official <code>.deb</code> and <code>.rpm</code> packages have the <code>bind_ip</code> configuration set to <code>127.0.0.1</code> by default. </p>
<dt><code>&#8211;unixSocketPrefix &lt;path&gt;</code></p>
<dd> Specifies a path for the UNIX socket. If this option has no value, <code>mongod</code> creates a socket with <code>/tmp</code> as a prefix. </p>
<p> MongoDB will always create and listen on a UNIX socket, unless <i>&#8211;nounixsocket</i> is set, <code>bind_ip</code> is not set, or <code>bind_ip</code> does not specify <code>127.0.0.1</code>.</p>
<dt><code>&#8211;fork</code></p>
<dd> Enables a <i>daemon</i> mode for <code>mongod</code> that runs the process in the background. This is the normal mode of operation in production and production-like environments but may not be desirable for testing.</p>
<dt><code>&#8211;auth</code></p>
<dd> Enables database authentication for users connecting from remote hosts. Configure users via the <code>mongo shell</code>. If no users exist, the localhost interface will continue to have access to the database until the you create the first user. </p>
<p> See <code>Security and Authentication</code> for more information.</p>
<dt><code>&#8211;noauth</code></p>
<dd> Disables authentication. Currently the default. Exists for future compatibility and clarity.</p>
<dt><code>&#8211;ipv6</code></p>
<dd> Enables IPv6 support, which allows <code>mongod</code> to connect to the MongoDB instance using an IPv6 network. All MongoDB programs and processes, including <code>mongod</code>, disable IPv6 support by default.</p>
<dt><code>&#8211;jsonp</code></p>
<dd> Permits <i>JSONP</i> access via an HTTP interface. Consider the security implications of allowing this activity before enabling this option. If the HTTP interface is disabled, the <i>&#8211;jsonp</i> also enables the HTTP interface. </p>
<p> <code>SEE ALSO:</code> <i>&#8211;httpinterface</i></p>
<dt><code>&#8211;rest</code></p>
<dd> Enables the simple <i>REST</i> API. Consider the security implications of allowing this activity before enabling this option. </p>
<p> If the HTTP interface is disabled, the <i>&#8211;rest</i> setting also enables the HTTP interface. </p>
<p> <code>SEE ALSO:</code> <i>&#8211;httpinterface</i> to enable the HTTP interface.</p>
<dt><code>&#8211;slowms &lt;value&gt;</code></p>
<dd> Defines the value of &quot;slow,&quot; for the <i>&#8211;profile</i> option. The database logs all slow queries to the log, even when the profiler is not turned on. When the database profiler is on, <code>mongod</code> the profiler writes to the <code>system.profile</code> collection. See the <code>profile</code> command for more information on the database profiler.</p>
<dt><code>&#8211;profile &lt;level&gt;</code></p>
<dd> Changes the level of database profiling, which inserts information about operation performance into output of <code>mongod</code> or the log file. The following levels are available: <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>Level</code> </td>
<td> <code>Setting</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 0 </td>
<td> Off. No profiling.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 1 </td>
<td> On. Only includes slow operations.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 2 </td>
<td> On. Includes all operations.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center> </p>
<p> Profiling is off by default. Database profiling can impact database performance. Enable this option only after careful consideration.</p>
<dt><code>&#8211;cpu</code></p>
<dd> Forces <code>mongod</code> to report the percentage of CPU time in write lock. <code>mongod</code> generates output every four seconds. MongoDB writes this data to standard output or the logfile if using the <code>logpath</code> option.</p>
<dt><code>&#8211;sysinfo</code></p>
<dd> Returns diagnostic system information and then exits. The information provides the page size, the number of physical pages, and the number of available physical pages.</p>
<dt><code>&#8211;dbpath &lt;path&gt;</code></p>
<dd> Specifies the directory where the <code>mongod</code> instance stores its data. Typical locations include: <code>/srv/mongodb</code>, <code>/var/lib/mongodb</code> or <code>/opt/mongodb</code> </p>
<p> Unless specified, <code>mongod</code> will look for data files in the default <code>/data/db</code> directory. (Windows systems use the <code>\data\db</code> directory.) If you installed using a package management system. Check the <code>/etc/mongodb.conf</code> file provided by your packages to see the configuration of the <i>&#8211;dbpath</i>.</p>
<dt><code>&#8211;directoryperdb</code></p>
<dd> Alters the storage pattern of the data directory to store each database&#8217;s files in a distinct folder. This option will create directories within the <i>&#8211;dbpath</i> named for each directory. </p>
<p> Use this option in conjunction with your file system and device configuration so that MongoDB will store data on a number of distinct disk devices to increase write throughput or disk capacity. </p>
<p> <code>WARNING:</code> If you have an existing <code>mongod</code> instance and <code>dbpath</code>, and you want to enable <i>&#8211;directoryperdb</i>, you <code>must</code> migrate your existing databases to directories before setting <i>&#8211;directoryperdb</i> to access those databases.</dl>
<h3>Example</h3>
<p> Given a <code>dbpath</code> directory with the following items: </p>
<pre>
journal
mongod.lock
local.0
local.1
local.ns
test.0
test.1
test.ns
</pre>
<p> To enable <i>&#8211;directoryperdb</i> you would need to modify the <code>dbpath</code> to resemble the following: </p>
<pre>
journal
mongod.lock
local/local.0
local/local.1
local/local.ns
test/test.0
test/test.1
test/test.ns
</pre>
<dl>
<dt><code>&#8211;noIndexBuildRetry</code></p>
<dd> Stops <code>mongod</code> from rebuilding indexes on the next start-up after the program had shut down or stopped in the middle of an index build.</p>
<dt><code>&#8211;noprealloc</code></p>
<dd> Disables the preallocation of data files. This shortens the start up time in some cases and can cause significant performance penalties during normal operations.</p>
<dt><code>&#8211;nssize &lt;value&gt;</code></p>
<dd> Specifies the default size for namespace files (i.e <code>.ns</code>). This option has no impact on the size of existing namespace files. The maximum size is 2047 megabytes. </p>
<p> The default value is 16 megabytes, which provides for approximately 24,000 namespaces. Each collection, as well as each index, counts as a namespace.</p>
<dt><code>&#8211;quota</code></p>
<dd> Enables a maximum limit for the number data files each database can have. When running with <i>&#8211;quota</i>, there are a maximum of 8 data files per database. Adjust the quota with the <i>&#8211;quotaFiles</i> option.</p>
<dt><code>&#8211;quotaFiles &lt;number&gt;</code></p>
<dd> Modifies the limit on the number of data files per database. This option requires the <i>&#8211;quota</i> setting. The default value for <i>&#8211;quotaFiles</i> is 8.</p>
<dt><code>&#8211;smallfiles</code></p>
<dd> Enables a mode where MongoDB uses a smaller default file size. Specifically, <i>&#8211;smallfiles</i> reduces the initial size for data files and limits them to 512 megabytes. <i>&#8211;smallfiles</i> also reduces the size of each <i>journal</i> files from 1 gigabyte to 128 megabytes. </p>
<p> Use <i>&#8211;smallfiles</i> if you have a large number of databases that each holds a small quantity of data. <i>&#8211;smallfiles</i> can lead your <code>mongod</code> to create a large number of files, which may affect performance for larger databases.</p>
<dt><code>&#8211;syncdelay &lt;value&gt;</code></p>
<dd> Controls how much time can pass before MongoDB flushes data to the data files via an <i>fsync</i> operation. <code>Do not set this value on production systems.</code> In almost every situation you should not set this value and use the default setting. </p>
<p> <code>WARNING:</code> If you set <i>&#8211;syncdelay</i> to <code>0</code>, MongoDB will not sync the memory mapped files to disk. </p>
<p> <code>mongod</code> writes data very quickly to the journal and lazily to the data files. The default <code>syncdelay</code> setting is 60 seconds. <code>syncdelay</code> has no effect on the <code>journal</code> files or <code>journaling</code>. </p>
<p> The <code>serverStatus</code> command reports the background flush thread&#8217;s status via the <code>backgroundFlushing</code> field.</p>
<dt><code>&#8211;upgrade</code></p>
<dd> Upgrades the on-disk data format of the files specified by the <i>&#8211;dbpath</i> to the latest version, if needed. </p>
<p> This option only affects the operation of <code>mongod</code> if the data files are in an old format. </p>
<p> In most cases you should <code>not</code> set this value, so you can exercise the most control over your upgrade process. See the MongoDB <i>release notes</i> (on the download page) for more information about the upgrade process.</p>
<dt><code>&#8211;repair</code></p>
<dd> Runs a repair routine on all databases. This is equivalent to shutting down and running the <code>repairDatabase</code> database command on all databases. </p>
<p> <code>WARNING:</code> During normal operations, only use the <code>repairDatabase</code> command and wrappers including <code>db.repairDatabase()</code> in the <code>mongo</code> shell and <i>mongod &#8211;repair</i>, to compact database files and/or reclaim disk space. Be aware that these operations remove and do not save any corrupt data during the repair process. </p>
<p> If you are trying to repair a <i>replica set</i> member, and you have access to an intact copy of your data (e.g. a recent backup or an intact member of the <i>replica set</i>), you should restore from that intact copy, and <code>not</code> use <code>repairDatabase</code>. </p>
<p> When using <i>journaling</i>, there is almost never any need to run <code>repairDatabase</code>. In the event of an unclean shutdown, the server will be able restore the data files to a pristine state automatically. </p>
<p> Changed in version 2.1.2. </p>
<p> If you run the repair option <i>and</i> have data in a journal file, <code>mongod</code> refuses to start. In these cases you should start <code>mongod</code> without the <i>&#8211;repair</i> option to allow <code>mongod</code> to recover data from the journal. This completes more quickly and is more likely to produce valid data files. To continue the repair operation despite the journal files, shut down <code>mongod</code> cleanly and restart with the <i>&#8211;repair</i> option. </p>
<p> <i>&#8211;repair</i> copies data from the source data files into new data files in the <code>repairpath</code>, and then replaces the original data files with the repaired data files. <i>If</i> <code>repairpath</code> is on the same device as <code>dbpath</code>, you <i>may</i> interrupt a <code>mongod</code> running <i>&#8211;repair</i> without affecting the integrity of the data set.</p>
<dt><code>&#8211;repairpath &lt;path&gt;</code></p>
<dd> Specifies the root directory containing MongoDB data files to use for the <i>&#8211;repair</i> operation. Defaults to a <code>_tmp</code> directory within the <code>dbpath</code>.</p>
<dt><code>&#8211;objcheck</code></p>
<dd> Forces the <code>mongod</code> to validate all requests from clients upon receipt to ensure that clients never insert invalid documents into the database. For objects with a high degree of sub-document nesting, <i>&#8211;objcheck</i> can have a small impact on performance. You can set <i>&#8211;noobjcheck</i> to disable object checking at runtime. </p>
<p> Changed in version 2.4: MongoDB enables <i>&#8211;objcheck</i> by default, to prevent any client from inserting malformed or invalid BSON into a MongoDB database. </p>
<dt><code>&#8211;noobjcheck</code></p>
<dd> New in version 2.4. </p>
<p> Disables the default document validation that MongoDB performs on all incoming BSON documents.</p>
<dt><code>&#8211;noscripting</code></p>
<dd> Disables the scripting engine.</p>
<dt><code>&#8211;notablescan</code></p>
<dd> Forbids operations that require a table scan.</p>
<dt><code>&#8211;journal</code></p>
<dd> Enables operation journaling to ensure write durability and data file validity. <code>mongod</code> enables journaling by default on 64-bit builds of versions after 2.0.</p>
<dt><code>&#8211;nojournal</code></p>
<dd> Disables the durability journaling. By default, <code>mongod</code> enables journaling in 64-bit versions after v2.0.</p>
<dt><code>&#8211;journalOptions &lt;arguments&gt;</code></p>
<dd> Provides functionality for testing. Not for general use, and will affect data file integrity in the case of abnormal system shutdown.</p>
<dt><code>&#8211;journalCommitInterval &lt;value&gt;</code></p>
<dd> Specifies the maximum amount of time for <code>mongod</code> to allow between journal operations. Possible values are between 2 and 300 milliseconds. Lower values increase the durability of the journal, at the expense of disk performance. </p>
<p> The default journal commit interval is 100 milliseconds if a single block device (e.g. physical volume, RAID device, or LVM volume) contains both the journal and the data files. </p>
<p> If the journal is on a different block device than the data files the default journal commit interval is 30 milliseconds. </p>
<p> To force <code>mongod</code> to commit to the journal more frequently, you can specify <code>j:true</code>. When a write operation with <code>j:true</code> is pending, <code>mongod</code> will reduce <code>journalCommitInterval</code> to a third of the set value.</p>
<dt><code>&#8211;shutdown</code></p>
<dd> Used in <i>control scripts</i>, the <i>&#8211;shutdown</i> cleanly and safely terminates the <code>mongod</code> process. When invoking <code>mongod</code> with this option you must set the <i>&#8211;dbpath</i> option either directly or by way of the <code>configuration file</code> and the <i>&#8211;config</i> option. </p>
<p> The <i>&#8211;shutdown</i> option is available only on Linux systems.</dl>
<h3>Replication Options</h3>
<dl>
<dt><code>&#8211;replSet &lt;setname&gt;</code></p>
<dd> Configures replication. Specify a replica set name as an argument to this set. All hosts in the replica set must have the same set name. </p>
<p> <code>IMPORTANT:</code> If your application connects to more than one replica set, each set should have a distinct name. Some drivers group replica set connections by replica set name.</p>
<dt><code>&#8211;oplogSize &lt;value&gt;</code></p>
<dd> Specifies a maximum size in megabytes for the replication operation log (e.g. <i>oplog</i>.) By <code>mongod</code> creates an <i>oplog</i> based on the maximum amount of space available. For 64-bit systems, the op log is typically 5% of available disk space. Once the <code>mongod</code> has created the oplog for the first time, changing <i>&#8211;oplogSize</i> will not affect the size of the oplog.</p>
<dt><code>&#8211;replIndexPrefetch</code></p>
<dd> New in version 2.2. </p>
<p> You must use <i>&#8211;replIndexPrefetch</i> in conjunction with <code>replSet</code>. The default value is <code>all</code> and available options are:</p>
<dt>&bull;</p>
<dd> <code>none</code></p>
<dt>&bull;</p>
<dd> <code>all</code></p>
<dt>&bull;</p>
<dd> <code>_id_only</code> </p>
<p> By default <i>secondary</i> members of a <i>replica set</i> will load all indexes related to an operation into memory before applying operations from the oplog. You can modify this behavior so that the secondaries will only load the <code>_id</code> index. Specify <code>_id_only</code> or <code>none</code> to prevent the <code>mongod</code> from loading <i>any</i> index into memory.</dl>
<h3>Master-Slave Replication</h3>
<p> These options provide access to conventional master-slave database replication. While this functionality remains accessible in MongoDB, replica sets are the preferred configuration for database replication.</p>
<dl>
<dt><code>&#8211;master</code></p>
<dd> Configures <code>mongod</code> to run as a replication <i>master</i>.</p>
<dt><code>&#8211;slave</code></p>
<dd> Configures <code>mongod</code> to run as a replication <i>slave</i>.</p>
<dt><code>&#8211;source &lt;host&gt;&lt;:port&gt;</code></p>
<dd> For use with the <i>&#8211;slave</i> option, the <code>&#8211;source</code> option designates the server that this instance will replicate.</p>
<dt><code>&#8211;only &lt;arg&gt;</code></p>
<dd> For use with the <i>&#8211;slave</i> option, the <code>&#8211;only</code> option specifies only a single <i>database</i> to replicate.</p>
<dt><code>&#8211;slavedelay &lt;value&gt;</code></p>
<dd> For use with the <i>&#8211;slave</i> option, the <code>&#8211;slavedelay</code> option configures a &quot;delay&quot; in seconds, for this slave to wait to apply operations from the <i>master</i> node.</p>
<dt><code>&#8211;autoresync</code></p>
<dd> For use with the <i>&#8211;slave</i> option. When set, <i>&#8211;autoresync</i> option allows this slave to automatically resync if it is more than 10 seconds behind the master. This setting may be problematic if the <i>&#8211;oplogSize</i> specifies a too small oplog. </p>
<p> If the <i>oplog</i> is not large enough to store the difference in changes between the master&#8217;s current state and the state of the slave, this instance will forcibly resync itself unnecessarily. When you set the <code>autoresync</code> option to <code>false</code>, the slave will not attempt an automatic resync more than once in a ten minute period.</p>
<dt><code>&#8211;fastsync</code></p>
<dd> In the context of <i>replica set</i> replication, set this option if you have seeded this member with a snapshot of the <i>dbpath</i> of another member of the set. Otherwise the <code>mongod</code> will attempt to perform an initial sync, as though the member were a new member. </p>
<p> In the context of <i>replica set</i> replication, set this option if you have seeded this member with a snapshot of the <i>dbpath</i> of another member of the set. Otherwise the <code>mongod</code> will attempt to perform an initial sync, as though the member were a new member. </p>
<p> <code>WARNING:</code> If the data is not perfectly synchronized <i>and</i> <code>mongod</code> starts with <code>fastsync</code>, then the secondary or slave will be permanently out of sync with the primary, which may cause significant consistency problems.</dl>
<h3>Sharded Cluster Options</h3>
<dl>
<dt><code>&#8211;configsvr</code></p>
<dd> Declares that this <code>mongod</code> instance serves as the <i>config database</i> of a sharded cluster. When running with this option, clients will not be able to write data to any database other than <code>config</code> and <code>admin</code>. The default port for a <code>mongod</code> with this option is <code>27019</code> and the default <i>&#8211;dbpath</i> directory is <code>/data/configdb</code>, unless specified. </p>
<p> Changed in version 2.2: <i>&#8211;configsvr</i> also sets <i>&#8211;smallfiles</i>. </p>
<p> Changed in version 2.4: <i>&#8211;configsvr</i> creates a local <i>oplog</i>. </p>
<p> Do not use <i>&#8211;configsvr</i> with <i>&#8211;replSet</i> or <i>&#8211;shardsvr</i>. Config servers cannot be a shard server or part of a <i>replica set</i>.</p>
<dt><code>&#8211;shardsvr</code></p>
<dd> Configures this <code>mongod</code> instance as a shard in a partitioned cluster. The default port for these instances is <code>27018</code>. The only effect of <i>&#8211;shardsvr</i> is to change the port number.</p>
<dt><code>&#8211;moveParanoia</code></p>
<dd> New in version 2.4. </p>
<p> During chunk migrations, <i>&#8211;moveParanoia</i> forces the <code>mongod</code> instances to save all documents migrated from this shard in the <code>moveChunk</code> directory of the <code>dbpath</code>. MongoDB does not delete data from this directory. </p>
<p> Prior to 2.4, <i>&#8211;moveParanoia</i> was the default behavior of MongoDB.</dl>
<h3>SSL Options</h3>
<h3>See</h3>
<p> <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/configure-ssl">http://docs.mongodb.org/manual/tutorial/configure-ssl</a> for full documentation of MongoDB&#8217;s support.</p>
<dl>
<dt><code>&#8211;ssl</code></p>
<dd> New in version 2.6. </p>
<p> Enables connection to a <code>mongod</code> or <code>mongos</code> that has SSL support enabled. </p>
<p> The default distribution of MongoDB does not contain support for SSL. For more information on MongoDB and SSL, see <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/configure-ssl.">http://docs.mongodb.org/manual/tutorial/configure-ssl.</a></p>
<dt><code>&#8211;sslMode &lt;mode&gt;</code></p>
<dd> New in version 2.6. </p>
<p> Enables SSL or mixed SSL on a port. The argument to the <i>&#8211;sslMode</i> option can be one of the following: <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Value </td>
<td> Description
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>disabled</code> </td>
<td> The server does not use SSL.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>allowSSL</code> </td>
<td> Connections between servers do not use SSL. For incoming connections, the server accepts both SSL and non-SSL.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>preferSSL</code> </td>
<td> Connections between servers use SSL. For incoming connections, the server accepts both SSL and non-SSL.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>requireSSL</code> </td>
<td> The server uses and accepts only SSL encrypted connections.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center> </p>
<p> The default distribution of MongoDB does not contain support for SSL. For more information on MongoDB and SSL, see <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/configure-ssl.">http://docs.mongodb.org/manual/tutorial/configure-ssl.</a></p>
<dt><code>&#8211;sslPEMKeyFile &lt;filename&gt;</code></p>
<dd> New in version 2.6. </p>
<p> Specifies the <code>.pem</code> file that contains both the SSL certificate and key. Specify the file name of the <code>.pem</code> file using relative or absolute paths. </p>
<p> This option is required when using the <i>&#8211;ssl</i> option to connect to a <code>mongod</code> or <code>mongos</code> that has <code>sslCAFile</code> enabled <i>without</i> <code>sslWeakCertificateValidation</code>. </p>
<p> The default distribution of MongoDB does not contain support for SSL. For more information on MongoDB and SSL, see <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/configure-ssl.">http://docs.mongodb.org/manual/tutorial/configure-ssl.</a></p>
<dt><code>&#8211;sslPEMKeyPassword &lt;value&gt;</code></p>
<dd> New in version 2.6. </p>
<p> Specifies the password to de-crypt the certificate-key file (i.e. <i>&#8211;sslPEMKeyFile</i>). Use <i>&#8211;sslPEMKeyPassword</i> only if the certificate-key file is encrypted. In all cases, <code>mongod</code> will redact the password from all logging and reporting output. </p>
<p> If the private key in the PEM file is encrypted and you do not specify <i>&#8211;sslPEMKeyPassword</i>, <code>mongod</code> will prompt for a passphrase. See <i>ssl-certificate-password</i>. </p>
<p> The default distribution of MongoDB does not contain support for SSL. For more information on MongoDB and SSL, see <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/configure-ssl.">http://docs.mongodb.org/manual/tutorial/configure-ssl.</a></p>
<dt><code>&#8211;sslClusterFile &lt;filename&gt;</code></p>
<dd> New in version 2.6. </p>
<p> Specifies the <code>.pem</code> file that contains the x.509 certificate-key file for <i>membership authentication</i> for the cluster or replica set. </p>
<p> The default distribution of MongoDB does not contain support for SSL. For more information on MongoDB and SSL, see <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/configure-ssl.">http://docs.mongodb.org/manual/tutorial/configure-ssl.</a></p>
<dt><code>&#8211;sslClusterPassword &lt;value&gt;</code></p>
<dd> New in version 2.6. </p>
<p> Specifies the password to de-crypt the x.509 certificate-key file specified with <i>&#8211;sslClusterFile</i>. Use <i>&#8211;sslClusterPassword</i> only if the certificate-key file is encrypted. In all cases, <code>mongod</code> will redact the password from all logging and reporting output. </p>
<p> Changed in version 2.6: If the x.509 key file is encrypted and you do not specify <i>&#8211;sslClusterPassword</i>, <code>mongod</code> will prompt for a passphrase. See <i>ssl-certificate-password</i>. </p>
<p> The default distribution of MongoDB does not contain support for SSL. For more information on MongoDB and SSL, see <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/configure-ssl.">http://docs.mongodb.org/manual/tutorial/configure-ssl.</a></p>
<dt><code>&#8211;sslCAFile &lt;filename&gt;</code></p>
<dd> New in version 2.6. </p>
<p> Specifies the <code>.pem</code> file that contains the root certificate chain from the Certificate Authority. Specify the file name of the <code>.pem</code> file using relative or absolute paths. </p>
<p> The default distribution of MongoDB does not contain support for SSL. For more information on MongoDB and SSL, see <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/configure-ssl.">http://docs.mongodb.org/manual/tutorial/configure-ssl.</a></p>
<dt><code>&#8211;sslCRLFile &lt;filename&gt;</code></p>
<dd> New in version 2.6. </p>
<p> Specifies the <code>.pem</code> file that contains the Certificate Revocation List. Specify the file name of the <code>.pem</code> file using relative or absolute paths. </p>
<p> The default distribution of MongoDB does not contain support for SSL. For more information on MongoDB and SSL, see <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/configure-ssl.">http://docs.mongodb.org/manual/tutorial/configure-ssl.</a></p>
<dt><code>&#8211;sslAllowInvalidCertificates</code></p>
<dd> New in version 2.6. </p>
<p> Bypasses the validation checks for server certificates and allows the use of invalid certificates. When using the <code>sslAllowInvalidCertificates</code> setting, MongoDB logs as a warning the use of the invalid certificate. </p>
<p> The default distribution of MongoDB does not contain support for SSL. For more information on MongoDB and SSL, see <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/configure-ssl.">http://docs.mongodb.org/manual/tutorial/configure-ssl.</a></p>
<dt><code>&#8211;sslWeakCertificateValidation</code></p>
<dd> New in version 2.4. </p>
<p> Disables the requirement for SSL certificate validation that <i>&#8211;sslCAFile</i> enables. With <i>&#8211;sslWeakCertificateValidation</i>, <code>mongod</code> will accept connections when the client does not present a certificate when establishing the connection. </p>
<p> If the client presents a certificate and <code>mongod</code> has <i>&#8211;sslWeakCertificateValidation</i> enabled, <code>mongod</code> will validate the certificate using the root certificate chain specified by <i>&#8211;sslCAFile</i> and reject clients with invalid certificates. </p>
<p> Use <i>&#8211;sslWeakCertificateValidation</i> if you have a mixed deployment that includes clients that do not or cannot present certificates to <code>mongod</code>. </p>
<p> The default distribution of MongoDB does not contain support for SSL. For more information on MongoDB and SSL, see <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/configure-ssl.">http://docs.mongodb.org/manual/tutorial/configure-ssl.</a></p>
<dt><code>&#8211;sslFIPSMode</code></p>
<dd> New in version 2.6. </p>
<p> Directs <code>mongod</code> to use the FIPS mode of the installed OpenSSL library. Your system must have a FIPS compliant OpenSSL library to use <i>&#8211;sslFIPSMode</i>. </p>
<p> The default distribution of MongoDB does not contain support for SSL. For more information on MongoDB and SSL, see <a rel="nofollow" href="http://docs.mongodb.org/manual/tutorial/configure-ssl.">http://docs.mongodb.org/manual/tutorial/configure-ssl.</a></dl>
<h3>Audit Options</h3>
<dl>
<dt><code>&#8211;auditDestination</code></p>
<dd> Enables auditing. The <i>&#8211;auditDestination</i> option can have one of the following values: <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Value </td>
<td> Description
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>syslog</code> </td>
<td> Output the audit events to syslog in JSON format. Not available on Windows. Audit messages have a syslog severity level of <code>info</code> and a facility level of <code>user</code>. </p>
<p> The syslog message limit can result in the truncation of the audit messages. The auditing system will neither detect the truncation nor error upon its occurrence.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>console</code> </td>
<td> Output the audit events to <code>stdout</code> in JSON format.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>file</code> </td>
<td> Output the audit events to the file specified in <i>&#8211;auditPath</i> in the format specified in <i>&#8211;auditFormat</i>.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center> </p>
<p> <code>NOTE:</code> The <code>audit system</code> is available only in <i>MongoDB Enterprise</i>.</p>
<dt><code>&#8211;auditFormat</code></p>
<dd> Specifies the format of the output file if <i>&#8211;auditDestination</i> is <code>file</code>. The <i>&#8211;auditFormat</i> can have one of the following values: <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Value </td>
<td> Description
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>JSON</code> </td>
<td> Output the audit events in JSON format to the file specified in <i>&#8211;auditPath</i>.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>BSON</code> </td>
<td> Output the audit events in BSON binary format to the file specified in <i>&#8211;auditPath</i>.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center> </p>
<p> Printing audit events to a file in JSON format degrades server performance more than printing to a file in BSON format. </p>
<p> <code>NOTE:</code> The <code>audit system</code> is available only in <i>MongoDB Enterprise</i>.</p>
<dt><code>&#8211;auditPath</code></p>
<dd> Specifies the output file for auditing if <i>&#8211;auditDestination</i> has value of <code>file</code>. The <i>&#8211;auditPath</i> option can take either a full path name or a relative path name. </p>
<p> <code>NOTE:</code> The <code>audit system</code> is available only in <i>MongoDB Enterprise</i>.</p>
<dt><code>&#8211;auditFilter</code></p>
<dd> Specifies the filter to limit the <i>types of operations</i> the audit system records. The option takes a document of the form: </p>
<pre>
{ atype: &lt;expression&gt; }
</pre>
<p> For authentication operations, the option can also take a document of the form: </p>
<pre>
{ atype: &lt;expression&gt;, &quot;param.db&quot;: &lt;database&gt; }
</pre>
<p> <code>NOTE:</code> The <code>audit system</code> is available only in <i>MongoDB Enterprise</i>.</dl>
<h2>AUTHOR</h2>
<p> MongoDB Documentation Project</p>
<h2>COPYRIGHT</h2>
<p> 2011-2014, MongoDB, Inc. </p>
<h2>Index</h2>
