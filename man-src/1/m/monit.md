---
title: "monit(1)"
name: "monit"
section: "1"
letter: "m"
url: "/docs/linux/man/1-monit/"
description: "Monit – utility for monitoring services on a Unix system"
---

<h2 class="name">NAME</h2>
<p> Monit &#8211; utility for monitoring services on a Unix system </p>
<h2>SYNOPSIS</h2>
<p> <code>monit</code> [options] {arguments}</p>
<h2>DESCRIPTION</h2>
<p> <code>Monit</code> is a utility for managing and monitoring processes, programs, files, directories and filesystems on a Unix system. Monit conducts automatic maintenance and repair and can execute meaningful causal actions in error situations. E.g. Monit can start a process if it does not run, restart a process if it does not respond and stop a process if it uses too much resources. You can use Monit to monitor files, directories and filesystems for changes, such as timestamps changes, checksum changes or size changes. </p>
<p> Monit is controlled via an easy to configure control file based on a free-format, token-oriented syntax. Monit logs to syslog or to its own log file and notifies you about error conditions via customizable alert messages. Monit can perform various <font SIZE="-1">TCP/IP</font> network checks, protocol checks and can utilize <font SIZE="-1">SSL</font> for such checks. Monit provides a http(s) interface and you may use a browser to access the Monit program.</p>
<h2>WHAT TO MONITOR?</h2>
<p> You can use Monit to monitor daemon <code>processes</code> or similar programs running on localhost. Monit is particularly useful for monitoring daemon processes, such as those started at system boot time. For instance sendmail, sshd, apache and mysql. In contrast to many other monitoring systems, Monit can act if an error situation should occur, e.g.; if sendmail is not running, monit can start sendmail again automatically or if apache is using too many resources (e.g. if a DoS attack is in progress) Monit can stop or restart apache and send you an alert message. Monit can also monitor process characteristics, such as how much memory or cpu cycles a process is using. </p>
<p> You can also use Monit to monitor <code>files</code>, <code>directories</code> and <code>filesystems</code> on localhost. Monit can monitor these items for changes, such as timestamps changes, checksum changes or size changes. This is also useful for security reasons &#8211; you can monitor the md5 or sha1 checksum of files that should not change and get an alert or perform an action if they should change. </p>
<p> Monit can monitor <code>network connections</code> to various servers, either on localhost or on remote hosts. <font SIZE="-1">TCP, UDP</font> and Unix Domain Sockets are supported. Network test can be performed on a protocol level; Monit has built-in tests for the main Internet protocols, such as <font SIZE="-1">HTTP, SMTP</font> etc. Even if a protocol is not supported you can still test the server because you can configure Monit to send any data and test the response from the server. </p>
<p> Monit can be used to test <code>programs</code> or scripts at certain times, much like cron, but in addition, you can test the exit value of a program and perform an action or send an alert if the exit value indicates an error. This means that you can use Monit to perform any type of check you can write a script for. </p>
<p> Finally, Monit can be used to monitor general <code>system</code> resources on localhost such as overall <font SIZE="-1">CPU</font> usage, Memory and System Load.</p>
<h2>GENERAL OPERATION</h2>
<p> The behavior of Monit is controlled by command-line options <i>and</i> a run control file, monitrc, the syntax of which we describe in a later section. Command-line options override <i>.monitrc</i> declarations. </p>
<p> The default location for <i>monitrc</i> is <i>~/.monitrc</i>. If this file does not exist, Monit will try <i>/etc/monitrc</i> and a few other places. See <font SIZE="-1">FILES</font> for details. You can also specify the control file directly by using the <i>-c</i> command-line switch to monit. For instance, </p>
<pre>
 $ monit -c /var/monit/monitrc
</pre>
<p> Before Monit is started the first time, you can test the control file for syntax errors: </p>
<pre>
 $ monit -t
 $ Control file syntax OK
</pre>
<p> If there was an error, Monit will print an error message to the console, including the line number in the control file from where the error was found. </p>
<p> Once you have a working Monit control file, simply start Monit from the console, like so: </p>
<pre>
 $ monit
