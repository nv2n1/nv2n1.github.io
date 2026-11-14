---
title: "mysqlfailover(1)"
name: "mysqlfailover"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mysqlfailover/"
description: "mysqlfailover – Automatic replication failover"
---

<h2 class="name">NAME</h2>
<p> mysqlfailover &#8211; Automatic replication failover </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mysqlfailover [</code><i>options</i><code>]</code></dl>
<h2>DESCRIPTION</h2>
<dd>This utility permits users to perform replication health monitoring and automatic failover on a replication topology consisting of a master and its slaves. The utility is designed to run interactively or continuously refreshing the health information at periodic intervals. Its primary mission is to monitor the master for failure and when a failure occurs, execute failover to the best slave available. The utility accepts a list of slaves to be considered the candidate slave. </p>
<p> This utility is designed to work exclusively for servers that support global transaction identifiers (GTIDs) and have GTID_MODE=ON. MySQL server versions 5.6.9 and higher support GTIDs. See the MySQL server online reference manual for more information about setting up replication with GTIDs enabled. </p>
<p> The user can specify the interval in seconds to use for detecting the master status and generating the health report using the <code>&#8211;interval</code> option. At each interval, the utility will check to see if the server is alive via a ping operation followed by a check of the connector to detect if the server is still reachable. The ping operation can be controlled with the <code>&#8211;ping</code> option (see below). </p>
<p> If the master is found to be offline or unreachable, the utility will execute one of the following actions based on the value of the <code>&#8211;failover-mode</code> option. </p>
<p> <code>auto</code> Execute automatic failover to the list of candidates first and if no slaves are viable, continue to locate a viable candidate from the list of slaves. If no slaves are found to be a viable candidate, the utility will generate and error and exit. </p>
<p> Once a candidate is found, the utility will conduct failover to the best slave. The command will test each candidate slave listed for the prerequisites. Once a candidate slave is elected, it is made a slave of each of the other slaves thereby collecting any transactions executed on other slaves but not the candidate. In this way, the candidate becomes the most up-to-date slave. </p>
<p> <code>elect</code> This mode is the same as auto except if no candidates specified in the list of candidate slaves are viable, it does not check the remaining slaves and generates and error and exits. </p>
<p> <code>fail</code> This mode produces an error and does not failover when the master is downed. This mode is used to provide periodic health monitoring without the failover action taken. </p>
<p> For all options that permit specifying multiple servers, the options require a comma-separated list of connection parameters in the following form (where the password, port, and socket are optional).: </p>
<dl>
<dt>
<dd>
<pre><code>
&lt;*user*&gt;[:&lt;*passwd*&gt;]@&lt;*host*&gt;[:&lt;*port*&gt;][:&lt;*socket*&gt;] or
&lt;*login-path*&gt;[:&lt;*port*&gt;][:&lt;*socket*&gt;]
</code></pre>
</dl>
<p> The utility permits users to discover slaves connected to the master. In order to use the discover slaves feature, all slaves must use the &#8211;report-host and &#8211;report-port startup variables to specify the correct hostname and ip port of the slave. If these are missing or report the incorrect information, the slaves health may not be reported correctly or the slave may not be listed at all. The discover slaves feature ignores any slaves it cannot connect to. </p>
<p> The discover slaves feature is run automatically on each interval. </p>
<p> The utility permits the user to specify an external script to execute before and after the switchover and failover commands. The user can specify these with the <code>&#8211;exec-before</code> and <code>&#8211;exec-after</code> options. The return code of the script is used to determine success thus each script must report 0 (success) to be considered successful. If a script returns a value other than 0, the result code is presented in an error message. </p>
<p> The utility also permits the user to specify a script to be used for detecting a downed master or an application-level event to trigger failover. This can be specified using the <code>&#8211;exec-fail-check</code> option. The return code for the script is used to invoke failover. A return code of 0 indicates failover should not take place. A return code other than 0 indicates failover should take place. This is checked at the start of each interval if a script is supplied. The timeout option is not used in this case and the script is run once at the start of each interval. </p>
<p> The utility permits the user to log all actions taken during the commands. The <code>&#8211;log</code> option requires a valid path and file name of the file to use for logging operations. The log is active only when this option is specified. The option <code>&#8211;log-age</code> specifies the age in days that log entries are kept. The default is seven (7) days. Older entries are automatically deleted from the log file (but only if the <code>&#8211;log</code> option is specified). </p>
<p> The format of the log file includes the date and time of the event, the level of the event (informational &#8211; INFO, warning &#8211; WARN, error &#8211; ERROR, critical failure &#8211; CRITICAL), and the message reported by the utility. </p>
<p> The interface provides the user with a number of options for displaying additional information. The user can choose to see the replication health report (default), or choose to see the list of GTIDs in use, the UUIDs in use, and if logging is enabled the contents of the log file. Each of these reports is described below. </p>
<p> <code>health</code> Display the replication health of the topology. This report is the default view for the interface. By default, this includes the host name, port, role (MASTER or SLAVE) of the server, state of the server (UP = is connected, WARN = not connected but can ping, DOWN = not connected and cannot ping), the GTID_MODE, and health state. </p>
<p> The master health state is based on the following; if GTID_MODE=ON, the server must have binary log enabled, and there must exist a user with the REPLICATE SLAVE privilege. </p>
<p> The slave health state is based on the following; the IO_THREAD and SQL_THREADS must be running, it must be connected to the master, there are no errors, the slave delay for non-gtid enabled scenarios is not more than the threshold provided by the <code>&#8211;max-position</code> and the slave is reading the correct master log file, and slave delay is not more than the <code>&#8211;seconds-behind</code> threshold option. </p>
<p> At each interval, if the discover slaves option was specified at startup and new slaves are discovered, the health report is refreshed. </p>
<p> <code>gtid</code>: Display the master&#8217;s list of executed GTIDs, contents of the GTID variables; @@GLOBAL.GTID_EXECUTED, @@GLOBAL.GTID_PURGED, and @@GLOBAL.GTID_OWNED. Thus, the user can toggle through four screens by pressing the &#8216;G&#8217; key repeatedly. The display will cycle through all four screens restarting after the fourth screen. </p>
<p> <code>UUID</code>: Display universally unique identifiers (UUIDs) for all servers. </p>
<p> <code>Log</code>: This option is visible only if the <code>&#8211;log</code> option is specified. Show the contents of the log file. This can be helpful to see at a later time when failover occurred and the actions or messages recorded at the time. </p>
<p> The user interface is designed to match the size of the terminal window in which it is run. A refresh option is provided to permit users to resize their terminal windows or refresh the display at any time. However, the interface will automatically resize to the terminal window on each interval. </p>
<p> The interface will display the name of the utility, the master&#8217;s status including binary log file, position, and filters as well as the date and time of the next interval event. </p>
<p> The interface will also permit the user to scroll up or down through a list longer than what the terminal window permits. When a long list is presented, the scroll options become enabled. The user can scroll the list up with the up arrow key and down with the down arrow key. </p>
<p> Use the <code>&#8211;verbose</code> option to see additional information in the health report and additional messages during failover. </p>
<p> The utility supports two modes of operation. The default mode, running as a console, works as described above. An additional mode that permits you to run the utility as a daemon is provided for POSIX platforms. </p>
<p> When run as a daemon, the utility does not have interactivity. However, all events are written to the log file. You can control what is written to the log by using the <code>&#8211;report-values</code> option. </p>
<p> To run the utility as a daemon, use the <code>&#8211;daemon</code> option. There are three commands that can by used in <code>&#8211;daemon</code> option. These include: </p>
<dl>
<dt>
<dd> &bull; start </p>
<p> Starts the daemon. The <code>&#8211;log</code> option is required.</dl>
<dl>
<dt>
<dd> &bull; stop </p>
<p> Stops the daemon. If you used the option <code>&#8211;pidfile</code>, the value must be the same when starting the daemon.</dl>
<dl>
<dt>
<dd> &bull; restart </p>
<p> Restarts the daemon. If you used the option <code>&#8211;pidfile</code>, the value must be the same when starting the daemon.</dl>
<dl>
<dt>
<dd> &bull; nodetach </p>
<p> Starts the daemon, but it will not detach the process from the console. The <code>&#8211;log</code> option is required.</dl>
<p> The utility supports two modes of operation. The default mode, running as a console, works as described above. An additional mode that permits you to run the utility as a daemon is provided for POSIX platforms. </p>
<p> When run as a daemon, the utility does not have interactivity. However, all events are written to the log file. You can control what is written to the log by using the <code>&#8211;report-values</code> option. </p>
<p> To run the utility as a daemon, use the <code>&#8211;daemon</code> option. There are three commands that can by used in <code>&#8211;daemon</code> option. These include: </p>
<dl>
<dt>
<dd> &bull; start </p>
<p> Starts the daemon. The <code>&#8211;log</code> option is required.</dl>
<dl>
<dt>
<dd> &bull; stop </p>
<p> Stops the daemon. The option <code>&#8211;pidfile</code> must be the same when starting the daemon.</dl>
<dl>
<dt>
<dd> &bull; restart </p>
<p> Restarts the daemon. The option <code>&#8211;pidfile</code> must be the same when starting the daemon.</dl>
<dl>
<dt>
<dd> &bull; nodetach </p>
<p> Starts the daemon, but it will not detach the process from the console. The <code>&#8211;log</code> option is required.</dl>
<p>OPTIONS </p>
<p> <code>mysqlfailover</code> accepts the following command-line options: </p>
<dl>
<dt>
<dd> &bull; &#8211;help </p>
<p> Display a help message and exit.</dl>
<dl>
<dt>
<dd> &bull; &#8211;candidates=&lt;candidate slave connections&gt; </p>
<p> Connection information for candidate slave servers for failover in the form: &lt;<i>user</i>&gt;[:&lt;<i>passwd</i>&gt;]@&lt;<i>host</i>&gt;[:&lt;<i>port</i>&gt;][:&lt;<i>socket</i>&gt;] or &lt;<i>login-path</i>&gt;[:&lt;<i>port</i>&gt;][:&lt;<i>socket</i>&gt;]. Valid only with failover command. List multiple slaves in comma-separated list.</dl>
<dl>
<dt>
<dd> &bull; &#8211;daemon=&lt;command&gt; </p>
<p> Run as a daemon. It can be <code>start</code> (start daemon), <code>stop</code> (stop daemon), <code>restart</code> (stop then start the daemon) or <code>nodetach</code> (start but do not detach the process). This option is only available for POSIX systems.</dl>
<dl>
<dt>
<dd> &bull; &#8211;discover-slaves-login=&lt;user:password&gt; </p>
<p> At startup, query master for all registered slaves and use the user name and password specified to connect. Supply the user and password in the form &lt;<i>user</i>&gt;[:&lt;<i>passwd</i>&gt;] or &lt;<i>login-path</i>&gt;. For example, &#8211;discover=joe:secret will use &#8216;joe&#8217; as the user and &#8216;secret&#8217; as the password for each discovered slave.</dl>
<dl>
<dt>
<dd> &bull; &#8211;exec-after=&lt;script&gt; </p>
<p> Name of script to execute after failover or switchover. Script name may include the path.</dl>
<dl>
<dt>
<dd> &bull; &#8211;exec-before=&lt;script&gt; </p>
<p> Name of script to execute before failover or switchover. Script name may include the path.</dl>
<dl>
<dt>
<dd> &bull; &#8211;exec-fail-check=&lt;script&gt; </p>
<p> Name of script to execute on each interval to invoke failover.</dl>
<dl>
<dt>
<dd> &bull; &#8211;exec-post-failover=&lt;script&gt; </p>
<p> Name of script to execute after failover is complete and the utility has refreshed the health report.</dl>
<dl>
<dt>
<dd> &bull; &#8211;failover-mode=&lt;mode&gt;, -f &lt;mode&gt; </p>
<p> Action to take when the master fails. &#8216;auto&#8217; = automatically fail to best slave, &#8216;elect&#8217; = fail to candidate list or if no candidate meets criteria fail, &#8216;fail&#8217; = take no action and stop when master fails. Default = &#8216;auto&#8217;.</dl>
<dl>
<dt>
<dd> &bull; &#8211;force </p>
<p> Override the registration check on master for multiple instances of the console monitoring the same master. See notes.</dl>
<dl>
<dt>
<dd> &bull; &#8211;interval=&lt;seconds&gt;, -i &lt;seconds&gt; </p>
<p> Interval in seconds for polling the master for failure and reporting health. Default = 15 seconds. Minimum is 5 seconds.</dl>
<dl>
<dt>
<dd> &bull; &#8211;log=&lt;log_file&gt; </p>
<p> Specify a log file to use for logging messages</dl>
<dl>
<dt>
<dd> &bull; &#8211;log-age=&lt;days&gt; </p>
<p> Specify maximum age of log entries in days. Entries older than this will be purged on startup. Default = 7 days.</dl>
<dl>
<dt>
<dd> &bull; &#8211;master=&lt;connection&gt; </p>
<p> Connection information for the master server in the format: &lt;<i>user</i>&gt;[:&lt;<i>passwd</i>&gt;]@&lt;<i>host</i>&gt;[:&lt;<i>port</i>&gt;][:&lt;<i>socket</i>&gt;] or &lt;<i>login-path</i>&gt;[:&lt;<i>port</i>&gt;][:&lt;<i>socket</i>&gt;].</dl>
<dl>
<dt>
<dd> &bull; &#8211;max-position=&lt;position&gt; </p>
<p> Used to detect slave delay. The maximum difference between the master&#8217;s log position and the slave&#8217;s reported read position of the master. A value greater than this means the slave is too far behind the master. Default = 0.</dl>
<dl>
<dt>
<dd> &bull; &#8211;pedantic, -p </p>
<p> Used to stop failover if some inconsistencies are found (e.g. errant transactions on slaves or SQL thread errors) during servers checks. By default, the utility will only issue warnings if issues are found when checking slaves status during failover and will continue its execution unless this option is specified.</dl>
<dl>
<dt>
<dd> &bull; &#8211;pidfile=&lt;pidfile&gt; </p>
<p> Pidfile for running mysqlfailover as a daemon. This file contains the PID (process identifier), that uniquely identify a process. It is needed to identify and control the process forked by mysqlfailover.</dl>
<dl>
<dt>
<dd> &bull; &#8211;ping=&lt;number&gt; </p>
<p> Number of ping attempts for detecting downed server. Note: on some platforms this is the same as number of seconds to wait for ping to return. Default is 3 seconds.</dl>
<dl>
<dt>
<dd> &bull; &#8211;report-values=&lt;report_values&gt; </p>
<p> Report values used in mysqlfailover running as a daemon. It can be health, gtid or uuid. Multiple values can be used separated by commas. </p>
<dl>
<dt>
<dd> &bull; health </p>
<p> Display the replication health of the topology.</dl>
<dl>
<dt>
<dd> &bull; gtid </p>
<p> Display the master&#8217;s list of executed GTIDs, contents of the GTID variables; @@GLOBAL.GTID_EXECUTED, @@GLOBAL.GTID_PURGED and @@GLOBAL.GTID_OWNED.</dl>
<dl>
<dt>
<dd> &bull; uuid </p>
<p> Display universally unique identifiers (UUIDs) for all servers.</dl>
<p> Default = health.</dl>
<dl>
<dt>
<dd> &bull; &#8211;rpl-user=:&lt;replication_user&gt; </p>
<p> The user and password for the replication user requirement , in the form: &lt;<i>user</i>&gt;[:&lt;<i>password</i>&gt;] or &lt;<i>login-path</i>&gt;. E.g. rpl:passwd </p>
<p> Default = None.</dl>
<dl>
<dt>
<dd> &bull; &#8211;script-threshold=&lt;return_code&gt; </p>
<p> Value for external scripts to trigger aborting the operation if result is greater than or equal to the threshold. </p>
<p> Default = None (no threshold checking).</dl>
<dl>
<dt>
<dd> &bull; &#8211;seconds-behind=&lt;seconds&gt; </p>
<p> Used to detect slave delay. The maximum number of seconds behind the master permitted before slave is considered behind the master. Default = 0.</dl>
<dl>
<dt>
<dd> &bull; &#8211;slaves=&lt;slave connections&gt; </p>
<p> Connection information for slave servers in the form: &lt;<i>user</i>&gt;[:&lt;<i>passwd</i>&gt;]@&lt;<i>host</i>&gt;[:&lt;<i>port</i>&gt;][:&lt;<i>socket</i>&gt;] or &lt;<i>login-path</i>&gt;[:&lt;<i>port</i>&gt;][:&lt;<i>socket</i>&gt;]. List multiple slaves in comma-separated list. The list will be evaluated literally whereby each server is considered a slave to the master listed regardless if they are a slave of the master.</dl>
<dl>
<dt>
<dd> &bull; &#8211;timeout=&lt;seconds&gt; </p>
<p> Maximum timeout in seconds to wait for each replication command to complete. For example, timeout for slave waiting to catch up to master. </p>
<p> Default = 3.</dl>
<dl>
<dt>
<dd> &bull; &#8211;verbose, -v </p>
<p> Specify how much information to display. Use this option multiple times to increase the amount of information. For example, <code>-v</code> = verbose, <code>-vv</code> = more verbose, <code>-vvv</code> = debug.</dl>
<dl>
<dt>
<dd> &bull; &#8211;version </p>
<p> Display version information and exit.</dl>
<p>NOTES </p>
<p> The login user must have the appropriate permissions to execute <code>SHOW SLAVE STATUS</code>, <code>SHOW MASTER STATUS</code>, and <code>SHOW VARIABLES</code> on the appropriate servers as well as grant the REPLICATE SLAVE privilege. Different permission are required by the failover utility to run successfully for master and slaves. In particular, users connectioned to slaves and candidates require <code>SUPER</code>, <code>GRANT OPTION</code>, <code>REPLICATION SLAVE</code>, and <code>RELOAD</code> privileges. </p>
<p> In addition, the user connected to the master requires <code>DROP</code>, <code>CREATE</code>, <code>INSERT</code> and <code>SELECT</code> privileges to register the failover console. The utility checks permissions for the master, slaves, and candidates at startup. </p>
<p> At startup, the console will attempt to register itself with the master. If another console is already registered, and the failover mode is auto or elect, the console will be blocked from running failover. When a console quits, it deregisters itself from the master. If this process is broken, the user may override the registration check by using the <code>&#8211;force</code> option. </p>
<p> Mixing IP and hostnames is not recommended. The replication-specific utilities will attempt to compare hostnames and IP addresses as aliases for checking slave connectivity to the master. However, if your installation does not support reverse name lookup, the comparison could fail. Without the ability to do a reverse name lookup, the replication utilities could report a false negative that the slave is (not) connected to the master. </p>
<p> For example, if you setup replication using MASTER_HOST=ubuntu.net on the slave and later connect to the slave with mysqlrplcheck and have the master specified as &#8211;master=192.168.0.6 using the valid IP address for ubuntu.net, you must have the ability to do a reverse name lookup to compare the IP (192.168.0.6) and the hostname (ubuntu.net) to determine if they are the same machine. </p>
<p> Similarly, in order to avoid issues mixing local IP &#8216;127.0.0.1&#8217; with &#8216;localhost&#8217;, all the addresses &#8216;127.0.0.1&#8217; will be internally converted to &#8216;localhost&#8217; by the utility. Nevertheless, It is best to use the actual hostname of the master when connecting or setting up replication. </p>
<p> The utility will check to see if the slaves are using the option &#8211;master-info-repository=TABLE. If they are not, the utility will stop with an error. </p>
<p> The path to the MySQL client tools should be included in the PATH environment variable in order to use the authentication mechanism with login-paths. This will allow the utility to use the my_print_defaults tools which is required to read the login-path values from the login configuration file (.mylogin.cnf). </p>
<p> The console creates a special table in the mysql database that is used to keep track of which instance is communicating with the master. If you use the <code>&#8211;force</code> option, the console will remove the rows in this table. The table is constructed with: </p>
<dl>
<dt>
<dd>
<pre>
CREATE TABLE IF NOT EXISTS mysql.failover_console (host char(30), port char(10))
</pre>
</dl>
<p> When the console starts, a row is inserted containing the hostname and port of the master. On startup, if a row matches these values, the console will not start. If you use the <code>&#8211;force</code> option, the row is deleted. </p>
<p> When running the utility using the <code>&#8211;daemon</code> option with <code>nodetach</code> the <code>&#8211;pidfile</code> option can be omitted, will be ignored if used. </p>
<p> When running the utility using the <code>&#8211;daemon</code> option with <code>nodetach</code> the <code>&#8211;pidfile</code> option can be omitted, will be ignored if used.<br />
EXAMPLES </p>
<p> To launch the utility, you must specify at a minimum the <code>&#8211;master</code> option and either the <code>&#8211;discover-slaves-login</code> option or the <code>&#8211;slaves</code> option. The option: option can be used in conjunction with the <code>&#8211;slaves</code> option to specify a list of known slaves (or slaves that do not report their host and ip) and to discover any other slaves connected to the master. </p>
<p> An example of the user interface and some of the report views are shown in the following examples. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> The &quot;GTID Executed Set&quot; will display the first GTID listed in the SHOW MASTER STATUS view. If there are multiple GTIDs listed, the utility shall display [&#8230;] to indicate there are additional GTIDs to view. You can view the complete list of GTIDs on the GTID display screens. </p>
</dl>
<p> The default interface will display the replication health report like the following. In this example the log file is enabled. A sample startup command is shown below: </p>
<dl>
<dt>
<dd>
$ mysqlfailover&#8211; master = root[at] localhost : 3331 &#8211;discover &#8211; slaves &#8211; login = root&#8211; log = log.txt<br />
                                                                                                    MySQL Replication Monitor and Failover Utility<br />
                                                                                                        Failover Mode = auto Next Interval = Mon Mar 19 15 : 56 : 03 2012 Master Information&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Binary Log File Position Binlog_Do_DB Binlog_Ignore_DB<br />
                                                                                                                                                     mysql &#8211;<br />
                                                                                                                                                 bin .000001 571 GTID Executed Set 2A67DE00 &#8211; 2DA1 &#8211; 11E2 &#8211; A711 &#8211; 00764F2BE90F : 1 &#8211; 7 [&#8230;] Replication Health Status + &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; -+ |<br />
                                                                                                                                             host | port | role | state | gtid_mode | health |<br />
                                                                                                                                             +&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; -+ | localhost | 3331 | MASTER | UP | ON | OK |<br />
                                                                                                                                             | localhost | 3332 | SLAVE | UP | ON | OK |<br />
                                                                                                                                             | localhost | 3333 | SLAVE | UP | ON | OK |<br />
                                                                                                                                             | localhost | 3334 | SLAVE | UP | ON | OK |<br />
                                                                                                                                             +&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; -+Q &#8211; quit R &#8211; refresh H &#8211; health G &#8211; GTID Lists U &#8211; UUIDs L &#8211; log entries
</dl>
<p> Pressing the &#8216;q&#8217; key will exit the utility. Pressing the &#8216;r&#8217; key will refresh the current display. Pressing the &#8216;h&#8217; key will return to the replication health report. </p>
<p> If the user presses the &#8216;g&#8217; key, the gtid report is shown like the following. The first page shown is the master&#8217;s executed GTID set: </p>
<dl>
<dt>
<dd>
MySQL Replication Monitor and Failover Utility<br />
    Failover Mode = auto Next Interval = Mon Mar 19 15 : 59 : 33 2012 Master Information&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Binary Log File Position Binlog_Do_DB Binlog_Ignore_DB<br />
                                                 mysql &#8211;<br />
                                             bin .000001 571 GTID Executed Set 2A67DE00 &#8211; 2DA1 &#8211; 11E2 &#8211; A711 &#8211; 00764F2BE90F : 1 &#8211; 7 [&#8230;] Master GTID Executed Set + &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+ |<br />
                                         gtid |<br />
                                         +&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+ | 2A67DE00 &#8211; 2DA1 &#8211; 11E2 &#8211; A711 &#8211; 00764F2BE90F : 1 &#8211; 7 |<br />
                                         | 5503D37E-2DB2 &#8211; 11E2 &#8211; A781 &#8211; 8077D4C14B33 : 1 &#8211; 3 |<br />
                                         +&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+Q &#8211; quit R &#8211; refresh H &#8211; health G &#8211; GTID Lists U &#8211; UUIDs L &#8211; log entries Up | Down &#8211; scroll
</dl>
<p> If the user continues to press the &#8216;g&#8217; key, the display will cycle through the three gtid lists. </p>
<p> If the list is longer than the screen permits as shown in the example above, the scroll up and down help is also shown. In this case, if the user presses the down arrow, the list will scroll down. </p>
<p> If the user presses the &#8216;u&#8217; key, the list of UUIDs used in the topology are shown.: </p>
<dl>
<dt>
<dd>
MySQL Replication Monitor and Failover Utility<br />
    Failover Mode = auto Next Interval = Mon Mar 19 16 : 02 : 34 2012 Master Information&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Binary Log File Position Binlog_Do_DB Binlog_Ignore_DB<br />
                                                 mysql &#8211;<br />
                                             bin .000001 571 GTID Executed Set 2A67DE00 &#8211; 2DA1 &#8211; 11E2 &#8211; A711 &#8211; 00764F2BE90F : 1 &#8211; 7 [&#8230;] UUIDs + &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+ |<br />
                                         host | port | role | uuid |<br />
                                         +&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+ | localhost | 3331 | MASTER | 55c65a00 &#8211; 71fd &#8211; 11e1 &#8211; 9f80 &#8211; ac64ef85c961 |<br />
                                         | localhost | 3332 | SLAVE | 5dd30888 &#8211; 71fd &#8211; 11e1 &#8211; 9f80 &#8211; dc242138b7ec |<br />
                                         | localhost | 3333 | SLAVE | 65ccbb38 &#8211; 71fd &#8211; 11e1 &#8211; 9f80 &#8211; bda8146bdb0a |<br />
                                         | localhost | 3334 | SLAVE | 6dd6abf4 &#8211; 71fd &#8211; 11e1 &#8211; 9f80 &#8211; d406a0117519 |<br />
                                         +&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+Q &#8211; quit R &#8211; refresh H &#8211; health G &#8211; GTID Lists U &#8211; UUIDs L &#8211; log entries
</dl>
<p> If, once the master is detected as down and failover mode is auto or elect and there are viable candidate slaves, the failover feature will engage automatically and the user will see the failover messages appear. When failover is complete, the interface returns to monitoring replication health after 5 seconds. The following shows an example of failover occurring.: </p>
<dl>
<dt>
<dd>
Failover starting&#8230;<br />
#Candidate slave localhost : 3332 will become the new master.<br />
#Preparing candidate for failover.<br />
#Creating replication user if it does not exist.<br />
#Stopping slaves.<br />
#Performing STOP on all slaves.<br />
#Switching slaves to new master.<br />
#Starting slaves.<br />
#Performing START on all slaves.<br />
#Checking slaves for errors.<br />
#Failover complete.<br />
#Discovering slaves for master at localhost : 3332<br />
    Failover console will restart in 5 seconds.
</dl>
<p> After the failover event, the new topology is shown in the replication health report.: </p>
<dl>
<dt>
<dd>
MySQL Replication Monitor and Failover Utility<br />
    Failover Mode = auto Next Interval = Mon Mar 19 16 : 05 : 12 2012 Master Information&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Binary Log File Position Binlog_Do_DB Binlog_Ignore_DB<br />
                                                 mysql &#8211;<br />
                                             bin .000001 1117 GTID Executed Set 2A67DE00 &#8211; 2DA1 &#8211; 11E2 &#8211; A711 &#8211; 00764F2BE90F : 1 &#8211; 7 [&#8230;] UUIDs + &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; -+ |<br />
                                         host | port | role | state | gtid_mode | health |<br />
                                         +&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; -+ | localhost | 3332 | MASTER | UP | ON | OK |<br />
                                         | localhost | 3333 | SLAVE | UP | ON | OK |<br />
                                         | localhost | 3334 | SLAVE | UP | ON | OK |<br />
                                         +&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; -+Q &#8211; quit R &#8211; refresh H &#8211; health G &#8211; GTID Lists U &#8211; UUIDs L &#8211; log entries
</dl>
<p> If the user presses the &#8216;l&#8217; key and the <code>&#8211;log</code> option was specified, the interface will show the entries in the log file. Note: example truncated for space allowance.: </p>
<dl>
<dt>
<dd>
<pre><code>
MySQL Replication Monitor and Failover Utility
Failover Mode = auto     Next Interval = Mon Mar 19 16:06:13 2012
Master Information
------------------
Binary Log File   Position  Binlog_Do_DB  Binlog_Ignore_DB
mysql-bin.000001  1117
GTID Executed Set
2A67DE00-2DA1-11E2-A711-00764F2BE90F:1-7 [...]
Log File
+-------------------------+----------------------------------------- ... --+
| Date                    | Entry                                    ...   |
+-------------------------+----------------------------------------- ... --+
| 2012-03-19 15:55:33 PM  | INFO Failover console started.           ...   |
| 2012-03-19 15:55:33 PM  | INFO Failover mode = auto.               ...   |
| 2012-03-19 15:55:33 PM  | INFO Getting health for master: localhos ...   |
| 2012-03-19 15:55:33 PM  | INFO Master status: binlog: mysql-bin.00 ...   |
+-------------------------+----------------------------------------- ... --+
Q-quit R-refresh H-health G-GTID Lists U-UUIDs L-log entries Up|Down-scroll\
</code></pre>
</dl>
<h2>COPYRIGHT</h2>
<h2>SEE ALSO</h2>
<p> For more information, please refer to the MySQL Utilities section of the MySQL Workbench Reference Manual, which is available online at <a rel="nofollow" href="http://dev.mysql.com/doc/workbench/en/.">http://dev.mysql.com/doc/workbench/en/.</a></p>
<h2>AUTHOR</h2>
<p> Oracle Corporation (<a rel="nofollow" href="http://dev.mysql.com/">http://dev.mysql.com/</a>). </p>
<h2>Index</h2>
