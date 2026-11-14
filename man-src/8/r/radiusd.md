---
title: "radiusd(8)"
name: "radiusd"
section: "8"
letter: "r"
url: "/docs/linux/man/8-radiusd/"
description: "radiusd – Authentication, Authorization and Accounting server"
---

<p>radiusd &#8211; Authentication, Authorization and Accounting server</p>
<h2>Synopsis</h2>
<p><code>radiusd</code> [<code>-C</code>] [<code>-d</code> <i>config_directory</i>] [<code>-f</code>] [<code>-h</code>] [<code>-i</code> <i>ip-address</i>] [<code>-l</code> <i>log_file</i>] [<code>-m</code>] [<code>-n</code> <i>name</i>] [<code>-p</code> <i>port</i>] [<code>-s</code>] [<code>-t</code>] [<code>-v</code>] [<code>-x</code>] [<code>-X</code>]</p>
<h2>Description</h2>
<p>FreeRADIUS is a high-performance and highly configurable RADIUS server. It supports many database back-ends such as flat-text files, SQL, LDAP, Perl, Python, etc. It also supports many authentication protocols such as PAP, CHAP, MS-CHAP(v2), HTTP Digest, and EAP (EAP-MD5, EAP-TLS, PEAP, EAP-TTLS, EAP-SIM, etc.). </p>
<p> It also has fullsupport for Cisco&#8217;s VLAN Query Protocol (VMPS) and DHCP. </p>
<p> Please read the DEBUGGING section below. It contains instructions for quickly configuring the server for your local system.</p>
<h2>Options</h2>
<p>The following command-line options are accepted by the server:</p>
<dl>
<dt>-C</p>
<dd>Check the configuration and exit immediately. If there is a problem reading the configuration, then the server will exit with a non-zero status code. If the configuration appears to be acceptable, then the server will exit with a zero status code. </p>
<p> Note that there are limitations to this check. Due to the complexities involved in <i>almost</i> starting a RADIUS server, these checks are necessarily incomplete. The server can return a zero status code when run with -C, but may still exit with an error when run normally. </p>
<p> See the output of <code>radiusd -XC</code> for an informative list of which modules are checked for correct configuration, and which modules are skipped, and therefore not checked.</p>
<dt>-d <i>config directory</i></p>
<dd>Defaults to <i>/etc/raddb</i>. <code>Radiusd</code> looks here for its configuration files such as the <i>dictionary</i> and the <i>users</i> files.</p>
<dt>-f</p>
<dd>Do not fork, stay running as a foreground process.</p>
<dt>-h</p>
<dd>Print usage help information.</p>
<dt>-i <i>ip-address</i></p>
<dd>Defines which IP address that the server uses for sending and receiving packets. </p>
<p> If this command-line option is given, then the &quot;bind_address&quot; and all &quot;listen{}&quot; entries in <i>radiusd.conf</i> are ignored. </p>
<p> This option MUST be used in conjunction with &quot;-p&quot;.</p>
<dt>-l <i>log_file</i></p>
<dd>Defaults to <i>${logdir}/radius.log</i>. <code>Radiusd</code> writes it&#8217;s logging information to this file. If log_file is the string &quot;stdout&quot; logging will be written to stdout.</p>
<dt>-m</p>
<dd>On SIGINT or SIGQUIT exit cleanly instead of immediately. This is most useful for when running the server with &quot;valgrind&quot;.</p>
<dt>-n <i>name</i></p>
<dd>Read <i>raddb/name.conf</i> instead of <i>raddb/radiusd.conf</i>.</p>
<dt>-p <i>port</i></p>
<dd>Defines which port is used for receiving authentication packets. Accounting packets are received on &quot;port + 1&quot;. </p>
<p> When this command-line option is given, all &quot;listen&quot; sections in <i>radiusd.conf</i> are ignored. </p>
<p> This option MUST be used in conjunction with &quot;-i&quot;.</p>
<dt>-s</p>
<dd>Run in &quot;single server&quot; mode. The server normally runs with multiple threads and/or processes, which can lower its response time to requests. Some systems have issues with threading, however, so running in &quot;single server&quot; mode may help to address those issues. In single server mode, the server will also not &quot;daemonize&quot; (auto-background) itself.</p>
<dt>-t</p>
<dd>Do not spawn threads.</p>
<dt>-v</p>
<dd>Print server version information and exit.</p>
<dt>-X</p>
<dd>Debugging mode. Equivalent to &quot;-sfxx -l stdout&quot;. When trying to understand how the server works, ALWAYS run it with &quot;radiusd -X&quot;. For production servers, use &quot;raddebug&quot;</p>
<dt>-x</p>
<dd>Finer-grained debug mode. In this mode the server will print details of every request on it&#8217;s <code>stdout</code> output. You can specify this option multiple times (-x -x or -xx) to get more detailed output.</dl>
<h2>Debugging</h2>
<p>The default configuration is set to work in the widest possible circumstances. It requires minimal changes for your system. </p>
<p> However, your needs may be complex, and may require significant changes to the server configuration. Making random changes is a guaranteed method of failure. Instead, we STRONGLY RECOMMEND proceeding via the following steps: </p>
<p> 1) Always run the server in debugging mode ( <code>radiusd -X</code> ) after making a configuration change. We cannot emphasize this enough. If you are not running the server in debugging mode, you <i>will not</i> be able to see what is doing, and you <i>will not</i> be able to correct any problems. </p>
<p> If you ask questions on the mailing list, the first response will be to tell you &quot;run the server in debugging mode&quot;. Please, follow these instructions. </p>
<p> 2) Change as little as possible in the default configuration files. The server contains a decade of experience with protocols, databases, and different systems. Its default configuration is designed to work almost everywhere, and to do almost everything you need. </p>
<p> 3) When you make a small change, testing it before changing anything else. If the change works, save a copy of the configuration, and make another change. If the change doesn&#8217;t work, debug it, and try to understand why it doesn&#8217;t work. </p>
<p> If you begin by making large changes to the server configuration, it will never work, and you will never be able to debug the problem. </p>
<p> 4) If you need to add a connection to a database FOO (e.g. LDAP or SQL), then: </p>
<p> a) Edit raddb/modules/foo<br />
 This file contains the default configuration for the module. It contains comments describing what can be configured, and what those configuration entries mean. </p>
