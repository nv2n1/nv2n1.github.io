---
title: "mon(8)"
name: "mon"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mon/"
description: "mon – monitor services for availability, sending alarms upon failures."
---

<p>mon &#8211; monitor services for availability, sending alarms upon failures.</p>
<h2>Synopsis</h2>
<p><code>mon</code> [<code>-dfhlMSv</code>] [<code>-a</code> <i>dir</i>] [<code>-A</code> <i>authfile</i>] [<code>-b</code> <i>dir</i>] [<code>-B</code> <i>dir</i>] [<code>-c</code> <i>config</i>] [<code>-D</code> <i>dir</i>] [<code>-i</code> <i>secs</i>] [<code>-k</code> <i>num</i>] [<code>-l</code> <i>[</i>statetype<i>]</i>] [<code>-L</code> <i>dir</i>] [<code>-m</code> <i>num</i>] [<code>-p</code> <i>num</i>] [<code>-P</code> <i>pidfile</i>] [<code>-r</code> <i>delay</i>] [<code>-s</code> <i>dir</i>]</p>
<h2>Description</h2>
<p><code>mon</code> is a general-purpose scheduler for monitoring service availability and triggering alerts upon detecting failures. <code>mon</code> was designed to be open in the sense that it supports arbitrary monitoring facilities and alert methods via a common interface, which are easily implemented through programs (in C, Perl, shell, etc.), SNMP traps, and special Mon (UDP packet) traps. </p>
<h2>Options</h2>
<dl>
<dt><code>-a&nbsp;<wbr></code><i>dir</i></p>
<dd>Path to alert scripts. Default is <i>/usr/local/lib/mon/alert.d:alert.d</i>. Multiple alert paths may be specified by separating them with a colon. Non-absolute paths are taken to be relative to the base directory (<i>/usr/lib/mon</i> by default).</p>
<dt><code>-b&nbsp;<wbr></code><i>dir</i></p>
<dd>Base directory for mon. scriptdir, alertdir, and statedir are all relative to this directory unless specified from /. Default is <i>/usr/lib/mon</i>.</p>
<dt><code>-B&nbsp;<wbr></code><i>dir</i></p>
<dd>Configuration file base directory. All config files are located here, including mon.cf, monusers.cf, and auth.cf.</p>
<dt><code>-A&nbsp;<wbr></code><i>authfile</i></p>
<dd>Authentication configuration file. By default this is <i>/etc/mon/auth.cf</i> if the <i>/etc/mon</i> directory exists, or <i>/usr/lib/mon/auth.cf</i> otherwise.</p>
<dt><code>-c&nbsp;<wbr></code><i>file</i></p>
<dd>Read configuration from <i>file</i>. This defaults to IR /etc/mon/mon.cf &quot; if the &quot; /etc/mon directory exists, otherwise to <i>/etc/mon.cf</i>.</p>
<dt><code>-d</code></p>
<dd>Enable debugging mode.</p>
<dt><code>-D dir</code></p>
<dd>Path to state directory. Default is the first of <i>/var/state/mon</i>, <i>/var/lib/mon</i>, and <i>/usr/lib/mon/state.d</i> which exists.</p>
<dt><code>-f</code></p>
<dd>Fork and run as a daemon process. This is the preferred way to run <code>mon</code>.</p>
<dt><code>-h</code></p>
<dd>Print help information.</p>
<dt><code>-i&nbsp;<wbr></code><i>secs</i></p>
<dd>Sleep interval, in seconds. Defaults to 1. This shouldn&#8217;t need to be adjusted for any reason.</p>
<dt><code>-k&nbsp;<wbr></code><i>num</i></p>
<dd>Set log history to a maximum of <i>num</i> entries. Defaults to 100.</p>
<dt><code>-l statetype</code></p>
<dd>Load state from the last saved state file. The supported saved state types are <code>disabled</code> for disabled watches, services, and hosts, <code>opstatus</code> for failure/alert/ack status of all services, and <code>all </code> for both. If no statetype is provided, <code>disabled</code> is assumed.</p>
<dt><code>-L dir</code></p>
<dd>Sets the log dir. See also <code>logdir</code> in the configuration file. The default is <code>/var/log/mon</code> if that directory exists, otherwise <code>log.d</code> in the base directory.</p>
<dt><code>-M</code></p>
<dd>Pre-process the configuration file with the macro expansion package <i>m4</i>.</p>
<dt><code>-m&nbsp;<wbr></code><i>num</i></p>
<dd>Set the throttle for the maximum number of processes to <i>num</i>.</p>
<dt><code>-p&nbsp;<wbr></code><i>num</i></p>
<dd>Make server listen on port <i>num</i>. This defaults to 2583.</p>
<dt><code>-S</code></p>
<dd>Start with the scheduler stopped.</p>
<dt><code>-P&nbsp;<wbr></code><i>pidfile</i></p>
<dd>Store the server&#8217;s pid in <i>pidfile</i>, the default is the first of <i>/var/run/mon/mon.pid</i>, <i>/var/run/mon.pid</i>, and <i>/etc/mon.pid</i> whose directory exists. An empty value tells <code>mon</code> not to use a pid file.</p>
<dt><code>-r&nbsp;<wbr></code><i>delay</i></p>
<dd>Sets the number of seconds used to randomize the startup delay before each service is scheduled. Refer to the global <i>randstart</i> variable in the configuration file.</p>
<dt><code>-s&nbsp;<wbr></code><i>dir</i></p>
<dd>Path to monitor scripts. Default is <i>/usr/local/lib/mon/mon.d:mon.d</i>. Multiple alert paths may be specified by separating them with a colon. Non-absolute paths are taken to be relative to the base directory (<i>/usr/lib/mon</i> by default).</p>
<dt><code>-v</code></p>
<dd>Print version information. </p>
</dl>
<h2>Definitions</h2>
<dl>
<dt><code>monitor</code></p>
<dd>A program which tests for a certain condition, returns either true or false, and optionally produces output to be passed back to the scheduler. Common monitors detect host reachability via ICMP echo messages, or connection to TCP services.</p>
<dt><code>period</code></p>
<dd>A period in time as interpreted by the Time::Period module.</p>
<dt><code>alert</code></p>
<dd>A program which sends a message when invoked by the scheduler. The scheduler calls upon an alert when it detects a failure from a monitor. An alert program accepts a set of command-line arguments from the scheduler, in addition to data via standard input.</p>
<dt><code>hostgroup</code></p>
<dd>A single host or list of hosts, specified as names or IP addresses.</p>
<dt><code>service</code></p>
<dd>A collection of parameters used to deal with monitoring a particular resource which is provided by a group. Services are usually modeled after things such as an SMTP server, ICMP echo capability, server disk space availability, or SNMP events.</p>
<dt><code>view</code></p>
<dd>A collection of hostgroups, used to filter mon output for client display. i.e. a &#8216;network-services&#8217; view might be defined so your network staff can see just the hostgroups which matter to them, without having to see all hostgroups defined in Mon.</p>
<dt><code>watch</code></p>
<dd>A collection of services which apply to a particular group.</dl>
<h2>Operation</h2>
<p>When the <code>mon</code> scheduler starts, it reads a configuration file to determine the services it needs to monitor. The configuration file defaults to <i>/etc/mon.cf</i>, and can be specified using the <code>-c</code> parameter. If the <code>-M</code> option is specified, then the configuration file is pre-processed with <i>m4</i>. If the configuration file ends with .m4, the file is also processed by m4 automatically. </p>
<p> The scheduler enters a loop which handles client connections, monitor invocations, and failure alerts. Each service has a timer, specified in the configuration file as the <code>interval</code> variable, which tells the scheduler how frequently to invoke a monitor process. The scheduler may be temporarily stopped. While it is stopped, client access still functions, but it just doesn&#8217;t schedule things. This is useful in conjunction while resetting the server, because you can do this: save the hosts and services which are disabled, reset the server with the scheduler stopped, re-disabled those hosts and services, then start the scheduler. It also allows making atomic changes across several client connections. See the <code>moncmd</code> man page for more information.</p>
<h2>Monitor Programs</h2>
<p>Monitor processes are invoked with the arguments specified in the configuration file, appended by the hosts from the applicable host group. For example, if the watch group is &quot;servers&quot;, which contain the hostnames &quot;smtp&quot;, &quot;nntp&quot;, and &quot;ns&quot;, and the monitor line reads as follows,<br />
 monitor fping.monitor -t 4000 -r 2<br />
 then the exectuable &quot;fping.monitor&quot; will be executed with these parameters:<br />
 MONITOR_DIR/fping.monitor -t 4000 -r 2 smtp nntp ns </p>
