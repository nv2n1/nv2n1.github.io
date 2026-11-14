---
title: "autossh(1)"
name: "autossh"
section: "1"
letter: "a"
url: "/docs/linux/man/1-autossh/"
description: "autossh – monitor and restart ssh sessions"
---

<h2>NAME</h2>
<p> <code>autossh</code> &#8211; monitor and restart ssh sessions</p>
<h2>SYNOPSIS</h2>
<p> <code>autossh</code> [-<code>V</code> ] [-<code>M </code><i>port[:echo_port]</i> ] [-<code>f</code> ] <i>[SSH_OPTIONS]</i></p>
<h2>DESCRIPTION</h2>
<p> <code>autossh</code> is a program to start a copy of ssh and monitor it, restarting it as necessary should it die or stop passing traffic. </p>
<p> The original idea and the mechanism were from rstunnel (Reliable SSH Tunnel). With version 1.2 of <code>autossh</code> the method changed: <code>autossh</code> uses ssh to construct a loop of ssh forwardings (one from local to remote, one from remote to local), and then sends test data that it expects to get back. (The idea is thanks to Terrence Martin.) </p>
<p> With version 1.3, a new method is added (thanks to Ron Yorston): a port may be specified for a remote echo service that will echo back the test data. This avoids the congestion and the aggravation of making sure all the port numbers on the remote machine do not collide. The loop-of-forwardings method remains available for situations where using an echo service may not be possible. </p>
<h2>CONTROLLING SSH</h2>
<h3>SSH exits</h3>
<dl>
<p> <code>autossh</code> tries to distinguish the manner of death of the ssh process it is monitoring and act appropriately. The rules are:</p>
<dl>
<dt><code>1.</code></p>
<dd> If the ssh process exited normally (for example, someone typed &quot;exit&quot; in an interactive session), <code>autossh</code> exits rather than restarting;</p>
<dt><code>2.</code></p>
<dd> If <code>autossh</code> itself receives a SIGTERM, SIGINT, or a SIGKILL signal, it assumes that it was deliberately signalled, and exits after killing the child ssh process;</p>
<dt><code>3.</code></p>
<dd> If <code>autossh</code> itself receives a SIGUSR1 signal, it kills the child ssh process and starts a new one;</p>
<dt><code>4.</code></p>
<dd> Periodically (by default every 10 minutes), <code>autossh</code> attempts to pass traffic on the monitor forwarded port. If this fails, <code>autossh</code> will kill the child ssh process (if it is still running) and start a new one;</p>
<dt><code>5.</code></p>
<dd> If the child ssh process dies for any other reason, <code>autossh</code> will attempt to start a new one.</dl>
</dl>
</dl>
<h3>Startup behaviour</h3>
<p> If the ssh session fails with an exit status of 1 on the very first try, <code>autossh</code></p>
<dl>
<dt><code>1.</code></p>
<dd> will assume that there is some problem with syntax or the connection setup, and will exit rather than retrying;</p>
<dt><code>2.</code></p>
<dd> There is a &quot;starting gate&quot; time. If the first ssh process fails within the first few seconds of being started, <code>autossh</code> assumes that it never made it &quot;out of the starting gate&quot;, and exits. This is to handle initial failed authentication, connection, etc. This time is 30 seconds by default, and can be adjusted (see the AUTOSSH_GATETIME environment variable below). If AUTOSSH_GATETIME is set to 0, then both behaviours are disabled: there is no &quot;starting gate&quot;, and autossh will restart even if ssh fails on the first run with an exit status of 1. The &quot;starting gate&quot; time is also set to 0 when the &#8211;<code>f</code> flag to autossh is used.</dl>
<h3>Continued failures</h3>
<p> If the ssh connection fails and attempts to restart it fail in quick succession, <code>autossh</code> will start delaying its attempts to restart, gradually backing farther and farther off up to a maximum interval of the <code>autossh</code> poll time (usually 10 minutes). <code>autossh</code> can be &quot;prodded&quot; to retry by signalling it, perhaps with SIGHUP (&quot;kill -HUP&quot;). </p>
<h3>Connection setup</h3>
<p> As connections must be established unattended, the use of <code>autossh</code> requires that some form of automatic authentication be set up. The use of RSAAuthentication with ssh-agent is the recommended method. The example wrapper script attempts to check if there is an agent running for the current environment, and to start one if there isn&#8217;t. </p>
<p> It cannot be stressed enough that you must make sure ssh works on its own, that you can set up the session you want before you try to run it under <code>autossh</code> </p>
<p> If you are tunnelling and using an older version of ssh that does not support the &#8211;<code>N</code> flag, you should upgrade (your version has security flaws). If you can&#8217;t upgrade, you may wish to do as rstunnel does, and give ssh a command to run, such as &quot;sleep 99999999999&quot;.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-M </code><i>port[:echo_port]</i></p>
<dd> specifies the base monitoring port to use. Without the echo port, this port and the port immediately above it ( <i>port</i> + 1) should be something nothing else is using. <code>autossh</code> will send test data on the base monitoring port, and receive it back on the port above. For example, if you specify &quot;-M 20000&quot;, <code>autossh</code> will set up forwards so that it can send data on port 20000 and receive it back on 20001. </p>
<p> Alternatively, a port for a remote echo service may be specified. This should be port 7 if you wish to use the standard inetd echo service. When an echo port is specified, only the specified monitor port is used, and it carries the monitor message in both directions. </p>
<p> Many people disable the echo service, or even disable inetd, so check that this service is available on the remote machine. Some operating systems allow one to specify that the service only listen on the localhost (loopback interface), which would suffice for this use. </p>
<p> The echo service may also be something more complicated: perhaps a daemon that monitors a group of ssh tunnels. </p>
<p> Setting the monitor port to 0 turns the monitoring function off, and autossh will only restart ssh upon ssh&#8217;s exit. For example, if you are using a recent version of OpenSSH, you may wish to explore using the <code>ServerAliveInterval</code> and <code>ServerAliveCountMax</code> options to have the SSH client exit if it finds itself no longer connected to the server. In many ways this may be a better solution than the monitoring port.</p>
<dt><code>-f</code></p>
<dd> causes autossh to drop to the background before running ssh. The &#8211;<code>f </code> flag is stripped from arguments passed to ssh. Note that there is a crucial a difference between &#8211;<code>f </code> with autossh, and &#8211;<code>f</code> with ssh: when used with <code>autossh</code> ssh will be unable to ask for passwords or passphrases. When &#8211;<code>f</code> is used, the &quot;starting gate&quot; time (see AUTOSSH_GATETIME) is set to 0.</p>
<dt><code>-V </code></p>
<dd> causes <code>autossh</code> to display its version number and exit.</dl>
<h2>ENVIRONMENT</h2>
<p> Other than the flag to set the connection monitoring port, <code>autossh</code> uses environment variables to control features. ssh seems to be still collecting letters for options, and this seems the easiest way to avoid collisions.</p>
<dl>
<dt><code>AUTOSSH_DEBUG</code></p>
<dd> If this variable is set, the logging level is set to to LOG_DEBUG, and if the operating system supports it, syslog is set to duplicate log entries to stderr.</p>
<dt><code>AUTOSSH_FIRST_POLL</code></p>
<dd> Specifies the time to wait before the first connection test. Thereafter the general poll time is used (see AUTOSSH_POLL below).</p>
<dt><code>AUTOSSH_GATETIME</code></p>
<dd> Specifies how long ssh must be up before we consider it a successful connection. The default is 30 seconds. Note that if AUTOSSH_GATETIME is set to 0, then not only is the gatetime behaviour turned off, but autossh also ignores the first run failure of ssh. This may be useful when running autossh at boot.</p>
<dt><code>AUTOSSH_LOGLEVEL</code></p>
<dd> Specifies the log level, corresponding to the levels used by syslog; so 0-7 with 7 being the chattiest.</p>
<dt><code>AUTOSSH_LOGFILE</code></p>
<dd> Specifies that <code>autossh</code> should use the named log file, rather than syslog.</p>
<dt><code>AUTOSSH_MAXLIFETIME</code></p>
<dd> Sets the maximum number of seconds that the program should run. Once the number of seconds has been passed, the ssh child will be killed and the program will exit.</p>
<dt><code>AUTOSSH_MAXSTART</code></p>
<dd> Specifies how many times ssh should be started. A negative number means no limit on the number of times ssh is started. The default value is -1.</p>
<dt><code>AUTOSSH_MESSAGE</code></p>
<dd> Append message to echo message sent when testing connections.</p>
<dt><code>AUTOSSH_NTSERVICE </code></p>
<dd> (Cygwin only.) When set to &quot;yes&quot; , autossh sets up to run as an NT service under cygrunsrv. This adds the -N flag for ssh if not already set, sets the log output to stdout, and changes the behaviour on ssh exit so that it will restart even on a normal exit.</p>
<dt><code>AUTOSSH_PATH</code></p>
<dd> Specifies the path to the ssh executable, in case it is different than the path compiled in.</p>
<dt><code>AUTOSSH_PIDFILE</code></p>
<dd> Write autossh pid to specified file.</p>
<dt><code>AUTOSSH_POLL</code></p>
<dd> Specifies the connection poll time in seconds; default is 600 seconds. Unless AUTOSSH_FIRST_POLL is used, the first poll time will set to match the poll time. If the poll time is less than twice the network timeouts (default 15 seconds) the network timeouts will be adjusted downward to 1/2 the poll time.</p>
<dt><code>AUTOSSH_PORT</code></p>
<dd> Sets the connection monitoring port. Mostly in case ssh appropriates -M at some time. But because of this possible use, AUTOSSH_PORT overrides the -M flag. A value of 0 turns the monitoring function off.</dl>
<h2>AUTHOR</h2>
<p> <code>autossh</code> was written by Carson Harding.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-ssh/">ssh</a>(1), ssh-add1, ssh-agent1, ssh-keygen1, <a href="/docs/linux/man/1-cygrunsrv/">cygrunsrv</a>(1). </p>
<h2>Index</h2>
