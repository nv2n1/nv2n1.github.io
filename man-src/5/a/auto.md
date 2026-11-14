---
title: "auto(5)"
name: "auto"
section: "5"
letter: "a"
url: "/docs/linux/man/5-auto/"
description: "auto.master – Master Map for automounter"
---

<p>auto.master &#8211; Master Map for automounter</p>
<h2>Description</h2>
<p>The <code>auto.master</code> map is consulted to set up automount managed mount points when the <code><a href="/docs/linux/man/8-autofs/">autofs</a></code>(8) script is invoked or the <code><a href="/docs/linux/man/8-automount/">automount</a></code>(8) program is run. Each line describes a mount point and refers to an autofs map describing file systems to be mounted under the mount point. The default location of the master map is <code>/etc/auto.master</code> but an alternate name may be given on the command line when running the automounter and the default master map may changed by setting the <code>MASTER_MAP_NAME</code> configuration variable in <code>/etc/sysconfig/autofs.</code> If the master map name has no path then the system Name Service Switch configuration will be consulted and each of the sources searched in line with the rules given in the Name Service Switch configuration. Access to mounts in maps is governed by a key. For direct maps the mount point is always specified as: /- and the key used within the direct map is the full path to the mount point. For indirect maps access is by using the path scheme: /<i>mount-point</i>/<i>key</i> where <i>mount-point</i> is one of the entries listed in the master map. The <i>key</i> is a single directory component and is matched against entries in the map given in the entry (See <code><a href="/docs/linux/man/5-autofs/">autofs</a></code>(5)). Additionally, a map may be included from its source as if it were itself present in the master map by including a line of the form: <code>+&nbsp;<wbr>[</code>maptype<code>,</code>format<code>:]</code>map<code>[</code>options<code>]</code> and <code><a href="/docs/linux/man/8-automount/">automount</a></code>(8) will process the map according to the specification described below for map entries.</p>
<h2>Format</h2>
<p>Master map entries have three fields separated by an arbitrary number of spaces or tabs. Lines beginning with # are comments. The first field is the mount point described above and the second field is the name of the map to be consulted for the mount point followed by the third field which contains options to be applied to all entries in the map. The format of a master map entry is:</p>
<dl>
<dt><i>mount-point&nbsp;<wbr></i>[<i>map-type</i>[,<i>format</i>]:]<i>map&nbsp;<wbr></i>[<i>options</i>]</p>
<dd>
<dt><code>mount-point</code></p>
<dd>Base location for the <code>autofs</code> filesystem to be mounted. For indirect maps this directory will be created (as with <code>mkdir -p</code>) and is removed when the <code>autofs</code> filesystem is umounted.</p>
<dt><code>map-type</code></p>
<dd>Type of map used for this mount point. The following are valid map types:</p>
<dl>
<dd>
<dl>
<dt><code>file</code></p>
<dd>The map is a regular text file.</p>
<dt><code>program</code></p>
<dd>The map is an executable program, which is passed a key on the command line and returns an entry (everything besides the key) on stdout if successful.</p>
<dt><code>yp</code></p>
<dd>The map is a NIS (YP) database.</p>
<dt><code>nisplus</code></p>
<dd>The map is a NIS+ database.</p>
<dt><code>hesiod</code></p>
<dd>The map is a hesiod database whose <code>filsys</code> entries are used for maps.</p>
<dt><code>ldap </code>or<code> ldaps</code></p>
<dd>The map is stored in an LDAP directory. If <code>ldaps</code> is used the appropriate certificate must be configured in the LDAP client.</p>
<dt><code>multi</code></p>
<dd>This map type allows the specification of multiple maps separated by &quot;&#8211;&quot;. These maps are searched in order to resolve key lookups.</dl>
</dl>
<dt><code>format</code></p>
<dd>Format of the map data; currently the only formats recognized are <code>sun</code>, which is a subset of the Sun automounter map format, and <code>hesiod</code>, for hesiod filesys entries. If the format is left unspecified, it defaults to <code>sun</code> for all map types except <code>hesiod</code>.</p>
<dt><code>map</code></p>
<dd>Name of the map to use. This is an absolute UNIX pathname for maps of types <code>file</code> or <code>program</code>, and the name of a database in the case for maps of type <code>yp</code>, <code>nisplus</code>, or <code>hesiod</code> or the <code>dn</code> of an LDAP entry for maps of type <code>ldap</code>.</p>
<dt><code>options</code></p>
<dd>Any remaining command line arguments without leading dashes (-) are taken as options (<i>-o</i>) to <code>mount</code>. Arguments with leading dashes are considered options for the maps. </p>
<p> The <code>sun</code> format supports the following options:</p>
<dl>
<dd>
<dl>
<dt><i>-Dvariable=value</i></p>
<dd>Replace <i>variable</i> with <i>value</i> in map substitutions.</p>
<dt><i>-strict</i></p>
<dd>Treat errors when mounting file systems as fatal. This is important when multiple file systems should be mounted (`multimounts&#8217;). If this option is given, no file system is mounted at all if at least one file system can&#8217;t be mounted.</p>
<dt><i>nosymlink</i></p>
<dd>This is an autofs specific option that is a pseudo mount option and so is given without a leading dash. Historically this option was used to prevent symlinking of local NFS mounts. Nowadays it can be used to prevent bind mounting of local NFS filesystems as well. If you need to prevent bind mounting for only specific entrys in a map then this can be done by adding the &quot;port=&quot; mount option to the given entries.</p>
<dt><i>-r, &#8211;random-multimount-selection</i></p>
<dd>Enables the use of ramdom selection when choosing a host from a list of replicated servers. This option is applied to this mount only, overriding the global setting that may be specified on the command line.</p>
<dt><i>-n, &#8211;negative-timeout &lt;seconds&gt;</i></p>
<dd>Set the timeout for caching failed key lookups. This option can be used to override the global default given either on the command line or in the configuration.</dl>
</dl>
</dl>
<h2>General System Defaults Configuration</h2>
<p>The default value of several general settings may be changed in the configuration file <code>/etc/sysconfig/autofs</code>. They are:</p>
<dl>
<dt><code>TIMEOUT</code></p>
<dd>sets the default mount timeout (program default 600).</p>
<dt><code>NEGATIVE_TIMEOUT</code></p>
<dd>Set the default timeout for caching failed key lookups (program default 60). If the equivalent command line option is given it will override this setting.</p>
<dt><code>MOUNT_WAIT</code></p>
<dd>Set the default time to wait for a response from a spawned <a href="/docs/linux/man/8-mount/">mount</a>(8) before sending it a SIGTERM. Note that we still need to wait for the RPC layer to timeout before the sub-process exits so this isn&#8217;t ideal but it is the best we can do. The default is to wait until <a href="/docs/linux/man/8-mount/">mount</a>(8) returns without intervention.</p>
<dt><code>UMOUNT_WAIT</code></p>
<dd>Set the default time to wait for a response from a spawned <a href="/docs/linux/man/8-umount/">umount</a>(8) before sending it a SIGTERM. Note that we still need to wait for the RPC layer to timeout before the sub-process exits so this isn&#8217;t ideal but it is the best we can do.</p>
<dt><code>BROWSE_MODE</code></p>
<dd>Maps are browsable by default (program default &quot;yes&quot;).</p>
<dt><code>MOUNT_NFS_DEFAULT_PROTOCOL</code></p>
<dd>Specify the default protocol used by <a href="/docs/linux/man/8-mount-nfs/">mount.nfs</a>(8) (program default 3). Since we can&#8217;t identify this default automatically we need to set it in the autofs configuration. This option will only make a difference for replicated map entries as availability probing isn&#8217;t used for single host map entries.</p>
<dt><code>APPEND_OPTIONS</code></p>
<dd>Determine whether global options, given on the command line or per mount in the master map, are appended to map entry options or if the map entry options replace the global options (program default &quot;yes&quot;, append options).</p>
<dt><code>LOGGING</code></p>
<dd>set default log level &quot;none&quot;, &quot;verbose&quot; or &quot;debug&quot; (program default &quot;none&quot;).</dl>
<h2>BUILTIN MAP -hosts</h2>
<p>If &quot;-hosts&quot; is given as the map then accessing a key under the mount point which corresponds to a hostname will allow access to the exports of that host. For example, with an entry in the master map of <code>/net -hosts</code> accessing /net/myserver will mount exports from myserver on directories below /net/myserver. NOTE: mounts done from a hosts map will be mounted with the &quot;nosuid,nodev,intr&quot; options unless overridden by explicily specifying the &quot;suid&quot;, &quot;dev&quot; or &quot;nointr&quot; options in the master map entry.</p>
<h2>Ldap Maps</h2>
<p>If the map type <code>ldap</code> is specified the mapname is of the form <code>[//servername/]dn</code>, where the optional <code>servername</code> is the name of the LDAP server to query, and <code>dn</code> is the Distinguished Name of a subtree to search for map entries. The old style <code>ldap:servername:mapname</code> is also understood. Alternatively, the type can be obtained from the Name Service Switch configuration, in which case the map name alone must be given. If no schema is set in the autofs configuration then autofs will check each of the commonly used schema for a valid entry and if one is found it will used for subsequent lookups. There are three common schemas in use:</p>
<dl>
<dt><i>nisMap</i></p>
<dd>Entries in the <code>nisMap</code> schema are <code>nisObject</code> objects in the specified subtree, where the <code>cn</code> attribute is the key (the wildcard key is &quot;/&quot;), and the <code>nisMapEntry</code> attribute contains the information used by the automounter.</p>
<dt><i>automountMap</i></p>
<dd>The <code>automountMap</code> schema has two variations that differ in the attribute used for the map key. Entries in the automountMap schema are <code>automount</code> objects in the specified subtree, where the <code>cn</code> or <code>automountKey</code> attribute (depending on local usage) is the key (the wildcard key is &quot;/&quot;), and the <code>automountInformation</code> attribute contains the information used by the automounter. Note that the <code>cn</code> attribute is case insensitive. The object classes and attributes used for accessing automount maps in LDAP can be changed by setting entries in the autofs configuration located in <code>/etc/sysconfig/autofs</code>.</p>
<dt><code>NOTE:</code></p>
<dd>If a schema is given in the configuration then all the schema configuration values must be set, any partial schema specification will be ignored. The configuration settings available are:</p>
<dt><code>LDAP_TIMEOUT</code></p>
<dd>Set the network response timeout (default 8). Set timeout value for the synchronous API calls. The default is the LDAP library default of an infinite timeout.</p>
<dt><code>LDAP_NETWORK_TIMEOUT</code></p>
<dd>Set the network response timeout (default 8).</p>
<dt><code>LDAP_URI</code></p>
<dd>A space seperated list of server uris of the form &lt;proto&gt;://&lt;server&gt;[/] where &lt;proto&gt; can be ldap or ldaps. The option can be given multiple times. Map entries that include a server name override this option and it is then not used. Default is an empty list in which case either the server given in a map entry or the LDAP configured default is used. This uri list is read at startup and whenever the daemon receives a HUP signal. This configuration option can also be used to request autofs lookup SRV RRs for a domain of the form &lt;proto&gt;:///[&lt;domain dn&gt;]. Note that a trailing &quot;/&quot; is not allowed when using this form. If the domain dn is not specified the dns domain name (if any) is used to construct the domain dn for the SRV RR lookup. The server list returned from an SRV RR lookup is refreshed according to the minimum ttl found in the SRV RR records or after one hour, whichever is less.</p>
<dt><code>SEARCH_BASE</code></p>
<dd>The base dn to use when searching for amap base dn. This entry may be given multiple times and each will be checked for a map base dn in the order they occur in the configuration. The search base list is read at startup and whenever the daemon recieves a HUP signal.</p>
<dt><code>MAP_OBJECT_CLASS</code></p>
<dd>The map object class. In the <code>nisMap</code> schema this corresponds to the class <code>nisMap</code> and in the <code>automountMap</code> schema it corresponds to the class <code>automountMap</code>.</p>
<dt><code>ENTRY_OBJECT_CLASS</code></p>
<dd>The map entry object class. In the <code>nisMap</code> schema this corresponds to the class <code>nisObject</code> and in the <code>automountMap</code> schema it corresponds to the class <code>automount</code>.</p>
<dt><code>MAP_ATTRIBUTE</code></p>
<dd>The attribute used to identify the name of the map to which this entry belongs. In the <code>nisMap</code> schema this corresponds to the attribute <code>nisMapName</code> and in the <code>automountMap</code> schema it corresponds to the attribute <code>ou</code> or <code>automountMapName</code>.</p>
<dt><code>ENTRY_ATTRIBUTE</code></p>
<dd>The attribute used to identify a map key. In the <code>nisMap</code> schema this corresponds to the attribute <code>cn</code> and in the <code>automountMap</code> schema it corresponds to the attribute <code>automountKey</code>.</p>
<dt><code>VALUE_ATTRIBUTE</code></p>
<dd>The attribute used to identify the value of the map entry. In the <code>nisMap</code> schema this corresponds to the attribute <code>nisMapEntry</code> and in the <code>automountMap</code> schema it corresponds to the attribute <code>automountInformation</code>.</p>
<dt><code>NOTE:</code></p>
<dd>It is essential that entries use class and attribute in a consistent manner for correct operation of autofs. For example mixing <code>cn</code> and <code>automountKey</code> attributes in <code>automount</code> schema map entries won&#8217;t work as expected.</dl>
<h2>Ldap Authentication, Encrypted And Certified Connections</h2>
<p>LDAP authenticated binds, TLS encrypted connections and certification may be used by setting appropriate values in the autofs authentication configuration file and configuring the LDAP client with appropriate settings. The default location of this file is <code>/etc/autofs_ldap_auth.conf</code>. If this file exists it will be used to establish whether TLS or authentication should be used. An example of this file is: </p>
<dl>
<dd>
<pre>&lt;?xml version=&quot;1.0&quot; ?&gt;
&lt;autofs_ldap_sasl_conf
 usetls=&quot;yes&quot;
 tlsrequired=&quot;no&quot;
 authrequired=&quot;no&quot;
 authtype=&quot;DIGEST-MD5&quot;
 user=&quot;xyz&quot;
 secret=&quot;abc&quot;
/&gt;</pre>
</dl>
<p> If TLS encryption is to be used the location of the Certificate Authority certificate must be set within the LDAP client configuration in order to validate the server certificate. If, in addition, a certified connection is to be used then the client certificate and private key file locations must also be configured within the LDAP client. In OpenLDAP these may be configured in the <code>ldap.conf</code> file or in the per-user configuration. For example it may be sensible to use the system wide configuration for the location of the Certificate Authority certificate and set the location of the client certificate and private key in the per-user configuration. The location of these files and the configuration entry requirements is system dependent so the documentation for your installation will need to be consulted to get further information.</p>
<h2>Example</h2>
<dl>
<dd>
<pre>/- auto.data
/home /etc/auto.home
/mnt yp:mnt.map</pre>
</dl>
<p> This will generate two mountpoints for <i>/home</i> and <i>/mnt</i> and install direct mount triggers for each entry in the direct mount map <i>auto.data</i>. All accesses to <i>/home</i> will lead to the consultation of the map in <i>/etc/auto.home</i> and all accesses to <i>/mnt</i> will consult the NIS map <i>mnt.map</i>. All accesses to paths in the map <i>auto.data</i> will trigger mounts when they are accessed and the Name Service Switch configuration will be used to locate the source of the map <i>auto.data</i>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-automount/">automount</a></code>(8), <code><a href="/docs/linux/man/5-autofs/">autofs</a></code>(5), <code><a href="/docs/linux/man/8-autofs/">autofs</a></code>(8).</p>
<h2>Author</h2>
<p>This manual page was written by Christoph Lameter &lt;chris [at] waterf.org&gt;, for the Dean GNU/Linux system. Edited by &lt;hpa [at] transmeta.com&gt; and Ian Kent &lt;raven [at] themaw.net&gt; .</p>
