---
title: "radmin(8)"
name: "radmin"
section: "8"
letter: "r"
url: "/docs/linux/man/8-radmin/"
description: "radmin – FreeRADIUS Administration tool"
---

<p>radmin &#8211; FreeRADIUS Administration tool</p>
<h2>Synopsis</h2>
<p><code>radmin</code> [<code>-d</code> <i>config_directory</i>] [<code>-e</code> <i>command</i>] [<code>-E</code>] [<code>-f</code> <i>socket_file</i>] [<code>-h</code>] [<code>-i</code> <i>input_file</i>] [<code>-n</code> <i>name</i>] [<code>-o</code> <i>output_file</i>] [<code>-q</code>]</p>
<h2>Description</h2>
<p>FreeRADIUS Server administration tool that connects to the control socket of a running server, and gives a command-line interface to it. </p>
<p> At this time, only a few commands are supported. Please type &quot;help&quot; at the command prompt for detailed information about the supported commands.</p>
<h2>Warning</h2>
<p>The security protections offered by this command are limited to the permissions on the Unix domain socket, and the server configuration. If someone can connect to the Unix domain socket, they have a substantial amount of control over the server.</p>
<h2>Options</h2>
<p>The following command-line options are accepted by the program.</p>
<dl>
<dt>-d <i>config directory</i></dt>
<dd>Defaults to <i>/etc/raddb</i>. <code>radmin</code> looks here for the server configuration files to find the &quot;listen&quot; section that defines the control socket filename.</dd>
<dt>-e <i>command</i></dt>
<dd>Run <i>command</i> and exit.</dd>
<dt>-E</dt>
<dd>Echo commands as they are being executed.</dd>
<dt>-f <i>socket_file</i></dt>
<dd>Specify the socket filename directly. The radiusd.conf file is not read.</dd>
<dt>-h</dt>
<dd>Print usage help information.</dd>
<dt>-i <i>input_file</i></dt>
<dd>Reads input from the specified file. If not specified, stdin is used. This also sets &quot;-q&quot;.</dd>
<dt>-n <i>mname</i></dt>
<dd>Read <i>raddb/name.conf</i> instead of <i>raddb/radiusd.conf</i>.</dd>
<dt>-o <i>output_file</i></dt>
<dd>Write output to the specified file. If not specified, stdout is used. This also sets &quot;-q&quot;.</dd>
<dt>-q</dt>
<dd>Quiet mode.</dd></dl>
<h2>Commands</h2>
<p>The commands implemented by the command-line interface are almost completely controlled by the server. There are a few commands interpreted locally by radmin:</p>
<dl>
<dt>reconnect</dt>
<dd>Reconnect to the server.</dd>
<dt>quit</dt>
<dd>Exit from radmin.</dd>
<dt>exit</dt>
<dd>Exit from radmin.</dd></dl>
<p> The other commands are implemented by the server. Type &quot;help&quot; at the prompt for more information.</p>
<h2>Examples</h2>
<dl>
<dt>debug file&nbsp;<wbr>/var/log/radius/bob.log</dt>
<dd>Set debug logs to /var/log/radius/bob.log. There is very little checking of this filename. Rogue administrators may be able use this command to over-write almost any file on the system. If those administrators have write access to &quot;radius.conf&quot;, they can do the same thing without radmin, too.</dd>
<dt>debug condition&nbsp;<wbr>&#8216;(User-Name&nbsp;<wbr>==&nbsp;<wbr>bob)&#8217;</dt>
<dd>Enable debugging output for all requests that match the condition. Any &quot;unlang&quot; condition is valid here. The condition is parsed as a string, so it must be enclosed in single or double quotes. Strings enclosed in double-quotes must have back-slashes and the quotation marks escaped inside of the string. </dd>
<p> Only one debug condition can be active at a time.</p>
<dt>debug condition&nbsp;<wbr>&#8216;((User-Name&nbsp;<wbr>==&nbsp;<wbr>bob)&nbsp;<wbr>||&nbsp;<wbr>(Packet-Src-IP-Address&nbsp;<wbr>==&nbsp;<wbr>192.0.2.22))&#8217;</dt>
<dd>A more complex condition that enables debugging output for requests containing User-Name &quot;bob&quot;, or requests that originate from source IP address 192.0.2.22.</dd>
<dt>debug condition</dt>
<dd>Disable debug conditionals.</dd></dl>
<h2>Full List Of Commands</h2>
<dl>
<dt>add&nbsp;<wbr>&lt;command&gt;</dt>
<dd>do sub-command of add</dd>
<dt>add client&nbsp;<wbr>&lt;command&gt;</dt>
<dd>Add client configuration commands</dd>
<dt>add client file&nbsp;<wbr>&lt;filename&gt;</dt>
<dd>Add new client definition from &lt;filename&gt;</dd>
<dt>debug&nbsp;<wbr>&lt;command&gt;</dt>
<dd>debugging commands</dd>
<dt>debug condition&nbsp;<wbr>[condition]</dt>
<dd>Enable debugging for requests matching [condition]</dd>
<dt>debug level&nbsp;<wbr>&lt;number&gt;</dt>
<dd>Set debug level to &lt;number&gt;. Higher is more debugging.</dd>
<dt>debug file&nbsp;<wbr>[filename]</dt>
<dd>Send all debugging output to [filename]</dd>
<dt>del&nbsp;<wbr>&lt;command&gt;</dt>
<dd>do sub-command of del</dd>
<dt>del client&nbsp;<wbr>&lt;command&gt;</dt>
<dd>Delete client configuration commands</dd>
<dt>del client ipaddr&nbsp;<wbr>&lt;ipaddr&gt;</dt>
<dd>Delete a dynamically created client</dd>
<dt>hup&nbsp;<wbr>[module]</dt>
<dd>sends a HUP signal to the server, or optionally to one module</dd>
<dt>inject&nbsp;<wbr>&lt;command&gt;</dt>
<dd>commands to inject packets into a running server</dd>
<dt>inject to&nbsp;<wbr>&lt;ipaddr&gt;&nbsp;<wbr>&lt;port&gt;</dt>
<dd>Inject packets to the destination IP and port.</dd>
<dt>inject from&nbsp;<wbr>&lt;ipaddr&gt;</dt>
<dd>Inject packets as if they came from &lt;ipaddr&gt;</dd>
<dt>inject file&nbsp;<wbr>&lt;input-file&gt;&nbsp;<wbr>&lt;output-file&gt;</dt>
<dd>Inject packet from input-file&gt;, with results sent to &lt;output-file&gt;</dd>
<dt>reconnect</dt>
<dd>reconnect to a running server</dd>
<dt>terminate</dt>
<dd>terminates the server, and cause it to exit</dd>
<dt>set&nbsp;<wbr>&lt;command&gt;</dt>
<dd>do sub-command of set</dd>
<dt>set module&nbsp;<wbr>&lt;command&gt;</dt>
<dd>set module commands</dd>
<dt>set module config&nbsp;<wbr>&lt;module&gt;&nbsp;<wbr>variable value</dt>
<dd>set configuration for &lt;module&gt;</dd>
<dt>set module status&nbsp;<wbr>[alive|dead]</dt>
<dd>set the module to be alive or dead (always return &quot;fail&quot;)</dd>
<dt>set home_server&nbsp;<wbr>&lt;command&gt;</dt>
<dd>set home server commands</dd>
<dt>set home_server state&nbsp;<wbr>&lt;ipaddr&gt;&nbsp;<wbr>&lt;port&gt;&nbsp;<wbr>[alive|dead]</dt>
<dd>set state for given home server</dd>
<dt>show&nbsp;<wbr>&lt;command&gt;</dt>
<dd>do sub-command of show</dd>
<dt>show client&nbsp;<wbr>&lt;command&gt;</dt>
<dd>do sub-command of client</dd>
<dt>show client config&nbsp;<wbr>&lt;ipaddr&gt;</dt>
<dd>show configuration for given client</dd>
<dt>show client list</dt>
<dd>shows list of global clients</dd>
<dt>show debug&nbsp;<wbr>&lt;command&gt;</dt>
<dd>show debug properties</dd>
<dt>show debug condition</dt>
<dd>Shows current debugging condition.</dd>
<dt>show debug level</dt>
<dd>Shows current debugging level.</dd>
<dt>show debug file</dt>
<dd>Shows current debugging file.</dd>
<dt>show home_server&nbsp;<wbr>&lt;command&gt;</dt>
<dd>do sub-command of home_server</dd>
<dt>show home_server config&nbsp;<wbr>&lt;ipaddr&gt;&nbsp;<wbr>&lt;port&gt;</dt>
<dd>show configuration for given home server</dd>
<dt>show home_server list</dt>
<dd>shows list of home servers</dd>
<dt>show home_server state&nbsp;<wbr>&lt;ipaddr&gt;&nbsp;<wbr>&lt;port&gt;</dt>
<dd>shows state of given home server</dd>
<dt>show module&nbsp;<wbr>&lt;command&gt;</dt>
<dd>do sub-command of module</dd>
<dt>show module config&nbsp;<wbr>&lt;module&gt;</dt>
<dd>show configuration for given module</dd>
<dt>show module flags&nbsp;<wbr>&lt;module&gt;</dt>
<dd>show other module properties</dd>
<dt>show module list</dt>
<dd>shows list of loaded modules</dd>
<dt>show module methods&nbsp;<wbr>&lt;module&gt;</dt>
<dd>show sections where &lt;module&gt; may be used</dd>
<dt>show uptime</dt>
<dd>shows time at which server started</dd>
<dt>show version</dt>
<dd>Prints version of the running server</dd>
<dt>show xml&nbsp;<wbr>&lt;reference&gt;</dt>
<dd>Prints out configuration as XML</dd>
<dt>stats&nbsp;<wbr>&lt;command&gt;</dt>
<dd>do sub-command of stats</dd>
<dt>stats client&nbsp;<wbr>[auth/acct]&nbsp;<wbr>&lt;ipaddr&gt;</dt>
<dd>show statistics for given client, or for all clients (auth or acct)</dd>
<dt>stats home_server&nbsp;<wbr>[&lt;ipaddr&gt;/auth/acct]&nbsp;<wbr>&lt;port&gt;</dt>
<dd>show statistics for given home server (ipaddr and port), or for all home servers (auth or acct)</dd>
<dt>stats detail&nbsp;<wbr>&lt;filename&gt;</dt>
<dd>show statistics for the given detail file</dd></dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-unlang/">unlang</a>(5), <a href="/docs/linux/man/5-radiusd-conf/">radiusd.conf</a>(5), raddb/sites-available/control-socket</p>
<h2>Author</h2>
<p>Alan DeKok &lt;aland [at] freeradius.org&gt;</p>
