---
title: "mysqld_safe(1)"
name: "mysqld_safe"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mysqld_safe/"
description: "mysqld_safe – MySQL server startup script"
---

<h2 class="name">NAME</h2>
<p> mysqld_safe &#8211; MySQL server startup script </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mysqld_safe </code><i>options</i></dl>
<h2>DESCRIPTION</h2>
<p> <code>mysqld_safe</code></p>
<dd>is the recommended way to start a <code>mysqld</code> server on Unix. <code>mysqld_safe</code> adds some safety features such as restarting the server when an error occurs and logging runtime information to an error log. A description of error logging is given later in this section. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> For some Linux platforms, MySQL installation from RPM or Debian packages includes systemd support for managing MySQL server startup and shutdown. On these platforms, <code>mysqld_safe</code> is not installed because it is unnecessary. For more information, see Section 2.5.9, &#8220;Managing MySQL Server with systemd&#8221;. </p>
</dl>
<p> <code>mysqld_safe</code> tries to start an executable named <code>mysqld</code>. To override the default behavior and specify explicitly the name of the server you want to run, specify a <code>&#8211;mysqld</code> or <code>&#8211;mysqld-version</code> option to <code>mysqld_safe</code>. You can also use <code>&#8211;ledir</code> to indicate the directory where <code>mysqld_safe</code> should look for the server. </p>
<p> Many of the options to <code>mysqld_safe</code> are the same as the options to <code>mysqld</code>. See Section 5.1.7, &#8220;Server Command Options&#8221;. </p>
<p> Options unknown to <code>mysqld_safe</code> are passed to <code>mysqld</code> if they are specified on the command line, but ignored if they are specified in the [mysqld_safe] group of an option file. See Section 4.2.2.2, &#8220;Using Option Files&#8221;. </p>
<p> <code>mysqld_safe</code> reads all options from the [mysqld], [server], and [mysqld_safe] sections in option files. For example, if you specify a [mysqld] section like this, <code>mysqld_safe</code> will find and use the <code>&#8211;log-error</code> option: </p>
<dl>
<dt>
<dd>
<pre>
[mysqld]
log-error=error.log
</pre>
</dl>
<p> For backward compatibility, <code>mysqld_safe</code> also reads [safe_mysqld] sections, but to be current you should rename such sections to [mysqld_safe]. </p>
<p> <code>mysqld_safe</code> accepts options on the command line and in option files, as described in the following table. For information about option files used by MySQL programs, see Section 4.2.2.2, &#8220;Using Option Files&#8221;. </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;help</code> </p>
<p> Display a help message and exit.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;basedir=</code><i>dir_name</i> </p>
<p> The path to the MySQL installation directory.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;core-file-size=</code><i>size</i> </p>
<p> The size of the core file that <code>mysqld</code> should be able to create. The option value is passed to <code>ulimit -c</code>. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font><br />
 The innodb_buffer_pool_in_core_file variable can be used to reduce the size of core files on operating systems that support it. For more information, see Section 15.8.3.7, &#8220;Excluding Buffer Pool Pages from Core Files&#8221;. </p>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;datadir=</code><i>dir_name</i> </p>
