---
title: "yaws(1)"
name: "yaws"
section: "1"
letter: "y"
url: "/docs/linux/man/1-yaws/"
description: "yaws – yet another webserver"
---

<h2>NAME</h2>
<p> yaws &#8211; yet another webserver</p>
<h2>SYNOPSIS</h2>
<p> <code>yaws</code> [<i>OPTIONS</i>]</p>
<h2>DESCRIPTION</h2>
<p> Yaws is fast lightweight webserver. It can run as daemon or in interactive mode where it is possible to directly interact with the webserver. Yaws is particularly good at generating dynamic content. See the user docs for more information on that topic. </p>
<h2>DAEMON/SERVER options</h2>
<dl>
<dt><code>-i | &#8211;interactive</code></p>
<dd> Interactive mode. This will start yaws in interactive mode with an erlang prompt. All error_logger messages will be written to the tty as well in this mode. Use this when developing yaws code.</p>
<dt><code>-w | &#8211;winteractive</code></p>
<dd> Cygwin inteactive mode (werl)</p>
<dt><code>-D | &#8211;daemon</code></p>
<dd> Daemon mode. This will start yaws as a daemon.</p>
<dt><code>&#8211;heart</code></p>
<dd> This will cause the yaws system to be automatically restarted in case it should crash. This switch also requires the <i>&#8211;daemon</i> switch to be present.</p>
<dt><code>&#8211;heart-restart=C,T</code></p>
<dd> This controls the number of restarts in a given time period that heart tolerates before refusing to restart Yaws. By default, heart allows up to 5 restarts within a 60 second period before refusing to restart Yaws again. This option allows up to <i>C</i> restarts in <i>T</i> seconds instead. To allow infinite restarts, set both <i>C</i> and <i>T</i> to 0. This switch automatically enables the <i>&#8211;heart</i> switch.</p>
<dt><code>&#8211;debug</code></p>
<dd> Debug mode. This will produce some auxiliary error output for some error conditions. It will also start the otp sasl lib for additional error printouts.</p>
<dt><code>&#8211;nodebug</code></p>
<dd> Non-debug mode. This is useful for running interactively via the FI-i option but without incurring the performance penalties of debug mode. </p>
<dt><code>&#8211;conf file</code></p>
<dd> Use a different configuration file than the default. If the configuration parameter <i>config</i> is set, yaws use it as default configuration file. Else, The default configuration file when running as root is /etc/yaws/yaws.conf. When running as a non priviliged user, yaws will search for its configuration file in the following order. First in $HOME/yaws.conf, then in ./yaws.conf and finally in /etc/yaws/yaws.conf.</p>
<dt><code>&#8211;runmod module</code></p>
<dd> Tells yaws to call <i>module:start/0</i> at startup. This makes it possible to startup user specific applications together with yaws. </p>
<dt><code>&#8211;pa path</code></p>
<dd> Add path to the yaws system search path </p>
<dt><code>&#8211;tracetraf</code></p>
<dd> Traffic trace mode. All traffic will be written to a trace file called trace.traffic in the log directory. </p>
<dt><code>&#8211;tracehttp</code></p>
<dd> HTTP trace mode. All HTTP messages will be written to a trace file called trace.http in the log directory. </p>
<dt><code>&#8211;traceout</code></p>
<dd> When yaws is put into trace mode using either &#8211;tracetraf or &#8211;tracehttp, traces are written to files. If we provide the &#8211;traceout flag, the trace will also be written to stdout. </p>
<dt><code>&#8211;trace</code></p>
<dd> Sames as &#8211;tracetraf &#8211;traceout. I.e. trace everything and write to stdout. </p>
<dt><code>&#8211;mnesiadir dir</code></p>
<dd> Start Mnesia in directory &lt;dir&gt; </p>
<dt><code>&#8211;sname xxx</code></p>
<dd> Start yaws as a distributed erlang node with name &lt;xxx&gt; using the unqualified hostname as nodename postfix </p>
<dt><code>&#8211;disable-kpoll</code></p>
<dd> By default, yaws starts erlang with <i>+K true</i>. This flag reverses that. </p>
<dt><code>&#8211;name xxx</code></p>
<dd> Start yaws as a distributed erlang node with name &lt;xxx&gt; using the fully qualified hostname as nodename postfix </p>
<dt><code>&#8211;proto_dist Mod</code></p>
<dd> Use module Mod for erlang distribution. This is typically only used when we want to run erlang distribution over SSL. </p>
<dt><code>&#8211;erlarg STRING</code></p>
<dd> Pass STRING as an additional argument to the &quot;erl&quot; program. If STRING comprises multiple words, you must quote it so that your shell passes it to yaws as a single argument. If STRING contains any single quote characters, you must quote each of them as well. For example, to pass the option <i>-env NAME O&#8217;Keeffe</i> to &quot;erl&quot; from a Bourne-compatible shell:</dl>
<pre>
<center>
--erlarg &quot;-env NAME O\'Keeffe&quot;<br>
</center>
</pre>
<dl>
<dt><code>&#8211;id ID</code></p>
<dd> This flag sets the id. If we&#8217;re starting a daemon (or an interactive system) it gives the Yaws server the identity ID. This means that the server will write all internal files into the directory $HOME/.yaws/yaws/ID. </p>
<p> Yaws also creates a file called ${VARDIR}/run/yaws/ctl-${ID} which contains the portnumber the daemon is listening on for control request by the control command such as &quot;yaws &#8211;hup&quot; etc. </p>
<p> If we&#8217;re invoking a control command which should perform some control function on the daemon, we may have to give the &#8211;id flag also to the control command. If we don&#8217;t do this the control command may interact with the wrong daemon due to finding the wrong &quot;ctl&quot; file. </p>
<p> The daemon may also optionally specify the &quot;id&quot; in the yaws.conf configuration file. </p>
<dt><code>&#8211;umask MASK</code></p>
<dd> Set the umask for the daemon to MASK. </p>
</dl>
<h2>CONTROL OPTIONS</h2>
<p> The following list of options are are used to control the daemon from the &quot;outside&quot; while it is running. </p>
<dl>
<dt><code>&#8211;hup [&#8211;id ID]</code></p>
<dd> HUP the daemon. This forces the daemon to reread the configuration file. It also makes the daemon empty all its internal content caches. Hence when updating the doc root, HUPing the daemon is the fastest way to see the content updates.</p>
<dt><code>&#8211;stop [&#8211;id id]</code></p>
<dd> Stop the daemon (called id)</p>
<dt><code>&#8211;ls </code></p>
<dd> Lists current ids and status of all yaws servers on localhost. In practice this amounts to a listdir in $HOME/.yaws/yaws &#8211; and check whether the different systems who has created files there are alive.</p>
<dt><code>&#8211;status [&#8211;id id]</code></p>
<dd> Query a running yaws daemon for its status, and print it.</p>
<dt><code>&#8211;stats [&#8211;id id]</code></p>
<dd> Query a running yaws daemon for its statistics, and print it.</p>
<dt><code>&#8211;running-config [&#8211;id id]</code></p>
<dd> Query a running yaws daemon for its current configuration, and print it. This can be useful when attempting to figure out how to set config in embedded mode. Configure yaws to you liking in non-embedded mode, run this command and use the output to populate the embedded mode records.</p>
<dt><code>&#8211;load Modules [&#8211;id id]</code></p>
<dd> Try to (re)load erlang modules into a running daemon. This is useful after modifying appmods or modules used by scripts. </p>
<dt><code>&#8211;debug-dump [&#8211;id id]</code></p>
<dd> Produce a debug dump on stdout. In particular this code lists what we refer to as suspicious processes. I.e. processes that might be hanging or processes that are &quot;large&quot; &#8211; hardcoded to 40k words. </p>
<dt><code>&#8211;ctltrace [&#8211;id ID] http | traffic | off</code></p>
<dd> Control the trace capabilities of a running yaws daemon. If the http or traffic option is given, the daemon will write a log for debug purposes into the logdir. </p>
<dt><code>&#8211;wait-started[=T] [&#8211;id ID] </code></p>
<dd> Waits at most 30 seconds for the server to start. Exits with 0 if server is running, 1 otherwise. Typically useful in test scripts. The default 30 seconds can be modified by appending <i>=T</i> to the option, where <i>T</i> is the desired number of seconds to wait for the server to start. </p>
</dl>
<h2>MISC OPTIONS</h2>
<dl>
<dt><code>&#8211;check YawsFile [IncDirs &#8230;.]</code></p>
<dd> Test compile a `.yaws&#8217; file. Useful in Makefiles when we want to ensure that all .yaws files are syntactically correct</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit </p>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>HOME</code></p>
<dd> Is used to determine where we write the temporary files. By default all tmp files end up in $HOME/.yaws. This includes the JIT files that are the result of processed .yaws files and also the so called control file that is used by the daemon to write the port number to which it is listening for control commands such as &quot;yaws &#8211;status&quot; </p>
<p> Thus HOME is the handle we use in the control commands to find the control file so that we know where to connect to. </p>
<dt><code>YAWSHOME</code></p>
<dd> Can be used to override the HOME variable. This is useful when we for example are running yaws under port binding programs such as authpriv. </p>
<p> It&#8217;s useful by distros that don&#8217;t want Yaws to write any files ever in the HOME directory of root. </p>
</dl>
<h2>AUTHOR</h2>
<p> Written by Claes Wikstrom</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-yaws-conf/">yaws.conf</a></code>(5) <code><a href="/docs/linux/man/1-erl/">erl</a></code>(1) </p>
<h2>Index</h2>
