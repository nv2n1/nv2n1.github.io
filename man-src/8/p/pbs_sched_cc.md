---
title: "pbs_sched_cc(8)"
name: "pbs_sched_cc"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pbs_sched_cc/"
description: "pbs_sched_cc – pbs C scheduler"
---

<p>pbs_sched_cc &#8211; pbs C scheduler</p>
<h2>Synopsis</h2>
<p>pbs_sched [-a alarm] [-d home] [-L logfile] [-p file] [-S port] [-R port] [-c file]</p>
<h2>Description</h2>
<p>The <code>pbs_sched</code> program runs in conjunction with the PBS server. It queries the server about the state of PBS and communicates with <code>pbs_resmon</code> to get information about the status of running jobs, memory available etc. It then makes decisions as to what jobs to run. </p>
<p> pbs_sched must be executed with root permission.</p>
<h2>Options</h2>
<dl>
<dt>-a alarm</p>
<dd>This specifies the time in seconds to wait for a schedule run to finish. If a script takes too long to finish, an alarm signal is sent, and the scheduler is restarted. If a core file does not exist in the current directory, <code>abort()</code> is called and a core file is generated. The default for <i>alarm</i> is 180 seconds.</p>
<dt>-d home</p>
<dd>This specifies the PBS home directory, PBS_HOME. The current working directory of the scheduler is PBS_HOME/sched_priv. If this option is not given, PBS_HOME defaults to $PBS_SERVER_HOME as defined during the PBS build procedure.</p>
<dt>-L logfile</p>
<dd>Specifies an absolute path name of the file to use as the log file. If not specified, the scheduler will open a file named for the current date in the PBS_HOME/sched_logs directory (see the -d option).</p>
<dt>-p file</p>
<dd>This specifies the &quot;print&quot; file. Any output from the C code which is written to standard out or standard error will be written to this file. If this option is not given, the file used will be <i>PBS_HOME/sched_priv/sched_out .</i> See the <i> </i><font SIZE="-1"><i> option.</p>
<dt>-S port</p>
<dd>This specifies the port to use. If this option is not given, the default port for the PBS scheduler is used.</p>
<dt>-R port</p>
<dd>This specifies the resource monitor port to use. If this option is not given, the default port for the PBS mom is used. NOTE: this option only makes the mom port available to the scheduler writer. It doesn&#8217;t force them to use it.</p>
<dt>-c file</p>
<dd>Specify a configuration file, see description below. If this is a relative file name it will be relative to PBS_HOME/sched_priv, see the -d option. If the -c option is not supplied, pbs_sched will not attempt to open a configuration file.</dl>
<p> The options that specify file names may be absolute or relative. If they are relative, their root directory will be PBS_HOME/sched_priv. </p>
<p> </i></font></p>
<h2>Usage</h2>
<p>This version of the scheduler requires knowledge of the C language and the PBS API. Source code is provided for a main program for the scheduler. The site must supply the heart of the program. When invoked, the main program performs general initialization and housekeeping chores. Then a locally supplied function, <i>schedinit()</i> is called to perform site specific initialization. </p>
<p> In the main loop, a locally supplied function, <i>schedule()</i> is called to make the scheduling decisions and perform any required actions. Information about jobs and queues is obtained from the Server through the standard PBS API as found in libifl.a. Information about the execution host(s) is obtained from the Resource Monitor. Routines to communicate with the Resource Monitor are found in libnet.a. </p>
<p> If the processing takes more than the allotted time, the scheduler will restart itself. The default amount of time is three minutes. This can be changed with the -a option. </p>
<p> On receipt of a SIGHUP signal, the scheduler will close and reopen its log file and reread its configuration file (if any).</p>
<h2>Configuration File</h2>
<p>A configuration file may be specified with the -c option. This file may be used to specify the hosts (servers) which are allowed to connect to pbs_sched. The hosts are specified in the configuration file in a manor identical to that used in pbs_mom.</p>
<dl>
<dt>clienthost</p>
<dd>One or more servers, one per line, may be specified:</p>
<dd><code> +.IP restricted Allows connections from non-priviledged ports on the named hosts. Typically only used with Mac OSX:</p>
<dd>
<dd>Two host names are always allowed to connection to pbs_sched, &quot;localhost&quot; and the name returned to pbs_sched by the system call gethostname(). These names need not be specified in the configuration file.</dl>
<p> The configuration file must be &quot;secure&quot;. It must be owned by a user id and group id less than 10 and not be world writable. </p>
<p> </code></p>
<h2>Files</h2>
<dl>
<dt>$PBS_SERVER_HOME/sched_priv</p>
<dd>the default directory for configuration files, typically (/usr/spool/pbs)/sched_priv.</dl>
<h2>Signal Handling</h2>
<p>A C based scheduler will handle the following signals:</p>
<dl>
<dt>SIGHUP</p>
<dd>The server will close and reopen its log file and reread the config file if one exists.</p>
<dt>SIGALRM</p>
<dd>If the site supplied scheduling module exceeds the time limit, the Alarm will cause the scheduler to attempt to core dump and restart itself.</p>
<dt>SIGINT and SIGTERM</p>
<dd>Will result in an orderly shutdown of the scheduler.</dl>
<p> All other signals have the default action installed.</p>
<h2>Exit Status</h2>
<p>Upon normal termination, an exit status of zero is returned.</p>
<h2>See Also</h2>
<p><a href="//www.systutorials.com/docs/linux/man/8B-pbs_sched_tcl/">pbs_sched_tcl</a>(8B), <a href="//www.systutorials.com/docs/linux/man/8B-pbs_server/">pbs_server</a>(8B), and <a href="//www.systutorials.com/docs/linux/man/8B-pbs_mom/">pbs_mom</a>(8B).<br />
 PBS Internal Design Specification </p>
