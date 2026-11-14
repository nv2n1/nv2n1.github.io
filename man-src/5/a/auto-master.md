---
title: "auto-master(5)"
name: "auto-master"
section: "5"
letter: "a"
url: "/docs/linux/man/5-auto-master/"
description: "auto.master – Master Map for automounter"
---

<p>auto.master &#8211; Master Map for automounter</p>
<h2>Description</h2>
<p>The <code>auto.master</code> map is consulted to set up automount managed mount points when the <code><a href="/docs/linux/man/8-autofs/">autofs</a></code>(8) script is invoked or the <code><a href="/docs/linux/man/8-automount/">automount</a></code>(8) program is run. Each line describes a mount point and refers to an autofs map describing file systems to be mounted under the mount point. </p>
<p> The default location of the master map is <code>/etc/auto.master</code> but an alternate name may be given on the command line when running the automounter and the default master map may changed by setting the <code>MASTER_MAP_NAME</code> configuration variable in <code>/etc/sysconfig/autofs.</code> If the master map name has no path then the system Name Service Switch configuration will be consulted and each of the sources searched in line with the rules given in the Name Service Switch configuration. </p>
<p> Access to mounts in maps is governed by a key. </p>
<p> For direct maps the mount point is always specified as: </p>
<p> <code>/-</code> </p>
<p> and the key used within the direct map is the full path to the mount point. The direct map may have multiple entries in the master map. </p>
<p> For indirect maps access is by using the path scheme: </p>
<p> <code>/mount-point/key</code> </p>
<p> where <i>mount-point</i> is one of the entries listed in the master map. The <i>key</i> is a single directory component and is matched against entries in the map given in the entry (See <code><a href="/docs/linux/man/5-autofs/">autofs</a></code>(5)). </p>
<p> Additionally, a map may be included from its source as if it were itself present in the master map by including a line of the form: </p>
<p> <code>+</code>[<code>maptype</code>[,<code>format</code>]:]<code>map&nbsp;<wbr></code>[<code>options</code>] </p>
<p> and <code><a href="/docs/linux/man/8-automount/">automount</a></code>(8) will process the map according to the specification described below for map entries. Indirect map entries must be unique in the master map so second and subsequent entries for an indirect mount point are ignored by <code><a href="/docs/linux/man/8-automount/">automount</a></code>(8).</p>
<h2>Format</h2>
<p>Master map entries have three fields separated by an arbitrary number of spaces or tabs. Lines beginning with # are comments. The first field is the mount point described above and the second field is the name of the map to be consulted for the mount point followed by the third field which contains options to be applied to all entries in the map. </p>
<p> The format of a master map entry is:</p>
<dl>
<dt><code>mount-point&nbsp;<wbr></code>[<code>map-type</code>[,<code>format</code>]:]<code>map&nbsp;<wbr></code>[<code>options</code>]</p>
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
<dd>The map is an executable program, which is passed a key on the command line and returns an entry (everything besides the key) on stdout if successful. Optinally, the keyword exec may be used as a synonym for program to avoid confusion with amd formated maps mount type program.</p>
<dt><code>yp</code></p>
<dd>The map is a NIS (YP) database.</p>
<dt><code>nisplus</code></p>
<dd>The map is a NIS+ database.</p>
<dt><code>hesiod</code></p>
<dd>The map is a hesiod database whose <code>filsys</code> entries are used for maps.</p>
<dt><code>ldap </code>or<code> ldaps</code></p>
<dd>The map is stored in an LDAP directory. If <code>ldaps</code> is used the appropriate certificate must be configured in the LDAP client.</p>
<dt><code>multi</code></p>
<dd>This map type allows the specification of multiple maps separated by &quot;&#8211;&quot;. These maps are searched in order to resolve key lookups.</p>
<dt><code>dir</code></p>
<dd>This map type can be used at <code>+</code> master map including notation. The contents of files under given directory are included to the master map. The name of file to be included must be ended with &quot;.autofs&quot;. A file will be ignored if its name is not ended with the suffix. In addition a dot file, a file which name is started with &quot;.&quot; is also ignored.</dl>
</dl>
<dt><code>format</code></p>
<dd>Format of the map data; currently the formats recognized are <code>sun</code>, which is a subset of the Sun automounter map format, <code>hesiod</code>, for hesiod filesys entries and <code>amd</code> for amd formated map entries. If the format is left unspecified, it defaults to <code>sun</code> for all map types except <code>hesiod</code> unless it is a top level <code>amd</code> mount that has a configuration entry for the mount point path, in which case the format used is <code>amd</code>.</p>
<dt><code>map</code></p>
<dd>Name of the map to use. This is an absolute UNIX pathname for maps of types <code>file</code>, <code>dir</code>, or <code>program</code>, and the name of a database in the case for maps of type <code>yp</code>, <code>nisplus</code>, or <code>hesiod</code> or the <code>dn</code> of an LDAP entry for maps of type <code>ldap</code>.</p>
<dt><code>options</code></p>
<dd>Any remaining command line arguments without leading dashes (-) are taken as options (<i>-o</i>) to <code>mount</code>. Arguments with leading dashes are considered options for the maps and are passed to automount (8). </p>
<p> The <code>sun</code> format supports the following options:</p>
<dl>
<dd>
<dl>
<dt><i>-Dvariable=value</i></p>
<dd>Replace <i>variable</i> with <i>value</i> in map substitutions.</p>
<dt><i>-strict</i></p>
<dd>Treat errors when mounting file systems as fatal. This is important when multiple file systems should be mounted (`multimounts&#8217;). If this option is given, no file system is mounted at all if at least one file system can&#8217;t be mounted.</p>
<dt><i>[no]browse</i></p>
<dd>This is an autofs specific option that is a pseudo mount option and so is given without a leading dash. Use of the browse option pre-creates mount point directories for indirect mount maps so the map keys can be seen in a directory listing without being mounted. Use of this option can cause performance problem if the indirect map is large so it should be used with caution. The internal program default is to enable browse mode for indirect mounts but the default installed configuration overrides this by setting BROWSE_MODE to &quot;no&quot; because of the potential performance problem.</p>
<dt><i>nobind</i></p>
<dd>This is an autofs specific option that is a pseudo mount option and so is given without a leading dash. It may be used either in the master map entry (so it effects all the map entries) or with individual map entries to prevent bind mounting of local NFS filesystems. For direct mount maps the option is only effective if specified on the first direct map entry and is applied to all direct mount maps in the master map. It is ignored if given on subsequent direct map entries. It may be used on individual map entries of both types. Bind mounting of NFS file systems can also be prevented for specific map entrys by adding the &quot;port=&quot; mount option to the entries.</p>
<dt><i>symlink</i></p>
<dd>This option makes bind mounting use a symlink instead of an actual bind mount. It is an autofs specific option that is a pseudo mount option and so is given without a leading dash. It may be used with indirect map entries only, either in the master map (so it effects all map entries) or with individual map entries. The option is ignored for direct mounts and non-root offest mount entries.</p>
<dt><i>-r, &#8211;random-multimount-selection</i></p>
<dd>Enables the use of ramdom selection when choosing a host from a list of replicated servers. This option is applied to this mount only, overriding the global setting that may be specified on the command line.</p>
<dt><i>-w, &#8211;use-weight-only</i></p>
<dd>Use only specified weights for server selection where more than one server is specified in the map entry. If no server weights are given then each available server will be tried in the order listed, within proximity.</p>
<dt><i>-t, &#8211;timeout &lt;seconds&gt;</i></p>
<dd>Set the expire timeout for map entries. This option can be used to override the global default given either on the command line or in the configuration.</p>
<dt><i>-n, &#8211;negative-timeout &lt;seconds&gt;</i></p>
<dd>Set the timeout for caching failed key lookups. This option can be used to override the global default given either on the command line or in the configuration.</dl>
</dl>
</dl>
<h2>BUILTIN MAP -hosts</h2>
<p>If &quot;-hosts&quot; is given as the map then accessing a key under the mount point which corresponds to a hostname will allow access to the exports of that host. The hosts map cannot be dynamically updated and requires a HUP signal to be sent to the daemon for it to check hosts for an update. Due to possible hierarchic dependencies within a mount tree, it might not be completely updated during the HUP signal processing. </p>
<p> For example, with an entry in the master map of <code>/net -hosts</code> accessing /net/myserver will mount exports from myserver on directories below /net/myserver. </p>
<p> NOTE: mounts done from a hosts map will be mounted with the &quot;nosuid,nodev,intr&quot; options unless overridden by explicily specifying the &quot;suid&quot;, &quot;dev&quot; or &quot;nointr&quot; options in the master map entry.</p>
<h2>Ldap Maps</h2>
<p>If the map type <code>ldap</code> is specified the mapname is of the form <code>[//servername/]dn</code>, where the optional <code>servername</code> is the name of the LDAP server to query, and <code>dn</code> is the Distinguished Name of a subtree to search for map entries. The old style <code>ldap:servername:mapname</code> is also understood. Alternatively, the type can be obtained from the Name Service Switch configuration, in which case the map name alone must be given. </p>
<p> If no schema is set in the autofs configuration then autofs will check each of the commonly used schema for a valid entry and if one is found it will used for subsequent lookups. </p>
<p> There are three common schemas in use:</p>
<dl>
<dt><i>nisMap</i></p>
<dd>Entries in the <code>nisMap</code> schema are <code>nisObject</code> objects in the specified subtree, where the <code>cn</code> attribute is the key (the wildcard key is &quot;/&quot;), and the <code>nisMapEntry</code> attribute contains the information used by the automounter.</p>
<dt><i>automountMap</i></p>
<dd>The <code>automountMap</code> schema has two variations that differ in the attribute used for the map key. Entries in the automountMap schema are <code>automount</code> objects in the specified subtree, where the <code>cn</code> or <code>automountKey</code> attribute (depending on local usage) is the key (the wildcard key is &quot;/&quot;), and the <code>automountInformation</code> attribute contains the information used by the automounter. Note that the <code>cn</code> attribute is case insensitive.</dl>
<p> The object classes and attributes used for accessing automount maps in LDAP can be changed by setting entries in the autofs configuration located in <code>/etc/sysconfig/autofs.conf</code>.</p>
<dl>
<dt><code>NOTE:</code></p>
<dd>If a schema is given in the configuration then all the schema configuration values must be set, any partial schema specification will be ignored.</p>
<dt>For <code>amd</code> format maps a different schema is used:</p>
<dd>
<dt><i>amdMap</i></p>
<dd>The <code>amdmap</code> schema contains attributes <code>amdmapName</code>, <code>amdmapKey</code> and <code>amdmapValue</code> where <code>amdmapName</code> contains the name of the containing map, <code>amdmapKey</code> contains the map key and <code>amdmapValue</code> contains the map entry.</dl>
<h2>Ldap Authentication, Encrypted And Certified Connections</h2>
<p>LDAP authenticated binds, TLS encrypted connections and certification may be used by setting appropriate values in the autofs authentication configuration file and configuring the LDAP client with appropriate settings. The default location of this file is <code>/etc/autofs_ldap_auth.conf</code>. </p>
<p> If this file exists it will be used to establish whether TLS or authentication should be used. </p>
<p> An example of this file is: </p>
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
<p> If TLS encryption is to be used the location of the Certificate Authority certificate must be set within the LDAP client configuration in order to validate the server certificate. If, in addition, a certified connection is to be used then the client certificate and private key file locations must also be configured within the LDAP client. </p>
<p> In OpenLDAP these may be configured in the <code>ldap.conf</code> file or in the per-user configuration. For example it may be sensible to use the system wide configuration for the location of the Certificate Authority certificate and set the location of the client certificate and private key in the per-user configuration. The location of these files and the configuration entry requirements is system dependent so the documentation for your installation will need to be consulted to get further information. </p>
<p> See <code>autofs_ldap_auth.conf (5)</code> for more information.</p>
<h2>Example</h2>
<dl>
<dd>
<pre>/- auto.data
/home /etc/auto.home
/mnt yp:mnt.map</pre>
</dl>
<p> This will generate two mountpoints for <i>/home</i> and <i>/mnt</i> and install direct mount triggers for each entry in the direct mount map <i>auto.data</i>. All accesses to <i>/home</i> will lead to the consultation of the map in <i>/etc/auto.home</i> and all accesses to <i>/mnt</i> will consult the NIS map <i>mnt.map</i>. All accesses to paths in the map <i>auto.data</i> will trigger mounts when they are accessed and the Name Service Switch configuration will be used to locate the source of the map <i>auto.data</i>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-automount/">automount</a></code>(8), <code><a href="/docs/linux/man/5-autofs/">autofs</a></code>(5), <code><a href="/docs/linux/man/8-autofs/">autofs</a></code>(8), <code><a href="/docs/linux/man/5-autofs-conf/">autofs.conf</a></code>(5), <code><a href="/docs/linux/man/5-autofs_ldap_auth-conf/">autofs_ldap_auth.conf</a></code>(5)</p>
<h2>Author</h2>
<p>This manual page was written by Christoph Lameter &lt;chris [at] waterf.org&gt;, for the Dean GNU/Linux system. Edited by &lt;hpa [at] transmeta.com&gt; and Ian Kent &lt;raven [at] themaw.net&gt; .</p>