<p> The path to the data directory.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;defaults-extra-file=</code><i>file_name</i> </p>
<p> Read this option file in addition to the usual option files. If the file does not exist or is otherwise inaccessible, the server will exit with an error. <i>file_name</i> is interpreted relative to the current directory if given as a relative path name rather than a full path name. This must be the first option on the command line if it is used. </p>
<p> For additional information about this and other option-file options, see Section 4.2.2.3, &#8220;Command-Line Options that Affect Option-File Handling&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;defaults-file=</code><i>file_name</i> </p>
<p> Use only the given option file. If the file does not exist or is otherwise inaccessible, the server will exit with an error. <i>file_name</i> is interpreted relative to the current directory if given as a relative path name rather than a full path name. This must be the first option on the command line if it is used. </p>
<p> For additional information about this and other option-file options, see Section 4.2.2.3, &#8220;Command-Line Options that Affect Option-File Handling&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;ledir=</code><i>dir_name</i> </p>
<p> If <code>mysqld_safe</code> cannot find the server, use this option to indicate the path name to the directory where the server is located. </p>
<p> This option is accepted only on the command line, not in option files. On platforms that use systemd, the value can be specified in the value of MYSQLD_OPTS. See Section 2.5.9, &#8220;Managing MySQL Server with systemd&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;log-error=</code><i>file_name</i> </p>
<p> Write the error log to the given file. See Section 5.4.2, &#8220;The Error Log&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;mysqld-safe-log-timestamps</code> </p>
<p> This option controls the format for timestamps in log output produced by <code>mysqld_safe</code>. The following list describes the permitted values. For any other value, <code>mysqld_safe</code> logs a warning and uses UTC format. </p>
<dl>
<dt>
<dd> &bull; UTC, utc </p>
<p> ISO 8601 UTC format (same as <code>&#8211;log_timestamps=UTC</code> for the server). This is the default.</dl>
<dl>
<dt>
<dd> &bull; SYSTEM, system </p>
<p> ISO 8601 local time format (same as <code>&#8211;log_timestamps=SYSTEM</code> for the server).</dl>
<dl>
<dt>
<dd> &bull; HYPHEN, hyphen </p>
<p> <i>YY-MM-DD h:mm:ss</i> format, as in <code>mysqld_safe</code> for MySQL 5.6.</dl>
<dl>
<dt>
<dd> &bull; LEGACY, legacy </p>
<p> <i>YYMMDD hh:mm:ss</i> format, as in <code>mysqld_safe</code> prior to MySQL 5.6.</dl>
</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;malloc-lib=[</code><i>lib_name</i><code>]</code> The name of the library to use for memory allocation instead of the system malloc() library. The option value must be one of the directories /usr/lib, /usr/lib64, /usr/lib/i386-linux-gnu, or /usr/lib/x86_64-linux-gnu. </p>
<p> The <code>&#8211;malloc-lib</code> option works by modifying the LD_PRELOAD environment value to affect dynamic linking to enable the loader to find the memory-allocation library when <code>mysqld</code> runs: </p>
<dl>
<dt>
<dd> &bull; If the option is not given, or is given without a value (<code>&#8211;malloc-lib=</code>), LD_PRELOAD is not modified and no attempt is made to use tcmalloc.</dl>
<dl>
<dt>
<dd> &bull; If the option is given as <code>&#8211;malloc-lib=tcmalloc</code>, <code>mysqld_safe</code> looks for a tcmalloc library in /usr/lib. If tmalloc is found, its path name is added to the beginning of the LD_PRELOAD value for <code>mysqld</code>. If tcmalloc is not found, <code>mysqld_safe</code> aborts with an error.</dl>
<dl>
<dt>
<dd> &bull; If the option is given as <code>&#8211;malloc-lib=</code><i>/path/to/some/library</i>, that full path is added to the beginning of the LD_PRELOAD value. If the full path points to a nonexistent or unreadable file, <code>mysqld_safe</code> aborts with an error.</dl>
<dl>
<dt>
<dd> &bull; For cases where <code>mysqld_safe</code> adds a path name to LD_PRELOAD, it adds the path to the beginning of any existing value the variable already has.</dl>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font><br />
 On systems that manage the server using systemd, <code>mysqld_safe</code> is not available. Instead, specify the allocation library by setting LD_PRELOAD in /etc/sysconfig/mysql. </p>
</dl>
<p> Linux users can use the libtcmalloc_minimal.so library on any platform for which a tcmalloc package is installed in /usr/lib by adding these lines to the my.cnf file: </p>
<dl>
<dt>
<dd>
<pre>
[mysqld_safe]
malloc-lib=tcmalloc
</pre>
</dl>
<p> To use a specific tcmalloc library, specify its full path name. Example: </p>
<dl>
<dt>
<dd>
<pre>
[mysqld_safe]
malloc-lib=/opt/lib/libtcmalloc_minimal.so
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;mysqld=</code><i>prog_name</i> </p>
<p> The name of the server program (in the ledir directory) that you want to start. This option is needed if you use the MySQL binary distribution but have the data directory outside of the binary distribution. If <code>mysqld_safe</code> cannot find the server, use the <code>&#8211;ledir</code> option to indicate the path name to the directory where the server is located. </p>
<p> This option is accepted only on the command line, not in option files. On platforms that use systemd, the value can be specified in the value of MYSQLD_OPTS. See Section 2.5.9, &#8220;Managing MySQL Server with systemd&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;mysqld-version=</code><i>suffix</i> </p>
<p> This option is similar to the <code>&#8211;mysqld</code> option, but you specify only the suffix for the server program name. The base name is assumed to be <code>mysqld</code>. For example, if you use <code>&#8211;mysqld-version=debug</code>, <code>mysqld_safe</code> starts the <code>mysqld-debug</code> program in the ledir directory. If the argument to <code>&#8211;mysqld-version</code> is empty, <code>mysqld_safe</code> uses <code>mysqld</code> in the ledir directory. </p>
<p> This option is accepted only on the command line, not in option files. On platforms that use systemd, the value can be specified in the value of MYSQLD_OPTS. See Section 2.5.9, &#8220;Managing MySQL Server with systemd&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;nice=</code><i>priority</i> </p>
<p> Use the nice program to set the server&#8217;s scheduling priority to the given value.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;no-defaults</code> </p>
<p> Do not read any option files. If program startup fails due to reading unknown options from an option file, <code>&#8211;no-defaults</code> can be used to prevent them from being read. This must be the first option on the command line if it is used. </p>
<p> For additional information about this and other option-file options, see Section 4.2.2.3, &#8220;Command-Line Options that Affect Option-File Handling&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;open-files-limit=</code><i>count</i> </p>
<p> The number of files that <code>mysqld</code> should be able to open. The option value is passed to <code>ulimit -n</code>. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font><br />
 You must start <code>mysqld_safe</code> as root for this to function properly. </p>
</dl>
</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;pid-file=</code><i>file_name</i> </p>
<p> The path name that <code>mysqld</code> should use for its process ID file.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;plugin-dir=</code><i>dir_name</i> </p>
<p> The path name of the plugin directory.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;port=</code><i>port_num</i> </p>
<p> The port number that the server should use when listening for TCP/IP connections. The port number must be 1024 or higher unless the server is started by the root operating system user.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;skip-kill-mysqld</code> </p>
<p> Do not try to kill stray <code>mysqld</code> processes at startup. This option works only on Linux.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;socket=</code><i>path</i> </p>
<p> The Unix socket file that the server should use when listening for local connections.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;syslog</code>, <code>&#8211;skip-syslog</code> </p>
<p> <code>&#8211;syslog</code> causes error messages to be sent to syslog on systems that support the <code>logger</code> program. &#8211;skip-syslog suppresses the use of syslog; messages are written to an error log file. </p>
<p> When syslog is used for error logging, the daemon.err facility/severity is used for all log messages. </p>
<p> Using these options to control <code>mysqld</code> logging is deprecated. To write error log output to the system log, use the instructions at Section 5.4.2.7, &#8220;Error Logging to the System Log&#8221;. To control the facility, use the server log_syslog_facility system variable.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;syslog-tag=</code><i>tag</i> </p>
<p> For logging to syslog, messages from <code>mysqld_safe</code> and <code>mysqld</code> are written with identifiers of mysqld_safe and mysqld, respectively. To specify a suffix for the identifiers, use <code>&#8211;syslog-tag=</code><i>tag</i>, which modifies the identifiers to be mysqld_safe-<i>tag</i> and mysqld-<i>tag</i>. </p>
<p> Using this option to control <code>mysqld</code> logging is deprecated. Use the server log_syslog_tag system variable instead. See Section 5.4.2.7, &#8220;Error Logging to the System Log&#8221;.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;timezone=</code><i>timezone</i> </p>
<p> Set the TZ time zone environment variable to the given option value. Consult your operating system documentation for legal time zone specification formats.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;user={</code><i>user_name</i><code>|</code><i>user_id</i><code>}</code> </p>
<p> Run the <code>mysqld</code> server as the user having the name <i>user_name</i> or the numeric user ID <i>user_id</i>. (&#8220;User&#8221; in this context refers to a system login account, not a MySQL user listed in the grant tables.)</dl>
<p> If you execute <code>mysqld_safe</code> with the <code>&#8211;defaults-file</code> or <code>&#8211;defaults-extra-file</code> option to name an option file, the option must be the first one given on the command line or the option file will not be used. For example, this command will not use the named option file: </p>
<dl>
<dt>
<dd>
<pre>
mysql&gt; <code>mysqld_safe --port=</code><i>port_num</i><code> --defaults-file=</code><i>file_name</i>
</pre>
</dl>
<p> Instead, use the following command: </p>
<dl>
<dt>
<dd>
<pre>
mysql&gt; <code>mysqld_safe --defaults-file=</code><i>file_name</i><code> --port=</code><i>port_num</i>
</pre>
</dl>
<p> The <code>mysqld_safe</code> script is written so that it normally can start a server that was installed from either a source or a binary distribution of MySQL, even though these types of distributions typically install the server in slightly different locations. (See Section 2.1.4, &#8220;Installation Layouts&#8221;.) <code>mysqld_safe</code> expects one of the following conditions to be true: </p>
<dl>
<dt>
<dd> &bull; The server and databases can be found relative to the working directory (the directory from which <code>mysqld_safe</code> is invoked). For binary distributions, <code>mysqld_safe</code> looks under its working directory for bin and data directories. For source distributions, it looks for libexec and var directories. This condition should be met if you execute <code>mysqld_safe</code> from your MySQL installation directory (for example, /usr/local/mysql for a binary distribution).</dl>
<dl>
<dt>
<dd> &bull; If the server and databases cannot be found relative to the working directory, <code>mysqld_safe</code> attempts to locate them by absolute path names. Typical locations are /usr/local/libexec and /usr/local/var. The actual locations are determined from the values configured into the distribution at the time it was built. They should be correct if MySQL is installed in the location specified at configuration time.</dl>
<p> Because <code>mysqld_safe</code> tries to find the server and databases relative to its own working directory, you can install a binary distribution of MySQL anywhere, as long as you run <code>mysqld_safe</code> from the MySQL installation directory: </p>
<dl>
<dt>
<dd>
<pre>
shell&gt; <code>cd </code><i>mysql_installation_directory</i>
shell&gt; <code>bin/mysqld_safe &amp;</code>
</pre>
</dl>
<p> If <code>mysqld_safe</code> fails, even when invoked from the MySQL installation directory, specify the <code>&#8211;ledir</code> and <code>&#8211;datadir</code> options to indicate the directories in which the server and databases are located on your system. </p>
<p> <code>mysqld_safe</code> tries to use the <code>sleep</code> and <code>date</code> system utilities to determine how many times per second it has attempted to start. If these utilities are present and the attempted starts per second is greater than 5, <code>mysqld_safe</code> waits 1 full second before starting again. This is intended to prevent excessive CPU usage in the event of repeated failures. (Bug #11761530, Bug #54035) </p>
<p> When you use <code>mysqld_safe</code> to start <code>mysqld</code>, <code>mysqld_safe</code> arranges for error (and notice) messages from itself and from <code>mysqld</code> to go to the same destination. </p>
<p> There are several <code>mysqld_safe</code> options for controlling the destination of these messages: </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;log-error=</code><i>file_name</i>: Write error messages to the named error file.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;syslog</code>: Write error messages to syslog on systems that support the <code>logger</code> program.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;skip-syslog</code>: Do not write error messages to syslog. Messages are written to the default error log file (<i>host_name</i>.err in the data directory), or to a named file if the <code>&#8211;log-error</code> option is given.</dl>
<p> If none of these options is given, the default is <code>&#8211;skip-syslog</code>. </p>
<p> When <code>mysqld_safe</code> writes a message, notices go to the logging destination (syslog or the error log file) and stdout. Errors go to the logging destination and stderr. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> Controlling <code>mysqld</code> logging from <code>mysqld_safe</code> is deprecated. Use the server&#8217;s native syslog support instead. For more information, see Section 5.4.2.7, &#8220;Error Logging to the System Log&#8221;. </p>
</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1997, 2020, Oracle and/or its affiliates. All rights reserved. </p>
<p> This documentation is free software; you can redistribute it and/or modify it only under the terms of the GNU General Public License as published by the Free Software Foundation; version 2 of the License. </p>
<p> This documentation is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with the program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA or see <a rel="nofollow" href="http://www.gnu.org/licenses/.">http://www.gnu.org/licenses/.</a> </p>
<h2>SEE ALSO</h2>
<p> For more information, please refer to the MySQL Reference Manual, which may already be installed locally and which is also available online at <a rel="nofollow" href="http://dev.mysql.com/doc/.">http://dev.mysql.com/doc/.</a></p>
<h2>AUTHOR</h2>
<p> Oracle Corporation (<a rel="nofollow" href="http://dev.mysql.com/">http://dev.mysql.com/</a>). </p>
<h2>Index</h2>
