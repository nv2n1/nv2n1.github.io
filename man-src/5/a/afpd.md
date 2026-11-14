---
title: "afpd(5)"
name: "afpd"
section: "5"
letter: "a"
url: "/docs/linux/man/5-afpd/"
description: "afpd.conf – Configuration file used by"
---

<p>afpd.conf &#8211; Configuration file used by </p>
<p><a href="/docs/linux/man/8-afpd/">afpd</a>(8) to determine the setup of its file sharing services</p>
<h2>Description</h2>
<p>/etc/atalk//afpd.conf is the configuration file used by <code>afpd</code> to determine the behavior and configuration of the different virtual file servers that it provides. </p>
<p> Any line not prefixed with # is interpreted. The configuration lines are composed like: server name [ options ] If a <code>&#8211;</code> is used instead of a server name, the default server is specified. Server names must be quoted if they contain spaces. They must not contain &quot;:&quot; or &quot;@&quot;. The path name must be a fully qualified path name, or a path name using either the ~ shell shorthand or any of the substitution variables, which are listed below. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> Each server has to be configured on a <code>single</code> line. Though newline escaping is supported. </p>
</dl>
<p> The possible options and their meanings are:</p>
<h2>Applevolumes Files</h2>
<p>-defaultvol <i>[path]</i></p>
<dl>
<dd>Specifies path to AppleVolumes.default file (default is /etc/atalk//AppleVolumes.default).</dl>
<p> -systemvol <i>[path]</i></p>
<dl>
<dd>Specifies path to AppleVolumes.system file (default is /etc/atalk//AppleVolumes.system).</dl>
<p> -[no]uservol</p>
<dl>
<dd>Enables or disables reading of the users&#8217; individual volumes file entirely.</dl>
<p> -[no]uservolfirst</p>
<dl>
<dd>Enables or disables reading of the users&#8217; individual volumes file before processing the global AppleVolumes.default file.</dl>
<h2>Authentication Methods</h2>
<p>-uamlist <i>[uams list]</i></p>
<dl>
<dd>Comma separated list of UAMs. (The default is uams_dhx.so,uams_dhx2.so). </p>
<p> The most commonly used UAMs are: </p>
<p> uams_guest.so</p>
<dl>
<dd>allows guest logins</dl>
<p> uams_clrtxt.so</p>
<dl>
<dd>(uams_pam.so or uams_passwd.so) Allow logins with passwords transmitted in the clear.</dl>
<p> uams_randum.so</p>
<dl>
<dd>allows Random Number and Two-Way Random Number Exchange for authentication (requires a separate file containing the passwords, either /etc/atalk//afppasswd file or the one specified via <code>-passwdfile</code>. See <code><a href="/docs/linux/man/1-afppasswd/">afppasswd</a></code>(1) for details</dl>
<p> uams_dhx.so</p>
<dl>
<dd>(uams_dhx_pam.so or uams_dhx_passwd.so) Allow Diffie-Hellman eXchange (DHX) for authentication.</dl>
<p> uams_dhx2.so</p>
<dl>
<dd>(uams_dhx2_pam.so or uams_dhx2_passwd.so) Allow Diffie-Hellman eXchange 2 (DHX2) for authentication.</dl>
<p> uam_gss.so</p>
<dl>
<dd>Allow Kerberos V for authentication (optional)</dl>
</dl>
<p> -uampath <i>[path]</i></p>
<dl>
<dd>Sets the default path for UAMs for this server (default is /etc/atalk//uams).</dl>
<p> -k5keytab <i>[path]</i>, -k5service <i>[service]</i>, -k5realm <i>[realm]</i></p>
<dl>
<dd>These are required if the server supports the Kerberos 5 authentication UAM.</dl>
<h2>Codepage Options</h2>
<p>With OS X Apple introduced the AFP3 protocol. One of the big changes was, that AFP3 uses Unicode names encoded as UTF-8 decomposed. Previous AFP/OS versions used codepages like MacRoman, MacCentralEurope, etc. </p>
<p> To be able to serve AFP3 and older clients at the same time, <code>afpd</code> needs to be able to convert between UTF-8 and Mac codepages. Even OS X clients partly still rely on codepages. As there&#8217;s no way, <code>afpd</code> can detect the codepage a pre AFP3 client uses, you have to specify it using the <code>-maccodepage</code> option. The default is MacRoman, which should be fine for most western users. </p>
<p> As <code>afpd</code> needs to interact with unix operating system as well, it need&#8217;s to be able to convert from UTF-8/MacCodepage to the unix codepage. By default <code>afpd</code> uses the systems LOCALE, or ASCII if your system doesn&#8217;t support locales. You can set the unix codepage using the <code>-unixcodepage</code> option. If you&#8217;re using extended characters in the configuration files for <code>afpd</code>, make sure your terminal matches the <code>-unixcodepage</code>. </p>
<p> -unixcodepage [<i>CODEPAGE</i>]</p>
<dl>
<dd>Specifies the servers unix codepage, e.g. &quot;ISO-8859-15&quot; or &quot;UTF8&quot;. This is used to convert strings to/from the systems locale, e.g. for authenthication, server messages and volume names. Defaults to LOCALE if your system supports it, otherwise ASCII will be used.</dl>
<p> -maccodepage [<i>CODEPAGE</i>]</p>
<dl>
<dd>Specifies the mac clients codepage, e.g. &quot;MAC_ROMAN&quot;. This is used to convert strings and filenames to the clients codepage for OS9 and Classic, i.e. for authentication and AFP messages (SIGUSR2 messaging). This will also be the default for the volumes maccharset. Defaults to MAC_ROMAN.</dl>
<h2>Password Options</h2>
<p>-loginmaxfail [<i>number</i>]</p>
<dl>
<dd>Sets the maximum number of failed logins, if supported by the UAM (currently none)</dl>
<p> -passwdfile [<i>path</i>]</p>
<dl>
<dd>Sets the path to the Randnum UAM passwd file for this server (default is /etc/atalk//afppasswd).</dl>
<p> -passwdminlen [<i>number</i>]</p>
<dl>
<dd>Sets the minimum password length, if supported by the UAM</dl>
<p> -[no]savepassword</p>
<dl>
<dd>Enables or disables the ability of clients to save passwords locally</dl>
<p> -[no]setpassword</p>
<dl>
<dd>Enables or disables the ability of clients to change their passwords via chooser or the &quot;connect to server&quot; dialog</dl>
<h2>Transport Protocols</h2>
<p>-[no]ddp</p>
<dl>
<dd>Enables or disables AFP-over-Appletalk. If <code>-proxy</code> is specified, you must instead use <code>-uamlist &quot;&quot;</code> to prevent DDP connections from working.</dl>
<p> -[no]tcp</p>
<dl>
<dd>Enables or disables AFP-over-TCP</dl>
<p> -transall</p>
<dl>
<dd>Make both available (default)</dl>
<h2>Transport Options</h2>
<p>-advertise_ssh</p>
<dl>
<dd>Allows Mac OS X clients (10.3.3 or above) to automagically establish a tunneled AFP connection through SSH. If this option is set, the server&#8217;s answers to client&#8217;s FPGetSrvrInfo requests contain an additional entry. It depends on both client&#8217;s settings and a correctly configured and running <code><a href="/docs/linux/man/8-sshd/">sshd</a></code>(8) on the server to let things work. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 Setting this option is not recommended since globally encrypting AFP connections via SSH will increase the server&#8217;s load significantly. On the other hand, Apple&#8217;s client side implementation of this feature in MacOS X versions prior to 10.3.4 contained a security flaw. </p>
</dl>
</dl>
<p> -ddpaddr <i>[ddp address]</i></p>
<dl>
<dd>Specifies the DDP address of the server. The default is to auto-assign an address (0.0). This is only useful if you are running AppleTalk on more than one interface.</dl>
<p> -fqdn <i>[name:port]</i></p>
<dl>
<dd>Specifies a fully-qualified domain name, with an optional port. This is discarded if the server cannot resolve it. This option is not honored by AppleShare clients &lt;= 3.8.3. This option is disabled by default. Use with caution as this will involve a second name resolution step on the client side. Also note that afpd will advertise this name:port combination but not automatically listen to it.</dl>
<p> -ipaddr <i>[ip address]</i></p>
<dl>
<dd>Specifies the IP address that the server should advertise <code>and</code> listens to (the default is the first IP address of the system). This option also allows to use one machine to advertise the AFP-over-TCP/IP settings of another machine via NBP when used together with the <code>-proxy</code> option.</dl>
<p> -port <i>[port number]</i></p>
<dl>
<dd>Allows a different TCP port to be used for AFP-over-TCP. The default is 548.</dl>
<p> -proxy</p>
<dl>
<dd>Runs an AppleTalk proxy server for the specified AFP-over-TCP server. If the address and port aren&#8217;t given, then the first IP address of the system and port 548 will be used. If you don&#8217;t want the proxy server to act as a DDP server as well, set <code>-uamlist &quot;&quot;</code>.</dl>
<p> -server_quantum <i>[number]</i></p>
<dl>
<dd>This specifies the DSI server quantum. The minimum value is 303840 (0x4A2E0). The maximum value is 0xFFFFFFFFF. If you specify a value that is out of range, the default value will be set (which is the minimum). Do not change this value unless you&#8217;re absolutely sure, what you&#8217;re doing</dl>
<p> -noslp</p>
<dl>
<dd>Do not register this server using the Service Location Protocol (if SLP support was compiled in). This is useful if you are running multiple servers and want one to be hidden, perhaps because it is advertised elsewhere, ie. by a SLP Directory Agent.</dl>
<h2>Miscellaneous Options</h2>
<p>-admingroup <i>[group]</i></p>
<dl>
<dd>Allows users of a certain group to be seen as the superuser when they log in. This option is disabled by default.</dl>
<p> -authprintdir <i>[path]</i></p>
<dl>
<dd>Specifies the path to be used (per server) to store the files required to do CAP-style print authentication which papd will examine to determine if a print job should be allowed. These files are created at login and if they are to be properly removed, this directory probably needs to be umode 1777. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 <code>-authprintdir</code> will only work for clients connecting via DDP. Almost all modern Clients will use TCP. </p>
</dl>
</dl>
<p> -client_polling</p>
<dl>
<dd>With this switch enabled, afpd won&#8217;t advertise that it is capable of server notifications, so that connected clients poll the server every 10 seconds to detect changes in opened server windows. <i>Note</i>: Depending on the number of simultaneously connected clients and the network&#8217;s speed, this can lead to a significant higher load on your network! </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 Do not use this option any longer as Netatalk 2.0 correctly supports server notifications, allowing connected clients to update folder listings in case another client changed the contents. </p>
</dl>
</dl>
<p> -cnidserver <i>[ipaddress:port]</i></p>
<dl>
<dd>Specifies the IP address and port of a cnid_metad server, required for CNID dbd backend. Defaults to localhost:4700.</dl>
<p> -guestname <i>[name]</i></p>
<dl>
<dd>Specifies the user that guests should use (default is &quot;nobody&quot;). The name should be quoted.</dl>
<p> -icon</p>
<dl>
<dd>Use the platform-specific icon</dl>
<p> -loginmesg <i>[message]</i></p>
<dl>
<dd>Sets a message to be displayed when clients logon to the server. The message should be in <code>unixcodepage</code> and should be quoted. Extended characters are allowed.</dl>
<p> -nodebug</p>
<dl>
<dd>Disables debugging.</dl>
<p> -sleep <i>[number]</i></p>
<dl>
<dd>AFP 3.x waits <i>number</i> hours before disconnecting clients in sleep mode. Default is 10 hours.</dl>
<p> -signature { user:&lt;text&gt; | host }</p>
<dl>
<dd>Specify a server signature. This option is useful while running multiple independent instances of afpd on one machine (eg. in clustered environments, to provide fault isolation etc.). &quot;host&quot; signature type allows afpd generating signature automatically (based on machine primary IP address). &quot;user&quot; signature type allows administrator to set up a signature string manually. The maximum length is 16 characters </p>
<p> <code>Example. Three server definitions using 2 different server signatures</code> </p>
<dl>
<dd>
<pre>first -signature user:USERS 
second -signature user:USERS 
third -signature user:ADMINS</pre>
</dl>
<p> First two servers will appear as one logical AFP service to the clients &#8211; if user logs in to first one and then connects to second one, session will be automatically redirected to the first one. But if client connects to first and then to third, will be asked for password twice and will see resources of both servers. Traditional method of signature generation causes two independent afpd instances to have the same signature and thus cause clients to be redirected automatically to server (s)he logged in first.</dl>
<h2>Logging Options</h2>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> Extended logging capabilities are only available if Netatalk was built using <code>&#8211;with-logfile</code>. As of Netatalk 2.0, the default is <code>&#8211;without-logfile</code> since the logger code is partially broken and needs a complete rewrite (the <code>-setuplog</code> option might not work as expected). If Netatalk was built without logger support then the daemons log to syslog. </p>
</dl>
<p> -[un]setuplog &quot;<i>&lt;logtype&gt; &lt;loglevel&gt; [&lt;filename&gt;]</i>&quot;</p>
<dl>
<dd>Specify that the given loglevel should be applied to log messages of the given logtype and that these messages should be logged to the given file. If the filename is ommited the loglevel applies to messages passed to syslog. Each logtype may have a loglevel applied to syslog and a loglevel applied to a single file. Latter <code>-setuplog</code> settings will override earlier ones of the same logtype (file or syslog). </p>
<p> logtypes: Default, Core, Logger, CNID, AFP </p>
<p> Daemon loglevels: LOG_SEVERE, LOG_ERROR, LOG_WARN, LOG_NOTE, LOG_INFO, LOG_DEBUG, LOG_DEBUG6, LOG_DEBUG7, LOG_DEBUG8, LOG_DEBUG9, LOG_MAXDEBUG </p>
<p> <code>Example. Some ways to change afpd&#8217;s logging behaviour via -[un]setuplog</code> Example: </p>
<dl>
<dd>
<pre>-setuplog &quot;logger log_maxdebug /var/log/netatalk-logger.log&quot; 
-setuplog &quot;afpdaemon log_maxdebug /var/log/netatalk-afp.log&quot; 
-unsetuplog &quot;default level file&quot; 
-setuplog &quot;default log_maxdebug&quot;</pre>
</dl>
</dl>
<h2>Debug Options</h2>
<p>These options are useful for debugging only. </p>
<p> -tickleval <i>[number]</i></p>
<dl>
<dd>Sets the tickle timeout interval (in seconds). Defaults to 30.</dl>
<p> -timeout <i>[number]</i></p>
<dl>
<dd>Specify the number of tickles to send before timing out a connection. The default is 4, therefore a connection will timeout after 2 minutes.</dl>
<h2>Examples</h2>
<p><code>Example. afpd.conf default configuration</code> </p>
<dl>
<dd>
<pre>- -transall -uamlist uams_dhx.so,uams_dhx2.so</pre>
</dl>
<p> <code>Example. afpd.conf MacCyrillic setup / UTF8 unix locale</code> </p>
<dl>
<dd>
<pre>- -transall -maccodepage mac_cyrillic -unixcodepage utf8</pre>
</dl>
<p> <code>Example. afpd.conf setup for Kerberos V auth with newline escaping</code> </p>
<dl>
<dd>
<pre>- -transall -uamlist uams_clrtxt.so,uams_dhx.so,uams_dhx2.so,uams_guest.so,uams_gss.so \ 
-k5service afpserver -k5keytab /path/to/afpserver.keytab \ 
-k5realm YOUR.REALM -fqdn your.fqdn.namel:548</pre>
</dl>
<p> <code>Example. afpd.conf letting afpd appear as three servers on the net</code> </p>
<dl>
<dd>
<pre>&quot;Guest Server&quot; -uamlist uams_guest.so -loginmesg &quot;Welcome guest!&quot;
&quot;User Server&quot; -uamlist uams_dhx2.so -port 12000
&quot;special&quot; -notcp -defaultvol &lt;path&gt; -systemvol &lt;path&gt;</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-afpd/">afpd</a></code>(8), <code><a href="/docs/linux/man/1-afppasswd/">afppasswd</a></code>(1), <code><a href="/docs/linux/man/5-applevolumes-default/">AppleVolumes.default</a></code>(5) </p>
