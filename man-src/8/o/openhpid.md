---
title: "openhpid(8)"
name: "openhpid"
section: "8"
letter: "o"
url: "/docs/linux/man/8-openhpid/"
description: "openhpid – HPI instance to which multiple clients can connect."
---

<p>openhpid &#8211; HPI instance to which multiple clients can connect.</p>
<h2>Synopsis</h2>
<p>openhpid -c config_file [<font SIZE="-1">OPTION</font>]</p>
<h2>Description</h2>
<p>The OpenHPI daemon runs as a background process and accepts connections from remote clients that invoke <font SIZE="-1">HPI</font> function calls. The daemon wraps the OpenHPI library with a sockets-based <font SIZE="-1">API</font> that is archicture neutral for all types of clients. </p>
<p> When you run the daemon, the standard method for locating the OpenHPI configuration file is used. However, the daemon will accept a configuration file as a command line option (-c) to override the default file. </p>
<p> A command option (-p) or environment variable determines the port number the daemon will listen on for client connections. The default port is 4743. </p>
<p> The daemon creates a <font SIZE="-1">PID</font> file in the /var/run subdirectory. This directory is only writable by the root user. Thus the daemon will fail when run as a normal user if the <font SIZE="-1">PID</font> file location is not overridden. To override the <font SIZE="-1">PID</font> file location you can use the -f command line option. </p>
<p> The client and the daemon do not have to be on the same hardware architecture. The daemon could be running on a P-series processor and the client running on an x86-series processor. The client library and daemon use a marshaling technique to resolve architecture and structure padding conflicts. The user does not need to concern themselves with architectureal differences between the client and daemon. The one exception to this rule is 64-bit architectures. The client and daemon currently cannot resolve differences between 32-bit and 64-bit architectures.</p>
<h2>Options</h2>
<dl>
<dt><code>-c</code>, <code>&#8211;cfg</code>=<i>conf_file</i></p>
<dd>Sets path/name of the configuration file. This option is required unless the environment variable <font SIZE="-1">OPENHPI_CONF</font> has been set to a valid configuration file.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>This option causes the daemon to display verbose messages. This option is optional.</p>
<dt><code>-b</code>, <code>&#8211;bind</code>=<i>bind_address</i></p>
<dd>Bind address for the daemon socket. Also bind address can be specified with <font SIZE="-1">OPENHPI_DAEMON_BIND_ADDRESS</font> environment variable. No bind address is used by default.</p>
<dt><code>-p</code>, <code>&#8211;port</code>=<i>port</i></p>
<dd>Overrides the default listening port (4743) of the daemon. The option is optional.</p>
<dt><code>-f</code>, <code>&#8211;pidfile</code>=<i>pidfile</i></p>
<dd>Overrides the default path/name for the daemon pid file. The option is optional.</p>
<dt><code>-s</code>, <code>&#8211;timeout</code>=<i>seconds</i></p>
<dd>Overrides the default socket read timeout of 30 minutes. The option is optional.</p>
<dt><code>-t</code>, <code>&#8211;threads</code>=<i>threads</i></p>
<dd>Sets the maximum number of connection threads. The default is umlimited. The option is optional.</p>
<dt><code>-n</code>, <code>&#8211;nondaemon</code></p>
<dd>Forces the code to run as a foreground process and <font SIZE="-1">NOT</font> as a daemon. The default is to run as a daemon. The option is optional.</p>
<dt><code>-6</code>, <code>&#8211;ipv6</code></p>
<dd>The daemon will try to bind IPv6 socket.</p>
<dt><code>-4</code>, <code>&#8211;ipv4</code></p>
<dd>The daemon will try to bind IPv4 socket (default). IPv6 option takes precedence over IPv6 option.</p>
<dt><code>-4 -6</code></p>
<dd>The daemon will try to bind IPv4 or IPv6 socket.</dl>
<h2>Environmental Variables</h2>
<p>All of these environment variables can instead be set in the openhpi.conf configuration file, except for <font SIZE="-1">OPENHPI_DAEMON_PORT</font> and <font SIZE="-1">OPENHPI_CONF.</font></p>
<dl>
<dt><font SIZE="-1"><code>OPENHPI_DAEMON_PORT</code></font>=PORT_NUMBER</p>
<dd>The port number the host will listen on for clent connections. Default port is 4743.</p>
<dt><font SIZE="-1"><code>OPENHPI_LOG_ON_SEV</code></font></p>
<dd>Valus can be one of: <font SIZE="-1">CRITICAL,MAJOR,MINOR,INFORMATIONAL,OK,DEBUG.</font> Events of this severity or higher will be logged to the domain event log. The default is <font SIZE="-1">MINOR.</font></p>
<dt><font SIZE="-1"><code>OPENHPI_EVT_QUEUE_LIMIT</code></font>=NUMBER</p>
<dd>Maximum number of events allowed in a subscribed session&#8217;s queue. Default is 10000.</p>
<dt><font SIZE="-1"><code>OPENHPI_DEL_SIZE_LIMIT</code></font>=NUMBER</p>
<dd>Maximum number of events allowed in the domain event log. Default is 10000</p>
<dt><font SIZE="-1"><code>OPENHPI_DEL_SAVE</code></font></p>
<dd>Set to <font SIZE="-1">YES</font> to persist the domain event logs to disk. They will be loaded in case the daemon restarts. Default is <font SIZE="-1">NO.</font></p>
<dt><font SIZE="-1"><code>OPENHPI_DAT_SIZE_LIMIT</code></font>=NUMBER</p>
<dd>Maximum number of alarms allowed in the domain alarm table. Default is unlimited.</p>
<dt><font SIZE="-1"><code>OPENHPI_DAT_USER_LIMIT</code></font>=NUMBER</p>
<dd>Maximum number of user alarms allowed in the domain alarm table. Default is unlimited.</p>
<dt><font SIZE="-1"><code>OPENHPI_DAT_SAVE</code></font></p>
<dd>Set to <font SIZE="-1">YES</font> to persist the domain alarm tables to disk. They will be loaded in case the daemon restarts. Default is <font SIZE="-1">NO.</font></p>
<dt><font SIZE="-1"><code>OPENHPI_PATH</code></font>=&quot;/path/to/plugins:/another/path/to/plugins&quot;</p>
<dd>This is a colon delimited list of directories used when searching for an OpenHPI plugin to load. The default is <tt>$prefix</tt>/lib/openhpi.</p>
<dt><font SIZE="-1"><code>OPENHPI_VARPATH</code></font>=&quot;/path/to/dir&quot;</p>
<dd>This sets the directory used to store openhpi internal data. The domain event logs and alarm tables are saved there (if configured to) along with resource <font SIZE="-1">ID</font> to entity path mappings. Default is <tt>$prefix</tt>/var/lib/openhpi.</p>
<dt><font SIZE="-1"><code>OPENHPI_CONF</code></font>=&quot;/path/to/configurationg/file&quot;</p>
<dd>This is another way of telling the daemon where to find the configuration file.</dl>
<h2>See Also</h2>
<p>The following man pages may also be of interest</p>
<dl>
<dt><code>openhpi</code></p>
<dd>General information about OpenHPI</dl>
<h2>Authors</h2>
<p>Authors of this man page: </p>
<pre> Renier Morales (renier [at] openhpi.org)
 Anton Pak (avpak [at] users.sourceforge.net)</pre>
