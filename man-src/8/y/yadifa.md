---
title: "yadifa(8)"
name: "yadifa"
section: "8"
letter: "y"
url: "/docs/linux/man/8-yadifa/"
description: "YADIFA is an utility for controlling YADIFAD"
---

<p>YADIFA is an utility for controlling YADIFAD </p>
<h2>Synopsis</h2>
<p>yadifa [<code>&#8211;config|-c</code><i> configfile</i>] [<code>-s</code><i> host</i>] [<code>@host </code>] [<code>-K</code><i> key-name</i>] [<code>&#8211;version|-V</code>] [<code>-h</code>] [<code>&#8211;verbose|-v</code>] <code>[-t]</code><i> command</i> [<code>[-q]</code><i> zone</i>] </p>
<h2>Description</h2>
<p>yadifa controls the operation of yadifad. yadifa communicates with a name server over a TCP connection. The protocol used between client &#8211; server is an extension of the DNS protocol. The authentication is done by a mutual key between client and server. This key has the same format as a TSIG. Authentication is not needed, but provides more secure communication if used. Several algorithms can be used for creating a TSIG:</p>
<dl>
<dt><code>*</code></p>
<dd>HMAC-MD5</p>
<dt><code>*</code></p>
<dd>HMAC-SHA1</dl>
<h2>Options</h2>
<dl>
<dt>[<code>&#8211;config|-c </code><i>configfile</i>]</p>
<dd>&nbsp;<wbr>Another config file will be used.&nbsp;<wbr></p>
<dt>[<code>&#8211;server|-s </code><i>host</i>] | [<code> @host </code>]</p>
<dd>&nbsp;<wbr>Host is the remote server to operate.&nbsp;<wbr> If used with a different port: e.g.: ./yadifa &#8211;server &quot;192.0.2.1 port 5353&quot;</p>
<dt>[<code>-k </code><i>key-name</i>]</p>
<dd>&nbsp;<wbr>Name of the key to be used for the controller.&nbsp;<wbr></p>
<dt>[<code>&#8211;verbose|-v</code>]</p>
<dd>&nbsp;<wbr>verbose output.&nbsp;<wbr></p>
<dt>[<code>&#8211;version|-V</code>]</p>
<dd>&nbsp;<wbr>Show version information.&nbsp;<wbr></p>
<dt>[<code>&#8211;help|-h</code>]</p>
<dd>&nbsp;<wbr>Show a help text&nbsp;<wbr></dl>
<h2>Commands</h2>
<dl>
<dt>[<code>-t</code>] freeze [<code>-q</code>] zone</p>
<dd>&nbsp;<wbr>disables updates to a zone.&nbsp;<wbr></dl>
<dl>
<dt>[<code>-t</code>] unfreeze [<code>-q</code>] zone</p>
<dd>&nbsp;<wbr>enables updates to a zone.&nbsp;<wbr></dl>
<dl>
<dt>[<code>-t</code>] reload [<code>-q</code>] zone</p>
<dd>&nbsp;<wbr>triggers the loading of the zone file(s)&nbsp;<wbr>if the serial number is incremented.&nbsp;<wbr></p>
<dt>[<code>-t</code>] cfgreload</p>
<dd>&nbsp;<wbr>reload the settings from the configuration file.&nbsp;<wbr></dl>
<dl>
<dt>[<code>-t</code>] zonecfgreload</p>
<dd>[<code>-q </code><i>zone</i>]<br />
&nbsp;<wbr>reload the zone information in the configuration file and reload the zone file(s)&nbsp;<wbr>with increased serial number.&nbsp;<wbr> If a zone is specified only that zone section is reloaded.</p>
<dt>[<code>-t</code>] sync [<code>-q</code>] zone [<code>&#8211;clean</code>]</p>
<dd>&nbsp;<wbr>write the zone to disk and optionally removes the journal.&nbsp;<wbr> The extra [&#8211;clean] option will remove the journal.</p>
<dt>[<code>-t</code>] querylog &#8211;enable|&#8211;disable</p>
<dd>&nbsp;<wbr>sets the log for queries on or off.&nbsp;<wbr></p>
<dt>[<code>-t</code>] loglevel {&#8211;level|-l} level</p>
<dd>&nbsp;<wbr>sets the log level to the given value&nbsp;<wbr>(0-15).&nbsp;<wbr></p>
<dt>[<code>-t</code>] logreopen</p>
<dd>&nbsp;<wbr>close all log files and reopens them.&nbsp;<wbr></p>
<dt>[<code>-t</code>] shutdown</p>
<dd>&nbsp;<wbr>shuts down the server.&nbsp;<wbr></dl>
<h2>Files</h2>
<dl>
<dt>yadifa</p>
<dd>&nbsp;<wbr>The name server remote client.&nbsp;<wbr></p>
<dt>SYSCONFDIR/yadifa.conf</p>
<dd>&nbsp;<wbr>The default yadifa configuration file.&nbsp;<wbr></p>
<dt>$HOME/.yadifa.rc</p>
<dd>&nbsp;<wbr>default rcfile.&nbsp;<wbr></dl>
<dl>
<dt>yadifa.rc.5</p>
<dd>&nbsp;<wbr>Configuration man page for yadifa.</p>
<dt>yadifa.8</p>
<dd>&nbsp;<wbr>This man page.&nbsp;<wbr></dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-yadifa-rc/">yadifa.rc</a></i>(5) <i><a href="/docs/linux/man/8-yadifad/">yadifad</a></i>(8) </p>
<h2>Requirements</h2>
<dl>
<dt>OpenSSL</p>
<dd>yadifad requires OpenSSL version 0.9.8 or later.</dl>
<h2>Changes</h2>
<p>Please check the ChangeLog file from the sources code.</p>
<h2>Version</h2>
<p>Version: 2.2.5 of 2017-04-20.</p>
<h2>Mailinglist</h2>
<p>There is a mailinglist for questions relating to any program in the yadifa package: </p>
<dl>
<dt><code>*</code></p>
<dd><code>yadifa-users [at] mailinglists.yadifa.eu</code><br />
 for submitting questions/answers.</dl>
<dl>
<dt><code>*</code></p>
<dd><code><a rel="nofollow" href="http://www.yadifa.eu/mailing-list-users">http://www.yadifa.eu/mailing-list-users</a></code><br />
 for subscription requests.</dl>
<p> If you would like to stay informed about new versions and official patches send a subscription request to via:</p>
<dl>
<dt><code>*</code></p>
<dd><code><a rel="nofollow" href="http://www.yadifa.eu/mailing-list-announcements">http://www.yadifa.eu/mailing-list-announcements</a></code></dl>
<p> (this is a read-only list).</p>
<h2>License And Copyright</h2>
<dl>
<dt>Copyright</p>
<dd>(C)2011-2017, EURid<br />
 B-1831 Diegem, Belgium<br />
 <code>info [at] yadifa.eu</code></dl>
<h2>Authors</h2>
<p>Gery Van Emelen<br />
 Email: <code>Gery.VanEmelen [at] EURid.eu</code><br />
 Eric Diaz Fernandez<br />
 Email: <code>Eric.DiazFernandez [at] EURid.eu</code> </p>
<p> WWW: <code><a rel="nofollow" href="http://www.EURid.eu">http://www.EURid.eu</a></code></p>