</pre>
<p> You can change some configuration directives via command-line switches, but for simplicity it is recommended that you put these in the control file. </p>
<p> Monit will detach from the terminal and run as a background process, i.e. as a daemon process. As a daemon, Monit runs in cycles; It monitor services, then goes to sleep for a configured period, then wakes up and start monitoring again in an endless loop.</p>
<h3>Options</h3>
<p> The following options are recognized by Monit. However, it is recommended that you set options (when applicable) directly in the <i>.monitrc</i> control file. </p>
<p> <code>-c</code> <i>file</i><br />
Use this control file </p>
<p> <code>-d</code> <i>n</i><br />
Run Monit as a daemon once per&nbsp;<wbr><i>n</i>&nbsp;<wbr>seconds. Or use&nbsp;<wbr><i>&#8220;set<br />
daemon&#8221;</i>&nbsp;<wbr>in monitrc. </p>
<p> <code>-g</code> <i>name</i><br />
Set group name for start, stop, restart, monitor, unmonitor,<br />
status and summary action. </p>
<p> <code>-l</code> <i>logfile</i><br />
Print log information to this file. Or use&nbsp;<wbr><i>&#8220;set logfile&#8221;</i><br />
&nbsp;<wbr>in monitrc. </p>
<p> <code>-p</code> <i>pidfile</i><br />
Use this lock file in daemon mode. Or use&nbsp;<wbr><i>&#8220;set pidfile&#8221;</i><br />
&nbsp;<wbr>in monitrc. </p>
<p> <code>-s</code> <i>statefile</i><br />
Write state information to this file. Or use&nbsp;<wbr><i>&#8220;set<br />
statefile&#8221;</i>&nbsp;<wbr>in monitrc. </p>
<p> <code>-I</code><br />
Do not run in background&nbsp;<wbr>(needed for run from init) </p>
<p> <code>-i</code><br />
Print Monit&#8217;s unique&nbsp;<wbr><font SIZE="-1">ID</font> </p>
<p> <code>-r</code><br />
Reset Monit&#8217;s unique&nbsp;<wbr><font SIZE="-1">ID.</font>&nbsp;<wbr>Use with caution </p>
<p> <code>-t</code><br />
Run syntax check for the control file </p>
<p> <code>-v</code><br />
Verbose mode, work noisy&nbsp;<wbr>(diagnostic output) </p>
<p> <code>-vv</code><br />
Very verbose mode, same as -v plus log stack-trace on error </p>
<p> <code>-H</code> <i>[filename]</i><br />
Print&nbsp;<wbr><font SIZE="-1">MD5</font>&nbsp;<wbr>and&nbsp;<wbr><font SIZE="-1">SHA1</font>&nbsp;<wbr>hashes of the file or of stdin if the<br />
filename is omitted;&nbsp;<wbr>Monit will exit afterwards </p>
<p> <code>-V</code><br />
Print version number and patch level </p>
<p> <code>-h</code><br />
Print a help text</p>
<h3>Arguments</h3>
<p> Once you have Monit running as a daemon process, you can call Monit with one of the following arguments. Monit will then connect to the Monit daemon (on <font SIZE="-1">TCP</font> port 127.0.0.1:2812 by default) and ask the Monit daemon to perform the requested action. In other words; calling monit without arguments starts the Monit daemon, and calling monit <i>with</i> arguments enables you to communicate with the Monit daemon process.</p>
<dl>
<dt>start all</p>
<dd> Start all services listed in the control file and enable monitoring for them. If the group option is set (<i>-g</i>), only start and enable monitoring of services in the named group (&#8220;all&#8221; is not required in this case).</p>
<dt>start name</p>
<dd> Start the named service and enable monitoring for it. The name is a service entry name from the monitrc file.</p>
<dt>stop all</p>
<dd> Stop all services listed in the control file and disable their monitoring. If the group option is set, only stop and disable monitoring of the services in the named group (all&quot; is not required in this case).</p>
<dt>stop name</p>
<dd> Stop the named service and disable its monitoring. The name is a service entry name from the monitrc file.</p>
<dt>restart all</p>
<dd> Stop and start <i>all</i> services. If the group option is set, only restart the services in the named group (&#8220;all&#8221; is not required in this case).</p>
<dt>restart name</p>
<dd> Restart the named service. The name is a service entry name from the monitrc file.</p>
<dt>monitor all</p>
<dd> Enable monitoring of all services listed in the control file. If the group option is set, only start monitoring of services in the named group (&#8220;all&#8221; is not required in this case).</p>
<dt>monitor name</p>
<dd> Enable monitoring of the named service. The name is a service entry name from the monitrc file. Monit will also enable monitoring of all services this service depends on.</p>
<dt>unmonitor all</p>
<dd> Disable monitoring of all services listed in the control file. If the group option is set, only disable monitoring of services in the named group (&#8220;all&#8221; is not required in this case).</p>
<dt>unmonitor name</p>
<dd> Disable monitoring of the named service. The name is a service entry name from the monitrc file. Monit will also disable monitoring of all services that depends on this service.</p>
<dt>status [name]</p>
<dd> Print service status information.</p>
<dt>summary [name]</p>
<dd> Print a short status summary.</p>
<dt>reload</p>
<dd> Reinitialize a running Monit daemon, the daemon will reread its configuration, close and reopen log files.</p>
<dt>quit</p>
<dd> Kill the Monit daemon process</p>
<dt>validate</p>
<dd> Check all services listed in the control file. This action is also the default behavior when Monit runs in daemon mode.</p>
<dt>procmatch regex</p>
<dd> Allows for easy testing of pattern for process match check. The command takes regular expression as an argument and displays all running processes matching the pattern.</dl>
<h2>THE MONIT CONTROL FILE</h2>
<p> Monit is configured and controlled via a control file called <i>monitrc</i>. The default location for this file is ~/.monitrc. If this file does not exist, Monit will try /etc/monitrc, then <tt>@sysconfdir</tt>@/monitrc and finally ./monitrc. If you build Monit from source, the value of <tt>@sysconfdir</tt>@ can be given at configure time as ./configure &#8211;sysconfdir. For instance, using <i>./configure &#8211;sysconfdir /var/monit/etc</i> will make Monit search for <i>monitrc</i> in <i>/var/monit/etc</i> </p>
<p> To protect the security of your control file and passwords the control file must have read-write permissions <i>no more than 0700</i> (u=xrw,g=,o=); Monit will complain and exit otherwise. </p>
<p> When there is a conflict between the command-line arguments and the arguments in this file, the command-line arguments takes precedence. </p>
<p> Monit uses its own Domain Specific Language (<font SIZE="-1">DSL</font>); The control file consists of a series of service entries and global option statements. </p>
<p> Comments begin with a <tt>'#'</tt> and extend through the end of the line. Otherwise the file consists of a series of service entries or global option statements in a free-format, token-oriented syntax. </p>
<p> You can use noise keywords like <tt>'if'</tt>, <tt>'and'</tt>, <tt>'with(in)'</tt>, <tt>'has'</tt>, <tt>'us(ing|e)'</tt>, <tt>'on(ly)'</tt>, <tt>'then'</tt>, <tt>'for'</tt>, <tt>'of'</tt> anywhere in an entry to make it resemble English. They&#8217;re ignored, but can make entries much easier to read at a glance. Keywords are case insensitive. </p>
<p> There are three kinds of tokens: <i>grammar</i>, <i>numbers</i> (i.e. decimal digit sequences) and <i>strings</i>. Strings can be either quoted or unquoted. A quoted string is bounded by double quotes and may contain whitespace (and quoted digits are treated as a string). An unquoted string is any whitespace-delimited token, containing characters and/or numbers. </p>
<p> On a semantic level, the control file consists of three types of entries:</p>
<dl>
<dt>1. Global set-statements</p>
<dd> A global set-statement starts with the keyword <tt>&quot;set&quot;</tt> and the item to configure.</p>
<dt>2. Global include-statement</p>
<dd> The include statement consists of the keyword <tt>&quot;include&quot;</tt> and a glob string. This statement is used to include configure directives from separate files.</p>
<dt>3. One or more service entry statements.</p>
<dd> Each service entry consists of the keywords <tt>&quot;check&quot;</tt>, followed by the service type. Each entry requires a <code>unique</code> descriptive name, which may be freely chosen. This name is used by Monit to refer to the service internally and in all interactions with the user.</dl>
<p> Currently, nine types of check statements are supported:</p>
<dl>
<dt>1. <font SIZE="-1">CHECK PROCESS</font> &lt;unique name&gt; &lt;<font SIZE="-1">PIDFILE</font> &lt;path&gt; | <font SIZE="-1">MATCHING</font> &lt;regex&gt;&gt;</p>
<dd> &lt;path&gt; is the absolute path to the program&#8217;s pid-file. A pid-file is a file, containing a Process&#8217;s unique <font SIZE="-1">ID.</font> If the pid-file does not exist or does not contain the <font SIZE="-1">PID</font> number of a running process, Monit will call the entry&#8217;s start method if defined. </p>
<p> &lt;regex&gt; is an alternative to using <font SIZE="-1">PID</font> files and uses process name pattern matching to find the process to monitor. The first match is used so this form of check is most useful if the process name is unique. Pid-file should be used where possible as it defines expected pid exactly (pattern matching won&#8217;t be useful for processes which start a child process using fork/clone as the child will match the same pattern temporarily). You can test if a process match a pattern from the command-line using <tt>&quot;monit procmatch &quot;regex-pattern&quot;&quot;</tt>. This will lists all processes matching or not, the regex-pattern.</p>
<dt>2. <font SIZE="-1">CHECK FILE</font> &lt;unique name&gt; <font SIZE="-1">PATH</font> &lt;path&gt;</p>
<dd> &lt;path&gt; is the absolute path to the file. If the file does not exist, Monit will call the entry&#8217;s start method if defined, if &lt;path&gt; does not point to a regular file type (for instance a directory), Monit will disable monitoring of this entry. If Monit runs in passive mode or the start methods is not defined, Monit will just send an alert on error.</p>
<dt>3. <font SIZE="-1">CHECK FIFO</font> &lt;unique name&gt; <font SIZE="-1">PATH</font> &lt;path&gt;</p>
<dd> &lt;path&gt; is the absolute path to the fifo. If the fifo does not exist, Monit will call the entry&#8217;s start method if defined, if &lt;path&gt; does not point to a fifo type (for instance a directory), Monit will disable monitoring of this entry. If Monit runs in passive mode or the start methods is not defined, Monit will just send an alert on error.</p>
<dt>4. <font SIZE="-1">CHECK FILESYSTEM</font> &lt;unique name&gt; <font SIZE="-1">PATH</font> &lt;path&gt;</p>
<dd> &lt;path&gt; is the path to the device/disk, mount point, file or a directory which is part of a filesystem. It is recommended to use a block special file directly (for example /dev/hda1 on Linux or /dev/dsk/c0t0d0s1 on Solaris, etc.) If you use a mount point (for example /data), note if the filesystem is unmounted the test will still be true because the mount point exist. </p>
<p> If the filesystem becomes unavailable, Monit will call the entry&#8217;s start method if defined. if &lt;path&gt; does not point to a filesystem, Monit will disable monitoring of this entry. If Monit runs in passive mode or the start methods is not defined, Monit will just send an alert on error.</p>
<dt>5. <font SIZE="-1">CHECK DIRECTORY</font> &lt;unique name&gt; <font SIZE="-1">PATH</font> &lt;path&gt;</p>
<dd> &lt;path&gt; is the absolute path to the directory. If the directory does not exist, Monit will call the entry&#8217;s start method if defined. If &lt;path&gt; does not point to a directory, monit will disable monitoring of this entry. If Monit runs in passive mode or the start methods is not defined, Monit will just send an alert on error.</p>
<dt>6. <font SIZE="-1">CHECK HOST</font> &lt;unique name&gt; <font SIZE="-1">ADDRESS</font> &lt;host address&gt;</p>
<dd> The host address can be specified as a hostname string or as an IP-address string on a dotted decimal format. Such as, tildeslash.com or &#8220;64.87.72.95&#8221;.</p>
<dt>7. <font SIZE="-1">CHECK SYSTEM</font> &lt;unique name&gt;</p>
<dd> The <i>unique name</i> is usually the local host name, but any descriptive name can be used. If you use the variable <tt>$HOST</tt> as the name, it will expand to the hostname. This check allows one to monitor general system resources such as <font SIZE="-1">CPU</font> usage, total memory usage or load average. The <i>unique name</i> is used as the system hostname in mail alerts and as the initial name of the host entry in M/Monit.</p>
<dt>8. <font SIZE="-1">CHECK PROGRAM</font> &lt;unique name&gt; <font SIZE="-1">PATH</font> &lt;executable file&gt; [<font SIZE="-1">TIMEOUT</font> &lt;number&gt; <font SIZE="-1">SECONDS</font>]</p>
<dd> &lt;path&gt; is the absolute path to the executable program or script. The status test allows one to check the program&#8217;s exit status. If the program does not finish executing within &lt;number&gt; seconds, Monit will terminate it. The default program timeout is 300 seconds (5 minutes). The output of the program is recorded and made available in the User Interface and in alerts (up to 1kB).</p>
<dt>9. <font SIZE="-1">CHECK NETWORK</font> &lt;unique name&gt; &lt;<font SIZE="-1">ADDRESS</font> &lt;ipaddress&gt; | <font SIZE="-1">INTERFACE</font> &lt;name&gt;&gt;</p>
<dd> &lt;ipaddress&gt; is the IPv4 or IPv6 address of the monitored network interface. It is also possible to use interface name, such as &#8220;eth0&#8221; on Linux.</dl>
<h2>LOGGING</h2>
<p> Monit will log status and error messages to a log file. Use the <i>set logfile</i> statement in the monitrc control file. To setup Monit to log to its own logfile, use e.g. <i>set logfile /var/log/monit.log</i>. If <code>syslog</code> is given as a value for the <tt>&quot;-l&quot;</tt> command-line switch (or the keyword <i>set logfile syslog</i> is found in the control file) Monit will use the <code>syslog</code> system daemon to log messages with a priority assigned to each message based on the context. To turn off logging, simply do not set the logfile in the control file (and of course, do not use the -l switch) </p>
<p> The format for logfile is: </p>
<pre>
    [date] priority : message
</pre>
<p> for example: </p>
<pre>
    [CET Jan  5 18:49:29] info : 'mymachine' Monit started
</pre>
<h2>DAEMON MODE</h2>
<p> Use </p>
<pre>
 set daemon n (where n is a number in seconds)
</pre>
<p> to specify Monit&#8217;s poll cycle length and run Monit in daemon mode. You must specify a numeric argument which is a polling interval in seconds. In daemon mode, Monit detaches from the console, puts itself in the background and runs continuously, monitoring each specified service and then goes to sleep for the given poll interval, wakes up and start monitoring again in an endless cycle. </p>
<p> Alternatively, you can use the <tt>&quot;-d&quot;</tt> command line switch to set the poll interval, but it is strongly recommended to set the poll interval in your <i>~/.monitrc</i> file, by using <i>set daemon</i>. </p>
<p> Monit will then always start in daemon mode. If you do not use this statement and do not start monit with the -d option, Monit will just run through the service checks once and then exit. This might be useful in some situations, but Monit is primarily designed to run as a daemon process. </p>
<p> Calling <tt>&quot;monit&quot;</tt> with a Monit daemon running in the background sends a wake-up signal to the daemon, forcing it to check services immediately. Calling <tt>&quot;monit&quot;</tt> with the quit argument will kill a running Monit daemon process instead of waking it up.</p>
<h2>INIT SUPPORT</h2>
<p> The <tt>&quot;set init&quot;</tt> statement prevents Monit from transforming itself into a daemon process. Instead Monit will run as a foreground process. (You should still use <tt>&quot;set daemon&quot;</tt> to specify the poll cycle). </p>
<p> This is required to run Monit from init. Using init to start Monit is probably the best way to run Monit if you want to be certain that you always have a running Monit daemon on your system. Another option is to run Monit from crontab. In any case, you should make sure that the control file does not have any syntax errors before you start Monit from init or crontab (use <tt>&quot;monit -t&quot;</tt> to check). </p>
<p> To setup Monit to run from init, you can either use the <tt>&quot;set init&quot;</tt> statement in Monit&#8217;s control file or use the <tt>&quot;-I&quot;</tt> option from the command line. Here is what you must add to <tt>&quot;/etc/inittab&quot;</tt>: </p>
<pre>
  # Run Monit in standard run-levels
  mo:2345:respawn:/usr/local/bin/monit -Ic /etc/monitrc
</pre>
<p> After you have modified init&#8217;s configuration file, you can run the following command to re-examine /etc/inittab and start Monit: </p>
<pre>
  telinit q
</pre>
<p> For systems without telinit: </p>
<pre>
  kill -1 1
</pre>
<p> If Monit is used to monitor services that are also started at boot time (e.g. services started via <font SIZE="-1">SYSV</font> init rc scripts or via inittab) then, in some cases, a race condition could occur. That is; if a service is slow to start, Monit can assume that the service is not running and possibly try to start it and raise an alert, while, in fact the service is already about to start or already in its startup sequence. Please see the <font SIZE="-1">FAQ</font> for a solution to this problem. The short version is to start Monit on a higher run-level after system processes.</p>
<h2>INCLUDE FILES</h2>
<p> The Monit control file, <tt>&quot;monitrc&quot;</tt>, can include additional configuration files. This feature helps one to organize configuration into separate files instead of having everything in one file, if you like this kind of thing. Include statements can be placed at virtually any place in <tt>&quot;monitrc&quot;</tt> though the convention is at the bottom. The syntax is the following: </p>
<pre>
  include globstring
</pre>
<p> The globstring is any kind of string as defined in <tt><a href="/docs/linux/man/7-glob/">glob</a>(7)</tt>. Thus, you can refer to a single file or you can load several files at once. If you want to use whitespace in your string the globstring needs to be embedded into quotes (&#8216;) or double quotes (&quot;). If the globstring matches a directory instead of a file, it is silently ignored. </p>
<p> Any <i>include</i> statements in an included file are parsed as in the main control file. </p>
<p> If the globstring matches several results, the files are included in a non sorted manner. If you need to rely on a certain order, you should avoid wild-card globbing and instead specify the full path of files included. </p>
<p> An example, </p>
<pre>
 include /etc/monit.d/*.cfg
</pre>
<p> This will load any file matching the globstring. That is, all files in <i>/etc/monit.d</i> that ends with the prefix <i>.cfg</i>.</p>
<h2>MONIT HTTPD</h2>
<p> If specified in the control file, Monit will start with http support. You can then use Monit <font SIZE="-1">CLI</font> to start and stop services, disable or enable service monitoring as well as view the status of each service. </p>
<p> If http support is enabled over <font SIZE="-1">TCP</font> rather than over a Unix Socket, you can also view Monit&#8217;s informative dashboard in your web browser. </p>
<p> Note that if <font SIZE="-1">HTTP</font> support is disabled, the Monit <font SIZE="-1">CLI</font> interface will have reduced functionality, as most <font SIZE="-1">CLI</font> commands (such as &#8220;monit status&#8221;) need to communicate with the Monit background process via the the <font SIZE="-1">HTTP</font> interface. We strongly recommend having <font SIZE="-1">HTTP</font> support enabled. If security is a concern, bind the <font SIZE="-1">HTTP</font> interface to local host only or use Unix Socket so Monit is not accessible from the outside. </p>
<p> Syntax for <font SIZE="-1">TCP</font> port: </p>
<pre><code>
SET HTTPD PORT&lt;number&gt;[ADDRESS&lt;hostname | IP - address&gt;]
                      [SSL&lt;ENABLE | DISABLE&gt;]
                      [PEMFILE&lt;path&gt;]
                      [CLIENTPEMFILE&lt;path&gt;]
                      [ALLOWSELFCERTIFICATION]
                      [SIGNATURE&lt;ENABLE | DISABLE&gt;] ALLOW&lt;user : password | IP - address | IP - range&gt; +
</code></pre>
<p> Example: </p>
<pre>
 set httpd port 2812
     allow username:password
</pre>
<p> You can now use &lt;<a rel="nofollow" href="http://localhost:2812/">http://localhost:2812/</a>&gt; to access Monit&#8217;s web interface from a browser, after you have entered username and password as credentials. </p>
<p> Syntax for Unix Socket: </p>
<pre>
  SET HTTPD UNIXSOCKET &lt;path&gt;
      ALLOW &lt;user:password&gt;+
</pre>
<p> Example: </p>
<pre>
 set httpd unixsocket /var/run/monit.sock
     allow username:password
</pre>
<p> <code>Options</code>: </p>
<p> <font SIZE="-1"><code>UNIXSOCKET</code></font> set the path to the Unix Socket Monit should bind to and listen on. </p>
<p> <font SIZE="-1"><code>PORT</code></font> set the port Monit should bind to and listen on. Monit is usually setup on port 2812. </p>
<p> <font SIZE="-1"><code>ADDRESS</code></font> make Monit listen on a specific interface only. For example if you <i>don&#8217;t</i> want to expose Monit&#8217;s web interface to the network, bind it to localhost only. Monit will accept connections on any address by default (if <font SIZE="-1">ADDRESS</font> option is missing). </p>
<p> For example to limit the web interface to localhost only: </p>
<pre>
 set httpd
     port 2812
     use address 127.0.0.1
     allow username:password
</pre>
<p> <font SIZE="-1"><code>SSL</code></font> enable <font SIZE="-1">TLS</font> for Monit&#8217;s web interface. The <i></i><font SIZE="-1"><i>PEMFILE</i></font><i></i> option holds both the server&#8217;s private key and certificate. This file should be stored in a safe place on the filesystem and should have strict permissions, no more than 0700. </p>
<p> For example: </p>
<pre>
 set httpd
     port 2812
     ssl enable
     pemfile /etc/certs/monit.pem
     allow myuser:mypassword
</pre>
<p> You can now use &lt;<a rel="nofollow" href="https://localhost:2812/">https://localhost:2812/</a>&gt; to access the Monit web server over a <font SIZE="-1">TLS</font> encrypted connection. </p>
<p> OpenSSL <font SIZE="-1">FIPS</font> is supported. To enable <font SIZE="-1">FIPS</font> mode (provided your OpenSSL library supports it), add this statement to Monit control file: </p>
<pre>
 SET FIPS
</pre>
<p> <font SIZE="-1"><code>CLIENTPEMFILE</code></font> client certificate based authentication. A connecting client has to provide a certificate known to Monit in order to connect. This file also needs to have all necessary <font SIZE="-1">CA</font> certificates. By default self-signed client certificates are <code>not</code> allowed. If you want to use a self signed certificate from a client it has to be allowed explicitly with the <font SIZE="-1"><code>ALLOWSELFCERTIFICATION</code></font> statement. </p>
<p> For example: </p>
<pre>
 set httpd
     port 2812
     ssl enable
     pemfile /etc/certs/monit.pem
     clientpemfile /etc/certs/monit-client.pem
</pre>
<p> <font SIZE="-1"><code>SIGNATURE</code></font> can be used to hide Monit version from the <font SIZE="-1">HTTP</font> response header and error pages. For example: </p>
<pre>
  set httpd
    port 2812
    signature disable
    allow myuser:mypassword
</pre>
<h3>Authentication</h3>
<p> Access to the Monit web interface is controlled primarily via the <font SIZE="-1"><code>ALLOW</code></font> option which is used to specify authentication and authorize only specific clients to connect. </p>
<p> If the Monit command line interface is being used, at least one cleartext password is necessary (see bellow), otherwise the Monit command line interface will not be able to connect to the Monit web interface. </p>
<p> Clients trying to connect to Monit, but submit a wrong username and/or password are logged with their IP-address. </p>
<p> <i>Client certificates</i> </p>
<p> This authentication method is a strong authentication mechanism and employ <font SIZE="-1">HTTPS</font> client certificates to verify the authenticity of a connecting client. Clients must posses a Public Key Certificate known by Monit. The client must connect to Monit over <font SIZE="-1">SSL</font> and Monit ask the client to send its certificate. Upon receiving the certificate Monit compares the certificate to certificates located in the <i></i><font SIZE="-1"><i>CLIENTPEMFILE</i></font><i></i> file. Access is granted if the client certificate is in this file. See <i></i><font SIZE="-1"><i>CLIENTPEMFILE</i></font><i></i> above for details. </p>
<p> <i>Host and network allow list</i> </p>
<p> Monit maintains an access-control list of hosts and networks allowed to connect. You can add as many hosts as you want to, but only hosts with a valid domain name or its <font SIZE="-1">IP</font> address are allowed. </p>
<p> Monit will query a name server to check any hosts trying to connect. If a host (client) is trying to connect, but cannot be found in the access list or cannot be resolved, Monit will shutdown the connection to the client promptly. </p>
<p> Control file example: </p>
<pre>
  set httpd port 2812
      allow localhost
      allow my.other.work.machine.com
      allow 10.1.1.1
      allow 192.168.1.0/255.255.255.0
      allow 10.0.0.0/8
</pre>
<p> Clients, not mentioned in the allow list, trying to connect to Monit will be denied access and are logged with their IP-address. </p>
<p> <i>Basic Authentication</i> </p>
<p> Monit supports Basic Authentication as described in <font SIZE="-1">RFC 2617.</font> </p>
<p> In short; a server challenge a client (e.g. a Browser) to send authentication information (username and password) and if accepted, the server will allow the client access to the requested document. </p>
<p> The biggest weakness with Basic Authentication is that username and password is sent in clear-text over the network (i.e. base64 encoded). It is therefor recommended that you do not use this authentication method unless you run Monit with <i>ssl</i> support. With ssl, it is safe to use Basic Authentication since <i>all</i> http data, including Basic Authentication headers will be encrypted. </p>
<p> Cleartext user and password </p>
<p> Monit will use Basic Authentication if an allow statement contains a username and a password separated with a single &#8216;:&#8217; character. Special characters can be used, but for non-alphanumerics the password has to be quoted. </p>
<p> Syntax: </p>
<pre>
 ALLOW &lt;username&gt;:&lt;password&gt;
</pre>
<p> <font SIZE="-1">PAM</font> </p>
<p> <font SIZE="-1">PAM</font> is supported on platforms which provide <font SIZE="-1">PAM </font>(such as Linux, Mac <font SIZE="-1">OS X,</font> FreeBSD, NetBSD). </p>
<p> Syntax: </p>
<pre>
 ALLOW @&lt;group&gt;
</pre>
<p> where <tt>&quot;group&quot;</tt> is the group name allowed to access Monit&#8217;s web interface. Monit uses a <font SIZE="-1">PAM</font> service called <i>monit</i> for <font SIZE="-1">PAM</font> authentication, see the <font SIZE="-1">PAM</font> manual page for detailed instructions on how to set the <font SIZE="-1">PAM</font> service and <font SIZE="-1">PAM</font> authentication plugins. </p>
<p> Sample <font SIZE="-1">PAM</font> service for Monit on Mac <font SIZE="-1">OS X </font>(store as &#8220;/etc/pam.d/monit&#8221; file): </p>
<pre>
  # monit: auth account password session
  auth       sufficient     pam_securityserver.so
  auth       sufficient     pam_unix.so
  auth       required       pam_deny.so
  account    required       pam_permit.so
</pre>
<p> And monitrc config which only allows group <tt>&quot;admin&quot;</tt> authenticated via <font SIZE="-1">PAM</font> to access the web interface: </p>
<pre>
  set httpd
      port 2812
      allow @admin
</pre>
<p> htpasswd file </p>
<p> Alternatively you can use files in <tt>&quot;htpasswd&quot;</tt> format (one <i>user:passwd</i> entry per line), like so: <i>allow [cleartext|crypt|md5] /path [users]</i>. By default cleartext passwords are read. In case the passwords are digested it is necessary to specify the cryptographic method. If you do not want all users in the password file to have access to Monit you can specify only those users that should have access, in the allow statement. Otherwise all users are added. </p>
<p> Example1: </p>
<pre>
  set httpd port 2812
      allow hauk:password
      allow md5 /etc/httpd/htpasswd john paul ringo george
</pre>
<p> If you use this method together with a host list, then only clients from the listed hosts will be allowed to connect to the Monit http server and each client will be asked to provide a username and a password. </p>
<p> Example2: </p>
<pre>
  set httpd port 2812
      allow localhost
      allow 10.1.1.1
      allow hauk:&quot;passw@rd&quot;
</pre>
<p> If you only want to use Basic Authentication, then just provide allow entries with username and password or password files as in example 1 above. </p>
<p> Read-only users </p>
<p> Finally it is possible to define some users as read-only. A read-only user can read the Monit web pages but will <i>not</i> get access to push-buttons and cannot change a service from the web interface. </p>
<pre>
  set httpd port 2812
      allow admin:password
      allow hauk:password read-only
      allow @admins
      allow @users read-only
</pre>
<p> A user is set to read-only by using the <i>read-only</i> keyword <code>after</code> username:password. In the above example the user <i>hauk</i> is defined as a read-only user, while the <i>admin</i> user has all access rights.</p>
<h2>ALERT MESSAGES</h2>
<p> Monit will raise an alert in the following situations: </p>
<pre>
 o A service does not exist (e.g. process is not running)
 o Cannot read service data (e.g. cannot get filesystem usage)
 o Execution of a service related script failed (e.g. start failed)
 o Invalid service type (e.g. if path points to directory instead of file)
 o Custom test script returned error
 o Ping test failed
 o TCP/UDP connection and/or port test failed
 o Resource usage test failed (e.g. cpu usage too high)
 o Checksum mismatch or change (e.g. file changed)
 o File size test failed (e.g. file too large)
 o Timestamp test failed (e.g. file is older then expected)
 o Permission test failed (e.g. file mode doesn't match)
 o An UID test failed (e.g. file owned by different user)
 o A GID test failed (e.g. file owned by different group)
 o A process' PID changed out of Monit's control
 o A process' PPID changed out of Monit control
 o Too many service recovery attempts failed
 o A file content test found a match
 o Filesystem flags changed
 o A service action was performed by administrator
 o A network link failed
 o A network link capacity changed
 o A network link saturation failed
 o A network link upload/download rate failed
 o Monit was started, stopped or reloaded
</pre>
<p> To get an alert via e-mail, set the alert target using the global <tt>&quot;set alert&quot;</tt> statement (for all services) or the <tt>&quot;alert&quot;</tt> statement in the context of a service entry (for a single service).</p>
<h3>Setting an alert recipient</h3>
<p> If an event occurs, Monit will send an alert. There are two kinds of alert statement: global and local. </p>
<p> Global syntax: </p>
<p>SET ALERT mail &#8211; address [[NOT]{event, &#8230;}][REMINDER cycles]</p>
<p> Example: </p>
<pre>
 set alert foo@bar
</pre>
<p> will send a default email to the address foo@bar whenever any event occurs on any service. </p>
<p> If you want to send alert messages to more email addresses, add a <tt>&quot;set alert 'email'&quot;</tt> statement for each address. </p>
<p> It is also possible to use the local alert statement in the context of a service check to enable alert for the given service only: </p>
<p>ALERT mail &#8211; address [[NOT]{event, &#8230;}][REMINDER cycles]</p>
<p> Local alert example: </p>
<pre>
 check host myhost with address 1.2.3.4
     if failed port 3306 protocol mysql then alert
     if failed port 80 protocol http then alert
     alert foo@baz # Local service alert
</pre>
<p> You can combine global and local alert statements. If there is a conflict, the local alert has precedence and overrides the global statement. </p>
<p> <i>Setting an event filter</i> </p>
<p> If you only want an alert message sent for certain events, list them in an <tt>&quot;{event, ...}&quot;</tt> block, e.g.: </p>
<pre>
 set alert foo@bar only on { timeout, nonexist }
</pre>
<p> The event list can also be negated to send alerts for all events <i>except</i> those which are listed, by prepending the list with the word <tt>&quot;not&quot;</tt>. For example, to receive all alerts except notification about Monit program start and stop: </p>
<pre>
 set alert foo@bar but not on { instance }
</pre>
<p> Here is a list of all possible event types emitted by Monit. Values from the first column can be used in the event filter list mentioned above: </p>
<p>Event : | Failure state : | Success state : &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -action | &#8220;Action done&#8221; | &#8220;Action done&#8221; checksum | &#8220;Checksum failed&#8221; | &#8220;Checksum succeeded&#8221; bytein | &#8220;Download bytes exceeded&#8221; | &#8220;Download bytes ok&#8221; byteout | &#8220;Upload bytes exceeded&#8221; | &#8220;Upload bytes ok&#8221; connection | &#8220;Connection failed&#8221; | &#8220;Connection succeeded&#8221; content | &#8220;Content failed&#8221;, | &#8220;Content succeeded&#8221; data | &#8220;Data access error&#8221; | &#8220;Data access succeeded&#8221; exec | &#8220;Execution failed&#8221; | &#8220;Execution succeeded&#8221; fsflags | &#8220;Filesystem flags failed&#8221; | &#8220;Filesystem flags succeeded&#8221; gid | &#8220;GID failed&#8221; | &#8220;GID succeeded&#8221; icmp | &#8220;Ping failed&#8221; | &#8220;Ping succeeded&#8221; instance | &#8220;Monit instance changed&#8221; | &#8220;Monit instance changed not&#8221; invalid | &#8220;Invalid type&#8221; | &#8220;Type succeeded&#8221; link | &#8220;Link down&#8221; | &#8220;Link up&#8221; nonexist | &#8220;Does not exist&#8221; | &#8220;Exists&#8221; packetin | &#8220;Download packets exceeded&#8221; | &#8220;Download packets ok&#8221; packetout | &#8220;Upload packets exceeded&#8221; | &#8220;Upload packets ok&#8221; permission | &#8220;Permission failed&#8221; | &#8220;Permission succeeded&#8221; pid | &#8220;PID failed&#8221; | &#8220;PID succeeded&#8221; ppid | &#8220;PPID failed&#8221; | &#8220;PPID succeeded&#8221; resource | &#8220;Resource limit matched&#8221; | &#8220;Resource limit succeeded&#8221; saturation | &#8220;Saturation exceeded&#8221; | &#8220;Saturation ok&#8221; size | &#8220;Size failed&#8221; | &#8220;Size succeeded&#8221; speed | &#8220;Speed failed&#8221; | &#8220;Speed ok&#8221; status | &#8220;Status failed&#8221; | &#8220;Status succeeded&#8221; timeout | &#8220;Timeout&#8221; | &#8220;Timeout recovery&#8221; timestamp | &#8220;Timestamp failed&#8221; | &#8220;Timestamp succeeded&#8221; uid | &#8220;UID failed&#8221; | &#8220;UID succeeded&#8221; uptime | &#8220;Uptime failed&#8221; | &#8220;Uptime succeeded&#8221;</p>
<p> Each alert recipient can have it&#8217;s own filter, for example: </p>
<p>set alert foo @bar{nonexist, timeout, resource, icmp, connection} set alert security @bar on{checksum, permission, uid, gid} set alert admin @bar</p>
<p> <i>Setting an error reminder</i> </p>
<p> Monit by default sends just <i>one</i> notification if a service failed and another when/if it recover. If you want to be notified that the service is still in a failed state, you can use the reminder option in the alert statement: </p>
<p>SET ALERT mail &#8211; address[WITH] REMINDER[ON] number[CYCLES]</p>
<p> For example if you want to be notified each tenth cycle if a service remains in a failed state, you can use: </p>
<pre>
 alert foo@bar with reminder on 10 cycles
</pre>
<p> Likewise if you want to be notified on each failed cycle, you can use: </p>
<pre>
  alert foo@bar with reminder on 1 cycle
</pre>
<h3>Disabling alerts for some service</h3>
<p> To suppress alerts for some user and service, add the <tt>&quot;noalert&quot;</tt> statement in the context of a service check. </p>
<pre>
 NOALERT mail-address
</pre>
<p> Example (send all alerts to foo@bar except for service p3): </p>
<pre>
 set alert foo@bar
 check process p1 with pidfile /var/run/p1.pid
 check process p2 with pidfile /var/run/p2.pid
 check process p3 with pidfile /var/run/p3.pid
     noalert foo@bar
</pre>
<h3>Message format</h3>
<p> The alert message format can be modified by using the <tt>&quot;set mail-format&quot;</tt> statement: </p>
<pre>
 SET MAIL-FORMAT {mail-format}
</pre>
<p> Example: </p>
<p>set mail &#8211; format<br />
{<br />
from:<br />
    monit[at] foo.bar<br />
            reply &#8211;<br />
        to : support[at] domain.com<br />
                 subject : $SERVICE $EVENT at $DATE<br />
                               message : Monit $ACTION $SERVICE at $DATE on $HOST : $DESCRIPTION.Yours sincerely,<br />
        monit<br />
}</p>
<p> The <i>from:</i> option is the sender&#8217;s email address. That is, the email address Monit will pretend it is sending alerts from. It does not have to be a real email-address only a proper formatted address. </p>
<p> The <i>reply-to:</i> option can be used to set the reply-to mail header. </p>
<p> The <i>subject:</i> option sets the message subject and must be on only <i>one</i> line. </p>
<p> The <i>message:</i> option sets the mail body. This option should always be the last in a mail-format statement. The mail body can be as long as needed, but must <i>not</i> contain the block-closing &#8216;}&#8217; character. </p>
<p> You need not use all options, only the option which you want to override. For example to globally change the senders address only: </p>
<p>set mail &#8211; format<br />
{<br />
from:<br />
    bofh[at] foo.bar<br />
}</p>
<p> The subject and body may contain <tt>$NAME</tt> variables, which are expanded by Monit. Here is a list of variables that can be used when composing an alert message.</p>
<dl>
<dt>&bull;</p>
<dd> <i></i>$EVENT<i></i> </p>
<p> A string describing the event that occurred.</p>
<dt>&bull;</p>
<dd> <i></i>$SERVICE<i></i> </p>
<p> The service name</p>
<dt>&bull;</p>
<dd> <i></i>$DATE<i></i> </p>
<p> The current time and date (<font SIZE="-1">RFC 822</font> date style).</p>
<dt>&bull;</p>
<dd> <i></i>$HOST<i></i> </p>
<p> The name of the host Monit is running on</p>
<dt>&bull;</p>
<dd> <i></i>$ACTION<i></i> </p>
<p> The name of the action which was done by Monit.</p>
<dt>&bull;</p>
<dd> <i></i>$DESCRIPTION<i></i> </p>
<p> The description of the error condition</dl>
<h3>Setting a mail server for alert delivery</h3>
<p> The mail server Monit should use to send alert messages is defined with a <tt>&quot;set mailserver&quot;</tt> statement: </p>
<p>SET MAILSERVER&lt;hostname | ip &#8211; address[PORT number][USERNAME string]<br />
                                      [PASSWORD string][using SSLAUTO | SSLV2 | SSLV3 | TLSV1 | TLSV11 | TLSV12]<br />
                                      [CERTMD5 checksum]&gt;,<br />
    &#8230;<br />
        [with TIMEOUT X SECONDS]<br />
        [using HOSTNAME hostname]</p>
<p> Multiple mail servers can be set by using a comma separated list. If Monit cannot connect to the first server, it will try the next in the list and so on. </p>
<p> The port statement allows to override the default <font SIZE="-1">SMTP</font> port (465 for <font SIZE="-1">SSL,</font> or 25 for <font SIZE="-1">TLS</font> and non secure connection). </p>
<p> Monit supports <font SIZE="-1">AUTH PLAIN</font> and <font SIZE="-1">AUTH LOGIN</font> for <font SIZE="-1">SMTP</font> authentication. You can set a username and a password using the <font SIZE="-1">USERNAME</font> and <font SIZE="-1">PASSWORD</font> options. </p>
<p> You can enable <font SIZE="-1">SSL</font> or <font SIZE="-1">TLS</font> with optional certificate checksum. </p>
<p> The default connection timeout is 5 seconds. You can rise this limit using the <font SIZE="-1">TIMEOUT</font> option. </p>
<p> Example (setting two mail servers for failover): </p>
<pre>
 set mailserver smtp.gmail.com, smtp.other.host
</pre>
<p> By default, Monit uses the local host name in <font SIZE="-1">SMTP HELO/EHLO</font> and in the Message-ID header. You can override this using the <font SIZE="-1">HOSTNAME</font> option.</p>
<h3>Event queue</h3>
<p> If no mail server is available, Monit <i>can</i> queue events in the local file-system for retry until the mail server recovers. </p>
<p> If Monit is used with M/Monit, the event queue provides a safe event store for M/Monit in the case of temporary problems. </p>
<p> The event queue is persistent across Monit restarts and provided that the back-end filesystem is persistent, across system restart as well. </p>
<p> By default, the queue is disabled and if the alert handler fails, Monit will simply drop the alert message. </p>
<p> To enable the event queue, add the following statement: </p>
<pre>
 SET EVENTQUEUE BASEDIR &lt;path&gt; [SLOTS &lt;number&gt;]
</pre>
<p> The &lt;path&gt; is the path to the directory where events will be stored. </p>
<p> Optionally if you want to limit the queue size, use the slots option to only store up to <i>number</i> event messages. </p>
<p> Example: </p>
<pre>
  set eventqueue basedir /var/monit slots 5000
</pre>
<p> If you are running more then one Monit instance on the same machine, you <code>must</code> use separated event queue directories.</p>
<h2>SERVICE METHODS</h2>
<p> Each service can have associated <i>start</i>, <i>stop</i> and <i>restart</i> methods which Monit can use to execute action on the service. </p>
<p> Syntax: </p>
<p> &lt;START | STOP | RESTART&gt; [PROGRAM] = &#8220;program&#8221;<br />
        [[AS] UID &lt;number | string&gt;]<br />
        [[AS] GID &lt;number | string&gt;]<br />
        [[WITH] TIMEOUT &lt;number&gt; SECOND(S)]</p>
<p> If the <tt>&quot;program&quot;</tt> is a shell script it must begin with <tt>&quot;#!&quot;</tt> and the remainder of the first line must specify an interpreter for the program. e.g. <tt>&quot;#!/bin/sh&quot;</tt> </p>
<p> The <tt>&quot;program&quot;</tt> must also be executable (for example mode 0755). </p>
<p> It&#8217;s possible to write scripts directly into the <i>program</i> this way: </p>
<pre>
 stop = &quot;/bin/bash -c 'kill -s SIGTERM `cat /var/run/process.pid`'&quot;
</pre>
<p> By default the program is executed as the user under which Monit is running. If Monit is running as root, you may optionally specify the <i></i><font SIZE="-1"><i>UID</i></font><i></i> and <i></i><font SIZE="-1"><i>GID</i></font><i></i> the executed program should switch to. </p>
<p> Example: </p>
<pre>
 check process mmonit with pidfile /usr/local/mmonit/mmonit/logs/mmonit.pid
   start program = &quot;/usr/local/mmonit/bin/mmonit&quot; as uid &quot;mmonit&quot; and gid &quot;mmonit&quot;
   stop program = &quot;/usr/local/mmonit/bin/mmonit stop&quot; as uid &quot;mmonit&quot; and gid &quot;mmonit&quot;
</pre>
<p> In the case of a process check, Monit will wait up to 30 seconds for the start/stop action to finish before giving up and report an error. You can override this timeout using the <i></i><font SIZE="-1"><i>TIMEOUT</i></font><i></i> option. </p>
<p> Example: </p>
<pre>
 check process foobar with pidfile /var/run/foobar.pid
   start program = &quot;/etc/init.d/foobar start&quot; with timeout 60 seconds
   stop program = &quot;/etc/init.d/foobar stop&quot;
</pre>
<h2>SERVICE POLL TIME</h2>
<p> Services are checked in regular intervals by the <tt>&quot;set daemon n&quot;</tt> statement. Checks are performed in the same order as they are written in the <tt>&quot;.monitrc&quot;</tt> file, except if dependencies are setup between services. </p>
<p> It is possible to modify a service check schedule by using the <tt>&quot;every&quot;</tt> statement. </p>
<p> There are three variants:</p>
<dl>
<dt>1. custom interval based on a poll cycle multiple</p>
<dd>
<pre>
 EVERY [number] CYCLES
</pre>
<dt>2. check is schedule based on a cron-style string</p>
<dd>
<pre>
 EVERY [cron]
</pre>
<dt>3. do-not-check schedule based on a cron-style string</p>
<dd>
<pre>
 NOT EVERY [cron]
</pre>
</dl>
<p> A cron-style string, consist of 5 fields separated with white-space. All fields are required: </p>
<p>Name : | Allowed values : | Special characters : &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -Minutes | 0 &#8211; 59 | *-,<br />
    Hours | 0 &#8211; 23 | *-,<br />
    Day of month | 1 &#8211; 31 | *-,<br />
    Month | 1 &#8211; 12(1 = jan, 12 = dec) | *-,<br />
    Day of week | 0 &#8211; 6(0 = sunday, 6 = saturday) | *-,</p>
<p> The special characters: </p>
<p> Character:   | Description:<br />
 &#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;<br />
 * (asterisk) | The asterisk indicates that the expression will<br />
              | match for all values of the field;<br />
 e.g., using | an asterisk in the 4th field(month) would | indicate every month.- (hyphen) | Hyphens are used to define ranges.For example,<br />
     | 8 &#8211; 9 in the hour field indicate between 8AM and<br />
         | 9AM. Note that range is from start time until and | including end time.That is,<br />
     from 8AM and until<br />
                      | 10AM unless minutes are set.Another example,<br />
     | 1 &#8211; 5 in the weekday field, specify from monday to | friday(including friday)., (comma) | Comma are used to specify a sequence.For example | 17, 18 in the day field indicate the 17th and 18th | day of the month.A sequence can also include | ranges.For example, using 1 &#8211; 5, 0 in the weekday | field indicate monday to friday and sunday.</p>
<p> Example 1: Check once per two cycles </p>
<pre>
 check process nginx with pidfile /var/run/nginx.pid
       every 2 cycles
</pre>
<p> Example 2: Check every workday 8AM-7PM </p>
<pre>
 check program checkOracleDatabase
        with path /var/monit/programs/checkoracle.pl
       every &quot;* 8-19 * * 1-5&quot;
</pre>
<p> Example 3: Do not run the check in the backup window on Sunday 0AM-3AM </p>
<pre>
 check process mysqld with pidfile /var/run/mysqld.pid
       not every &quot;* 0-3 * * 0&quot;
</pre>
<p> Limitations: </p>
<p> The current scheduler is poll cycle based. When a service check is constraint with the <i>every cron</i> statement, Monit will check whether the current time match the cron-string pattern. If it does, the check is performed, otherwise it is skipped. The cron specification thus does not guarantee when exactly the test will run, this depends on the default poll time and the length of the check cycle. In other words, we cannot guarantee that Monit will run on a specific time. Therefor we <code>strongly</code> recommend to use an asterix in the minute field or at minimum a range, e..g. 0-15. <code>Never</code> use a specific minute as Monit may not run on that minute. </p>
<p> We will address this limitation in a future release and convert the scheduler from serial polling into a parallel non-blocking scheduler where checks are guaranteed to run on time and with seconds resolution.</p>
<h2>SERVICE GROUPS</h2>
<p> Service entries in the control file, <i>monitrc</i>, can be grouped together by the <i>group</i> statement. The syntax is simply (keyword in capital): </p>
<pre>
  GROUP groupname
</pre>
<p> With this statement it is possible to group similar service entries together and manage them as a whole. Monit provides functions to start, stop, restart, monitor and unmonitor a group of services, like so: </p>
<p> To start a group of services from the console: </p>
<pre>
  monit -g &lt;groupname&gt; start
</pre>
<p> To stop a group of services: </p>
<pre>
  monit -g &lt;groupname&gt; stop
</pre>
<p> To restart a group of services: </p>
<pre>
  monit -g &lt;groupname&gt; restart
</pre>
<p> A service can be added to multiple groups by using more than one group statement: </p>
<pre>
  group www
  group filesystem
</pre>
<h2>SERVICE MONITORING MODE</h2>
<p> Monit supports three monitoring modes per service: <i>active</i>, <i>passive</i> and <i>manual</i>. </p>
<p> Syntax: </p>
<pre>
  MODE &lt;ACTIVE | PASSIVE | MANUAL&gt;
</pre>
<p> In <i>active</i> mode (the default), Monit will pro-actively monitor a service and in case of problems raise alerts and/or restart the service. </p>
<p> In <i>passive</i> mode, Monit will passively monitor a service and will raise alerts, but will <code>not</code> try to fix a problem by executing <i>start</i>, <i>stop</i> or <i>restart</i>. </p>
<p> In <i>manual</i> mode, Monit will enter <i>active</i> mode <i>only</i> if a service was started via Monit: </p>
<pre>
  monit start &lt;servicename&gt;
</pre>
<p> Use &#8220;monit stop &lt;servicename&gt;&#8221; to stop the service and take it out of Monit&#8217;s control. The manual mode can be used to build a simple cluster with active/passive HA-services. </p>
<p> A service&#8217;s monitoring state is persistent across Monit restart. </p>
<p> If you use Monit in a HA-cluster you should place the Monit state file in a temporary filesystem so if the machine which runs HA-services should crash and the stand-by machine take over its services, the HA-services won&#8217;t be started after the crashed node will boot again: </p>
<pre>
  set statefile /tmp/monit.state
</pre>
<h2>SERVICE RESTART LIMIT</h2>
<p> <code>Monit</code> provides a restart limit mechanism for situations where a service simply refuses to start or respond over a longer period. </p>
<p> The restart limit mechanism is based on number of service restarts and number of poll-cycles. For example, if a service had <i>x</i> restarts within <i>y</i> poll-cycles (where <i>x</i> &lt;= <i>y</i>) then Monit will perform an action (for example unmonitor the service). If a timeout occurs, Monit will send an alert message if you have register interest for this event. </p>
<p> The syntax for the timeout statement is as follows (keywords are in capital): </p>
<pre>
 IF &lt;number&gt; RESTART &lt;number&gt; CYCLE(S) THEN &lt;action&gt;
</pre>
<p> The <i>action</i> value is either one of common actions or <font SIZE="-1">TIMEOUT </font>(for backward compatibility, equals to <font SIZE="-1">UNMONITOR</font> action). </p>
<p> Here is an example where Monit will unmonitor the service if it was restarted 2 times within 3 cycles: </p>
<pre>
 if 2 restarts within 3 cycles then unmonitor
</pre>
<p> To have Monit check the service again after monitoring was disabled, run <tt>&quot;monit monitor servicename&quot;</tt> from the command line. </p>
<p> Example for setting custom exec on timeout: </p>
<pre>
 if 5 restarts within 5 cycles then exec &quot;/foo/bar&quot;
</pre>
<p> Example for stopping the service: </p>
<pre>
 if 7 restarts within 10 cycles then stop
</pre>
<h2>SERVICE DEPENDENCIES</h2>
<p> If specified in the control file, Monit can do dependency checking before start, stop, monitoring or unmonitoring of services. The dependency statement may be used within any service entries in the Monit control file. </p>
<p> The syntax for the depend statement is simply: </p>
<p>DEPENDS on service[, service[, &#8230;]]</p>
<p> Where <code>service</code> is a check service entry name used in your <tt>&quot;.monitrc&quot;</tt> file, for instance <code>apache</code> or <code>datafs</code>. </p>
<p> You may add more than one service name of any type or use more than one depend statement in an entry. </p>
<p> Services specified in a <i>depend</i> statement will be checked during stop/start/monitor/unmonitor operations. If a service is stopped or unmonitored it will stop/unmonitor any services that depends on itself. Likewise, if a service is started, it will first stop any services that depends on itself and after it is started, start all depending services again. If the service is to be monitored (enable monitoring), all services which this service depends on will be monitored before enabling monitoring of this service. </p>
<p> Here is an example where we set up an apache service entry to depend on the underlying apache binary. If the binary should change an alert is sent and apache is not monitored anymore. The rationale is security and that Monit should not execute a possibly cracked apache binary. </p>
<pre>
 (1) check process apache
 (2)    with pidfile &quot;/usr/local/apache/logs/httpd.pid&quot;
 (3)    ...
 (4)    depends on httpd
 (5)
 (6) check file httpd with path /usr/local/apache/bin/httpd
 (7)    if failed checksum then unmonitor
</pre>
<p> The first entry is the process entry for apache (abbreviated for clarity). The fourth line sets up a dependency between this entry and the service entry named httpd in line 6. A dependency tree works as follows, if an action is conducted in a lower branch it will propagate upward in the tree and for every dependent entry execute the same action. In this case, if the checksum should fail in line 7 then an unmonitor action is executed and the apache binary is not checked anymore. But since the apache process entry depends on the httpd entry this entry will also execute the unmonitor action. In short, if the checksum test for the httpd binary file should fail, both the check file httpd entry and the check process apache entry is set in un-monitoring mode. </p>
<p> A dependency tree is a general construct and can be used between all types of service entries and span many levels and propagate any supported action (except the exec action which will not propagate upward in a dependency tree for obvious reasons). </p>
<p> Here is another different example. Consider the following common server setup: </p>
<pre>
  WEB-SERVER -&gt; APPLICATION-SERVER -&gt; DATABASE -&gt; FILESYSTEM
      (a)               (b)             (c)          (d)
</pre>
<p> You can set dependencies so that the web-server depends on the application server to run before the web-server starts and the application server depends on the database server and the database depends on the file-system to be mounted before it starts. See also the example section below for examples using the depend statement. </p>
<p> Here we describe how Monit will function with the above dependencies:</p>
<dl>
<dt>If no servers are running</p>
<dd> Monit will start the servers in the following order: <i>d</i>, <i>c</i>, <i>b</i>, <i>a</i></p>
<dt>If all servers are running</p>
<dd> When you run &#8216;Monit stop all&#8217; this is the stop order: <i>a</i>, <i>b</i>, <i>c</i>, <i>d</i>. If you run &#8216;Monit stop d&#8217; then <i>a</i>, <i>b</i> and <i>c</i> are also stopped because they depend on <i>d</i> and finally <i>d</i> is stopped.</p>
<dt>If <i>a</i> does not run</p>
<dd> When Monit runs it will start <i>a</i></p>
<dt>If <i>b</i> does not run</p>
<dd> When Monit runs it will first stop <i>a</i> then start <i>b</i> and finally start <i>a</i> again.</p>
<dt>If <i>c</i> does not run</p>
<dd> When Monit runs it will first stop <i>a</i> and <i>b</i> then start <i>c</i> and finally start <i>b</i> then <i>a</i>.</p>
<dt>If <i>d</i> does not run</p>
<dd> When Monit runs it will first stop <i>a</i>, <i>b</i> and <i>c</i> then start <i>d</i> and finally start <i>c</i>, <i>b</i> then <i>a</i>.</p>
<dt>If the control file contains a depend loop.</p>
<dd> A depend loop is for example; a-&gt;b and b-&gt;a or a-&gt;b-&gt;c-&gt;a. </p>
<p> When Monit starts it will check for such loops and complain and exit if a loop was found. It will also exit with a complaint if a depend statement was used that does not point to a service in the control file.</dl>
<h2>SERVICE TESTS</h2>
<p> <i></i><font SIZE="-1"><i>GENERAL SYNTAX</i></font><i></i> </p>
<p> Monit provides several tests you can use in a &#8216;check&#8217; statement to test a service. </p>
<p> You can test either for some expected value or range and take actions if the value changed. </p>
<p> General syntax for testing a specific value or range: </p>
<pre>
 IF &lt;TEST&gt; THEN ACTION [ELSE IF SUCCEEDED THEN ACTION]
</pre>
<p> The action is evaluated each time the &lt;<font SIZE="-1">TEST</font>&gt; condition is true. Success action is optional and executed only when the state changes from failure to success. If success action is not set, Monit will send a recovery alert by default. </p>
<p> General syntax for a value change test: </p>
<pre>
 IF CHANGED &lt;TEST&gt; THEN ACTION
</pre>
<p> The action is executed each time the value changes. Monit will remember the new value and will trigger event if the value change again. </p>
<p> <i></i><font SIZE="-1"><i>ACTION</i></font><i></i> </p>
<p> In each test you must select the action to be executed from this list:</p>
<dl>
<dt>&bull;</p>
<dd> <font SIZE="-1"><code>ALERT</code></font> sends the user an alert event on each state change.</p>
<dt>&bull;</p>
<dd> <font SIZE="-1"><code>RESTART</code></font> restarts the service <code>and</code> send an alert. Restart is performed by calling the service&#8217;s registered restart method or by first calling the stop method followed by the start method if restart is not set.</p>
<dt>&bull;</p>
<dd> <font SIZE="-1"><code>START</code></font> starts the service by calling the service&#8217;s registered start method <code>and</code> send an alert.</p>
<dt>&bull;</p>
<dd> <font SIZE="-1"><code>STOP</code></font> stops the service by calling the service&#8217;s registered stop method <code>and</code> send an alert. If Monit stops a service it will not be checked by Monit anymore nor restarted again later. To reactivate monitoring of the service again you must explicitly enable monitoring from the web interface or from the console.</p>
<dt>&bull;</p>
<dd> <font SIZE="-1"><code>EXEC</code></font> can be used to execute an arbitrary program <code>and</code> send an alert. If you choose this action you must state the program to be executed and if the program require arguments you must enclose the program and its arguments in a quoted string. You may optionally specify the uid and gid the executed program should switch to upon start. For instance: </p>
<pre>
 exec &quot;/usr/local/tomcat/bin/startup.sh&quot;
      as uid nobody and gid nobody
</pre>
<p> Remember, if Monit is run by root, then all programs executed by Monit will be started with superuser privileges unless the uid and gid extension is used.</p>
<dt>&bull;</p>
<dd> <font SIZE="-1"><code>UNMONITOR</code></font> will disable monitoring of the service <code>and</code> send an alert. The service will not be checked by Monit anymore nor restarted again later. To reactivate monitoring of the service you must explicitly enable monitoring from the web interface or from the console.</dl>
<p> <i></i><font SIZE="-1"><i>FAILURE TOLERANCE</i></font><i></i> </p>
<p> By default the action is executed if it matches and the service set in an error state. However, you can require a test to fail more than once before the error event is triggered and the service state changed to failed. This is useful to avoid getting alerts on spurious errors, which can happen, especially with network tests. </p>
<p> Syntax: </p>
<pre>
 FOR &lt;X&gt; CYCLES ...
</pre>
<p> or: </p>
<pre>
 &lt;X&gt; [TIMES WITHIN] &lt;Y&gt; CYCLES ...
</pre>
<p> The condition can be used both for failure and success action. </p>
<p> The first, simpler and recommended format requires <tt>&quot;X&quot;</tt> consecutive events before switching the state: </p>
<pre>
 if failed
    port 80
    for 3 cycles
 then alert
</pre>
<p> The second format is more advanced and allows to tolerate intermittent issues, but still catch excessive problems, where the service is flapping between error and success states frequently. </p>
<p> For example if every second cycle fails (1-0-1-0-1-0-&#8230;), then &#8220;for 2 cycles&#8221; condition will never match, despite the service having problems. The following statement will catch such a state: </p>
<pre>
 if failed
    port 80
    for 3 times within 5 cycles
 then alert
</pre>
<p> Example which sets multiple error levels and actions: </p>
<p> check filesystem rootfs with path /dev/hda1<br />
  if space usage &gt; 80% for 5 times within 15 cycles then alert<br />
  if space usage &gt; 90% for 5 cycles then exec &#8216;/try/to/free/the/space&#8217;</p>
<p> Note: the maximum value for cycles is 64.</p>
<h3><font SIZE="-1">EXISTENCE TESTING</font></h3>
<p> This test is always active for the process, file, directory and fifo checks and is if not defined, it defaults to a restart action. </p>
<p> You can override the default action with the following statement: </p>
<pre>
 IF [DOES] NOT EXIST THEN action
</pre>
<p> <i>action</i> is a choice of &#8220;<font SIZE="-1">ALERT&#8221;, &#8220;RESTART&#8221;, &#8220;START&#8221;, &#8220;STOP&#8221;, &#8220;EXEC&#8221;</font> or &#8220;<font SIZE="-1">UNMONITOR&#8221;.</font> </p>
<p> Example: </p>
<pre>
 check file with path /cifs/mydata
       if does not exist then exec &quot;/usr/bin/mount_cifs.sh&quot;
</pre>
<h3><font SIZE="-1">RESOURCE TESTING</font></h3>
<p> Monit can examine how much system resources a service is using. This test can only be used within a system or process service entry in the Monit control file. </p>
<p> Depending on system or process characteristics, services can be stopped or restarted and alerts can be generated. Thus it is possible to utilize systems which are idle and to spare system under high load. </p>
<p> The full syntax for a resource-statement used for resource testing is as follows (keywords are in capital and optional statements in [brackets]), </p>
<pre>
 IF resource operator value THEN action
</pre>
<p> <i>resource</i> is a choice of &#8220;<font SIZE="-1">CPU&#8221;, &#8220;TOTAL CPU&#8221;, &#8220;CPU</font>([user|system|wait])&#8221;, &#8220;<font SIZE="-1">MEMORY&#8221;, &#8220;SWAP&#8221;, &#8220;CHILDREN&#8221;, &#8220;TOTAL MEMORY&#8221;, &#8220;LOADAVG</font>([1min|5min|15min])&#8221;. Some resource tests can be used inside a check system entry, some in a check process entry and some in both: </p>
<p> System only resource tests: </p>
<p> <font SIZE="-1">CPU</font>([user|system|wait]) is the percent of time the system spend in user or kernel space and I/O. The user/system/wait modifier is optional, if not used, the total system cpu usage is tested. </p>
<p> <font SIZE="-1">SWAP</font> is the swap usage of the system in either percent (of the systems total) or as an amount (Byte, kB, <font SIZE="-1">MB, GB</font>). </p>
<p> Process only resource tests: </p>
<p> <font SIZE="-1">CPU</font> is the <font SIZE="-1">CPU</font> usage of the process itself (percent). </p>
<p> <font SIZE="-1">TOTAL CPU</font> is the total <font SIZE="-1">CPU</font> usage of the process and its children in (percent). You will want to use <font SIZE="-1">TOTAL CPU</font> typically for services like Apache web server where one master process forks child processes as workers. </p>
<p> <font SIZE="-1">CHILDREN</font> is the number of child processes of the process. </p>
<p> <font SIZE="-1">TOTAL MEMORY</font> is the memory usage of the process and its child processes in either percent or as an amount (Byte, kB, <font SIZE="-1">MB, GB</font>). </p>
<p> System and process resource tests: </p>
<p> <font SIZE="-1">MEMORY</font> is the memory usage of the system or of a process (without children) in either percent (of the systems total) or as an amount (Byte, kB, <font SIZE="-1">MB, GB</font>). </p>
<p> <font SIZE="-1">LOADAVG</font>([1min|5min|15min]) refers to the system&#8217;s load average. The load average is the number of processes in the system run queue, averaged over the specified time period. </p>
<p> <i>operator</i> is a choice of &#8220;&lt;&#8221;, &#8220;&gt;&#8221;, &#8220;!=&#8221;, &#8220;==&#8221; in C notation, &#8220;gt&#8221;, &#8220;lt&#8221;, &#8220;eq&#8221;, &#8220;ne&#8221; in shell sh notation and &#8220;greater&#8221;, &#8220;less&#8221;, &#8220;equal&#8221;, &#8220;notequal&#8221; in human readable form (if not specified, default is <font SIZE="-1">EQUAL</font>). </p>
<p> <i>value</i> is either an integer or a real number (except for <font SIZE="-1">CHILDREN</font>). For <font SIZE="-1">CPU, TOTAL CPU, MEMORY</font> and <font SIZE="-1">TOTAL MEMORY</font> you need to specify a <i>unit</i>. This could be &#8220;%&#8221; or if applicable &#8220;B&#8221; (Byte), &#8220;kB&#8221; (1024 Byte), &#8220;<font SIZE="-1">MB&#8221; </font>(1024 KiloByte) or &#8220;<font SIZE="-1">GB&#8221; </font>(1024 MegaByte). </p>
<p> <i>action</i> is a choice of &#8220;<font SIZE="-1">ALERT&#8221;, &#8220;RESTART&#8221;, &#8220;START&#8221;, &#8220;STOP&#8221;, &#8220;EXEC&#8221;</font> or &#8220;<font SIZE="-1">UNMONITOR&#8221;.</font> </p>
<p> To calculate the cycles, a counter is raised whenever the expression above is true and it is lowered whenever it is false (but not below 0). All counters are reset in case of a restart. </p>
<p> The following is an example to check that the <font SIZE="-1">CPU</font> usage of a service is not going beyond 50% during five poll cycles. If it does, Monit will restart the service: </p>
<pre>
 if cpu is greater than 50% for 5 cycles then restart
</pre>
<h3><font SIZE="-1">FILE CHECKSUM TESTING</font></h3>
<p> The checksum statement may only be used in a file service entry and can be used to check the file&#8217;s <font SIZE="-1">MD5</font> or <font SIZE="-1">SHA1</font> checksum. </p>
<p> Check specific checksum: </p>
<p>IF FAILED[MD5 | SHA1] CHECKSUM[EXPECT checksum] THEN action</p>
<p> Check any file changes: </p>
<pre>
 IF CHANGED [MD5|SHA1] CHECKSUM THEN action
</pre>
<p> The choice of <font SIZE="-1">MD5</font> or <font SIZE="-1">SHA1</font> is optional. <font SIZE="-1">MD5</font> features a 128 bits checksum (32 bytes hex encoded string) and <font SIZE="-1">SHA1</font> a 160 bits checksum (40 bytes hex encoded string). If this option is omitted, Monit will try to guess the method from the <font SIZE="-1">EXPECT</font> string or use <font SIZE="-1">MD5</font> as the default checksum. </p>
<p> <tt>&quot;expect&quot;</tt> is optional and if used, specifies the md5 or sha1 string Monit should expect when testing a file&#8217;s checksum. Monit will then not compute an initial checksum for the file, but instead use the string you submit. For example: </p>
<pre>
 if failed
    checksum expect 8f7f419955cefa0b33a2ba316cba3659
 then alert
</pre>
<p> You can, for example, use the <font SIZE="-1">GNU</font> utility <i><a href="/docs/linux/man/1-md5sum/">md5sum</a>(1)</i> or <i><a href="/docs/linux/man/1-sha1sum/">sha1sum</a>(1)</i> to create a checksum string for a file and use this string in the expect-statement. </p>
<p> Reloading a server if its configuration file was changed: </p>
<pre>
 check file apache_conf with path /etc/apache/httpd.conf
     if changed checksum then exec &quot;/usr/bin/apachectl graceful&quot;
</pre>
<p> <i>action</i> is a choice of &#8220;<font SIZE="-1">ALERT&#8221;, &#8220;RESTART&#8221;, &#8220;START&#8221;, &#8220;STOP&#8221;, &#8220;EXEC&#8221;</font> or &#8220;<font SIZE="-1">UNMONITOR&#8221;.</font></p>
<h3><font SIZE="-1">TIMESTAMP TESTING</font></h3>
<p> The timestamp statement may only be used in a file, fifo or directory service entry. </p>
<p> Specific timestamp syntax: </p>
<p> IF TIMESTAMP [[operator] value [unit]] THEN action</p>
<p> Timestamp changed syntax: </p>
<pre>
 IF CHANGED TIMESTAMP THEN action
</pre>
<p> <i>operator</i> is a choice of &#8220;&lt;&#8221;, &#8220;&gt;&#8221;, &#8220;!=&#8221;, &#8220;==&#8221; in C notation, &#8220;<font SIZE="-1">GT&#8221;, &#8220;LT&#8221;, &#8220;EQ&#8221;, &#8220;NE&#8221;</font> in shell sh notation and &#8220;<font SIZE="-1">GREATER&#8221;, &#8220;LESS&#8221;, &#8220;EQUAL&#8221;, &#8220;NOTEQUAL&#8221;</font> in human readable form (if not specified, default is <font SIZE="-1">EQUAL</font>). </p>
<p> <i>value</i> is a time watermark. </p>
<p> <i>unit</i> is either &#8220;<font SIZE="-1">SECOND</font>(S)&#8221;, &#8220;<font SIZE="-1">MINUTE</font>(S)&#8221;, &#8220;<font SIZE="-1">HOUR</font>(S)&#8221; or &#8220;<font SIZE="-1">DAY</font>(S)&#8221;. </p>
<p> <i>action</i> is a choice of &#8220;<font SIZE="-1">ALERT&#8221;, &#8220;RESTART&#8221;, &#8220;START&#8221;, &#8220;STOP&#8221;, &#8220;EXEC&#8221;</font> or &#8220;<font SIZE="-1">UNMONITOR&#8221;.</font> </p>
<p> For example to reload apache if the configuration file timestamp changed: </p>
<pre>
 check file apache_conf with path /etc/apache/httpd.conf
   if changed timestamp then exec &quot;/usr/bin/apachectl graceful&quot;
</pre>
<p> For example testing directory for file addition or removal: </p>
<pre>
 check directory bar path /foo/bar
       if timestamp &lt; 1 hour then alert
</pre>
<h3><font SIZE="-1">FILE SIZE TESTING</font></h3>
<p> The size statement may only be used in a check file service entry. If specified in the control file, Monit will compute a size for a file. </p>
<p> Testing specific size or range: </p>
<p> IF SIZE [[operator] value [unit]] THEN action</p>
<p> Testing size changes: </p>
<pre>
 IF CHANGED SIZE THEN action
</pre>
<p> <i>operator</i> is a choice of &#8220;&lt;&#8221;, &#8220;&gt;&#8221;, &#8220;!=&#8221;, &#8220;==&#8221; in C notation, &#8220;<font SIZE="-1">GT&#8221;, &#8220;LT&#8221;, &#8220;EQ&#8221;, &#8220;NE&#8221;</font> in shell sh notation and &#8220;<font SIZE="-1">GREATER&#8221;, &#8220;LESS&#8221;, &#8220;EQUAL&#8221;, &#8220;NOTEQUAL&#8221;</font> in human readable form (if not specified, default is <font SIZE="-1">EQUAL</font>). </p>
<p> <i>value</i> is a size watermark. </p>
<p> <i>unit</i> is a choice of &#8220;B&#8221;,&#8220;<font SIZE="-1">KB&#8221;,&#8220;MB&#8221;,&#8220;GB&#8221;</font> or long alternatives &#8220;byte&#8221;, &#8220;kilobyte&#8221;, &#8220;megabyte&#8221;, &#8220;gigabyte&#8221;. If it is not specified, &#8220;byte&#8221; unit is assumed by default. </p>
<p> <i>action</i> is a choice of &#8220;<font SIZE="-1">ALERT&#8221;, &#8220;RESTART&#8221;, &#8220;START&#8221;, &#8220;STOP&#8221;, &#8220;EXEC&#8221;</font> or &#8220;<font SIZE="-1">UNMONITOR&#8221;.</font> </p>
<p> For example to send an alert if the file is too large: </p>
<pre>
 check file mydb with path /data/mydatabase.db
       if size &gt; 1 GB then alert
</pre>
<h3><font SIZE="-1">FILE CONTENT TESTING</font></h3>
<p> The match statement can be used to incrementally test the content of a text file by using regular expressions. </p>
<p> Syntax: </p>
<p>IF[NOT] MATCH{regex | path} THEN action</p>
<p> <i>regex</i> is a string containing the extended regular expression. See also <i><a href="/docs/linux/man/7-regex/">regex</a></i>(7). </p>
<p> <i>path</i> is an absolute path to a file containing extended regular expression on every line. See also <i><a href="/docs/linux/man/7-regex/">regex</a></i>(7). </p>
<p> <i>action</i> is a choice of &#8220;<font SIZE="-1">ALERT&#8221;, &#8220;RESTART&#8221;, &#8220;START&#8221;, &#8220;STOP&#8221;, &#8220;EXEC&#8221;</font> or &#8220;<font SIZE="-1">UNMONITOR&#8221;.</font> </p>
<p> You can use the <i></i><font SIZE="-1"><i>NOT</i></font><i></i> statement to invert a match. </p>
<p> On startup the read position is set to the end of the file and Monit continues to scan to the end of the file on each cycle. </p>
<p> If the file size should decrease or inode changed, the read position is set to the start of the file. </p>
<p> Only lines ending with a newline character are inspected. </p>
<p> Only the first 511 characters of a line are inspected. </p>
<p>IGNORE[NOT] MATCH<br />
{<br />
    regex | path<br />
}</p>
<p> Lines matching an <i></i><font SIZE="-1"><i>IGNORE</i></font><i></i> are not inspected during later evaluations. <i></i><font SIZE="-1"><i>IGNORE MATCH</i></font><i></i> has always precedence over <i></i><font SIZE="-1"><i>IF MATCH</i></font><i></i>. </p>
<p> All <i></i><font SIZE="-1"><i>IGNORE MATCH</i></font><i></i> statements are evaluated first, in the order of their appearance. Thereafter, all the <i></i><font SIZE="-1"><i>IF MATCH</i></font><i></i> statements are evaluated. </p>
<p> For example: </p>
<pre>
  check file syslog with path /var/log/syslog
        ignore match &quot;^monit&quot;
        if match &quot;^mrcoffee&quot; then alert
</pre>
<h3><font SIZE="-1">FILESYSTEM FLAGS TESTING</font></h3>
<p> Monit can test the flags of a filesystem for changes. This test is implicit and Monit will send alert in case of failure by default. </p>
<p> This test is useful for detecting changes of filesystem flags such as if the filesystem become read-only (on disk error) or mount flags were changed (such as nosuid). </p>
<p> The syntax for the fsflags statement is: </p>
<pre>
 IF CHANGED FSFLAGS THEN action
</pre>
<p> <i>action</i> is a choice of &#8220;<font SIZE="-1">ALERT&#8221;, &#8220;RESTART&#8221;, &#8220;START&#8221;, &#8220;STOP&#8221;, &#8220;EXEC&#8221;</font> or &#8220;<font SIZE="-1">UNMONITOR&#8221;.</font> </p>
<p> Example: </p>
<pre>
 check filesystem rootfs with path /
       if changed fsflags then exec &quot;/my/script&quot;
</pre>
<h3><font SIZE="-1">SPACE TESTING</font></h3>
<p> Monit can test a filesystem or a disk for space usage. This test may only be used in the context of a filesystem service type. </p>
<p> Filesystems usually have some space reserved for the root user (ca. 1-5%), so non-superusers cannot write to a nearly full filesystem. If you set a limit for the filesystem which is used by non-root users you might want to consider these reserved blocks when setting the limit. You can use Monit itself to view the reserved blocks percentage by using the <font SIZE="-1">CLI</font> status command or the <font SIZE="-1">HTTP</font> interface for the given filesystem. </p>
<p> Syntax: </p>
<pre>
 IF SPACE operator value unit THEN action
</pre>
<p> or: </p>
<pre>
 IF SPACE FREE operator value unit THEN action
</pre>
<p> <i>operator</i> is a choice of &#8220;&lt;&#8221;,&#8220;&gt;&#8221;,&#8220;!=&#8221;,&#8220;==&#8221; in c notation, &#8220;gt&#8221;, &#8220;lt&#8221;, &#8220;eq&#8221;, &#8220;ne&#8221; in shell sh notation and &#8220;greater&#8221;, &#8220;less&#8221;, &#8220;equal&#8221;, &#8220;notequal&#8221; in human readable form (if not specified, default is <font SIZE="-1">EQUAL</font>). </p>
<p> <i>unit</i> is a choice of &#8220;B&#8221;,&#8220;<font SIZE="-1">KB&#8221;,&#8220;MB&#8221;,&#8220;GB&#8221;, </font>&#8220;%&#8221; or long alternatives &#8220;byte&#8221;, &#8220;kilobyte&#8221;, &#8220;megabyte&#8221;, &#8220;gigabyte&#8221;, &#8220;percent&#8221;. </p>
<p> <i>action</i> is a choice of &#8220;<font SIZE="-1">ALERT&#8221;, &#8220;RESTART&#8221;, &#8220;START&#8221;, &#8220;STOP&#8221;, &#8220;EXEC&#8221;</font> or &#8220;<font SIZE="-1">UNMONITOR&#8221;.</font> </p>
<p> Example: </p>
<pre>
 check filesystem rootfs with path /
       if space usage &gt; 90% then alert
</pre>
<h3><font SIZE="-1">INODE TESTING</font></h3>
<p> Monit can test filesystem inode usage. This test may only be used in the context of a filesystem service type. </p>
<p> Syntax: </p>
<pre>
 IF INODE(S) operator value [unit] THEN action
</pre>
<p> or: </p>
<pre>
 IF INODE(S) FREE operator value [unit] THEN action
</pre>
<p> <i>operator</i> is a choice of &#8220;&lt;&#8221;,&#8220;&gt;&#8221;,&#8220;!=&#8221;,&#8220;==&#8221; in c notation, &#8220;gt&#8221;, &#8220;lt&#8221;, &#8220;eq&#8221;, &#8220;ne&#8221; in shell sh notation and &#8220;greater&#8221;, &#8220;less&#8221;, &#8220;equal&#8221;, &#8220;notequal&#8221; in human readable form (if not specified, default is <font SIZE="-1">EQUAL</font>). </p>
<p> <i>unit</i> is optional. If not specified, the value is an absolute count of inodes. You can use the &#8220;%&#8221; character or the longer alternative &#8220;percent&#8221; as a unit. </p>
<p> <i>action</i> is a choice of &#8220;<font SIZE="-1">ALERT&#8221;, &#8220;RESTART&#8221;, &#8220;START&#8221;, &#8220;STOP&#8221;, &#8220;EXEC&#8221;</font> or &#8220;<font SIZE="-1">UNMONITOR&#8221;.</font> </p>
<p> Example: </p>
<pre>
 check filesystem rootfs with path /
       if inode usage &gt; 90% then alert
</pre>
<h3><font SIZE="-1">PERMISSION TESTING</font></h3>
<p> Monit can test the permissions of file objects. This test may only be used in the context of a file, fifo, directory or filesystem service types. </p>
<p> Syntax for testing specific permissions: </p>
<pre>
 IF FAILED PERM(ISSION) octalnumber THEN action
</pre>
<p> Syntax for testing any permission change: </p>
<pre>
 IF CHANGED PERM(ISSION) THEN action
</pre>
<p> <i>octalnumber</i> defines permissions for a file, a directory or a filesystem as four octal digits (0-7). Valid range is 0000 &#8211; 7777 (you can omit the leading zeros, Monit will add the zeros to the left. For example, &#8220;640&#8221; is a valid value and matches &#8220;0640&#8221;). </p>
<p> <i>action</i> is a choice of &#8220;<font SIZE="-1">ALERT&#8221;, &#8220;RESTART&#8221;, &#8220;START&#8221;, &#8220;STOP&#8221;, &#8220;EXEC&#8221;</font> or &#8220;<font SIZE="-1">UNMONITOR&#8221;.</font> </p>
<p> Example: </p>
<pre>
 check file shadow with path /etc/shadow
       if failed permission 0640 then alert
</pre>
<h3><font SIZE="-1">UID TESTING</font></h3>
<p> Monit can monitor the owner user id (uid) of a file, fifo, directory or owner and effective user of a process. </p>
<p> Syntax: </p>
<pre>
 IF FAILED [E]UID user THEN action
</pre>
<p> <i>user</i> defines a user id either in numeric or in string form. </p>
<p> <i>action</i> is a choice of &#8220;<font SIZE="-1">ALERT&#8221;, &#8220;RESTART&#8221;, &#8220;START&#8221;, &#8220;STOP&#8221;, &#8220;EXEC&#8221;</font> or &#8220;<font SIZE="-1">UNMONITOR&#8221;.</font> </p>
<p> Example: </p>
<pre>
 check file shadow with path /etc/shadow
       if failed uid root then alert
</pre>
<h3><font SIZE="-1">GID TESTING</font></h3>
<p> Monit can monitor the owner group id (gid) of a file, fifo, directory or process. </p>
<p> Syntax: </p>
<pre>
 IF FAILED GID group THEN action
</pre>
<p> <i>group</i> defines a group id either in numeric or in string form. </p>
<p> <i>action</i> is a choice of &#8220;<font SIZE="-1">ALERT&#8221;, &#8220;RESTART&#8221;, &#8220;START&#8221;, &#8220;STOP&#8221;, &#8220;EXEC&#8221;</font> or &#8220;<font SIZE="-1">UNMONITOR&#8221;.</font> </p>
<p> Example: </p>
<pre>
 check file shadow with path /etc/shadow
       if failed gid shadow then alert
</pre>
<h3><font SIZE="-1">PID TESTING</font></h3>
<p> Monit can test the process&#8217; <font SIZE="-1">PID.</font> This test is implicit and Monit will send an alert in case the <font SIZE="-1">PID</font> changed outside of Monit&#8217;s control. </p>
<p> Syntax: </p>
<pre>
 IF CHANGED PID THEN action
</pre>
<p> <i>action</i> is a choice of &#8220;<font SIZE="-1">ALERT&#8221;, &#8220;RESTART&#8221;, &#8220;START&#8221;, &#8220;STOP&#8221;, &#8220;EXEC&#8221;</font> or &#8220;<font SIZE="-1">UNMONITOR&#8221;.</font> </p>
<p> This test is useful to detect possible process restarts which has occurred in the timeframe between two Monit testing cycles. </p>
<p> For example if someone changes sshd configuration and did sshd restart outside of Monit&#8217;s control you will be notified that the process was replaced by a new instance: </p>
<pre>
 check process sshd with pidfile /var/run/sshd.pid
       if changed pid then alert
</pre>
<h3><font SIZE="-1">PPID TESTING</font></h3>
<p> Monit can test the process&#8217; parent <font SIZE="-1">PID </font>(<font SIZE="-1">PPID</font>) for changes. This test is implicit and Monit will send alert in the case that the <font SIZE="-1">PPID</font> changed outside of Monit control. </p>
<p> The syntax for the ppid statement is: </p>
<pre>
 IF CHANGED PPID THEN action
</pre>
<p> <i>action</i> is a choice of &#8220;<font SIZE="-1">ALERT&#8221;, &#8220;RESTART&#8221;, &#8220;START&#8221;, &#8220;STOP&#8221;, &#8220;EXEC&#8221;</font> or &#8220;<font SIZE="-1">UNMONITOR&#8221;.</font> </p>
<p> Example: </p>
<pre>
 check process myproc with pidfile /var/run/myproc.pid
       if changed ppid then exec &quot;/my/script&quot;
</pre>
<h3><font SIZE="-1">PROCESS UPTIME TESTING</font></h3>
<p> The uptime statement may only be used in a process service type context. </p>
<p> Syntax: </p>
<p> IF UPTIME [[operator] value [unit]] THEN action</p>
<p> <i>operator</i> is a choice of &#8220;&lt;&#8221;, &#8220;&gt;&#8221;, &#8220;!=&#8221;, &#8220;==&#8221; in C notation, &#8220;<font SIZE="-1">GT&#8221;, &#8220;LT&#8221;, &#8220;EQ&#8221;, &#8220;NE&#8221;</font> in shell sh notation and &#8220;<font SIZE="-1">GREATER&#8221;, &#8220;LESS&#8221;, &#8220;EQUAL&#8221;, &#8220;NOTEQUAL&#8221;</font> in human readable form (if not specified, default is <font SIZE="-1">EQUAL</font>). </p>
<p> <i>value</i> is a uptime watermark. </p>
<p> <i>unit</i> is either &#8220;<font SIZE="-1">SECOND&#8221;, &#8220;MINUTE&#8221;, &#8220;HOUR&#8221;</font> or &#8220;<font SIZE="-1">DAY&#8221; </font>(it is also possible to use &#8220;<font SIZE="-1">SECONDS&#8221;, &#8220;MINUTES&#8221;, &#8220;HOURS&#8221;,</font> or &#8220;<font SIZE="-1">DAYS&#8221;</font>). </p>
<p> <i>action</i> is a choice of &#8220;<font SIZE="-1">ALERT&#8221;, &#8220;RESTART&#8221;, &#8220;START&#8221;, &#8220;STOP&#8221;, &#8220;EXEC&#8221;</font> or &#8220;<font SIZE="-1">UNMONITOR&#8221;.</font> </p>
<p> Example of restarting the process every three days: </p>
<pre>
 check process myapp with pidfile /var/run/myapp.pid
    start program = &quot;/etc/init.d/myapp start&quot;
    stop program = &quot;/etc/init.d/myapp stop&quot;
    if uptime &gt; 3 days then restart
</pre>
<h3><font SIZE="-1">PROGRAM STATUS TESTING</font></h3>
<p> You can check the exit status of a program or a script. This test may only be used within a check program service entry in the Monit control file. </p>
<p> Syntax for testing specific exit value: </p>
<pre>
 IF STATUS operator value THEN action
</pre>
<p> Syntax for testing any exit value change: </p>
<pre>
 IF CHANGED STATUS THEN action
</pre>
<p> <i>operator</i> is a choice of &#8220;&lt;&#8221;,&#8220;&gt;&#8221;,&#8220;!=&#8221;,&#8220;==&#8221; in c notation, &#8220;gt&#8221;, &#8220;lt&#8221;, &#8220;eq&#8221;, &#8220;ne&#8221; in shell sh notation and &#8220;greater&#8221;, &#8220;less&#8221;, &#8220;equal&#8221;, &#8220;notequal&#8221; in human readable form (if not specified, default is <font SIZE="-1">EQUAL</font>). </p>
<p> <i>action</i> is a choice of &#8220;<font SIZE="-1">ALERT&#8221;, &#8220;RESTART&#8221;, &#8220;START&#8221;, &#8220;STOP&#8221;, &#8220;EXEC&#8221;</font> or &#8220;<font SIZE="-1">UNMONITOR&#8221;.</font> </p>
<p> Example: </p>
<pre>
 check program myscript with path /usr/local/bin/myscript.sh
       if status != 0 then alert
</pre>
<p> Sample script for the above example (/usr/local/bin/myscript.sh): </p>
<pre>
 #!/bin/bash
 echo test
 exit $?
</pre>
<p> You can also send parameters with the program: </p>
<pre>
 check program list-files with path &quot;/bin/ls -lrt /tmp/&quot;
       if status != 0 then alert
</pre>
<p> Arguments to the program or script is a sequence of whitespace separated strings. In the above example the strings &#8216;-lrt&#8217; and &#8216;/tmp/&#8217; are arguments to the program &#8216;/bin/ls&#8217;. If arguments are used, it is recommended to use quotes <code>&quot;</code> to enclose the string, otherwise, if no arguments are used, quotes are not needed. </p>
<p> Notes: If the program is a script, the interpreter is required in the first line. The program or script must also be executable. </p>
<p> If Monit is run as the super user, you can optionally run the program as a different user and/or group. In this example we run the <i>ls</i> program as user www and as group staff: </p>
<pre>
 check program ls with path &quot;/bin/ls /tmp&quot; as uid &quot;www&quot;
          and gid &quot;staff&quot;
       if status != 0 then alert
</pre>
<p> Monit will execute the program periodically and if the exit status of the program does not match the expected result, Monit can perform an action. In the example above, Monit will raise an alert if the exit value is different from 0. By convention, 0 means the program exited normally. </p>
<p> Program checks are asynchronous. Meaning that Monit will not wait for the program to exit, but instead, Monit will start the program in the background and immediately continue checking the next service entry in <i>monitrc</i>. At the next cycle, Monit will check if the program has finished and if so, collect the program&#8217;s exit status. If the status indicate a failure, Monit will raise an alert message containing the program&#8217;s error (stderr) output, if any. If the program has not exited after the first cycle, Monit will wait another cycle and so on. If the program is still running after 5 minutes, Monit will kill it and generate a program timeout event. It is possible to override the default timeout (see the syntax below). </p>
<p> The asynchronous nature of the program check allows for non-blocking behavior in the current Monit design, but it comes with a side-effect: when the program has finished executing and is waiting for Monit to collect the result, it becomes a so-called &#8220;zombie&#8221; process. A zombie process does not consume any system resources (only the <font SIZE="-1">PID</font> remains in use) and it is under Monit&#8217;s control and the zombie process is removed from the system as soon as Monit collects the exit status. This means that every &#8220;check program&#8221; will be associated with either a running process or a temporary zombie. This unwanted zombie side-effect will be removed in a later release of Monit. </p>
<p> Multiple status tests can be used, for example: </p>
<pre>
 check program hwtest with path /usr/local/bin/hwtest.sh
       with timeout 500 seconds
       if status = 1 then alert
       if status = 3 for 5 cycles then exec &quot;/usr/local/bin/emergency.sh&quot;
</pre>
<h3><font SIZE="-1">NETWORK LINK STATUS TEST</font></h3>
<p> You can check the network link state. This test may only be used within a check network service entry in the Monit control file. </p>
<p> Syntax: </p>
<pre>
 IF FAILED LINK THEN action
</pre>
<p> <i>action</i> is a choice of &#8220;<font SIZE="-1">ALERT&#8221;, &#8220;RESTART&#8221;, &#8220;START&#8221;, &#8220;STOP&#8221;, &#8220;EXEC&#8221;</font> or &#8220;<font SIZE="-1">UNMONITOR&#8221;.</font> </p>
<p> The test will fail if the link/interface is down or link errors were detected. </p>
<p> Example: </p>
<pre>
 check network eth0 with interface eth0 
       if failed link then alert
</pre>
<p> In case a link failed you can add a start and stop program to automatically restart the interface which might help. (Substitute with the relevant network commands for your system) </p>
<pre>
 check network eth0 with interface eth0
       start program = '/sbin/ipup eth0'
       stop program = '/sbin/ipdown eth0'
       if failed link then restart
</pre>
<h3><font SIZE="-1">NETWORK LINK CAPACITY TEST</font></h3>
<p> You can check the network link mode capacity for changes. This test may only be used within a check network service entry in the Monit control file. </p>
<p> Syntax: </p>
<pre>
 IF CHANGED LINK [CAPACITY] THEN action
</pre>
<p> <i>action</i> is a choice of &#8220;<font SIZE="-1">ALERT&#8221;, &#8220;RESTART&#8221;, &#8220;START&#8221;, &#8220;STOP&#8221;, &#8220;EXEC&#8221;</font> or &#8220;<font SIZE="-1">UNMONITOR&#8221;.</font> </p>
<p> The test will match if the link mode has changed (e.g. maximum speed dropped) or if the duplex mode has changed. </p>
<p> <font SIZE="-1">NOTE:</font> not all interface types allow for capacity monitoring. Pseudo interfaces such as loopback device or VMWare interfaces does not have a speed attribute. </p>
<p> Example: </p>
<pre>
 check network eth0 with interface eth0 
       if changed link capacity then alert
</pre>
<h3><font SIZE="-1">NETWORK SATURATION TEST</font></h3>
<p> You can check the network link saturation. Monit then computes the link utilization based on the current transfer rate vs. link capacity. This test may only be used within a check network service entry in the Monit control file. </p>
<p> Syntax: </p>
<pre>
 IF SATURATION operator value% THEN action
</pre>
<p> <i>operator</i> is a choice of &#8220;&lt;&#8221;,&#8220;&gt;&#8221;,&#8220;!=&#8221;,&#8220;==&#8221; in c notation, &#8220;gt&#8221;, &#8220;lt&#8221;, &#8220;eq&#8221;, &#8220;ne&#8221; in shell sh notation and &#8220;greater&#8221;, &#8220;less&#8221;, &#8220;equal&#8221;, &#8220;notequal&#8221; in human readable form (if not specified, default is <font SIZE="-1">EQUAL</font>). </p>
<p> <i>action</i> is a choice of &#8220;<font SIZE="-1">ALERT&#8221;, &#8220;RESTART&#8221;, &#8220;START&#8221;, &#8220;STOP&#8221;, &#8220;EXEC&#8221;</font> or &#8220;<font SIZE="-1">UNMONITOR&#8221;.</font> </p>
<p> <font SIZE="-1">NOTE:</font> this test depends on the availability of the speed attribute and not all interface types have this attribute. See the <font SIZE="-1">LINK SPEED</font> test description. </p>
<p> Example: </p>
<pre>
 check network eth0 with interface eth0 
       if saturation &gt; 90% then alert
</pre>
<h3><font SIZE="-1">NETWORK BANDWIDTH TEST</font></h3>
<p> You can check a network link upload and download bandwidth usage, current transfer rate and total data transferred in the last 24 hours. This test may only be used within a check network service entry in the Monit control file. </p>
<p> Warning: this test requires monit poll time to be at maximum 30 seconds. </p>
<p> Current upload bandwidth rate test syntax: </p>
<pre>
 IF UPLOAD operator value unit THEN action
</pre>
<p> Current download bandwidth rate test syntax: </p>
<pre>
 IF DOWNLOAD operator value unit THEN action
</pre>
<p> Total upload test syntax: </p>
<pre>
 IF TOTAL UPLOAD operator value unit IN LAST number time-unit THEN action
</pre>
<p> Total download test syntax: </p>
<pre>
 IF TOTAL DOWNLOAD operator value unit IN LAST number time-unit THEN action
</pre>
<p> <i>operator</i> is a choice of &#8220;&lt;&#8221;,&#8220;&gt;&#8221;,&#8220;!=&#8221;,&#8220;==&#8221; in c notation, &#8220;gt&#8221;, &#8220;lt&#8221;, &#8220;eq&#8221;, &#8220;ne&#8221; in shell sh notation and &#8220;greater&#8221;, &#8220;less&#8221;, &#8220;equal&#8221;, &#8220;notequal&#8221; in human readable form (if not specified, default is <font SIZE="-1">EQUAL</font>). </p>
<p> <i>unit</i> is a choice of &#8220;B&#8221;,&#8220;<font SIZE="-1">KB&#8221;,&#8220;MB&#8221;,&#8220;GB&#8221;</font> or long alternatives &#8220;byte&#8221;, &#8220;kilobyte&#8221;, &#8220;megabyte&#8221;, &#8220;gigabyte&#8221;. </p>
<p> <i>time-unit</i> is a choice of &#8220;<font SIZE="-1">MINUTE</font>(S)&#8221;, &#8220;<font SIZE="-1">HOUR</font>(S)&#8221;, &#8220;<font SIZE="-1">DAY&#8221;. NOTE:</font> Monit maintains a rolling count of total uploaded and downloaded bytes for the last 24 hours only. The value of time-unit can therefor not specify a range wider than one day. </p>
<p> <i>action</i> is a choice of &#8220;<font SIZE="-1">ALERT&#8221;, &#8220;RESTART&#8221;, &#8220;START&#8221;, &#8220;STOP&#8221;, &#8220;EXEC&#8221;</font> or &#8220;<font SIZE="-1">UNMONITOR&#8221;.</font> </p>
<p> Examples: </p>
<pre>
 check network eth0 with interface eth0 
       if upload &gt; 500 kB/s then alert
       if total download &gt; 1 GB in last 2 hours then alert
       if total download &gt; 10 GB in last day then alert
</pre>
<h3><font SIZE="-1">NETWORK PACKETS TEST</font></h3>
<p> You can check the network link upload and download packets count, current transfer rate and total data transferred in last 24 hours. This test may only be used within a check network service entry in the Monit control file. </p>
<p> Warning: this test requires monit poll time to be at maximum 30 seconds. </p>
<p> Current upload bandwidth rate test syntax: </p>
<pre>
 IF UPLOAD operator value PACKETS/S THEN action
</pre>
<p> Current download bandwidth rate test syntax: </p>
<pre>
 IF DOWNLOAD operator value PACKETS/S THEN action
</pre>
<p> Total upload test syntax: </p>
<pre>
 IF TOTAL UPLOAD operator value PACKETS IN LAST number time-unit THEN action
</pre>
<p> Total download test syntax: </p>
<pre>
 IF TOTAL DOWNLOAD operator value PACKETS IN LAST number time-unit THEN action
</pre>
<p> <i>operator</i> is a choice of &#8220;&lt;&#8221;,&#8220;&gt;&#8221;,&#8220;!=&#8221;,&#8220;==&#8221; in c notation, &#8220;gt&#8221;, &#8220;lt&#8221;, &#8220;eq&#8221;, &#8220;ne&#8221; in shell sh notation and &#8220;greater&#8221;, &#8220;less&#8221;, &#8220;equal&#8221;, &#8220;notequal&#8221; in human readable form (if not specified, default is <font SIZE="-1">EQUAL</font>). </p>
<p> <i>time-unit</i> is a choice of &#8220;<font SIZE="-1">MINUTE</font>(S)&#8221;, &#8220;<font SIZE="-1">HOUR</font>(S)&#8221;, &#8220;<font SIZE="-1">DAY&#8221;. NOTE:</font> Monit keeps total upload/download statistics only for the last 24 hours. The time-unit value cannot therefor span more than one day. </p>
<p> <i>action</i> is a choice of &#8220;<font SIZE="-1">ALERT&#8221;, &#8220;RESTART&#8221;, &#8220;START&#8221;, &#8220;STOP&#8221;, &#8220;EXEC&#8221;</font> or &#8220;<font SIZE="-1">UNMONITOR&#8221;.</font> </p>
<p> Examples: </p>
<pre>
 check network eth0 with interface eth0 
       if upload &gt; 1000 packets/s then alert
       if total upload &gt; 900000 packets in last hour then alert
</pre>
<h3><font SIZE="-1">NETWORK PING TEST</font></h3>
<p> Monit can perform a network ping test by sending <font SIZE="-1">ICMP</font> echo request datagram packets to a host and wait for the reply. This test can only be used within a check host statement. Monit must also run as the root user in order to be able to perform the ping test (because the ping test must use raw sockets which usually only the super user is allowed to). </p>
<p> Syntax: </p>
<p>IF FAILED PING[4 | 6]<br />
              [COUNT number][WITH][TIMEOUT number SECONDS] THEN action</p>
<p> If a <font SIZE="-1">DNS</font> host name was used in the <i>check host</i> statement and the host name resolve to several addresses (either IPv4 or IPv6), Monit will ping the first available address and continue with the next address until one connection succeed or until there are no more addresses left to try. You can force Monit to only ping IPv4 or IPv6 addresses by using the <font SIZE="-1">PING4</font> or the <font SIZE="-1">PING6</font> keyword instead of <font SIZE="-1">PING.</font> </p>
<p> The <font SIZE="-1"><code>COUNT</code></font> parameter specifies how many consecutive ping requests will be sent to the host in one cycle. If no reply arrive within <font SIZE="-1"><code>TIMEOUT</code></font> seconds, Monit reports an error. If at least one reply was received, the ping test is considered a success. Monit will, by default, send <i>three</i> ping request packets in one cycle to prevent false alarm (i.e. up to 66% packet loss is tolerated). You can set the <font SIZE="-1"><code>COUNT</code></font> option to a value between 1 and 20 to send more or fewer packets. If you require 100% ping success, set the count to 1 (i.e. just one request will be sent, and if the packet was lost an error will be reported). </p>
<p> Note that many ISPs have started to filter out ping or <font SIZE="-1">ICMP</font> packets now, in which case there will be no reply from the host. </p>
<p> If a ping test is used in a check host entry, this test is run first and if the test should fail, we assume that the connection to the host is down and Monit will <i>not</i> continue with any subsequent port tests. </p>
<p> Example: </p>
<pre>
 check host mmonit.com with address mmonit.com
       if failed ping then alert  # IPv4 or IPv6
 check host mmonit.com with address 62.109.39.247
       if failed ping then alert # Address is IPv4 so IPv4 is preferred
</pre>
<p> or test that the system is explicit accessible via IPv4 and IPv6: </p>
<pre>
 check host mmonit.com with address mmonit.com
       if failed ping4 then alert  # IPv4 only
       if failed ping6 then alert  # IPv6 only
</pre>
<p> or with all parameters; Send 5 pings to mmonit.com and wait for up to 10 seconds for a reply </p>
<pre>
  check host mmonit.com with address mmonit.com
        if failed ping count 5 with timeout 10 seconds then alert
</pre>
<h3><font SIZE="-1">CONNECTION TESTING</font></h3>
<p> Monit can perform connection testing via network ports or via Unix sockets. A connection test may only be used within a process or host service type context. </p>
<p> If a service listens on one or more sockets, Monit can connect to the port (using <font SIZE="-1">TCP</font> or <font SIZE="-1">UDP</font>) and verify that the service will accept a connection and that it is possible to write and read from the socket. If a connection is not accepted or if there is a problem with socket I/O, Monit will execute a specified action. </p>
<p> <font SIZE="-1">TCP/UDP</font> port test syntax: </p>
<p>IF FAILED<br />
    [host]&lt;port&gt;[ipversion]<br />
                [type]<br />
                [protocol | {send / expect} + ]<br />
                [timeout]<br />
                [retry] THEN action</p>
<p> Unix socket test syntax: </p>
<p>IF FAILED&lt;unixsocket&gt;[type]<br />
                     [protocol | {send / expect} + ]<br />
                     [timeout]<br />
                     [retry] THEN action</p>
<p> Examples: </p>
<pre>
 if failed port 80 then alert
 if failed port 53 type udp protocol dns then alert
 if failed unixsocket /var/run/sophie then alert
</pre>
<p> Options: </p>
<p> <i>host: </i><font SIZE="-1"><i>HOST</i></font><i> hostname</i>. Optionally specify the host to connect to. If the host is not given then localhost is assumed if this test is used inside a process entry. If this test is used inside a remote host entry then the entry&#8217;s remote host is assumed. </p>
<p> <i>port: </i><font SIZE="-1"><i>PORT</i></font><i> number</i>. The port number to connect to </p>
<p> <i>unixsocket: </i><font SIZE="-1"><i>UNIXSOCKET</i></font><i> path</i>. Specifies the path to a Unix socket (local machine only). </p>
<p> <i>ipversion: </i><font SIZE="-1"><i>IPV4</i></font><i> | </i><font SIZE="-1"><i>IPV6 </i></font><i></i>. Optionally specify the <font SIZE="-1">IP</font> version Monit should use when trying to connect to the port. If not used, Monit will try to connect to the first available address (IPv4 or IPv6). If multiple addresses are available and connection to one address failed, Monit will try the next address and so on until a connection succeed or until there are no more addresses left to try. </p>
<p> <i>type: </i><font SIZE="-1"><i>TYPE</i></font><i> {TCP|UDP|TCPSSL}</i>. Optionally specify the socket type Monit should use when trying to connect to the port. The different socket types are; <font SIZE="-1">TCP, UDP</font> or <font SIZE="-1">TCPSSL,</font> where <font SIZE="-1">TCP</font> is a regular stream based socket, <font SIZE="-1">UDP</font> is a datagram socket and <font SIZE="-1">TCPSSL</font> specifies that Monit should use a <font SIZE="-1">TCP</font> socket with <font SIZE="-1">SSL</font> when connecting to a port. The default socket type is <font SIZE="-1">TCP.</font> If <font SIZE="-1">TCPSSL</font> is used you may optionally specify the <font SIZE="-1">SSL/TLS</font> protocol to be used and the <font SIZE="-1">MD5</font> checksum of the server&#8217;s certificate. </p>
<p> The <font SIZE="-1">TCPSSL</font> options are: </p>
<p>TCPSSL[SSLAUTO | SSLV2 | SSLV3 | TLSV1 | TLSV11 | TLSV12][CERTMD5 md5sum]</p>
<p> The default mode is <i></i><font SIZE="-1"><i>SSLAUTO</i></font><i></i> and it will select the method automatically, but for security reasons only <font SIZE="-1">TLS</font> is used, not <font SIZE="-1">SSL.</font> If you need SSLv2 or SSLv3 you have to explicitly select that method using <i></i><font SIZE="-1"><i>SSLV2</i></font><i></i> or <i></i><font SIZE="-1"><i>SSLV3</i></font><i></i> option. </p>
<p> <i>protocol: </i><font SIZE="-1"><i>PROTO</i></font><i>(</i><font SIZE="-1"><i>COL</i></font><i>) protocol</i>. Optionally specify the protocol Monit should speak when a connection is established. At the moment Monit knows how to speak:<br />
&nbsp;<wbr><i>APACHE-STATUS</i><br />
&nbsp;<wbr><i></i><font SIZE="-1"><i>DNS</i></font><i></i><br />
&nbsp;<wbr><i></i><font SIZE="-1"><i>DWP</i></font><i></i><br />
&nbsp;<wbr><i></i><font SIZE="-1"><i>FTP</i></font><i></i><br />
&nbsp;<wbr><i></i><font SIZE="-1"><i>GPS</i></font><i></i><br />
&nbsp;<wbr><i></i><font SIZE="-1"><i>HTTP</i></font><i></i><br />
&nbsp;<wbr><i></i><font SIZE="-1"><i>HTTPS</i></font><i></i><br />
&nbsp;<wbr><i></i><font SIZE="-1"><i>IMAP</i></font><i></i><br />
&nbsp;<wbr><i></i><font SIZE="-1"><i>IMAPS</i></font><i></i><br />
&nbsp;<wbr><i></i><font SIZE="-1"><i>CLAMAV</i></font><i></i><br />
&nbsp;<wbr><i></i><font SIZE="-1"><i>LDAP2</i></font><i></i><br />
&nbsp;<wbr><i></i><font SIZE="-1"><i>LDAP3</i></font><i></i><br />
&nbsp;<wbr><i></i><font SIZE="-1"><i>LMTP</i></font><i></i><br />
&nbsp;<wbr><i></i><font SIZE="-1"><i>MEMCACHE</i></font><i></i><br />
&nbsp;<wbr><i></i><font SIZE="-1"><i>MONGODB</i></font><i></i><br />
&nbsp;<wbr><i></i><font SIZE="-1"><i>MYSQL</i></font><i></i><br />
&nbsp;<wbr><i></i><font SIZE="-1"><i>NNTP</i></font><i></i><br />
&nbsp;<wbr><i></i><font SIZE="-1"><i>NTP3</i></font><i></i><br />
&nbsp;<wbr><i></i><font SIZE="-1"><i>PGSQL</i></font><i></i><br />
&nbsp;<wbr><i></i><font SIZE="-1"><i>POP</i></font><i></i><br />
&nbsp;<wbr><i></i><font SIZE="-1"><i>POPS</i></font><i></i><br />
&nbsp;<wbr><i>POSTFIX-POLICY</i><br />
&nbsp;<wbr><i></i><font SIZE="-1"><i>RADIUS</i></font><i></i><br />
&nbsp;<wbr><i></i><font SIZE="-1"><i>RDATE</i></font><i></i><br />
&nbsp;<wbr><i></i><font SIZE="-1"><i>REDIS</i></font><i></i><br />
&nbsp;<wbr><i></i><font SIZE="-1"><i>RSYNC</i></font><i></i><br />
&nbsp;<wbr><i></i><font SIZE="-1"><i>SIEVE</i></font><i></i><br />
&nbsp;<wbr><i></i><font SIZE="-1"><i>SIP</i></font><i></i><br />
&nbsp;<wbr><i></i><font SIZE="-1"><i>SMTP</i></font><i></i><br />
&nbsp;<wbr><i></i><font SIZE="-1"><i>SMTPS</i></font><i></i><br />
&nbsp;<wbr><i></i><font SIZE="-1"><i>SSH</i></font><i></i><br />
&nbsp;<wbr><i></i><font SIZE="-1"><i>TNS</i></font><i></i><br />
&nbsp;<wbr><i></i><font SIZE="-1"><i>WEBSOCKET</i></font><i></i> </p>
<p> If the target server&#8217;s protocol is not found in this list, simply do not specify the protocol and Monit will use a default connection test. </p>
<p> <i>timeout: [</i><font SIZE="-1"><i>WITH</i></font><i>] </i><font SIZE="-1"><i>TIMEOUT</i></font><i> number </i><font SIZE="-1"><i>SECONDS</i></font><i></i>. Optionally specifies the connect and read timeout for the connection. If Monit cannot connect to the server within this time it will assume that the connection failed and execute the specified action. The default connect timeout is 5 seconds. </p>
<p> <i>retry: </i><font SIZE="-1"><i>RETRY</i></font><i> number</i>. Optionally specifies the number of consecutive retries within the same testing cycle in the case that the connection failed. The default is fail on first error. </p>
<p> <i>action</i> is a choice of &#8220;<font SIZE="-1">ALERT&#8221;, &#8220;RESTART&#8221;, &#8220;START&#8221;, &#8220;STOP&#8221;, &#8220;EXEC&#8221;</font> or &#8220;<font SIZE="-1">UNMONITOR&#8221;.</font> </p>
<p> <i>Specific protocol test options</i> </p>
<p> <font SIZE="-1">GENERIC </font>(<font SIZE="-1">SEND/EXPECT</font>) </p>
<p> If Monit does not support the protocol spoken by the server, you can write your own protocol-test using <i>send</i> and <i>expect</i> strings. The <i></i><font SIZE="-1"><i>SEND</i></font><i></i> statement sends a string to the server port and the <i></i><font SIZE="-1"><i>EXPECT</i></font><i></i> statement compares a string read from the server with the string given in the expect statement. </p>
<p> Syntax: </p>
<p>[{ SEND | EXPECT } &#8220;string&#8221;] +</p>
<p> Monit will send a string as it is, and you <code>must</code> remember to include <font SIZE="-1">CR</font> and <font SIZE="-1">LF</font> in the string sent to the server if the protocol expects such characters to terminate a string (most text based protocols used over Internet do). </p>
<p> Monit will by default read up to 255 bytes from the server and use this string when comparing the <font SIZE="-1">EXPECT</font> string. You can override the default value by using this statement at the top of the Monit configuration file: </p>
<pre>
 SET EXPECTBUFFER &lt;number&gt; [&quot;b&quot;|&quot;kb&quot;]
</pre>
<p> Max value for the expect buffer is 100 kb. For example, to set the expect buffer to read 10 kilobytes: </p>
<pre>
 set expectbuffer 10 kb
</pre>
<p> You can use non-printable characters in a <font SIZE="-1">SEND</font> string if needed. Use the hex notation, 
