---
title: "sudoreplay(8)"
name: "sudoreplay"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sudoreplay/"
description: "sudoreplay – replay sudo session logs"
---

<p>Sudo 1.9.9</p>
<h2>Name</h2>
<p><code>sudoreplay</code> &#8211; replay sudo session logs</p>
<h2>Synopsis</h2>
<p><code>sudoreplay</code> [-<code>FhnRS</code> ] [-<code>d </code><i>dir</i> ] [-<code>f </code><i>filter</i> ] [-<code>m </code><i>num</i> ] [-<code>s </code><i>num</i> ] <code>ID </code>[<i>@offset</i> ] </p>
<p><code>sudoreplay</code> [-<code>h</code> ] [-<code>d </code><i>dir</i> ] &#8211;<code>l</code> [search expression]</p>
<h2>Description</h2>
<p><code>sudoreplay</code> plays back or lists the output logs created by <code>sudo</code> When replaying, <code>sudoreplay</code> can play the session back in real-time, or the playback speed may be adjusted (faster or slower) based on the command line options. </p>
<p> The <i>ID</i> should either be a six character sequence of digits and upper case letters, e.g., <code>0100A5</code> or a path name. The <i>ID</i> may include an optional <i>@offset</i> suffix which may be used to start replaying at a specific time offset. The <i>@offset</i> is specified as a number in seconds since the start of the session with an optional decimal fraction. </p>
<p> Path names may be relative to the I/O log directory /var/log/sudo-io (unless overridden by the &#8211;<code>d</code> option) or fully qualified, beginning with a `/&#8217; character. When a command is run via <code>sudo</code> with <i>log_output</i> enabled in the <i>sudoers</i> file, a <code>TSID=ID</code> string is logged via syslog or to the <code>sudo</code> log file. The <i>ID</i> may also be determined using <code>sudoreplay &#8216;s</code> list mode. </p>
<p> In list mode, <code>sudoreplay</code> can be used to find the ID of a session based on a number of criteria such as the user, tty, or command run. </p>
<p> In replay mode, if the standard input and output are connected to a terminal and the &#8211;<code>n</code> option is not specified, <code>sudoreplay</code> will operate interactively. In interactive mode, <code>sudoreplay</code> will attempt to adjust the terminal size to match that of the session and write directly to the terminal (not all terminals support this). Additionally, it will poll the keyboard and act on the following keys:</p>
<dl>
<dt><code>So </code><code>
 Sc </code><code>or So </code><code> Sc </code>Skip to the next replay event; useful for long pauses.</p>
<dd>
<dt><code>So </code><code>&nbsp; Sc </code>(space)</p>
<dd>Pause output; press any key to resume.</p>
<dt><code>`&lt;&#8216; </code></p>
<dd>Reduce the playback speed by one half.</p>
<dt><code>`&gt;&#8217; </code></p>
<dd>Double the playback speed.</dl>
<p> The session can be interrupted via control-C. When the session has finished, the terminal is restored to its original size if it was changed during playback. </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-d </code><i>dir , &#8211;</i><code>-directory = </code><i>dir</i></p>
<dd>Store session logs in <i>dir</i> instead of the default, /var/log/sudo-io</p>
<dt><code>-f </code><i>filter , &#8211;</i><code>-filter = </code><i>filter</i></p>
<dd>Select which I/O type(s) to display. By default, <code>sudoreplay</code> will display the command&#8217;s standard output, standard error, and tty output. The <i>filter</i> argument is a comma-separated list, consisting of one or more of following: <i>stdin</i> <i>stdout</i> <i>stderr</i> <i>ttyin</i> and <i>ttyout</i></p>
<dt><code>-F , -follow</code></p>
<dd>Enable &#8220;follow mode&#8221; When replaying a session, <code>sudoreplay</code> will ignore end-of-file and keep replaying until the log is complete. This can be used to replay a session that is still in progress, similar to &#8220;tail -f&#8221; An I/O log file is considered to be complete when the write bits have been cleared on the session&#8217;s timing file. Note that versions of <code>sudo</code> prior to 1.9.1 do not clear the write bits upon completion.</p>
<dt><code>-h , -help</code></p>
<dd>Display a short help message to the standard output and exit.</p>
<dt><code>-l , -list </code>[<i>search expression</i> ]</p>
<dd>Enable &#8220;list mode&#8221; In this mode, <code>sudoreplay</code> will list available sessions in a format similar to the <code>sudo</code> log file format, sorted by file name (or sequence number). Any control characters present in the log data are formatted in octal with a leading `#&#8217; character. For example, a horizontal tab is displayed as `#011&#8242; and an embedded carriage return is displayed as `#015&#8242; Space characters in the command name and arguments are also formatted in octal. </p>
<p> If a <i>search expression</i> is specified, it will be used to restrict the IDs that are displayed. An expression is composed of the following predicates:</p>
<dl>
<dt><code>command </code><i>pattern</i></p>
<dd>Evaluates to true if the command run matches the POSIX extended regular expression <i>pattern</i></p>
<dt><code>cwd </code><i>directory</i></p>
<dd>Evaluates to true if the command was run with the specified current working directory.</p>
<dt><code>fromdate </code><i>date</i></p>
<dd>Evaluates to true if the command was run on or after <i>date</i> See Sx Date and time format for a description of supported date and time formats.</p>
<dt><code>group </code><i>runas_group</i></p>
<dd>Evaluates to true if the command was run with the specified <i>runas_group</i> Note that unless a <i>runas_group</i> was explicitly specified when <code>sudo</code> was run this field will be empty in the log.</p>
<dt><code>host </code><i>hostname</i></p>
<dd>Evaluates to true if the command was run on the specified <i>hostname</i></p>
<dt><code>runas </code><i>runas_user</i></p>
<dd>Evaluates to true if the command was run as the specified <i>runas_user</i> Note that <code>sudo</code> runs commands as user <i>root</i> by default.</p>
<dt><code>todate </code><i>date</i></p>
<dd>Evaluates to true if the command was run on or prior to <i>date</i> See Sx Date and time format for a description of supported date and time formats.</p>
<dt><code>tty </code><i>tty name</i></p>
<dd>Evaluates to true if the command was run on the specified terminal device. The <i>tty name</i> should be specified without the /dev/ prefix, e.g., tty01 instead of /dev/tty01</p>
<dt><code>user </code><i>user name</i></p>
<dd>Evaluates to true if the ID matches a command run by <i>user name</i></dl>
<p> Predicates may be abbreviated to the shortest unique string. </p>
<p> Predicates may be combined using <i>and</i> <i>or</i> and <i>!</i> operators as well as `(&#8216; and `)&#8217; grouping (note that parentheses must generally be escaped from the shell). The <i>and</i> operator is optional, adjacent predicates have an implied <i>and</i> unless separated by an <i>or</i></p>
<dt><code>-m , -max-wait </code><i>max_wait</i></p>
<dd>Specify an upper bound on how long to wait between key presses or output data. By default, <code>sudoreplay</code> will accurately reproduce the delays between key presses or program output. However, this can be tedious when the session includes long pauses. When the &#8211;<code>m</code> option is specified, <code>sudoreplay</code> will limit these pauses to at most <i>max_wait</i> seconds. The value may be specified as a floating point number, e.g., <i>2.5</i> A <i>max_wait</i> of zero or less will eliminate the pauses entirely.</p>
<dt><code>-n , -non-interactive</code></p>
<dd>Do not prompt for user input or attempt to re-size the terminal. The session is written to the standard output, not directly to the user&#8217;s terminal.</p>
<dt><code>-R , -no-resize</code></p>
<dd>Do not attempt to re-size the terminal to match the terminal size of the session.</p>
<dt><code>-S , -suspend-wait</code></p>
<dd>Wait while the command was suspended. By default, <code>sudoreplay</code> will ignore the time interval between when the command was suspended and when it was resumed. If the &#8211;<code>S</code> option is specified, <code>sudoreplay</code> will wait instead.</p>
<dt><code>-s , -speed </code><i>speed_factor</i></p>
<dd>This option causes <code>sudoreplay</code> to adjust the number of seconds it will wait between key presses or program output. This can be used to slow down or speed up the display. For example, a <i>speed_factor</i> of <i>2</i> would make the output twice as fast whereas a <i>speed_factor</i> of <i>.5</i> would make the output twice as slow.</p>
<dt><code>-V , -version</code></p>
<dd>Print the <code>sudoreplay</code> versions version number and exit.</dl>
<h3>Date and time format</h3>
<p>The time and date may be specified multiple ways, common formats include:</p>
<dl>
<dt><code>HH:MM:SS am MM/DD/CCYY timezone</code></p>
<dd>24 hour time may be used in place of am/pm.</p>
<dt><code>HH:MM:SS am Month, Day Year timezone</code></p>
<dd>24 hour time may be used in place of am/pm, and month and day names may be abbreviated. Note that month and day of the week names must be specified in English.</p>
<dt><code>CCYY-MM-DD HH:MM:SS</code></p>
<dd>ISO time format</p>
<dt><code>DD Month CCYY HH:MM:SS</code></p>
<dd>The month name may be abbreviated.</dl>
<p> Either time or date may be omitted, the am/pm and timezone are optional. If no date is specified, the current day is assumed; if no time is specified, the first second of the specified date is used. The less significant parts of both time and date may also be omitted, in which case zero is assumed. </p>
<p> The following are all valid time and date specifications:</p>
<dl>
<dt><code>now</code></p>
<dd>The current time and date.</p>
<dt><code>tomorrow</code></p>
<dd>Exactly one day from now.</p>
<dt><code>yesterday</code></p>
<dd>24 hours ago.</p>
<dt><code>2 hours ago</code></p>
<dd>2 hours ago.</p>
<dt><code>next Friday</code></p>
<dd>The first second of the Friday in the next (upcoming) week. Not to be confused with &#8220;this Friday&#8221; which would match the Friday of the current week.</p>
<dt><code>last week</code></p>
<dd>The current time but 7 days ago. This is equivalent to &#8220;a week ago&#8221;</p>
<dt><code>a fortnight ago</code></p>
<dd>The current time but 14 days ago.</p>
<dt><code>10:01 am 9/17/2009</code></p>
<dd>10:01 am, September 17, 2009.</p>
<dt><code>10:01 am</code></p>
<dd>10:01 am on the current day.</p>
<dt><code>10</code></p>
<dd>10:00 am on the current day.</p>
<dt><code>9/17/2009</code></p>
<dd>00:00 am, September 17, 2009.</p>
<dt><code>10:01 am Sep 17, 2009</code></p>
<dd>10:01 am, September 17, 2009.</dl>
<p> Note that relative time specifications do not always work as expected. For example, the &#8220;next&#8221; qualifier is intended to be used in conjunction with a day such as &#8220;next Monday&#8221; When used with units of weeks, months, years, etc the result will be one more than expected. For example, &#8220;next week&#8221; will result in a time exactly two weeks from now, which is probably not what was intended. This will be addressed in a future version of <code>sudoreplay.</code></p>
<h3>Debugging sudoreplay</h3>
<p><code>sudoreplay</code> versions 1.8.4 and higher support a flexible debugging framework that is configured via <code>Debug</code> lines in the sudo.conf5 file. </p>
<p> For more information on configuring sudo.conf5, please refer to its manual.</p>
<h2>Files</h2>
<dl>
<dt><code>/etc/sudo.conf </code></p>
<dd>Debugging framework configuration</p>
<dt><code>/var/log/sudo-io </code></p>
<dd>The default I/O log directory.</p>
<dt><code>/var/log/sudo-io/00/00/01/log </code></p>
<dd>Example session log info.</p>
<dt><code>/var/log/sudo-io/00/00/01/log.json </code></p>
<dd>Example session log info (JSON format).</p>
<dt><code>/var/log/sudo-io/00/00/01/stdin </code></p>
<dd>Example session standard input log.</p>
<dt><code>/var/log/sudo-io/00/00/01/stdout </code></p>
<dd>Example session standard output log.</p>
<dt><code>/var/log/sudo-io/00/00/01/stderr </code></p>
<dd>Example session standard error log.</p>
<dt><code>/var/log/sudo-io/00/00/01/ttyin </code></p>
<dd>Example session tty input file.</p>
<dt><code>/var/log/sudo-io/00/00/01/ttyout </code></p>
<dd>Example session tty output file.</p>
<dt><code>/var/log/sudo-io/00/00/01/timing </code></p>
<dd>Example session timing file.</dl>
<p> Note that the <i>stdin</i> <i>stdout</i> and <i>stderr</i> files will be empty unless <code>sudo</code> was used as part of a pipeline for a particular command.</p>
<h2>Examples</h2>
<p>List sessions run by user <i>millert</i> </p>
<blockquote>
<pre># sudoreplay -l user millert</pre>
</blockquote>
<p> List sessions run by user <i>bob</i> with a command containing the string vi: </p>
<blockquote>
<pre># sudoreplay -l user bob command vi</pre>
</blockquote>
<p> List sessions run by user <i>jeff</i> that match a regular expression: </p>
<blockquote>
<pre># sudoreplay -l user jeff command '/bin/[a-z]*sh'</pre>
</blockquote>
<p> List sessions run by jeff or bob on the console: </p>
<blockquote>
<pre># sudoreplay -l ( user jeff or user bob ) tty console</pre>
</blockquote>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-script/">script</a>(1), sudo.conf5, <a href="/docs/linux/man/8-sudo/">sudo</a>(8)</p>
<h2>Authors</h2>
<p>Many people have worked on <code>sudo</code> over the years; this version consists of code written primarily by: </p>
<blockquote><p> An Todd C. Miller </p></blockquote>
<p> See the CONTRIBUTORS file in the <code>sudo</code> distribution (<a rel="nofollow" href="https://www.sudo.ws/contributors.html)">https://www.sudo.ws/contributors.html)</a> for an exhaustive list of people who have contributed to <code>sudo</code></p>
<h2>Bugs</h2>
<p>If you feel you have found a bug in <code>sudoreplay,</code> please submit a bug report at <a rel="nofollow" href="https://bugzilla.sudo.ws/">https://bugzilla.sudo.ws/</a></p>
<h2>Support</h2>
<p>Limited free support is available via the sudo-users mailing list, see <a rel="nofollow" href="https://www.sudo.ws/mailman/listinfo/sudo-users">https://www.sudo.ws/mailman/listinfo/sudo-users</a> to subscribe or search the archives.</p>
<h2>Disclaimer</h2>
<p><code>sudoreplay</code> is provided &#8220;AS IS&#8221; and any express or implied warranties, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose are disclaimed. See the LICENSE file distributed with <code>sudo</code> or <a rel="nofollow" href="https://www.sudo.ws/license.html">https://www.sudo.ws/license.html</a> for complete details.</p>