<p> MONITOR_DIR is actually a search path, by default <i>/usr/local/lib/mon/mon.d</i> then <i>/usr/lib/mon/mon.d</i>, but it can be overridden by the <code>-s</code> option or in the configuration file. If all hosts in the hostgroup have been disabled, then a warning is sent to syslog and the monitor is not run. This behavior may be overridden with the &quot;allow_empty_group&quot; option in the service definition. If the final argument to the &quot;monitor&quot; line is &quot;;;&quot; (it must be preceded by whitespace), then the host list will not be appended to the parameter list. </p>
<p> In addition to environment variables defined by the user in the service definition, <code>mon</code> passes certain variables to monitor process. </p>
<dl>
<dt><code>MON_LAST_SUMMARY</code></p>
<dd>The first line of the output from the last time the monitor exited. This is not the summary of the current monitor run, but the previous one. This may be used by an alert script to provide historical context in an alert. </p>
<dt><code>MON_LAST_OUTPUT</code></p>
<dd>The entire output of the monitor from the last time it exited. This is not the output of the current monitor run, but the previous one. This may be used by an alert script to provide historical context in an alert. </p>
<dt><code>MON_LAST_FAILURE</code></p>
<dd>The <a href="/docs/linux/man/2-time/">time</a>(2) of the last failure for this service. </p>
<dt><code>MON_FIRST_FAILURE</code></p>
<dd>The <a href="/docs/linux/man/2-time/">time</a>(2) of the first time this service failed. </p>
<dt><code>MON_LAST_SUCCESS</code></p>
<dd>The <a href="/docs/linux/man/2-time/">time</a>(2) of the last time this service passed. </p>
<dt><code>MON_DESCRIPTION</code></p>
<dd>The description of this service, as defined in the configuration file using the <i>description</i> tag. </p>
<dt><code>MON_DEPEND_STATUS</code></p>
<dd>The depend status, &quot;o&quot; if dependency failure, &quot;1&quot; otherwise. </p>
<dt><code>MON_LOGDIR</code></p>
<dd>The directory log files should be placed, as indicated by the <i>logdir</i> global configuration variable. </p>
<dt><code>MON_STATEDIR</code></p>
<dd>The directory where state files should be kept, as indicated by the <i>statedir</i> global configuration variable. </p>
<dt><code>MON_CFBASEDIR</code></p>
<dd>The directory where configuration files should be kept, as indicated by the <i>cfbasedir</i> global configuration variable. </p>
<p> &quot;fping.monitor&quot; should return an exit status of 0 if it completed successfully (found no problems), or nonzero if a problem was detected. The first line of output from the monitor script has a special meaning: it is used as a brief summary of the exact failure which was detected, and is passed to the alert program. All remaining output is also passed to the alert program, but it has no required interpretation. </p>
<p> If a monitor for a particular service is still running, and the time comes for <code>mon</code> to run another monitor for that service, it will not start another monitor. For example, if the <i>interval</i> is 10s, and the monitor does not finish running within 10 seconds, then <code>mon</code> will wait until the first monitor exits before running another one. </p>
</dl>
<h2>Alert Decision Logic</h2>
<p>Upon a non-zero or zero exit status, the associated alert or upalert program (respectively) is started, pending the following conditions: If an alert for a specific service is disabled, do not send an alert. If <code>dep_behavior</code> is set to <i>&#8216;a&#8217;</i>, or <code>alertdepend</code> is set, and a parent dependency is failing, then suppress the alert. If the alert has previously been acknowledged, do not send the alert, unless it is an upalert. If an alert is not within the specified period, record the failure via <a href="/docs/linux/man/3-syslog/">syslog</a>(3) and do not send an alert. If the failure does not fall within a defined period, do not send an alert. No upalerts are sent without corresponding down alerts, unless <code>no_comp_alerts</code> is defined in the period section. An upalert will only be sent if the previous state is a failure. If an alert was already sent within the last <code>alertevery</code> interval, do not send another alert, <i>unless</i> the summary output from the current monitor program differs from the last monitor process. Otherwise, send an alert using each alert program listed for that period. The <code>observe_detail</code> argument to <code>alertevery</code> affects this behavior by observing the changes in the detail part of the output in addition to the summary line. If a monitor has successive failures and the summary output changes in each of them, <code>alertevery</code> will not suppress multiple consecutive alerts. The reasoning is that if the summary output changes, then a significant event occurred and the user should be alerted. The &quot;strict&quot; argument to alertevery will suppress both comparing the output from the previous monitor run to the current and prevent a successful return value of the monitor from resetting the alertevery timer. For example, &quot;alertevery 24h strict&quot; will only send out an alert once every 24 hours, regardless of whether the monitor output changes, or if the service stops and then starts failing.</p>
<h2>Alert Programs</h2>
<p>Alert programs are found in the path supplied with the <code>-a</code> parameter, or in the <i>/usr/local/lib/mon/alert.d</i> and directories if not specified. They are invoked with the following command-line parameters: </p>
<dl>
<dt><code>-s&nbsp;<wbr></code><i>service</i></p>
<dd>Service tag from the configuration file.</p>
<dt><code>-g&nbsp;<wbr></code><i>group</i></p>
<dd>Host group name from the configuration file.</p>
<dt><code>-h&nbsp;<wbr></code><i>hosts</i></p>
<dd>The expanded version of the host group, space delimited, but contained in one shell &quot;word&quot;.</p>
<dt><code>-l&nbsp;<wbr></code><i>alertevery</i></p>
<dd>The number of seconds until the next alarm will be sent.</p>
<dt><code>-O</code></p>
<dd>This option is supplied to an alert only if the alert is being generated as a result of an expected traap timing out</p>
<dt><code>-t&nbsp;<wbr></code><i>time</i></p>
<dd>The time (in <code><a href="/docs/linux/man/2-time/">time</a></code>(2) format) of when this failure condition was detected.</p>
<dt><code>-T</code></p>
<dd>This option is supplied to an alert only if the alert was triggered by a trap</p>
<dt><code>-u</code></p>
<dd>This option is supplied to an alert only if it is being called as an upalert. </p>
<p> The remaining arguments are supplied from the trailing parameters in the configuration file, after the &quot;alert&quot; service parameter. </p>
<p> As with monitor programs, alert programs are invoked with environment variables defined by the user in the service definition, in addition to the following which are explicitly set by the server: </p>
<dt><code>MON_LAST_SUMMARY</code></p>
<dd>The first line of the output from the last time the monitor exited. </p>
<dt><code>MON_LAST_OUTPUT</code></p>
<dd>The entire output of the monitor from the last time it exited. </p>
<dt><code>MON_LAST_FAILURE</code></p>
<dd>The <a href="/docs/linux/man/2-time/">time</a>(2) of the last failure for this service. </p>
<dt><code>MON_FIRST_FAILURE</code></p>
<dd>The <a href="/docs/linux/man/2-time/">time</a>(2) of the first time this service failed. </p>
<dt><code>MON_LAST_SUCCESS</code></p>
<dd>The <a href="/docs/linux/man/2-time/">time</a>(2) of the last time this service passed. </p>
<dt><code>MON_DESCRIPTION</code></p>
<dd>The description of this service, as defined in the configuration file using the <i>description</i> tag. </p>
<dt><code>MON_GROUP</code></p>
<dd>The watch group which triggered this alarm </p>
<dt><code>MON_SERVICE</code></p>
<dd>The service heading which generated this alert </p>
<dt><code>MON_RETVAL</code></p>
<dd>The exit value of the failed monitor program, or return value as accepted from a trap. </p>
<dt><code>MON_OPSTATUS</code></p>
<dd>The operational status of the service. </p>
<dt><code>MON_ALERTTYPE</code></p>
<dd>Has one of the following values: &quot;failure&quot;, &quot;up&quot;, &quot;startup&quot;, &quot;trap&quot;, or &quot;traptimeout&quot;, and signifies the type of alert which was triggered. </p>
<dt><code>MON_TRAP_INTENDED</code></p>
<dd>This is only set when an unknown mon trap is received and caught by the default/defaut watch/service. This contains colon separated entries of the trap&#8217;s intended watch group and service name. </p>
<dt><code>MON_LOGDIR</code></p>
<dd>The directory log files should be placed, as indicated by the <i>logdir</i> global configuration variable. </p>
<dt><code>MON_STATEDIR</code></p>
<dd>The directory where state files should be kept, as indicated by the <i>statedir</i> global configuration variable. </p>
<dt><code>MON_CFBASEDIR</code></p>
<dd>The directory where configuration files should be kept, as indicated by the <i>cfbasedir</i> global configuration variable. </p>
<p> The first line from standard input must be used as a brief summary of the problem, normally supplied as the subject line of an email, or text sent to an alphanumeric pager. Interpretation of all subsequent lines read from stdin is left up to the alerting program. The usual parameters are a list of recipients to deliver the notification to. The interpretation of the recipients is not specified, and is up to the alert program. </p>
</dl>
<h2>Configuration File</h2>
<p>The configuration file consists of zero or more global variable definitions, zero or more hostgroup definitions, and one or more watch definitions. Each watch definition may have one or more service definitions. A watch definition is terminated by a blank line, another definition, or the end of the file. A line beginning with optional leading whitespace and a pound (&quot;#&quot;) is regarded as a comment, and is ignored. </p>
<p> Lines are parsed as they are read. Long lines may be continued by ending them with a backslash (&quot;\&quot;). If a line is continued, then the backslash, the trailing whitespace after the backslash, and the leading whitespace of the following line are removed. The end result is assembled into a single line. </p>
<p> Typically the configuration file has the following layout: </p>
<p> 1. Global variable definitions </p>
<p> 2. Hostgroup definitions </p>
<p> 3. Watch definitions </p>
<p> See the &quot;etc/example.cf&quot; file which comes for the distribution for an example.</p>
<h3>Global Variables</h3>
<p>The following variables may be set to override compiled-in defaults. Command-line options will have a higher precedence than these definitions. </p>
<dl>
<dt><code>alertdir = </code><i>dir</i></p>
<dd><i>dir</i> is the full path to the alert scripts. This is the value set by the <code>-a</code> command-line parameter. </p>
<p> Multiple alert paths may be specified by separating them with a colon. Non-absolute paths are taken to be relative to the base directory (<i>/usr/lib/mon</i> by default). </p>
<p> When the configuration file is read, all alerts referenced from the configuration will be looked up in each of these paths, and the full path to the first instance of the alert found is stored in a hash. This hash is only generated upon startup or after a &quot;reset&quot; command, so newly added alert scripts will not be recognized until a &quot;reset&quot; is performed. </p>
<dt><code>mondir = </code><i>dir</i></p>
<dd><i>dir</i> is the full path to the monitor scripts. This value may also be set by the <code>-s</code> command-line parameter. If this path does not begin with a &quot;/&quot;, it will be relative to <i>basedir</i>. </p>
<p> Multiple alert paths may be specified by separating them with a colon. All paths must be absolute. </p>
<p> When the configuration file is read, all monitors referenced from the configuration will be looked up in each of these paths, and the full path to the first instance of the monitor found is stored in a hash. This hash is only generated upon startup or after a &quot;reset&quot; command, so newly added monitor scripts will not be recognized until a &quot;reset&quot; is performed. </p>
<dt><code>statedir = </code><i>dir</i></p>
<dd><i>dir</i> is the full path to the state directory. <code>mon</code> uses this directory to save various state information. If this path does not begin with a &quot;/&quot;, it will be relative to <i>basedir</i>. </p>
<dt><code>logdir = </code><i>dir</i></p>
<dd><i>dir</i> is the full path to the log directory. <code>mon</code> uses this directory to save various logs, including the downtime log. If this path does not begin with a &quot;/&quot;, it will be relative to <i>basedir</i>. </p>
<dt><code>basedir = </code><i>dir</i></p>
<dd><i>dir</i> is the full path for the state, log, monitor, and alert directories. </p>
<dt><code>cfbasedir = </code><i>dir</i></p>
<dd><i>dir</i> is the full path where all the config files can be found (monusers.cf, auth.cf, etc.). </p>
<dt><code>authfile = </code><i>file</i></p>
<dd><i>file</i> is the path to the authentication file. If the path does not begin with a &quot;/&quot;, it will be relative to <i>cfbasedir</i>. </p>
<dt><code>authtype = </code><i>type [type&#8230;]</i></p>
<dd><i>type</i> is the type of authentication to use. A space-separated list of types may be specified, and they will be checked the order they are listed. As soon as a successful authentication is performed, the user is considered authenticated by mon for the duration of the session and no more authentication checks are performed. </p>
<p> If <i>type</i> is <code>getpwnam</code>, then the standard Unix passwd file authentication method will be used (calls <a href="/docs/linux/man/3-getpwnam/">getpwnam</a>(3) on the user and compares the <a href="/docs/linux/man/3-crypt/">crypt</a>(3)ed version of the password with what it gets from getpwnam). This will not work if shadow passwords are enabled on the system. </p>
<p> If <i>type</i> is <code>userfile</code>, then usernames and hashed passwords are read from <i>userfile</i>, which is defined via the <code>userfile</code> configuration variable. </p>
<p> If <i>type</i> is <code>pam</code>, then PAM (pluggable authentication modules) will be used for authentication. The service specified by the <code>pamservice</code> global will be used. If no global is given, the PAM <code>passwd</code> service will be used. </p>
<p> If <i>type</i> is <code>trustlocal</code>, then if the client connection comes from locahost, the username passed from the client will be trusted, and the password will be ignored. This can be used when you want the client to handle the authentication for you. I.e. a CGI script using one of the many apache authentication methods. </p>
<dt><code>userfile = </code><i>file</i></p>
<dd>This file is used when <code>authtype</code> is set to <i>userfile</i>. It consists of a sequence of lines of the format <code>&#8216;username : password&#8217;</code>. <code>password</code> is stored as the hash returned by the standard Unix <a href="/docs/linux/man/3-crypt/">crypt</a>(3) function. <code>NOTE:</code> the format of this file is compatible with the Apache file based username/password file format. It is possible to use the <i>htpasswd</i> program supplied with Apache to manage the mon userfile. </p>
<p> Blank lines and lines beginning with # are ignored. </p>
<dt><code>pamservice = </code><i>service</i></p>
<dd>The PAM service used for authentication. This is applicable only if &quot;pam&quot; is specified as a parameter to the <code>authtype</code> setting. If this global is not defined, it defaults to <code>passwd</code>. </p>
<dt><code>serverbind = </code><i>addr</i></p>
<dd>
<dt><code>trapbind = </code><i>addr</i></p>
<dd><code>serverbind</code> and <code>trapbind</code> specify which address to bind the server and trap ports to, respectively. If these are not defined, the default address is INADDR_ANY, which allows connections on all interfaces. For security reasons, it could be a good idea to bind only to the loopback interface. </p>
<dt><code>dtlogfile = </code><i>file</i></p>
<dd><i>file</i> is a file which will be used to record the downtime log. Whenever a service fails for some amount of time and then stop failing, this event is written to the log. If this parameter is not set, no logging is done. The format of the file is as follows (# is a comment and may be ignored): </p>
<p> <code>timenoticed group service firstfail downtime interval summary.</code> </p>
<p> <code>timenoticed</code> is the <a href="/docs/linux/man/2-time/">time</a>(2) the service came back up. </p>
<p> <code>group service</code> is the group and service which failed. </p>
<p> <code>firstfail</code> is the <a href="/docs/linux/man/2-time/">time</a>(2) when the service began to fail. </p>
<p> <code>downtime</code> is the number of seconds the service failed. </p>
<p> <code>interval</code> is the frequency (in seconds) that the service is polled. </p>
<p> <code>summary</code> is the summary line from when the service was failing. </p>
<dt><code>monerrfile = </code><i>filename</i></p>
<dd>By default, when mon daemonizes itself, it connects stdout and stderr to /dev/null. If <code>monerrfile</code> is set to a file, then stdout and stderr will be appended to that file. In all cases stdin is connected to /dev/null. If mon is told to run in the foreground and to not daemonize, then none of this applies, since stdin/stdout/stderr stay connected to whatever they were at the time of invocation. </p>
<dt><code>dtlogging = </code><i>yes/no</i></p>
<dd>Turns downtime logging on or off. The default is off. </p>
<dt><code>histlength = </code><i>num</i></p>
<dd><i>num</i> is the the maximum number of events to be retained in history list. The default is 100. This value may also be set by the <code>-k</code> command-line parameter. </p>
<dt><code>historicfile = </code><i>file</i></p>
<dd>If this variable is set, then alerts are logged to <i>file</i>, and upon startup, some (or all) of the past history is read into memory. </p>
<dt><code>historictime = </code><i>timeval</i></p>
<dd><i>num</i> is the amount of the history file to read upon startup. &quot;Now&quot; &#8211; <i>timeval</i> is read. See the explanation of <i>interval</i> in the &quot;Service Definitions&quot; section for a description of <i>timeval</i>. </p>
<dt><code>serverport = </code><i>port</i></p>
<dd><i>port</i> is the TCP port number that the server should bind to. This value may also be set by the <code>-p</code> command-line parameter. Normally this port is looked up via <a href="/docs/linux/man/3-getservbyname/">getservbyname</a>(3), and it defaults to 2583. </p>
<dt><code>trapport = </code><i>port</i></p>
<dd><i>port</i> is the UDP port number that the trap server should bind to. Normally this port is looked up via <a href="/docs/linux/man/3-getservbyname/">getservbyname</a>(3), and it defaults to 2583. </p>
<dt><code>pidfile = </code><i>path</i></p>
<dd><i>path</i> is the file the sever will store its pid in. This value may also be set by the <code>-P</code> command-line parameter. </p>
<dt><code>maxprocs = </code><i>num</i></p>
<dd>Throttles the number of concurrently forked processes to <i>num.</i> The intent is to provide a safety net for the unlikely situation when the server tries to take on too many tasks at once. Note that this situation has only been reported to happen when trying to use a garbled configuration file! You don&#8217;t want to use a garbled configuration file now, do you? </p>
<dt><code>cltimeout = </code><i>secs</i></p>
<dd>Sets the client inactivity timeout to <i>secs.</i> This is meant to help thwart denial of service attacks or recover from crashed clients. <i>secs</i> is interpreted as a &quot;1h/1m/1s&quot; string, where &quot;1m&quot; = 60 seconds. </p>
<dt><code>randstart = </code><i>interval</i></p>
<dd>When the server starts, normally all services will not be scheduled until the interval defined in the respective service section. This can cause long delays before the first check of a service, and possibly a high load on the server if multiple things are scheduled at the same intervals. This option is used to randomize the scheduling of the first test for all services during the startup period, and immediately after the <i>reset</i> command. If <i>randstart</i> is defined, the scheduled run time of all services of all watch groups will be a random number between zero and <i>randstart</i> seconds. </p>
<dt><code>dep_recur_limit = </code><i>depth</i></p>
<dd>Limit dependency recursion level to <i>depth</i>. If dependency recursion (dependencies which depend on other dependencies) tries to go beyond <i>depth</i>, then the recursion is aborted and a messages is logged to syslog. The default limit is 10. </p>
<dt><code>dep_behavior = </code><i>{a|m|hm}</i></p>
<dd><code>dep_behavior</code> controls whether the dependency expression suppresses one of: the running of alerts, the running of monitors, or the passing of individual hosts to the monitors. Read more about the behavior in the &quot;Service Definitions&quot; section below. </p>
<p> This is a global setting which controls the default settings for the service-specified variable. </p>
<dt><code>dep_memory = </code><i>timeval</i></p>
<dd>If set, dep_memory will cause dependencies to continue to prevent alerts/monitoring for a period of time after the service returns to a normal state. This can be used to prevent over-eager alerting when a machine is rebooting, for example. See the explanation of <i>interval</i> in the &quot;Service Definitions&quot; section for a description of <i>timeval</i>. </p>
<p> This is a global setting which controls the default settings for the service-specified variable. </p>
<dt><code>syslog_facility = </code><i>facility</i></p>
<dd>Specifies the syslog facility used for logging. <code>daemon</code> is the default. </p>
<dt><code>startupalerts_on_reset = </code><i>{yes|no}</i></p>
<dd>If set to &quot;yes&quot;, startupalerts will be invoked when the <code>reset</code> client command is executed. The default is &quot;no&quot;. </p>
<dt><code>monremote = </code><i>program</i></p>
<dd>If set, this external program will be called by Mon when various client requests are processed. This can be used to propagate those changes from one Mon server to another, if you have multiple monitoring machines. An example script, <code>monremote.pl</code> is available in the clients directory. </p>
</dl>
<h3>Hostgroup Entries</h3>
<p>Hostgroup entries begin with the keyword <code>hostgroup</code>, and are followed by a hostgroup tag and one or more hostnames or IP addresses, separated by whitespace. The hostgroup tag must be composed of alphanumeric characters, a dash (&quot;-&quot;), a period (&quot;.&quot;), or an underscore (&quot;_&quot;). Non-blank lines following the first hostgroup line are interpreted as more hostnames. The hostgroup definition ends with a blank line. For example: </p>
<dl>
<dd>
<pre>hostgroup servers nameserver smtpserver nntpserver
 nfsserver httpserver smbserver
hostgroup router_group cisco7000 agsplus</pre>
</dl>
<h3>View Entries</h3>
<p>View entries begin with the keyword <code>view</code>, and are followed by a view tag and the names of one or more hostgroups. The view tag must be composed of alphanumeric characters, a dash (&quot;-&quot;), a period (&quot;.&quot;), or an underscore (&quot;_&quot;). Non-blank lines following the first view line are interpreted as more hostgroup names. The view definition ends with a blank line. For example: </p>
<dl>
<dd>
<pre>view servers dns-servers web-servers file-servers
 mail-servers
view network-services routers switches vpn-servers</pre>
</dl>
<h3>Watch Group Entries</h3>
<p>Watch entries begin with a line that starts with the keyword <code>watch</code>, followed by whitespace and a single word which normally refers to a pre-defined hostgroup. If the second word is not recognized as a hostgroup tag, a new hostgroup is created whose tag is that word, and that word is its only member. </p>
<p> Watch entries consist of one or more service definitions. </p>
<p> A watch group is terminated by a blank line, the end of the file, or by a subsequent definition, &quot;watch&quot;, &quot;hostgroup&quot;, or otherwise. </p>
<p> There may be a special watch group entry called &quot;default&quot;. If a default watch group is defined with a service entry named &quot;default&quot;, then this definition will be used in handling traps received for an unrecognized watch and service.</p>
<h3>Service Definitions</h3>
<dl>
<dt><code>service</code><i> servicename</i></p>
<dd>A service definition begins with they keyword <code>service</code> followed by a word which is the tag for this service. This word must be unique among all services defined for the same watch group. </p>
<p> The components of a service are an interval, monitor, and one or more time period definitions, as defined below. </p>
<p> If a service name of &quot;default&quot; is defined within a watch group called &quot;dafault&quot; (see above), then the default/default definition will be used for handling unknown mon traps. </p>
<p> The following configuration parameters are valid only following a service definition: </p>
<dt><code>VARIABLE=</code><i>value</i></p>
<dd>Environment variables may be defined for each service, which will be included in the environment of monitors and alerts. Variables must be specified in all capital letters, must begin with an alphabetical character or an underscore, and there must be no spaces to the left of the equal sign. </p>
<dt><code>interval</code><i> timeval</i></p>
<dd>The keyword <code>interval</code> followed by a time value specifies the frequency that a monitor script will be triggered. Time values are defined as &quot;30s&quot;, &quot;5m&quot;, &quot;1h&quot;, or &quot;1d&quot;, meaning 30 seconds, 5 minutes, 1 hour, or 1 day. The numeric portion may be a fraction, such as &quot;1.5h&quot; or an hour and a half. This format of a time specification will be referred to as <i>timeval</i>. </p>
<dt><code>failure_interval</code><i> timeval</i></p>
<dd>Adjusts the polling interval to <i>timeval</i> when the service check is failing. Resets the interval to the original when the service succeeds. </p>
<dt><code>traptimeout</code><i> timeval</i></p>
<dd>This keyword takes the same time specification argument as <code>interval</code><i>,</i> and makes the service expect a trap from an external source at least that often, else a failure will be registered. This is used for a heartbeat-style service. </p>
<dt><code>trapduration</code><i> timeval</i></p>
<dd>If a trap is received, the status of the service the trap was delivered to will normally remain constant. If <code>trapduration</code> is specified, the status of the service will remain in a failure state for the duration specified by <i>timeval</i>, and then it will be reset to &quot;success&quot;. </p>
<dt><code>randskew</code><i> timeval</i></p>
<dd>Rather than schedule the monitor script to run at the start of each interval, randomly adjust the interval specified by the <code>interval</code> parameter by plus-or-minus <code>randskew.</code> The skew value is specified as the <code>interval</code> parameter: &quot;30s&quot;, &quot;5m&quot;, etc&#8230; For example if <code>interval</code> is 1m, and <code>randskew</code> is &quot;5s&quot;, then <i>mon</i> will schedule the monitor script some time between every 55 seconds and 65 seconds. The intent is to help distribute the load on the server when many services are scheduled at the same intervals. </p>
<dt><code>monitor</code><i> monitor-name [arg&#8230;]</i></p>
<dd>The keyword <code>monitor</code> followed by a script name and arguments specifies the monitor to run when the timer expires. Shell-like quoting conventions are followed when specifying the arguments to send to the monitor script. The script is invoked from the directory given with the <code>-s</code> argument, and all following words are supplied as arguments to the monitor program, followed by the list of hosts in the group referred to by the current watch group. If the monitor line ends with &quot;;;&quot; as a separate word, the host groups are not appended to the argument list when the program is invoked. </p>
<dt><code>allow_empty_group</code></p>
<dd>The <code>allow_empty_group</code> option will allow a monitor to be invoked even when the hostgroup for that watch is empty because of disabled hosts. The default behavior is not to invoke the monitor when all hosts in a hostgroup have been disabled. </p>
<dt><code>description</code><i> descriptiontext</i></p>
<dd>The text following <code>description</code> is queried by client programs, passed to alerts and monitors via an environment variable. It should contain a brief description of the service, suitable for inclusion in an email or on a web page. </p>
<dt><code>exclude_hosts</code><i> host [host&#8230;]</i></p>
<dd>Any hosts listed after <code>exclude_hosts</code> will be excluded from the service check. </p>
<dt><code>exclude_period</code><i> periodspec</i></p>
<dd>Do not run a scheduled monitor during the time identified by <i>periodspec</i>. </p>
<dt><code>depend</code><i> dependexpression</i></p>
<dd>The <code>depend</code> keyword is used to specify a dependency expression, which evaluates to either true of false, in the boolean sense. Dependencies are actual Perl expressions, and must obey all syntactical rules. The expressions are evaluated in their own package space so as to not accidentally have some unwanted side-effect. If a syntax error is found when evaluating the expression, it is logged via syslog. </p>
<p> Before evaluation, the following substitutions on the expression occur: phrases which look like &quot;group:service&quot; are substituted with the value of the current operational status of that specified service. These opstatus substitutions are computed recursively, so if service A depends upon service B, and service B depends upon service C, then service A depends upon service C. Successful operational statuses (which evaluate to &quot;1&quot;) are &quot;STAT_OK&quot;, &quot;STAT_COLDSTART&quot;, &quot;STAT_WARMSTART&quot;, and &quot;STAT_UNKNOWN&quot;. The word &quot;SELF&quot; (in all caps) can be used for the group (e.g. &quot;SELF:service&quot;), and is an abbreviation for the current watch group. </p>
<p> This feature can be used to control alerts for services which are dependent on other services, e.g. an SMTP test which is dependent upon the machine being ping-reachable. </p>
<dt><code>dep_behavior</code><i> {a|m|hm}</i></p>
<dd>The evaluation of the dependency graphs specified via the <code>depend</code> keyword can control the suppression of alert or monitor invocations, or the suppression of individual hosts passed to the monitor. </p>
<p> <code>Alert suppression</code>. If this option is set to &quot;a&quot;, then the dependency expression will be evaluated after the monitor for the service exits or after a trap is received. An alert will only be sent if the evaluation succeeds, meaning that none of the nodes in the dependency graph indicate failure. </p>
<p> <code>Monitor suppression</code>. If it is set to &quot;m&quot;, then the dependency expression will be evaulated before the monitor for the service is about to run. If the evaulation succeeds, then the monitor will be run. Otherwise, the monitor will not be run and the status of the service will remain the same. </p>
<p> <code>Host suppression</code>. If it is set to &quot;hm&quot; then Mon will extract the list of &quot;parent&quot; services from the dependency expression. (In fact the expression can be just a list of services.) Then when the monitor for the service is about to be run, for each host in the current hostgroup Mon will search all the parent services which are currently failing and look for the hostname in the current summary output. If the hostname is found, this host will be excluded from this run of the monitor. This can be used to e.g. allow an SMTP test on a group of hosts to still be run even when a single host is not ping-reachable. If all the rest of the hosts are working fine, the service will be in an OK state, but if another host fails the SMTP test Mon can still alert about that host even though the parent dependency was failing. The dependency expression will <code>not</code> be used recursively in this case. </p>
<dt><code>alertdepend</code><i> dependexpression</i></p>
<dd>
<dt><code>monitordepend</code><i> dependexpression</i></p>
<dd>
<dt><code>hostdepend</code><i> dependexpression</i></p>
<dd>These keywords allow you to specify multiple dependency expressions of different types. Each one corresponds to the different <code>dep_behavior</code> settings listed above. They will be evaluated independently in the different contexts as listed above. If <code>depend</code> is present, it takes precedence over the matching keyword, depending on the <code>dep_behavior</code> setting. </p>
<dt><code>dep_memory </code><i>timeval</i></p>
<dd>If set, dep_memory will cause dependencies to continue to prevent alerts/monitoring for a period of time after the service returns to a normal state. This can be used to prevent over-eager alerting when a machine is rebooting, for example. See the explanation of <i>interval</i> in the &quot;Service Definitions&quot; section for a description of <i>timeval</i>. </p>
<dt><code>redistribute</code><i> alert [arg&#8230;]</i></p>
<dd>A service may have one redistribute option, which is a special form of an an alert definition. This alert will be called on every service status update, even sequential success status updates. This can be used to integrate Mon with another monitoring system, or to link together multiple Mon servers via an alert script that generates Mon traps. See the &quot;ALERT PROGRAMS&quot; section above for a list of the parameters mon will pass automatically to alert programs. </p>
<dt><code>unack_summary</code></p>
<dd>Remove the &quot;acknowledged&quot; state from a service if the summary component of the failure message changes. In most common usage the summary is the list of hosts that are failing, so additional hosts failing would remove an ack. </p>
</dl>
<h3>Period Definitions</h3>
<p>Periods are used to define the conditions which should allow alerts to be delivered. </p>
<dl>
<dt><code>period</code><i> [label:] periodspec</i></p>
<dd>A period groups one or more alarms and variables which control how often an alert happens when there is a failure. The <code>period</code> definition has two forms. The first takes an argument which is a period specification from Patrick Ryan&#8217;s Time::Period Perl 5 module. Refer to &quot;perldoc Time::Period&quot; for more information. </p>
<p> The second form requires a label followed by a period specification, as defined above. The label is a tag consisting of an alphabetic character or underscore followed by zero or more alphanumerics or underscores and ending with a colon. This form allows multiple periods with the same period definition. One use is to have a period definition which has no <code>alertafter</code> or <code>alertevery</code> parameters for a particular time period, and another for the same time period with a different set of alerts that does contain those parameters. </p>
<p> Period definitions, in either the first or second form, must be unique within each service definition. For example, if you need to define two periods both for &quot;wd {Sun-Sat}&quot;, then one or both of the period definitions must specify a label such as &quot;period t1: wd {Sun-Sat}&quot; and &quot;period t2: wd {Sun-Sat}&quot;. </p>
<dt><code>alertevery</code><i> timeval [observe_detail | strict]</i></p>
<dd>The <code>alertevery</code> keyword (within a <code>period</code> definition) takes the same type of argument as the <code>interval</code> variable, and limits the number of times an alert is sent when the service continues to fail. For example, if the interval is &quot;1h&quot;, then only the alerts in the period section will only be triggered once every hour. If the <code>alertevery</code> keyword is omitted in a period entry, an alert will be sent out every time a failure is detected. By default, if the summary output of two successive failures changes, then the alertevery interval is overridden, and an alert will be sent. If the string &quot;observe_detail&quot; is the last argument, then both the summary and detail output lines will be considered when comparing the output of successive failures. If the string &quot;strict&quot; is the last argument, then the output of the monitor or the state change of the service will have no effect on when alerts are sent. That is, &quot;alertevery 24h strict&quot; will send only one alert every 24 hours, no matter what. Please refer to the <code>ALERT DECISION LOGIC</code> section for a detailed explanation of how alerts are suppressed. </p>
<dt><code>alertafter</code><i> num</i></p>
<dd>
<dt><code>alertafter</code><i> num timeval</i></p>
<dd>
<dt><code>alertafter</code><i> timeval</i></p>
<dd>The <code>alertafter</code> keyword (within a <code>period</code> section) has three forms: only with the &quot;num&quot; argument, or with the &quot;num timeval&quot; arguments, or only with the &quot;timeval&quot; argument. In the first form, an alert will only be invoked after &quot;num&quot; consecutive failures. </p>
<p> In the second form, the arguments are a positive integer followed by an interval, as described by the <code>interval</code> variable above. If these parameters are specified, then the alerts for that period will only be called after that many failures happen within that interval. For example, if <code>alertafter</code> is given the arguments &quot;3 30m&quot;, then the alert will be called if 3 failures happen within 30 minutes. </p>
<p> In the third form, the argument is an interval, as described by the <code>interval</code> variable above. Alerts for that period will only be called if the service has been in a failure state for more than the length of time desribed by the interval, regardless of the number of failures noticed within that interval. </p>
<dt><code>numalerts</code><i> num</i></p>
<dd>This variable tells the server to call no more than <i>num</i> alerts during a failure. The alert counter is kept on a per-period basis, and is reset upon each success. </p>
<dt><code>no_comp_alerts</code></p>
<dd>If this option is specified, then upalerts will be called whenever the service state changes from failure to success, rather than only after a corresponding &quot;down&quot; alert. </p>
<dt><code>alert</code><i> alert [arg&#8230;]</i></p>
<dd>A period may contain multiple alerts, which are triggered upon failure of the service. An alert is specified with the <code>alert</code> keyword, followed by an optional <code>exit</code> parameter, and arguments which are interpreted the same as the <code>monitor</code> definition, but without the &quot;;;&quot; exception. The <code>exit</code> parameter takes the form of <code>exit=x</code> or <code>exit=x-y</code> and has the effect that the alert is only called if the exit status of the monitor script falls within the range of the <code>exit</code> parameter. If, for example, the alert line is <i>alert exit=10-20 mail.alert mis</i> then <i>mail-alert</i> will only be invoked with <i>mis</i> as its arguments if the monitor program&#8217;s exit value is between 10 and 20. This feature allows you to trigger different alerts at different severity levels (like when free disk space goes from 8% to 3%). </p>
<p> See the <code>ALERT PROGRAMS</code> section above for a list of the pramaeters mon will pass automatically to alert programs. </p>
<dt><code>upalert</code><i> alert [arg&#8230;]</i></p>
<dd>An <code>upalert</code> is the compliment of an <code>alert</code>. An upalert is called when a services makes the state transition from failure to success, if a corresponding &quot;down&quot; alert was previously sent. The <code>upalert</code> script is called supplying the same parameters as the <code>alert</code> script, with the addition of the <code>-u</code> parameter which is simply used to let an alert script know that it is being called as an upalert. Multiple upalerts may be specified for each period definition. Set the per-period <code>no_comp_alerts</code> option to send an upalert regardless if whether or not a &quot;down&quot; alert was sent. </p>
<dt><code>startupalert</code><i> alert [arg&#8230;]</i></p>
<dd>A <code>startupalert</code> is only called when the <code>mon</code> server starts execution, or when a &quot;reset&quot; command was issued to the server, depending on the setting of the <code>startupalerts_on_reset</code> global. Unlike other alerts, <code>startupalerts</code> are not called following the exit of a monitor, i.e. they are called in their own right, therefore the &quot;exit=&quot; argument is not applicable to <code>startupalert.</code> </p>
<dt><code>upalertafter</code><i> timeval</i></p>
<dd>The <code>upalertafter</code> parameter is specified as a string that follows the syntax of the <code>interval</code> parameter (&quot;30s&quot;, &quot;1m&quot;, etc.), and controls the triggering of an <code>upalert</code>. If a service comes back up after being down for a time greater than or equal to the value of this option, an <code>upalert</code> will be called. Use this option to prevent upalerts to be called because of &quot;blips&quot; (brief outages). </p>
</dl>
<h2>Authentication Configuration File</h2>
<p>The file specified by the <code>authfile</code> variable in the configuration file (or passed via the <code>-A</code> parameter) will be loaded upon startup. This file defines restrictions upon which client commands may be executed by which users. It is a text file which consists of comments, command definitions, and trap authentication parameters. A comment line begins with optional whitespace followed by pound sign. Blank lines are ignored. </p>
<p> The file is separated into a command section and a trap section. Sections are specified by a single line containing one of the following statements: </p>
<dl>
<dd>
<pre> command section</pre>
</dl>
<p> or </p>
<dl>
<dd>
<pre> trap section</pre>
</dl>
<p> Lines following one of the above statements apply to that section until either the end of the file or another section begins. </p>
<p> A command definition consists of a command, followed by a colon, followed by a comma-separated list of users who may execute the command. The default is that no users may execute any commands unless they are explicitly allowed in this configuration file. For clarity, a user can be denied by prefixing the user name with &quot;!&quot;. If the word &quot;AUTH_ANY&quot; is used for a username, then any authenticated user will be allowed to execute the command. If the word &quot;all&quot; is used for a username, then that command may be executed by any user, authenticated or not. </p>
<p> The trap section allows configuration of which users may send traps from which hosts. The syntax is a source host (name or ip address), whitespace, a username, whitespace, and a plaintext password for that user. If the source host is &quot;*&quot;, then allow traps from any host. If the username is &quot;*&quot;, then accept traps without regard for the username or password. If no hosts or users are specified, then no traps will be accepted. </p>
<p> An example configuration file: </p>
<dl>
<dd>
<pre>command section
list: all
reset: root,admin
loadstate: root
savestate: root
trap section
127.0.0.1 root r@@tp4sswrd</pre>
</dl>
<p> This means that all clients are able to perform the <code>list</code> command, &quot;root&quot; is able to perform &quot;reset&quot;, &quot;loadstate&quot;, &quot;savestate&quot;, and &quot;admin&quot; is able to execute the &quot;reset&quot; command.</p>
<h2>Client-Server Interface</h2>
<p>The server listens on TCP port 2583, which may be overridden using the <code>-p&nbsp;<wbr></code><i>port</i> option. Commands are a single line each, terminated by a newline. The server can handle any number of simultaneous client connections.</p>
<h2>Client Interface Commands</h2>
<p>See manual page for <code>moncmd</code>.</p>
<h2>Mon Trapping</h2>
<p>Mon has the facility to receive special &quot;mon traps&quot; from any local or remote machine. Currently, the only available method for sending mon traps are through the Mon::Client perl interface, though the UDP packet format is defined well enough to permit the writing of traps in other languages. </p>
<p> Traps are handled similarly to monitors: a trap sends an operational status, summary line, and description text, and mon generates an alert or upalert as necessary. </p>
<p> Traps can be caught by any watch/service group set up in the mon configuration file, however it is suggested that you configure watch/service groups specifically for the traps you expect to receive. When defining a special watch/service group for traps, do not include a &quot;monitor&quot; directive (as no monitor need be invoked). Since a monitor is not being invoked, it is not necessary for the watch definition to have a hostgroup which contains real host names. Just make up a useful name, and mon will automatically create the watch group for you. </p>
<p> Here is a simple config file example: </p>
<dl>
<dd>
<pre>watch trap-service
 service host1-disks
 description TRAP: for host1 disk status
 period wd {Sun-Sat}
 alert mail.alert someone [at] your.org
 upalert mail.alert -u someone [at] your.org</pre>
</dl>
<p> Since mon listens on a UDP port for any trap, a default facility is available for handling traps to unknown groups or services. To enable this facility, you must include a &quot;default&quot; watch group with a &quot;default&quot; service entry containing the specifics of alarms. If a default/default watch group and service are not configured, then unknown traps get logged via syslog, and no alarm is sent. <code>NOTE:</code> The default/default facility is a single entity as far as accounting and alarming go. Alarm programs which are not aware of this fact may send confusing information when a failure trap comes from one machine, followed by a success (ok) trap from a different machine. See the alarm environment variable <code>MON_TRAP_INTENDED</code> above for a possible way around this. It is intended that default/default be used as a facility to catch unknown traps, and should not be relied upon to catch all traps in a production environment. If you are lazy and only want to use default/default for catching all traps, it would be best to disable upalerts, and use the MON_TRAP_INTENDED environment variable in alert scripts to make the alerts more meaningful to you. </p>
<p> Here is an example default facility: </p>
<dl>
<dd>
<pre>watch default
 service default
 description Default trap service
 period wd {Sun-Sat}
 alert mail.alert someone [at] your.org
 upalert mail.alert -u someone [at] your.org</pre>
</dl>
<h2>Examples</h2>
<p>The <code>mon</code> distribution comes with an example configuration called <i>example.cf</i>. Refer to that file for more information. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-moncmd/">moncmd</a></code>(1), <code><a href="//www.systutorials.com/docs/linux/man/3pm-Time::Period/">Time::Period</a></code>(3pm), <code><a href="//www.systutorials.com/docs/linux/man/3pm-Mon::Client/">Mon::Client</a></code>(3pm)</p>
<h2>History</h2>
<p><code>mon</code> was written because I couldn&#8217;t find anything out there that did just what I needed, and nothing was worth modifying to add the features I wanted. It doesn&#8217;t have a cool name, and that bothers me because I couldn&#8217;t think of one.</p>
<h2>Bugs</h2>
<p>Report bugs to the email address below.</p>
<h2>Author</h2>
<p>Jim Trocki &lt;trockij [at] arctic.org&gt;</p>
