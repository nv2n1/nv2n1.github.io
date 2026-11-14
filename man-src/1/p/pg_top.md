---
title: "pg_top(1)"
name: "pg_top"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pg_top/"
description: "pg_top – display and update information about the top cpu PostgreSQL processes"
---

<h2 class="name">NAME</h2>
<p> pg_top &#8211; display and update information about the top cpu PostgreSQL processes </p>
<h2>SYNOPSIS</h2>
<p> <code>pg_top</code> [ OPTIONS ] [ NUMBER ]</p>
<h2>DESCRIPTION</h2>
<p> <i>pg_top</i> displays the top processes on the system and periodically updates this information. Raw cpu percentage is used to rank the processes. If <i>number</i> is given, then the top <i>number</i> processes will be displayed instead of the default. </p>
<p> <i>pg_top</i> makes a distinction between terminals that support advanced capabilities and those that do not. This distinction affects the choice of defaults for certain options. In the remainder of this document, an &quot;intelligent&quot; terminal is one that supports cursor addressing, clear screen, and clear to end of line. Conversely, a &quot;dumb&quot; terminal is one that does not support such features. If the output of <i>pg_top</i> is redirected to a file, it acts as if it were being run on a dumb terminal.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-C, &#8211;color-mode</code></p>
<dd> Turn off the use of color in the display.</p>
<dt><code>-I, &#8211;hide-idle</code></p>
<dd> Do not display idle processes. By default, pg_top displays both active and idle processes.</p>
<dt><code>-T, &#8211;show-tags</code></p>
<dd> List all available color tags and the current set of tests used for color highlighting, then exit.</p>
<dt><code>-W, &#8211;password</code></p>
<dd> Forces pg_top to prompt for a password before connecting to a database.</p>
<dt><code>-b, &#8211;batch</code></p>
<dd> Use &quot;batch&quot; mode. In this mode, all input from the terminal is ignored. Interrupt characters (such as ^C and ^\) still have an effect. This is the default on a dumb terminal, or when the output is not a terminal.</p>
<dt><code>-c, &#8211;show-command</code></p>
<dd> Show the command name for each process. Default is to show the full command line. This option is not supported on all platforms.</p>
<dt><code>-i, &#8211;interactive</code></p>
<dd> Use &quot;interactive&quot; mode. In this mode, any input is immediately read for processing. See the section on &quot;Interactive Mode&quot; for an explanation of which keys perform what functions. After the command is processed, the screen will immediately be updated, even if the command was not understood. This mode is the default when standard output is an intelligent terminal.</p>
<dt><code>-n, &#8211;non-interactive</code></p>
<dd> Use &quot;non-interactive&quot; mode. This is indentical to &quot;batch&quot; mode.</p>
<dt><code>-q, &#8211;quick-mode</code></p>
<dd> Renice <i>pg_top</i> to -20 so that it will run faster. This can be used when the system is being very sluggish to improve the possibility of discovering the problem. This option can only be used by root.</p>
<dt><code>-r, &#8211;remote-mode</code></p>
<dd> Monitor a remote database where the database is on a system other than where pg_top is running from. <i>pg_top</i> will monitor a remote database if it has the pg_proctab extension installed.</p>
<dt><code>-u, &#8211;show-uid</code></p>
<dd> Do not take the time to map uid numbers to usernames. Normally, <i>pg_top</i> will read as much of the file &quot;/etc/passwd&quot; as is necessary to map all the user id numbers it encounters into login names. This option disables all that, while possibly decreasing execution time. The uid numbers are displayed instead of the names.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Write version number information to stderr then exit immediately. No other processing takes place when this option is used. To see current revision information while pg_top is running, use the help command &quot;?&quot;.</p>
<dt><code>-s </code><i>TIME</i>, <code>&#8211;set-delay=</code><i>TIME</i></p>
<dd> <i>TIME</i> Set the delay between screen updates to <i>TIME</i> seconds. The default delay between updates is seconds.</p>
<dt><code>-o </code><i>FIELD</i>, <code>&#8211;order-field=</code><i>FIELD</i></p>
<dd> Sort the process display area on the specified field. The field name is the name of the column as seen in the output, but in lower case. Likely values are &quot;cpu&quot;, &quot;size&quot;, &quot;res&quot;, and &quot;time&quot;, but may vary on different operating systems. Note that not all operating systems support this option.</p>
<dt><code>-x </code><i>COUNT</i>, <code>&#8211;set-display=</code><i>COUNT</i></p>
<dd> Show only <i>count</i> displays, then exit. A display is considered to be one update of the screen. This option allows the user to select the number of displays he wants to see before <i>pg_top</i> automatically exits. For intelligent terminals, no upper limit is set. The default is 1 for dumb terminals.</p>
<dt><code>-z </code><i>USERNAME</i>, <code>&#8211;show-username=</code><i>USERNAME</i></p>
<dd> Show only those processes owned by <i>USERNAME</i>. This option currently only accepts usernames and will not understand uid numbers.</p>
<dt><code>-h </code><i>HOST</i>, <code>&#8211;host=</code><i>HOST</i></p>
<dd> Specifies the host name of the machine on which the server is running. If the value begins with a slash, it is used as the directory for the Unix domain socket. The default is taken from the PGHOST environment variable, if set.</p>
<dt><code>-p </code><i>PORT</i>, <code>&#8211;port=</code><i>PORT</i></p>
<dd> Specifies the TCP port or local Unix domain socket file extension on which the server is listening for connections. Defaults to the PGPORT environment variable, if set.</p>
<dt><code>-U </code><i>USERNAME</i>, <code>&#8211;username=</code><i>USERNAME</i></p>
<dd> User name to connect as.</p>
<dt><code>-W, &#8211;password</code></p>
<dd> Force pg_top to prompt for a password before connecting to a database.</dl>
<p> Both <i>COUNT</i> and <i>NUMBER</i> fields can be specified as &quot;infinite&quot;, indicating that they can stretch as far as possible. This is accomplished by using any proper prefix of the keywords &quot;infinity&quot;, &quot;maximum&quot;, or &quot;all&quot;. The default for <i>count</i> on an intelligent terminal is, in fact, <code>infinity</code><i>.</i> </p>
<p> The environment variable <code>PG_TOP</code> is examined for options before the command line is scanned. This enables a user to set his or her own defaults. The number of processes to display can also be specified in the environment variable <code>PG_TOP</code>. The options <code>-C</code>, <code>-I</code>, and <code>-u</code> are actually toggles. A second specification of any of these options will negate the first. Thus a user who has the environment variable <code>PG_TOP</code> set to &quot;-I&quot; may use the command &quot;top -I&quot; to see idle processes.</p>
<h2>INTERACTIVE MODE</h2>
<p> When <i>pg_top</i> is running in &quot;interactive mode&quot;, it reads commands from the terminal and acts upon them accordingly. In this mode, the terminal is put in &quot;CBREAK&quot;, so that a character will be processed as soon as it is typed. Almost always, a key will be pressed when <i>pg_top</i> is between displays; that is, while it is waiting for <i>time</i> seconds to elapse. If this is the case, the command will be processed and the display will be updated immediately thereafter (reflecting any changes that the command may have specified). This happens even if the command was incorrect. If a key is pressed while <i>pg_top</i> is in the middle of updating the display, it will finish the update and then process the command. Some commands require additional information, and the user will be prompted accordingly. While typing this information in, the user&#8217;s erase and kill keys (as set up by the command <i>stty</i>) are recognized, and a newline terminates the input. </p>
<p> These commands are currently recognized (^L refers to control-L):</p>
<dl>
<dt><code>^L</code></p>
<dd> Redraw the screen.</p>
<dt><code>A</code></p>
<dd> Display the actual query plan (EXPLAIN ANALYZE) of the currently running SQL statement by re-running the SQL statement (prompt for process id.)</p>
<dt><code>C</code></p>
<dd> Toggle the use of color in the display.</p>
<dt><code>c</code></p>
<dd> Toggle the display of the full command line.</p>
<dt><code>d</code></p>
<dd> Change the number of displays to show (prompt for new number). Remember that the next display counts as one, so typing <code>d1</code> will make <i>pg_top</i> show one final display and then immediately exit.</p>
<dt><code>h</code>&nbsp;<wbr>or&nbsp;<wbr><code>?</code></p>
<dd> Display a summary of the commands (help screen). Version information is included in this display.</p>
<dt><code>E</code></p>
<dd> Display re-determined execution plan (EXPLAIN) of the SQL statement by a backend process (prompt for process id.)</p>
<dt><code>e</code></p>
<dd> Display a list of system errors (if any) generated by the last <code>k</code>ill or <code>r</code>enice command.</p>
<dt><code>i</code></p>
<dd> (or <code>I</code>) Toggle the display of idle processes.</p>
<dt><code>k</code></p>
<dd> Send a signal (&quot;kill&quot; by default) to a list of processes. This acts similarly to the command <i><a href="/docs/linux/man/1-kill/">kill</a></i>(1)).</p>
<dt><code>L</code></p>
<dd> Display the currently held locks by a backend process (prompt for process id.)</p>
<dt><code>M</code></p>
<dd> Order by memory utilization.</p>
<dt><code>N</code></p>
<dd> Sort by process id.</p>
<dt><code>n or #</code></p>
<dd> Change the number of processes to display (prompt for new number).</p>
<dt><code>o</code></p>
<dd> Change the order in which the display is sorted. This command is not available on all systems. The sort key names when viewing processes vary fron system to system but usually include: &quot;cpu&quot;, &quot;res&quot;, &quot;size&quot;, &quot;time&quot;. The default is cpu. When viewing user table statistics: &quot;seq_scan&quot;, &quot;seq_tup_read&quot;, &quot;idx_scan&quot;, &quot;idx_tup_fetch&quot;, &quot;n_tup_ins&quot;, &quot;n_tup_upd&quot;, &quot;n_tup_del&quot;. The default is seq_scan. When viewing user index statistics: &quot;idx_scan&quot;, &quot;idx_tup_fetch&quot;, &quot;idx_tup_read&quot;. The default is idx_scan.</p>
<dt><code>P</code></p>
<dd> Sort by processor utilization.</p>
<dt><code>Q</code></p>
<dd> Display the currently running query of a backend process (prompt for process id.)</p>
<dt><code>q</code></p>
<dd> Quit <i>pg_top.</i></p>
<dt><code>R</code></p>
<dd> Display user table statistics.</p>
<dt><code>r</code></p>
<dd> Change the priority (the &quot;nice&quot;) of a list of processes. This acts similarly to the command <i><a href="/docs/linux/man/8-renice/">renice</a></i>(8)).</p>
<dt><code>s</code></p>
<dd> Change the number of seconds to delay between displays (prompt for new number).</p>
<dt><code>T</code></p>
<dd> Order by time.</p>
<dt><code>t</code></p>
<dd> Toggle between cumulative or differential statistics when viewing user table or user index statistics.</p>
<dt><code>u</code></p>
<dd> Display only processes owned by a specific username (prompt for username). If the username specified is simply &quot;+&quot;, then processes belonging to all users will be displayed.</p>
<dt><code>X</code></p>
<dd> Display user index statistics.</dl>
<h2>THE DISPLAY</h2>
<p> The actual display varies depending on the specific variant of Unix that the machine is running. This description may not exactly match what is seen by pg_top running on this particular machine. Differences are listed at the end of this manual entry. </p>
<p> The top few lines of the display show general information about the state of the system, including the last process id assigned to a process (on most systems), the three load averages, the current time, the number of existing processes, the number of processes in each state (sleeping, running, starting, zombies, and stopped), and a percentage of time spent in each of the processor states (user, nice, system, and idle). It also includes information about physical and virtual memory allocation. </p>
<p> The remainder of the screen displays information about individual processes. This display is similar in spirit to <i><a href="/docs/linux/man/1-ps/">ps</a></i>(1) but it is not exactly the same. The columns displayed by pg_top will differ slightly between operating systems. Generally, the following fields are displayed:</p>
<dl>
<dt><code>PID</code></p>
<dd> The process id.</p>
<dt><code>USERNAME</code></p>
<dd> Username of the process&#8217;s owner (if <code>-u</code> is specified, a UID column will be substituted for USERNAME).</p>
<dt><code>PRI</code></p>
<dd> Current priority of the process.</p>
<dt><code>NICE</code></p>
<dd> Nice amount in the range -20 to 20, as established by the use of the command <i>nice</i>.</p>
<dt><code>SIZE</code></p>
<dd> Total size of the process (text, data, and stack) given in kilobytes.</p>
<dt><code>RES</code></p>
<dd> Resident memory: current amount of process memory that resides in physical memory, given in kilobytes.</p>
<dt><code>STATE</code></p>
<dd> Current state (typically one of &quot;sleep&quot;, &quot;run&quot;, &quot;idl&quot;, &quot;zomb&quot;, or &quot;stop&quot;).</p>
<dt><code>TIME</code></p>
<dd> Number of system and user cpu seconds that the process has used.</p>
<dt><code>CPU</code></p>
<dd> Percentage of available cpu time used by this process.</p>
<dt><code>COMMAND</code></p>
<dd> Name of the command that the process is currently running.</dl>
<h2>COLOR</h2>
<p> pg_top supports the use of ANSI color in its output. By default, color is available but not used. The environment variable <code>TOPCOLORS</code> specifies colors to use and conditions for which they should be used. At the present time, only numbers in the summay display area can be colored. In a future version it will be possible to highlight numbers in the process display area as well. The environment variable is the only way to specify color: there is no equivalent command line option. Note that the environment variable <code>TOPCOLOURS</code> is also understood. The British spelling takes precedence. The use of color only works on terminals that understand and process ANSI color escape sequences. </p>
<p> The environment variable is a sequence of color specifications, separated by colons. Each specification takes the form tag=min,max#code where <i>tag</i> is the name of the value to check, <i>min</i> and <i>max</i> specify a range for the value, and <i>code</i> is an ANSI color code. Multiple color codes can be listed and separated with semi-colons. A missing <i>min</i> implies the lowest possible value (usually 0) and a missing <i>max</i> implies infinity. The comma must always be present. When specifying numbers for load averages, they should be multiplied by 100. For example, the specification <code>1min=500,1000#31</code> indicates that a 1 minute load average between 5 and 10 should be displayed in red. Color attributes can be combined. For example, the specification <code>5min=1000,#37;41</code> indicates that a 5 minute load average higher than 10 should be displayed with white characters on a red background. A special tag named <i>header</i> is used to control the color of the header for process display. It should be specified with no lower and upper limits, specifically <code>header=,#</code> followed by the ANSI color code. </p>
<p> You can see a list of color codes recognized by this installation of pg_top with the <code>-T</code> option. This will also show the current set of tests used for color highligting, as specified in the environment.</p>
<h2>AUTHOR</h2>
<p> William LeFebvre Mark Wong</p>
<h2>ENVIRONMENT</h2>
<p> PG_TOP<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>user-configurable defaults for options.<br />
 PG_TOPCOLORS<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>color specification</p>
<h2>BUGS</h2>
<p> As with <i><a href="/docs/linux/man/1-ps/">ps</a></i>(1), things can change while <i>pg_top</i> is collecting information for an update. The picture it gives is only a close approximation to reality.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-kill/">kill</a>(1), <a href="/docs/linux/man/1-ps/">ps</a>(1), <a href="/docs/linux/man/1-stty/">stty</a>(1), <a href="/docs/linux/man/4-mem/">mem</a>(4), <a href="/docs/linux/man/8-renice/">renice</a>(8)</p>
<h2>LINUX NOTES</h2>
<p> The Linux port was written by Richard Henderson &lt;rth [at] tamu.edu&gt;. The CPU% calculation was brazenly stolen from the Solaris 2 port and should be attributed to one of the many names listed in its man page. </p>
<p> The order support was stolen from SUNOS 5 port by Alexey Klimkin &lt;kad [at] klon.tme.mcst.ru&gt; </p>
<p> Made to work under 2.4 by William LeFebvre. </p>
<h2>Index</h2>
