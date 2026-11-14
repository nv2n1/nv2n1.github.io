---
title: "mysqlrpladmin(1)"
name: "mysqlrpladmin"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mysqlrpladmin/"
description: "mysqlrpladmin – Administration utility for MySQL replication"
---

<h2 class="name">NAME</h2>
<p> mysqlrpladmin &#8211; Administration utility for MySQL replication </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mysqlrpladmin [</code><i>options</i><code>]</code></dl>
<h2>DESCRIPTION</h2>
<dd>This utility permits users to perform administrative actions on a replication topology consisting of a master and its slaves. The utility is designed to make it easy to recover from planned maintenance of the master or from an event that takes the master offline unexpectedly. </p>
<p> The act of taking the master offline intentionally and switching control to another slave is called switchover. In this case, there is no loss of transactions as the master is locked and all slaves are allowed to catch up to the master. Once the slaves have read all events from the master, the master is shutdown and control switched to a slave (in this case called a candidate slave). </p>
<p> Recovering from the loss of a downed master is more traumatic and since there is no way to know what transactions the master may have failed to send, the new master (called a candidate slave) must be the slave that is most up-to-date. How this is determined depends on the version of the server (see below). However, it can result in the loss of some transactions that were executed on the downed master but not sent. The utility accepts a list of slaves to be considered the candidate slave. If no slave is found to meet the requirements, the operation will search the list of known slaves. </p>
<p> The utility also provides a number of useful commands for managing a replication topology including the following. </p>
<p> <code>elect</code> This command is available to only those servers supporting global transaction identifiers (GTIDs), perform best slave election and report best slave to use in the event a switchover or failover is required. Best slave election is simply the first slave to meet the prerequisites. GTIDs are supported in version 5.6.5 and higher. This command requires the options <code>&#8211;master</code> and either <code>&#8211;slaves</code> or <code>&#8211;discover-slaves-login</code>. </p>
<p> <code>failover</code> This command is available to only those servers supporting GTIDs. Conduct failover to the best slave. The command will test each candidate slave listed for the prerequisites. Once a candidate slave is elected, it is made a slave of each of the other slaves thereby collecting any transactions executed on other slaves but not the candidate. In this way, the candidate becomes the most up-to-date slave. This command requires the <code>&#8211;slaves</code> option. The <code>&#8211;discover-slaves-login</code> option is not allowed because, for failover, the master is presumed to be offline or otherwise unreachable (so there is no way to discover the slaves). The <code>&#8211;master</code> option is ignored for this command. </p>
<p> <code>gtid</code> This command is available to only those servers supporting GTIDs. It displays the contents of the GTID variables, @@GLOBAL.GTID_EXECUTED, @@GLOBAL.GTID_PURGED, and @@GLOBAL.GTID_OWNED. The command also displays universally unique identifiers (UUIDs) for all servers. This command requires one of the following combinations: <code>&#8211;master</code> and <code>&#8211;slaves</code>, or <code>&#8211;master</code> and <code>&#8211;discover-slaves-login</code>. </p>
<p> <code>health</code> Display the replication health of the topology. By default, this includes the host name, port, role (MASTER or SLAVE) of the server, state of the server (UP = is connected, WARN = not connected but can ping, DOWN = not connected and cannot ping), the GTID_MODE, and health state. This command requires one of the following combinations: </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;master</code> and <code>&#8211;slaves</code>;</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;master</code> and <code>&#8211;discover-slaves-login</code>;</dl>
<p> The master health state is based on the following; if GTID_MODE=ON, the server must have binary log enabled, and there must exist a user with the REPLICATE SLAVE privilege. </p>
<p> The slave health state is based on the following; the IO_THREAD and SQL_THREADS must be running, it must be connected to the master, there are no errors, the slave delay for non-gtid enabled scenarios is not more than the threshold provided by the <code>&#8211;max-position</code> and the slave is reading the correct master log file, and slave delay is not more than the <code>&#8211;seconds-behind</code> threshold option. </p>
<p> <code>reset</code> Execute the STOP SLAVE and RESET SLAVE commands on all slaves. This command requires the <code>&#8211;slaves</code> option. The <code>&#8211;discover-slaves-login</code> option is not allowed because it might not provide the expected result, excluding slaves with the IO thread stopped. Optionally, the <code>&#8211;master</code> option can also be used and in this case the utility will perform an additional check to verify if the specified slaves are associated (i.e. replication configured) to the given master. </p>
<p> <code>start</code> Execute the START SLAVE command on all slaves. This command requires the <code>&#8211;slaves</code> option. The <code>&#8211;discover-slaves-login</code> option is not allowed because it might not provide the expected result, excluding slaves with the IO thread stopped. Optionally, the <code>&#8211;master</code> option can also be used and in this case the utility will perform an additional check to verify if the specified slaves are associated (i.e. replication configured) to the given master. </p>
<p> <code>stop</code> Execute the STOP SLAVE command on all slaves. This command requires the <code>&#8211;slaves</code> option. The <code>&#8211;discover-slaves-login</code> option is not allowed because it might not provide the expected result, excluding slaves with the IO thread stopped. Optionally, the <code>&#8211;master</code> option can also be used and in this case the utility will perform an additional check to verify if the specified slaves are associated (i.e. replication configured) to the given master. </p>
<p> <code>switchover</code> Perform slave promotion to a specified candidate slave as designated by the <code>&#8211;new-master</code> option. This command is available for both gtid-enabled servers and non-gtid-enabled scenarios. This command requires one of the following combinations: </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;master</code>, <code>&#8211;new-master</code> and <code>&#8211;slaves</code>;</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;master</code>, <code>&#8211;new-master</code> and <code>&#8211;discover-slaves-login</code>;</dl>
<p> Detection of a downed master is performed as follows. If the connection to the master is lost, wait <code>&#8211;ping</code> seconds and check again. If the master connection is lost and the master cannot be pinged or reconnected, the failover event occurs. </p>
<p> For all commands that require specifying multiple servers, the options require a comma-separated list of connection parameters in the following form (where the password, port, and socket are optional).: </p>
<dl>
<dt>
<dd>
<pre><code>
&lt;*user*&gt;[:&lt;*passwd*&gt;]@&lt;*host*&gt;[:&lt;*port*&gt;][:&lt;*socket*&gt;] or
&lt;*login-path*&gt;[:&lt;*port*&gt;][:&lt;*socket*&gt;]
</code></pre>
</dl>
<p> The utility permits users to discover slaves connected to the master. In order to use the discover slaves feature, all slaves must use the &#8211;report-host and &#8211;report-port startup variables to specify the correct hostname and ip port of the slave. If these are missing or report the incorrect information, the slaves health may not be reported correctly or the slave may not be listed at all. The discover slaves feature ignores any slaves it cannot connect to or with the IO thread stopped (i.e. not connected to the master). </p>
<p> The utility permits the user to demote a master to a slave during the switchover operation. The <code>&#8211;demote-master</code> option tells the utility to, once the new master is established, make the old master a slave of the new master. This permits rotation of the master role among a set of servers. </p>
<p> The utility permits the user to specify an external script to execute before and after the switchover and failover commands. The user can specify these with the <code>&#8211;exec-before</code> and <code>&#8211;exec-after</code> options. The return code of the script is used to determine success thus each script must report 0 (success) to be considered successful. If a script returns a value other than 0, the result code is presented in an error message. </p>
<p> The utility permits the user to log all actions taken during the commands. The <code>&#8211;log</code> option requires a valid path and file name of the file to use for logging operations. The log is active only when this option is specified. The option <code>&#8211;log-age</code> specifies the age in days that log entries are kept. The default is seven (7) days. Older entries are automatically deleted from the log file (but only if the <code>&#8211;log</code> option is specified). </p>
<p> The format of the log file includes the date and time of the event, the level of the event (informational &#8211; INFO, warning &#8211; WARN, error &#8211; ERROR, critical failure &#8211; CRITICAL), and the message reported by the utility. </p>
<p> The utility has a number of options each explained in more detail below. Some of the options are specific to certain commands. Warning messages are issued whenever an option is used that does not apply to the command requested. A brief overview of each command and its options is presented in the following paragraphs. </p>
<p> The start, stop, and reset commands require the <code>&#8211;slaves</code> option to list all of the slaves in the topology. Optionally, the <code>&#8211;master</code> option can be specified for the utility to check if the specified slaves are associated to the given master before executing the command, making sure that the command is only applied to slaves connected to the right replication master. </p>
<p> The options required for the elect, health and gtid commands include the <code>&#8211;master</code> option to specify the existing master, and either the <code>&#8211;slaves</code> option to list all of the slaves in the topology or the <code>&#8211;discover-slaves-login</code> option to provide the user name and password to discover any slaves in the topology that are registered and connected to the master. </p>
<p> The options required for switchover include the <code>&#8211;master</code> option to specify the existing master, the <code>&#8211;new-master</code> option to specify the candidate slave (the slave to become the new master), and either the <code>&#8211;slaves</code> option to list the considered slaves in the topology or the <code>&#8211;discover-slaves-login</code> option to provide the user name and password to discover any slaves in the topology that are registered and connected to the master. </p>
<p> The failover command requires only the <code>&#8211;slaves</code> option to explicitly list all of the slaves in the topology because it is expected that the master is down when this command is used. </p>
<p> Use the <code>&#8211;verbose</code> option to see additional information in the health report and additional messages during switchover or failover.<br />
OPTIONS </p>
<p> <code>mysqlrpladmin</code> accepts the following command-line options: </p>
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
<dd> &bull; &#8211;demote-master </p>
<p> Make master a slave after switchover.</dl>
<dl>
<dt>
<dd> &bull; &#8211;discover-slaves-login=&lt;slave_login&gt; </p>
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
<dd> &bull; &#8211;force </p>
<p> Ignore prerequisite checks or any inconsistencies found (e.g. errant transactions on the slaves or SQL thread errors) forcing the execution of the specified command. This option need to be used carefully as it will not solve any detected issue, but will only ignore them displaying a warning message.</dl>
<dl>
<dt>
<dd> &bull; &#8211;format=&lt;format&gt;, -f &lt;format&gt; </p>
<p> Display the replication health output in either grid (default), tab, csv, or vertical format.</dl>
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
<dd> &bull; &#8211;new-master=&lt;connection&gt; </p>
<p> Connection information for the slave to be used to replace the master for switchover in the form: &lt;<i>user</i>&gt;[:&lt;<i>passwd</i>&gt;]@&lt;<i>host</i>&gt;[:&lt;<i>port</i>&gt;][:&lt;<i>socket</i>&gt;] or &lt;<i>login-path</i>&gt;[:&lt;<i>port</i>&gt;][:&lt;<i>socket</i>&gt;]. Valid only with switchover command.</dl>
<dl>
<dt>
<dd> &bull; &#8211;no-health </p>
<p> Turn off health report after switchover or failover.</dl>
<dl>
<dt>
<dd> &bull; &#8211;ping=&lt;number&gt; </p>
<p> Number of ping attempts for detecting downed server. Note: on some platforms this is the same as number of seconds to wait for <i>ping</i> to return. This value is also used to check down status of master. Failover will wait <i>ping</i> seconds to check master response. If no response, failover event occurs.</dl>
<dl>
<dt>
<dd> &bull; &#8211;quiet, -q </p>
<p> Turn off all messages for quiet execution.</dl>
<dl>
<dt>
<dd> &bull; &#8211;rpl-user=&lt;replication_user&gt; </p>
<p> The user and password for the replication user requirement, in the format: &lt;<i>user</i>&gt;[:&lt;<i>password</i>&gt;] or &lt;<i>login-path</i>&gt;. E.g. rpl:passwd Default = None.</dl>
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
<p> Maximum timeout in seconds to wait for each replication command to complete. For example, timeout for slave waiting to catch up to master. Default = 300 seconds.</dl>
<dl>
<dt>
<dd> &bull; &#8211;verbose, -v </p>
<p> Specify how much information to display. Use this option multiple times to increase the amount of information. For example, <code>-v</code> = verbose, <code>-vv</code> = more verbose, <code>-vvv</code> = debug.</dl>
<dl>
<dt>
<dd> &bull; &#8211;version </p>
<p> Display version information and exit.</dl>
<p>NOTES </p>
<p> The login user must have the appropriate permissions to execute <code>SHOW SLAVE STATUS</code>, <code>SHOW MASTER STATUS</code>, and <code>SHOW VARIABLES</code> on the appropriate servers as well as grant the REPLICATE SLAVE privilege. The utility checks permissions for the master, slaves, and candidates at startup. </p>
<p> Mixing IP and hostnames is not recommended. The replication-specific utilities will attempt to compare hostnames and IP addresses as aliases for checking slave connectivity to the master. However, if your installation does not support reverse name lookup, the comparison could fail. Without the ability to do a reverse name lookup, the replication utilities could report a false negative that the slave is (not) connected to the master. </p>
<p> For example, if you setup replication using MASTER_HOST=ubuntu.net on the slave and later connect to the slave with mysqlrplcheck and have the master specified as &#8211;master=192.168.0.6 using the valid IP address for ubuntu.net, you must have the ability to do a reverse name lookup to compare the IP (192.168.0.6) and the hostname (ubuntu.net) to determine if they are the same machine. </p>
<p> Similarly, if you use localhost to connect to the master, the health report may not show all of the slaves. It is best to use the actual hostname of the master when connecting or setting up replication. </p>
<p> If the user does not specify the <code>&#8211;rpl-user </code> and the user has specified the switchover or failover command, the utility will check to see if the slaves are using &#8211;master-info-repository=TABLE. If they are not, the utility will stop with an error. </p>
<p> All the commands require either the <code>&#8211;slaves</code> or <code>&#8211;discover-slaves-login</code> option but both cannot be used at the same time. In fact, some commands only allow the use of the <code>&#8211;slaves</code> option which is safer to specify the list slaves, because <code>&#8211;discover-slaves-login</code> might not provide an up to date list of available slaves. </p>
<p> The path to the MySQL client tools should be included in the PATH environment variable in order to use the authentication mechanism with login-paths. This will allow the utility to use the my_print_defaults tools which is required to read the login-path values from the login configuration file (.mylogin.cnf).<br />
EXAMPLES </p>
<p> To perform best slave election for a topology with GTID_MODE=ON (server version 5.6.5 or higher) where all slaves are specified with the <code>&#8211;slaves</code> option, run the following command.: </p>
<dl>
<dt>
<dd>
$ mysqlrpladmin&#8211; master = root[at] localhost : 3331 &#8211;slaves = root[at] localhost : 3332, root[at] localhost : 3333, root[at] localhost : 3334 elect<br />
#Electing candidate slave from known slaves.<br />
#Best slave found is located on localhost : 3332.<br />
#&#8230; done.
</dl>
<p> To perform best slave election supplying a candidate list, use the following command.: </p>
<dl>
<dt>
<dd>
$ mysqlrpladmin&#8211; master = root[at] localhost : 3331 &#8211;slaves = root[at] localhost : 3332, root[at] localhost : 3333, root[at] localhost : 3334 &#8211;candidates = root[at] localhost : 3333, root[at] localhost : 3334 elect<br />
#Electing candidate slave from candidate list then slaves list.<br />
#Best slave found is located on localhost : 3332.<br />
#&#8230; done.
</dl>
<p> To perform failover after a master has failed, use the following command.: </p>
<dl>
<dt>
<dd>
$ mysqlrpladmin&#8211; slaves = root[at] localhost : 3332, root[at] localhost : 3333, root[at] localhost : 3334 &#8211;candidates = root[at] localhost : 3333, root[at] localhost : 3334 failover<br />
#Performing failover.<br />
#Candidate slave localhost : 3333 will become the new master.<br />
#Preparing candidate for failover.<br />
#Creating replication user if it does not exist.<br />
#Stopping slaves.<br />
#Performing STOP on all slaves.<br />
#Switching slaves to new master.<br />
#Starting slaves.<br />
#Performing START on all slaves.<br />
#Checking slaves for errors.<br />
#Failover complete.<br />
#&#8230; done.
</dl>
<p> To see the replication health of a topology with GTID_MODE=ON (server version 5.6.5 or higher) and discover all slaves attached to the master, run the following command. We use the result of the failover command above.: </p>
<dl>
<dt>
<dd>
$ mysqlrpladmin&#8211; master = root[at] localhost : 3333 &#8211;slaves = root[at] localhost : 3332, root[at] localhost : 3334 health<br />
#Getting health for master : localhost : 3333.<br />
#<br />
#Replication Topology Health:<br />
                                                                                                   + &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; -+ |<br />
                                                                                               host | port | role | state | gtid_mode | health |<br />
                                                                                               +&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; -+ | localhost | 3333 | MASTER | UP | ON | OK |<br />
                                                                                               | localhost | 3332 | SLAVE | UP | ON | OK |<br />
                                                                                               | localhost | 3334 | SLAVE | UP | ON | OK |<br />
                                                                                               +&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; -+<br />
#&#8230; done.
</dl>
<p> To view a detailed replication health report but with all of the replication health checks revealed, use the <code>&#8211;verbose</code> option as shown below. In this example, we use vertical format to make viewing easier.: </p>
<dl>
<dt>
<dd>
$ mysqlrpladmin&#8211; master = root[at] localhost : 3331 &#8211;slaves = root[at] localhost : 3332, root[at] localhost : 3333, root[at] localhost : 3334 &#8211;verbose health<br />
#Getting health for master : localhost : 3331.<br />
#Attempting to contact localhost&#8230; Success<br />
#Attempting to contact localhost&#8230; Success<br />
#Attempting to contact localhost&#8230; Success<br />
#Attempting to contact localhost&#8230; Success<br />
#<br />
#Replication Topology Health:<br />
                                                                                                                                  ************************ *<br />
                                                                                                                              1. row *************************host : localhost port : 3331 role : MASTER state : UP gtid_mode : ON health : OK version : 5.6.5 &#8211;<br />
                                                                                                                          m8 &#8211; debug &#8211; log master_log_file : mysql &#8211; bin .000001 master_log_pos : 571 IO_Thread : SQL_Thread : Secs_Behind : Remaining_Delay : IO_Error_Num : IO_Error : *************************2. row *************************host : localhost port : 3332 role : SLAVE state : UP gtid_mode : ON health : OK version : 5.6.5 &#8211; m8 &#8211; debug &#8211; log master_log_file : mysql &#8211; bin .000001 master_log_pos : 571 IO_Thread : Yes SQL_Thread : Yes Secs_Behind : 0 Remaining_Delay : No IO_Error_Num : 0 IO_Error : *************************3. row *************************host : localhost port : 3333 role : SLAVE state : UP gtid_mode : ON health : OK version : 5.6.5 &#8211; m8 &#8211; debug &#8211; log master_log_file : mysql &#8211; bin .000001 master_log_pos : 571 IO_Thread : Yes SQL_Thread : Yes Secs_Behind : 0 Remaining_Delay : No IO_Error_Num : 0 IO_Error : *************************4. row *************************host : localhost port : 3334 role : SLAVE state : UP gtid_mode : ON health : OK version : 5.6.5 &#8211; m8 &#8211; debug &#8211; log master_log_file : mysql &#8211; bin .000001 master_log_pos : 571 IO_Thread : Yes SQL_Thread : Yes Secs_Behind : 0 Remaining_Delay : No IO_Error_Num : 0 IO_Error : 4 rows.<br />
#&#8230; done.
</dl>
<p> To run the same failover command above, but specify a log file, use the following command.: </p>
<dl>
<dt>
<dd>
$ mysqlrpladmin&#8211; slaves = root[at] localhost : 3332, root[at] localhost : 3333, root[at] localhost : 3334 &#8211;candidates = root[at] localhost : 3333, root[at] localhost : 3334 &#8211;log = test_log.txt failover<br />
#Performing failover.<br />
#Candidate slave localhost : 3333 will become the new master.<br />
#Preparing candidate for failover.<br />
#Creating replication user if it does not exist.<br />
#Stopping slaves.<br />
#Performing STOP on all slaves.<br />
#Switching slaves to new master.<br />
#Starting slaves.<br />
#Performing START on all slaves.<br />
#Checking slaves for errors.<br />
#Failover complete.<br />
#&#8230; done.
</dl>
<p> After this command, the log file will contain entries like the following: </p>
<dl>
<dt>
<dd>
<pre>
2012-03-19 14:44:17 PM INFO Executing failover command...
2012-03-19 14:44:17 PM INFO Performing failover.
2012-03-19 14:44:17 PM INFO Candidate slave localhost:3333 will become the new master.
2012-03-19 14:44:17 PM INFO Preparing candidate for failover.
2012-03-19 14:44:19 PM INFO Creating replication user if it does not exist.
2012-03-19 14:44:19 PM INFO Stopping slaves.
2012-03-19 14:44:19 PM INFO Performing STOP on all slaves.
2012-03-19 14:44:19 PM INFO Switching slaves to new master.
2012-03-19 14:44:20 PM INFO Starting slaves.
2012-03-19 14:44:20 PM INFO Performing START on all slaves.
2012-03-19 14:44:20 PM INFO Checking slaves for errors.
2012-03-19 14:44:21 PM INFO Failover complete.
2012-03-19 14:44:21 PM INFO ...done.
</pre>
</dl>
<p> To perform switchover and demote the current master to a slave, use the following command.: </p>
<dl>
<dt>
<dd>
$ mysqlrpladmin&#8211; master = root[at] localhost : 3331 &#8211;slaves = root[at] localhost : 3332, root[at] localhost : 3333, root[at] localhost : 3334 &#8211;new &#8211; master = root[at] localhost : 3332 &#8211;demote &#8211; master switchover<br />
#Performing switchover from master at localhost : 3331 to slave at localhost : 3332.<br />
#Checking candidate slave prerequisites.<br />
#Waiting for slaves to catch up to old master.<br />
#Stopping slaves.<br />
#Performing STOP on all slaves.<br />
#Demoting old master to be a slave to the new master.<br />
#Switching slaves to new master.<br />
#Starting all slaves.<br />
#Performing START on all slaves.<br />
#Checking slaves for errors.<br />
#Switchover complete.<br />
#&#8230; done.
</dl>
<p> If the replication health report is generated on the topology following the above command, it will display the old master as a slave as shown below.: </p>
<dl>
<dt>
<dd>
#Replication Topology Health:<br />
+ &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; -+ | host | port | role | state | gtid_mode | health |<br />
    +&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; -+ | localhost | 3332 | MASTER | UP | ON | OK |<br />
    | localhost | 3331 | SLAVE | UP | ON | OK |<br />
    | localhost | 3333 | SLAVE | UP | ON | OK |<br />
    | localhost | 3334 | SLAVE | UP | ON | OK |<br />
    +&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; -+
</dl>
<p> You can use the discover slaves feature, if and only if all slaves report their host and port to the master. A sample command to generate a replication health report with discovery is shown below. Note that the option <code>&#8211;discover-slaves-login</code> cannot be used in conjunction with the <code>&#8211;slaves</code> option.: </p>
<dl>
<dt>
<dd>
<pre><code>
$ mysqlrpladmin-- master = root[at] localhost : 3332 --discover - slaves - login = root health
#Discovering slaves for master at localhost : 3332
#Discovering slave at localhost : 3331
#Found slave : localhost : 3331
#Discovering slave at localhost : 3333
#Found slave : localhost : 3333
#Discovering slave at localhost : 3334
#Found slave : localhost : 3334
#Checking privileges.
#
#Replication Topology Health:
                                                                                       + -- -- -- -- -- --+-- -- -- -+-- -- -- -- -+-- -- -- --+-- -- -- -- -- --+-- -- -- -- -+ |
                                                                                   host | port | role | state | gtid_mode | health |
                                                                                   +-- -- -- -- -- --+-- -- -- -+-- -- -- -- -+-- -- -- --+-- -- -- -- -- --+-- -- -- -- -+ | localhost | 3332 | MASTER | UP | ON | OK |
                                                                                   | localhost | 3331 | SLAVE | UP | ON | OK |
                                                                                   | localhost | 3333 | SLAVE | UP | ON | OK |
                                                                                   | localhost | 3334 | SLAVE | UP | ON | OK |
                                                                                   +-- -- -- -- -- --+-- -- -- -+-- -- -- -- -+-- -- -- --+-- -- -- -- -- --+-- -- -- -- -+
#... done.
</code></pre>
</dl>
<h2>COPYRIGHT</h2>
<h2>SEE ALSO</h2>
<p> For more information, please refer to the MySQL Utilities section of the MySQL Workbench Reference Manual, which is available online at <a rel="nofollow" href="http://dev.mysql.com/doc/workbench/en/.">http://dev.mysql.com/doc/workbench/en/.</a></p>
<h2>AUTHOR</h2>
<p> Oracle Corporation (<a rel="nofollow" href="http://dev.mysql.com/">http://dev.mysql.com/</a>). </p>
<h2>Index</h2>
