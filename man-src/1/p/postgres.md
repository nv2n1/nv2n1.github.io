---
title: "postgres(1)"
name: "postgres"
section: "1"
letter: "p"
url: "/docs/linux/man/1-postgres/"
description: "postgres – PostgreSQL database server"
---

<h2 class="name">NAME</h2>
<p> postgres &#8211; PostgreSQL database server </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>postgres</code> [<i>option</i>&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>postgres</code></p>
<dd>is the PostgreSQL database server. In order for a client application to access a database it connects (over a network or locally) to a running <code>postgres</code> instance. The <code>postgres</code> instance then starts a separate server process to handle the connection. </p>
<p> One <code>postgres</code> instance always manages the data of exactly one database cluster. A database cluster is a collection of databases that is stored at a common file system location (the &#8220;data area&#8221;). More than one <code>postgres</code> instance can run on a system at one time, so long as they use different data areas and different communication ports (see below). When <code>postgres</code> starts it needs to know the location of the data area. The location must be specified by the <code>-D</code> option or the <code>PGDATA</code> environment variable; there is no default. Typically, <code>-D</code> or <code>PGDATA</code> points directly to the data area directory created by <code><a href="/docs/linux/man/1-initdb/">initdb</a></code>(1). Other possible file layouts are discussed in Section 18.2, &#8220;File Locations&#8221;, in the documentation. </p>
<p> By default <code>postgres</code> starts in the foreground and prints log messages to the standard error stream. In practical applications <code>postgres</code> should be started as a background process, perhaps at boot time. </p>
<p> The <code>postgres</code> command can also be called in single-user mode. The primary use for this mode is during bootstrapping by <code><a href="/docs/linux/man/1-initdb/">initdb</a></code>(1). Sometimes it is used for debugging or disaster recovery; note that running a single-user server is not truly suitable for debugging the server, since no realistic interprocess communication and locking will happen. When invoked in single-user mode from the shell, the user can enter queries and the results will be printed to the screen, but in a form that is more useful for developers than end users. In the single-user mode, the session user will be set to the user with ID 1, and implicit superuser powers are granted to this user. This user does not actually have to exist, so the single-user mode can be used to manually recover from certain kinds of accidental damage to the system catalogs.</p>
<h2>OPTIONS</h2>
<p> <code>postgres</code> accepts the following command-line arguments. For a detailed discussion of the options consult Chapter 18, Server Configuration, in the documentation. You can save typing most of these options by setting up a configuration file. Some (safe) options can also be set from the connecting client in an application-dependent way to apply only for that session. For example, if the environment variable <code>PGOPTIONS</code> is set, then libpq-based clients will pass that string to the server, which will interpret it as <code>postgres</code> command-line options.</p>
<h3>General Purpose</h3>
<p> <code>-A 0|1</code></p>
<dl>
<dt>
<dd> Enables run-time assertion checks, which is a debugging aid to detect programming mistakes. This option is only available if assertions were enabled when PostgreSQL was compiled. If so, the default is on.</dl>
<p> <code>-B </code><i>nbuffers</i></p>
<dl>
<dt>
<dd> Sets the number of shared buffers for use by the server processes. The default value of this parameter is chosen automatically by initdb. Specifying this option is equivalent to setting the shared_buffers configuration parameter.</dl>
<p> <code>-c </code><i>name</i><code>=</code><i>value</i></p>
<dl>
<dt>
<dd> Sets a named run-time parameter. The configuration parameters supported by PostgreSQL are described in Chapter 18, Server Configuration, in the documentation. Most of the other command line options are in fact short forms of such a parameter assignment. <code>-c</code> can appear multiple times to set multiple parameters.</dl>
<p> <code>-C </code><i>name</i></p>
<dl>
<dt>
<dd> Prints the value of the named run-time parameter, and exits. (See the <code>-c</code> option above for details.) This can be used on a running server, and returns values from postgresql.conf, modified by any parameters supplied in this invocation. It does not reflect parameters supplied when the cluster was started. </p>
<p> This option is meant for other programs that interact with a server instance, such as <code><a href="/docs/linux/man/1-pg_ctl/">pg_ctl</a></code>(1), to query configuration parameter values. User-facing applications should instead use <code><a href="/docs/linux/man/7-show/">SHOW</a></code>(7) or the pg_settings view.</dl>
<p> <code>-d </code><i>debug-level</i></p>
<dl>
<dt>
<dd> Sets the debug level. The higher this value is set, the more debugging output is written to the server log. Values are from 1 to 5. It is also possible to pass -d 0 for a specific session, which will prevent the server log level of the parent <code>postgres</code> process from being propagated to this session.</dl>
<p> <code>-D </code><i>datadir</i></p>
<dl>
<dt>
<dd> Specifies the file system location of the data directory or configuration file(s). See Section 18.2, &#8220;File Locations&#8221;, in the documentation for details.</dl>
<p> <code>-e</code></p>
<dl>
<dt>
<dd> Sets the default date style to &#8220;European&#8221;, that is DMY ordering of input date fields. This also causes the day to be printed before the month in certain date output formats. See Section 8.5, &#8220;Date/Time Types&#8221;, in the documentation for more information.</dl>
<p> <code>-F</code></p>
<dl>
<dt>
<dd> Disables <code>fsync</code> calls for improved performance, at the risk of data corruption in the event of a system crash. Specifying this option is equivalent to disabling the fsync configuration parameter. Read the detailed documentation before using this!</dl>
<p> <code>-h </code><i>hostname</i></p>
<dl>
<dt>
<dd> Specifies the IP host name or address on which <code>postgres</code> is to listen for TCP/IP connections from client applications. The value can also be a comma-separated list of addresses, or * to specify listening on all available interfaces. An empty value specifies not listening on any IP addresses, in which case only Unix-domain sockets can be used to connect to the server. Defaults to listening only on localhost. Specifying this option is equivalent to setting the listen_addresses configuration parameter.</dl>
<p> <code>-i</code></p>
<dl>
<dt>
<dd> Allows remote clients to connect via TCP/IP (Internet domain) connections. Without this option, only local connections are accepted. This option is equivalent to setting <i>listen_addresses</i> to * in postgresql.conf or via <code>-h</code>. </p>
<p> This option is deprecated since it does not allow access to the full functionality of listen_addresses. It&#8217;s usually better to set <i>listen_addresses</i> directly.</dl>
<p> <code>-k </code><i>directory</i></p>
<dl>
<dt>
<dd> Specifies the directory of the Unix-domain socket on which <code>postgres</code> is to listen for connections from client applications. The value can also be a comma-separated list of directories. An empty value specifies not listening on any Unix-domain sockets, in which case only TCP/IP sockets can be used to connect to the server. The default value is normally /tmp, but that can be changed at build time. Specifying this option is equivalent to setting the unix_socket_directories configuration parameter.</dl>
<p> <code>-l</code></p>
<dl>
<dt>
<dd> Enables secure connections using SSL. PostgreSQL must have been compiled with support for SSL for this option to be available. For more information on using SSL, refer to Section 17.9, &#8220;Secure TCP/IP Connections with SSL&#8221;, in the documentation.</dl>
<p> <code>-N </code><i>max-connections</i></p>
<dl>
<dt>
<dd> Sets the maximum number of client connections that this server will accept. The default value of this parameter is chosen automatically by initdb. Specifying this option is equivalent to setting the max_connections configuration parameter.</dl>
<p> <code>-o </code><i>extra-options</i></p>
<dl>
<dt>
<dd> The command-line-style options specified in <i>extra-options</i> are passed to all server processes started by this <code>postgres</code> process. If the option string contains any spaces, the entire string must be quoted. </p>
<p> The use of this option is obsolete; all command-line options for server processes can be specified directly on the <code>postgres</code> command line.</dl>
<p> <code>-p </code><i>port</i></p>
<dl>
<dt>
<dd> Specifies the TCP/IP port or local Unix domain socket file extension on which <code>postgres</code> is to listen for connections from client applications. Defaults to the value of the <code>PGPORT</code> environment variable, or if <code>PGPORT</code> is not set, then defaults to the value established during compilation (normally 5432). If you specify a port other than the default port, then all client applications must specify the same port using either command-line options or <code>PGPORT</code>.</dl>
<p> <code>-s</code></p>
<dl>
<dt>
<dd> Print time information and other statistics at the end of each command. This is useful for benchmarking or for use in tuning the number of buffers.</dl>
<p> <code>-S</code> <i>work-mem</i></p>
<dl>
<dt>
<dd> Specifies the amount of memory to be used by internal sorts and hashes before resorting to temporary disk files. See the description of the <i>work_mem</i> configuration parameter in Section 18.4.1, &#8220;Memory&#8221;, in the documentation.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print the postgres version and exit.</dl>
<p> <code>&#8212;</code><i>name</i><code>=</code><i>value</i></p>
<dl>
<dt>
<dd> Sets a named run-time parameter; a shorter form of <code>-c</code>.</dl>
<p> <code>&#8211;describe-config</code></p>
<dl>
<dt>
<dd> This option dumps out the server&#8217;s internal configuration variables, descriptions, and defaults in tab-delimited <code>COPY</code> format. It is designed primarily for use by administration tools.</dl>
<p> <code>-?</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help about postgres command line arguments, and exit.</dl>
<h3>Semi-internal Options</h3>
<p> The options described here are used mainly for debugging purposes, and in some cases to assist with recovery of severely damaged databases. There should be no reason to use them in a production database setup. They are listed here only for use by PostgreSQL system developers. Furthermore, these options might change or be removed in a future release without notice. </p>
<p> <code>-f</code> { s | i | o | b | t | n | m | h }</p>
<dl>
<dt>
<dd> Forbids the use of particular scan and join methods: s and i disable sequential and index scans respectively, o, b and t disable index-only scans, bitmap index scans, and TID scans respectively, while n, m, and h disable nested-loop, merge and hash joins respectively. </p>
<p> Neither sequential scans nor nested-loop joins can be disabled completely; the -fs and -fn options simply discourage the optimizer from using those plan types if it has any other alternative.</dl>
<p> <code>-n</code></p>
<dl>
<dt>
<dd> This option is for debugging problems that cause a server process to die abnormally. The ordinary strategy in this situation is to notify all other server processes that they must terminate and then reinitialize the shared memory and semaphores. This is because an errant server process could have corrupted some shared state before terminating. This option specifies that <code>postgres</code> will not reinitialize shared data structures. A knowledgeable system programmer can then use a debugger to examine shared memory and semaphore state.</dl>
<p> <code>-O</code></p>
<dl>
<dt>
<dd> Allows the structure of system tables to be modified. This is used by <code>initdb</code>.</dl>
<p> <code>-P</code></p>
<dl>
<dt>
<dd> Ignore system indexes when reading system tables, but still update the indexes when modifying the tables. This is useful when recovering from damaged system indexes.</dl>
<p> <code>-t</code> pa[rser] | pl[anner] | e[xecutor]</p>
<dl>
<dt>
<dd> Print timing statistics for each query relating to each of the major system modules. This option cannot be used together with the <code>-s</code> option.</dl>
<p> <code>-T</code></p>
<dl>
<dt>
<dd> This option is for debugging problems that cause a server process to die abnormally. The ordinary strategy in this situation is to notify all other server processes that they must terminate and then reinitialize the shared memory and semaphores. This is because an errant server process could have corrupted some shared state before terminating. This option specifies that <code>postgres</code> will stop all other server processes by sending the signal SIGSTOP, but will not cause them to terminate. This permits system programmers to collect core dumps from all server processes by hand.</dl>
<p> <code>-v</code> <i>protocol</i></p>
<dl>
<dt>
<dd> Specifies the version number of the frontend/backend protocol to be used for a particular session. This option is for internal use only.</dl>
<p> <code>-W</code> <i>seconds</i></p>
<dl>
<dt>
<dd> A delay of this many seconds occurs when a new server process is started, after it conducts the authentication procedure. This is intended to give an opportunity to attach to the server process with a debugger.</dl>
<h3>Options for Single-User Mode</h3>
<p> The following options only apply to the single-user mode. </p>
<p> <code>&#8211;single</code></p>
<dl>
<dt>
<dd> Selects the single-user mode. This must be the first argument on the command line.</dl>
<p> <i>database</i></p>
<dl>
<dt>
<dd> Specifies the name of the database to be accessed. This must be the last argument on the command line. If it is omitted it defaults to the user name.</dl>
<p> <code>-E</code></p>
<dl>
<dt>
<dd> Echo all commands.</dl>
<p> <code>-j</code></p>
<dl>
<dt>
<dd> Disables use of newline as a statement delimiter.</dl>
<p> <code>-r</code> <i>filename</i></p>
<dl>
<dt>
<dd> Send all server log output to <i>filename</i>. In normal multiuser mode, this option is ignored, and stderr is used by all processes.</dl>
<h2>ENVIRONMENT</h2>
<p> <code>PGCLIENTENCODING</code></p>
<dl>
<dt>
<dd> Default character encoding used by clients. (The clients can override this individually.) This value can also be set in the configuration file.</dl>
<p> <code>PGDATA</code></p>
<dl>
<dt>
<dd> Default data directory location</dl>
<p> <code>PGDATESTYLE</code></p>
<dl>
<dt>
<dd> Default value of the DateStyle run-time parameter. (The use of this environment variable is deprecated.)</dl>
<p> <code>PGPORT</code></p>
<dl>
<dt>
<dd> Default port number (preferably set in the configuration file)</dl>
<h2>DIAGNOSTICS</h2>
<p> A failure message mentioning semget or shmget probably indicates you need to configure your kernel to provide adequate shared memory and semaphores. For more discussion see Section 17.4, &#8220;Managing Kernel Resources&#8221;, in the documentation. You might be able to postpone reconfiguring your kernel by decreasing shared_buffers to reduce the shared memory consumption of PostgreSQL, and/or by reducing max_connections to reduce the semaphore consumption. </p>
<p> A failure message suggesting that another server is already running should be checked carefully, for example by using the command </p>
<dl>
<dt>
<dd>
<pre>
$ <code>ps ax | grep postgres</code>
</pre>
</dl>
<p> or </p>
<dl>
<dt>
<dd>
<pre>
$ <code>ps -ef | grep postgres</code>
</pre>
</dl>
<p> depending on your system. If you are certain that no conflicting server is running, you can remove the lock file mentioned in the message and try again. </p>
<p> A failure message indicating inability to bind to a port might indicate that that port is already in use by some non-PostgreSQL process. You might also get this error if you terminate <code>postgres</code> and immediately restart it using the same port; in this case, you must simply wait a few seconds until the operating system closes the port before trying again. Finally, you might get this error if you specify a port number that your operating system considers to be reserved. For example, many versions of Unix consider port numbers under 1024 to be &#8220;trusted&#8221; and only permit the Unix superuser to access them.</p>
<h2>NOTES</h2>
<p> The utility command <code><a href="/docs/linux/man/1-pg_ctl/">pg_ctl</a></code>(1) can be used to start and shut down the <code>postgres</code> server safely and comfortably. </p>
<p> If at all possible, <i>do not</i> use SIGKILL to kill the main <code>postgres</code> server. Doing so will prevent <code>postgres</code> from freeing the system resources (e.g., shared memory and semaphores) that it holds before terminating. This might cause problems for starting a fresh <code>postgres</code> run. </p>
<p> To terminate the <code>postgres</code> server normally, the signals SIGTERM, SIGINT, or SIGQUIT can be used. The first will wait for all clients to terminate before quitting, the second will forcefully disconnect all clients, and the third will quit immediately without proper shutdown, resulting in a recovery run during restart. </p>
<p> The SIGHUP signal will reload the server configuration files. It is also possible to send SIGHUP to an individual server process, but that is usually not sensible. </p>
<p> To cancel a running query, send the SIGINT signal to the process running that command. </p>
<p> The <code>postgres</code> server uses SIGTERM to tell subordinate server processes to quit normally and SIGQUIT to terminate without the normal cleanup. These signals <i>should not</i> be used by users. It is also unwise to send SIGKILL to a server process &#8212; the main <code>postgres</code> process will interpret this as a crash and will force all the sibling processes to quit as part of its standard crash-recovery procedure.</p>
<h2>BUGS</h2>
<p> The <code>&#8212;</code> options will not work on FreeBSD or OpenBSD. Use <code>-c</code> instead. This is a bug in the affected operating systems; a future release of PostgreSQL will provide a workaround if this is not fixed.</p>
<h2>USAGE</h2>
<p> To start a single-user mode server, use a command like </p>
<dl>
<dt>
<dd>
<pre>
<code>postgres --single -D /usr/local/pgsql/data </code><i>other-options</i><code> my_database</code>
</pre>
</dl>
<p> Provide the correct path to the database directory with <code>-D</code>, or make sure that the environment variable <code>PGDATA</code> is set. Also specify the name of the particular database you want to work in. </p>
<p> Normally, the single-user mode server treats newline as the command entry terminator; there is no intelligence about semicolons, as there is in psql. To continue a command across multiple lines, you must type backslash just before each newline except the last one. </p>
<p> But if you use the <code>-j</code> command line switch, then newline does not terminate command entry. In this case, the server will read the standard input until the end-of-file (EOF) marker, then process the input as a single command string. Backslash-newline is not treated specially in this case. </p>
<p> To quit the session, type EOF (Control+D, usually). If you&#8217;ve used <code>-j</code>, two consecutive EOFs are needed to exit. </p>
<p> Note that the single-user mode server does not provide sophisticated line-editing features (no command history, for example). Single-User mode also does not do any background processing, like automatic checkpoints.</p>
<h2>EXAMPLES</h2>
<p> To start <code>postgres</code> in the background using default values, type: </p>
<dl>
<dt>
<dd>
<pre>
$ <code>nohup postgres &gt;logfile 2&gt;&amp;1 &lt;/dev/null &amp;</code>
</pre>
</dl>
<p> To start <code>postgres</code> with a specific port, e.g. 1234: </p>
<dl>
<dt>
<dd>
<pre>
$ <code>postgres -p 1234</code>
</pre>
</dl>
<p> To connect to this server using psql, specify this port with the -p option: </p>
<dl>
<dt>
<dd>
<pre>
$ <code>psql -p 1234</code>
</pre>
</dl>
<p> or set the environment variable <code>PGPORT</code>: </p>
<dl>
<dt>
<dd>
<pre>
$ <code>export PGPORT=1234</code>
$ <code>psql</code>
</pre>
</dl>
<p> Named run-time parameters can be set in either of these styles: </p>
<dl>
<dt>
<dd>
<pre>
$ <code>postgres -c work_mem=1234</code>
$ <code>postgres --work-mem=1234</code>
</pre>
</dl>
<p> Either form overrides whatever setting might exist for <i>work_mem</i> in postgresql.conf. Notice that underscores in parameter names can be written as either underscore or dash on the command line. Except for short-term experiments, it&#8217;s probably better practice to edit the setting in postgresql.conf than to rely on a command-line switch to set a parameter.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-initdb/">initdb</a></code>(1), <code><a href="/docs/linux/man/1-pg_ctl/">pg_ctl</a></code>(1) </p>
<h2>Index</h2>
