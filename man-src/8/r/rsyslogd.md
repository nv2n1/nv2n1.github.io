---
title: "rsyslogd(8)"
name: "rsyslogd"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rsyslogd/"
description: "rsyslogd – reliable and extended syslogd"
---

<p>rsyslogd &#8211; reliable and extended syslogd</p>
<h2>Synopsis</h2>
<p><code>rsyslogd</code> [<code> -d </code>] [<code> -D </code>] [<code> -f </code> <i>config file</i> ] [<code> -i </code> <i>pid file</i> ] [<code> -n </code>] [<code> -N </code> <i>level</i> ] [<code> -o </code> <i>fullconf</i> ] [<code> -C </code>] [<code> -v </code>] </p>
<h2>Description</h2>
<p><code>Rsyslogd</code> is a system utility providing support for message logging. Support of both internet and unix domain sockets enables this utility to support both local and remote logging. <code>Note that this version of rsyslog ships with extensive documentation in HTML format.</code> This is provided in the ./doc subdirectory and probably in a separate package if you installed rsyslog via a packaging system. To use rsyslog&#8217;s advanced features, you <code>need</code> to look at the HTML documentation, because the man pages only covers basic aspects of operation. <code>For details and configuration examples, see the rsyslog.conf (5)</code> <code>man page and the online documentation at <a rel="nofollow" href="https://www.rsyslog.com/doc/">https://www.rsyslog.com/doc/</a></code> <code><a href="/docs/linux/man/8-rsyslogd/">Rsyslogd</a></code>(8) is derived from the sysklogd package which in turn is derived from the stock BSD sources. <code>Rsyslogd</code> provides a kind of logging that many modern programs use. Every logged message contains at least a time and a hostname field, normally a program name field, too, but that depends on how trusty the logging program is. The rsyslog package supports free definition of output formats via templates. It also supports precise timestamps and writing directly to databases. If the database option is used, tools like phpLogCon can be used to view the log data. While the <code>rsyslogd</code> sources have been heavily modified a couple of notes are in order. First of all there has been a systematic attempt to ensure that rsyslogd follows its default, standard BSD behavior. Of course, some configuration file changes are necessary in order to support the template system. However, rsyslogd should be able to use a standard syslog.conf and act like the original syslogd. However, an original syslogd will not work correctly with a rsyslog-enhanced configuration file. At best, it will generate funny looking file names. The second important concept to note is that this version of rsyslogd interacts transparently with the version of syslog found in the standard libraries. If a binary linked to the standard shared libraries fails to function correctly we would like an example of the anomalous behavior. The main configuration file <i>/etc/rsyslog.conf</i> or an alternative file, given with the <code>-f</code> option, is read at startup. Any lines that begin with the hash mark (&#8220;#&#8221;) and empty lines are ignored. If an error occurs during parsing the error element is ignored. It is tried to parse the rest of the line. </p>
<h2>Options</h2>
<dl>
<dt><code>-D</code></p>
<dd>Runs the Bison config parser in debug mode. This may help when hard to find syntax errors are reported. Please note that the output generated is deeply technical and orignally targeted towards developers.</p>
<dt><code>-d</code></p>
<dd>Turns on debug mode. See the DEBUGGING section for more information.</p>
<dt><code>-f </code><i>config file</i></p>
<dd>Specify an alternative configuration file instead of <i>/etc/rsyslog.conf</i>, which is the default.</p>
<dt><code>-i </code><i>pid file</i></p>
<dd>Specify an alternative pid file instead of the default one. This option must be used if multiple instances of rsyslogd should run on a single machine. To disable writing a pid file, use the reserved name &quot;NONE&quot; (all upper case!), so &quot;-iNONE&quot;.</p>
<dt><code>-n</code></p>
<dd>Avoid auto-backgrounding. This is needed especially if the <code>rsyslogd</code> is started and controlled by <code><a href="/docs/linux/man/8-init/">init</a></code>(8).</p>
<dt><code>-N level</code></p>
<dd>Do a config check. Do NOT run in regular mode, just check configuration file correctness. This option is meant to verify a config file. To do so, run rsyslogd interactively in foreground, specifying -f &lt;config-file&gt; and -N level. The level argument modifies behaviour. Currently, 0 is the same as not specifying the -N option at all (so this makes limited sense) and 1 actually activates the code. Later, higher levels will mean more verbosity (this is a forward-compatibility option).</p>
<dt><code>-o fullconf</code></p>
<dd>Generates a consolidated config file <i>fullconf</i> that contains all of rsyslog&#8217;s configuration in a single file. Include files are exploded into that file in exactly the way rsyslog sees them. This option is useful for troubleshooting, especially if problems with the order of action processing is suspected. It may also be used to check for &quot;unexepectedly&quot; included config content.</p>
<dt><code>-C</code></p>
<dd>This prevents rsyslogd from changing to the root directory. This is almost never a good idea in production use. This option was introduced in support of the internal testbed.</p>
<dt><code>-v</code></p>
<dd>Print version and exit.</dl>
<h2>Signals</h2>
<p><code>Rsyslogd</code> reacts to a set of signals. You may easily send a signal to <code>rsyslogd</code> using the following:</p>
<dl>
<dd>
<pre>kill -SIGNAL $(cat /var/run/rsyslogd.pid)</pre>
</dl>
<p> Note that -SIGNAL must be replaced with the actual signal you are trying to send, e.g. with HUP. So it then becomes:</p>
<dl>
<dd>
<pre>kill -HUP $(cat /var/run/rsyslogd.pid)</pre>
</dl>
<dl>
<dt><code>HUP</code></p>
<dd>This lets <code>rsyslogd</code> perform close all open files.</p>
<dt><code>TERM , INT , QUIT</code></p>
<dd><code>Rsyslogd</code> will die.</p>
<dt><code>USR1</code></p>
<dd>Switch debugging on/off. This option can only be used if <code>rsyslogd</code> is started with the <code>-d</code> debug option.</p>
<dt><code>CHLD</code></p>
<dd>Wait for childs if some were born, because of wall&#8217;ing messages.</dl>
<h2>Security Threats</h2>
<p>There is the potential for the rsyslogd daemon to be used as a conduit for a denial of service attack. A rogue program(mer) could very easily flood the rsyslogd daemon with syslog messages resulting in the log files consuming all the remaining space on the filesystem. Activating logging over the inet domain sockets will of course expose a system to risks outside of programs or individuals on the local machine. </p>
<p> There are a number of methods of protecting a machine:</p>
<dl>
<dt>1.</p>
<dd>Implement kernel firewalling to limit which hosts or networks have access to the 514/UDP socket.</p>
<dt>2.</p>
<dd>Logging can be directed to an isolated or non-root filesystem which, if filled, will not impair the machine.</p>
<dt>3.</p>
<dd>The ext2 filesystem can be used which can be configured to limit a certain percentage of a filesystem to usage by root only. <code>NOTE</code> that this will require rsyslogd to be run as a non-root process. <code>ALSO NOTE</code> that this will prevent usage of remote logging on the default port since rsyslogd will be unable to bind to the 514/UDP socket.</p>
<dt>4.</p>
<dd>Disabling inet domain sockets will limit risk to the local machine.</dl>
<h3>Message replay and spoofing</h3>
<p>If remote logging is enabled, messages can easily be spoofed and replayed. As the messages are transmitted in clear-text, an attacker might use the information obtained from the packets for malicious things. Also, an attacker might replay recorded messages or spoof a sender&#8217;s IP address, which could lead to a wrong perception of system activity. These can be prevented by using GSS-API authentication and encryption. Be sure to think about syslog network security before enabling it.</p>
<h2>Debugging</h2>
<p>When debugging is turned on using the <code>-d</code> option, <code>rsyslogd</code> produces debugging information according to the <code>RSYSLOG_DEBUG</code> environment variable and the signals received. When run in foreground, the information is written to stdout. An additional output file can be specified using the <code>RSYSLOG_DEBUGLOG</code> environment variable.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/rsyslog.conf</i></p>
<dd>Configuration file for <code>rsyslogd</code>. See <code><a href="/docs/linux/man/5-rsyslog-conf/">rsyslog.conf</a></code>(5) for exact information.</p>
<dt><i>/dev/log</i></p>
<dd>The Unix domain socket to from where local syslog messages are read.</p>
<dt><i>/var/run/rsyslogd.pid</i></p>
<dd>The file containing the process id of <code>rsyslogd</code>.</p>
<dt><i>prefix/lib/rsyslog</i></p>
<dd>Default directory for <code>rsyslogd</code> modules. The <i>prefix</i> is specified during compilation (e.g. /usr/local).</dl>
<h2>Environment</h2>
<dl>
<dt><code>RSYSLOG_DEBUG</code></p>
<dd>Controls runtime debug support. It contains an option string with the following options possible (all are case insensitive): </p>
<dl>
<dd>
<dl>
<dt>Debug</p>
<dd>Turns on debugging and prevents forking. This is processed earlier in the startup than command line options (i.e. -d) and as such enables earlier debugging output. Mutually exclusive with DebugOnDemand.</p>
<dt>DebugOnDemand</p>
<dd>Enables debugging but turns off debug output. The output can be toggled by sending SIGUSR1. Mutually exclusive with Debug.</p>
<dt>LogFuncFlow</p>
<dd>Print out the logical flow of functions (entering and exiting them)</p>
<dt>FileTrace</p>
<dd>Specifies which files to trace LogFuncFlow. If not set (the default), a LogFuncFlow trace is provided for all files. Set to limit it to the files specified.FileTrace may be specified multiple times, one file each (e.g. export RSYSLOG_DEBUG=&quot;LogFuncFlow FileTrace=vm.c FileTrace=expr.c&quot;</p>
<dt>PrintFuncDB</p>
<dd>Print the content of the debug function database whenever debug information is printed (e.g. abort case)!</p>
<dt>PrintAllDebugInfoOnExit</p>
<dd>Print all debug information immediately before rsyslogd exits (currently not implemented!)</p>
<dt>PrintMutexAction</p>
<dd>Print mutex action as it happens. Useful for finding deadlocks and such.</p>
<dt>NoLogTimeStamp</p>
<dd>Do not prefix log lines with a timestamp (default is to do that).</p>
<dt>NoStdOut</p>
<dd>Do not emit debug messages to stdout. If RSYSLOG_DEBUGLOG is not set, this means no messages will be displayed at all.</p>
<dt>Help</p>
<dd>Display a very short list of commands &#8211; hopefully a life saver if you can&#8217;t access the documentation&#8230;</dl>
</dl>
<dt><code>RSYSLOG_DEBUGLOG</code></p>
<dd>If set, writes (almost) all debug message to the specified log file in addition to stdout.</p>
<dt><code>RSYSLOG_MODDIR</code></p>
<dd>Provides the default directory in which loadable modules reside.</dl>
<h2>Bugs</h2>
<p>Please review the file BUGS for up-to-date information on known bugs and annoyances.</p>
<h2>Further Information</h2>
<p>Please visit <code><a rel="nofollow" href="https://www.rsyslog.com/doc/">https://www.rsyslog.com/doc/</a></code> for additional information, tutorials and a support forum.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-rsyslog-conf/">rsyslog.conf</a></code>(5), <code><a href="/docs/linux/man/1-logger/">logger</a></code>(1), <code><a href="/docs/linux/man/2-syslog/">syslog</a></code>(2), <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3), <code><a href="/docs/linux/man/5-services/">services</a></code>(5), <code><a href="/docs/linux/man/8-savelog/">savelog</a></code>(8) </p>
<h2>Collaborators</h2>
<p><code>rsyslogd</code> is derived from sysklogd sources, which in turn was taken from the BSD sources. Special thanks to Greg Wettstein (greg [at] wind.enjellic.com) and Martin Schulze (joey [at] linux.de) for the fine sysklogd package. </p>
<dl>
<dt>Rainer Gerhards</p>
<dd>
<dt>Adiscon GmbH</p>
<dd>
<dt>Grossrinderfeld, Germany</p>
<dd>
<dt>rgerhards [at] adiscon.com</p>
<dd></dl>
