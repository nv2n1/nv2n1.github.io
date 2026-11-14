---
title: "pbs_sched_tcl(8)"
name: "pbs_sched_tcl"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pbs_sched_tcl/"
description: "pbs_sched_tcl – pbs Tcl scheduler"
---

<p>pbs_sched_tcl &#8211; pbs Tcl scheduler</p>
<h2>Synopsis</h2>
<p>pbs_sched [-a alarm] [-b file] [-d home] [-i file] [-L logfile] [-p file] [-S port] [-t file] [-v] [-c file]</p>
<h2>Description</h2>
<p>The <code>pbs_sched</code> program runs in conjunction with the PBS server. It queries the server about the state of PBS and communicates with <code>pbs_mom</code> to get information about the status of running jobs, memory available etc. It then makes decisions as to what jobs to run. </p>
<p> pbs_sched must be executed with root permission.</p>
<h2>Options</h2>
<dl>
<dt>-a alarm</p>
<dd>This specifies the time in seconds to wait for a schedule run to finish. If a script takes too long to finish, an alarm signal is sent, and the scheduler is restarted. If a core file does not exist in the current directory, <code>abort()</code> is called and a core file is generated. The default for <i>alarm</i> is 180 seconds.</p>
<dt>-b file</p>
<dd>This specifies the &quot;body&quot; file. The file given is read into memory once at program start or after the program receives a SIGHUP and executed each time the scheduler is awakened by the server. If this option is not given, the file &quot;sched_tcl&quot; in the directory PBS_HOME/sched_priv is read for the body code.</p>
<dt>-d home</p>
<dd>This specifies the PBS home directory, PBS_HOME. The current working directory of the scheduler is PBS_HOME/sched_priv. If this option is not given, PBS_HOME defaults to $PBS_SERVER_HOME as defined during the PBS build procedure.</p>
<dt>-i file</p>
<dd>This specifies the &quot;initialize&quot; file. The file given is executed once before the main processing loop is entered. If this option is not given, no initialization code is executed.</p>
<dt>-L logfile</p>
<dd>Specifies an absolute path name of the file to use as the log file. If not specified, the scheduler will open a file named for the current date in the PBS_HOME/sched_logs directory (see the -d option).</p>
<dt>-p file</p>
<dd>This specifies the &quot;print&quot; file. Any output from the Tcl code which is written to standard out or standard error will be written to this file. If this option is not given, the file used will be <i>PBS_HOME/sched_priv/sched_out.</i> See the <i> </i><font SIZE="-1"><i> option.</p>
<dt>-S port</p>
<dd>This specifies the port to use. If this option is not given, the default port for the PBS scheduler is used.</p>
<dt>-t file</p>
<dd>This specifies the &quot;terminator&quot; file. If a QUIT command is sent from the server, this code is executed before the scheduler exits. If this option is not given, no special termination handling is done.</p>
<dt>-v</p>
<dd>This puts the scheduler into &quot;verbose&quot; mode. Any errors will be shown no matter what this may be set to, but some &quot;uninteresting&quot; events may be logged by using this flag. An example is a message each time the server contacts the scheduler.</p>
<dt>-c file</p>
<dd>Specify a configuration file, see description below. If this is a relative file name it will be relative to PBS_HOME/sched_priv, see the -d option. If the -c option is not supplied, pbs_sched will not attempt to open a configuration file.</dl>
<p> The options that specify file names may be absolute or relative. If they are relative, their root directory will be PBS_HOME/sched_priv. </p>
<p> </i></font></p>
<h2>Usage</h2>
<p>This version of the scheduler requires knowledge of the Tcl language. A set of functions to communicate with the PBS server and resource monitor have been added to those normally available with Tcl. All these calls will set the Tcl variable &quot;pbs_errno&quot; to a value to indicate if an error occured. In all cases, the value &quot;0&quot; means no error. If a call to a Resource Monitor function is made, any error value will come from the system supplied <code>errno</code> variable. If the function call communicates with the PBS Server, any error value will come from the error number returned by the server.</p>
<dl>
<dt>openrm host ?port?</p>
<dd>Creates a connection to the PBS Resource Monitor on <i>host</i> using <i>port</i> as the port number or the standard port for the resource monitor if it is not given. A connection handle is returned. If the open is successful, this will be a non-negative integer. If not, an error occurred.</p>
<dt>closerm connection</p>
<dd>The parameter <i>connection</i> is a handle to a resource monitor which was previously returned from <code>openrm.</code> This connection is closed. Nothing is returned.</dl>
<dl>
<dt>downrm connection</p>
<dd>Sends a command to the connected resource monitor to shutdown. Nothing is returned.</dl>
<dl>
<dt>configrm connection filename</p>
<dd>Sends a command to the connected resource monitor to read the configuration file given by <i>filename.</i> If this is successful, a &quot;0&quot; is returned, otherwise, &quot;-1&quot; is returned.</dl>
<dl>
<dt>addreq connection request</p>
<dd>A resource request is sent to the connected resource monitor. If this is successful, a &quot;0&quot; is returned, otherwise, &quot;-1&quot; is returned.</dl>
<dl>
<dt>getreq connection</p>
<dd>One resource request response from the connected resource monitor is returned. If an error occurred or there are no more responses, an empty string is returned.</dl>
<dl>
<dt>allreq request</p>
<dd>A resource request is sent to all connected resource monitors. The number of streams acted upon is returned.</dl>
<dl>
<dt>flushreq</p>
<dd>All resource requests previously sent to all connected resource monitors are flushed out to the network. Nothing is returned.</dl>
<dl>
<dt>activereq</p>
<dd>The connection number of the next stream with something to read is returned. If there is nothing to read from any of the connections, a negative number is returned.</dl>
<dl>
<dt>fullresp flag</p>
<dd>Evaluates <i>flag</i> as a boolean value and sets the response mode used by <code>getreq</code> to <code>full</code> if <i>flag</i> evaluates to &quot;true&quot;. The full return from a resource monitor includes the original request followed by an equal sign followed by the response. The default situation is only to return the response following the equal sign. If a script needs to &quot;see&quot; the entire line, this function may be used.</dl>
<dl>
<dt>pbsstatserv</p>
<dd>The server is sent a status request for information about the server itself. If the request succeeds, a list with three elements is returned, otherwise an empty string is returned. The first element is the server&#8217;s name. The second is a list of attributes. The third is the &quot;text&quot; associated with the server (usually blank).</dl>
<dl>
<dt>pbsstatjob</p>
<dd>The server is sent a status request for information about the all jobs resident within the server. If the request succeeds, a list is returned, otherwise an empty string is returned. The list contains an entry for each job. Each element is a list with three elements. The first is the job&#8217;s jobid. The second is a list of attributes. The attribute names which specify resources will have a name of the form &quot;Resource_List:name&quot; where &quot;name&quot; is the resource name. The third is the &quot;text&quot; associated with the job (usually blank).</dl>
<dl>
<dt>pbsstatque</p>
<dd>The server is sent a status request for information about all queues resident within the server. If the request succeeds, a list is returned, otherwise an empty string is returned. The list contains an entry for each queue. Each element is a list with three elements. This first is the queue&#8217;s name. The second is a list of attributes similar to <code>pbsstatjob.</code> The third is the &quot;text&quot; associated with the queue (usually blank).</dl>
<dl>
<dt>pbsstatnode</p>
<dd>The server is sent a status request for information about all nodes defined within the server. If the request succeeds, a list is returned, otherwise an empty string is returned. The list contains an entry for each node. Each element is a list with three elements. This first is the nodes&#8217;s name. The second is a list of attributes similar to <code>pbsstatjob.</code> The third is the &quot;text&quot; associated with the node (usually blank).</dl>
<dl>
<dt>pbsselstat</p>
<dd>The server is sent a status request for information about the all runnable jobs resident within the server. If the request succeeds, a list similar to <code>pbsstatjob</code> is returned, otherwise an empty string is returned.</dl>
<dl>
<dt>pbsrunjob jobid ?location?</p>
<dd>Run the job given by <i>jobid</i> at the location given by <i>location.</i> If <i>location</i> is not given, the default location is used. If this is successful, a &quot;0&quot; is returned, otherwise, &quot;-1&quot; is returned.</dl>
<dl>
<dt>pbsasyrunjob jobid ?location?</p>
<dd>Run the job given by <i>jobid</i> at the location given by <i>location</i> without waiting for a positive response that the job has actually started. If <i>location</i> is not given, the default location is used. If this is successful, a &quot;0&quot; is returned, otherwise, &quot;-1&quot; is returned.</dl>
<dl>
<dt>pbsrerunjob jobid</p>
<dd>Re-runs the job given by <i>jobid.</i> If this is successful, a &quot;0&quot; is returned, otherwise, &quot;-1&quot; is returned.</dl>
<dl>
<dt>pbsdeljob jobid</p>
<dd>Delete the job given by <i>jobid.</i> If this is successful, a &quot;0&quot; is returned, otherwise, &quot;-1&quot; is returned.</dl>
<dl>
<dt>pbsholdjob jobid</p>
<dd>Place a hold on the job given by <i>jobid.</i> If this is successful, a &quot;0&quot; is returned, otherwise, &quot;-1&quot; is returned.</dl>
<dl>
<dt>pbsmovejob jobid ?location?</p>
<dd>Move the job given by <i>jobid</i> to the location given by <i>location.</i> If <i>location</i> is not given, the default location is used. If this is successful, a &quot;0&quot; is returned, otherwise, &quot;-1&quot; is returned.</dl>
<dl>
<dt>pbsqenable queue</p>
<dd>Set the &quot;enabled&quot; attribute for the queue given by <i>queue</i> to true. If this is successful, a &quot;0&quot; is returned, otherwise, &quot;-1&quot; is returned.</dl>
<dl>
<dt>pbsqdisable queue</p>
<dd>Set the &quot;enabled&quot; attribute for the queue given by <i>queue</i> to false. If this is successful, a &quot;0&quot; is returned, otherwise, &quot;-1&quot; is returned.</dl>
<dl>
<dt>pbsqstart queue</p>
<dd>Set the &quot;started&quot; attribute for the queue given by <i>queue</i> to true. If this is successful, a &quot;0&quot; is returned, otherwise, &quot;-1&quot; is returned.</dl>
<dl>
<dt>pbsqstop queue</p>
<dd>Set the &quot;started&quot; attribute for the queue given by <i>queue</i> to false. If this is successful, a &quot;0&quot; is returned, otherwise, &quot;-1&quot; is returned.</dl>
<dl>
<dt>pbsalterjob jobid attribute_list</p>
<dd>Alter the attributes for a job specified by <i>jobid.</i> The parameter <i>attribute_list</i> is the list of attributes to be altered. There can be more than one. Each attribute consists of a list of three elements. The first is the name, the second the resource and the third is the new value. If the alter is successful, a &quot;0&quot; is returned, otherwise, &quot;-1&quot; is returned.</dl>
<dl>
<dt>pbsrescquery resource_list</p>
<dd>Obtain information about the resources specified by <i>resource_list.</i> This will be a list of strings. If the request succeeds, a list with the same number of elements as <i>resource_list</i> is returned. Each element in this list will be a list with four numbers. The numbers specify <i>available,</i> <i>allocated,</i> <i>reserved,</i> and <i>down</i> in that order.</dl>
<dl>
<dt>pbsrescreserve resource_id resource_list</p>
<dd>Make (or extend) a reservation for the resources specified by <i>resource_list</i> which will be given as a list of strings. The parameter <i>resource_id</i> is a number which provides a unique identifier for a reservation being tracked by the server. If <i>resource_id</i> is given as &quot;0&quot;, a new reservation is created. In this case, a new identifier is generated and returned by the function. If an old identifier is used, that same number will be returned. The Tcl variable &quot;pbs_errno&quot; will be set to indicate the success or failure of the reservation.</dl>
<dl>
<dt>pbsrescrelease resource_id</p>
<dd>The reservation specified by <i>resource_id</i> is released.</dl>
<p> The two following commands are not normally used by the scheduler. They are included here because there could be a need for a scheduler to contact a server other than the one which it normally communicates with. Also, these commands are used by the Tcl tools. </p>
<dl>
<dt>pbsconnect ?server?</p>
<dd>Make a connection to the named server or the default server if a parameter is not given. Only one connection to a server is allowed at any one time.</dl>
<dl>
<dt>pbsdisconnect</p>
<dd>Disconnect from the currently connected server.</dl>
<p> The above Tcl functions use PBS interface library calls for communication with the server and the PBS resource monitor library to communicate with pbs_mom. </p>
<dl>
<dt>datetime ?day? ?time?</p>
<dd>The number of arguments used determine the type of date to be calculated. With no arguments, the current POSIX date is returned. This is an integer in seconds. </p>
<p> With one argument there are two possible formats. The first is a 12 (or more) character string specifying a complete date in the following format: </p>
<pre>YYMMDDhhmmss</pre>
<p>All characters must be digits. The year (YY) is given by the first two (or more) characters and is the number of years since 1900. The month (MM) is the number of the month [01-12]. The day (DD) is the day of the month [01-32]. The hour (hh) is the hour of the day [00-23]. The minute (mm) is minutes after the hour [00-59]. The second (ss) is seconds after the minute [00-59]. The POSIX date for the given date/time is returned. </p>
<p> The second option with one argument is a relative time. The format for this is </p>
<pre>HH:MM:SS</pre>
<p>With hours (HH), minutes (MM) and seconds (SS) being separated by colons &quot;:&quot;. The number returned in this case will be the number of seconds in the interval specified, not an absolute POSIX date. </p>
<p> With two arguments a relative date is calculated. The first argument specifies a day of the week and must be one of the following strings: &quot;Sun&quot;, &quot;Mon&quot;, &quot;Tue&quot;, &quot;Wed&quot;, &quot;Thr&quot;, &quot;Fri&quot;, or &quot;Sat&quot;. The second argument is a relative time as given above. The POSIX date calculated will be the day of the week given which follows the current day, and the time given in the second argument. For example, if the current day was Monday, and the two arguments were &quot;Fri&quot; and &quot;04:30:00&quot;, the date calculated would be the POSIX date for the Friday following the current Monday, at four-thirty in the morning. If the day specified and the current day are the same, the current day is used, not the day one week later.</dl>
<dl>
<dt>strftime format time</p>
<dd>This function calls the POSIX function <i>strftime().</i> It requires two arguments. The first is a format string. The format conventions are the same as those for the POSIX function strftime(). The second argument is POSIX calendar time in second as returned by <i>datetime.</i> It returns a string based on the format given. This gives the ability to extract information about a time, or format it for printing.</dl>
<p> The Tcl interpreter is started at program initialization and after a reset (the receipt of a SIGHUP signal). It is not deleted between scheduling runs so variables which are set in one can be accessed later. </p>
<p> The &quot;initialize&quot; and &quot;terminator&quot; files are run with no supplied connection to the server. This means that none of the above functions which talk to the server will work unless <code>pbsconnect</code> is called first. The &quot;body&quot; file is run with a connection to the server already established.</p>
<h2>Configuration File</h2>
<p>A configuration file may be specified with the -c option. This file may be used to specify the hosts (servers) which are allowed to connect to pbs_sched. The hosts are specified in the configuration file in a manor identical to that used in pbs_mom. There is one line per host with the syntax:<br />
 <code><br />
 where clienthost and hostname are separated by white space. </p>
<p> Two host names are always allowed to connection to pbs_sched, &quot;localhost&quot; and the name returned to pbs_sched by the system call gethostname(). These names need not be specified in the configuration file. </p>
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
<p><a href="//www.systutorials.com/docs/linux/man/8B-pbs_scheduler_cc/">pbs_scheduler_cc</a>(8B), <a href="//www.systutorials.com/docs/linux/man/8B-pbs_scheduler_rule/">pbs_scheduler_rule</a>(8B), <a href="//www.systutorials.com/docs/linux/man/8B-pbs_server/">pbs_server</a>(8B), and <a href="//www.systutorials.com/docs/linux/man/8B-pbs_mom/">pbs_mom</a>(8B).<br />
 PBS Internal Design Specification </p>
