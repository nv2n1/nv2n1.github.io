---
title: "conman-conf(5)"
name: "conman-conf"
section: "5"
letter: "c"
url: "/docs/linux/man/5-conman-conf/"
description: "conman.conf – ConMan daemon configuration file"
---

<p>conman.conf &#8211; ConMan daemon configuration file</p>
<h2>Description</h2>
<p>The <code>conman.conf</code> configuration file is used to specify the consoles being managed by <code>conmand</code>. Comments are introduced by a hash sign (#), and continue until the end of the line. Blank lines and white-space are ignored. Directives are terminated by a newline, but may span multiple lines by escaping it (i.e., immediately preceding the newline with a backslash). Strings may be either single-quoted or double-quoted, but they may not contain newlines. Keywords are case-insensitive. </p>
<h2>Server Directives</h2>
<p>These directives begin with the <code>SERVER</code> keyword followed by one of the following key/value pairs:</p>
<dl>
<dt><code>coredump</code> <code>=</code> (<code>on</code>|<code>off</code>)</p>
<dd>Specifies whether the daemon should generate a core dump file. This file will be created in the current working directory (or &#8216;/&#8217; when running in the background) unless you also set <code>coredumpdir</code>. The default is off.</p>
<dt><code>coredumpdir</code> <code>=</code> &quot;<i>directory</i>&quot;</p>
<dd>Specifies the directory where the daemon tries to write core dump files. The default is empty, meaning the current working directory (or &#8216;/&#8217; when running in the background) will be used.</p>
<dt><code>execpath</code> <code>=</code> &quot;<i>dir1:dir2:dir3&#8230;</i>&quot;</p>
<dd>Specifies a colon-separated list of directories in which to search for external process-based console executables that are not defined by an absolute or relative pathname. The default is empty.</p>
<dt><code>keepalive</code> <code>=</code> (<code>on</code>|<code>off</code>)</p>
<dd>Specifies whether the daemon will use TCP keep-alives for detecting dead connections. The default is <code>on</code>.</p>
<dt><code>logdir</code> <code>=</code> &quot;<i>directory</i>&quot;</p>
<dd>Specifies a directory prefix for log files that are not defined via an absolute pathname. This affects the <code>server logfile</code>, <code>global log</code>, and <code>console log</code> directives.</p>
<dt><code>logfile</code> <code>=</code> &quot;<i>file</i>[,<i>priority</i>]&quot;</p>
<dd>Specifies the file to which log messages are appended if the daemon is not running in the foreground. This string undergoes conversion specifier expansion (cf., <code>CONVERSION SPECIFICATIONS</code>) each time the file is opened. If an absolute pathname is not given, the file&#8217;s location is relative to either <code>logdir</code> (if defined) or the current working directory. Intermediate directories will be created as needed. The filename may optionally be followed by a comma and a minimum priority at which messages will be logged. Refer to <code><a href="/docs/linux/man/5-syslog-conf/">syslog.conf</a>(5)</code> for a list of priorities. The default priority is <code>info</code>. If this keyword is used in conjunction with the <code>syslog</code> keyword, messages will be sent to both locations.</p>
<dt><code>loopback</code> <code>=</code> (<code>on</code>|<code>off</code>)</p>
<dd>Specifies whether the daemon will bind its socket to the loopback address, thereby only accepting local client connections directed to that address (127.0.0.1). The default is <code>off</code>.</p>
<dt><code>pidfile</code> <code>=</code> &quot;<i>file</i>&quot;</p>
<dd>Specifies the file to which the daemon&#8217;s PID is written. Intermediate directories will be created as needed. The use of a pidfile is recommended if you want to use the daemon&#8217;s &#8216;<code>-k</code>&#8216;, &#8216;<code>-q</code>&#8216;, or &#8216;<code>-r</code>&#8216; options.</p>
<dt><code>port</code> <code>=</code> <i>integer</i></p>
<dd>Specifies the port on which the daemon will listen for client connections.</p>
<dt><code>resetcmd</code> <code>=</code> &quot;<i>string</i>&quot;</p>
<dd>Specifies a command string to be invoked by a subshell upon receipt of the client&#8217;s &quot;reset&quot; escape. Multiple commands within a string may be separated with semicolons. This string undergoes conversion specifier expansion (cf., <code>CONVERSION SPECIFICATIONS</code>) and will be invoked multiple times if the client is connected to multiple consoles.</p>
<dt><code>syslog</code> <code>=</code> &quot;<i>facility</i>&quot;</p>
<dd>Specifies that log messages are to be sent to the system logger (<code>syslogd</code>) at the given facility. Refer to <code><a href="/docs/linux/man/5-syslog-conf/">syslog.conf</a>(5)</code> for a list of facilities. If this keyword is used in conjunction with the <code>logfile</code> keyword, messages will be sent to both locations.</p>
<dt><code>tcpwrappers</code> <code>=</code> (<code>on</code>|<code>off</code>)</p>
<dd>Specifies whether the daemon will use TCP-Wrappers when accepting client connections. Support for this feature must be enabled at compile-time (via configure&#8217;s &quot;&#8211;with-tcp-wrappers&quot; option). Refer to <code><a href="/docs/linux/man/5-hosts_access/">hosts_access</a>(5)</code> and <code><a href="/docs/linux/man/5-hosts_options/">hosts_options</a>(5)</code> for more details. The default is <code>off</code>.</p>
<dt><code>timestamp</code> <code>=</code> <i>integer</i><code> (m</code>|<code>h</code>|<code>d</code>)</p>
<dd>Specifies the interval between timestamps written to the individual console log files. The interval is an integer that may be followed by a single-character modifier; &#8216;<code>m</code>&#8216; for minutes (the default), &#8216;<code>h</code>&#8216; for hours, or &#8216;<code>d</code>&#8216; for days. The default is 0 (i.e., no timestamps). </p>
</dl>
<h2>Global Directives</h2>
<p>These directives begin with the <code>GLOBAL</code> keyword followed by one of the following key/value pairs:</p>
<dl>
<dt><code>log</code> <code>=</code> &quot;<i>file</i>&quot;</p>
<dd>Specifies the default log file to use for each <code>console</code> directive. This string undergoes conversion specifier expansion (cf., <code>CONVERSION SPECIFICATIONS</code>) each time the file is opened; it must contain either &#8216;<code>%N</code>&#8216; or &#8216;<code>%D</code>&#8216;. If an absolute pathname is not given, the file&#8217;s location is relative to either <code>logdir</code> (if defined) or the current working directory. Intermediate directories will be created as needed.</p>
<dt><code>logopts</code> <code>=</code> &quot;(<code>lock</code>|<code>nolock</code>),(<code>sanitize</code>|<code>nosanitize</code>),(<code>timestamp</code>|<code>notimestamp</code>)&quot;</p>
<dd>Specifies global options for the console log files. These options can be overridden on a per-console basis by specifying the <code>CONSOLE</code> <code>logopts</code> keyword. Note that options affecting the output of the console&#8217;s logfile also affect the output of the console&#8217;s log-replay escape. The valid <code>logopts</code> include the following: </p>
<p> <code>lock</code> or <code>nolock</code> &#8211; locked logs are protected with a write lock. </p>
<p> <code>sanitize</code> or <code>nosanitize</code> &#8211; sanitized logs convert non-printable characters into 7-bit printable characters. </p>
<p> <code>timestamp</code> or <code>notimestamp</code> &#8211; timestamped logs prepend each line of console output with a timestamp in &quot;YYYY-MM-DD HH:MM:SS&quot; format. This timestamp is generated when the first character following the line break is output. </p>
<p> The default is &quot;<code>lock</code>,<code>nosanitize</code>,<code>notimestamp</code>&quot;.</p>
<dt><code>seropts</code> <code>=</code> &quot;<i>bps</i>[,<i>databits</i>[<i>parity</i>[<i>stopbits</i>]]]&quot;</p>
<dd>Specifies global options for local serial devices. These options can be overridden on a per-console basis by specifying the <code>CONSOLE</code> <code>seropts</code> keyword. </p>
<p> <i>bps</i> is an integer specifying the baud rate in bits-per-second. If this exact value is not supported by the system, it will be rounded down to the next supported value. </p>
<p> <i>databits</i> is an integer from 5-8. </p>
<p> <i>parity</i> is a single case-insensitive character: &#8216;<code>n</code>&#8216; for none, &#8216;<code>o</code>&#8216; for odd, and &#8216;<code>e</code>&#8216; for even. </p>
<p> <i>stopbits</i> is an integer from 1-2. </p>
<p> The default is &quot;9600,8n1&quot; for 9600 bps, 8 data bits, no parity, and 1 stop bit.</p>
<dt><code>ipmiopts</code> <code>=</code> &quot;<code>U</code>:<i>str</i>,<code>P</code>:<i>str</i>,<code>K</code>:<i>str</i>,<code>C</code>:<i>int</i>,<code>L</code>:<i>str</i>,<code>W</code>:<i>flag</i>&quot;</p>
<dd>Specifies global options for IPMI Serial-Over-LAN devices. These options can be overridden on a per-console basis by specifying the <code>CONSOLE</code> <code>IPMIOPTS</code> keyword. This directive is only available if configured using the &quot;&#8211;with-freeipmi&quot; option. </p>
<p> The <code>IPMIOPTS</code> string is parsed into comma-delimited substrings where each substring is of the form &quot;<i>X</i>:<i>VALUE</i>&quot;. &quot;<i>X</i>&quot; is a single-character case-insensitive key specifying the option type, and &quot;<i>VALUE</i>&quot; is its corresponding value. The IPMI default will be used if either &quot;<i>VALUE</i>&quot; is omitted from the substring (&quot;<i>X</i>:&quot;) or the substring is omitted altogether. Note that since the <code>IPMIOPTS</code> string is delimited by commas, substring values cannot contain commas. </p>
<p> The valid <code>IPMIOPTS</code> substrings include the following (in any order): </p>
<p> <code>U</code>:<i>username</i> &#8211; a string of at most 16 bytes for the username with which to authenticate to the BMCs serving the remote consoles. </p>
<p> <code>P</code>:<i>password</i> &#8211; a string of at most 20 bytes for the password with which to authenticate to the BMCs serving the remote consoles. </p>
<p> <code>K</code>:<i>K_g</i> &#8211; a string of at most 20 bytes for the K_g key with which to authenticate to the BMCs serving the remote consoles. </p>
<p> <code>C</code>:<i>cipher_suite</i> &#8211; an integer for the IPMI cipher suite ID. Refer to <code><a href="/docs/linux/man/8-ipmiconsole/">ipmiconsole</a>(8)</code> for a list of currently supported IDs. </p>
<p> <code>L</code>:<i>privilege_level</i> &#8211; the string &quot;user&quot;, &quot;op&quot;, or &quot;admin&quot;. </p>
<p> <code>W</code>:<i>workaround_flag</i> &#8211; a string or integer for an IPMI workaround. Refer to <code><a href="/docs/linux/man/8-ipmiconsole/">ipmiconsole</a>(8)</code> for a list of currently supported flags. This substring may be repeated to specify multiple workaround flags. </p>
<p> Both the <i>password</i> and <i>K_g</i> values can be specified in either ASCII or hexadecimal; in the latter case, the string should begin with &quot;0x&quot; and contain at most 40 hexadecimal digits. A <i>K_g</i> key entered in hexadecimal may contain embedded null characters, but any characters following the first null character in the <i>password</i> key will be ignored. </p>
</dl>
<h2>Console Directives</h2>
<p>This directive defines an individual console being managed by the daemon. The <code>CONSOLE</code> keyword is followed by one or more of the following key/value pairs:</p>
<dl>
<dt><code>name</code> <code>=</code> &quot;<i>string</i>&quot;</p>
<dd>Specifies the name used by clients to refer to the console. This keyword is required.</p>
<dt><code>dev</code> <code>=</code> &quot;<i>string</i>&quot;</p>
<dd>Specifies the type and location of the device. This keyword is required. </p>
<p> A local serial port connection is defined by the pathname of the character device file. </p>
<p> A remote terminal server connection using the telnet protocol is defined by the &quot;<i>host</i>:<i>port</i>&quot; format (where <i>host</i> is the remote hostname or IPv4 address, and <i>port</i> is the remote port number). </p>
<p> An external process-based connection is defined by the &quot;<i>path</i> <i>args</i>&quot; format (where <i>path</i> is the pathname to an executable file/script, and any additional <i>args</i> are space-delimited); the <i>/usr/lib/conman/exec</i> directory contains scripts for various console types. </p>
<p> A local Unix domain socket connection is defined by the &quot;unix:<i>path</i>&quot; format (where &quot;unix:&quot; is the literal character string prefix and <i>path</i> is the pathname of the local socket). </p>
<p> An IPMI Serial-Over-LAN connection is defined by the &quot;ipmi:<i>host</i>&quot; format (where &quot;ipmi:&quot; is the literal string and <i>host</i> is a hostname or IPv4 address). </p>
<p> The &#8216;<code>%N</code>&#8216; character sequence will be replaced by the console name.</p>
<dt><code>log</code> <code>=</code> &quot;<i>file</i>&quot;</p>
<dd>Specifies the file where console output is logged. This string undergoes conversion specifier expansion (cf., <code>CONVERSION SPECIFICATIONS</code>) each time the file is opened. If an absolute pathname is not given, the file&#8217;s location is relative to either <code>logdir</code> (if defined) or the current working directory. Intermediate directories will be created as needed. An empty log string (i.e., <code>log</code>=&quot;&quot;) disables logging, overriding the <code>global log</code> name.</p>
<dt><code>logopts</code> <code>=</code> &quot;<i>string</i>&quot;</p>
<dd>This keyword is optional (cf., <code>GLOBAL DIRECTIVES</code>).</p>
<dt><code>seropts</code> <code>=</code> &quot;<i>string</i>&quot;</p>
<dd>This keyword is optional (cf., <code>GLOBAL DIRECTIVES</code>).</p>
<dt><code>ipmiopts</code> <code>=</code> &quot;<i>string</i>&quot;</p>
<dd>This keyword is optional (cf., <code>GLOBAL DIRECTIVES</code>). </p>
</dl>
<h2>Conversion Specifications</h2>
<p>A conversion specifier is a two-character sequence beginning with a &#8216;<code>%</code>&#8216; character. The second character in the sequence specifies the type of conversion to be applied. The following specifiers are supported:</p>
<dl>
<dt><code>%N</code></p>
<dd>The console name (from the <code>name</code> string).</p>
<dt><code>%D</code></p>
<dd>The console device basename (from the <code>dev</code> string), with leading directory components removed.</p>
<dt><code>%P</code></p>
<dd>The daemon&#8217;s process identifier.</p>
<dt><code>%Y</code></p>
<dd>The year as a 4-digit number with the century.</p>
<dt><code>%y</code></p>
<dd>The year as a 2-digit number without the century.</p>
<dt><code>%m</code></p>
<dd>The month as a 2-digit number (01-12).</p>
<dt><code>%d</code></p>
<dd>The day of the month as a 2-digit number (01-31).</p>
<dt><code>%H</code></p>
<dd>The hour as a 2-digit number using a 24-hour clock (00-23).</p>
<dt><code>%M</code></p>
<dd>The minute as a 2-digit number (00-59).</p>
<dt><code>%S</code></p>
<dd>The seconds as a 2-digit number (00-61).</p>
<dt><code>%s</code></p>
<dd>The number of seconds since the Epoch.</p>
<dt><code>%%</code></p>
<dd>A literal &#8216;%&#8217; character.</dl>
<p> The console name (<code>%N</code>) and device (<code>%D</code>) specifiers are &quot;sanitized&quot; in that non-printable characters and the forward-slash (/) character are replaced with underscores.</p>
<h2>Files</h2>
<p><i>/etc/conman.conf</i></p>
<h2>Author</h2>
<p>Chris Dunlap &lt;cdunlap [at] llnl.gov&gt;</p>
<h2>Copyright</h2>
<p>Copyright (C) 2007-2011 Lawrence Livermore National Security, LLC.<br />
 Copyright (C) 2001-2007 The Regents of the University of California. </p>
<p> ConMan is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-conman/">conman</a></code>(1), <code><a href="/docs/linux/man/8-conmand/">conmand</a></code>(8). <code><a rel="nofollow" href="http://conman.googlecode.com/">http://conman.googlecode.com/</a></code> </p>
