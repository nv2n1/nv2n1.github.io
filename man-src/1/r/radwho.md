---

title: "radwho(1)"
name: "radwho"
section: "1"
letter: "r"
url: "/docs/linux/man/1-radwho/"
description: "radwho – show online users"
---

<p> radwho &#8211; show online users</p>
<h2>SYNOPSIS</h2>
<p> <code>radwho</code> [<code>-c</code>] [<code>-d</code> <i>raddb_directory</i>] [<code>-F</code> <i>radutmp_file</i>] [<code>-i</code>] [<code>-n</code>] [<code>-N</code> <i>nas_ip_address</i>] [<code>-p</code>] [<code>-P</code> <i>nas_port</i>] [<code>-r</code>] [<code>-R</code>] [<code>-s</code>] [<code>-S</code>] [<code>-u</code> <i>user</i>] [<code>-U</code> <i>user</i>] [<code>-Z</code>]</p>
<h2>DESCRIPTION</h2>
<p> The FreeRADIUS server can be configured to maintain an active session database in a file called <i>radutmp</i>. This utility shows the content of that session database.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-c</dt>
<dd> Shows caller ID (if available) instead of the full name.</dd>
<dt>-d&nbsp;<wbr><i>raddb_directory</i></dt>
<dd> The directory that contains the RADIUS configuration files. Defaults to <i>/etc/raddb</i>.</dd>
<dt>-F&nbsp;<wbr><i>radutmp_file</i></dt>
<dd> The file that contains the radutmp file. If this is specified, -d is not necessary.</dd>
<dt>-i</dt>
<dd> Shows the session ID instead of the full name.</dd>
<dt>-n</dt>
<dd> Normally radwho looks up the username in the systems password file, and shows the full username as well. The <code>-n</code> flags prevents this.</dd>
<dt>-N&nbsp;<wbr><i>nas_ip_address</i></dt>
<dd> Show only those entries which match the given NAS IP address.</dd>
<dt>-p</dt>
<dd> Adds an extra column for the port type &#8211; I for ISDN, A for Analog.</dd>
<dt>-P&nbsp;<wbr><i>nas_port</i></dt>
<dd> Show only those entries which match the given NAS port.</dd>
<dt>-r</dt>
<dd> Outputs all data in <i>raw</i> format &#8211; no headers, no formatting, fields are comma-separated.</dd>
<dt>-R</dt>
<dd> Output all data in RADIUS attribute format. All fields are printed.</dd>
<dt>-s</dt>
<dd> Show full name.</dd>
<dt>-S</dt>
<dd> Hide shell users. Doesn&#8217;t show the entries for users that do not have a SLIP or PPP session.</dd>
<dt>-u&nbsp;<wbr><i>user</i></dt>
<dd> Show only those entries which match the given username (case insensitive).</dd>
<dt>-U&nbsp;<wbr><i>user</i></dt>
<dd> Show only those entries which match the given username (case sensitive).</dd>
<dt>-Z</dt>
<dd> When combined with <i>-R</i>, prints out the contents of an Accounting-Request packet which can be passed to <i>radclient</i>, in order to &quot;zap&quot; that users session from <i>radutmp</i>.</dd></dl>
<p> For example,</p>
<dl>
<dt>
</dt><dd>
<pre>
$ radwho -ZRN 10.0.0.1 | radclient -f - radius.example.net acct testing123
</pre>
</dd></dl>
<p> will result in all an Accounting-Request packet being sent to the RADIUS server, which tells the server that the NAS rebooted. i.e. It &quot;zaps&quot; all of the users on that NAS. </p>
<p> To &quot;zap&quot; one user, specifiy NAS, username, and NAS port:</p>
<dl>
<dt>
</dt><dd>
<pre>
$ radwho -ZRN 10.0.0.1 -u user -P 10 | radclient -f - radius.example.net acct testing123
</pre>
</dd></dl>
<p> Other combinations are also possible. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/8-radiusd/">radiusd</a>(8), <a href="/docs/linux/man/1-radclient/">radclient</a>(1), <a href="/docs/linux/man/5-radiusd-conf/">radiusd.conf</a>(5).</p>
<h2>AUTHOR</h2>
<p> Miquel van Smoorenburg, miquels [at] cistron.nl. </p>
