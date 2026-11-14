---
title: "slapd(8)"
name: "slapd"
section: "8"
letter: "s"
url: "/docs/linux/man/8-slapd/"
description: "slapd – Stand-alone LDAP Daemon"
---

<p>slapd &#8211; Stand-alone LDAP Daemon</p>
<h2>Synopsis</h2>
<p><code>slapd</code> [<code>-4</code>|<code>-6</code>] [<code>-T</code>&nbsp;<wbr>{<code>acl</code>|<code>a</code>[<code>dd</code>]|<code>auth</code>|<code>c</code>[<code>at</code>]| <code>d</code>[<code>n</code>]|<code>i</code>[<code>ndex</code>]|<code>p</code>[<code>asswd</code>]|<code>s</code>[<code>chema</code>]|<code>t</code>[<code>est</code>]}] [<code>-d</code><i>&nbsp;<wbr>debug-level</i>] [<code>-f</code><i>&nbsp;<wbr>slapd-config-file</i>] [<code>-F</code><i>&nbsp;<wbr>slapd-config-directory</i>] [<code>-h</code><i>&nbsp;<wbr>URLs</i>] [<code>-n</code><i>&nbsp;<wbr>service-name</i>] [<code>-s</code><i>&nbsp;<wbr>syslog-level</i>] [<code>-l</code><i>&nbsp;<wbr>syslog-local-user</i>] [<code>-o</code><i>&nbsp;<wbr>option</i>[<code>=</code><i>value</i>]] [<code>-r</code><i>&nbsp;<wbr>directory</i>] [<code>-u</code><i>&nbsp;<wbr>user</i>] [<code>-g</code><i>&nbsp;<wbr>group</i>] [<code>-c</code><i>&nbsp;<wbr>cookie</i>]</p>
<h2>Description</h2>
<p><code>Slapd</code> is the stand-alone LDAP daemon. It listens for LDAP connections on any number of ports (default <code>389</code>), responding to the LDAP operations it receives over these connections. <code>slapd</code> is typically invoked at boot time, usually out of <code>/etc/rc.local</code>. Upon startup, <code>slapd</code> normally forks and disassociates itself from the invoking tty. If configured in the config file (or config directory), the <code>slapd</code> process will print its process ID (see <code><a href="/docs/linux/man/2-getpid/">getpid</a></code>(2)) to a <code>.pid</code> file, as well as the command line options during invocation to an <code>.args</code> file (see <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5)). If the <code>-d</code> flag is given, even with a zero argument, <code>slapd</code> will not fork and disassociate from the invoking tty. </p>
<p> See the &quot;OpenLDAP Administrator&#8217;s Guide&quot; for more details on <code>slapd</code>.</p>
<h2>Options</h2>
<dl>
<dt><code>-4</code></p>
<dd>Listen on IPv4 addresses only.</p>
<dt><code>-6</code></p>
<dd>Listen on IPv6 addresses only.</p>
<dt><code>-T</code><i>&nbsp;<wbr>tool</i></p>
<dd>Run in Tool mode. The <i>tool</i> argument selects whether to run as <i>slapadd</i>, <i>slapcat</i>, <i>slapdn</i>, <i>slapindex</i>, <i>slappasswd</i>, <i>slapschema</i>, or <i>slaptest</i> (<i>slapacl</i> and <i>slapauth</i> need the entire <code>acl</code> and <code>auth</code> option value to be spelled out, as <code>a</code> is reserved to <i>slapadd</i>). This option should be the first option specified when it is used; any remaining options will be interpreted by the corresponding slap tool program, according to the respective man pages. Note that these tool programs will usually be symbolic links to <code>slapd</code>. This option is provided for situations where symbolic links are not provided or not usable.</p>
<dt><code>-d</code><i>&nbsp;<wbr>debug-level</i></p>
<dd>Turn on debugging as defined by <i>debug-level</i>. If this option is specified, even with a zero argument, <code>slapd</code> will not fork or disassociate from the invoking terminal. Some general operation and status messages are printed for any value of <i>debug-level</i>. <i>debug-level</i> is taken as a bit string, with each bit corresponding to a different kind of debugging information. See &lt;ldap_log.h&gt; for details. Comma-separated arrays of friendly names can be specified to select debugging output of the corresponding debugging information. All the names recognized by the <i>loglevel</i> directive described in <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) are supported. If <i>debug-level</i> is <code>?</code>, a list of installed debug-levels is printed, and slapd exits. </p>
<p> Remember that if you turn on packet logging, packets containing bind passwords will be output, so if you redirect the log to a logfile, that file should be read-protected.</p>
<dt><code>-s</code><i>&nbsp;<wbr>syslog-level</i></p>
<dd>This option tells <code>slapd</code> at what debug-level debugging statements should be logged to the <code><a href="/docs/linux/man/8-syslog/">syslog</a></code>(8) facility. The value <i>syslog-level</i> can be set to any value or combination allowed by the <code>-d</code> switch. Slapd logs all messages selected by <i>syslog-leveli</i> at the <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) severity debug-level <code>DEBUG</code>, on the unit specified with <code>-l</code>.</p>
<dt><code>-n</code><i>&nbsp;<wbr>service-name</i></p>
<dd>Specifies the service name for logging and other purposes. Defaults to basename of argv[0], i.e.: &quot;slapd&quot;.</p>
<dt><code>-l</code><i>&nbsp;<wbr>syslog-local-user</i></p>
<dd>Selects the local user of the <code><a href="/docs/linux/man/8-syslog/">syslog</a></code>(8) facility. Value can be <code>LOCAL0</code>, through <code>LOCAL7</code>, as well as <code>USER</code> and <code>DAEMON</code>. The default is <code>LOCAL4</code>. However, this option is only permitted on systems that support local users with the <code><a href="/docs/linux/man/8-syslog/">syslog</a></code>(8) facility. Logging to <a href="/docs/linux/man/8-syslog/">syslog</a>(8) occurs at the &quot;DEBUG&quot; severity debug-level.</p>
<dt><code>-f</code><i>&nbsp;<wbr>slapd-config-file</i></p>
<dd>Specifies the slapd configuration file. The default is <code>/etc/openldap/slapd.conf</code>.</p>
<dt><code>-F</code><i>&nbsp;<wbr>slapd-config-directory</i></p>
<dd>Specifies the slapd configuration directory. The default is <code>/etc/openldap/slapd.d</code>. If both <code>-f</code> and <code>-F</code> are specified, the config file will be read and converted to config directory format and written to the specified directory. If neither option is specified, slapd will attempt to read the default config directory before trying to use the default config file. If a valid config directory exists then the default config file is ignored. All of the slap tools that use the config options observe this same behavior.</p>
<dt><code>-h</code><i>&nbsp;<wbr>URLlist</i></p>
<dd><code>slapd</code> will by default serve <code><a href="ldap:///">ldap:///</a></code> (LDAP over TCP on all interfaces on default LDAP port). That is, it will bind using INADDR_ANY and port <code>389</code>. The <code>-h</code> option may be used to specify LDAP (and other scheme) URLs to serve. For example, if slapd is given <code>-h &quot;<a href="ldap://127.0.0.1:9009/">ldap://127.0.0.1:9009/</a> <a href="ldaps:///">ldaps:///</a> <a href="ldapi:///">ldapi:///</a>&quot;</code>, it will listen on 127.0.0.1:9009 for LDAP, 0.0.0.0:636 for LDAP over TLS, and LDAP over IPC (Unix domain sockets). Host 0.0.0.0 represents INADDR_ANY (any interface). A space separated list of URLs is expected. The URLs should be of the LDAP, LDAPS, or LDAPI schemes, and generally without a DN or other optional parameters (excepting as discussed below). Support for the latter two schemes depends on selected configuration options. Hosts may be specified by name or IPv4 and IPv6 address formats. Ports, if specified, must be numeric. The default ldap:// port is <code>389</code> and the default ldaps:// port is <code>636</code>. </p>
<p> For LDAP over IPC, <code>name </code> is the name of the socket, and no <code>port</code> is required, nor allowed; note that directory separators must be URL-encoded, like any other characters that are special to URLs; so the socket </p>
<p>&nbsp;<wbr>&nbsp;<wbr>/usr/local/var/ldapi </p>
<p> must be specified as </p>
<p>&nbsp;<wbr>&nbsp;<wbr><a href="ldapi://%2Fusr%2Flocal%2Fvar%2Fldapi">ldapi://%2Fusr%2Flocal%2Fvar%2Fldapi</a> </p>
<p> The default location for the IPC socket is /var/run/ldapi </p>
<p> The listener permissions are indicated by &quot;x-mod=-rwxrwxrwx&quot;, &quot;x-mod=0777&quot; or &quot;x-mod=777&quot;, where any of the &quot;rwx&quot; can be &quot;-&quot; to suppress the related permission, while any of the &quot;7&quot; can be any legal octal digit, according to <a href="/docs/linux/man/1-chmod/">chmod</a>(1). The listeners can take advantage of the &quot;x-mod&quot; extension to apply rough limitations to operations, e.g. allow read operations (&quot;r&quot;, which applies to search and compare), write operations (&quot;w&quot;, which applies to add, delete, modify and modrdn), and execute operations (&quot;x&quot;, which means bind is required). &quot;User&quot; permissions apply to authenticated users, while &quot;other&quot; apply to anonymous users; &quot;group&quot; permissions are ignored. For example, &quot;<a href="ldap:///????x-mod=-rw-------">ldap:///????x-mod=-rw&#8212;&#8212;-</a>&quot; means that read and write is only allowed for authenticated connections, and bind is required for all operations. This feature is experimental, and requires to be manually enabled at configure time.</p>
<dt><code>-r</code><i>&nbsp;<wbr>directory</i></p>
<dd>Specifies a directory to become the root directory. slapd will change the current working directory to this directory and then <code><a href="/docs/linux/man/2-chroot/">chroot</a></code>(2) to this directory. This is done after opening listeners but before reading any configuration file or initializing any backend. When used as a security mechanism, it should be used in conjunction with <code>-u</code> and <code>-g</code> options.</p>
<dt><code>-u</code><i>&nbsp;<wbr>user</i></p>
<dd><code>slapd</code> will run slapd with the specified user name or id, and that user&#8217;s supplementary group access list as set with <a href="/docs/linux/man/3-initgroups/">initgroups</a>(3). The group ID is also changed to this user&#8217;s gid, unless the <code>-g</code> option is used to override. Note when used with <code>-r</code>, slapd will use the user database in the change root environment. </p>
<p> Note that on some systems, running as a non-privileged user will prevent passwd back-ends from accessing the encrypted passwords. Note also that any shell back-ends will run as the specified non-privileged user.</p>
<dt><code>-g</code><i>&nbsp;<wbr>group</i></p>
<dd><code>slapd</code> will run with the specified group name or id. Note when used with <code>-r</code>, slapd will use the group database in the change root environment.</p>
<dt><code>-c</code><i>&nbsp;<wbr>cookie</i></p>
<dd>This option provides a cookie for the syncrepl replication consumer. The cookie is a comma separated list of <i>name=value</i> pairs. Currently supported syncrepl cookie fields are <code>rid</code>, <code>sid</code>, and <code>csn</code>. <code>rid</code> identifies a replication thread within the consumer server and is used to find the syncrepl specification in <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) or <code><a href="/docs/linux/man/5-slapd-config/">slapd-config</a></code>(5) having the matching replication identifier in its definition. The <code>rid</code> must be provided in order for any other specified values to be used. <code>sid</code> is the server id in a multi-master/mirror-mode configuration. <code>csn</code> is the commit sequence number received by a previous synchronization and represents the state of the consumer replica content which the syncrepl engine will synchronize to the current provider content. In case of <i>mirror-mode</i> or <i>multi-master</i> replication agreement, multiple <code>csn</code> values, semicolon separated, can appear. Use only the <code>rid</code> part to force a full reload.</p>
<dt><code>-o</code><i>&nbsp;<wbr>option</i>[<code>=</code><i>value</i>]</p>
<dd>This option provides a generic means to specify options without the need to reserve a separate letter for them. </p>
<p> It supports the following options:</p>
<dl>
<dd>
<dl>
<dt><code>slp=</code>{<code>on</code>|<code>off</code>|<i>slp-attrs</i>}</p>
<dd>When SLP support is compiled into slapd, disable it (<code>off</code>),<br />
&nbsp;<wbr>enable it by registering at SLP DAs without specific SLP attributes&nbsp;<wbr>(<code>on</code>), or with specific SLP attributes <i>slp-attrs</i> that must be an SLP attribute list definition according to the SLP standard. </p>
<p> For example, <code>&quot;slp=(tree=production),(server-type=OpenLDAP),(server-version=2.4.15)&quot;</code> registers at SLP DAs with the three SLP attributes tree, server-type and server-version that have the values given above. This allows to specifically query the SLP DAs for LDAP servers holding the <i>production</i> tree in case multiple trees are available.</dl>
</dl>
</dl>
<h2>Examples</h2>
<p>To start <i>slapd</i> and have it fork and detach from the terminal and start serving the LDAP databases defined in the default config file, just type: </p>
<pre> slapd</pre>
<p>To start <code>slapd</code> with an alternate configuration file, and turn on voluminous debugging which will be printed on standard error, type: </p>
<pre> slapd -f /var/tmp/slapd.conf -d 255</pre>
<p>To test whether the configuration file is correct or not, type: </p>
<pre> slapd -Tt</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-ldap/">ldap</a></code>(3), <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5), <code><a href="/docs/linux/man/5-slapd-config/">slapd-config</a></code>(5), <code><a href="/docs/linux/man/5-slapd-access/">slapd.access</a></code>(5), <code><a href="/docs/linux/man/8-slapacl/">slapacl</a></code>(8), <code><a href="/docs/linux/man/8-slapadd/">slapadd</a></code>(8), <code><a href="/docs/linux/man/8-slapauth/">slapauth</a></code>(8), <code><a href="/docs/linux/man/8-slapcat/">slapcat</a></code>(8), <code><a href="/docs/linux/man/8-slapdn/">slapdn</a></code>(8), <code><a href="/docs/linux/man/8-slapindex/">slapindex</a></code>(8), <code><a href="/docs/linux/man/8-slappasswd/">slappasswd</a></code>(8), <code><a href="/docs/linux/man/8-slapschema/">slapschema</a></code>(8), <code><a href="/docs/linux/man/8-slaptest/">slaptest</a></code>(8). </p>
<p> &quot;OpenLDAP Administrator&#8217;s Guide&quot; (<a rel="nofollow" href="http://www.OpenLDAP.org/doc/admin/)">http://www.OpenLDAP.org/doc/admin/)</a></p>
<h2>Bugs</h2>
<p>See <a rel="nofollow" href="http://www.openldap.org/its/">http://www.openldap.org/its/</a></p>
<h2>Acknowledgements</h2>
<p><code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release.</p>
