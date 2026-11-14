---
title: "virt-admin(1)"
name: "virt-admin"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virt-admin/"
description: "virt-admin – daemon administration interface"
---

<h2 class="name">NAME</h2>
<p> virt-admin &#8211; daemon administration interface </p>
<h2>SYNOPSIS</h2>
<p> <code>virt-admin</code> [<i></i><font SIZE="-1"><i>OPTION</i></font><i></i>]&#8230; [<i></i><font SIZE="-1"><i>COMMAND_STRING</i></font><i></i>] </p>
<p> <code>virt-admin</code> [<i></i><font SIZE="-1"><i>OPTION</i></font><i></i>]&#8230; <i></i><font SIZE="-1"><i>COMMAND</i></font><i></i> [<i></i><font SIZE="-1"><i>ARG</i></font><i></i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> The <code>virt-admin</code> program is the main administration interface for modifying the libvirt daemon configuration at runtime, changing daemon behaviour as well as for monitoring and managing all clients connected to the daemon. </p>
<p> The basic structure of most virt-admin usage is: </p>
<pre><code>
virt - admin[OPTION]...&lt;command&gt;[ARG]...
</code></pre>
<p> Where <i>command</i> is one of the commands listed below. </p>
<p> The <code>virt-admin</code> program can be used either to run one <i></i><font SIZE="-1"><i>COMMAND</i></font><i></i> by giving the command and its arguments on the shell command line, or a <i></i><font SIZE="-1"><i>COMMAND_STRING</i></font><i></i> which is a single shell argument consisting of multiple <i></i><font SIZE="-1"><i>COMMAND</i></font><i></i> actions and their arguments joined with whitespace, and separated by semicolons between commands. Within <i></i><font SIZE="-1"><i>COMMAND_STRING</i></font><i></i>, virt-admin understands the same single, double, and backslash escapes as the shell, although you must add another layer of shell escaping in creating the single shell argument. If no command is given in the command line, <code>virt-admin</code> will then start a minimal interpreter waiting for your commands, and the <code>quit</code> command will then exit the program. </p>
<p> The <code>virt-admin</code> program understands the following <i></i><font SIZE="-1"><i>OPTIONS</i></font><i></i>.</p>
<dl>
<dt><code>-c</code>, <code>&#8211;connect</code> <i></i><font SIZE="-1"><i>URI</i></font><i></i></p>
<dd> Connect to the specified <i></i><font SIZE="-1"><i>URI</i></font><i></i>, as if by the <code>connect</code> command, instead of the default connection.</p>
<dt><code>-d</code>, <code>&#8211;debug</code> <i></i><font SIZE="-1"><i>LEVEL</i></font><i></i></p>
<dd> Enable debug messages at integer <i></i><font SIZE="-1"><i>LEVEL</i></font><i></i> and above. <i></i><font SIZE="-1"><i>LEVEL</i></font><i></i> can range from 0 to 4 (default). See the documentation of <font SIZE="-1"><code>VIRT_ADMIN_DEBUG</code></font> environment variable below for the description of each <i></i><font SIZE="-1"><i>LEVEL</i></font><i></i>.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Ignore all other arguments, and behave as if the <code>help</code> command were given instead.</p>
<dt><code>-l</code>, <code>&#8211;log</code> <i></i><font SIZE="-1"><i>FILE</i></font><i></i></p>
<dd> Output logging details to <i></i><font SIZE="-1"><i>FILE</i></font><i></i>.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> Avoid extra informational messages.</p>
<dt><code>-v</code>, <code>&#8211;version[=short]</code></p>
<dd> Ignore all other arguments, and prints the version of the libvirt library virt-admin is coming from</p>
<dt><code>-V</code>, <code>&#8211;version=long</code></p>
<dd> Ignore all other arguments, and prints the version of the libvirt library virt-admin is coming from.</dl>
<h2>NOTES</h2>
<p> Running <code>virt-admin</code> requires root privileges due to the communications channels used to talk to the daemon. Consider changing the <i>unix_sock_group</i> ownership setting to grant access to specific set of users or modifying <i>unix_sock_rw_perms</i> permissions. Daemon configuration file provides more information about setting permissions.</p>
<h2>GENERIC COMMANDS</h2>
<p> The following commands are generic.</p>
<dl>
<dt><code>help</code> [<i>command-or-group</i>]</p>
<dd> This lists each of the virt-admin commands. When used without options, all commands are listed, one per line, grouped into related categories, displaying the keyword for each group. </p>
<p> To display detailed information for a specific command, use its name as the option.</p>
<dt><code>quit</code>, <code>exit</code></p>
<dd> quit this interactive terminal</p>
<dt><code>version</code></p>
<dd> Will print out the version info about which libvirt library was this client built from. As opposed to <i>virsh</i> client, the output already includes the version of the daemon. </p>
<p> <code>Example</code> </p>
<pre>
 $ virt-admin version
 Compiled against library: libvirt 1.2.21
 Using library: libvirt 1.2.21
 Running against daemon: 1.2.20
