---
title: "wlog(7)"
name: "wlog"
section: "7"
letter: "w"
url: "/docs/linux/man/7-wlog/"
description: "wLog – WinPR logging facility"
---

<p>wLog &#8211; WinPR logging facility</p>
<h2>Description</h2>
<p>wLog is a configurable and flexible logging system used throughout WinPR and FreeRDP. The primary concept is to have a hierarchy of loggers that can be be configured independently. </p>
<h2>Appenders</h2>
<p>WLog uses different appenders that define where the log output should be written to. If the application doesn&#8217;t explicitly configure the appenders the below described variable WLOG_APPENDER can be used to choose one appender. </p>
<p> The following kind of appenders are available: </p>
<dl>
<dt>Binary</p>
<dd>Write the log data into a binary format file. </p>
<dt>Console</p>
<dd>The console appender writes to the console. Depending of the operating system the application runs on, the output might be handled differently. For example on android log print would be used. </p>
<dt>File</p>
<dd>The file appender writes the textual output to a file. </p>
<dt>Udp</p>
<dd>This appender sends the logging messages to a pre-defined remote host via UDP. </p>
<p> If no target is set the default one 127.0.0.1:20000 is used. To receive the log messages one can use netcat. To receive the default target the following command can be used: nc -u 127.0.0.1 -p 20000 -l</p>
<dt>Syslog</p>
<dd>Use syslog for outputting the debug messages.</p>
<dt>Journald</p>
<dd>This appender outputs messages to journald. </p>
</dl>
<h2>Levels</h2>
<p>The WLog are complementary, the higher level always includes the lower ones. The level list below is top down. Top the highest level. </p>
<dl>
<dt>TRACE</p>
<dd>print everything including packets dumps</p>
<dt>DEBUG</p>
<dd>debug messages</p>
<dt>INFO</p>
<dd>general information</p>
<dt>WARN</p>
<dd>warnings</p>
<dt>ERROR</p>
<dd>errors</p>
<dt>FATAL</p>
<dd>fatal problems</p>
<dt>OFF</p>
<dd>completely disable the wlog output </p>
</dl>
<h2>Formats</h2>
<p>The format a logger prints has the following possible options: </p>
<dl>
<dt>lv</p>
<dd>log level</p>
<dt>mn</p>
<dd>module name</p>
<dt>fl</p>
<dd>file name</p>
<dt>fn</p>
<dd>function</p>
<dt>ln</p>
<dd>line number</p>
<dt>pid</p>
<dd>process id</p>
<dt>tid</p>
<dd>thread id</p>
<dt>yr</p>
<dd>year</p>
<dt>mo</p>
<dd>month</p>
<dt>dw</p>
<dd>day of week</p>
<dt>hr</p>
<dd>hour</p>
<dt>mi</p>
<dd>minute</p>
<dt>se</p>
<dd>second</p>
<dt>ml</p>
<dd>millisecond</dl>
<p> A maximum of 16 options can be used per format string. </p>
<p> An example that generally sets the WLOG_PREFIX for xfreerdp would look like: WLOG_PREFIX=&quot;pid=%pid:tid=%tid:fn=%fn -&quot; xfreerdp /v:xxx</p>
<h2>Environment</h2>
<dl>
<dt>WLOG_APPENDER</p>
<dd>The kind of appender, the accepted values are: CONSOLE, FILE, BINARY, SYSLOG, JOURNALD or UDP </p>
<dt>WLOG_PREFIX</p>
<dd>configure the prefix used for outputting the message (see Format for more details and examples) </p>
<dt>WLOG_LEVEL</p>
<dd>the level to output messages for </p>
<dt>WLOG_FILTER</p>
<dd>sets a filter for WLog messages. Only the filtered messages are printed. The format of the filter is a series of &lt;logger name&gt;:&lt;level&gt; separated by comas </p>
<p> example: WLOG_FILTER=core.channel:DEBUG,dummy:TRACE will display debug messages for the core.channel logger and trace level for the dummy logger </p>
<dt>WLOG_FILEAPPENDER_OUTPUT_FILE_PATH</p>
<dd>When using the file appender it may contains the output log file&#8217;s path </p>
<dt>WLOG_FILEAPPENDER_OUTPUT_FILE_NAME</p>
<dd>When using the file appender it may contains the output log file&#8217;s name </p>
<dt>WLOG_JOURNALD_ID</p>
<dd>When using the systemd journal appender, this variable contains the id used with the journal (by default the executable&#8217;s name) </p>
<dt>WLOG_UDP_TARGET</p>
<dd>target to use for the UDP appender in the format <code>host:port</code> </p>
</dl>
<h2>Bugs</h2>
<p>Please report any bugs using the bug reporting form on the <code>FreeRDP</code> web site </p>
<h2>See Also</h2>
<p>Additional information and the latest version is available at the web site: <code><a rel="nofollow" href="http://www.freerdp.com">http://www.freerdp.com</a></code> </p>
<h2>Author</h2>
<p>David Fort &lt;contact [at] hardening-consulting.com&gt; wrote this manpage from materials written by Bernhard Miklautz &lt;bernhard.miklautz [at] thincast.com&gt;.</p>
