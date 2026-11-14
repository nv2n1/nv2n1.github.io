---
title: "gkrellmd(1)"
name: "gkrellmd"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gkrellmd/"
description: "gkrellmd – The GNU Krell Monitors Server"
---

<h2 class="name">NAME</h2>
<p> gkrellmd &#8211; The GNU Krell Monitors Server</p>
<h2>SYNOPSIS</h2>
<p> <code>gkrellmd</code> [ <code>&#8211;help</code> ] [ <code>&#8211;verbose</code> ] [ <code>-u</code> | <code>&#8211;update-hz</code> f ] [ <code>-m</code> | <code>&#8211;max-clients</code> N ] [ <code>-A</code> | <code>&#8211;address</code> server_address ] [ <code>-P</code> | <code>&#8211;port</code> server_port ] [ <code>-a</code> | <code>&#8211;allow-host</code> hostname ] [ <code>-d</code> | <code>&#8211;detach</code> ] [ <code>-p</code> | <code>&#8211;plugin</code> name ] [ <code>-pe</code> | <code>&#8211;plugin-enable</code> name ] [ <code>&#8211;plist</code> ] [ <code>&#8211;plog</code> ] | <code>&#8211;logfile</code> path ] | <code>&#8211;syslog</code> ] [ <code>-U</code> | <code>&#8211;user</code> username ] [ <code>-G</code> | <code>&#8211;group</code> groupname ] [ <code>&#8211;pidfile</code> path ] [ <code>&#8211;inet-interval</code> seconds ] [ <code>&#8211;io-timeout</code> seconds ] [ <code>&#8211;reconnect-timeout</code> seconds ] [ <code>&#8211;mailbox</code> mbox_path ] [ <code>&#8211;net-timer</code> net_interface ] [ <code>&#8211;mbmon-port</code> number ] </p>
<h2>DESCRIPTION</h2>
<p> <code>gkrellmd</code> Listens for connections from <code>gkrellm</code> clients. When a <code>gkrellm</code> client connects to a <code>gkrellmd</code> server all builtin monitors collect their data from the server. However, the <code>gkrellm</code> process is running on the local machine, so plugins enabled in <code>gkrellm</code> will collect data from the local context unless the plugin is client/server capable and has a <code>gkrellmd</code> plugin counterpart which is installed and enabled on the server. Enabling a <code>gkrellmd</code> plugin installed on a server requires adding a <i>plugin-enable</i> line to a <i>gkrellmd.conf</i> file. </p>
<p> Any command launching from a gkrellm client will run commands on the local machine. If you want to execute commands on the server, the client side commands can use ssh. </p>
<p> There is no support for file system mounting on the machine where the <code>gkrellmd</code> server is running. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h &#8211;help</code></p>
<dd> Displays usage information and exits.</p>
<dt><code>-v &#8211;version</code></p>
<dd> Prints <code>gkrellmd</code> version and exits.</p>
<dt><code>-V &#8211;verbose</code></p>
<dd> Prints connection progress.</p>
<dt><code>-u, &#8211;update-hz f</code></p>
<dd> Sets the data update frequency in samples per second for the server. This is independent of and should be less than the <code>gkrellm</code> client update rate. The rate can be from 1 to 10 and should be lower to minimize network traffic. A value of not much more than 1/2 the client update rate is best where it is not important to minimize network traffic.</p>
<dt><code>-m, &#8211;max-clients N</code></p>
<dd> Sets the maximum number of simultaneous clients allowed to connect to the server.</p>
<dt><code>-A, &#8211;address server_address</code></p>
<dd> Use <i>server_address</i> for the network connection.</p>
<dt><code>-P, &#8211;port server_port</code></p>
<dd> Use <i>server_port</i> for the network connection.</p>
<dt><code>-a, &#8211;allow-host hostname</code></p>
<dd> Specify hosts which are allowed to connect. Multiple <i>allow-host</i> arguments may be given. If no hosts are specified on the command line or in a gkrellmd.conf file, then all hosts are allowed to connect. The <i>hostname</i> argument may be a text name or a IPv4 or IPv6 dotted notation. For IPv4, the simple subnet pattern x.y.z.* may be used. Also, if <i>hostname</i> is the keyword <code>ALL</code> then all hosts are allowed. This option is additive and specified hosts will be added to the hostnames listed in gkrellmd.conf files unless the <i>&#8211;clear-hosts</i> option is given first. </p>
<dt><code>-p, &#8211;plugin name</code></p>
<dd> For plugin development convenience, load and enable the command line specified plugin to avoid repeated install steps in the development cycle. See the README from the gkrellm <i>demo5</i> for more information on gkrellmd plugin development. Requires at least gkrellmd version 2.2.0.</p>
<dt><code>-pe, &#8211;plugin-enable name</code></p>
<dd> Specify an installed plugin to enable (this is probably more convenient to specify in a gkrellmd.conf file). Requires at least gkrellmd version 2.2.0. </p>
<dt><code>-plist</code></p>
<dd> Output a list of plugins which are installed and available to enable and exit. Requires at least gkrellmd version 2.2.0.</p>
<dt><code>-plog</code></p>
<dd> Output a log of the plugin install process. When requesting a log, the <i>&#8211;detach</i> option will have no effect. Requires at least gkrellmd version 2.2.0.</p>
<dt><code>-l, &#8211;logfile path</code></p>
<dd> Enable sending error and debugging messages to a log file.</p>
<dt><code>&#8211;syslog</code></p>
<dd> Enable sending logging messages to the syslog file. </p>
<dt><code>-c, &#8211;clear-hosts</code></p>
<dd> Clears the current list of allowed hosts. Use this before any <i>&#8211;allow-host</i> arguments if you want command line allowed hosts to override and not be additive to those specified in gkrellmd.conf files.</p>
<dt><code>-d, &#8211;detach</code></p>
<dd> Runs gkrellmd in the background and detaches from the terminal.</p>
<dt><code>-U, &#8211;user username</code></p>
<dd> Changes user to <i>username</i> after startup. Useful if you want to run gkrellmd as root, but set it to run with another privileges; typically as the <i>nobody</i> user.</p>
<dt><code>-G, &#8211;group groupname</code></p>
<dd> Changes group to <i>groupname</i> after startup.</p>
<dt><code>&#8211;pidfile path</code></p>
<dd> Create a PID file for the running gkrellmd. Typically, <i>path</i> would be <i>/var/run/gkrellmd.pid.</i> Default is no PID file.</p>
<dt><code>&#8211;inet-interval seconds</code></p>
<dd> The Internet monitor defaults to reading TCP connections once per second. However, for Linux SMP kernels where reading /proc/net/tcp causes high cpu usage, the <i>inet-interval</i> may be set to 1-20 seconds to slow down /proc/net/tcp reads. Or set it to 0 to totally disable the Internet monitor. Requires at least gkrellmd version 2.1.8.</p>
<dt><code>&#8211;io-timeout seconds</code></p>
<dd> Configure gkrellm clients to disconnect from a gkrellmd server if there is an <i>io-timeout</i> interval where the client receives no input from the server. Use this for conditions where gkrellmd may be ungracefully terminated such that socket connections are not closed. Minimum is 2 (less than 2 for no I/O disconnecting and is the default). Requires at least 2.1.8 versions of both gkrellmd and gkrellm.</p>
<dt><code>&#8211;reconnect-timeout seconds</code></p>
<dd> Configure gkrellm clients to attempt automatic reconnects to a gkrellmd server every <i>reconnect-timeout</i> seconds after a disconnected state is detected. Disconnected states are created by normal gkrellmd shutdowns or by an expiring <i>io-timeout.</i> Minimum is 2 (less than 2 for no automatic reconnecting and is the default). Requires at least 2.1.8 versions of both gkrellmd and gkrellm.</p>
<dt><code>&#8211;mailbox mbox_path</code></p>
<dd> Check the server side mailbox <i>mbox_path</i> and send mail counts to connected gkrellm clients. Mailbox types may be mbox, Maildir, and MH mail. Requires at least 2.1.11 versions of both gkrellmd and gkrellm. </p>
<dt><code>&#8211;net-timer net_interface</code></p>
<dd> Configure gkrellmd to send the connect time for a network interface to all clients to be displayed in the client gkrellm timer button monitor display. If this is done, the client gkrellm timer button can still execute commands on the client, but the button will not affect the timer display. If you want the client timer button to execute commands on the server, your timer button commands can use ssh. So set this if your server box has say a ppp0 or ippp0 connection and you want to monitor its connect time. Requires at least 2.2.7 versions of both gkrellmd and gkrellm. </p>
<dt><code>&#8211;mbmon-port port_number</code></p>
<dd> If the mbmon daemon is running when gkrellmd is started, gkrellmd will connect to mbmon using the given port_number and send mbmon sensor data to connected gkrellm clients. The mbmon daemon should have been started using the same port number like so: <code>mbmon -r -P port_number</code> </p>
</dl>
<h2>EXAMPLE</h2>
<p> On the server machine where gkrellmd is installed, copy the sample <i>gkrellmd.conf</i> file from the <i>server</i> subdirectory of the <code>gkrellm</code> source tarball to one of the <i>gkrellmd.conf</i> locations listed in the <code>FILES</code> section and edit it to set your preferences or to enable plugins. Probably don&#8217;t set the <i>detached</i> option until you are happy with the configuration. Run: <code>gkrellmd</code> </p>
<p> On a client machine, run: <code>gkrellm -s server-machine-name</code> </p>
<p> Configure the client gkrellm in its graphical configuration window as you wish, and that&#8217;s all there is to it. Of course, if you don&#8217;t use the default <code>gkrellmd</code> <i>port</i> number you will have to supply an appropriate <i>port</i> argument to the client <code>gkrellm.</code> </p>
<p> Available plugins will be installed in the <i>plugins-gkrellmd</i> directory locations listed in the <code>FILES</code> section. You may test enable any of these plugins with the <i>-pe</i> option, but for permanent enabling you should add a <i>plugin-enable</i> line to any <i>gkrellmd.conf</i> file listed in the <code>FILES</code> section. Run <code>gkrellmd -plist</code> to see a list of all installed plugins and run <code>gkrellmd -plog</code> to see a log of the plugin install process. </p>
<h2>FILES</h2>
<dl>
<dt><i>/etc/gkrellmd.conf</i></p>
<dd> System server config which is read first. The config file may contain lines similar to the command line args. For example:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>allow-host localhost</code></p>
<dd>
<dt><code>allow-host 127.0.0.1</code></p>
<dd>
<dt><code>allow-host 192.168.0.*</code></p>
<dd>
<dt><code>port 19150</code></p>
<dd>
<dt><code>max-clients 2</code></p>
<dd>
<dt><code>update-hz 2</code></p>
<dd>
<dt><code>detach</code></p>
<dd>
<dt><code>io-timeout 5</code></p>
<dd>
<dt><code>reconnect-timeout 5</code></p>
<dd>
<dt><code>plugin-enable gkrelltopd</code></p>
<dd>
</dl>
<p> With the exception of <i>&#8211;allow-host,</i> command line args will override options in gkrellmd.conf files. </p>
</dl>
<dt><i>/usr/local/etc/gkrellmd.conf</i></p>
<dd> Local server config file which is read second.</p>
<dt><i>~/.gkrellmd.conf</i></p>
<dd> User server config file which is read last.</p>
<dt><i>~/.gkrellm2/plugins-gkrellmd</i></p>
<dd> User server plugin directory.</p>
<dt><i>/usr/lib64/gkrellm2/plugins-gkrellmd</i></p>
<dd> System wide server plugin directory.</p>
<dt><i>/usr/local/lib64/gkrellm2/plugins-gkrellmd</i></p>
<dd> Local server plugin directory. </p>
</dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Bill Wilson &lt;billw [at] gkrellm.net&gt;. <a rel="nofollow" href="http://www.gkrellm.net/">http://www.gkrellm.net/</a> </p>
<h2>Index</h2>