<p> b) Edit raddb/sites-available/default<br />
 This file contains the default policy for the server. e.g. &quot;enable CHAP, MS-CHAP, and EAP authentication&quot;. Look in this file for all references to your module &quot;foo&quot;. Read the comments, and remove the leading hash &#8216;#&#8217; from the lines referencing the module. This enables the module. </p>
<p> c) Edit raddb/sites-available/inner-tunnel<br />
 This file contains the default policy for the &quot;tunneled&quot; portion of certain EAP methods. Perform the same kind of edits as above, for the &quot;default&quot; file.. If you are not using EAP (802.1X), then this step can be skipped. </p>
<p> d) Start the server in debugging mode ( <code>radiusd -X</code> ), and start testing. </p>
<p> 5) Ask questions on the mailing list (freeradius-users [at] lists.freeradius.org). When asking questions, include the output from debugging mode ( <code>radiusd -X</code> ). This information will allow people to help you. If you do not include it, the first response to your message will be &quot;post the output of debug mode&quot;. </p>
<p> Ask questions earlier, rather than later. If you cannot solve a problem in a day, ask a question on the mailing list. Most questions have been seen before, and can be answered quickly.</p>
<h2>Background</h2>
<p><code>RADIUS</code> is a protocol spoken between an access server, typically a device connected to several modems or ISDN lines, and a <code>radius</code> server. When a user connects to the access server, (s)he is asked for a loginname and a password. This information is then sent to the <code>radius</code> server. The server replies with &quot;access denied&quot;, or &quot;access OK&quot;. In the latter case login information is sent along, such as the IP address in the case of a PPP connection. </p>
<p> The access server also sends login and logout records to the <code>radius</code> server so accounting can be done. These records are kept for each terminal server seperately in a file called <code>detail</code>, and in the <i>wtmp</i> compatible logfile <code>/var/log/radwtmp</code>.</p>
<h2>Configuration</h2>
<p><code>Radiusd</code> uses a number of configuration files. Each file has it&#8217;s own manpage describing the format of the file. These files are:</p>
<dl>
<dt>radiusd.conf</p>
<dd>The main configuration file, which sets the administrator-controlled items.</p>
<dt>dictionary</p>
<dd>This file is usually static. It defines all the possible RADIUS attributes used in the other configuration files. You don&#8217;t have to modify it. It includes other dictionary files in the same directory.</p>
<dt>hints</p>
<dd>Defines certain hints to the radius server based on the users&#8217;s loginname or other attributes sent by the access server. It also provides for mapping user names (such as Pusername -&gt; username). This provides the functionality that the <i>Livingston 2.0</i> server has as &quot;Prefix&quot; and &quot;Suffix&quot; support in the <i>users</i> file, but is more general. Ofcourse the Livingston way of doing things is also supported, and you can even use both at the same time (within certain limits).</p>
<dt>huntgroups</p>
<dd>Defines the huntgroups that you have, and makes it possible to restrict access to certain huntgroups to certain (groups of) users.</p>
<dt>users</p>
<dd>Here the users are defined. On a typical setup, this file mainly contains DEFAULT entries to process the different types of logins, based on hints from the hints file. Authentication is then based on the contents of the UNIX <i>/etc/passwd</i> file. However it is also possible to define all users, and their passwords, in this file.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-radiusd-conf/">radiusd.conf</a>(5), <a href="/docs/linux/man/5-users/">users</a>(5), <a href="/docs/linux/man/5-huntgroups/">huntgroups</a>(5), <a href="/docs/linux/man/5-hints/">hints</a>(5), <a href="/docs/linux/man/5-dictionary/">dictionary</a>(5), <a href="/docs/linux/man/8-raddebug/">raddebug</a>(8)</p>
<h2>Author</h2>
<p>The FreeRADIUS Server Project (<a rel="nofollow" href="http://www.freeradius.org)">http://www.freeradius.org)</a></p>
