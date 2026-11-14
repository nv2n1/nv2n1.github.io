---
title: "raddebug(8)"
name: "raddebug"
section: "8"
letter: "r"
url: "/docs/linux/man/8-raddebug/"
description: "raddebug – Display debugging output from a running server."
---

<p>raddebug &#8211; Display debugging output from a running server.</p>
<h2>Synopsis</h2>
<p><code>raddebug</code> [<code>-c</code> <i>condition</i>] [<code>-d</code> <i>config_directory</i>] [<code>-i</code> <i>ipv4-address</i>] [<code>-I</code> <i>ipv6-address</i>] [<code>-f</code> <i>socket_file</i>] [<code>-t</code> <i>timeout</i>] [<code>-u</code> <i>user-name</i>]</p>
<h2>Description</h2>
<p><code>raddebug</code> is a shell script wrapper around <code>radmin</code> that automates the process of obtaining debugging output from a running server. It does this without impacting service availability, unlike using <code>radiusd -X</code>. There are a number of prerequisites that are required for its proper operation: </p>
<p> * <code>radmin</code> must be available in the PATH.<br />
 * The user running <code>raddebug</code> must have permission to connect to<br />
&nbsp;<wbr>&nbsp;<wbr>the server control socket.<br />
 * The control socket must be configured. For instructions, see<br />
&nbsp;<wbr>&nbsp;<wbr>raddb/sites-available/control-socket<br />
 * The control socket must be marked as &quot;mode = rw&quot;.<br />
 * The user running <code>raddebug</code> must have permission to read and<br />
&nbsp;<wbr>&nbsp;<wbr>write files in the&nbsp;<wbr>&quot;logdir&quot;&nbsp;<wbr>directory.&nbsp;<wbr>&nbsp;<wbr>This is usually<br />
&nbsp;<wbr>&nbsp;<wbr>/var/log/radiusd. </p>
<p> For a number of reasons, the debugging output is placed in an intermediate file, rather than being sent directly to standard output. In order to prevent this file from growing too large, the <code>raddebug</code> program is automatically terminated after 10 seconds. This timeout can be changed via the &quot;-t&quot; parameter. </p>
<p> When the script exits, debug mode in the server is disabled, and the intermediate file is deleted. </p>
<p> Debug output from a live server can be redirected to only one location. If a second instance of <i>raddebug</i> is started while the first one is still running, the later one will over-ride the first one, and the first will stop producing output.</p>
<h2>Options</h2>
<dl>
<dt>-c&nbsp;<wbr><i>condition</i></p>
<dd>Set a specific debug condition. The format of the condition is as specified in the CONDITIONS section of the <i>unlang</i> manual page.</p>
<dt>-f&nbsp;<wbr><i>socket_file</i></p>
<dd>The path to the control socket. See the <i>radmin</i> manual page for more description of this option.</p>
<dt>-i&nbsp;<wbr><i>ipv4-address</i></p>
<dd>Show debug output for the client having the given IPv4 address. This option is equivalent to using:<br />
 -c &#8216;(Packet-Src-IP-Address == ipv4-address)&#8217;</p>
<dt>-d <i>config directory</i></p>
<dd>The radius configuration directory, usually /etc/raddb. See the <i>radmin</i> manual page for more description of this option.</p>
<dt>-I&nbsp;<wbr><i>ipv6-address</i></p>
<dd>Show debug output for the client having the given IPv6 address. This option is equivalent to using:<br />
 -c &#8216;(Packet-Src-IPv6-Address == ipv6-address)&#8217;</p>
<dt>-t&nbsp;<wbr><i>timeout</i></p>
<dd>Stop printing debug output after &quot;timeout&quot; seconds. The default timeout is sixty (60) seconds. Use &quot;-t 0&quot; to print debugging output forever, or until the script exits.</p>
<dt>-u&nbsp;<wbr><i>name</i></p>
<dd>Show debug output for users having the given name. This option is equivalent to using:<br />
 -c &#8216;(User-Name == name)&#8217; </p>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-radmin/">radmin</a>(8), raddb/sites-available/control-socket, <a href="/docs/linux/man/5-unlang/">unlang</a>(5), <a href="/docs/linux/man/5-radiusd-conf/">radiusd.conf</a>(5)</p>
<h2>Authors</h2>
<p>Alan DeKok &lt;aland [at] freeradius.org&gt;</p>
