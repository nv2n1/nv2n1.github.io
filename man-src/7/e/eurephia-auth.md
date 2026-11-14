---
title: "eurephia-auth(7)"
name: "eurephia-auth"
section: "7"
letter: "e"
url: "/docs/linux/man/7-eurephia-auth/"
description: "eurephia-auth – The eurephia OpenVPN authentication plug-in"
---

<p><code>eurephia-auth</code> &#8211; The eurephia OpenVPN authentication plug-in</p>
<h2>Description</h2>
<p>The <code>eurephia-auth.so</code> is a plug-in for OpenVPN. It is loaded by providing the <code>&#8211;plugin</code> option in the OpenVPN configuration. The syntax for OpenVPN and eurephia-auth is:</p>
<dl>
<dd>plugin eurephia-auth.so &quot;&lt;plugin args&gt; &#8212; &lt;DB args&gt;&quot;</dl>
<p> Please notice the quotes and the double dash. They are important markers so that the eurephia-auth module receives all arguments (the quotes) and that it knows when to pass on the rest of the arguments to the defined database driver, separated by the double dash. This manual page will only look at the <code>&lt;plugin args&gt;</code> options. For the <code>&lt;DB args&gt;</code> options, refer to the corresponding database driver you are using. </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;log-destination</code> | <code>-l</code></p>
<dd>This defines how eurephia will do its logging. It can take a filename to log to a file. If the string is <code>openvpn:</code> it will pass the log data over to OpenVPN, which will combine the OpenVPN and eurephia logs. You can also log via syslog, by indicating <code>syslog:</code>. The last possible special value is <code>none:</code> which will disable logging completely.</p>
<dd>With syslog: you can also define which syslog facility the logging will go to. The default is to log to the user facility. Other supported facilities are authpriv, daemon and local0 to local7. To send log data to the daemon the &#8211;log-destination argument need to be</p>
<dd>&nbsp;<wbr>&#8211;log-destination syslog:daemon</p>
<dt><code>&#8211;log-level</code> | <code>-L</code></p>
<dd>This defines how verbose the eurephia logging will be. The required argument to this option must be a numeric value, where 0 indicates as little logging as possible &#8211; only giving informative messages, or a high value like 50 to give really verbose logging. In general a log level less than 4 should be more than enough under normal circumstances.</p>
<dd><code>NOTICE:</code> The highest log level is 10, unless the eurephia-auth modules have been compiled with debug features.</p>
<dt><code>&#8211;database-interface</code> | <code>-i</p>
<dd>This argument must have a full path to the eurephia database driver module. This defines which database interface eurephia will use.</dl>
<p> </code></p>
<h2>Openvpn Clients</h2>
<p>The only change the OpenVPN clients needs to do is to add</p>
<dl>
<dd>auth-user-pass</dl>
<p> to their configuration file. This instructs the OpenVPN client to ask for user name and password when starting the connection.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-eurephia-sqlite/">eurephia-sqlite</a></code>(8), <code><a href="/docs/linux/man/8-eurephia_init/">eurephia_init</a></code>(8)</p>
<h2>Author</h2>
<p>Copyright (C) 2008-2010 David Sommerseth &lt;dazo [at] users.sourceforge.net&gt;</p>
