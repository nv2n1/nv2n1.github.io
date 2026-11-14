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
<dt>-d <i>config directory</i></p>
<dd>Defaults to <i>/etc/raddb</i>. <code>radmin</code> looks here for the server configuration files to find the &quot;listen&quot; section that defines the control socket filename.</p>
<dt>-e <i>command</i></p>
<dd>Run <i>command</i> and exit.</p>
<dt>-E</p>
<dd>Echo commands as they are being executed.</p>
<dt>-f <i>socket_file</i></p>
<dd>Specify the socket filename directly. The radiusd.conf file is not read.</p>
<dt>-h</p>
<dd>Print usage help information.</p>
<dt>-i <i>input_file</i></p>
<dd>Reads input from the specified file. If not specified, stdin is used. This also sets &quot;-q&quot;.</p>
<dt>-n <i>mname</i></p>
<dd>Read <i>raddb/name.conf</i> instead of <i>raddb/radiusd.conf</i>.</p>
<dt>-o <i>output_file</i></p>
<dd>Write output to the specified file. If not specified, stdout is used. This also sets &quot;-q&quot;.</p>
<dt>-q</p>
<dd>Quiet mode.</dl>
<h2>Commands</h2>
<p>The commands implemented by the command-line interface are almost completely controlled by the server. There are a few commands interpreted locally by radmin:</p>
<dl>
<dt>reconnect</p>
<dd>Reconnect to the server.</p>
<dt>quit</p>
<dd>Exit from radmin.</p>
<dt>exit</p>
<dd>Exit from radmin.</dl>
<p> The other commands are implemented by the server. Type &quot;help&quot; at the prompt for more information.</p>
<h2>Examples</h2>
<dl>
<dt>debug file&nbsp;<wbr>/var/log/radius/bob.log</p>
<dd>Set debug logs to /var/log/radius/bob.log. There is very little checking of this filename. Rogue administrators may be able use this command to over-write almost any file on the system. If those administrators have write access to &quot;radius.conf&quot;, they can do the same thing without radmin, too.</p>
<dt>debug condition&nbsp;<wbr>&#8216;(User-Name&nbsp;<wbr>==&nbsp;<wbr>bob)&#8217;</p>
<dd>Enable debugging output for all requests that match the condition. Any &quot;unlang&quot; condition is valid here. The condition is parsed as a string, so it must be enclosed in single or double quotes. Strings enclosed in double-quotes must have back-slashes and the quotation marks escaped inside of the string. </p>
<p> Only one debug condition can be active at a time.</p>
<dt>debug condition&nbsp;<wbr>&#8216;((User-Name&nbsp;<wbr>==&nbsp;<wbr>bob)&nbsp;<wbr>||&nbsp;<wbr>(Packet-Src-IP-Address&nbsp;<wbr>==&nbsp;<wbr>192.0.2.22))&#8217;</p>
<dd>A more complex condition that enables debugging output for requests containing User-Name &quot;bob&quot;, or requests that originate from source IP address 192.0.2.22.</p>
<dt>debug condition</p>
<dd>Disable debug conditionals.</dl>
<h2>Full List Of Commands</h2>
<dl>
<dt>add&nbsp;<wbr>&lt;command&gt;</p>
<dd>do sub-command of add</p>
<dt>add client&nbsp;<wbr>&lt;command&gt;</p>
<dd>Add client configuration commands</p>
<dt>add client file&nbsp;<wbr>&lt;filename&gt;</p>
<dd>Add new client definition from &lt;filename&gt;</p>
<dt>debug&nbsp;<wbr>&lt;command&gt;</p>
<dd>debugging commands</p>
<dt>debug condition&nbsp;<wbr>[condition]</p>
<dd>Enable debugging for requests matching [condition]</p>
<dt>debug level&nbsp;<wbr>&lt;number&gt;</p>
<dd>Set debug level to &lt;number&gt;. Higher is more debugging.</p>
<dt>debug file&nbsp;<wbr>[filename]</p>
<dd>Send all debugging output to [filename]</p>
<dt>del&nbsp;<wbr>&lt;command&gt;</p>
<dd>do sub-command of del</p>
<dt>del client&nbsp;<wbr>&lt;command&gt;</p>
<dd>Delete client configuration commands</p>
<dt>del client ipaddr&nbsp;<wbr>&lt;ipaddr&gt;</p>
<dd>Delete a dynamically created client</p>
<dt>hup&nbsp;<wbr>[module]</p>
<dd>sends a HUP signal to the server, or optionally to one module</p>
<dt>inject&nbsp;<wbr>&lt;command&gt;</p>
<dd>commands to inject packets into a running server</p>
<dt>inject to&nbsp;<wbr>&lt;ipaddr&gt;&nbsp;<wbr>&lt;port&gt;</p>
<dd>Inject packets to the destination IP and port.</p>
<dt>inject from&nbsp;<wbr>&lt;ipaddr&gt;</p>
<dd>Inject packets as if they came from &lt;ipaddr&gt;</p>
<dt>inject file&nbsp;<wbr>&lt;input-file&gt;&nbsp;<wbr>&lt;output-file&gt;</p>
<dd>Inject packet from input-file&gt;, with results sent to &lt;output-file&gt;</p>
<dt>reconnect</p>
<dd>reconnect to a running server</p>
<dt>terminate</p>
<dd>terminates the server, and cause it to exit</p>
<dt>set&nbsp;<wbr>&lt;command&gt;</p>
<dd>do sub-command of set</p>
<dt>set module&nbsp;<wbr>&lt;command&gt;</p>
<dd>set module commands</p>
<dt>set module config&nbsp;<wbr>&lt;module&gt;&nbsp;<wbr>variable value</p>
<dd>set configuration for &lt;module&gt;</p>
<dt>set module status&nbsp;<wbr>[alive|dead]</p>
<dd>set the module to be alive or dead (always return &quot;fail&quot;)</p>
<dt>set home_server&nbsp;<wbr>&lt;command&gt;</p>
<dd>set home server commands</p>
<dt>set home_server state&nbsp;<wbr>&lt;ipaddr&gt;&nbsp;<wbr>&lt;port&gt;&nbsp;<wbr>[alive|dead]</p>
<dd>set state for given home server</p>
<dt>show&nbsp;<wbr>&lt;command&gt;</p>
<dd>do sub-command of show</p>
<dt>show client&nbsp;<wbr>&lt;command&gt;</p>
<dd>do sub-command of client</p>
<dt>show client config&nbsp;<wbr>&lt;ipaddr&gt;</p>
<dd>show configuration for given client</p>
<dt>show client list</p>
<dd>shows list of global clients</p>
<dt>show debug&nbsp;<wbr>&lt;command&gt;</p>
<dd>show debug properties</p>
<dt>show debug condition</p>
<dd>Shows current debugging condition.</p>
<dt>show debug level</p>
<dd>Shows current debugging level.</p>
<dt>show debug file</p>
<dd>Shows current debugging file.</p>
<dt>show home_server&nbsp;<wbr>&lt;command&gt;</p>
<dd>do sub-command of home_server</p>
<dt>show home_server config&nbsp;<wbr>&lt;ipaddr&gt;&nbsp;<wbr>&lt;port&gt;</p>
<dd>show configuration for given home server</p>
<dt>show home_server list</p>
<dd>shows list of home servers</p>
<dt>show home_server state&nbsp;<wbr>&lt;ipaddr&gt;&nbsp;<wbr>&lt;port&gt;</p>
<dd>shows state of given home server</p>
<dt>show module&nbsp;<wbr>&lt;command&gt;</p>
<dd>do sub-command of module</p>
<dt>show module config&nbsp;<wbr>&lt;module&gt;</p>
<dd>show configuration for given module</p>
<dt>show module flags&nbsp;<wbr>&lt;module&gt;</p>
<dd>show other module properties</p>
<dt>show module list</p>
<dd>shows list of loaded modules</p>
<dt>show module methods&nbsp;<wbr>&lt;module&gt;</p>
<dd>show sections where &lt;module&gt; may be used</p>
<dt>show uptime</p>
<dd>shows time at which server started</p>
<dt>show version</p>
<dd>Prints version of the running server</p>
<dt>show xml&nbsp;<wbr>&lt;reference&gt;</p>
<dd>Prints out configuration as XML</p>
<dt>stats&nbsp;<wbr>&lt;command&gt;</p>
<dd>do sub-command of stats</p>
<dt>stats client&nbsp;<wbr>[auth/acct]&nbsp;<wbr>&lt;ipaddr&gt;</p>
<dd>show statistics for given client, or for all clients (auth or acct)</p>
<dt>stats home_server&nbsp;<wbr>[&lt;ipaddr&gt;/auth/acct]&nbsp;<wbr>&lt;port&gt;</p>
<dd>show statistics for given home server (ipaddr and port), or for all home servers (auth or acct)</p>
<dt>stats detail&nbsp;<wbr>&lt;filename&gt;</p>
<dd>show statistics for the given detail file</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-unlang/">unlang</a>(5), <a href="/docs/linux/man/5-radiusd-conf/">radiusd.conf</a>(5), raddb/sites-available/control-socket</p>
<h2>Author</h2>
<p>Alan DeKok &lt;aland [at] freeradius.org&gt;</p>
