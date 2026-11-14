---
title: "sssd(8)"
name: "sssd"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sssd/"
description: "sssd – System Security Services Daemon"
---

<p>sssd &#8211; System Security Services Daemon</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>sssd</code> [<i>options</i>]</dl>
<h2>Description</h2>
<p><code>SSSD</code></p>
<dd>provides a set of daemons to manage access to remote directories and authentication mechanisms. It provides an NSS and PAM interface toward the system and a pluggable backend system to connect to multiple different account sources as well as D-Bus interface. It is also the basis to provide client auditing and policy services for projects like FreeIPA. It provides a more robust database to store local users as well as extended user data.</p>
<h2>Options</h2>
<p><code>-d</code>,<code>&#8211;debug-level</code> <i>LEVEL</i></p>
<dl>
<dd>SSSD supports two representations for specifying the debug level. The simplest is to specify a decimal value from 0-9, which represents enabling that level and all lower-level debug messages. The more comprehensive option is to specify a hexadecimal bitmask to enable or disable specific levels (such as if you wish to suppress a level). </p>
<p> Please note that each SSSD service logs into its own log file. Also please note that enabling &#8220;debug_level&#8221; in the &#8220;[sssd]&#8221; section only enables debugging just for the sssd process itself, not for the responder or provider processes. The &#8220;debug_level&#8221; parameter should be added to all sections that you wish to produce debug logs from. </p>
<p> In addition to changing the log level in the config file using the &#8220;debug_level&#8221; parameter, which is persistent, but requires SSSD restart, it is also possible to change the debug level on the fly using the <code><a href="/docs/linux/man/8-sss_debuglevel/">sss_debuglevel</a></code>(8) tool. </p>
<p> Currently supported debug levels: </p>
<p> <i>0</i>, <i>0x0010</i>: Fatal failures. Anything that would prevent SSSD from starting up or causes it to cease running. </p>
<p> <i>1</i>, <i>0x0020</i>: Critical failures. An error that doesn&#8217;t kill SSSD, but one that indicates that at least one major feature is not going to work properly. </p>
<p> <i>2</i>, <i>0x0040</i>: Serious failures. An error announcing that a particular request or operation has failed. </p>
<p> <i>3</i>, <i>0x0080</i>: Minor failures. These are the errors that would percolate down to cause the operation failure of 2. </p>
<p> <i>4</i>, <i>0x0100</i>: Configuration settings. </p>
<p> <i>5</i>, <i>0x0200</i>: Function data. </p>
<p> <i>6</i>, <i>0x0400</i>: Trace messages for operation functions. </p>
<p> <i>7</i>, <i>0x1000</i>: Trace messages for internal control functions. </p>
<p> <i>8</i>, <i>0x2000</i>: Contents of function-internal variables that may be interesting. </p>
<p> <i>9</i>, <i>0x4000</i>: Extremely low-level tracing information. </p>
<p> To log required bitmask debug levels, simply add their numbers together as shown in following examples: </p>
<p> <i>Example</i>: To log fatal failures, critical failures, serious failures and function data use 0x0270. </p>
<p> <i>Example</i>: To log fatal failures, configuration settings, function data, trace messages for internal control functions use 0x1310. </p>
<p> <i>Note</i>: The bitmask format of debug levels was introduced in 1.7.0. </p>
<p> <i>Default</i>: 0</dl>
<p> <code>&#8211;debug-timestamps=</code><i>mode</i></p>
<dl>
<dd><i>1</i>: Add a timestamp to the debug messages </p>
<p> <i>0</i>: Disable timestamp in the debug messages </p>
<p> Default: 1</dl>
<p> <code>&#8211;debug-microseconds=</code><i>mode</i></p>
<dl>
<dd><i>1</i>: Add microseconds to the timestamp in debug messages </p>
<p> <i>0</i>: Disable microseconds in timestamp </p>
<p> Default: 0</dl>
<p> <code>-f</code>,<code>&#8211;debug-to-files</code></p>
<dl>
<dd>Send the debug output to files instead of stderr. By default, the log files are stored in /var/log/sssd and there are separate log files for every SSSD service and domain.</dl>
<p> <code>-D</code>,<code>&#8211;daemon</code></p>
<dl>
<dd>Become a daemon after starting up.</dl>
<p> <code>-i</code>,<code>&#8211;interactive</code></p>
<dl>
<dd>Run in the foreground, don&#8217;t become a daemon.</dl>
<p> <code>-c</code>,<code>&#8211;config</code></p>
<dl>
<dd>Specify a non-default config file. The default is /etc/sssd/sssd.conf. For reference on the config file syntax and options, consult the <code><a href="/docs/linux/man/5-sssd-conf/">sssd.conf</a></code>(5) manual page.</dl>
<p> <code>-?</code>,<code>&#8211;help</code></p>
<dl>
<dd>Display help message and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dd>Print version number and exit.</dl>
<h2>Signals</h2>
<p>SIGTERM/SIGINT</p>
<dl>
<dd>Informs the SSSD to gracefully terminate all of its child processes and then shut down the monitor.</dl>
<p> SIGHUP</p>
<dl>
<dd>Tells the SSSD to stop writing to its current debug file descriptors and to close and reopen them. This is meant to facilitate log rolling with programs like logrotate.</dl>
<p> SIGUSR1</p>
<dl>
<dd>Tells the SSSD to simulate offline operation for the duration of the &#8220;offline_timeout&#8221; parameter. This is useful for testing. The signal can be sent to either the sssd process or any sssd_be process directly.</dl>
<p> SIGUSR2</p>
<dl>
<dd>Tells the SSSD to go online immediately. This is useful for testing. The signal can be sent to either the sssd process or any sssd_be process directly.</dl>
<h2>Notes</h2>
<p>If the environment variable SSS_NSS_USE_MEMCACHE is set to &quot;NO&quot;, client applications will not use the fast in memory cache.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-sssd/">sssd</a></code>(8), <code><a href="/docs/linux/man/5-sssd-conf/">sssd.conf</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ldap/">sssd-ldap</a></code>(5), <code><a href="/docs/linux/man/5-sssd-krb5/">sssd-krb5</a></code>(5), <code><a href="/docs/linux/man/5-sssd-simple/">sssd-simple</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ipa/">sssd-ipa</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ad/">sssd-ad</a></code>(5), <code><a href="/docs/linux/man/5-sssd-sudo/">sssd-sudo</a></code>(5),<code><a href="/docs/linux/man/5-sssd-secrets/">sssd-secrets</a></code>(5),<code><a href="/docs/linux/man/8-sss_cache/">sss_cache</a></code>(8), <code><a href="/docs/linux/man/8-sss_debuglevel/">sss_debuglevel</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupadd/">sss_groupadd</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupdel/">sss_groupdel</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupshow/">sss_groupshow</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupmod/">sss_groupmod</a></code>(8), <code><a href="/docs/linux/man/8-sss_useradd/">sss_useradd</a></code>(8), <code><a href="/docs/linux/man/8-sss_userdel/">sss_userdel</a></code>(8), <code><a href="/docs/linux/man/8-sss_usermod/">sss_usermod</a></code>(8), <code><a href="/docs/linux/man/8-sss_obfuscate/">sss_obfuscate</a></code>(8), <code><a href="/docs/linux/man/8-sss_seed/">sss_seed</a></code>(8), <code><a href="/docs/linux/man/8-sssd_krb5_locator_plugin/">sssd_krb5_locator_plugin</a></code>(8), <code><a href="/docs/linux/man/8-sss_ssh_authorizedkeys/">sss_ssh_authorizedkeys</a></code>(8), <code><a href="/docs/linux/man/8-sss_ssh_knownhostsproxy/">sss_ssh_knownhostsproxy</a></code>(8),<code><a href="/docs/linux/man/5-sssd-ifp/">sssd-ifp</a></code>(5),<code><a href="/docs/linux/man/8-pam_sss/">pam_sss</a></code>(8). <code><a href="/docs/linux/man/5-sss_rpcidmapd/">sss_rpcidmapd</a></code>(5)</p>
<h2>Authors</h2>
<p><code>The SSSD upstream &#8211; <a rel="nofollow" href="https://pagure.io/SSSD/sssd/">https://pagure.io/SSSD/sssd/</a></code></p>
