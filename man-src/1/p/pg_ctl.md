---
title: "pg_ctl(1)"
name: "pg_ctl"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pg_ctl/"
description: "pg_ctl – initialize, start, stop, or control a PostgreSQL server"
---
<h2 class="name">NAME</h2>
<p> pg_ctl - initialize, start, stop, or control a PostgreSQL server </p>
<h2>SYNOPSIS</h2>
<dl>
<dt><code>pg_ctl</code><code>init[db]</code> [<code>-s</code>] [<code>-D</code>&nbsp;<wbr><i>datadir</i>] [<code>-o</code>&nbsp;<wbr><i>initdb-options</i>] </dt>
<dt><code>pg_ctl</code><code>start</code> [<code>-w</code>] [<code>-t</code>&nbsp;<wbr><i>seconds</i>] [<code>-s</code>] [<code>-D</code>&nbsp;<wbr><i>datadir</i>] [<code>-l</code>&nbsp;<wbr><i>filename</i>] [<code>-o</code>&nbsp;<wbr><i>options</i>] [<code>-p</code>&nbsp;<wbr><i>path</i>] [<code>-c</code>] </dt>
<dt><code>pg_ctl</code><code>stop</code> [<code>-W</code>] [<code>-t</code>&nbsp;<wbr><i>seconds</i>] [<code>-s</code>] [<code>-D</code>&nbsp;<wbr><i>datadir</i>] [<code>-m</code>&nbsp;<wbr><code>s[mart]</code>&nbsp;<wbr>|&nbsp;<wbr><code>f[ast]</code>&nbsp;<wbr>|&nbsp;<wbr><code>i[mmediate]</code>] </dt>
<dt><code>pg_ctl</code><code>restart</code> [<code>-w</code>] [<code>-t</code>&nbsp;<wbr><i>seconds</i>] [<code>-s</code>] [<code>-D</code>&nbsp;<wbr><i>datadir</i>] [<code>-c</code>] [<code>-m</code>&nbsp;<wbr><code>s[mart]</code>&nbsp;<wbr>|&nbsp;<wbr><code>f[ast]</code>&nbsp;<wbr>|&nbsp;<wbr><code>i[mmediate]</code>] [<code>-o</code>&nbsp;<wbr><i>options</i>] </dt>
<dt><code>pg_ctl</code><code>reload</code> [<code>-s</code>] [<code>-D</code>&nbsp;<wbr><i>datadir</i>] </dt>
<dt><code>pg_ctl</code><code>status</code> [<code>-D</code>&nbsp;<wbr><i>datadir</i>] </dt>
<dt><code>pg_ctl</code><code>promote</code> [<code>-s</code>] [<code>-D</code>&nbsp;<wbr><i>datadir</i>] </dt>
<dt><code>pg_ctl</code><code>kill</code><i>signal_name</i><i>process_id</i></dt>
<dt><code>pg_ctl</code><code>register</code> [<code>-N</code>&nbsp;<wbr><i>servicename</i>] [<code>-U</code>&nbsp;<wbr><i>username</i>] [<code>-P</code>&nbsp;<wbr><i>password</i>] [<code>-D</code>&nbsp;<wbr><i>datadir</i>] [<code>-S</code>&nbsp;<wbr><code>a[uto]</code>&nbsp;<wbr>|&nbsp;<wbr><code>d[emand]</code>] [<code>-w</code>] [<code>-t</code>&nbsp;<wbr><i>seconds</i>] [<code>-s</code>] [<code>-o</code>&nbsp;<wbr><i>options</i>] </dt>
<dt><code>pg_ctl</code><code>unregister</code> [<code>-N</code>&nbsp;<wbr><i>servicename</i>] </dt>
</dl>
<h2>DESCRIPTION</h2>
<dd> <p> pg_ctl is a utility for initializing a PostgreSQL database cluster, starting, stopping, or restarting the PostgreSQL database server (<code><a href="/docs/linux/man/1-postgres/">postgres</a></code>(1)), or displaying the status of a running server. Although the server can be started manually, pg_ctl encapsulates tasks such as redirecting log output and properly detaching from the terminal and process group. It also provides convenient options for controlled shutdown. </p>
<p> The <code>init</code> or <code>initdb</code> mode creates a new PostgreSQL database cluster. A database cluster is a collection of databases that are managed by a single server instance. This mode invokes the <code>initdb</code> command. See <code><a href="/docs/linux/man/1-initdb/">initdb</a></code>(1) for details. </p>
<p> In <code>start</code> mode, a new server is launched. The server is started in the background, and its standard input is attached to /dev/null (or nul on Windows). On Unix-like systems, by default, the server&#8217;s standard output and standard error are sent to pg_ctl&#8217;s standard output (not standard error). The standard output of pg_ctl should then be redirected to a file or piped to another process such as a log rotating program like rotatelogs; otherwise <code>postgres</code> will write its output to the controlling terminal (from the background) and will not leave the shell&#8217;s process group. On Windows, by default the server&#8217;s standard output and standard error are sent to the terminal. These default behaviors can be changed by using <code>-l</code> to append the server&#8217;s output to a log file. Use of either <code>-l</code> or output redirection is recommended. </p>
<p> In <code>stop</code> mode, the server that is running in the specified data directory is shut down. Three different shutdown methods can be selected with the <code>-m</code> option. "Smart" mode (the default) waits for all active clients to disconnect and any online backup to finish. If the server is in hot standby, recovery and streaming replication will be terminated once all clients have disconnected. "Fast" mode does not wait for clients to disconnect and will terminate an online backup in progress. All active transactions are rolled back and clients are forcibly disconnected, then the server is shut down. "Immediate" mode will abort all server processes immediately, without a clean shutdown. This will lead to a crash-recovery run on the next restart. </p>
<p> <code>restart</code> mode effectively executes a stop followed by a start. This allows changing the <code>postgres</code> command-line options. </p>
<p> <code>reload</code> mode simply sends the <code>postgres</code> process a SIGHUP signal, causing it to reread its configuration files (postgresql.conf, pg_hba.conf, etc.). This allows changing of configuration-file options that do not require a complete restart to take effect. </p>
<p> <code>status</code> mode checks whether a server is running in the specified data directory. If it is, the PID and the command line options that were used to invoke it are displayed. If the server is not running, the process returns an exit status of 3. </p>
<p> In <code>promote</code> mode, the standby server that is running in the specified data directory is commanded to exit recovery and begin read-write operations. </p>
<p> <code>kill</code> mode allows you to send a signal to a specified process. This is particularly valuable for Microsoft Windows which does not have a kill command. Use --help to see a list of supported signal names. </p>
<p> <code>register</code> mode allows you to register a system service on Microsoft Windows. The <code>-S</code> option allows selection of service start type, either "auto" (start service automatically on system startup) or "demand" (start service on demand). </p>
<p> <code>unregister</code> mode allows you to unregister a system service on Microsoft Windows. This undoes the effects of the <code>register</code> command.  </p>
<h2>OPTIONS</h2>
<p> <code>-c</code>, <code>--core-file</code> </p>
 </dd>
