---
title: "sesman-ini(5)"
name: "sesman-ini"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sesman-ini/"
description: "sesman.ini – Configuration file for xrdp-sesman(8)"
---

<p><code>sesman.ini</code> &#8211; Configuration file for <code><a href="/docs/linux/man/8-xrdp-sesman/">xrdp-sesman</a></code>(8) </p>
<h2>Description</h2>
<p><code>sesman.ini</code> consists of several sections. Each section starts with the section name in square brackets, followed by a list of <i>parameter</i>=<i>value</i> lines. Following sections are recognized:</p>
<dl>
<dt><code>[Globals]</code></p>
<dd>Global configuration</p>
<dt><code>[Logging]</code></p>
<dd>Logging subsystem</p>
<dt><code>[Sessions]</code></p>
<dd>Session management</p>
<dt><code>[Security]</code></p>
<dd>Access control</p>
<dt><code>[X11rdp]</code>, <code>[Xvnc]</code>, <code>[Xorg]</code></p>
<dd>X11 server settings for supported servers</p>
<dt><code>[Chansrv]</code></p>
<dd>Settings for <a href="/docs/linux/man/8-xrdp-chansrv/">xrdp-chansrv</a>(8)</p>
<dt><code>[SessionVariables]</code></p>
<dd>Environment variables for the session  All parameters and values (except for file names and paths) are case insensitive, and are described in detail below. If any parameter is specified more than once, the last entry will be used. Options specified outside their proper section will be <i>ignored</i>. </p>
<h2>Globals</h2>
<p>Following parameters can be used in the <code>[Globals]</code> section. </p>
<dl>
<dt><code>ListenAddress</code>=<i>ip address</i></p>
<dd>xrdp-sesman listening address. If not specified, defaults to <i>0.0.0.0</i> (all interfaces). </p>
<dt><code>ListenPort</code>=<i>port number</i></p>
<dd>xrdp-sesman listening port. If not specified, defaults to <i>3350</i>. </p>
<dt><code>EnableUserWindowManager</code>=<i>[true|false]</i></p>
<dd>If set to <code>1</code>, <code>true</code> or <code>yes</code>, this option enables user specific startup script. That is, xrdp-sesman will execute the script specified by <code>UserWindowManager</code> if it exists. </p>
<dt><code>UserWindowManager</code>=<i>filename</i></p>
<dd>Name of the startup script relative to the user&#8217;s home directory. If present and enabled by <code>EnableUserWindowManager</code>, that script is executed instead of <code>DefaultWindowManager</code>. </p>
<dt><code>DefaultWindowManager</code>=<i>filename</i></p>
<dd>Full path to the default startup script used by xrdp-sesman to start a session if the user script is disabled or missing. </p>
</dl>
<h2>Logging</h2>
<p>Following parameters can be used in the <code>[Logging]</code> section. </p>
<dl>
<dt><code>LogFile</code>=<i>filename</i></p>
<dd>Log file path. It can be either absolute or relative. If not specified, defaults to <i>./sesman.log</i> </p>
<dt><code>LogLevel</code>=<i>level</i></p>
<dd>This option can have one of the following values: </p>
<p> <code>CORE</code> or <code>0</code> &#8211; Log only core messages. Those messages are logged <i>regardless</i> of the selected logging level. </p>
<p> <code>ERROR</code> or <code>1</code> &#8211; Log only error messages. </p>
<p> <code>WARNING</code>, <code>WARN</code> or <code>2</code> &#8211; Logs warnings and error messages. </p>
<p> <code>INFO</code> or <code>3</code> &#8211; Log errors, warnings and informational messages. </p>
<p> <code>DEBUG</code> or <code>4</code> &#8211; Log everything. If xrdp-sesman is compiled in debug mode, this options will output many more low-level messages. </p>
<dt><code>EnableSyslog</code>=<i>[true|false]</i></p>
<dd>If set to <code>1</code>, <code>true</code> or <code>yes</code>, this option enables logging to syslog. </p>
<dt><code>SyslogLevel</code>=<i>level</i></p>
<dd>Logging level for syslog. It can have the same values as <code>LogLevel</code>. If <code>SyslogLevel</code> and <code>LogLevel</code> differ, the least verbose setting takes effect for syslog. </p>
</dl>
<h2>Sessions</h2>
<p>Following parameters can be used in the <code>[Sessions]</code> section. </p>
<dl>
<dt><code>X11DisplayOffset</code>=<i>number</i></p>
<dd>The first X display number available for xrdp-sesman. This prevents xrdp-sesman from interfering with real X11 servers. If not specified, defaults to <i>10</i>. </p>
<dt><code>MaxSessions</code>=<i>number</i></p>
<dd>Sets the maximum number of simultaneous sessions. If not set or set to <i>0</i>, unlimited session are allowed. </p>
<dt><code>KillDisconnected</code>=<i>[true|false]</i></p>
<dd>If set to <code>1</code>, <code>true</code> or <code>yes</code>, every session will be killed within 60 seconds after the user disconnects. </p>
<dt><code>IdleTimeLimit</code>=<i>number</i></p>
<dd><i>This option is currently ignored!</i> Time limit before an idle session is disconnected. If set to <i>0</i>, automatic disconnection is disabled. </p>
<dt><code>DisconnectedTimeLimit</code>=<i>number</i></p>
<dd>Sets the time limit (in seconds) before a disconnected session is killed. If set to <i>0</i>, automatic killing is disabled. </p>
<dt><code>Policy</code>=<i>[Default|UBD|UBI|UBC|UBDI|UBDC]</i></p>
<dd>Session allocation policy. By default, a new session is created for the combination &lt;User,BitPerPixel&gt; when using Xrdp, and for the combination &lt;User,BitPerPixel,DisplaySize&gt; when using Xvnc. This behavior can be changed by setting session policy to: </p>
<p> <code>UBD</code> &#8211; session per &lt;User,BitPerPixel,DisplaySize&gt;<br />
 <code>UBI</code> &#8211; session per &lt;User,BitPerPixel,IPAddr&gt;<br />
 <code>UBC</code> &#8211; session per &lt;User,BitPerPixel,Connection&gt;<br />
 <code>UBDI</code> &#8211; session per &lt;User,BitPerPixel,DisplaySize,IPAddr&gt;<br />
 <code>UBDC</code> &#8211; session per &lt;User,BitPerPixel,DisplaySize,Connection&gt; </p>
