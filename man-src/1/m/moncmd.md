---
title: "moncmd(1)"
name: "moncmd"
section: "1"
letter: "m"
url: "/docs/linux/man/1-moncmd/"
description: "moncmd – send commands to mon daemon and show the results."
---

<h2>NAME</h2>
<p> moncmd &#8211; send commands to mon daemon and show the results.</p>
<h2>SYNOPSIS</h2>
<p> <code>moncmd</code> [<code>-a</code>] [<code>-d</code>] [<code>-l</code> <i>username</i>] [<code>-f</code> <i>file</i>] [<code>-s</code> <i>server</i>] [<code>-p</code> <i>port</i>] [<code>command</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code>moncmd</code> sends commands to the <code>mon</code> server.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></dt>
<dd> Authenticate with the server.</dd>
<dt><code>-d</code></dt>
<dd> enable debugging, which is the same as <code>-s</code> <i>localhost</i>.</dd>
<dt><code>-f </code><i>file</i></dt>
<dd> Read and execute commands from <i>file</i>.</dd>
<dt><code>-l </code><i>username</i></dt>
<dd> Supply <i>username</i> as the username while authenticating to the server.</dd>
<dt><code>-s&nbsp;<wbr></code><i>server</i></dt>
<dd> Connect to <i>server</i>.</dd>
<dt><code>-p&nbsp;<wbr></code><i>port</i></dt>
<dd> Use TCP port <i>port</i> when connecting to the server, instead of the default of 32777. </dd>
</dl>
<h2>MONITOR HOST</h2>
<p> <code>moncmd</code> will use the host specified by the <code>-s</code> parameter as the server. If there is no <code>-s</code> parameter it will use the host specified in the MONHOST environment variable. If there is no host in either of these locations it will exit with an error. </p>
<h2>BATCH OPERATION</h2>
<p> If no commands are supplied to <code>moncmd</code> on the command line, then commands will be taken from either standard input, or from the file specified by the -f parameter. If standard input is connected to a TTY and the -a option is supplied, then it will prompt for a password. If the -a option is supplied without the -f option and standard input is not a TTY, then the username and password are read from standard input using the syntax &quot;USER=username&quot; and &quot;PASS=password&quot;. The remaining input lines are interpreted as commands to send to the server. <code>moncmd</code> will not take usernames or passwords from a file, for obvious security reasons. </p>
<p> If the username is neither supplied by the -l parameter or through standard input, it is taken from the effective user ID of the current process. </p>
<h2>COMMANDS</h2>
<p> The following is a list of the commands that the server understands.</p>
<dl>
<dt><code>enable | disable service </code><i>group</i><i>servicename</i></dt>
<dd> Enables/disables alerts for <i>group</i> and <i>servicename</i>. All disabled states are automatically saved to the state file, which may optionally be re-loaded upon restarting or initial startup of the server. </dd>
<dt><code>ack </code><i>group service comment</i></dt>
<dd> Acknowledge a failure condition. This will store <i>comment</i> in the state of service (queryable by doing a <i>list opstatus</i> command), and will surppress further alerts for the service. Once the service returns to a non-failure state, then the acknowledgement is reset. </dd>
<dt><code>version</code></dt>
<dd> Displays the protocol version in the form of &quot;version <code>num</code> where <code>num</code> is the protocol version number. </dd>
<dt><code>list aliases</code></dt>
<dd> Lists aliases. </dd>
<dt><code>list aliasgroups</code></dt>
<dd> Lists alias groups. </dd>
<dt><code>savestate</code></dt>
<dd> Save the state of the server. Currently, the only state which is saved is the host/watches/services which are disabled. </dd>
<dt><code>loadstate</code></dt>
<dd> Load the state of the server. Currently, the only state which is loaded is the host/watches/services which are disabled. </dd>
<dt><code>enable | disable host </code><i>hostname</i></dt>
<dd> Enables/disables host <i>hostname</i> in all groups. When the monitor is called, this hostname will not be included in the list of hostnames sent to the monitor. If a group has only one hostname in it, then the <code>enable | disable watch</code> command should be used instead. </dd>
<dt><code>enable | disable watch </code><i>watchgroup</i></dt>
<dd> Enables/disables an entire watch for <i>watchgroup</i>, as defined in the configuration file. Disabling a watch not only stops alerts from happening, but it stops the actual monitor processes from being scheduled. </dd>
<dt><code>reset</code></dt>
<dd> Resets the server, forcing it to re-read the configuration file, kill off currently running monitors, restart all monitoring, and reset all counters. This command is only accessible if <code>moncmd</code> connects from the host which is running the <code>mon</code> server.</dd>
<dt><code>reset stopped</code></dt>
<dd> Resets the server and immediately stops the scheduler. This is an atomic version of the commands <code>reset</code> and <code>stop</code>. </dd>
<dt><code>reload auth</code></dt>
<dd> Reloads the auth.cf file in order to incorporate any new changes. The auth table is completely re-generated; it is not merged. </dd>
<dt><code>reset keepstate</code></dt>
<dd> If the word &quot;keepstate&quot; comes after the reset command, the server will do a &quot;loadstate&quot; right after the reset, before the scheduler kicks back in. </dd>
<dt><code>stop</code></dt>
<dd> Stops the scheduler, but continues to allow client connections. </dd>
<dt><code>start</code></dt>
<dd> Re-starts the scheduler after it has been stopped. </dd>
<dt><code>test monitor </code><i>group</i><i>servicename</i></dt>
<dd> Triggers a test for <i>group</i> and <i>service</i> immediately by setting the service&#8217;s countdown timer to zero. </dd>
<dt><code>test (alert | upalert | startupalert) </code><i>group</i><i>servicename</i><i>retval</i><i>period</i></dt>
<dd> Triggers a test alert, upalert, or startupalert for <i>group</i> and <i>servicename</i>. <i>retval</i> is the integer exit value to pass to the alert via the MON_RETVAL environment variable. You must also specify the <i>period</i> as it appears in the configuration file. All alerts of the given type in that period will be triggered, but the alert will not be logged. </dd>
<dt><code>servertime</code></dt>
<dd> Returns the current time of the server as seconds since Jan 1, 1970. </dd>
<dt><code>list group </code><i>groupname</i></dt>
<dd> Lists the members of group <i>groupname</i>. </dd>
<dt><code>list descriptions</code></dt>
<dd> List the descriptions of each service, as defined in the configuration file. If a service description is undefined, then it is not listed. </dd>
<dt><code>list alerthist</code></dt>
<dd> Lists the last alarms triggered for each service of each watch group, in addition to the summary output. The number of alerts to keep in memory is bounded by the <i>maxkeep</i> variable, configurable on the <code>mon</code> command line at startup, and expandable with the <code>set</code> command during runtime. </dd>
<dt><code>list failurehist</code></dt>
<dd> Lists the last failures, in addition to the summary output. This is also limited by the <i>maxkeep</i> variable. </dd>
<dt><code>list opstatus</code></dt>
<dd> Lists operational status of all services. Reports whether the last time a service group was tested resulted in success or failure. The output is: </dd>
<pre>
group service untested
group service time timeleft succeeded
group service time timeleft failed output
</pre>
<p> where <i>output</i> is the first line of output from the monitor script which failed, <i>time</i> is the time that the condition was last noticed in <code><a href="/docs/linux/man/2-time/">time</a></code>(2) format, and <i>timeleft</i> is the number of seconds left until the service is tested again. </p>
<dt><code>list successes</code></dt>
<dd> Generates the same output as the <code>list opstatus</code> command, but only shows the services that have succeeded the last time they were tested. </dd>
<dt><code>list failures</code></dt>
<dd> Generates the same output as the <code>list opstatus</code> command, but only shows the services that have failed the last time they were tested. </dd>
<dt><code>list disabled</code></dt>
<dd> Lists all hosts and services which have been disabled by the <code>disable host|service</code> command. </dd>
<dt><code>list pids</code></dt>
<dd> Shows the currently active watch groups/services along with their process IDs, and it process ID of the server daemon. </dd>
<dt><code>list watch</code></dt>
<dd> Lists all watches and services. </dd>
<dt><code>list state</code></dt>
<dd> Lists the state of the scheduler. </dd>
<dt><code>set </code><i>group</i><i>service</i><i>variable</i><i>value</i></dt>
<dd> Sets a variable to value. Useful for temporarily changing an interval or alertevery value. Be careful, because this can just set any value in the %watch hash, and some values that are specified in the configuration file like &quot;10m&quot; or &quot;35s&quot; are converted and stored as just plain integer seconds (e.g. &quot;alertevery&quot;). </dd>
<dt><code>get </code><i>group</i><i>service</i><i>variable</i></dt>
<dd> Displays the value of group service variable. </dd>
<dt><code>set </code><i>variable</i><i>value</i></dt>
<dd> Assigns <i>value</i> to the global variable <i>variable</i>. </dd>
<dt><code>set opstatus </code><i>group</i><i>service</i><i>value</i></dt>
<dd> Sets the opstatus value for <i>group</i> and <i>service.</i> </dd>
<dt><code>get </code><i>variable</i></dt>
<dd> Shows the value of global variable <i>variable</i>. </dd>
<dt><code>term</code></dt>
<dd> Terminates the server. This command is only accessible if <code>moncmd</code> connects from the host which is running the <code>mon</code> server. </dd>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt>MONSERVER</dt>
<dd> The hostname of the server which runs the <code>mon</code> process.</dd>
<dt>MONPORT</dt>
<dd> The port number to connect to. </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/8-mon/">mon</a>(8)</p>
<h2>BUGS</h2>
<p> Report bugs to the email address below.</p>
<h2>AUTHOR</h2>
<p> Jim Trocki &lt;trockij [at] arctic.org&gt; </p>
