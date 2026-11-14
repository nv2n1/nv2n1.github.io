---
title: "stap-server(8)"
name: "stap-server"
section: "8"
letter: "s"
url: "/docs/linux/man/8-stap-server/"
description: "stap-server – systemtap compile server management"
---

<p>stap-server &#8211; systemtap compile server management </p>
<h2>Synopsis</h2>
<p>[ <code>service</code> ] <code>stap-server</code> { <code>start</code> | <code>stop</code> | <code>restart</code> | <code>condrestart</code> | <code>try-restart</code> | <code>force-reload</code> | <code>status</code> } [ <i>options</i> ] </p>
<h2>Description</h2>
<p>A systemtap compile server listens for connections from stap clients on a secure SSL network port and accepts requests to run the <i>stap</i> front end. Each server advertises its presence and configuration on the local network using mDNS (<i>avahi</i>) allowing for automatic detection by clients. The stap-server script aims to provide:</p>
<dl>
<dt>&bull;</p>
<dd>management of systemtap compile servers as a service.</p>
<dt>&bull;</p>
<dd>convenient control over configured servers and individual (ad-hoc) servers. </p>
<h2>Arguments</h2>
<p>One of the actions below must be specified:</p>
<dl>
<dt><code>start</code></p>
<dd>Start servers. The specified servers are started. If no server is specified, the configured servers are started. If no servers are configured, a server for the kernel release and architecture of the host is started. If a specified server is already started, this action will be ignored for that server. If a server fails to start, this action fails. </p>
<dt><code>stop</code></p>
<dd>Stop server(s). The specified servers are stopped. If no server is specified, all currently running servers are stopped. If a specified server is not running, this action will be successful for that server. If a server fails to stop, this action fails. </p>
<dt><code>restart</code></p>
<dd>Stop and restart servers. The specified servers are stopped and restarted. If no server is specified, all currently running servers are stopped and restarted. If no servers are running, this action behaves like <i>start</i>. </p>
<dt><code>condrestart</code></p>
<dd>Stop and restart servers. The specified servers are stopped and restarted. If a specified server is not running, it is not started. If no server is specified, all currently running servers are stopped and restarted. If no servers are running, none will be started. </p>
<dt><code>try-restart</code></p>
<dd>This action is identical to <i>condrestart</i>. </p>
<dt><code>force-reload</code></p>
<dd>Stop all running servers, reload config files and restart the service as if <i>start</i> was specified. </p>
<dt><code>status</code></p>
<dd>Print information about running servers. Information about the specified server(s) will be printed. If no server is specified, information about all running servers will be printed. </p>
</dl>
<h2>Options</h2>
<p>The following options are used to provide additional configuration and to specify servers to be managed: </p>
<dl>
<dt><code>-c</code> <i>configfile</i></p>
<dd>This option specifies a global configuration file in addition to the default global configuration file described below. This file will be processed after the default global configuration file. If the <code>-c</code> option is specified more than once, the last configuration file specified will be used. </p>
<dt><code>-a</code> <i>architecture</i></p>
<dd>This option specifies the target architecture of the server and is analogous to the <code>-a</code> option of <i>stap</i>. See the <i><a href="/docs/linux/man/1-stap/">stap</a></i>(1) manual page for more details. The default architecture is the architecture of the host. </p>
<dt><code>-r</code> <i>kernel-release</i></p>
<dd>This option specifies the target kernel release of the server and is analogous to the <code>-r</code> option of <i>stap</i>. See the <i><a href="/docs/linux/man/1-stap/">stap</a></i>(1) manual page for more details. The default release is that of the currently running kernel. </p>
<dt><code>-I</code> <i>path</i></p>
<dd>This option specifies an additional path to be searched by the server(s) for tapsets and is analogous to the <code>-I</code> option of <i>stap</i>. See the <i><a href="/docs/linux/man/1-stap/">stap</a></i>(1) manual page for more details. </p>
<dt><code>-R</code> <i>path</i></p>
<dd>This option specifies the location of the systemtap runtime to be used by the server(s) and is analogous to the <code>-R</code> option of <i>stap</i>. See the <i><a href="/docs/linux/man/1-stap/">stap</a></i>(1) manual page for more details. </p>
<dt><code>-B</code> <i>options</i></p>
<dd>This option specifies options to be passed to <i>make</i> when building systemtap modules and is analogous to the <code>-B</code> option of <i>stap</i>. See the <i><a href="/docs/linux/man/1-stap/">stap</a></i>(1) manual page for more details. </p>
<dt><code>-i</code></p>
<dd>This option is a shortcut which specifies one server for each kernel release installed in <i>/lib/modules/</i>. Previous <code>-I</code>, <code>-R</code>, <code>-B</code> and <code>-u</code> options will be applied to each server, however previous <code>-a</code> options will be ignored and the default architecture will be used. </p>
<dt><code>-n</code> <i>nickname</i></p>
<dd>This option allows the specification of a server configuration by nickname. When <code>-n</code> is specified, a currently running server with the given nickname will be searched for. If no currently running server with the given nickname is found, a server configuration with the given nickname will be searched for in the configuration files for default servers, or the path configured in the global configuration file or the configuration file specified by the <code>-c</code> option. If a server configuration for the given nickname is found, the <code>-a</code>, <code>-r</code>, <code>-I</code>, <code>-R</code>, <code>-B</code> and <code>-u</code> options for that server will be used as if they were specified on the command line. If no configuration with the given nickname is found, and the action is <i>start</i> (or an action behaving like <i>start</i> (see <code>ARGUMENTS</code>), the server will be started with the given nickname. If no configuration with the given nickname is found, and the action is not <i>start</i> (or an action behaving like <i>start</i>), it is an error. If a nickname is not specified for a server which is being started, its nickname will be its process id. </p>
<dt><code>-p</code> <i>pid</i></p>
<dd>This option allows the specification of a server configuration by process id. When <code>-p</code> is specified, a currently running server with the given process id will be searched for. If no such server is found, it is an error. If a server with the given process id is found, the <code>-a</code>, <code>-r</code>, <code>-I</code>, <code>-R</code>, <code>-B</code> and <code>-u</code> options for that server will be used as if they were specified on the command line. </p>
<dt><code>-u</code> <i>user-name</i></p>
<dd>Each systemtap compile server is normally run by the user name <i>stap-server</i> (for the initscript) or as the user invoking <i>stap-server</i>, unless otherwise configured (see <code>FILES</code>). This option specifies the user name used to run the server(s). The user name specified must be a member of the group <i>stap-server</i>. </p>
<dt><code>&#8211;log</code> <i>logfile</i></p>
<dd>This option allows the specification of a separate log file for each server. Each &#8211;log option is added to a list which will be applied, in turn, to each server specified. If more servers are specified than &#8211;log options, the default log file (see <code>FILES</code>) will be used for subsequent servers. </p>
<dt><code>&#8211;port</code> <i>port-number</i></p>
<dd>This option allows the specification of a specific network port for each server. Each &#8211;port option is added to a list which will be applied, in turn, to each server specified. If more servers are specified than &#8211;port options, a randomly selected port is used for subsequent servers. </p>
<dt><code>&#8211;ssl</code> <i>certificate-db-path</i></p>
<dd>This option allows the specification of a separate NSS certificate database for each server. Each &#8211;ssl option is added to a list which will be applied, in turn, to each server specified. If more servers are specified than &#8211;ssl options, the default certificate database (see <code>FILES</code>) for subsequent servers. </p>
<dt><code>&#8211;max-threads</code> <i>threads</i></p>
<dd>This option allows the specification of the maximum number of worker threads to handle concurrent requests. If <i>threads</i> == 0, each request will be handled on the main thread, serially. The default is the number of available processor cores. </p>
<dt><code>&#8211;max-request-size</code> <i>size</i></p>
<dd>This options allows the specification of the maximum size of an uncompressed client request. The arguement <i>size</i> is specified in bytes. The default is the 50000 bytes. </p>
<dt><code>&#8211;max-compressed-request</code> <i>size</i></p>
<dd>This options allows the specification of the maximum size of a compressed client request. The arguement <i>size</i> is specified in bytes. The default is the 5000 bytes. </p>
</dl>
<h2>Configuration</h2>
<p>Configuration files allow us to:</p>
<dl>
<dt>&bull;</p>
<dd>specify global configuration of logging, server configuration files, status files and other global parameters.</p>
<dt>&bull;</p>
<dd>specify which servers are to be started by default. </p>
</dl>
<h2>Global Configuration</h2>
<p>The Global Configuration file contains variable assignments used to configure the overall operation of the service. Each line beginning with a &#8216;#&#8217; character is ignored. All other lines must be of the form <i>VARIABLE=VALUE</i>. This is not a shell script. The entire contents of the line after the = will be assigned as-is to the variable. </p>
<p> The following variables may be assigned: </p>
<dl>
<dt><code>CONFIG_PATH</code></p>
<dd>Specifies the absolute path of the directory containing the default server configurations. </p>
<dt><code>STAT_PATH</code></p>
<dd>Specifies the absolute path of the running server status directory. </p>
<dt><code>LOG_FILE</code></p>
<dd>Specifies the absolute path of the log file. </p>
<dt><code>STAP_USER</code></p>
<dd>Specifies the userid which will be used to run the server(s) (default: for the initscript <i>stap-server</i>, otherwise the user running <i>stap-server</i>). </p>
</dl>
<p> Here is an example of a Global Configuration file: </p>
<dl>
<dd>
<pre>CONFIG_PATH=~&lt;user&gt;/my-stap-server-configs
LOG_FILE=/tmp/stap-server/log</pre>
</dl>
<h2>Individual Server Configuration</h2>
<p>Each server configuration file configures a server to be started when no server is specified for the <i>start</i> action, or an action behaving like the <i>start</i> action (see <i>ARGUMENTS</i>). Each configuration file contains variable assignments used to configure an individual server. </p>
<p> Each line beginning with a &#8216;#&#8217; character is ignored. All other lines must be of the form <i>VARIABLE=VALUE</i>. This is not a shell script. The entire contents of the line after the = will be assigned as-is to the variable. </p>
<p> Each configuration file must have a filename suffix of <i>.conf</i>. See <i><a href="/docs/linux/man/7-stappaths/">stappaths</a></i>(7) for the default location of these files. This default location can be overridden in the global configuration file using the <code>-c</code> option (see <i>OPTIONS</i>). </p>
<p> The following variables may be assigned:</p>
<dl>
<dt><code>ARCH</code></p>
<dd>Specifies the target architecture for this server and corresponds to the <code>-a</code> option (see <i>OPTIONS</i>). If <code>ARCH</code> is not set, the architecture of the host will be used. </p>
<dt><code>RELEASE</code></p>
<dd>Specifies the kernel release for this server and corresponds to the <code>-r</code> option (see <i>OPTIONS</i>). If <code>RELEASE</code> is not set, the release of the kernel running on the host will be used.<br />
&nbsp;<wbr></p>
<dt><code>BUILD</code></p>
<dd>Specifies options to be passed to the <i>make</i> process used by <i>systemtap</i> to build kernel modules. This an array variable with each element corresponding to a <code>-B</code> option (see <i>OPTIONS</i>). Using the form <code>BUILD=STRING</code> clears the array and sets the first element to <code>STRING</code>. Using the form <code>BUILD+=STRING</code> adds <code>STRING</code> as an additional element to the array.<br />
&nbsp;<wbr></p>
<dt><code>INCLUDE</code></p>
<dd>Specifies a list of directories to be searched by the server for tapsets. This is an array variable with each element corresponding to a <code>-I</code> option (see <i>OPTIONS</i>). Using the form <code>INCLUDE=PATH</code> clears the array and sets the first element to <code>PATH</code>. Using the form <code>INCLUDE+=PATH</code> adds <code>PATH</code> as an additional element to the array. </p>
<dt><code>RUNTIME</code></p>
<dd>Specifies the directory which contains the systemtap runtime code to be used by this server and corresponds to the <code>-R</code> option (see <i>OPTIONS</i>). </p>
<dt><code>USER</code></p>
<dd>Specifies the user name to be used to run this server and corresponds to the <code>-u</code> option (see <i>OPTIONS</i>). </p>
<dt><code>NICKNAME</code></p>
<dd>Specifies the nickname to be used to refer to this server and corresponds to the <code>-n</code> option (see <i>OPTIONS</i>). </p>
<dt><code>LOG</code></p>
<dd>Specifies the location of the log file to be used by this server and corresponds to the <code>&#8211;log</code> option (see <i>OPTIONS</i>). </p>
<dt><code>PORT</code></p>
<dd>Specifies the network port to be used by this server and corresponds to the <code>&#8211;port</code> option (see <i>OPTIONS</i>). </p>
<dt><code>SSL</code></p>
<dd>Specifies the location of the NSS certificate database to be used by this server and corresponds to the <code>&#8211;ssl</code> option (see <i>OPTIONS</i>). </p>
<dt><code>MAXTHREADS</code></p>
<dd>Specifies the maximum number of worker threads to handle concurrent requests to be used by this server and corresponds to the <code>&#8211;max-threads</code> option (see <i>OPTIONS</i>). </p>
<dt><code>MAXREQSIZE</code></p>
<dd>Specifies the maximum size of an uncompressed client request, to be used by this server and correspnds to the <code>&#8211;max-request-size</code> option (see <i>OPTIONS</i>). </p>
<dt><code>MAXCOMPRESSEDREQ</code></p>
<dd>Specifies the maximum size of an compressed client request, to be used by this server and correspnds to the <code>&#8211;max-compressed-request</code> option (see <i>OPTIONS</i>). </p>
</dl>
<p> Here is an example of a server configuration file: </p>
<dl>
<dd>
<pre>ARCH=
USER=
RELEASE=
NICKNAME=native</pre>
</dl>
<p> By keeping the ARCH, USER, and RELEASE fields blank, they will default to the current arch and release and use the default user. </p>
<p> A more specific example: </p>
<dl>
<dd>
<pre>ARCH=i386
RELEASE=2.6.18-128.el5
PORT=5001
LOG=/path/to/log/file</pre>
</dl>
<p> And here is a more complicated example: </p>
<dl>
<dd>
<pre>USER=serveruser
RELEASE=/kernels/2.6.18-92.1.18.el5/build
INCLUDE=/mytapsets
INCLUDE+=/yourtapsets
BUILD='VARIABLE1=VALUE1 VARIABLE2=VALUE2'
DEFINE=STP_MAXMEMORY=1024
DEFINE+=DEBUG_TRANS
RUNTIME=/myruntime
NICKNAME=my-server
SSL=/path/to/NSS/certificate/database</pre>
</dl>
<h2>Server Authentication</h2>
<p>The security of the SSL network connection between the client and server depends on the proper management of server certificates. </p>
<p> The trustworthiness of a given systemtap compile server can not be determined automatically without a trusted certificate authority issuing systemtap compile server certificates. This is not practical in everyday use and so, clients must authenticate servers against their own database of trusted server certificates. In this context, establishing a given server as trusted by a given client means adding that server&#8217;s certificate to the client&#8217;s database of trusted servers. </p>
<p> For the <i>stap-server</i> initscript, on the local host, this is handled automatically. When the <i>systemtap-server</i> package is installed, the server&#8217;s certificate for the default user (<i>stap-server</i>) is automatically generated and installed. This means that servers started by the <i>stap-server</i> initscript, with the default user, are automatically trusted by clients on the local host, both as an SSL peer and as a systemtap module signer. </p>
<p> Furthermore, when stap is invoked by an unprivileged user (not root, not a member of the group stapdev, but a member of the group stapusr and possibly the group stapsys), the options <i>&#8211;use-server</i> and <i>&#8211;privilege</i> are automatically added to the specified options. This means that unprivileged users on the local host can use a server on the local host in unprivileged mode with no further setup or options required. Normal users (those in none of the SystemTap groups) can also use compile-servers through the <i>&#8211;use-server</i> and <i>&#8211;privilege</i> options. But they will of course be unable to load the module (the <i>-p4</i> option can be used to stop short of loading). </p>
<p> In order to use a server running on another host, that server&#8217;s certificate must be installed on the client&#8217;s host. See the <i>&#8211;trust-servers</i> option in the <i><a href="/docs/linux/man/1-stap/">stap</a></i>(1) manual page for more details and README.unprivileged in the systemtap sources for more details.</p>
<h2>Examples</h2>
<p>See the <i><a href="//www.systutorials.com/docs/linux/man/3stap-stapex/">stapex</a></i>(3stap) manual page for a collection of sample <i>systemtap</i> scripts. To start the configured servers, or the default server, if none are configured: <code> $ [ service ] stap-server start</code> To start a server for each kernel installed in /lib/modules: <code> $ [ service ] stap-server start -i</code> To obtain information about the running server(s): <code> $ [ service ] stap-server status</code> To start a server like another one, except targeting a different architecture, by referencing the first server&#8217;s nickname: <code> $ [ service ] stap-server start -n </code><i>NICKNAME</i><code> -a </code><i>ARCH</i> To start a server for a kernel release not installed (cross-compiling) <code> $ [ service ] stap-server start -a </code><i>ARCH</i><code> -r </code><i>/BUILDDIR</i> To stop one of the servers by referencing its process id (obtained by running <code>stap-server status</code>): <code> $ [ service ] stap-server stop -p </code><i>PID</i> To run a script using a compile server: <code> $ stap SCRIPT &#8211;use-server</code> To run a script as an unprivileged user using a compile server: <code> $ stap SCRIPT</code> To stop all running servers: <code> $ [ service ] stap-server stop</code> To restart servers after a global configuration change and/or when default servers have been added, changed, or removed: <code> $ [ service ] stap-server force-reload</code> </p>
<h2>Safety And Security</h2>
<p>Systemtap is an administrative tool. It exposes kernel internal data structures and potentially private user information. See the <i><a href="/docs/linux/man/1-stap/">stap</a></i>(1) manual page for additional information on safety and security. </p>
<p> As a network server, stap-server should be activated with care in order to limit the potential effects of bugs or mischevious users. Consider the following prophylactic measures.</p>
<dl>
<dt>1</p>
<dd>Run stap-server as an unprivileged user, never as root. </p>
<p> When invoked as a service (i.e. <code>service stap-server</code> &#8230;), each server is run, by default, as the user <i>stap-server</i>. When invoked directly (i.e. <code>stap-server</code> &#8230;), each server is run, by default, as the invoking user. In each case, another user may be selected by using the <i>-u</i> option on invocation, by specifying <i>STAP_USER=</i>username in the global configuration file or by specifying <i>USER=</i>username in an individual server configuration file. The invoking user must have authority to run processes as another user. See <i>CONFIGURATION</i>. </p>
<p> The selected user must have write access to the server log file. The location of the server log file may be changed by setting <i>LOG_FILE=</i>path in the global configuration file. See <i>CONFIGURATION</i>. </p>
<p> The selected user must have read/write access to the directory containing the server status files. The location of the server status files may be changed by setting <i>STAT_PATH=</i>path in the global configuration file. See <i>CONFIGURATION</i>. </p>
<p> The selected user must have read/write access to the uprobes.ko build directory and its files. </p>
<p> Neither form of stap-server will run if the selected user is root. </p>
<dt>2</p>
<dd>Run stap-server requests with resource limits that impose maximum cpu time, file size, memory consumption, in order to bound the effects of processing excessively large or bogus inputs. </p>
<p> When the user running the server is <i>stap-server</i>, each server request is run with limits specified in <i>~stap-server/.systemtap/rc</i> otherwise, no limits are imposed. </p>
<dt>3</p>
<dd>Run stap-server with a TMPDIR environment variable that points to a separate and/or quota-enforced directory, in order to prevent filling up of important filesystems. </p>
<p> The default TMPDIR is <i>/tmp/</i>. </p>
<dt>4</p>
<dd>Activate network firewalls to limit stap client connections to relatively trustworthy networks. </p>
<p> For automatic selection of servers by clients, <i>avahi</i> must be installed on both the server and client hosts and <i>mDNS</i> messages must be allowed through the firewall. </p>
</dl>
<p> The systemtap compile server and its related utilities use the Secure Socket Layer (SSL) as implemented by Network Security Services (NSS) for network security. NSS is also used for the generation and management of certificates. The related certificate databases must be protected in order to maintain the security of the system. Use of the utilities provided will help to ensure that the proper protection is maintained. The systemtap client will check for proper access permissions before making use of any certificate database.</p>
<h2>Files</h2>
<dl>
<dt>Important files and their corresponding paths can be located in the</p>
<dd>stappaths (7) manual page. </p>
</dl>
<h2>See Also</h2>
<pre><i><a href="//www.systutorials.com/docs/linux/man/1-stap/">stap</a></i>(1),
<i><a href="//www.systutorials.com/docs/linux/man/8-staprun/">staprun</a></i>(8),
<i><a href="//www.systutorials.com/docs/linux/man/3stap-stapprobes/">stapprobes</a></i>(3stap),
<i><a href="//www.systutorials.com/docs/linux/man/7-stappaths/">stappaths</a></i>(7),
<i><a href="//www.systutorials.com/docs/linux/man/3stap-stapex/">stapex</a></i>(3stap),
<i>avahi</i>,
<i><a href="//www.systutorials.com/docs/linux/man/1-ulimit/">ulimit</a></i>(1),
<i>NSS</i></pre>
<h2>Bugs</h2>
<p>Use the Bugzilla link of the project web page or our mailing list. <code><a rel="nofollow" href="http://sourceware.org/systemtap/">http://sourceware.org/systemtap/</a></code>, <code>&lt;systemtap [at] sourceware.org&gt;</code>. </p>