<dl>
<dd> <p> Attempt to allow server crashes to produce core files, on platforms where this is possible, by lifting any soft resource limit placed on core files. This is useful in debugging or diagnosing problems by allowing a stack trace to be obtained from a failed server process. </p>
 </dd></dl>
<p> <code>-D </code><i>datadir</i>, <code>--pgdata </code><i>datadir</i> </p>
<dl>
<dd> <p> Specifies the file system location of the database files. If this is omitted, the environment variable <code>PGDATA</code> is used. </p>
 </dd></dl>
<p> <code>-l </code><i>filename</i>, <code>--log </code><i>filename</i> </p>
<dl>
<dd> <p> Append the server log output to <i>filename</i>. If the file does not exist, it is created. The umask is set to 077, so access to the log file is disallowed to other users by default. </p>
 </dd></dl>
<p> <code>-m </code><i>mode</i>, <code>--mode </code><i>mode</i> </p>
<dl>
<dd> <p> Specifies the shutdown mode. <i>mode</i> can be smart, fast, or immediate, or the first letter of one of these three. If this is omitted, smart is used. </p>
 </dd></dl>
<p> <code>-o </code><i>options</i> </p>
<dl>
<dd> <p> Specifies options to be passed directly to the <code>postgres</code> command. </p>
<p> The options should usually be surrounded by single or double quotes to ensure that they are passed through as a group. </p>
 </dd></dl>
