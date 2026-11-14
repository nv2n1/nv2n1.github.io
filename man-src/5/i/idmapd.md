---
title: "idmapd(5)"
name: "idmapd"
section: "5"
letter: "i"
url: "/docs/linux/man/5-idmapd/"
description: "idmapd.conf – configuration file for libnfsidmap"
---

<p>idmapd.conf &#8211; configuration file for libnfsidmap</p>
<h2>Synopsis</h2>
<p>Configuration file for libnfsidmap. Used by idmapd and svcgssd to map NFSv4 name to and from ids.</p>
<h2>Description</h2>
<p>The <code>idmapd.conf</code> configuration file consists of several sections, initiated by strings of the form [General] and [Mapping]. Each section may contain lines of the form </p>
<pre> variable = value</pre>
<p>The recognized sections and their recognized variables are as follows:</p>
<h3>[General] section variables</h3>
<dl>
<dt><code>Verbosity</code></p>
<dd>Verbosity level of debugging (Default: 0)</p>
<dt><code>Domain</code></p>
<dd>The local NFSv4 domain name. An NFSv4 domain is a namespace with a unique username&lt;-&gt;UID and groupname&lt;-&gt;GID mapping. (Default: Host&#8217;s fully-qualified DNS domain name)</p>
<dt><code>Local-Realms</code></p>
<dd>A comma-separated list of Kerberos realm names that may be considered equivalent to the local realm name. For example, users juser [at] ORDER.EDU and juser [at] MAIL.ORDER.EDU may be considered to be the same user in the specified <code>Domain.</code> (Default: the host&#8217;s default realm name)<br />
 <code>Note:</code> If a value is specified here, the default local realm must be included as well.</dl>
<h3>[Mapping] section variables</h3>
<dl>
<dt><code>Nobody-User</code></p>
<dd>Local user name to be used when a mapping cannot be completed.</p>
<dt><code>Nobody-Group</code></p>
<dd>Local group name to be used when a mapping cannot be completed.</dl>
<h3>[Translation] section variables</h3>
<dl>
<dt><code>Method</code></p>
<dd>A comma-separated, ordered list of mapping methods (plug-ins) to use when mapping between NFSv4 names and local IDs. Each specified method is tried in order until a mapping is found, or there are no more methods to try. The methods included in the default distribution include &quot;nsswitch&quot;, &quot;umich_ldap&quot;, and &quot;static&quot;. (Default: nsswitch)</p>
<dt><code>GSS-Methods</code></p>
<dd>An optional comma-separated, ordered list of mapping methods (plug-ins) to use when mapping between GSS Authenticated names and local IDs. (Default: the same list as specified for <code>Method)</code></dl>
<h3>[Static] section variables</h3>
<p>The &quot;static&quot; translation method uses a static list of GSS-Authenticated names to local user names. Entries in the list are of the form: </p>
<pre> principal [at] REALM = localusername</pre>
<h3>[UMICH_SCHEMA] section variables</h3>
<p>If the &quot;umich_ldap&quot; translation method is specified, the following variables within the [UMICH_SCHEMA] section are used.</p>
<dl>
<dt><code>LDAP_server</code></p>
<dd>LDAP server name or address (Required if using UMICH_LDAP)</p>
<dt><code>LDAP_base</code></p>
<dd>Absolute LDAP search base. (Required if using UMICH_LDAP)</p>
<dt><code>LDAP_people_base</code></p>
<dd>Absolute LDAP search base for people accounts. (Default: The <code>LDAP_base</code> value)</p>
<dt><code>LDAP_group_base</code></p>
<dd>Absolute LDAP search base for group accounts. (Default: The <code>LDAP_base</code> value)</p>
<dt><code>LDAP_canonicalize_name</code></p>
<dd>Whether or not to perform name canonicalization on the name given as <code>LDAP_server</code> (Default: &quot;true&quot;)</p>
<dt><code>LDAP_use_ssl</code></p>
<dd>Set to &quot;true&quot; to enable SSL communication with the LDAP server. (Default: &quot;false&quot;)</p>
<dt><code>LDAP_ca_cert</code></p>
<dd>Location of a trusted CA certificate used when SSL is enabled (Required if <code>LDAP_use_ssl</code> is true)</p>
<dt><code>NFSv4_person_objectclass</code></p>
<dd>The object class name for people accounts in your local LDAP schema (Default: NFSv4RemotePerson)</p>
<dt><code>NFSv4_name_attr</code></p>
<dd>Your local schema&#8217;s attribute name to be used for NFSv4 user names (Default: NFSv4Name)</p>
<dt><code>NFSv4_uid_attr</code></p>
<dd>Your local schema&#8217;s attribute name to be used for uidNumber (Default: uidNumber)</p>
<dt><code>GSS_principal_attr</code></p>
<dd>Your local schema&#8217;s attribute name for GSSAPI Principal names (Default: GSSAuthName)</p>
<dt><code>NFSv4_acctname_attr</code></p>
<dd>Your local schema&#8217;s attribute name to be used for account names (Default: uid)</p>
<dt><code>NFSv4_group_objectclass</code></p>
<dd>The object class name for group accounts in your local LDAP schema (Default: NFSv4RemoteGroup)</p>
<dt><code>NFSv4_gid_attr</code></p>
<dd>Your local schema&#8217;s attribute name to be used for gidNumber (Default: gidNumber)</p>
<dt><code>NFSv4_group_attr</code></p>
<dd>Your local schema&#8217;s attribute name to be used for NFSv4 group names (Default: NFSv4Name)</p>
<dt><code>LDAP_use_memberof_for_groups</code></p>
<dd>Some LDAP servers do a better job with indexing where searching through all the groups searching for the user in the memberuid list. Others like SunOne directory that search can takes minutes if there are thousands of groups. So setting <code>LDAP_use_memberof_for_groups</code> to true in the configuration file will use the memberof lists of the account and search through only those groups to obtain gids. (Default: false)</p>
<dt><code>NFSv4_member_attr</code></p>
<dd>If <code>LDAP_use_memberof_for_groups</code> is true, this is the attribute to be searched for. (Default: memberUid)</p>
<dt><code>NFSv4_grouplist_filter</code></p>
<dd>An optional search filter for determining group membership. (No Default)</p>
<dt><code>LDAP_timeout_seconds</code></p>
<dd>Number of seconds before timing out an LDAP request (Default: 4)</dl>
<h2>Examples</h2>
<p>An example <i>/etc/idmapd.conf</i> file: </p>
<pre>[General]
Verbosity = 0
Domain = domain.org
Local-Realms = DOMAIN.ORG,MY.DOMAIN.ORG,YOUR.DOMAIN.ORG
[Mapping]
Nobody-User = nfsnobody
Nobody-Group = nfsnobody
[Translation]
Method = umich_ldap,nsswitch
GSS-Methods = umich_ldap,static
[Static]
johndoe [at] OTHER.DOMAIN.ORG = johnny
[UMICH_SCHEMA]
LDAP_server = ldap.domain.org
LDAP_base = dc=org,dc=domain</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-idmapd/">idmapd</a></code>(8) <code><a href="/docs/linux/man/8-svcgssd/">svcgssd</a></code>(8)</p>
<h2>Bugs</h2>
<p>Report bugs to &lt;nfsv4 [at] linux-nfs.org&gt; </p>