</pre>
<dt><code>cd</code> [<i>directory</i>]</p>
<dd> Will change current directory to <i>directory</i>. The default directory for the <code>cd</code> command is the home directory or, if there is no <i></i><font SIZE="-1"><i>HOME</i></font><i></i> variable in the environment, the root directory. </p>
<p> This command is only available in interactive mode.</p>
<dt><code>pwd</code></p>
<dd> Will print the current directory.</p>
<dt><code>connect</code> [<i></i><font SIZE="-1"><i>URI</i></font><i></i>]</p>
<dd> (Re)-Connect to a daemon&#8217;s administrating server. The <i></i><font SIZE="-1"><i>URI</i></font><i></i> parameter specifies how to connect to the administrating server. If <i></i><font SIZE="-1"><i>LIBVIRT_ADMIN_DEFAULT_URI</i></font><i></i> or <i>uri_default</i> (see below) were set, <i>connect</i> is automatically issued every time a command that requires an active connection is executed. Note that this only applies if there is no connection at all or there is an inactive one. </p>
<p> To find the currently used <font SIZE="-1">URI,</font> check the <i>uri</i> command documented below. </p>
<p> For remote access see the documentation page at &lt;<a rel="nofollow" href="http://libvirt.org/uri.html">http://libvirt.org/uri.html</a>&gt; on how to make URIs.</p>
<dt><code>uri</code></p>
<dd> Prints the administrating server canonical <font SIZE="-1">URI,</font> can be useful in shell mode. If no <i>uri</i> was specified, neither <i></i><font SIZE="-1"><i>LIBVIRT_ADMIN_DEFAULT_URI</i></font><i></i> environment variable nor <i>uri_default</i> option (libvirt-admin.conf) were set, libvirtd:///system is used.</dl>
<h2>SERVER COMMANDS</h2>
<p> Following commands manipulate daemon&#8217;s server internal configuration. The <i>server</i> is specified by its name.</p>
<dl>
<dt><code>srv-threadpool-info</code> <i>server</i></p>
<dd> Retrieve server&#8217;s threadpool attributes. These attributes include:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>minWorkers</i> as the bottom limit to the number of active workers,</p>
<dd>
<dt><i>maxWorkers</i> as the top limit to the number of active workers,</p>
<dd>
<dt><i>nWorkers</i> as the current number of workers in the threadpool,</p>
<dd>
<dt><i>freeWorkers</i> as the current number of workers available for a task,</p>
<dd>
<dt><i>prioWorkers</i> as the current number of priority workers in the threadpool, and</p>
<dd>
<dt><i>jobQueueDepth</i> as the current depth of threadpool&#8217;s job queue.</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd>
<p> <code>Background</code> </p>
<p> Each daemon server utilizes a threadpool to accomplish tasks requested by clients connected to it. Every time a client request arrives to the server, it checks whether there is a worker available to accomplish the given task or it should create a new worker for the job (rather than being destroyed, the worker becomes free once the task is finished). Creating new workers, however, is only possible when the current number of workers is still below the configured upper limit. </p>
<p> In addition to these &#8216;standard&#8217; workers, a threadpool also contains a special set of workers called <i>priority</i> workers. Their purpose is to perform tasks that, unlike tasks carried out by normal workers, are within libvirt&#8217;s full control and libvirt guarantees that such a task cannot hang, thus will always finish. An example of such a task this would be destroying a domain:<br />
&nbsp;<wbr>$&nbsp;<wbr>virsh destroy&nbsp;<wbr>&lt;domain&gt;.</dl>
<dt><code>srv-threadpool-set</code> <i>server</i> [<i>&#8211;min-workers</i> <code>count</code>] [<i>&#8211;max-workers</i> <code>count</code>] [<i>&#8211;priority-workers</i> <code>count</code>]</p>
<dd> Change threadpool attributes on a server. Only a fraction of all attributes as described in <i>srv-threadpool-info</i> is supported for the setter.</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>&#8211;min-workers</i></p>
<dd> The bottom limit to number of active workers in a threadpool.</p>
<dt><i>&#8211;max-workers</i></p>
<dd> The upper limit to number of active workers in a threadpool. If used in combination with option <i>&#8211;min-workers</i>, the value for the upper limit has to be greater than the value for the bottom limit, otherwise the command results in an error.</p>
<dt><i>&#8211;priority-workers</i></p>
<dd> The current number of active priority workers in a threadpool.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>srv-clients-list</code> <i>server</i></p>
<dd> Print a table showing the list of clients connected to &lt;server&gt;, also providing information about transport type used on client&#8217;s connection (supported transports include <code>unix</code>, <code>tcp</code>, and <code>tls</code>), as well as providing information about client&#8217;s connection time (system local time is used).</p>
<dt><code>srv-clients-info</code> <i>server</i></p>
<dd> Get information about the current setting of limits regarding connections of new clients. This information comprises of the limits to the maximum number of clients connected to <i>server</i>, maximum number of clients waiting for authentication, in order to be connected to the server, as well as the current runtime values, more specifically, the current number of clients connected to <i>server</i> and the current number of clients waiting for authentication. </p>
<p> <code>Example</code><br />
&nbsp;<wbr>#&nbsp;<wbr>virt-admin srv-clients-info libvirtd<br />
&nbsp;<wbr>nclients_max&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: 120<br />
&nbsp;<wbr>nclients&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: 3<br />
&nbsp;<wbr>nclients_unauth_max : 20<br />
&nbsp;<wbr>nclients_unauth&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: 0</p>
<dt><code>srv-clients-set</code> <i>server</i> [<i>&#8211;max-clients</i> <code>count</code>] [<i>&#8211;max-unauth-clients</i> <code>count</code>]</p>
<dd> Set new client-related limits on <i>server</i>.</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>&#8211;max-clients</i></p>
<dd> Change the upper limit of the maximum overall number of clients connected to <i>server</i> to value <code>count</code>. The value for this limit has to be always greater than the value of <i>&#8211;max-unauth-clients</i>.</p>
<dt><i>&#8211;max-unauth-clients</i></p>
<dd> Change the upper limit of the maximum number of clients waiting for authentication, in order to be connected to <i>server</i>, to value <code>count</code>. The value for this limit has to be always lower than the value of <i>&#8211;max-clients</i>.</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h2>CLIENT COMMANDS</h2>
<p> Following commands provide management and monitoring of clients connected to one of daemon&#8217;s available servers. Clients are specified by their numeric <font SIZE="-1">ID</font> which is obtained by listing all clients connected to a specified server (see command <code>srv-clients-list</code>).</p>
<dl>
<dt><code>client-info</code> <i>server</i> <i>client</i></p>
<dd> Retrieve identity information about <i>client</i> from <i>server</i>. The attributes returned may vary depending on the connection transport used. Transport-dependent attributes include local client process&#8217;s pid, uid, user name, and group name, as well as socket address of the remote peer, see <code>Examples</code> below. </p>
<p> On the other hand, transport-independent attributes include client&#8217;s SELinux context (if enabled on the host) and <font SIZE="-1">SASL</font> username (if <font SIZE="-1">SASL</font> authentication is enabled within daemon). </p>
<p> <code>Examples</code> </p>
<pre>
 # virt-admin client-info libvirtd 1
 id             : 1
 connection_time: 2016-05-03 13:27:04+0200
 transport      : unix
 readonly       : yes
 unix_user_id   : 0
 unix_user_name : root
 unix_group_id  : 0
 unix_group_name: root
 unix_process_id: 10201
 # virt-admin client-info libvirtd 2
 id             : 2
 connection_time: 2016-05-03 13:30:33+0200
 transport      : tcp
 readonly       : no
 sock_addr      : 127.0.0.1:57060
</pre>
<dt><code>client-disconnect</code> <i>server</i> <i>client</i></p>
<dd> Close a connection originating from <i>client</i>. The <i>server</i> argument specifies the name of the server <i>client</i> is currently connected to.</dl>
<h2>ENVIRONMENT</h2>
<p> The following environment variables can be set to alter the behaviour of <tt>&quot;virt-admin&quot;</tt></p>
<dl>
<dt>VIRT_ADMIN_DEBUG=&lt;0 to 4&gt;</p>
<dd> Turn on verbose debugging of virt-admin commands. Valid levels are</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> VIRT_ADMIN_DEBUG=0 </p>
<p> <font SIZE="-1">DEBUG &#8211;</font> Messages at <font SIZE="-1">ALL</font> levels get logged</p>
<dt>&bull;</p>
<dd> VIRT_ADMIN_DEBUG=1 </p>
<p> <font SIZE="-1">INFO &#8211;</font> Logs messages at levels <font SIZE="-1">INFO, NOTICE, WARNING</font> and <font SIZE="-1">ERROR</font></p>
<dt>&bull;</p>
<dd> VIRT_ADMIN_DEBUG=2 </p>
<p> <font SIZE="-1">NOTICE &#8211;</font> Logs messages at levels <font SIZE="-1">NOTICE, WARNING</font> and <font SIZE="-1">ERROR</font></p>
<dt>&bull;</p>
<dd> VIRT_ADMIN_DEBUG=3 </p>
<p> <font SIZE="-1">WARNING &#8211;</font> Logs messages at levels <font SIZE="-1">WARNING</font> and <font SIZE="-1">ERROR</font></p>
<dt>&bull;</p>
<dd> VIRT_ADMIN_DEBUG=4 </p>
<p> <font SIZE="-1">ERROR &#8211;</font> Messages at only <font SIZE="-1">ERROR</font> level gets logged.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>VIRT_ADMIN_LOG_FILE=&quot;LOGFILE&quot;</p>
<dd> The file to log virt-admin debug messages.</p>
<dt><font SIZE="-1">LIBVIRT_ADMIN_DEFAULT_URI</font></p>
<dd> The daemon whose admin server to connect to by default. Set this to a <font SIZE="-1">URI,</font> in the same format as accepted by the <code>connect</code> option. This overrides the default <font SIZE="-1">URI</font> set in any client config file.</p>
<dt><font SIZE="-1">VIRT_ADMIN_HISTSIZE</font></p>
<dd> The number of commands to remember in the command history. The default value is 500.</p>
<dt>LIBVIRT_DEBUG=LEVEL</p>
<dd> Turn on verbose debugging of all libvirt <font SIZE="-1">API</font> calls. Valid levels are</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> LIBVIRT_DEBUG=1 </p>
<p> Messages at level <font SIZE="-1">DEBUG</font> or above</p>
<dt>&bull;</p>
<dd> LIBVIRT_DEBUG=2 </p>
<p> Messages at level <font SIZE="-1">INFO</font> or above</p>
<dt>&bull;</p>
<dd> LIBVIRT_DEBUG=3 </p>
<p> Messages at level <font SIZE="-1">WARNING</font> or above</p>
<dt>&bull;</p>
<dd> LIBVIRT_DEBUG=4 </p>
<p> Messages at level <font SIZE="-1">ERROR</font> or above</dl>
</dl>
<dl>
<dt>
<dd>
<p> For further information about debugging options consult &lt;<a rel="nofollow" href="http://libvirt.org/logging.html">http://libvirt.org/logging.html</a>&gt;</dl>
</dl>
<h2>BUGS</h2>
<p> Report any bugs discovered to the libvirt community via the mailing list &lt;<a rel="nofollow" href="http://libvirt.org/contact.html">http://libvirt.org/contact.html</a>&gt; or bug tracker &lt;<a rel="nofollow" href="http://libvirt.org/bugs.html">http://libvirt.org/bugs.html</a>&gt;. Alternatively report bugs to your software distributor / vendor.</p>
<h2>AUTHORS</h2>
<pre>
  Please refer to the AUTHORS file distributed with libvirt.
  Based on the virsh man page.
</pre>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2015 Red Hat, Inc., and the authors listed in the libvirt <font SIZE="-1">AUTHORS</font> file.</p>
<h2>LICENSE</h2>
<p> virt-admin is distributed under the terms of the <font SIZE="-1">GNU LGPL</font> v2+. This is free software; see the source for copying conditions. There is <font SIZE="-1">NO</font> warranty; not even for <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE</font></p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-virsh/">virsh</a></i>(1), <i><a href="/docs/linux/man/1-virt-xml-validate/">virt-xml-validate</a></i>(1), <i><a href="/docs/linux/man/1-virt-host-validate/">virt-host-validate</a></i>(1), &lt;<a rel="nofollow" href="http://www.libvirt.org/">http://www.libvirt.org/</a>&gt; </p>
<h2>Index</h2>