<p> <code>-o </code><i>initdb-options</i> </p>
<dl>
<dd> <p> Specifies options to be passed directly to the <code>initdb</code> command. </p>
<p> The options should usually be surrounded by single or double quotes to ensure that they are passed through as a group. </p>
 </dd></dl>
<p> <code>-p </code><i>path</i> </p>
<dl>
<dd> <p> Specifies the location of the postgres executable. By default the postgres executable is taken from the same directory as <code>pg_ctl</code>, or failing that, the hard-wired installation directory. It is not necessary to use this option unless you are doing something unusual and get errors that the postgres executable was not found. </p>
<p> In init mode, this option analogously specifies the location of the initdb executable. </p>
 </dd></dl>
<p> <code>-s</code>, <code>--silent</code> </p>
<dl>
<dd> <p> Print only errors, no informational messages. </p>
 </dd></dl>
<p> <code>-t</code>, <code>--timeout</code> </p>
<dl>
<dd> <p> The maximum number of seconds to wait when waiting for startup or shutdown to complete. Defaults to the value of the <code>PGCTLTIMEOUT</code> environment variable or, if not set, to 60 seconds. </p>
 </dd></dl>
<p> <code>-V</code>, <code>--version</code> </p>
<dl>
<dd> <p> Print the pg_ctl version and exit. </p>
 </dd></dl>
<p> <code>-w</code> </p>
<dl>
<dd> <p> Wait for the startup or shutdown to complete. Waiting is the default option for shutdowns, but not startups. When waiting for startup, <code>pg_ctl</code> repeatedly attempts to connect to the server. When waiting for shutdown, <code>pg_ctl</code> waits for the server to remove its PID file. <code>pg_ctl</code> returns an exit code based on the success of the startup or shutdown. </p>
 </dd></dl>
<p> <code>-W</code> </p>
<dl>
<dd> <p> Do not wait for startup or shutdown to complete. This is the default for start and restart modes. </p>
 </dd></dl>
<p> <code>-?</code>, <code>--help</code> </p>
<dl>
<dd> <p> Show help about pg_ctl command line arguments, and exit. </p>
 </dd></dl>
<h3>Options for Windows</h3>
<p> <code>-N </code><i>servicename</i> </p>
<dl>
<dd> <p> Name of the system service to register. The name will be used as both the service name and the display name. </p>
 </dd></dl>
<p> <code>-P </code><i>password</i> </p>
<dl>
<dd> <p> Password for the user to start the service. </p>
 </dd></dl>
<p> <code>-S </code><i>start-type</i> </p>
<dl>
<dd> <p> Start type of the system service to register. start-type can be auto, or demand, or the first letter of one of these two. If this is omitted, auto is used. </p>
 </dd></dl>
<p> <code>-U </code><i>username</i> </p>
<dl>
<dd> <p> User name for the user to start the service. For domain users, use the format DOMAIN\username. </p>
 </dd></dl>
<h2>ENVIRONMENT</h2>
<p> <code>PGCTLTIMEOUT</code> </p>
<dl>
<dd> <p> Default limit on the number of seconds to wait when waiting for startup or shutdown to complete. If not set, the default is 60 seconds. </p>
 </dd></dl>
<p> <code>PGDATA</code> </p>
<dl>
<dd> <p> Default data directory location. </p>
 </dd></dl>
<p> <code>pg_ctl</code>, like most other PostgreSQL utilities, also uses the environment variables supported by libpq (see Section 31.14, "Environment Variables", in the documentation). For additional server variables, see <code><a href="/docs/linux/man/1-postgres/">postgres</a></code>(1).  </p>
<h2>FILES</h2>
<p> postmaster.pid </p>
<dl>
<dd> <p> The existence of this file in the data directory is used to help pg_ctl determine if the server is currently running. </p>
 </dd></dl>
