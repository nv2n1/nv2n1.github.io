---
title: "radtest(1)"
name: "radtest"
section: "1"
letter: "r"
url: "/docs/linux/man/1-radtest/"
description: "radtest – send packets to a RADIUS server, show reply"
---

<h2>NAME</h2>
<p> radtest &#8211; send packets to a RADIUS server, show reply</p>
<h2>SYNOPSIS</h2>
<p> <code>radtest</code> [<code>-d</code> <i>raddb_directory</i>] [<code>-P</code> <i>tcp/udp</i>] [<code>-t</code> <i>pap/chap/mschap/eap-md5</i>] [<code>-x</code> <i>]</i> [<code>-4</code> <i>]</i> [<code>-6</code> <i>]</i> <i>user password radius-server nas-port-number secret</i> [<code>ppphint</code>] [<code>nasname</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code>radtest</code> is a frontend to <code><a href="/docs/linux/man/1-radclient/">radclient</a></code>(1). It generates a list of attribute/value pairs based on the command line arguments, and feeds these into <code>radclient</code>. It&#8217;s a fast and convenient way to test a radius server. </p>
<h2>OPTIONS</h2>
<dl>
<dt>-d <i>raddb_directory</i></p>
<dd> The directory that contains the RADIUS dictionary files. Defaults to <i>/etc/raddb</i>. </p>
<dt>-P&nbsp;<wbr><i>proto</i></p>
<dd> Use <i>proto</i> transport protocol (&quot;tcp&quot; or &quot;udp&quot;). Only available if FreeRADIUS is compiled with TCP transport support. </p>
<dt>-t <i>pap/chap/mschap/eap-md5</i></p>
<dd> Choose the authentiction method to use. e.g. &quot;-t pap&quot;, &quot;-t chap&quot;, &quot;-t mschap&quot;, or &quot;-t eap-md5&quot;,. Defaults to &quot;pap&quot;. Using EAP-MD5 requires that the &quot;radeapclient&quot; program is installed. </p>
<dt>-x</p>
<dd> Enables debugging output for the RADIUS client. </p>
<dt>-4</p>
<dd> Use NAS-IP-Address for the NAS address (default) </p>
<dt>-6</p>
<dd> Use NAS-IPv6-Address for the NAS address (default) </p>
<dt>user</p>
<dd> Username to send. </p>
<dt>password</p>
<dd> Password of the user. </p>
<dt>radius-server</p>
<dd> Hostname or IP address of the radius server. Optionally, you may specify a port by appending :port </p>
<dt>nas-port-number</p>
<dd> The value of the NAS-Port attribute. Is an integer between 0 and 2^31, and it really doesn&#8217;t matter what you put here. <i>10</i> will do fine. </p>
<dt>secret</p>
<dd> The shared secret for this client. </p>
<dt>ppphint</p>
<dd> If you put an integer &gt; 0 here, radtest (or actually radclient) will add the attribute <i>Framed-Protocol = PPP</i> to the request packet. </p>
<dt>nasname</p>
<dd> If present, this will be resolved to an IP address and added to the request packet as the <i>NAS-IP-Address</i> attribute. If you don&#8217;t specify it, the local hostname of the system will be used. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/8-radiusd/">radiusd</a>(8), <a href="/docs/linux/man/1-radclient/">radclient</a>(1).</p>
<h2>AUTHOR</h2>
<p> Miquel van Smoorenburg, miquels [at] cistron.nl. </p>
<h2>Index</h2>
