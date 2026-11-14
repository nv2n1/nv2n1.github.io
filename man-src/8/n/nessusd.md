---
title: "nessusd(8)"
name: "nessusd"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nessusd/"
description: "nessusd – The server part of the Nessus Security Scanner"
---

<p>nessusd &#8211; The server part of the Nessus Security Scanner</p>
<h2>Synopsis</h2>
<p><code>nessusd [-v] [-h] [-c </code><i>config-file</i><code>] [-S </code><i>ip[,ip2,&#8230;]</i><code>] [-a </code><i>address</i> <code>] [-p </code><i>port-number</i><code>] [-D] [-d] [-R] [-P] [-q]</code> </p>
<h2>Description</h2>
<p>The <code>Nessus Security Scanner</code> is a security auditing tool made up of two parts: a server, and a client. The server, <code>nessusd</code> is in charge of the attacks, while the client <code>nessus</code> interfaces with the user. <code>nessusd</code> inspect the remote hosts and attempts to list all the vulnerabilities and common misconfigurations that affects them. </p>
<h2>Options</h2>
<dl>
<dt><code>-c </code><i>&lt;config-file&gt;</i><code>, &#8211;config-file=</code><i>&lt;config-file&gt;</i></p>
<dd>Use the alternate configuration file instead of <i>/etc/nessus/nessusd.conf</i> </p>
<dt><code>-a </code><i>&lt;address&gt;</i><code>, &#8211;listen=</code><i>&lt;address&gt;</i></p>
<dd>Tell the server to only listen to connections on the address <i>&lt;address&gt;</i> which is an IP, not a machine name. For instance, &quot;nessusd -a 192.168.1.1&quot; will make <code>nessusd</code> only listen to requests going to <i>192.168.1.1</i> This option is useful if you are running nessusd on a gateway and if you don&#8217;t want people on the outside to connect to your <code>nessusd</code>. </p>
<dt><code>-S </code><i>&lt;ip[,ip2,&#8230;]&gt;</i><code>, &#8211;src-ip=</code><i>&lt;ip[,ip2,&#8230;]&gt;</i></p>
<dd>Force the source IP of the connections established by Nessus to <i>&lt;ip&gt;</i> . Note that you can not set arbitrary addresses here, as most Nessus checks need to fully establish a connection to the remote host. This option is only useful if you have a multi-homed machine with multiple public IP addresses that you would like to use instead of the default one. Example : <code>nessusd -S 192.168.1.1,192.168.1.2,192.168.1.3,192.168.1.4</code> will make <code>nessusd</code> establish connections with a source IP of one among those listed above. For this setup to work, the host running nessusd should have multiple NICs with these IP addresses set. </p>
<dt><code>-p </code><i>&lt;port-number&gt;</i><code>, &#8211;port=</code><i>&lt;port-number&gt;</i></p>
<dd>Tell the server to listen on connection on the port &lt;port-number&gt; rather than listening on port 1241 (default). </p>
<dt><code>-D, &#8211;background</code></p>
<dd>Make the server run in background (daemon mode) </p>
<dt><code>-q, &#8211;quiet</code></p>
<dd>Prevent the server from printing the loading status of the plugins at startup </p>
<dt><code>-d, &#8211;dump-cfg</code></p>
<dd>Make the server dumps its compilation options </p>
<dt><code>-v, &#8211;version</code></p>
<dd>Writes the version number and exits </p>
<dt><code>-R, &#8211;recompile</code></p>
<dd>Compiles every .nasl plugin as a binary file and exits. </p>
<dt><code>-h, &#8211;help</code></p>
<dd>Show a summary of the commands </p>
</dl>
<h2>The Configuration File</h2>
<p>The default <code>nessusd </code> configuration file, <i>/etc/nessus/nessusd.conf</i> contains these options: </p>
<dl>
<dt>plugins_folder</p>
<dd>Contains the location of the plugins folder. This is usually /var/lib/nessus/plugins, but you may change this.</p>
<dt>logfile</p>
<dd>path to the logfile. if you want the nessusd logs to be written on stderr. <i>Because nessusd is a sensitive program, you should keep your logs. </i> </p>
<dt>max_hosts</p>
<dd>is maximum number of hosts to test at the same time which should be given to the client (which can override it). This value must be computed given your bandwidth, the number of hosts you want to test, your amount of memory and the horsepower of your processor(s). </p>
<dt>max_checks</p>
<dd>is the number of plugins that will run against each host being tested. Note that the total number of process will be <i>max_checks</i> x <i>max_hosts</i> so you need to find a balance between these two options. Note that launching too many plugins at the same time may disable the remote host, either temporarily (ie: inetd closes its ports) or definitely (the remote host crash because it is asked to do too many things at the same time), so be careful. </p>
<dt>be_nice</p>
<dd>If this option is set to &#8216;yes&#8217;, then each child forked by nessusd will <a href="/docs/linux/man/2-nice/">nice</a>(2) itself to a very low priority. This may speed up your scan as the main nessusd process will be able to continue to spew processes, and this guarantees that nessusd does not deprives other important processes from their resources. </p>
<dt>log_whole_attack</p>
<dd>If this option is set to &#8216;yes&#8217;, nessusd will store the name, pid, date and target of each plugin launched. This is helpful for monitoring and debugging purpose, however this option might make nessusd fill your disk rather quickly. </p>
<dt>log_plugins_name_at_load</p>
<dd>If this option is set to &#8216;yes&#8217;, nessusd will log the name of each plugin being loaded at startup, or each time it receives the HUP signal. </p>
<dt>dumpfile</p>
<dd>Some plugins might issue messages, most of the time to inform you that something went wrong. If you want to read these messages, set this value to a given file name. If you want to save space, set this option value to /dev/null </p>
<dt>cgi_path</p>
<dd>By default, nessusd looks for default CGIs in /cgi-bin and /scripts. You may change these to something else to reflect the policy of your site. The syntax of this option is the same as the shell $PATH variable: path1:path2:&#8230; </p>
<dt>port_range</p>
<dd>This is the default range of ports that the scanner plugins will probe. The syntax of this option is flexible, it can be a single range (&quot;1-1500&quot;), several ports (&quot;21,23,80&quot;), several ranges of ports (&quot;1-1500,32000-33000&quot;). Note that you can specify UDP and TCP ports by prefixing each range by T or U. For instance, the following range will make nessusd scan UDP ports 1 to 1024 and TCP ports 1 to 65535 : &quot;T:1-65535,U:1-1024&quot;. </p>
<dt>optimize_test</p>
<dd>By default, nessusd does not trust the remote host banners. It means that it will check a webserver claiming to be IIS for Apache flaws, and so on. This behavior might generate false positive and will slow the scan down somehow. If you are sure the banners of the remote host have not been tampered with, you can safely enable this option, which will force the plugins to perform their job only against the services they have been designed to check. </p>
<dt>checks_read_timeout</p>
<dd>Number of seconds that the security checks will wait for when doing a recv(). You should increase this value if you are running nessusd across a slow network slink (testing a host via a dialup connection for instance) </p>
<dt>non_simult_ports</p>
<dd>Some services (in particular SMB) do not appreciate multiple connections at the same time coming from the same host. This option allows you to prevent nessusd to make two connections on the same given ports at the same time. The syntax of this option is &quot;port1[, port2&#8230;.]&quot;. Note that you can use the KB notation of nessusd to designate a service formally. Ex: &quot;139, Services/www&quot;, will prevent nessusd from making two connections at the same time on port 139 and on every port which hosts a web server. </p>
<dt>plugins_timeout</p>
<dd>This is the maximum lifetime, in seconds of a plugin. It may happen that some plugins are slow because of the way they are written or the way the remote server behaves. This option allows you to make sure your scan is never caught in an endless loop because of a non-finishing plugin. </p>
<dt>safe_checks</p>
<dd>Most of the time, nessusd attempts to reproduce an exceptional condition to determine if the remote services are vulnerable to certain flaws. This includes the reproduction of buffer overflows or format strings, which may make the remote server crash. If you set this option to &#8216;yes&#8217;, nessusd will disable the plugins which have the potential to crash the remote services, and will at the same time make several checks rely on the banner of the service tested instead of its behavior towards a certain input. This reduces false positives and makes nessusd nicer towards your network, however this may make you miss important vulnerabilities (as a vulnerability affecting a given service may also affect another one). </p>
<dt>auto_enable_dependencies</p>
<dd>Nessus plugins use the result of each other to execute their job. For instance, a plugin which logs into the remote SMB registry will need the results of the plugin which finds the SMB name of the remote host and the results of the plugin which attempts to log into the remote host. If you want to only select a subset of the plugins available, tracking the dependencies can quickly become tiresome. If you set this option to &#8216;yes&#8217;, nessusd will automatically enable the plugins that are depended on. </p>
<dt>use_mac_addr</p>
<dd>Set this option to &#8216;yes&#8217; if you are testing your local network and each local host has a dynamic IP address (affected by DHCP or BOOTP), and all the tested hosts will be referred to by their MAC address. </p>
<dt>plugin_upload</p>
<dd>Set this option to &#8216;yes&#8217; if you want to let nessusd users upload their own plugins. Note that the plugins they will upload will end up in their nessusd home directory, so they won&#8217;t be shared among users (except if the user who uploads the plugins is the one declared in the option &#8216;admin_user&#8217; </p>
<dt>admin_user</p>
<dd>The user listed in this option will upload his plugins into the global nessus plugins directory, and they will be shared by every other users </p>
<dt>rules</p>
<dd>path to the rules database </p>
<p> The other options in this file can usually be redefined by the client. </p>
</dl>
<h2>Users Management</h2>
<p>The utility <a href="/docs/linux/man/8-nessus-adduser/">nessus-adduser</a>(8) creates new nessusd users. Each nessusd user is attributed a &quot;home&quot;, in @NESSUS_STATEDIR@/users/&lt;username&gt;. This home contains the following directories :</p>
<dl>
<dt>auth/</p>
<dd>This directory contains the authentification information for this user. It might contain the file &#8216;dname&#8217; if the user is authenticating using a certificate, or &#8216;hash&#8217; (or &#8216;passwd&#8217;) if the user is authenticating using a password. The file &#8216;hash&#8217; contains a MD5 hash of the user password, as well as a random seed. The file &#8216;password&#8217; should contain the password in clear text. </p>
<p> This directory also contains the file &#8216;rules&#8217; which contains the rules which apply to this user. </p>
<p> The content of this directory can <code>not</code> be altered by the user in any way whatsoever </p>
<dt>kbs/</p>
<dd>This directory contains the knowledge base (KB) of each host tested by this user, if the user has enable the option &#8216;save_kb&#8217;. </p>
<dt>sessions/</p>
<dd>This directory contains the list and contents of the sessions done by this user. </p>
<dt>plugins/</p>
<dd>This directory contains the plugins this user uploaded. </p>
<p> When a user attempts to log in, nessusd first checks that the directory @NESSUS_STATEDIR@/users/&lt;username&gt; exists, then hashes the password sent by the user with the random salt found in &lt;username&gt;/auth/hash, and compares it with the password hash stored in the same file. If the users authenticates using a certificate, then nessusd checks that the certificate has been signed by a recognized authority, and makes sure that the dname of the certificate shown by the user is the same as the one in &lt;username&gt;/dname. </p>
<p> To remove a given user, use the command <a href="/docs/linux/man/8-nessus-rmuser/">nessus-rmuser</a>(8). </p>
</dl>
<h2>The Rule Set Format</h2>
<p>A rule has always the same format which is:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>keyword IP/mask</p>
<p> <i>Keyword </i> is one of <i>reject </i> , <i>accept</i> or <i>default</i> </p>
<p> In addition to this, the IP address may be preceded by an exclamation mark (!) which means: &#8220;not&#8221; There are three sources of rules: </p>
<dl>
<dt>*</p>
<dd>the rules database, which applies to every users</p>
<dt>*</p>
<dd>the users database rules, which applies to one user</p>
<dt>*</p>
<dd>the users rules, defined by the user in the client </p>
<p> You must know that there is a priority in the rules: the user can not extend its privileges, but can only lower them. (that it, it can only restrict the set of hosts he is allowed to test). </p>
</dl>
<h2>The Rules Database</h2>
<p>The rules database contains the system-wide rules, which applies for every user. Its syntax has been defined in the previous section. Example: </p>
<dl>
<dd>accept 127.0.0.0/8<br />
 reject 192.168.1.1/32<br />
 reject !192.168.0.0/16<br />
 default reject</dl>
<p> This allows the user to test localhost, and all the hosts on 192.168.0.0/16, except 192.168.1.1/32.<br />
 The rules accept the special keyword <i>client_ip</i> which is replaced, at connection time, by the IP of the user who logs in. If you want everyone to test his own box only, then you can do: </p>
<dl>
<dd>accept client_ip/32<br />
 default reject</dl>
<h2>Network Usage</h2>
<p>Bear in mind that Nessus can be quite network intensive. Even if the Nessus developers have taken every effor to avoid packet loss (including transparently resending UDP packets, waiting for data to be received in TCP connections, etc.) so bandwidth use should always be closely monitored, with current server hardware, bandwidth is usually the bottleneck in a Nessus scan. It might not became too aparent in the final reports, scanners will still run, holes might be detected, but you will risk to run into <i>false negatives</i> (i.e. Nessus will not report a security hole that is present in a remote host) </p>
<p> Users might need to tune Nessus configuration if running the server in low bandwidth conditions (<i>low</i> being &#8216;less bandwidth that the one your hardware system can produce) or otherwise will get erratic results. There are several parameters that can be modified to reduce network load: </p>
<dl>
<dt>checks_read_timeout</p>
<dd>(Introduced in Nessus 0.99.4) The default value is set to 5 seconds, that can (should) be increased if network bandwidth is low in the nessus.conf or nessusrc configuration files. Notice that it is recommended to increase this this value, if you are running a test outside your LAN (i.e. to Internet hosts through an Internet connection), to over 10 seconds. </p>
<dt>max_hosts</p>
<dd>Number of hosts to test at the same time (this value is set by the Nessus GUI client or by .nessusrc) it can be as low as you want it to be (obviously 1 is the minimum) </p>
<dt>max_checks</p>
<dd>Number of checkst to test at the same time (this value is also set by the Nessus GUI client or by .nessusrc ) it can be as low as you want it to be and it will also reduce network load and improve performance (obviously 1 is the minimum) Notice that the Nessus server will spawn max_hosts * max_checks processes. </p>
<p> Other options might be using the QoS features offered by your server operating system or your network to improve the bandwidth use. </p>
<p> It is not easy to give a bandwidth estimate for a Nessus run, you will probably need to make your own counts. However, assuming you test 65536 TCP ports. This will require at least a single packet per port that is at least 40 bytes large. Add 14 bytes for the ethernet header and you will send 65536 * (40 + 14) = 3670016 bytes. So for just probing all TCP ports we may need a multitude of this as nmap will try to resend the packets twice if no response is received. </p>
<p> A very rough estimate is that a full scan for UDP, TCP and RPC as well as all NASL scripts may result in 8 to 32 MB wrth of traffic per scanned host. Reducing the amount of tested part and such will reduce the amout of data to be transfered significantly. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-nessus/">nessus</a></code>(1),&nbsp;<wbr><code><a href="/docs/linux/man/8-nessus-adduser/">nessus-adduser</a></code>(8),&nbsp;<wbr><code><a href="/docs/linux/man/8-nessus-rmuser/">nessus-rmuser</a></code>(8),&nbsp;<wbr><code><a href="/docs/linux/man/8-nessus-mkcert/">nessus-mkcert</a></code>(8) </p>
<h2>More Information About The Nessus Project</h2>
<p>The canonical places where you will find more information about the Nessus project are: </p>
<dl>
<dd><a rel="nofollow" href="http://www.nessus.org/">http://www.nessus.org/</a> (Official site)<br />
 <a rel="nofollow" href="http://cvs.nessus.org/">http://cvs.nessus.org/</a> (Developers site)<br />
 <a rel="nofollow" href="http://list.nessus.org/">http://list.nessus.org/</a> (Mailing lists)</dl>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<h2>Authors</h2>
<p>nessusd was written by Renaud Deraison &lt;deraison [at] cvs.nessus.org&gt;</p>