<p> postmaster.opts </p>
<dl>
<dd> <p> If this file exists in the data directory, pg_ctl (in <code>restart</code> mode) will pass the contents of the file as options to postgres, unless overridden by the <code>-o</code> option. The contents of this file are also displayed in <code>status</code> mode. </p>
 </dd></dl>
<h2>EXAMPLES</h2>
<h3>Starting the Server</h3>
<p> To start the server: </p>
<dl>
<dd> <pre><code>$ pg_ctl start 
</code></pre>
 </dd></dl>
<p> To start the server, waiting until the server is accepting connections: </p>
<dl>
<dd> <pre><code>$ pg_ctl -w start 
</code></pre>
 </dd></dl>
<p> To start the server using port 5433, and running without <code>fsync</code>, use: </p>
<dl>
<dd> <pre><code>$ pg_ctl -o &quot;-F -p 5433&quot; start 
</code></pre>
 </dd></dl>
<h3>Stopping the Server</h3>
<p> To stop the server, use: </p>
<dl>
<dd> <pre><code>$ pg_ctl stop 
</code></pre>
 </dd></dl>
<p> The <code>-m</code> option allows control over <i>how</i> the server shuts down: </p>
<dl>
<dd> <pre><code>$ pg_ctl stop -m fast 
</code></pre>
 </dd></dl>
<h3>Restarting the Server</h3>
<p> Restarting the server is almost equivalent to stopping the server and starting it again, except that <code>pg_ctl</code> saves and reuses the command line options that were passed to the previously running instance. To restart the server in the simplest form, use: </p>
<dl>
<dd> <pre><code>$ pg_ctl restart 
</code></pre>
 </dd></dl>
<p> To restart the server, waiting for it to shut down and restart: </p>
<dl>
<dd> <pre><code>$ pg_ctl -w restart 
</code></pre>
 </dd></dl>
<p> To restart using port 5433, disabling <code>fsync</code> upon restart: </p>
<dl>
<dd> <pre><code>$ pg_ctl -o &quot;-F -p 5433&quot; restart 
</code></pre>
 </dd></dl>
<h3>Showing the Server Status</h3>
<p> Here is sample status output from pg_ctl: </p>
<dl>
<dd> <pre><code>$ pg_ctl status pg_ctl: server is running (PID: 13718)
/usr/local/pgsql/bin/postgres &quot;-D&quot; &quot;/usr/local/pgsql/data&quot; &quot;-p&quot; &quot;5433&quot; &quot;-B&quot; &quot;128&quot;
</code></pre>
 </dd></dl>
<p> This is the command line that would be invoked in restart mode.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-initdb/">initdb</a></code>(1), <code><a href="/docs/linux/man/1-postgres/">postgres</a></code>(1) </p>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">NAME</a></dt>
<dd>  </dd>
<dt><a href="#lbAC">SYNOPSIS</a></dt>
<dd>  </dd>
<dt><a href="#lbAD">DESCRIPTION</a></dt>
<dd>  </dd>
<dt><a href="#lbAE">OPTIONS</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbAF">Options for Windows</a></dt>
<dd>  </dd></dl>
<dt><a href="#lbAG">ENVIRONMENT</a></dt>
<dd>  </dd>
<dt><a href="#lbAH">FILES</a></dt>
<dd>  </dd>
<dt><a href="#lbAI">EXAMPLES</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbAJ">Starting the Server</a></dt>
<dd>  </dd>
<dt><a href="#lbAK">Stopping the Server</a></dt>
<dd>  </dd>
<dt><a href="#lbAL">Restarting the Server</a></dt>
<dd>  </dd>
<dt><a href="#lbAM">Showing the Server Status</a></dt>
<dd>  </dd></dl>
<dt><a href="#lbAN">SEE ALSO</a></dt>
<dd>  </dd></dl>
