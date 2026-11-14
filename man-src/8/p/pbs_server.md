---
title: "pbs_server(8)"
name: "pbs_server"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pbs_server/"
description: "pbs_server – start a pbs batch server"
---

<p>pbs_server &#8211; start a pbs batch server</p>
<h2>Synopsis</h2>
<p>pbs_server&nbsp;<wbr>[-a active] [-c] [-d config_path]&nbsp;<wbr>[-e] [-f] [-h] [-l port] [-p port] [-t type] [-v] [-A acctfile] [-D] [-H hostname] [-L logfile] [-M mom_port] [-R momRPP_port] [-S scheduler_port] [&#8211;about] [&#8211;ha] [&#8211;help] [&#8211;version]</p>
<h2>Description</h2>
<p>The <code>pbs_server</code> command starts the operation of a batch server on the local host. Typically, this command will be in a local boot file such as <i>/etc/rc.local .</i> If the batch server is already in execution, <code>pbs_server</code> will exit with an error. To insure that the <code>pbs_server</code> command is not runnable by the general user community, the server will only execute if its real and effective uid is zero. </p>
<p> The server will record a diagnostic message in a log file for any error occurrence. The log files are maintained in the server_logs directory below the home directory of the server. If the log file cannot be opened, the diagnostic message is written to the system console.</p>
<h2>Options</h2>
<dl>
<dt>-a active</p>
<dd>Specifies if scheduling is active or not. This sets the server attribute <i> </i><font SIZE="-1"><i> If the option argument is &quot;true&quot; (&quot;True&quot;, &quot;t&quot;, &quot;T&quot;, or &quot;1&quot;), the server is </i><code>active</code> and the PBS job scheduler will be called. If the argument is &quot;false&quot; (&quot;False&quot;, &quot;f&quot;, &quot;F&quot;, or &quot;0), the server is <code>idle</code>, and the scheduler will not be called and no jobs will be run. If this option is not specified, the server will retain the prior value of the <i> </i></font><font SIZE="-2"><i> attribute.</p>
<dt>-c</p>
<dd>Wait 10 minutes before contacting moms. Any mom reporting in does not get pinged if starting </i><code>pbs_server</code> before moms.</p>
<dt>-d config_path</p>
<dd>Specifies the path of the directory which is home to the servers configuration files, PBS_HOME. A host may have multiple servers. Each server must have a different configuration directory. The default configuration directory is given by the symbol $PBS_SERVER_HOME which is typically <code></p>
<dt>-e</p>
<dd>Accept status update from any mom. Adds node to nodes file.</p>
<dt>-f</p>
<dd>Force overwrite of server database.</p>
<dt>-h</p>
<dd>Print help information.</p>
<dt>-l scheduler_port</p>
<dd>Specifies the host name and port number of listening schedulers. By default pbs_server communicates to the scheduler on the loop back address at port 15004. If the scheduler and pbs_server are not on the same host the -l option tells pbs_server where to find the scheduler. When using TORQUE in high availability mode the -l option should be used to let TORQUE know where all potential schedulers are located. If pbs_server and the scheduler are not on the same node the -l option or the -S option must be used in order for TORQUE to communicate with the scheduler.</p>
<dt>-p port</p>
<dd>Specifies the port number on which the server will listen for batch requests. If multiple servers are running on a single host, each must have its own unique port number. This option is for use in testing with multiple batch systems on a single host.</p>
<dt>-t type</p>
<dd>Specifies the impact on jobs which were in execution, running, when the server shut down. If the running job is not rerunnable or restartable from a checkpoint image, the job is aborted. If the job is rerunnable or restartable, then the actions described below are taken. When the </code><i> argument is:</p>
<dl>
<dd>
<dl>
<dt>hot</p>
<dd>All jobs are requeued except non-rerunnable jobs that were executing. Any rerunnable job which was executing when the server went down will be run immediately. This returns the server to the same state as when it went down. After those jobs are restarted, then normal scheduling takes place for all remaining queued jobs.</p>
<dd>If a job cannot be restarted immediately because of a missing resource, such as a node being down, the server will attempt to restart it periodically for upto 5 minutes. After that period, the server will revert to a normal state, as if warm started, and will no longer attempt to restart any remaining jobs which were running prior to the shutdown.</p>
<dt>warm</p>
<dd>All rerunnable jobs which were running when the server went down are requeued. All other jobs are maintained. New selections are made for which jobs are placed into execution. Warm is the default if -t is not specified.</p>
<dt>cold</p>
<dd>All jobs are deleted. Positive confirmation is required before this direction is accepted.</p>
<dt>create</p>
<dd>The server will discard any existing configuration files, queues and jobs, and initialize configuration files to the default values. The server is idled.</dl>
</dl>
<dt>-v</p>
<dd>Shows version.</p>
<dt>-A acctfile</p>
<dd>Specifies an absolute path name of the file to use as the accounting file. If not specified, the file is named for the current date in the PBS_HOME/server_priv/accounting directory.</p>
<dt>-D</p>
<dd>Debug mode.</p>
<dt>-H hostname</p>
<dd>Causes the server to start under a different hostname as obtained from <a href="/docs/linux/man/2-gethostname/">gethostname</a>(2). Useful for servers with multiple network interfaces to support connections from clients over an interface that has a hostname assigned that differs from the one that is returned by <a href="/docs/linux/man/2-gethostname/">gethostname</a>(2).</p>
<dt>-L logfile</p>
<dd>Specifies an absolute path name of the file to use as the log file. If not specified, the file is one named for the current date in the PBS_HOME/server_logs directory, see the </i></font><font SIZE="-3"><i> option.</p>
<dt>-M mom_port</p>
<dd>Specifies the host name and/or port number on which the server should connect the job executor, MOM. The option argument, is one of the forms: host_name, [:]port_number, or host_name:port_number. If host_name not specified, the local host is assumed. If port_number is not specified, the default port is assumed. See the -M option for <a href="/docs/linux/man/8-pbs_mom/">pbs_mom</a>(8).</p>
<dt>-R mom_RPPport</p>
<dd>Specifies the port number on which the the server should query the up/down status of Mom. See the -R option for <a href="/docs/linux/man/8-pbs_mom/">pbs_mom</a>(8).</p>
<dt>-S scheduler_port</p>
<dd>Specifies the port number to which the server should connect when contacting the Scheduler. By default pbs_server looks for the scheduler on the loopback address at port 15004. The -S option changes the default to the value given in the option argument. The option argument, is of the same syntax as under the -M option.</p>
<dt>&#8211;about</p>
<dd>Shows information about </i><code>pbs_server.</code></p>
<dt>&#8211;ha</p>
<dd>Enables high availability mode.</p>
<dt>&#8211;help</p>
<dd>Prints help information.</p>
<dt>&#8211;version</p>
<dd>Shows version and commit information.</dl>
<p> </font></p>
<h2>Files</h2>
<dl>
<dt>$PBS_SERVER_HOME/server_priv</p>
<dd>default directory for configuration files, typically /usr/spool/pbs/server_priv</p>
<dt>$PBS_SERVER_HOME/server_logs</p>
<dd>directory for log files recorded by the server.</dl>
<h2>Signal Handling</h2>
<p>On receipt of the following signals, the server performs the defined action:</p>
<dl>
<dt>SIGHUP</p>
<dd>The current server log and accounting log are closed and reopened. This allows for the prior log to be renamed and a new log started from the time of the signal.</p>
<dt>SIGINT</p>
<dd>Causes an orderly shutdown of pbs_server.</p>
<dt>SIGUSR1, SIGUSR2</p>
<dd>Causes server to increase and decrease logging levels, respectively.</p>
<dt>SIGTERM</p>
<dd>Causes an orderly shutdown of pbs_server.</p>
<dt>SIGSHUTDN</p>
<dd>On systems (Unicos) where SIGSHUTDN is defined, it also causes an orderly shutdown of the server.</p>
<dt>SIGPIPE</p>
<dd>This signal is ignored.</dl>
<p> All other signals have their default behavior installed.</p>
<h2>Exit Status</h2>
<p>If the server command fails to begin batch operation, the server exits with a value greater than zero.</p>
<h2>See Also</h2>
<p>qsub (1B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_connect/">pbs_connect</a>(3B), <a href="//www.systutorials.com/docs/linux/man/8B-pbs_mom/">pbs_mom</a>(8B), <a href="//www.systutorials.com/docs/linux/man/8B-pbs_sched_basl/">pbs_sched_basl</a>(8B), <a href="//www.systutorials.com/docs/linux/man/8B-pbs_sched_tcl/">pbs_sched_tcl</a>(8B), <a href="//www.systutorials.com/docs/linux/man/8B-pbsnodes/">pbsnodes</a>(8B), <a href="//www.systutorials.com/docs/linux/man/8B-qdisable/">qdisable</a>(8B), <a href="//www.systutorials.com/docs/linux/man/8B-qenable/">qenable</a>(8B), <a href="//www.systutorials.com/docs/linux/man/1B-qmgr/">qmgr</a>(1B), <a href="//www.systutorials.com/docs/linux/man/8B-qrun/">qrun</a>(8B), <a href="//www.systutorials.com/docs/linux/man/8B-qstart/">qstart</a>(8B), <a href="//www.systutorials.com/docs/linux/man/8B-qstop/">qstop</a>(8B), <a href="//www.systutorials.com/docs/linux/man/8B-qterm/">qterm</a>(8B), and the PBS External Reference Specification. </p>