<p> Note that the <code>User</code> and <code>BitPerPixel</code> criteria cannot be turned off. For Xvnc connections, <code>DisplaySize</code> is always enabled as well. </p>
</dl>
<h2>Security</h2>
<p>Following parameters can be used in the <code>[Security]</code> section. </p>
<dl>
<dt><code>AllowRootLogin</code>=<i>[true|false]</i></p>
<dd>If set to <code>1</code>, <code>true</code> or <code>yes</code>, enables root login on the terminal server. </p>
<dt><code>MaxLoginRetry</code>=<i>number</i></p>
<dd>The number of login attempts that are allowed on terminal server. If set to <i>0</i>, unlimited attempts are allowed. If not specified, defaults to <i>3</i>. </p>
<dt><code>TerminalServerUsers</code>=<i>group</i></p>
<dd>Only the users belonging to the specified group are allowed to login on terminal server. If unset or set to an invalid or non-existent group, login for all users is enabled. </p>
<dt><code>TerminalServerAdmins</code>=<i>group</i></p>
<dd><i>This option is currently ignored!</i> Only members of this group can have session management rights. </p>
<dt><code>AlwaysGroupCheck</code>=<i>[true|false]</i></p>
<dd>If set to <code>1</code>, <code>true</code> or <code>yes</code>, require group membership even if the group specified in <code>TerminalServerUsers</code> doesn&#8217;t exist. </p>
</dl>
<h2>X11 Server</h2>
<p>Following parameters can be used in the <code>[X11rdp]</code>, <code>[Xvnc]</code> and <code>[Xorg]</code> sections. </p>
<dl>
<dt><code>param</code>=<i>string</i></p>
<dd>Multiple <i>param</i> lines are supported. This first line specifies the path to the X11 server executable. Following lines specify command line arguments passed to the X11 server. </p>
</dl>
<h2>Chansrv</h2>
<p>Following parameters can be used in the <code>[Chansrv]</code> section. </p>
<dl>
<dt><code>FuseMountName</code>=<i>string</i></p>
<dd>Directory for drive redirection, relative to the user home directory. Created if it doesn&#8217;t exist. If not specified, defaults to <i>xrdp_client</i>. </p>
</dl>
<h2>Sessions Variables</h2>
<p>All entries in the <code>[SessionVariables]</code> section are set as environment variables in the user&#8217;s session.</p>
<h2>Files</h2>
<p>/etc/xrdp/sesman.ini</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-xrdp-sesman/">xrdp-sesman</a></code>(8), <code><a href="/docs/linux/man/8-xrdp-sesrun/">xrdp-sesrun</a></code>(8), <code><a href="/docs/linux/man/8-xrdp/">xrdp</a></code>(8), <code><a href="/docs/linux/man/5-xrdp-ini/">xrdp.ini</a></code>(5) For more info on <code>xrdp</code> see <a rel="nofollow" href="http://www.xrdp.org/">http://www.xrdp.org/</a> </p>
