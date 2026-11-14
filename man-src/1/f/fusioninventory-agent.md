---
title: "fusioninventory-agent(1)"
name: "fusioninventory-agent"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fusioninventory-agent/"
description: "fusioninventory-agent – FusionInventory agent For Linux/UNIX, Windows and MacOSX"
---

<h2 class="name">NAME</h2>
<p> fusioninventory-agent &#8211; FusionInventory agent For Linux/UNIX, Windows and MacOSX </p>
<h2>SYNOPSIS</h2>
<p> <code>fusioninventory-agent</code> [options] [&#8211;server server|&#8211;local path] </p>
<pre><code>
  Target definition options:
    -s --server=URI                send tasks result to a server
    -l --local=PATH                write tasks results locally
  Target scheduling options:
    --delaytime=LIMIT              maximum delay before first target,
                                     in seconds (3600)
    --lazy                         do not contact the target before
                                   next scheduled time
  Task selection options:
    --list-tasks                   list available tasks and exit
    --no-task=TASK[,TASK]...       do not run given task
    --tasks=TASK1[,TASK]...[,...]  run given tasks in given order
  Inventory task specific options:
    --no-category=CATEGORY         do not list given category items
    --scan-homedirs                scan user home directories (false)
    --scan-profiles                scan user profiles (false)
    --html                         save the inventory as HTML (false)
    -f --force                     always send data to server (false)
    --backend-collect-timeout=TIME timeout for inventory modules
                                     execution (30)
    --additional-content=FILE      additional inventory content file
  Package deployment task specific options:
    --no-p2p                       do not use peer to peer to download
                                     files (false)
  Network options:
    -P --proxy=PROXY               proxy address
    -u --user=USER                 user name for server authentication
    -p --password=PASSWORD         password for server authentication
    --ca-cert-dir=DIRECTORY        CA certificates directory
    --ca-cert-file=FILE            CA certificates file
    --no-ssl-check                 do not check server SSL certificate
                                     (false)
    --timeout=TIME                 connection timeout, in seconds (180)
  Web interface options:
    --no-httpd                     disable embedded web server (false)
    --httpd-ip=IP                  network interface to listen to (all)
    --httpd-port=PORT              network port to listen to (62354)
    --httpd-trust=IP               trust requests without authentication
                                     token (false)
  Logging options:
    --logger=BACKEND               logger backend (stderr)
    --logfile=FILE                 log file
    --logfile-maxsize=SIZE         maximum size of the log file in MB (0)
    --logfacility=FACILITY         syslog facility (LOG_USER)
    --color                        use color in the console (false)
  Configuration options:
    --config=BACKEND                   configuration backend
    --conf-file=FILE                   configuration file
    --conf-reload-interval=&lt;SECONDS&gt;   number of seconds between two
                                         configuration reloadings
  Execution mode options:
    -w --wait=LIMIT                maximum delay before execution,
                                     in seconds
    -d --daemon                    run the agent as a daemon (false)
    --no-fork                      don't fork in background (false)
    -t --tag=TAG                   add given tag to inventory results
    --debug                        debug mode (false)
    --setup                        print the agent setup directories
                                     and exit
    --version                      print the version and exit
    --no-win32-ole-workaround      [win32 only] disable win32 work-around
                                     used to better handle Win32::OLE apis.
                                     !!! Use it at your own risk as you may
                                     experiment perl crash under win32 !!!
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <i>fusioninventory-agent</i> agent is a generic multi-platform agent. It can perform a large array of management tasks, such as local inventory, software deployment or network discovery. It can be used either standalone, or in combination with a compatible server (<font SIZE="-1">OCS, GLPI, OTRS</font>) acting as a centralized control point.</p>
<h2>OPTIONS</h2>
<p> Most of the options are available in a <i>short</i> form and a <i>long</i> form. For example, the two lines below are all equivalent: </p>
<pre>
    % fusioninventory-agent -s localhost
    % fusioninventory-agent --server localhost
</pre>
<h3>Target definition options</h3>
<dl>
<dt><code>-s</code>, <code>&#8211;server</code>=<i></i><font SIZE="-1"><i>URI</i></font><i></i></p>
<dd> Send the results of tasks execution to given server. </p>
<p> If <i></i><font SIZE="-1"><i>URI</i></font><i></i> doesn&#8217;t start with http:// or <a rel="nofollow" href="https://,">https://,</a> the agent assume the parameter is a hostname and rewrite it as: </p>
<pre>
    % --server=<a rel="nofollow" href="http://servername/ocsinventory">http://servername/ocsinventory</a>
</pre>
<p> In general, <font SIZE="-1">OCS</font> Inventory server <font SIZE="-1">URL</font> have this format: </p>
<pre>
    <a rel="nofollow" href="http://servername/ocsinventory">http://servername/ocsinventory</a>
</pre>
<p> and FusionInventory for <font SIZE="-1">GLPI</font> this one: </p>
<pre>
    <a rel="nofollow" href="http://servername/glpi/plugins/fusioninventory/front/plugin_fusioninventory.communication.php">http://servername/glpi/plugins/fusioninventory/front/plugin_fusioninventory.communication.php</a>
</pre>
<p> Multiple values can be specified, using comma as a separator.</p>
<dt><code>-l</code>, <code>&#8211;local</code>=<i></i><font SIZE="-1"><i>PATH</i></font><i></i></p>
<dd> Write the results of tasks execution locally. </p>
<p> Exact behaviour according to given path:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> if <i></i><font SIZE="-1"><i>PATH</i></font><i></i> is a directory, a file will be created therein</p>
<dt>&bull;</p>
<dd> if <i></i><font SIZE="-1"><i>PATH</i></font><i></i> is a file, it will be used directly</p>
<dt>&bull;</p>
<dd> if <i></i><font SIZE="-1"><i>PATH</i></font><i></i> is &#8216;-&#8216;, <font SIZE="-1">STDOUT</font> will be used</dl>
</dl>
<dl>
<dt>
<dd>
<p> Multiple values can be specified, using comma as a separator.</dl>
</dl>
<h3>Target scheduling options</h3>
<dl>
<dt><code>&#8211;delaytime</code>=<i></i><font SIZE="-1"><i>LIMIT</i></font><i></i></p>
<dd> Set an initial delay before the first target, whose value is computed randomly between <font SIZE="-1">LIMIT / 2</font> and <font SIZE="-1">LIMIT</font> seconds. This setting is ignored for server targets after the initial contact, in favor of server-specified parameter (<font SIZE="-1">PROLOG_FREQ</font>).</p>
<dt><code>&#8211;lazy</code></p>
<dd> Do not contact the target before next scheduled time. </p>
<p> This option is only available when the agent is not run as a server.</dl>
<h3>Task selection options</h3>
<dl>
<dt><code>&#8211;list-tasks</code></p>
<dd> List all available tasks, tasks planned for execution and exit</p>
<dt><code>&#8211;no-task</code>=<i></i><font SIZE="-1"><i>TASK</i></font><i></i></p>
<dd> Do not run given task. </p>
<p> Multiple values can be specified, using comma as a separator. See option <i>&#8211;list-tasks</i> for the list of available tasks.</p>
<dt><code>&#8211;tasks</code>=<i></i><font SIZE="-1"><i>TASK</i></font><i></i></p>
<dd> Run given tasks in given order. </p>
<p> Multiple tasks can be specified, using comma as a separator. A task can be specified several times. if &#8216;&#8230;&#8217; is given as last element, all other available tasks are executed. </p>
<p> See option <i>&#8211;list-tasks</i> for the list of available tasks. </p>
<p> Examples : * &#8211;tasks=inventory,deploy,inventory<br />
&nbsp;<wbr>&nbsp;<wbr>First task executed is&nbsp;<wbr>&#8216;inventory&#8217;, second task is&nbsp;<wbr>&#8216;deploy&#8217;, third and last<br />
&nbsp;<wbr>&nbsp;<wbr>task is&nbsp;<wbr>&#8216;inventory&#8217;. </p>
<p> * &#8211;tasks=inventory,deploy,&#8230;<br />
&nbsp;<wbr>&nbsp;<wbr>First executed task is&nbsp;<wbr>&#8216;inventory&#8217;, second task is&nbsp;<wbr>&#8216;deploy&#8217;&nbsp;<wbr>and then all<br />
&nbsp;<wbr>&nbsp;<wbr>other available tasks are executed.</dl>
<h3>Inventory task specific options</h3>
<dl>
<dt><code>&#8211;no-category</code>=<i></i><font SIZE="-1"><i>CATEGORY</i></font><i></i></p>
<dd> Do not list given category items in inventory. </p>
<p> Multiple values can be specified, using comma as a separator. The available categories are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> battery</p>
<dt>&bull;</p>
<dd> controller</p>
<dt>&bull;</p>
<dd> cpu</p>
<dt>&bull;</p>
<dd> drive</p>
<dt>&bull;</p>
<dd> environment</p>
<dt>&bull;</p>
<dd> input</p>
<dt>&bull;</p>
<dd> license</p>
<dt>&bull;</p>
<dd> local_group</p>
<dt>&bull;</p>
<dd> local_user</p>
<dt>&bull;</p>
<dd> lvm</p>
<dt>&bull;</p>
<dd> memory</p>
<dt>&bull;</p>
<dd> modem</p>
<dt>&bull;</p>
<dd> monitor</p>
<dt>&bull;</p>
<dd> network</p>
<dt>&bull;</p>
<dd> printer</p>
<dt>&bull;</p>
<dd> process</p>
<dt>&bull;</p>
<dd> slot</p>
<dt>&bull;</p>
<dd> software</p>
<dt>&bull;</p>
<dd> sound</p>
<dt>&bull;</p>
<dd> storage</p>
<dt>&bull;</p>
<dd> usb</p>
<dt>&bull;</p>
<dd> user</p>
<dt>&bull;</p>
<dd> video</p>
<dt>&bull;</p>
<dd> virtualmachine</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;scan-homedirs</code></p>
<dd> Allow the agent to scan home directories for virtual machines.</p>
<dt><code>&#8211;scan-profiles</code></p>
<dd> Allow the agent to scan user profiles for softwares.</p>
<dt><code>&#8211;html</code></p>
<dd> Save the inventory as <font SIZE="-1">HTML.</font> </p>
<p> This is only used for local inventories.</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd> Send an inventory to the server, even if this last one doesn&#8217;t ask for it.</p>
<dt><code>&#8211;backend-collect-timeout</code>=<i></i><font SIZE="-1"><i>TIME</i></font><i></i></p>
<dd> Timeout for inventory modules execution.</p>
<dt><code>&#8211;additional-content</code>=<i></i><font SIZE="-1"><i>FILE</i></font><i></i></p>
<dd> Additional inventory content file. </p>
<p> This file should be an <font SIZE="-1">XML</font> file, using same syntax as the one produced by the agent.</dl>
<h3>Package deployment task specific options</h3>
<dl>
<dt><code>&#8211;no-p2p</code></p>
<dd> Do not use peer to peer to download files.</dl>
<h3>Server target specific options</h3>
<dl>
<dt><code>-P</code>, <code>&#8211;proxy</code>=<i></i><font SIZE="-1"><i>PROXY</i></font><i></i></p>
<dd> Use <i></i><font SIZE="-1"><i>PROXY</i></font><i></i> as <font SIZE="-1">HTTP</font> proxy. </p>
<p> By default, the agent uses <font SIZE="-1">HTTP_PROXY</font> environment variable.</p>
<dt><code>-u</code> <i></i><font SIZE="-1"><i>USER</i></font><i></i>, <code>&#8211;user</code>=<i></i><font SIZE="-1"><i>USER</i></font><i></i></p>
<dd> Use <i></i><font SIZE="-1"><i>USER</i></font><i></i> for server authentication.</p>
<dt><code>-p</code>, <code>&#8211;password</code>=<i></i><font SIZE="-1"><i>PASSWORD</i></font><i></i></p>
<dd> Use <i></i><font SIZE="-1"><i>PASSWORD</i></font><i></i> for server authentication.</p>
<dt><code>&#8211;ca-cert-dir</code>=<i></i><font SIZE="-1"><i>DIRECTORY</i></font><i></i></p>
<dd> <font SIZE="-1">CA</font> certificates directory.</p>
<dt><code>&#8211;ca-cert-file</code>=<i></i><font SIZE="-1"><i>FILE</i></font><i></i></p>
<dd> <font SIZE="-1">CA</font> certificates file.</p>
<dt><code>&#8211;no-ssl-check</code></p>
<dd> Do not check server <font SIZE="-1">SSL</font> certificate.</p>
<dt><code>&#8211;timeout</code>=<i></i><font SIZE="-1"><i>TIME</i></font><i></i></p>
<dd> Timeout for server connections.</dl>
<h3>Web interface options</h3>
<dl>
<dt><code>&#8211;no-httpd</code></p>
<dd> Disable the embedded web server.</p>
<dt><code>&#8211;httpd-ip</code>=<i></i><font SIZE="-1"><i>IP</i></font><i></i></p>
<dd> The network interface to use for the embedded web server (all).</p>
<dt><code>&#8211;httpd-port</code>=<i></i><font SIZE="-1"><i>PORT</i></font><i></i></p>
<dd> The network port to use for the embedded web server (62354).</p>
<dt><code>&#8211;httpd-trust</code>=<i></i><font SIZE="-1"><i>IP</i></font><i></i></p>
<dd> Trust requests from given addresses without authentication token (false). </p>
<p> For example: &#8220;192.168.0.0/24&#8221;, &#8220;192.168.168.0.5&#8221; or an <font SIZE="-1">IP</font> range like &#8220;20.34.101.207 &#8211; 201.3.9.99&#8221;. Hostnames are also accepted. See Net::IP documentation to get more example. </p>
<p> Multiple values can be specified, using comma as a separator.</dl>
<h3>Logging options</h3>
<dl>
<dt><code>&#8211;logger</code>=<i></i><font SIZE="-1"><i>BACKEND</i></font><i></i></p>
<dd> Logger backend to use. </p>
<p> Multiple values can be specified, using comma as a separator. The available backends are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> stderr: log messages directly in the console.</p>
<dt>&bull;</p>
<dd> file: log messages in a file.</p>
<dt>&bull;</p>
<dd> syslog: log messages through the local syslog server.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Multiple values can be specified, using comma as a separator.</dl>
<dt><code>&#8211;logfile</code>=<i></i><font SIZE="-1"><i>FILE</i></font><i></i></p>
<dd> Log message in <i></i><font SIZE="-1"><i>FILE</i></font><i></i> (implies File logger backend).</p>
<dt><code>&#8211;logfile-maxsize</code>=<i></i><font SIZE="-1"><i>SIZE</i></font><i></i></p>
<dd> Max logfile size in <font SIZE="-1">MB,</font> default is unlimited. When the max size is reached, the file is truncated. This is only useful if there is no log rotation mechanism on the system.</p>
<dt><code>&#8211;logfacility</code>=<i></i><font SIZE="-1"><i>FACILITY</i></font><i></i></p>
<dd> Syslog facility to use (default <font SIZE="-1">LOG_USER</font>).</p>
<dt><code>&#8211;color</code></p>
<dd> Display color on the terminal, when the Stderr backend is used. </p>
<p> This options is ignored on Windows.</dl>
<h3>Configuration options</h3>
<dl>
<dt><code>&#8211;config</code>=<i></i><font SIZE="-1"><i>BACKEND</i></font><i></i></p>
<dd> Configuration backend to use. </p>
<p> The available backends are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> file: read configuration from a file (default anywhere else as Windows).</p>
<dt>&bull;</p>
<dd> registry: read configuration from the registry (default on Windows).</p>
<dt>&bull;</p>
<dd> none: don&#8217;t read any configuration.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;conf-file</code>=<i></i><font SIZE="-1"><i>FILE</i></font><i></i></p>
<dd> Use <i></i><font SIZE="-1"><i>FILE</i></font><i></i> as configuration file (implies file configuration backend).</p>
<dt><code>&#8211;conf-reload-interval</code>=<i></i><font SIZE="-1"><i>SECONDS</i></font><i></i></p>
<dd> <font SIZE="-1">SECONDS</font> is the number of seconds between two configuration reloadings. Default value is 0, which means that configuration is never reloaded. Minimum value is 60. If given value is less than this minimum, it is set to this minimum. If given value is less than 0, it is set to 0.</dl>
<h3>Execution mode options</h3>
<dl>
<dt><code>-w</code> <i></i><font SIZE="-1"><i>LIMIT</i></font><i></i>, <code>&#8211;wait</code>=<i></i><font SIZE="-1"><i>LIMIT</i></font><i></i></p>
<dd> Wait a random delay whose value is computed randomly between 0 and <font SIZE="-1">LIMIT</font> seconds, before execution. This is useful when execution is triggered from some kind of system scheduling on multiple clients, to spread the server load.</p>
<dt><code>-d</code>, <code>&#8211;daemon</code></p>
<dd> Run the agent as a daemon.</p>
<dt><code>&#8211;no-fork</code></p>
<dd> Don&#8217;t fork in background. </p>
<p> This is only useful when running as a daemon.</p>
<dt><code>&#8211;pidfile</code>=<i></i><font SIZE="-1"><i>FILE</i></font><i></i></p>
<dd> Store pid in <i></i><font SIZE="-1"><i>FILE</i></font><i></i>. </p>
<p> This is only useful when running as a daemon.</p>
<dt><code>&#8211;tag</code>=<i></i><font SIZE="-1"><i>TAG</i></font><i></i></p>
<dd> Add the given tag to every inventory results.</p>
<dt><code>&#8211;debug</code></p>
<dd> Turn the debug mode on. You can use the parameter up to 3 times in a row to increase the verbosity (e.g: <code>&#8211;debug &#8211;debug</code>). </p>
<p> Level 3 turns on the debug mode of some external libraries like Net::SSLeay. These messages will only be be printed on <font SIZE="-1">STDERR.</font></p>
<dt><code>&#8211;setup</code></p>
<dd> Print the agent setup directories and exit.</p>
<dt><code>&#8211;version</code></p>
<dd> Print the version and exit. </p>
</dl>
<h2>Index</h2>
