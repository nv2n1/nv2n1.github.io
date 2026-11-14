---
title: "smb-conf(5)"
name: "smb-conf"
section: "5"
letter: "s"
url: "/docs/linux/man/5-smb-conf/"
description: "smb.conf – The configuration file for the Samba suite"
---

<p>smb.conf &#8211; The configuration file for the Samba suite</p>
<h2>Synopsis</h2>
<p>The smb.conf file is a configuration file for the Samba suite. smb.conf contains runtime configuration information for the Samba programs. The complete description of the file format and possible parameters held within are here for reference purposes.</p>
<h2>File Format</h2>
<p>The file consists of sections and parameters. A section begins with the name of the section in square brackets and continues until the next section begins. Sections contain parameters of the form: </p>
<dl>
<dd>
<pre><i>name</i> = <i>value </i></pre>
</dl>
<p> The file is line-based &#8211; that is, each newline-terminated line represents either a comment, a section name or a parameter. </p>
<p> Section and parameter names are not case sensitive. </p>
<p> Only the first equals sign in a parameter is significant. Whitespace before or after the first equals sign is discarded. Leading, trailing and internal whitespace in section and parameter names is irrelevant. Leading and trailing whitespace in a parameter value is discarded. Internal whitespace within a parameter value is retained verbatim. </p>
<p> Any line beginning with a semicolon (&#8220;;&#8221;) or a hash (&#8220;#&#8221;) character is ignored, as are lines containing only whitespace. </p>
<p> Any line ending in a &#8220;\&#8221; is continued on the next line in the customary UNIX fashion. </p>
<p> The values following the equals sign in parameters are all either a string (no quotes needed) or a boolean, which may be given as yes/no, 1/0 or true/false. Case is not significant in boolean values, but is preserved in string values. Some items such as create masks are numeric.</p>
<h2>Section Descriptions</h2>
<p>Each section in the configuration file (except for the [global] section) describes a shared resource (known as a &#8220;share&#8221;). The section name is the name of the shared resource and the parameters within the section define the shares attributes. </p>
<p> There are three special sections, [global], [homes] and [printers], which are described under <i>special sections</i>. The following notes apply to ordinary section descriptions. </p>
<p> A share consists of a directory to which access is being given plus a description of the access rights which are granted to the user of the service. Some housekeeping options are also specifiable. </p>
<p> Sections are either file share services (used by the client as an extension of their native file systems) or printable services (used by the client to access print services on the host running the server). </p>
<p> Sections may be designated <i>guest</i> services, in which case no password is required to access them. A specified UNIX <i>guest account</i> is used to define access privileges in this case. </p>
<p> Sections other than guest services will require a password to access them. The client provides the username. As older clients only provide passwords and not usernames, you may specify a list of usernames to check against the password using the user = option in the share definition. For modern clients such as Windows 95/98/ME/NT/2000, this should not be necessary. </p>
<p> The access rights granted by the server are masked by the access rights granted to the specified or guest UNIX user by the host system. The server does not grant more access than the host system grants. </p>
<p> The following sample section defines a file space share. The user has write access to the path /home/bar. The share is accessed via the share name foo: </p>
<dl>
<dd>
<pre> <i>[foo]</i>
 m[blue]<code>path = /home/bar</code>m[]
 m[blue]<code>read only = no</code>m[]</pre>
</dl>
<p> The following sample section defines a printable share. The share is read-only, but printable. That is, the only write access permitted is via calls to open, write to and close a spool file. The <i>guest ok</i> parameter means access will be permitted as the default guest user (specified elsewhere): </p>
<dl>
<dd>
<pre> <i>[aprinter]</i>
 m[blue]<code>path = /usr/spool/public</code>m[]
 m[blue]<code>read only = yes</code>m[]
 m[blue]<code>printable = yes</code>m[]
 m[blue]<code>guest ok = yes</code>m[]</pre>
</dl>
<h2>Special Sections</h2>
<h3>The [global] section</h3>
<p>Parameters in this section apply to the server as a whole, or are defaults for sections that do not specifically define certain items. See the notes under PARAMETERS for more information.</p>
<h3>The [homes] section</h3>
<p>If a section called [homes] is included in the configuration file, services connecting clients to their home directories can be created on the fly by the server. </p>
<p> When the connection request is made, the existing sections are scanned. If a match is found, it is used. If no match is found, the requested section name is treated as a username and looked up in the local password file. If the name exists and the correct password has been given, a share is created by cloning the [homes] section. </p>
<p> Some modifications are then made to the newly created share:</p>
<dl>
<dd>
<dl>
<dd>&bull; The share name is changed from homes to the located username.</dl>
<dl>
<dd>&bull; If no path was given, the path is set to the user&#8217;s home directory.</dl>
</dl>
<p> If you decide to use a <i>path =</i> line in your [homes] section, it may be useful to use the %S macro. For example: </p>
<dl>
<dd>
<pre><code>path = /data/pchome/%S</code></pre>
</dl>
<p> is useful if you have different home directories for your PCs than for UNIX access. </p>
<p> This is a fast and simple way to give a large number of clients access to their home directories with a minimum of fuss. </p>
<p> A similar process occurs if the requested section name is &#8220;homes&#8221;, except that the share name is not changed to that of the requesting user. This method of using the [homes] section works well if different users share a client PC. </p>
<p> The [homes] section can specify all the parameters a normal service section can specify, though some make more sense than others. The following is a typical and suitable [homes] section: </p>
<dl>
<dd>
<pre><i>[homes]</i>
m[blue]<code>read only = no</code>m[]</pre>
</dl>
<p> An important point is that if guest access is specified in the [homes] section, all home directories will be visible to all clients <i>without a password</i>. In the very unlikely event that this is actually desirable, it is wise to also specify <i>read only access</i>. </p>
<p> The <i>browseable</i> flag for auto home directories will be inherited from the global browseable flag, not the [homes] browseable flag. This is useful as it means setting <i>browseable = no</i> in the [homes] section will hide the [homes] share but make any auto home directories visible.</p>
<h3>The [printers] section</h3>
<p>This section works like [homes], but for printers. </p>
<p> If a [printers] section occurs in the configuration file, users are able to connect to any printer specified in the local host&#8217;s printcap file. </p>
<p> When a connection request is made, the existing sections are scanned. If a match is found, it is used. If no match is found, but a [homes] section exists, it is used as described above. Otherwise, the requested section name is treated as a printer name and the appropriate printcap file is scanned to see if the requested section name is a valid printer share name. If a match is found, a new printer share is created by cloning the [printers] section. </p>
<p> A few modifications are then made to the newly created share:</p>
<dl>
<dd>
<dl>
<dd>&bull; The share name is set to the located printer name</dl>
<dl>
<dd>&bull; If no printer name was given, the printer name is set to the located printer name</dl>
<dl>
<dd>&bull; If the share does not permit guest access and no username was given, the username is set to the located printer name.</dl>
</dl>
<p> The [printers] service MUST be printable &#8211; if you specify otherwise, the server will refuse to load the configuration file. </p>
<p> Typically the path specified is that of a world-writeable spool directory with the sticky bit set on it. A typical [printers] entry looks like this: </p>
<dl>
<dd>
<pre><i>[printers]</i>
m[blue]<code>path = /usr/spool/public</code>m[]
m[blue]<code>guest ok = yes</code>m[]
m[blue]<code>printable = yes</code>m[]</pre>
</dl>
<p> All aliases given for a printer in the printcap file are legitimate printer names as far as the server is concerned. If your printing subsystem doesn&#8217;t work like that, you will have to set up a pseudo-printcap. This is a file consisting of one or more lines like this: </p>
<dl>
<dd>
<pre>alias|alias|alias|alias... </pre>
</dl>
<p> Each alias should be an acceptable printer name for your printing subsystem. In the [global] section, specify the new file as your printcap. The server will only recognize names found in your pseudo-printcap, which of course can contain whatever aliases you like. The same technique could be used simply to limit access to a subset of your local printers. </p>
<p> An alias, by the way, is defined as any component of the first entry of a printcap record. Records are separated by newlines, components (if there are more than one) are separated by vertical bar symbols (|). </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> On SYSV systems which use lpstat to determine what printers are defined on the system you may be able to use printcap name = lpstat to automatically obtain a list of printers. See the printcap name option for more details. </p>
</dl>
<h2>Usershares</h2>
<p>Starting with Samba version 3.0.23 the capability for non-root users to add, modify, and delete their own share definitions has been added. This capability is called <i>usershares</i> and is controlled by a set of parameters in the [global] section of the smb.conf. The relevant parameters are : </p>
<p> usershare allow guests</p>
<dl>
<dd>Controls if usershares can permit guest access.</dl>
<p> usershare max shares</p>
<dl>
<dd>Maximum number of user defined shares allowed.</dl>
<p> usershare owner only</p>
<dl>
<dd>If set only directories owned by the sharing user can be shared.</dl>
<p> usershare path</p>
<dl>
<dd>Points to the directory containing the user defined share definitions. The filesystem permissions on this directory control who can create user defined shares.</dl>
<p> usershare prefix allow list</p>
<dl>
<dd>Comma-separated list of absolute pathnames restricting what directories can be shared. Only directories below the pathnames in this list are permitted.</dl>
<p> usershare prefix deny list</p>
<dl>
<dd>Comma-separated list of absolute pathnames restricting what directories can be shared. Directories below the pathnames in this list are prohibited.</dl>
<p> usershare template share</p>
<dl>
<dd>Names a pre-existing share used as a template for creating new usershares. All other share parameters not specified in the user defined share definition are copied from this named share.</dl>
<p> To allow members of the UNIX group foo to create user defined shares, create the directory to contain the share definitions as follows: </p>
<p> Become root: </p>
<dl>
<dd>
<pre>mkdir /usr/local/samba/lib/usershares
chgrp foo /usr/local/samba/lib/usershares
chmod 1770 /usr/local/samba/lib/usershares</pre>
</dl>
<p> Then add the parameters </p>
<dl>
<dd>
<pre> m[blue]<code>usershare path = /usr/local/samba/lib/usershares</code>m[]
 m[blue]<code>usershare max shares = 10</code>m[] # (or the desired number of shares)</pre>
</dl>
<p> to the global section of your smb.conf. Members of the group foo may then manipulate the user defined shares using the following commands. </p>
<p> net usershare add sharename path [comment] [acl] [guest_ok=[y|n]]</p>
<dl>
<dd>To create or modify (overwrite) a user defined share.</dl>
<p> net usershare delete sharename</p>
<dl>
<dd>To delete a user defined share.</dl>
<p> net usershare list wildcard-sharename</p>
<dl>
<dd>To list user defined shares.</dl>
<p> net usershare info wildcard-sharename</p>
<dl>
<dd>To print information about user defined shares.</dl>
<h2>Parameters</h2>
<p>Parameters define the specific attributes of sections. </p>
<p> Some parameters are specific to the [global] section (e.g., <i>security</i>). Some parameters are usable in all sections (e.g., <i>create mask</i>). All others are permissible only in normal sections. For the purposes of the following descriptions the [homes] and [printers] sections will be considered normal. The letter <i>G</i> in parentheses indicates that a parameter is specific to the [global] section. The letter <i>S</i> indicates that a parameter can be specified in a service specific section. All <i>S</i> parameters can also be specified in the [global] section &#8211; in which case they will define the default behavior for all services. </p>
<p> Parameters are arranged here in alphabetical order &#8211; this may not create best bedfellows, but at least you can find them! Where there are synonyms, the preferred synonym is described, others refer to the preferred synonym.</p>
<h2>Variable Substitutions</h2>
<p>Many of the strings that are settable in the config file can take substitutions. For example the option &#8220;path = /tmp/%u&#8221; is interpreted as &#8220;path = /tmp/john&#8221; if the user connected with the username john. </p>
<p> These substitutions are mostly noted in the descriptions below, but there are some general substitutions which apply whenever they might be relevant. These are: </p>
<p> %U</p>
<dl>
<dd>session username (the username that the client wanted, not necessarily the same as the one they got).</dl>
<p> %G</p>
<dl>
<dd>primary group name of %U.</dl>
<p> %h</p>
<dl>
<dd>the Internet hostname that Samba is running on.</dl>
<p> %m</p>
<dl>
<dd>the NetBIOS name of the client machine (very useful). </p>
<p> This parameter is not available when Samba listens on port 445, as clients no longer send this information. If you use this macro in an include statement on a domain that has a Samba domain controller be sure to set in the [global] section <i>smb ports = 139</i>. This will cause Samba to not listen on port 445 and will permit include functionality to function as it did with Samba 2.x.</dl>
<p> %L</p>
<dl>
<dd>the NetBIOS name of the server. This allows you to change your config based on what the client calls you. Your server can have a &#8220;dual personality&#8221;.</dl>
<p> %M</p>
<dl>
<dd>the Internet name of the client machine.</dl>
<p> %R</p>
<dl>
<dd>the selected protocol level after protocol negotiation. It can be one of CORE, COREPLUS, LANMAN1, LANMAN2, NT1, SMB2_02, SMB2_10, SMB2_22, SMB2_24, SMB3_00, SMB3_02, SMB3_10, SMB3_11 or SMB2_FF.</dl>
<p> %d</p>
<dl>
<dd>the process id of the current server process.</dl>
<p> %a</p>
<dl>
<dd>The architecture of the remote machine. It currently recognizes Samba (<code>Samba</code>), the Linux CIFS file system (<code>CIFSFS</code>), OS/2, (<code>OS2</code>), Mac OS X (<code>OSX</code>), Windows for Workgroups (<code>WfWg</code>), Windows 9x/ME (<code>Win95</code>), Windows NT (<code>WinNT</code>), Windows 2000 (<code>Win2K</code>), Windows XP (<code>WinXP</code>), Windows XP 64-bit(<code>WinXP64</code>), Windows 2003 including 2003R2 (<code>Win2K3</code>), and Windows Vista (<code>Vista</code>). Anything else will be known as <code>UNKNOWN</code>.</dl>
<p> %I</p>
<dl>
<dd>the IP address of the client machine. </p>
<p> Before 4.0.0 it could contain IPv4 mapped IPv6 addresses, now it only contains IPv4 or IPv6 addresses.</dl>
<p> %J</p>
<dl>
<dd>the IP address of the client machine, colons/dots replaced by underscores.</dl>
<p> %i</p>
<dl>
<dd>the local IP address to which a client connected. </p>
<p> Before 4.0.0 it could contain IPv4 mapped IPv6 addresses, now it only contains IPv4 or IPv6 addresses.</dl>
<p> %j</p>
<dl>
<dd>the local IP address to which a client connected, colons/dots replaced by underscores.</dl>
<p> %T</p>
<dl>
<dd>the current date and time.</dl>
<p> %t</p>
<dl>
<dd>the current date and time in a minimal format without colons (YYYYYmmdd_HHMMSS).</dl>
<p> %D</p>
<dl>
<dd>name of the domain or workgroup of the current user.</dl>
<p> %w</p>
<dl>
<dd>the winbind separator.</dl>
<p> %$(<i>envvar</i>)</p>
<dl>
<dd>the value of the environment variable <i>envar</i>.</dl>
<p> The following substitutes apply only to some configuration options (only those that are used when a connection has been established): </p>
<p> %S</p>
<dl>
<dd>the name of the current service, if any.</dl>
<p> %P</p>
<dl>
<dd>the root directory of the current service, if any.</dl>
<p> %u</p>
<dl>
<dd>username of the current service, if any.</dl>
<p> %g</p>
<dl>
<dd>primary group name of %u.</dl>
<p> %H</p>
<dl>
<dd>the home directory of the user given by %u.</dl>
<p> %N</p>
<dl>
<dd>the name of your NIS home directory server. This is obtained from your NIS auto.map entry. If you have not compiled Samba with the <i>&#8211;with-automount</i> option, this value will be the same as %L.</dl>
<p> %p</p>
<dl>
<dd>the path of the service&#8217;s home directory, obtained from your NIS auto.map entry. The NIS auto.map entry is split up as %N:%p.</dl>
<p> There are some quite creative things that can be done with these substitutions and other smb.conf options.</p>
<h2>Name Mangling</h2>
<p>Samba supports name mangling so that DOS and Windows clients can use files that don&#8217;t conform to the 8.3 format. It can also be set to adjust the case of 8.3 format filenames. </p>
<p> There are several options that control the way mangling is performed, and they are grouped here rather than listed separately. For the defaults look at the output of the testparm program. </p>
<p> These options can be set separately for each service. </p>
<p> The options are: </p>
<p> case sensitive = yes/no/auto</p>
<dl>
<dd>controls whether filenames are case sensitive. If they aren&#8217;t, Samba must do a filename search and match on passed names. The default setting of auto allows clients that support case sensitive filenames (Linux CIFSVFS and smbclient 3.0.5 and above currently) to tell the Samba server on a per-packet basis that they wish to access the file system in a case-sensitive manner (to support UNIX case sensitive semantics). No Windows or DOS system supports case-sensitive filename so setting this option to auto is that same as setting it to no for them. Default <i>auto</i>.</dl>
<p> default case = upper/lower</p>
<dl>
<dd>controls what the default case is for new filenames (ie. files that don&#8217;t currently exist in the filesystem). Default <i>lower</i>. IMPORTANT NOTE: As part of the optimizations for directories containing large numbers of files, the following special case applies. If the options m[blue]<code>case sensitive = yes</code>m[], m[blue]<code>preserve case = No</code>m[], and m[blue]<code>short preserve case = No</code>m[] are set, then the case of <i>all</i> incoming client filenames, not just new filenames, will be modified. See additional notes below.</dl>
<p> preserve case = yes/no</p>
<dl>
<dd>controls whether new files (ie. files that don&#8217;t currently exist in the filesystem) are created with the case that the client passes, or if they are forced to be the default case. Default <i>yes</i>.</dl>
<p> short preserve case = yes/no</p>
<dl>
<dd>controls if new files (ie. files that don&#8217;t currently exist in the filesystem) which conform to 8.3 syntax, that is all in upper case and of suitable length, are created upper case, or if they are forced to be the default case. This option can be used with preserve case = yes to permit long filenames to retain their case, while short names are lowercased. Default <i>yes</i>.</dl>
<p> By default, Samba 3.0 has the same semantics as a Windows NT server, in that it is case insensitive but case preserving. As a special case for directories with large numbers of files, if the case options are set as follows, &quot;case sensitive = yes&quot;, &quot;case preserve = no&quot;, &quot;short preserve case = no&quot; then the &quot;default case&quot; option will be applied and will modify all filenames sent from the client when accessing this share.</p>
<h2>Registry-Based Configuration</h2>
<p>Starting with Samba version 3.2.0, the capability to store Samba configuration in the registry is available. The configuration is stored in the registry key <i>HKLM\Software\Samba\smbconf</i>. There are two levels of registry configuration:</p>
<dl>
<dd>
<dl>
<dd>1. Share definitions stored in registry are used. This is triggered by setting the global parameter <i>registry shares</i> to &#8220;yes&#8221; in <i>smb.conf</i>. </p>
<p> The registry shares are loaded not at startup but on demand at runtime by <i>smbd</i>. Shares defined in <i>smb.conf</i> take priority over shares of the same name defined in registry.</dl>
<dl>
<dd>2. Global <i>smb.conf</i> options stored in registry are used. This can be activated in two different ways: </p>
<p> Firstly, a registry only configuration is triggered by setting m[blue]<code>config backend = registry</code>m[] in the [global] section of <i>smb.conf</i>. This resets everything that has been read from config files to this point and reads the content of the global configuration section from the registry. This is the recommended method of using registry based configuration. </p>
<p> Secondly, a mixed configuration can be activated by a special new meaning of the parameter m[blue]<code>include = registry</code>m[] in the [global] section of <i>smb.conf</i>. This reads the global options from registry with the same priorities as for an include of a text file. This may be especially useful in cases where an initial configuration is needed to access the registry. </p>
<p> Activation of global registry options automatically activates registry shares. So in the registry only case, shares are loaded on demand only.</dl>
</dl>
<p> Note: To make registry-based configurations foolproof at least to a certain extent, the use of <i>lock directory</i> and <i>config backend</i> inside the registry configuration has been disabled: Especially by changing the <i>lock directory</i> inside the registry configuration, one would create a broken setup where the daemons do not see the configuration they loaded once it is active. </p>
<p> The registry configuration can be accessed with tools like <i>regedit</i> or <i>net (rpc) registry</i> in the key <i>HKLM\Software\Samba\smbconf</i>. More conveniently, the <i>conf</i> subcommand of the <code><a href="/docs/linux/man/8-net/">net</a></code>(8) utility offers a dedicated interface to read and write the registry based configuration locally, i.e. directly accessing the database file, circumventing the server.</p>
<h2>Identity Mapping Considerations</h2>
<p>In the SMB protocol, users, groups, and machines are represented by their security identifiers (SIDs). On POSIX system Samba processes need to run under corresponding POSIX user identities and with supplemental POSIX groups to allow access to the files owned by those users and groups. The process of mapping SIDs to POSIX users and groups is called <i>IDENTITY MAPPING</i> or, in short, <i>ID MAPPING</i>. </p>
<p> Samba supports multiple ways to map SIDs to POSIX users and groups. The configuration is driven by the m[blue]<code>idmap config DOMAIN : OPTION</code>m[] option which allows one to specify identity mapping (idmap) options for each domain separately. </p>
<p> Identity mapping modules implement different strategies for mapping of SIDs to POSIX user and group identities. They are applicable to different use cases and scenarios. It is advised to read the documentation of the individual identity mapping modules before choosing a specific scenario to use. Each identity management module is documented in a separate manual page. The standard idmap backends are tdb (<code><a href="/docs/linux/man/8-idmap_tdb/">idmap_tdb</a></code>(8)), tdb2 (<code><a href="/docs/linux/man/8-idmap_tdb2/">idmap_tdb2</a></code>(8)), ldap (<code><a href="/docs/linux/man/8-idmap_ldap/">idmap_ldap</a></code>(8)), rid (<code><a href="/docs/linux/man/8-idmap_rid/">idmap_rid</a></code>(8)), hash (<code><a href="/docs/linux/man/8-idmap_hash/">idmap_hash</a></code>(8)), autorid (<code><a href="/docs/linux/man/8-idmap_autorid/">idmap_autorid</a></code>(8)), ad (<code><a href="/docs/linux/man/8-idmap_ad/">idmap_ad</a></code>(8)), nss (<code><a href="/docs/linux/man/8-idmap_nss/">idmap_nss</a></code>(8)), and rfc2307 (<code><a href="/docs/linux/man/8-idmap_rfc2307/">idmap_rfc2307</a></code>(8)). </p>
<p> Overall, ID mapping configuration should be decided carefully. Changes to the already deployed ID mapping configuration may create the risk of losing access to the data or disclosing the data to the wrong parties. </p>
<p> This example shows how to configure two domains with <code><a href="/docs/linux/man/8-idmap_rid/">idmap_rid</a></code>(8), the principal domain and a trusted domain, leaving the default id mapping scheme at tdb. </p>
<dl>
<dd>
<pre> [global]
 security = domain
 workgroup = MAIN
 idmap config * : backend = tdb
 idmap config * : range = 1000000-1999999
 idmap config MAIN : backend = rid
 idmap config MAIN : range = 5000000-5999999
 idmap config TRUSTED : backend = rid
 idmap config TRUSTED : range = 6000000-6999999</pre>
</dl>
<h2>Explanation Of Each Parameter</h2>
<p>abort shutdown script (G) </p>
<dl>
<dd>This a full path name to a script called by <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) that should stop a shutdown procedure issued by the m[blue]<code>shutdown script</code>m[]. </p>
<p> If the connected user possesses the <code>SeRemoteShutdownPrivilege</code>, right, this command will be run as root. </p>
<p> Default: <i>abort shutdown script</i><i> = </i><i>&quot;&quot;</i><i> </i> </p>
<p> Example: <i>abort shutdown script</i><i> = </i><i>/sbin/shutdown -c</i><i> </i></dl>
<p> access based share enum (S) </p>
<dl>
<dd>If this parameter is <code>yes</code> for a service, then the share hosted by the service will only be visible to users who have read or write access to the share during share enumeration (for example net view \sambaserver). The share ACLs which allow or deny the access to the share can be modified using for example the sharesec command or using the appropriate Windows tools. This has parallels to access based enumeration, the main difference being that only share permissions are evaluated, and security descriptors on files contained on the share are not used in computing enumeration access rights. </p>
<p> Default: <i>access based share enum</i><i> = </i><i>no</i><i> </i></dl>
<p> acl allow execute always (S) </p>
<dl>
<dd>This boolean parameter controls the behaviour of <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) when receiving a protocol request of &quot;open for execution&quot; from a Windows client. With Samba 3.6 and older, the execution right in the ACL was not checked, so a client could execute a file even if it did not have execute rights on the file. In Samba 4.0, this has been fixed, so that by default, i.e. when this parameter is set to &quot;False&quot;, &quot;open for execution&quot; is now denied when execution permissions are not present. </p>
<p> If this parameter is set to &quot;True&quot;, Samba does not check execute permissions on &quot;open for execution&quot;, thus re-establishing the behaviour of Samba 3.6. This can be useful to smoothen upgrades from older Samba versions to 4.0 and newer. This setting is not meant to be used as a permanent setting, but as a temporary relief: It is recommended to fix the permissions in the ACLs and reset this parameter to the default after a certain transition period. </p>
<p> Default: <i>acl allow execute always</i><i> = </i><i>no</i><i> </i></dl>
<p> acl check permissions (S) </p>
<dl>
<dd>Please note this parameter is now deprecated in Samba 3.6.2 and will be removed in a future version of Samba. </p>
<p> This boolean parameter controls what <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) does on receiving a protocol request of &quot;open for delete&quot; from a Windows client. If a Windows client doesn&#8217;t have permissions to delete a file then they expect this to be denied at open time. POSIX systems normally only detect restrictions on delete by actually attempting to delete the file or directory. As Windows clients can (and do) &quot;back out&quot; a delete request by unsetting the &quot;delete on close&quot; bit Samba cannot delete the file immediately on &quot;open for delete&quot; request as we cannot restore such a deleted file. With this parameter set to true (the default) then smbd checks the file system permissions directly on &quot;open for delete&quot; and denies the request without actually deleting the file if the file system permissions would seem to deny it. This is not perfect, as it&#8217;s possible a user could have deleted a file without Samba being able to check the permissions correctly, but it is close enough to Windows semantics for mostly correct behaviour. Samba will correctly check POSIX ACL semantics in this case. </p>
<p> If this parameter is set to &quot;false&quot; Samba doesn&#8217;t check permissions on &quot;open for delete&quot; and allows the open. If the user doesn&#8217;t have permission to delete the file this will only be discovered at close time, which is too late for the Windows user tools to display an error message to the user. The symptom of this is files that appear to have been deleted &quot;magically&quot; re-appearing on a Windows explorer refresh. This is an extremely advanced protocol option which should not need to be changed. This parameter was introduced in its final form in 3.0.21, an earlier version with slightly different semantics was introduced in 3.0.20. That older version is not documented here. </p>
<p> Default: <i>acl check permissions</i><i> = </i><i>yes</i><i> </i></dl>
<p> acl group control (S) </p>
<dl>
<dd>In a POSIX filesystem, only the owner of a file or directory and the superuser can modify the permissions and ACLs on a file. If this parameter is set, then Samba overrides this restriction, and also allows the <i>primary group owner</i> of a file or directory to modify the permissions and ACLs on that file. </p>
<p> On a Windows server, groups may be the owner of a file or directory &#8211; thus allowing anyone in that group to modify the permissions on it. This allows the delegation of security controls on a point in the filesystem to the group owner of a directory and anything below it also owned by that group. This means there are multiple people with permissions to modify ACLs on a file or directory, easing manageability. </p>
<p> This parameter allows Samba to also permit delegation of the control over a point in the exported directory hierarchy in much the same way as Windows. This allows all members of a UNIX group to control the permissions on a file or directory they have group ownership on. </p>
<p> This parameter is best used with the m[blue]<code>inherit owner</code>m[] option and also on a share containing directories with the UNIX <i>setgid bit</i> set on them, which causes new files and directories created within it to inherit the group ownership from the containing directory. </p>
<p> This parameter was deprecated in Samba 3.0.23, but re-activated in Samba 3.0.31 and above, as it now only controls permission changes if the user is in the owning primary group. It is now no longer equivalent to the <i>dos filemode</i> option. </p>
<p> Default: <i>acl group control</i><i> = </i><i>no</i><i> </i></dl>
<p> acl map full control (S) </p>
<dl>
<dd>This boolean parameter controls whether <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) maps a POSIX ACE entry of &quot;rwx&quot; (read/write/execute), the maximum allowed POSIX permission set, into a Windows ACL of &quot;FULL CONTROL&quot;. If this parameter is set to true any POSIX ACE entry of &quot;rwx&quot; will be returned in a Windows ACL as &quot;FULL CONTROL&quot;, is this parameter is set to false any POSIX ACE entry of &quot;rwx&quot; will be returned as the specific Windows ACL bits representing read, write and execute. </p>
<p> Default: <i>acl map full control</i><i> = </i><i>yes</i><i> </i></dl>
<p> add group script (G) </p>
<dl>
<dd>This is the full pathname to a script that will be run <i>AS ROOT</i> by <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) when a new group is requested. It will expand any <i>%g</i> to the group name passed. This script is only useful for installations using the Windows NT domain administration tools. The script is free to create a group with an arbitrary name to circumvent unix group name restrictions. In that case the script must print the numeric gid of the created group on stdout. </p>
<p> Default: <i>add group script</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>add group script</i><i> = </i><i>/usr/sbin/groupadd %g</i><i> </i></dl>
<p> additional dns hostnames (G) </p>
<dl>
<dd>A list of additional DNS names by which this host can be identified </p>
<p> Default: <i>additional dns hostnames</i><i> = </i><i> # empty string (no additional dns names)</i><i> </i> </p>
<p> Example: <i>additional dns hostnames</i><i> = </i><i> host2.example.com host3.other.com </i><i> </i></dl>
<p> add machine script (G) </p>
<dl>
<dd>This is the full pathname to a script that will be run by <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) when a machine is added to Samba&#8217;s domain and a Unix account matching the machine&#8217;s name appended with a &quot;$&quot; does not already exist. </p>
<p> This option is very similar to the m[blue]<code>add user script</code>m[], and likewise uses the %u substitution for the account name. Do not use the %m substitution. </p>
<p> Default: <i>add machine script</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>add machine script</i><i> = </i><i>/usr/sbin/adduser -n -g machines -c Machine -d /var/lib/nobody -s /bin/false %u</i><i> </i></dl>
<p> addport command (G) </p>
<dl>
<dd>Samba 3.0.23 introduced support for adding printer ports remotely using the Windows &quot;Add Standard TCP/IP Port Wizard&quot;. This option defines an external program to be executed when smbd receives a request to add a new Port to the system. The script is passed two parameters:</p>
<dl>
<dd>
<dl>
<dd>&bull; <i>port name</i></dl>
<dl>
<dd>&bull; <i>device URI</i></dl>
</dl>
<p> The deviceURI is in the format of socket://&lt;hostname&gt;[:&lt;portnumber&gt;] or lpd://&lt;hostname&gt;/&lt;queuename&gt;. </p>
<p> Default: <i>addport command</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>addport command</i><i> = </i><i>/etc/samba/scripts/addport.sh</i><i> </i></dl>
<p> addprinter command (G) </p>
<dl>
<dd>With the introduction of MS-RPC based printing support for Windows NT/2000 clients in Samba 2.2, The MS Add Printer Wizard (APW) icon is now also available in the &quot;Printers&#8230;&quot; folder displayed a share listing. The APW allows for printers to be add remotely to a Samba or Windows NT/2000 print server. </p>
<p> For a Samba host this means that the printer must be physically added to the underlying printing system. The <i>addprinter command</i> defines a script to be run which will perform the necessary operations for adding the printer to the print system and to add the appropriate service definition to the smb.conf file in order that it can be shared by <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8). </p>
<p> The <i>addprinter command</i> is automatically invoked with the following parameter (in order):</p>
<dl>
<dd>
<dl>
<dd>&bull; <i>printer name</i></dl>
<dl>
<dd>&bull; <i>share name</i></dl>
<dl>
<dd>&bull; <i>port name</i></dl>
<dl>
<dd>&bull; <i>driver name</i></dl>
<dl>
<dd>&bull; <i>location</i></dl>
<dl>
<dd>&bull; <i>Windows 9x driver location</i></dl>
</dl>
<p> All parameters are filled in from the PRINTER_INFO_2 structure sent by the Windows NT/2000 client with one exception. The &quot;Windows 9x driver location&quot; parameter is included for backwards compatibility only. The remaining fields in the structure are generated from answers to the APW questions. </p>
<p> Once the <i>addprinter command</i> has been executed, smbd will reparse the smb.conf to determine if the share defined by the APW exists. If the sharename is still invalid, then smbd will return an ACCESS_DENIED error to the client. </p>
<p> The <i>addprinter command</i> program can output a single line of text, which Samba will set as the port the new printer is connected to. If this line isn&#8217;t output, Samba won&#8217;t reload its printer shares. </p>
<p> Default: <i>addprinter command</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>addprinter command</i><i> = </i><i>/usr/bin/addprinter</i><i> </i></dl>
<p> add share command (G) </p>
<dl>
<dd>Samba 2.2.0 introduced the ability to dynamically add and delete shares via the Windows NT 4.0 Server Manager. The <i>add share command</i> is used to define an external program or script which will add a new service definition to smb.conf. </p>
<p> In order to successfully execute the <i>add share command</i>, smbd requires that the administrator connects using a root account (i.e. uid == 0) or has the SeDiskOperatorPrivilege. Scripts defined in the <i>add share command</i> parameter are executed as root. </p>
<p> When executed, smbd will automatically invoke the <i>add share command</i> with five parameters.</p>
<dl>
<dd>
<dl>
<dd>&bull; <i>configFile</i> &#8211; the location of the global smb.conf file.</dl>
<dl>
<dd>&bull; <i>shareName</i> &#8211; the name of the new share.</dl>
<dl>
<dd>&bull; <i>pathName</i> &#8211; path to an **existing** directory on disk.</dl>
<dl>
<dd>&bull; <i>comment</i> &#8211; comment string to associate with the new share.</dl>
<dl>
<dd>&bull; <i>max connections</i> Number of maximum simultaneous connections to this share.</dl>
</dl>
<p> This parameter is only used to add file shares. To add printer shares, see the m[blue]<code>addprinter command</code>m[]. </p>
<p> Default: <i>add share command</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>add share command</i><i> = </i><i>/usr/local/bin/addshare</i><i> </i></dl>
<p> add user script (G) </p>
<dl>
<dd>This is the full pathname to a script that will be run <i>AS ROOT</i> by <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) under special circumstances described below. </p>
<p> Normally, a Samba server requires that UNIX users are created for all users accessing files on this server. For sites that use Windows NT account databases as their primary user database creating these users and keeping the user list in sync with the Windows NT PDC is an onerous task. This option allows smbd to create the required UNIX users <i>ON DEMAND</i> when a user accesses the Samba server. </p>
<p> When the Windows user attempts to access the Samba server, at login (session setup in the SMB protocol) time, <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) contacts the m[blue]<code>password server</code>m[] and attempts to authenticate the given user with the given password. If the authentication succeeds then smbd attempts to find a UNIX user in the UNIX password database to map the Windows user into. If this lookup fails, and m[blue]<code>add user script</code>m[] is set then smbd will call the specified script <i>AS ROOT</i>, expanding any <i>%u</i> argument to be the user name to create. </p>
<p> If this script successfully creates the user then smbd will continue on as though the UNIX user already existed. In this way, UNIX users are dynamically created to match existing Windows NT accounts. </p>
<p> See also m[blue]<code>security</code>m[], m[blue]<code>password server</code>m[], m[blue]<code>delete user script</code>m[]. </p>
<p> Default: <i>add user script</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>add user script</i><i> = </i><i>/usr/local/samba/bin/add_user %u</i><i> </i></dl>
<p> add user to group script (G) </p>
<dl>
<dd>Full path to the script that will be called when a user is added to a group using the Windows NT domain administration tools. It will be run by <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) <i>AS ROOT</i>. Any <i>%g</i> will be replaced with the group name and any <i>%u</i> will be replaced with the user name. </p>
<p> Note that the adduser command used in the example below does not support the used syntax on all systems. </p>
<p> Default: <i>add user to group script</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>add user to group script</i><i> = </i><i>/usr/sbin/adduser %u %g</i><i> </i></dl>
<p> administrative share (S) </p>
<dl>
<dd>If this parameter is set to <code>yes</code> for a share, then the share will be an administrative share. The Administrative Shares are the default network shares created by all Windows NT-based operating systems. These are shares like C$, D$ or ADMIN$. The type of these shares is STYPE_DISKTREE_HIDDEN. </p>
<p> See the section below on m[blue]<code>security</code>m[] for more information about this option. </p>
<p> Default: <i>administrative share</i><i> = </i><i>no</i><i> </i></dl>
<p> admin users (S) </p>
<dl>
<dd>This is a list of users who will be granted administrative privileges on the share. This means that they will do all file operations as the super-user (root). </p>
<p> You should use this option very carefully, as any user in this list will be able to do anything they like on the share, irrespective of file permissions. </p>
<p> Default: <i>admin users</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>admin users</i><i> = </i><i>jason</i><i> </i></dl>
<p> afs share (S) </p>
<dl>
<dd>This parameter controls whether special AFS features are enabled for this share. If enabled, it assumes that the directory exported via the <i>path</i> parameter is a local AFS import. The special AFS features include the attempt to hand-craft an AFS token if you enabled &#8211;with-fake-kaserver in configure. </p>
<p> Default: <i>afs share</i><i> = </i><i>no</i><i> </i></dl>
<p> afs token lifetime (G) </p>
<dl>
<dd>This parameter controls the lifetime of tokens that the AFS fake-kaserver claims. In reality these never expire but this lifetime controls when the afs client will forget the token. </p>
<p> Set this parameter to 0 to get <code>NEVERDATE</code>. </p>
<p> Default: <i>afs token lifetime</i><i> = </i><i>604800</i><i> </i></dl>
<p> afs username map (G) </p>
<dl>
<dd>If you are using the fake kaserver AFS feature, you might want to hand-craft the usernames you are creating tokens for. For example this is necessary if you have users from several domain in your AFS Protection Database. One possible scheme to code users as DOMAIN+User as it is done by winbind with the + as a separator. </p>
<p> The mapped user name must contain the cell name to log into, so without setting this parameter there will be no token. </p>
<p> Default: <i>afs username map</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>afs username map</i><i> = </i><i>%u [at] afs.samba.org</i><i> </i></dl>
<p> aio max threads (G) </p>
<dl>
<dd>The integer parameter specifies the maximum number of threads each smbd process will create when doing parallel asynchronous IO calls. If the number of outstanding calls is greater than this number the requests will not be refused but go onto a queue and will be scheduled in turn as outstanding requests complete. </p>
<p> Related command: m[blue]<code>aio read size</code>m[] </p>
<p> Related command: m[blue]<code>aio write size</code>m[] </p>
<p> Default: <i>aio max threads</i><i> = </i><i>100</i><i> </i></dl>
<p> aio read size (S) </p>
<dl>
<dd>If this integer parameter is set to a non-zero value, Samba will read from files asynchronously when the request size is bigger than this value. Note that it happens only for non-chained and non-chaining reads and when not using write cache. </p>
<p> The only reasonable values for this parameter are 0 (no async I/O) and 1 (always do async I/O). </p>
<p> Related command: m[blue]<code>write cache size</code>m[] </p>
<p> Related command: m[blue]<code>aio write size</code>m[] </p>
<p> Default: <i>aio read size</i><i> = </i><i>1</i><i> </i> </p>
<p> Example: <i>aio read size</i><i> = </i><i>0 # Always do reads synchronously </i><i> </i></dl>
<p> aio write behind (S) </p>
<dl>
<dd>If Samba has been built with asynchronous I/O support, Samba will not wait until write requests are finished before returning the result to the client for files listed in this parameter. Instead, Samba will immediately return that the write request has been finished successfully, no matter if the operation will succeed or not. This might speed up clients without aio support, but is really dangerous, because data could be lost and files could be damaged. </p>
<p> The syntax is identical to the m[blue]<code>veto files</code>m[] parameter. </p>
<p> Default: <i>aio write behind</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>aio write behind</i><i> = </i><i>/*.tmp/</i><i> </i></dl>
<p> aio write size (S) </p>
<dl>
<dd>If this integer parameter is set to a non-zero value, Samba will write to files asynchronously when the request size is bigger than this value. Note that it happens only for non-chained and non-chaining reads and when not using write cache. </p>
<p> The only reasonable values for this parameter are 0 (no async I/O) and 1 (always do async I/O). </p>
<p> Compared to m[blue]<code>aio read size</code>m[] this parameter has a smaller effect, most writes should end up in the file system cache. Writes that require space allocation might benefit most from going asynchronous. </p>
<p> Related command: m[blue]<code>write cache size</code>m[] </p>
<p> Related command: m[blue]<code>aio read size</code>m[] </p>
<p> Default: <i>aio write size</i><i> = </i><i>1</i><i> </i> </p>
<p> Example: <i>aio write size</i><i> = </i><i>0 # Always do writes synchronously </i><i> </i></dl>
<p> algorithmic rid base (G) </p>
<dl>
<dd>This determines how Samba will use its algorithmic mapping from uids/gid to the RIDs needed to construct NT Security Identifiers. </p>
<p> Setting this option to a larger value could be useful to sites transitioning from WinNT and Win2k, as existing user and group rids would otherwise clash with system users etc. </p>
<p> All UIDs and GIDs must be able to be resolved into SIDs for the correct operation of ACLs on the server. As such the algorithmic mapping can&#8217;t be &#8216;turned off&#8217;, but pushing it &#8216;out of the way&#8217; should resolve the issues. Users and groups can then be assigned &#8216;low&#8217; RIDs in arbitrary-rid supporting backends. </p>
<p> Default: <i>algorithmic rid base</i><i> = </i><i>1000</i><i> </i> </p>
<p> Example: <i>algorithmic rid base</i><i> = </i><i>100000</i><i> </i></dl>
<p> allocation roundup size (S) </p>
<dl>
<dd>This parameter allows an administrator to tune the allocation size reported to Windows clients. This is only useful for old SMB1 clients because modern SMB dialects eliminated that bottleneck and have better performance by default. Using this parameter may cause difficulties for some applications, e.g. MS Visual Studio. If the MS Visual Studio compiler starts to crash with an internal error, set this parameter to zero for this share. Settings this parameter to a large value can also cause small files to allocate more space on the disk than needed. </p>
<p> This parameter is deprecated and will be removed in one of the next Samba releases. </p>
<p> The integer parameter specifies the roundup size in bytes. </p>
<p> Default: <i>allocation roundup size</i><i> = </i><i>0</i><i> </i> </p>
<p> Example: <i>allocation roundup size</i><i> = </i><i>1048576 # (to set it to the former default of 1 MiB)</i><i> </i></dl>
<p> allow dcerpc auth level connect (G) </p>
<dl>
<dd>This option controls whether DCERPC services are allowed to be used with DCERPC_AUTH_LEVEL_CONNECT, which provides authentication, but no per message integrity nor privacy protection. </p>
<p> Some interfaces like samr, lsarpc and netlogon have a hard-coded default of <code>no</code> and epmapper, mgmt and rpcecho have a hard-coded default of <code>yes</code>. </p>
<p> The behavior can be overwritten per interface name (e.g. lsarpc, netlogon, samr, srvsvc, winreg, wkssvc &#8230;) by using &#8216;allow dcerpc auth level connect:interface = yes&#8217; as option. </p>
<p> This option yields precedence to the implementation specific restrictions. E.g. the drsuapi and backupkey protocols require DCERPC_AUTH_LEVEL_PRIVACY. The dnsserver protocol requires DCERPC_AUTH_LEVEL_INTEGRITY. </p>
<p> Default: <i>allow dcerpc auth level connect</i><i> = </i><i>no</i><i> </i> </p>
<p> Example: <i>allow dcerpc auth level connect</i><i> = </i><i>yes</i><i> </i></dl>
<p> allow dns updates (G) </p>
<dl>
<dd>This option determines what kind of updates to the DNS are allowed. </p>
<p> DNS updates can either be disallowed completely by setting it to <code>disabled</code>, enabled over secure connections only by setting it to <code>secure only</code> or allowed in all cases by setting it to <code>nonsecure</code>. </p>
<p> Default: <i>allow dns updates</i><i> = </i><i>secure only</i><i> </i> </p>
<p> Example: <i>allow dns updates</i><i> = </i><i>disabled</i><i> </i></dl>
<p> allow insecure wide links (G) </p>
<dl>
<dd>In normal operation the option m[blue]<code>wide links</code>m[] which allows the server to follow symlinks outside of a share path is automatically disabled when m[blue]<code>unix extensions</code>m[] are enabled on a Samba server. This is done for security purposes to prevent UNIX clients creating symlinks to areas of the server file system that the administrator does not wish to export. </p>
<p> Setting m[blue]<code>allow insecure wide links</code>m[] to true disables the link between these two parameters, removing this protection and allowing a site to configure the server to follow symlinks (by setting m[blue]<code>wide links</code>m[] to &quot;true&quot;) even when m[blue]<code>unix extensions</code>m[] is turned on. </p>
<p> It is not recommended to enable this option unless you fully understand the implications of allowing the server to follow symbolic links created by UNIX clients. For most normal Samba configurations this would be considered a security hole and setting this parameter is not recommended. </p>
<p> This option was added at the request of sites who had deliberately set Samba up in this way and needed to continue supporting this functionality without having to patch the Samba code. </p>
<p> Default: <i>allow insecure wide links</i><i> = </i><i>no</i><i> </i></dl>
<p> allow nt4 crypto (G) </p>
<dl>
<dd>This option controls whether the netlogon server (currently only in &#8216;active directory domain controller&#8217; mode), will reject clients which does not support NETLOGON_NEG_STRONG_KEYS nor NETLOGON_NEG_SUPPORTS_AES. </p>
<p> This option was added with Samba 4.2.0. It may lock out clients which worked fine with Samba versions up to 4.1.x. as the effective default was &quot;yes&quot; there, while it is &quot;no&quot; now. </p>
<p> If you have clients without RequireStrongKey = 1 in the registry, you may need to set &quot;allow nt4 crypto = yes&quot;, until you have fixed all clients. </p>
<p> &quot;allow nt4 crypto = yes&quot; allows weak crypto to be negotiated, maybe via downgrade attacks. </p>
<p> This option yields precedence to the &#8216;reject md5 clients&#8217; option. </p>
<p> Default: <i>allow nt4 crypto</i><i> = </i><i>no</i><i> </i></dl>
<p> allow trusted domains (G) </p>
<dl>
<dd>This option only takes effect when the m[blue]<code>security</code>m[] option is set to <code>server</code>, <code>domain</code> or <code>ads</code>. If it is set to no, then attempts to connect to a resource from a domain or workgroup other than the one which smbd is running in will fail, even if that domain is trusted by the remote server doing the authentication. </p>
<p> This is useful if you only want your Samba server to serve resources to users in the domain it is a member of. As an example, suppose that there are two domains DOMA and DOMB. DOMB is trusted by DOMA, which contains the Samba server. Under normal circumstances, a user with an account in DOMB can then access the resources of a UNIX account with the same account name on the Samba server even if they do not have an account in DOMA. This can make implementing a security boundary difficult. </p>
<p> Default: <i>allow trusted domains</i><i> = </i><i>yes</i><i> </i></dl>
<p> allow unsafe cluster upgrade (G) </p>
<dl>
<dd>If set to no (the default), smbd checks at startup if other smbd versions are running in the cluster and refuses to start if so. This is done to protect data corruption in internal data structures due to incompatible Samba versions running concurrently in the same cluster. Setting this parameter to yes disables this safety check. </p>
<p> Default: <i>allow unsafe cluster upgrade</i><i> = </i><i>no</i><i> </i></dl>
<p> apply group policies (G) </p>
<dl>
<dd>This option controls whether winbind will execute the gpupdate command defined in m[blue]<code>gpo update command</code>m[] on the Group Policy update interval. The Group Policy update interval is defined as every 90 minutes, plus a random offset between 0 and 30 minutes. This applies Group Policy Machine polices to the client or KDC and machine policies to a server. </p>
<p> Default: <i>apply group policies</i><i> = </i><i>no</i><i> </i> </p>
<p> Example: <i>apply group policies</i><i> = </i><i>yes</i><i> </i></dl>
<p> async smb echo handler (G) </p>
<dl>
<dd>This parameter specifies whether Samba should fork the async smb echo handler. It can be beneficial if your file system can block syscalls for a very long time. In some circumstances, it prolongs the timeout that Windows uses to determine whether a connection is dead. This parameter is only for SMB1. For SMB2 and above TCP keepalives can be used instead. </p>
<p> Default: <i>async smb echo handler</i><i> = </i><i>no</i><i> </i></dl>
<p> auth event notification (G) </p>
<dl>
<dd>When enabled, this option causes Samba (acting as an Active Directory Domain Controller) to stream authentication events across the internal message bus. Scripts built using Samba&#8217;s python bindings can listen to these events by registering as the service auth_event. </p>
<p> This should be considered a developer option (it assists in the Samba testsuite) rather than a facility for external auditing, as message delivery is not guaranteed (a feature that the testsuite works around). Additionally Samba must be compiled with the jansson support for this option to be effective. </p>
<p> The authentication events are also logged via the normal logging methods when the m[blue]<code>log level</code>m[] is set appropriately. </p>
<p> Default: <i>auth event notification</i><i> = </i><i>no</i><i> </i></dl>
<p> preload </p>
<dl>
<dd>This parameter is a synonym for auto services.</dl>
<p> auto services (G) </p>
<dl>
<dd>This is a list of services that you want to be automatically added to the browse lists. This is most useful for homes and printers services that would otherwise not be visible. </p>
<p> Note that if you just want all printers in your printcap file loaded then the m[blue]<code>load printers</code>m[] option is easier. </p>
<p> Default: <i>auto services</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>auto services</i><i> = </i><i>fred lp colorlp</i><i> </i></dl>
<p> available (S) </p>
<dl>
<dd>This parameter lets you &quot;turn off&quot; a service. If <i>available = no</i>, then <i>ALL</i> attempts to connect to the service will fail. Such failures are logged. </p>
<p> Default: <i>available</i><i> = </i><i>yes</i><i> </i></dl>
<p> bind dns directory </p>
<dl>
<dd>This parameter is a synonym for binddns dir.</dl>
<p> binddns dir (G) </p>
<dl>
<dd>This parameters defines the directory samba will use to store the configuration files for bind, such as named.conf. NOTE: The bind dns directory needs to be on the same mount point as the private directory! </p>
<p> Default: <i>binddns dir</i><i> = </i><i>/var/lib/samba/bind-dns</i><i> </i></dl>
<p> bind interfaces only (G) </p>
<dl>
<dd>This global parameter allows the Samba admin to limit what interfaces on a machine will serve SMB requests. It affects file service <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) and name service <code><a href="/docs/linux/man/8-nmbd/">nmbd</a></code>(8) in a slightly different ways. </p>
<p> For name service it causes nmbd to bind to ports 137 and 138 on the interfaces listed in the m[blue]<code>interfaces</code>m[] parameter. nmbd also binds to the &quot;all addresses&quot; interface (0.0.0.0) on ports 137 and 138 for the purposes of reading broadcast messages. If this option is not set then nmbd will service name requests on all of these sockets. If m[blue]<code>bind interfaces only</code>m[] is set then nmbd will check the source address of any packets coming in on the broadcast sockets and discard any that don&#8217;t match the broadcast addresses of the interfaces in the m[blue]<code>interfaces</code>m[] parameter list. As unicast packets are received on the other sockets it allows nmbd to refuse to serve names to machines that send packets that arrive through any interfaces not listed in the m[blue]<code>interfaces</code>m[] list. IP Source address spoofing does defeat this simple check, however, so it must not be used seriously as a security feature for nmbd. </p>
<p> For file service it causes <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) to bind only to the interface list given in the m[blue]<code>interfaces</code>m[] parameter. This restricts the networks that smbd will serve, to packets coming in on those interfaces. Note that you should not use this parameter for machines that are serving PPP or other intermittent or non-broadcast network interfaces as it will not cope with non-permanent interfaces. </p>
<p> If m[blue]<code>bind interfaces only</code>m[] is set and the network address <i>127.0.0.1</i> is not added to the m[blue]<code>interfaces</code>m[] parameter list <code><a href="/docs/linux/man/8-smbpasswd/">smbpasswd</a></code>(8) may not work as expected due to the reasons covered below. </p>
<p> To change a users SMB password, the smbpasswd by default connects to the <i>localhost &#8211; 127.0.0.1</i> address as an SMB client to issue the password change request. If m[blue]<code>bind interfaces only</code>m[] is set then unless the network address <i>127.0.0.1</i> is added to the m[blue]<code>interfaces</code>m[] parameter list then smbpasswd will fail to connect in it&#8217;s default mode. smbpasswd can be forced to use the primary IP interface of the local host by using its <code><a href="/docs/linux/man/8-smbpasswd/">smbpasswd</a></code>(8) <i>-r </i><i>remote machine</i> parameter, with <i>remote machine</i> set to the IP name of the primary interface of the local host. </p>
<p> Default: <i>bind interfaces only</i><i> = </i><i>no</i><i> </i></dl>
<p> blocking locks (S) </p>
<dl>
<dd>This parameter controls the behavior of <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) when given a request by a client to obtain a byte range lock on a region of an open file, and the request has a time limit associated with it. </p>
<p> If this parameter is set and the lock range requested cannot be immediately satisfied, samba will internally queue the lock request, and periodically attempt to obtain the lock until the timeout period expires. </p>
<p> If this parameter is set to <code>no</code>, then samba will behave as previous versions of Samba would and will fail the lock request immediately if the lock range cannot be obtained. </p>
<p> Default: <i>blocking locks</i><i> = </i><i>yes</i><i> </i></dl>
<p> block size (S) </p>
<dl>
<dd>This parameter controls the behavior of <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) when reporting disk free sizes. By default, this reports a disk block size of 1024 bytes. </p>
<p> Changing this parameter may have some effect on the efficiency of client writes, this is not yet confirmed. This parameter was added to allow advanced administrators to change it (usually to a higher value) and test the effect it has on client write performance without re-compiling the code. As this is an experimental option it may be removed in a future release. </p>
<p> Changing this option does not change the disk free reporting size, just the block size unit reported to the client. </p>
<p> Default: <i>block size</i><i> = </i><i>1024</i><i> </i> </p>
<p> Example: <i>block size</i><i> = </i><i>4096</i><i> </i></dl>
<p> browsable </p>
<dl>
<dd>This parameter is a synonym for browseable.</dl>
<p> browseable (S) </p>
<dl>
<dd>This controls whether this share is seen in the list of available shares in a net view and in the browse list. </p>
<p> Default: <i>browseable</i><i> = </i><i>yes</i><i> </i></dl>
<p> browse list (G) </p>
<dl>
<dd>This controls whether <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) will serve a browse list to a client doing a NetServerEnum call. Normally set to <code>yes</code>. You should never need to change this. </p>
<p> Default: <i>browse list</i><i> = </i><i>yes</i><i> </i></dl>
<p> cache directory (G) </p>
<dl>
<dd>Usually, most of the TDB files are stored in the <i>lock directory</i>. Since Samba 3.4.0, it is possible to differentiate between TDB files with persistent data and TDB files with non-persistent data using the <i>state directory</i> and the <i>cache directory</i> options. </p>
<p> This option specifies the directory for storing TDB files containing non-persistent data that will be kept across service restarts. The directory should be placed on persistent storage, but the data can be safely deleted by an administrator. </p>
<p> Default: <i>cache directory</i><i> = </i><i>/var/cache/samba</i><i> </i> </p>
<p> Example: <i>cache directory</i><i> = </i><i>/var/run/samba/locks/cache</i><i> </i></dl>
<p> casesignames </p>
<dl>
<dd>This parameter is a synonym for case sensitive.</dl>
<p> case sensitive (S) </p>
<dl>
<dd>See the discussion in the section m[blue]<code>name mangling</code>m[]. </p>
<p> Default: <i>case sensitive</i><i> = </i><i>auto</i><i> </i></dl>
<p> change notify (G) </p>
<dl>
<dd>This parameter specifies whether Samba should reply to a client&#8217;s file change notify requests. </p>
<p> You should never need to change this parameter </p>
<p> Default: <i>change notify</i><i> = </i><i>yes</i><i> </i></dl>
<p> change share command (G) </p>
<dl>
<dd>Samba 2.2.0 introduced the ability to dynamically add and delete shares via the Windows NT 4.0 Server Manager. The <i>change share command</i> is used to define an external program or script which will modify an existing service definition in smb.conf. </p>
<p> In order to successfully execute the <i>change share command</i>, smbd requires that the administrator connects using a root account (i.e. uid == 0) or has the SeDiskOperatorPrivilege. Scripts defined in the <i>change share command</i> parameter are executed as root. </p>
<p> When executed, smbd will automatically invoke the <i>change share command</i> with six parameters.</p>
<dl>
<dd>
<dl>
<dd>&bull; <i>configFile</i> &#8211; the location of the global smb.conf file.</dl>
<dl>
<dd>&bull; <i>shareName</i> &#8211; the name of the new share.</dl>
<dl>
<dd>&bull; <i>pathName</i> &#8211; path to an **existing** directory on disk.</dl>
<dl>
<dd>&bull; <i>comment</i> &#8211; comment string to associate with the new share.</dl>
<dl>
<dd>&bull; <i>max connections</i> Number of maximum simultaneous connections to this share.</dl>
<dl>
<dd>&bull; <i>CSC policy</i> &#8211; client side caching policy in string form. Valid values are: manual, documents, programs, disable.</dl>
</dl>
<p> This parameter is only used to modify existing file share definitions. To modify printer shares, use the &quot;Printers&#8230;&quot; folder as seen when browsing the Samba host. </p>
<p> Default: <i>change share command</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>change share command</i><i> = </i><i>/usr/local/bin/changeshare</i><i> </i></dl>
<p> check parent directory delete on close (S) </p>
<dl>
<dd>A Windows SMB server prevents the client from creating files in a directory that has the delete-on-close flag set. By default Samba doesn&#8217;t perform this check as this check is a quite expensive operation in Samba. </p>
<p> Default: <i>check parent directory delete on close</i><i> = </i><i>no</i><i> </i></dl>
<p> check password script (G) </p>
<dl>
<dd>The name of a program that can be used to check password complexity. The password is sent to the program&#8217;s standard input. </p>
<p> The program must return 0 on a good password, or any other value if the password is bad. In case the password is considered weak (the program does not return 0) the user will be notified and the password change will fail. </p>
<p> In Samba AD, this script will be run <i>AS ROOT</i> by <code><a href="/docs/linux/man/8-samba/">samba</a></code>(8) without any substitutions. </p>
<p> Note that starting with Samba 4.11 the following environment variables are exported to the script:</p>
<dl>
<dd>
<dl>
<dd>&bull; SAMBA_CPS_ACCOUNT_NAME is always present and contains the sAMAccountName of user, the is the same as the %u substitutions in the none AD DC case.</dl>
<dl>
<dd>&bull; SAMBA_CPS_USER_PRINCIPAL_NAME is optional in the AD DC case if the userPrincipalName is present.</dl>
<dl>
<dd>&bull; SAMBA_CPS_FULL_NAME is optional if the displayName is present.</dl>
</dl>
<p> Note: In the example directory is a sample program called crackcheck that uses cracklib to check the password quality. </p>
<p> Default: <i>check password script</i><i> = </i><i> # Disabled</i><i> </i> </p>
<p> Example: <i>check password script</i><i> = </i><i>/usr/local/sbin/crackcheck</i><i> </i></dl>
<p> cldap port (G) </p>
<dl>
<dd>This option controls the port used by the CLDAP protocol. </p>
<p> Default: <i>cldap port</i><i> = </i><i>389</i><i> </i> </p>
<p> Example: <i>cldap port</i><i> = </i><i>3389</i><i> </i></dl>
<p> client ipc max protocol (G) </p>
<dl>
<dd>The value of the parameter (a string) is the highest protocol level that will be supported for IPC$ connections as DCERPC transport. </p>
<p> Normally this option should not be set as the automatic negotiation phase in the SMB protocol takes care of choosing the appropriate protocol. </p>
<p> The value <code>default</code> refers to the latest supported protocol, currently <code>SMB3_11</code>. </p>
<p> See m[blue]<code>client max protocol</code>m[] for a full list of available protocols. The values CORE, COREPLUS, LANMAN1, LANMAN2 are silently upgraded to NT1. </p>
<p> Default: <i>client ipc max protocol</i><i> = </i><i>default</i><i> </i> </p>
<p> Example: <i>client ipc max protocol</i><i> = </i><i>SMB2_10</i><i> </i></dl>
<p> client ipc min protocol (G) </p>
<dl>
<dd>This setting controls the minimum protocol version that the will be attempted to use for IPC$ connections as DCERPC transport. </p>
<p> Normally this option should not be set as the automatic negotiation phase in the SMB protocol takes care of choosing the appropriate protocol. </p>
<p> The value <code>default</code> refers to the higher value of <code>NT1</code> and the effective value of m[blue]<code>client min protocol</code>m[]. </p>
<p> See m[blue]<code>client max protocol</code>m[] for a full list of available protocols. The values CORE, COREPLUS, LANMAN1, LANMAN2 are silently upgraded to NT1. </p>
<p> Default: <i>client ipc min protocol</i><i> = </i><i>default</i><i> </i> </p>
<p> Example: <i>client ipc min protocol</i><i> = </i><i>SMB3_11</i><i> </i></dl>
<p> client ipc signing (G) </p>
<dl>
<dd>This controls whether the client is allowed or required to use SMB signing for IPC$ connections as DCERPC transport. Possible values are <i>auto</i>, <i>mandatory</i> and <i>disabled</i>. </p>
<p> When set to mandatory or default, SMB signing is required. </p>
<p> When set to auto, SMB signing is offered, but not enforced and if set to disabled, SMB signing is not offered either. </p>
<p> Connections from winbindd to Active Directory Domain Controllers always enforce signing. </p>
<p> Default: <i>client ipc signing</i><i> = </i><i>default</i><i> </i></dl>
<p> client lanman auth (G) </p>
<dl>
<dd>This parameter determines whether or not <code><a href="/docs/linux/man/8-smbclient/">smbclient</a></code>(8) and other samba client tools will attempt to authenticate itself to servers using the weaker LANMAN password hash. If disabled, only server which support NT password hashes (e.g. Windows NT/2000, Samba, etc&#8230; but not Windows 95/98) will be able to be connected from the Samba client. </p>
<p> The LANMAN encrypted response is easily broken, due to its case-insensitive nature, and the choice of algorithm. Clients without Windows 95/98 servers are advised to disable this option. </p>
<p> Disabling this option will also disable the client plaintext auth option. </p>
<p> Likewise, if the client ntlmv2 auth parameter is enabled, then only NTLMv2 logins will be attempted. </p>
<p> Default: <i>client lanman auth</i><i> = </i><i>no</i><i> </i></dl>
<p> client ldap sasl wrapping (G) </p>
<dl>
<dd>The m[blue]<code>client ldap sasl wrapping</code>m[] defines whether ldap traffic will be signed or signed and encrypted (sealed). Possible values are <i>plain</i>, <i>sign</i> and <i>seal</i>. </p>
<p> The values <i>sign</i> and <i>seal</i> are only available if Samba has been compiled against a modern OpenLDAP version (2.3.x or higher). </p>
<p> This option is needed in the case of Domain Controllers enforcing the usage of signed LDAP connections (e.g. Windows 2000 SP3 or higher). LDAP sign and seal can be controlled with the registry key &quot;HKLM\System\CurrentControlSet\Services\ NTDS\Parameters\LDAPServerIntegrity&quot; on the Windows server side. </p>
<p> Depending on the used KRB5 library (MIT and older Heimdal versions) it is possible that the message &quot;integrity only&quot; is not supported. In this case, <i>sign</i> is just an alias for <i>seal</i>. </p>
<p> The default value is <i>sign</i>. That implies synchronizing the time with the KDC in the case of using <i>Kerberos</i>. </p>
<p> Default: <i>client ldap sasl wrapping</i><i> = </i><i>sign</i><i> </i></dl>
<p> client max protocol (G) </p>
<dl>
<dd>The value of the parameter (a string) is the highest protocol level that will be supported by the client. </p>
<p> Possible values are :</p>
<dl>
<dd>
<dl>
<dd>&bull; <code>CORE</code>: Earliest version. No concept of user names.</dl>
<dl>
<dd>&bull; <code>COREPLUS</code>: Slight improvements on CORE for efficiency.</dl>
<dl>
<dd>&bull; <code>LANMAN1</code>: First <i>modern</i> version of the protocol. Long filename support.</dl>
<dl>
<dd>&bull; <code>LANMAN2</code>: Updates to Lanman1 protocol.</dl>
<dl>
<dd>&bull; <code>NT1</code>: Current up to date version of the protocol. Used by Windows NT. Known as CIFS.</dl>
<dl>
<dd>&bull; <code>SMB2</code>: Re-implementation of the SMB protocol. Used by Windows Vista and later versions of Windows. SMB2 has sub protocols available.</p>
<dl>
<dd>
<dl>
<dd>&bull; <code>SMB2_02</code>: The earliest SMB2 version.</dl>
<dl>
<dd>&bull; <code>SMB2_10</code>: Windows 7 SMB2 version.</dl>
<dl>
<dd>&bull; <code>SMB2_22</code>: Early Windows 8 SMB2 version.</dl>
<dl>
<dd>&bull; <code>SMB2_24</code>: Windows 8 beta SMB2 version.</dl>
</dl>
<p> By default SMB2 selects the SMB2_10 variant.</dl>
<dl>
<dd>&bull; <code>SMB3</code>: The same as SMB2. Used by Windows 8. SMB3 has sub protocols available.</p>
<dl>
<dd>
<dl>
<dd>&bull; <code>SMB3_00</code>: Windows 8 SMB3 version. (mostly the same as SMB2_24)</dl>
<dl>
<dd>&bull; <code>SMB3_02</code>: Windows 8.1 SMB3 version.</dl>
<dl>
<dd>&bull; <code>SMB3_10</code>: early Windows 10 technical preview SMB3 version.</dl>
<dl>
<dd>&bull; <code>SMB3_11</code>: Windows 10 technical preview SMB3 version (maybe final).</dl>
</dl>
<p> By default SMB3 selects the SMB3_11 variant.</dl>
</dl>
<p> Normally this option should not be set as the automatic negotiation phase in the SMB protocol takes care of choosing the appropriate protocol. </p>
<p> The value <code>default</code> refers to <code>SMB3_11</code>. </p>
<p> IPC$ connections for DCERPC e.g. in winbindd, are handled by the m[blue]<code>client ipc max protocol</code>m[] option. </p>
<p> Default: <i>client max protocol</i><i> = </i><i>default</i><i> </i> </p>
<p> Example: <i>client max protocol</i><i> = </i><i>LANMAN1</i><i> </i></dl>
<p> client min protocol (G) </p>
<dl>
<dd>This setting controls the minimum protocol version that the client will attempt to use. </p>
<p> Normally this option should not be set as the automatic negotiation phase in the SMB protocol takes care of choosing the appropriate protocol unless you connect to a legacy SMB1-only server. </p>
<p> See Related command: m[blue]<code>client max protocol</code>m[] for a full list of available protocols. </p>
<p> IPC$ connections for DCERPC e.g. in winbindd, are handled by the m[blue]<code>client ipc min protocol</code>m[] option. </p>
<p> Note that most command line tools support &#8211;option=&#8217;client min protocol=NT1&#8242;, so it may not be required to enable SMB1 protocols globally in smb.conf. </p>
<p> Default: <i>client min protocol</i><i> = </i><i>SMB2_02</i><i> </i> </p>
<p> Example: <i>client min protocol</i><i> = </i><i>NT1</i><i> </i></dl>
<p> client NTLMv2 auth (G) </p>
<dl>
<dd>This parameter determines whether or not <code><a href="/docs/linux/man/8-smbclient/">smbclient</a></code>(8) will attempt to authenticate itself to servers using the NTLMv2 encrypted password response. </p>
<p> If enabled, only an NTLMv2 and LMv2 response (both much more secure than earlier versions) will be sent. Older servers (including NT4 &lt; SP4, Win9x and Samba 2.2) are not compatible with NTLMv2 when not in an NTLMv2 supporting domain </p>
<p> Similarly, if enabled, NTLMv1, client lanman auth and client plaintext auth authentication will be disabled. This also disables share-level authentication. </p>
<p> If disabled, an NTLM response (and possibly a LANMAN response) will be sent by the client, depending on the value of client lanman auth. </p>
<p> Note that Windows Vista and later versions already use NTLMv2 by default, and some sites (particularly those following &#8216;best practice&#8217; security polices) only allow NTLMv2 responses, and not the weaker LM or NTLM. </p>
<p> When m[blue]<code>client use spnego</code>m[] is also set to <code>yes</code> extended security (SPNEGO) is required in order to use NTLMv2 only within NTLMSSP. This behavior was introduced with the patches for CVE-2016-2111. </p>
<p> Default: <i>client NTLMv2 auth</i><i> = </i><i>yes</i><i> </i></dl>
<p> client plaintext auth (G) </p>
<dl>
<dd>Specifies whether a client should send a plaintext password if the server does not support encrypted passwords. </p>
<p> Default: <i>client plaintext auth</i><i> = </i><i>no</i><i> </i></dl>
<p> client schannel (G) </p>
<dl>
<dd>This option is deprecated with Samba 4.8 and will be removed in future. At the same time the default changed to yes, which will be the hardcoded behavior in future. </p>
<p> This controls whether the client offers or even demands the use of the netlogon schannel. m[blue]<code>client schannel = no</code>m[] does not offer the schannel, m[blue]<code>client schannel = auto</code>m[] offers the schannel but does not enforce it, and m[blue]<code>client schannel = yes</code>m[] denies access if the server is not able to speak netlogon schannel. </p>
<p> Note that for active directory domains this is hardcoded to m[blue]<code>client schannel = yes</code>m[]. </p>
<p> This option yields precedence to the m[blue]<code>require strong key</code>m[] option. </p>
<p> Default: <i>client schannel</i><i> = </i><i>yes</i><i> </i> </p>
<p> Example: <i>client schannel</i><i> = </i><i>auto</i><i> </i></dl>
<p> client signing (G) </p>
<dl>
<dd>This controls whether the client is allowed or required to use SMB signing. Possible values are <i>auto</i>, <i>mandatory</i> and <i>disabled</i>. </p>
<p> When set to auto or default, SMB signing is offered, but not enforced. </p>
<p> When set to mandatory, SMB signing is required and if set to disabled, SMB signing is not offered either. </p>
<p> IPC$ connections for DCERPC e.g. in winbindd, are handled by the m[blue]<code>client ipc signing</code>m[] option. </p>
<p> Default: <i>client signing</i><i> = </i><i>default</i><i> </i></dl>
<p> client use spnego principal (G) </p>
<dl>
<dd>This parameter determines whether or not <code><a href="/docs/linux/man/8-smbclient/">smbclient</a></code>(8) and other samba components acting as a client will attempt to use the server-supplied principal sometimes given in the SPNEGO exchange. </p>
<p> If enabled, Samba can attempt to use Kerberos to contact servers known only by IP address. Kerberos relies on names, so ordinarily cannot function in this situation. </p>
<p> This is a VERY BAD IDEA for security reasons, and so this parameter SHOULD NOT BE USED. It will be removed in a future version of Samba. </p>
<p> If disabled, Samba will use the name used to look up the server when asking the KDC for a ticket. This avoids situations where a server may impersonate another, soliciting authentication as one principal while being known on the network as another. </p>
<p> Note that Windows XP SP2 and later versions already follow this behaviour, and Windows Vista and later servers no longer supply this &#8216;rfc4178 hint&#8217; principal on the server side. </p>
<p> This parameter is deprecated in Samba 4.2.1 and will be removed (along with the functionality) in a later release of Samba. </p>
<p> Default: <i>client use spnego principal</i><i> = </i><i>no</i><i> </i></dl>
<p> client use spnego (G) </p>
<dl>
<dd>This variable controls whether Samba clients will try to use Simple and Protected NEGOciation (as specified by rfc2478) with supporting servers (including WindowsXP, Windows2000 and Samba 3.0) to agree upon an authentication mechanism. This enables Kerberos authentication in particular. </p>
<p> When m[blue]<code>client NTLMv2 auth</code>m[] is also set to <code>yes</code> extended security (SPNEGO) is required in order to use NTLMv2 only within NTLMSSP. This behavior was introduced with the patches for CVE-2016-2111. </p>
<p> Default: <i>client use spnego</i><i> = </i><i>yes</i><i> </i></dl>
<p> cluster addresses (G) </p>
<dl>
<dd>With this parameter you can add additional addresses that nmbd will register with a WINS server. Similarly, these addresses will be registered by default when <i>net ads dns register</i> is called with m[blue]<code>clustering = yes</code>m[] configured. </p>
<p> Default: <i>cluster addresses</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>cluster addresses</i><i> = </i><i>10.0.0.1 10.0.0.2 10.0.0.3</i><i> </i></dl>
<p> clustering (G) </p>
<dl>
<dd>This parameter specifies whether Samba should contact ctdb for accessing its tdb files and use ctdb as a backend for its messaging backend. </p>
<p> Set this parameter to yes only if you have a cluster setup with ctdb running. </p>
<p> Default: <i>clustering</i><i> = </i><i>no</i><i> </i></dl>
<p> comment (S) </p>
<dl>
<dd>This is a text field that is seen next to a share when a client does a queries the server, either via the network neighborhood or via net view to list what shares are available. </p>
<p> If you want to set the string that is displayed next to the machine name then see the m[blue]<code>server string</code>m[] parameter. </p>
<p> Default: <i>comment</i><i> = </i><i> # No comment</i><i> </i> </p>
<p> Example: <i>comment</i><i> = </i><i>Fred&#8217;s Files</i><i> </i></dl>
<p> config backend (G) </p>
<dl>
<dd>This controls the backend for storing the configuration. Possible values are <i>file</i> (the default) and <i>registry</i>. When m[blue]<code>config backend = registry</code>m[] is encountered while loading <i>smb.conf</i>, the configuration read so far is dropped and the global options are read from registry instead. So this triggers a registry only configuration. Share definitions are not read immediately but instead <i>registry shares</i> is set to <i>yes</i>. </p>
<p> Note: This option can not be set inside the registry configuration itself. </p>
<p> Default: <i>config backend</i><i> = </i><i>file</i><i> </i> </p>
<p> Example: <i>config backend</i><i> = </i><i>registry</i><i> </i></dl>
<p> config file (G) </p>
<dl>
<dd>This allows you to override the config file to use, instead of the default (usually smb.conf). There is a chicken and egg problem here as this option is set in the config file! </p>
<p> For this reason, if the name of the config file has changed when the parameters are loaded then it will reload them from the new config file. </p>
<p> This option takes the usual substitutions, which can be very useful. </p>
<p> If the config file doesn&#8217;t exist then it won&#8217;t be loaded (allowing you to special case the config files of just a few clients). </p>
<p> <i>No default</i> </p>
<p> Example: <i>config file</i><i> = </i><i>/usr/local/samba/lib/smb.conf.%m</i><i> </i></dl>
<p> copy (S) </p>
<dl>
<dd>This parameter allows you to &quot;clone&quot; service entries. The specified service is simply duplicated under the current service&#8217;s name. Any parameters specified in the current section will override those in the section being copied. </p>
<p> This feature lets you set up a &#8216;template&#8217; service and create similar services easily. Note that the service being copied must occur earlier in the configuration file than the service doing the copying. </p>
<p> Default: <i>copy</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>copy</i><i> = </i><i>otherservice</i><i> </i></dl>
<p> create krb5 conf (G) </p>
<dl>
<dd>Setting this parameter to no prevents winbind from creating custom krb5.conf files. Winbind normally does this because the krb5 libraries are not AD-site-aware and thus would pick any domain controller out of potentially very many. Winbind is site-aware and makes the krb5 libraries use a local DC by creating its own krb5.conf files. </p>
<p> Preventing winbind from doing this might become necessary if you have to add special options into your system-krb5.conf that winbind does not see. </p>
<p> Default: <i>create krb5 conf</i><i> = </i><i>yes</i><i> </i></dl>
<p> create mode </p>
<dl>
<dd>This parameter is a synonym for create mask.</dl>
<p> create mask (S) </p>
<dl>
<dd>When a file is created, the necessary permissions are calculated according to the mapping from DOS modes to UNIX permissions, and the resulting UNIX mode is then bit-wise &#8216;AND&#8217;ed with this parameter. This parameter may be thought of as a bit-wise MASK for the UNIX modes of a file. Any bit <i>not</i> set here will be removed from the modes set on a file when it is created. </p>
<p> The default value of this parameter removes the group and other write and execute bits from the UNIX modes. </p>
<p> Following this Samba will bit-wise &#8216;OR&#8217; the UNIX mode created from this parameter with the value of the m[blue]<code>force create mode</code>m[] parameter which is set to 000 by default. </p>
<p> This parameter does not affect directory masks. See the parameter m[blue]<code>directory mask</code>m[] for details. </p>
<p> Default: <i>create mask</i><i> = </i><i>0744</i><i> </i> </p>
<p> Example: <i>create mask</i><i> = </i><i>0775</i><i> </i></dl>
<p> csc policy (S) </p>
<dl>
<dd>This stands for <i>client-side caching policy</i>, and specifies how clients capable of offline caching will cache the files in the share. The valid values are: manual, documents, programs, disable. </p>
<p> These values correspond to those used on Windows servers. </p>
<p> For example, shares containing roaming profiles can have offline caching disabled using m[blue]<code>csc policy = disable</code>m[]. </p>
<p> Default: <i>csc policy</i><i> = </i><i>manual</i><i> </i> </p>
<p> Example: <i>csc policy</i><i> = </i><i>programs</i><i> </i></dl>
<p> ctdbd socket (G) </p>
<dl>
<dd>If you set clustering=yes, you need to tell Samba where ctdbd listens on its unix domain socket. The default path as of ctdb 1.0 is /tmp/ctdb.socket which you have to explicitly set for Samba in smb.conf. </p>
<p> Default: <i>ctdbd socket</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>ctdbd socket</i><i> = </i><i>/tmp/ctdb.socket</i><i> </i></dl>
<p> ctdb locktime warn threshold (G) </p>
<dl>
<dd>In a cluster environment using Samba and ctdb it is critical that locks on central ctdb-hosted databases like locking.tdb are not held for long. With the current Samba architecture it happens that Samba takes a lock and while holding that lock makes file system calls into the shared cluster file system. This option makes Samba warn if it detects that it has held locks for the specified number of milliseconds. If this happens, <i>smbd</i> will emit a debug level 0 message into its logs and potentially into syslog. The most likely reason for such a log message is that an operation of the cluster file system Samba exports is taking longer than expected. The messages are meant as a debugging aid for potential cluster problems. </p>
<p> The default value of 0 disables this logging. </p>
<p> Default: <i>ctdb locktime warn threshold</i><i> = </i><i>0</i><i> </i></dl>
<p> ctdb timeout (G) </p>
<dl>
<dd>This parameter specifies a timeout in milliseconds for the connection between Samba and ctdb. It is only valid if you have compiled Samba with clustering and if you have set <i>clustering=yes</i>. </p>
<p> When something in the cluster blocks, it can happen that we wait indefinitely long for ctdb, just adding to the blocking condition. In a well-running cluster this should never happen, but there are too many components in a cluster that might have hickups. Choosing the right balance for this value is very tricky, because on a busy cluster long service times to transfer something across the cluster might be valid. Setting it too short will degrade the service your cluster presents, setting it too long might make the cluster itself not recover from something severely broken for too long. </p>
<p> Be aware that if you set this parameter, this needs to be in the file smb.conf, it is not really helpful to put this into a registry configuration (typical on a cluster), because to access the registry contact to ctdb is required. </p>
<p> Setting <i>ctdb timeout</i> to n makes any process waiting longer than n milliseconds for a reply by the cluster panic. Setting it to 0 (the default) makes Samba block forever, which is the highly recommended default. </p>
<p> Default: <i>ctdb timeout</i><i> = </i><i>0</i><i> </i></dl>
<p> cups connection timeout (G) </p>
<dl>
<dd>This parameter is only applicable if m[blue]<code>printing</code>m[] is set to <code>cups</code>. </p>
<p> If set, this option specifies the number of seconds that smbd will wait whilst trying to contact to the CUPS server. The connection will fail if it takes longer than this number of seconds. </p>
<p> Default: <i>cups connection timeout</i><i> = </i><i>30</i><i> </i> </p>
<p> Example: <i>cups connection timeout</i><i> = </i><i>60</i><i> </i></dl>
<p> cups encrypt (G) </p>
<dl>
<dd>This parameter is only applicable if m[blue]<code>printing</code>m[] is set to <code>cups</code> and if you use CUPS newer than 1.0.x.It is used to define whether or not Samba should use encryption when talking to the CUPS server. Possible values are <i>auto</i>, <i>yes</i> and <i>no</i> </p>
<p> When set to auto we will try to do a TLS handshake on each CUPS connection setup. If that fails, we will fall back to unencrypted operation. </p>
<p> Default: <i>cups encrypt</i><i> = </i><i>no</i><i> </i></dl>
<p> cups options (S) </p>
<dl>
<dd>This parameter is only applicable if m[blue]<code>printing</code>m[] is set to <code>cups</code>. Its value is a free form string of options passed directly to the cups library. </p>
<p> You can pass any generic print option known to CUPS (as listed in the CUPS &quot;Software Users&#8217; Manual&quot;). You can also pass any printer specific option (as listed in &quot;lpoptions -d printername -l&quot;) valid for the target queue. Multiple parameters should be space-delimited name/value pairs according to the PAPI text option ABNF specification. Collection values (&quot;name={a=&#8230; b=&#8230; c=&#8230;}&quot;) are stored with the curley brackets intact. </p>
<p> You should set this parameter to <code>raw</code> if your CUPS server error_log file contains messages such as &quot;Unsupported format &#8216;application/octet-stream&#8217;&quot; when printing from a Windows client through Samba. It is no longer necessary to enable system wide raw printing in /etc/cups/mime.{convs,types}. </p>
<p> Default: <i>cups options</i><i> = </i><i>&quot;&quot;</i><i> </i> </p>
<p> Example: <i>cups options</i><i> = </i><i>&quot;raw media=a4&quot;</i><i> </i></dl>
<p> cups server (G) </p>
<dl>
<dd>This parameter is only applicable if m[blue]<code>printing</code>m[] is set to <code>cups</code>. </p>
<p> If set, this option overrides the ServerName option in the CUPS client.conf. This is necessary if you have virtual samba servers that connect to different CUPS daemons. </p>
<p> Optionally, a port can be specified by separating the server name and port number with a colon. If no port was specified, the default port for IPP (631) will be used. </p>
<p> Default: <i>cups server</i><i> = </i><i>&quot;&quot;</i><i> </i> </p>
<p> Example: <i>cups server</i><i> = </i><i>mycupsserver</i><i> </i> </p>
<p> Example: <i>cups server</i><i> = </i><i>mycupsserver:1631</i><i> </i></dl>
<p> dcerpc endpoint servers (G) </p>
<dl>
<dd>Specifies which DCE/RPC endpoint servers should be run. </p>
<p> Default: <i>dcerpc endpoint servers</i><i> = </i><i>epmapper, wkssvc, rpcecho, samr, netlogon, lsarpc, drsuapi, dssetup, unixinfo, browser, eventlog6, backupkey, dnsserver</i><i> </i> </p>
<p> Example: <i>dcerpc endpoint servers</i><i> = </i><i>rpcecho</i><i> </i></dl>
<p> deadtime (G) </p>
<dl>
<dd>The value of the parameter (a decimal integer) represents the number of minutes of inactivity before a connection is considered dead, and it is disconnected. The deadtime only takes effect if the number of open files is zero. </p>
<p> This is useful to stop a server&#8217;s resources being exhausted by a large number of inactive connections. </p>
<p> Most clients have an auto-reconnect feature when a connection is broken so in most cases this parameter should be transparent to users. </p>
<p> Using this parameter with a timeout of a few minutes is recommended for most systems. </p>
<p> A deadtime of zero indicates that no auto-disconnection should be performed. </p>
<p> Default: <i>deadtime</i><i> = </i><i>10080</i><i> </i> </p>
<p> Example: <i>deadtime</i><i> = </i><i>15</i><i> </i></dl>
<p> debug class (G) </p>
<dl>
<dd>With this boolean parameter enabled, the debug class (DBGC_CLASS) will be displayed in the debug header. </p>
<p> For more information about currently available debug classes, see section about m[blue]<code>log level</code>m[]. </p>
<p> Default: <i>debug class</i><i> = </i><i>no</i><i> </i></dl>
<p> debug encryption (G) </p>
<dl>
<dd>This option will make the smbd server and client code using libsmb (smbclient, smbget, smbspool, &#8230;) dump the Session Id, the decrypted Session Key, the Signing Key, the Application Key, the Encryption Key and the Decryption Key every time an SMB3+ session is established. This information will be printed in logs at level 0. </p>
<p> Warning: access to these values enables the decryption of any encrypted traffic on the dumped sessions. This option should only be enabled for debugging purposes. </p>
<p> Default: <i>debug encryption</i><i> = </i><i>no</i><i> </i></dl>
<p> debug hires timestamp (G) </p>
<dl>
<dd>Sometimes the timestamps in the log messages are needed with a resolution of higher that seconds, this boolean parameter adds microsecond resolution to the timestamp message header when turned on. </p>
<p> Note that the parameter m[blue]<code>debug timestamp</code>m[] must be on for this to have an effect. </p>
<p> Default: <i>debug hires timestamp</i><i> = </i><i>yes</i><i> </i></dl>
<p> debug pid (G) </p>
<dl>
<dd>When using only one log file for more then one forked <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8)-process there may be hard to follow which process outputs which message. This boolean parameter is adds the process-id to the timestamp message headers in the logfile when turned on. </p>
<p> Note that the parameter m[blue]<code>debug timestamp</code>m[] must be on for this to have an effect. </p>
<p> Default: <i>debug pid</i><i> = </i><i>no</i><i> </i></dl>
<p> debug prefix timestamp (G) </p>
<dl>
<dd>With this option enabled, the timestamp message header is prefixed to the debug message without the filename and function information that is included with the m[blue]<code>debug timestamp</code>m[] parameter. This gives timestamps to the messages without adding an additional line. </p>
<p> Note that this parameter overrides the m[blue]<code>debug timestamp</code>m[] parameter. </p>
<p> Default: <i>debug prefix timestamp</i><i> = </i><i>no</i><i> </i></dl>
<p> debug uid (G) </p>
<dl>
<dd>Samba is sometimes run as root and sometime run as the connected user, this boolean parameter inserts the current euid, egid, uid and gid to the timestamp message headers in the log file if turned on. </p>
<p> Note that the parameter m[blue]<code>debug timestamp</code>m[] must be on for this to have an effect. </p>
<p> Default: <i>debug uid</i><i> = </i><i>no</i><i> </i></dl>
<p> dedicated keytab file (G) </p>
<dl>
<dd>Specifies the absolute path to the kerberos keytab file when m[blue]<code>kerberos method</code>m[] is set to &quot;dedicated keytab&quot;. </p>
<p> Default: <i>dedicated keytab file</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>dedicated keytab file</i><i> = </i><i>/usr/local/etc/krb5.keytab</i><i> </i></dl>
<p> default case (S) </p>
<dl>
<dd>See the section on m[blue]<code>name mangling</code>m[]. Also note the m[blue]<code>short preserve case</code>m[] parameter. </p>
<p> Default: <i>default case</i><i> = </i><i>lower</i><i> </i></dl>
<p> default devmode (S) </p>
<dl>
<dd>This parameter is only applicable to m[blue]<code>printable</code>m[] services. When smbd is serving Printer Drivers to Windows NT/2k/XP clients, each printer on the Samba server has a Device Mode which defines things such as paper size and orientation and duplex settings. The device mode can only correctly be generated by the printer driver itself (which can only be executed on a Win32 platform). Because smbd is unable to execute the driver code to generate the device mode, the default behavior is to set this field to NULL. </p>
<p> Most problems with serving printer drivers to Windows NT/2k/XP clients can be traced to a problem with the generated device mode. Certain drivers will do things such as crashing the client&#8217;s Explorer.exe with a NULL devmode. However, other printer drivers can cause the client&#8217;s spooler service (spoolsv.exe) to die if the devmode was not created by the driver itself (i.e. smbd generates a default devmode). </p>
<p> This parameter should be used with care and tested with the printer driver in question. It is better to leave the device mode to NULL and let the Windows client set the correct values. Because drivers do not do this all the time, setting default devmode = yes will instruct smbd to generate a default one. </p>
<p> For more information on Windows NT/2k printing and Device Modes, see the MSDN documentation. </p>
<p> Default: <i>default devmode</i><i> = </i><i>yes</i><i> </i></dl>
<p> default </p>
<dl>
<dd>This parameter is a synonym for default service.</dl>
<p> default service (G) </p>
<dl>
<dd>This parameter specifies the name of a service which will be connected to if the service actually requested cannot be found. Note that the square brackets are <i>NOT</i> given in the parameter value (see example below). </p>
<p> There is no default value for this parameter. If this parameter is not given, attempting to connect to a nonexistent service results in an error. </p>
<p> Typically the default service would be a m[blue]<code>guest ok</code>m[], m[blue]<code>read-only</code>m[] service. </p>
<p> Also note that the apparent service name will be changed to equal that of the requested service, this is very useful as it allows you to use macros like <i>%S</i> to make a wildcard service. </p>
<p> Note also that any &quot;_&quot; characters in the name of the service used in the default service will get mapped to a &quot;/&quot;. This allows for interesting things. </p>
<p> Default: <i>default service</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>default service</i><i> = </i><i>pub</i><i> </i></dl>
<p> defer sharing violations (G) </p>
<dl>
<dd>Windows allows specifying how a file will be shared with other processes when it is opened. Sharing violations occur when a file is opened by a different process using options that violate the share settings specified by other processes. This parameter causes smbd to act as a Windows server does, and defer returning a &quot;sharing violation&quot; error message for up to one second, allowing the client to close the file causing the violation in the meantime. </p>
<p> UNIX by default does not have this behaviour. </p>
<p> There should be no reason to turn off this parameter, as it is designed to enable Samba to more correctly emulate Windows. </p>
<p> Default: <i>defer sharing violations</i><i> = </i><i>yes</i><i> </i></dl>
<p> delete group script (G) </p>
<dl>
<dd>This is the full pathname to a script that will be run <i>AS ROOT</i> by <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) when a group is requested to be deleted. It will expand any <i>%g</i> to the group name passed. This script is only useful for installations using the Windows NT domain administration tools. </p>
<p> Default: <i>delete group script</i><i> = </i><i></i><i> </i></dl>
<p> deleteprinter command (G) </p>
<dl>
<dd>With the introduction of MS-RPC based printer support for Windows NT/2000 clients in Samba 2.2, it is now possible to delete a printer at run time by issuing the DeletePrinter() RPC call. </p>
<p> For a Samba host this means that the printer must be physically deleted from the underlying printing system. The m[blue]<code>deleteprinter command</code>m[] defines a script to be run which will perform the necessary operations for removing the printer from the print system and from smb.conf. </p>
<p> The m[blue]<code>deleteprinter command</code>m[] is automatically called with only one parameter: m[blue]<code>printer name</code>m[]. </p>
<p> Once the m[blue]<code>deleteprinter command</code>m[] has been executed, smbd will reparse the smb.conf to check that the associated printer no longer exists. If the sharename is still valid, then smbd will return an ACCESS_DENIED error to the client. </p>
<p> Default: <i>deleteprinter command</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>deleteprinter command</i><i> = </i><i>/usr/bin/removeprinter</i><i> </i></dl>
<p> delete readonly (S) </p>
<dl>
<dd>This parameter allows readonly files to be deleted. This is not normal DOS semantics, but is allowed by UNIX. </p>
<p> This option may be useful for running applications such as rcs, where UNIX file ownership prevents changing file permissions, and DOS semantics prevent deletion of a read only file. </p>
<p> Default: <i>delete readonly</i><i> = </i><i>no</i><i> </i></dl>
<p> delete share command (G) </p>
<dl>
<dd>Samba 2.2.0 introduced the ability to dynamically add and delete shares via the Windows NT 4.0 Server Manager. The <i>delete share command</i> is used to define an external program or script which will remove an existing service definition from smb.conf. </p>
<p> In order to successfully execute the <i>delete share command</i>, smbd requires that the administrator connects using a root account (i.e. uid == 0) or has the SeDiskOperatorPrivilege. Scripts defined in the <i>delete share command</i> parameter are executed as root. </p>
<p> When executed, smbd will automatically invoke the <i>delete share command</i> with two parameters.</p>
<dl>
<dd>
<dl>
<dd>&bull; <i>configFile</i> &#8211; the location of the global smb.conf file.</dl>
<dl>
<dd>&bull; <i>shareName</i> &#8211; the name of the existing service.</dl>
</dl>
<p> This parameter is only used to remove file shares. To delete printer shares, see the m[blue]<code>deleteprinter command</code>m[]. </p>
<p> Default: <i>delete share command</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>delete share command</i><i> = </i><i>/usr/local/bin/delshare</i><i> </i></dl>
<p> delete user from group script (G) </p>
<dl>
<dd>Full path to the script that will be called when a user is removed from a group using the Windows NT domain administration tools. It will be run by <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) <i>AS ROOT</i>. Any <i>%g</i> will be replaced with the group name and any <i>%u</i> will be replaced with the user name. </p>
<p> Default: <i>delete user from group script</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>delete user from group script</i><i> = </i><i>/usr/sbin/deluser %u %g</i><i> </i></dl>
<p> delete user script (G) </p>
<dl>
<dd>This is the full pathname to a script that will be run by <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) when managing users with remote RPC (NT) tools. </p>
<p> This script is called when a remote client removes a user from the server, normally using &#8216;User Manager for Domains&#8217; or rpcclient. </p>
<p> This script should delete the given UNIX username. </p>
<p> Default: <i>delete user script</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>delete user script</i><i> = </i><i>/usr/local/samba/bin/del_user %u</i><i> </i></dl>
<p> delete veto files (S) </p>
<dl>
<dd>This option is used when Samba is attempting to delete a directory that contains one or more vetoed directories (see the m[blue]<code>veto files</code>m[] option). If this option is set to <code>no</code> (the default) then if a vetoed directory contains any non-vetoed files or directories then the directory delete will fail. This is usually what you want. </p>
<p> If this option is set to <code>yes</code>, then Samba will attempt to recursively delete any files and directories within the vetoed directory. This can be useful for integration with file serving systems such as NetAtalk which create meta-files within directories you might normally veto DOS/Windows users from seeing (e.g. .AppleDouble) </p>
<p> Setting m[blue]<code>delete veto files = yes</code>m[] allows these directories to be transparently deleted when the parent directory is deleted (so long as the user has permissions to do so). </p>
<p> Default: <i>delete veto files</i><i> = </i><i>no</i><i> </i></dl>
<p> dfree cache time (S) </p>
<dl>
<dd>The <i>dfree cache time</i> should only be used on systems where a problem occurs with the internal disk space calculations. This has been known to happen with Ultrix, but may occur with other operating systems. The symptom that was seen was an error of &quot;Abort Retry Ignore&quot; at the end of each directory listing. </p>
<p> This is a new parameter introduced in Samba version 3.0.21. It specifies in seconds the time that smbd will cache the output of a disk free query. If set to zero (the default) no caching is done. This allows a heavily loaded server to prevent rapid spawning of m[blue]<code>dfree command</code>m[] scripts increasing the load. </p>
<p> By default this parameter is zero, meaning no caching will be done. </p>
<p> <i>No default</i> </p>
<p> Example: <i>dfree cache time</i><i> = </i><i>60</i><i> </i></dl>
<p> dfree command (S) </p>
<dl>
<dd>The <i>dfree command</i> setting should only be used on systems where a problem occurs with the internal disk space calculations. This has been known to happen with Ultrix, but may occur with other operating systems. The symptom that was seen was an error of &quot;Abort Retry Ignore&quot; at the end of each directory listing. </p>
<p> This setting allows the replacement of the internal routines to calculate the total disk space and amount available with an external routine. The example below gives a possible script that might fulfill this function. </p>
<p> In Samba version 3.0.21 this parameter has been changed to be a per-share parameter, and in addition the parameter m[blue]<code>dfree cache time</code>m[] was added to allow the output of this script to be cached for systems under heavy load. </p>
<p> The external program will be passed a single parameter indicating a directory in the filesystem being queried. This will typically consist of the string ./. The script should return two integers in ASCII. The first should be the total disk space in blocks, and the second should be the number of available blocks. An optional third return value can give the block size in bytes. The default blocksize is 1024 bytes. </p>
<p> Note: Your script should <i>NOT</i> be setuid or setgid and should be owned by (and writeable only by) root! </p>
<p> Where the script dfree (which must be made executable) could be: </p>
<dl>
<dd>
<pre>#!/bin/sh
df &quot;$1&quot; | tail -1 | awk '{print $(NF-4),$(NF-2)}'</pre>
</dl>
<p> or perhaps (on Sys V based systems): </p>
<dl>
<dd>
<pre>#!/bin/sh
/usr/bin/df -k &quot;$1&quot; | tail -1 | awk '{print $3&quot; &quot;$5}'</pre>
</dl>
<p> Note that you may have to replace the command names with full path names on some systems. Also note the arguments passed into the script should be quoted inside the script in case they contain special characters such as spaces or newlines. </p>
<p> By default internal routines for determining the disk capacity and remaining space will be used. </p>
<p> <i>No default</i> </p>
<p> Example: <i>dfree command</i><i> = </i><i>/usr/local/samba/bin/dfree</i><i> </i></dl>
<p> dgram port (G) </p>
<dl>
<dd>Specifies which ports the server should listen on for NetBIOS datagram traffic. </p>
<p> Default: <i>dgram port</i><i> = </i><i>138</i><i> </i></dl>
<p> directory mode </p>
<dl>
<dd>This parameter is a synonym for directory mask.</dl>
<p> directory mask (S) </p>
<dl>
<dd>This parameter is the octal modes which are used when converting DOS modes to UNIX modes when creating UNIX directories. </p>
<p> When a directory is created, the necessary permissions are calculated according to the mapping from DOS modes to UNIX permissions, and the resulting UNIX mode is then bit-wise &#8216;AND&#8217;ed with this parameter. This parameter may be thought of as a bit-wise MASK for the UNIX modes of a directory. Any bit <i>not</i> set here will be removed from the modes set on a directory when it is created. </p>
<p> The default value of this parameter removes the &#8216;group&#8217; and &#8216;other&#8217; write bits from the UNIX mode, allowing only the user who owns the directory to modify it. </p>
<p> Following this Samba will bit-wise &#8216;OR&#8217; the UNIX mode created from this parameter with the value of the m[blue]<code>force directory mode</code>m[] parameter. This parameter is set to 000 by default (i.e. no extra mode bits are added). </p>
<p> Default: <i>directory mask</i><i> = </i><i>0755</i><i> </i> </p>
<p> Example: <i>directory mask</i><i> = </i><i>0775</i><i> </i></dl>
<p> directory name cache size (S) </p>
<dl>
<dd>This parameter specifies the size of the directory name cache for SMB1 connections. It is not used for SMB2. It will be needed to turn this off for *BSD systems. </p>
<p> Default: <i>directory name cache size</i><i> = </i><i>100</i><i> </i></dl>
<p> directory security mask (S) </p>
<dl>
<dd>This parameter has been removed for Samba 4.0.0. </p>
<p> <i>No default</i></dl>
<p> disable netbios (G) </p>
<dl>
<dd>Enabling this parameter will disable netbios support in Samba. Netbios is the only available form of browsing in all windows versions except for 2000 and XP. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 Clients that only support netbios won&#8217;t be able to see your samba server when netbios support is disabled. </p>
</dl>
<p> Default: <i>disable netbios</i><i> = </i><i>no</i><i> </i></dl>
<p> disable spoolss (G) </p>
<dl>
<dd>Enabling this parameter will disable Samba&#8217;s support for the SPOOLSS set of MS-RPC&#8217;s and will yield identical behavior as Samba 2.0.x. Windows NT/2000 clients will downgrade to using Lanman style printing commands. Windows 9x/ME will be unaffected by the parameter. However, this will also disable the ability to upload printer drivers to a Samba server via the Windows NT Add Printer Wizard or by using the NT printer properties dialog window. It will also disable the capability of Windows NT/2000 clients to download print drivers from the Samba host upon demand. <i>Be very careful about enabling this parameter.</i> </p>
<p> Default: <i>disable spoolss</i><i> = </i><i>no</i><i> </i></dl>
<p> dmapi support (S) </p>
<dl>
<dd>This parameter specifies whether Samba should use DMAPI to determine whether a file is offline or not. This would typically be used in conjunction with a hierarchical storage system that automatically migrates files to tape. </p>
<p> Note that Samba infers the status of a file by examining the events that a DMAPI application has registered interest in. This heuristic is satisfactory for a number of hierarchical storage systems, but there may be system for which it will fail. In this case, Samba may erroneously report files to be offline. </p>
<p> This parameter is only available if a supported DMAPI implementation was found at compilation time. It will only be used if DMAPI is found to enabled on the system at run time. </p>
<p> Default: <i>dmapi support</i><i> = </i><i>no</i><i> </i></dl>
<p> dns forwarder (G) </p>
<dl>
<dd>This option specifies the list of DNS servers that DNS requests will be forwarded to if they can not be handled by Samba itself. </p>
<p> The DNS forwarder is only used if the internal DNS server in Samba is used. </p>
<p> Default: <i>dns forwarder</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>dns forwarder</i><i> = </i><i>192.168.0.1 192.168.0.2</i><i> </i></dl>
<p> dns proxy (G) </p>
<dl>
<dd>Specifies that <code><a href="/docs/linux/man/8-nmbd/">nmbd</a></code>(8) when acting as a WINS server and finding that a NetBIOS name has not been registered, should treat the NetBIOS name word-for-word as a DNS name and do a lookup with the DNS server for that name on behalf of the name-querying client. </p>
<p> Note that the maximum length for a NetBIOS name is 15 characters, so the DNS name (or DNS alias) can likewise only be 15 characters, maximum. </p>
<p> nmbd spawns a second copy of itself to do the DNS name lookup requests, as doing a name lookup is a blocking action. </p>
<p> Default: <i>dns proxy</i><i> = </i><i>yes</i><i> </i></dl>
<p> dns update command (G) </p>
<dl>
<dd>This option sets the command that is called when there are DNS updates. It should update the local machines DNS names using TSIG-GSS. </p>
<p> Default: <i>dns update command</i><i> = </i><i>/build/samba-1K9o3x/samba-4.11.6+dfsg/source4/scripting/bin/samba_dnsupdate</i><i> </i> </p>
<p> Example: <i>dns update command</i><i> = </i><i>/usr/local/sbin/dnsupdate</i><i> </i></dl>
<p> dns zone scavenging (G) </p>
<dl>
<dd>When enabled (the default is disabled) unused dynamic dns records are periodically removed. </p>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font><br />
 This option should not be enabled for installations created with versions of samba before 4.9. Doing this will result in the loss of static DNS entries. This is due to a bug in previous versions of samba (BUG 12451) which marked dynamic DNS records as static and static records as dynamic. </p>
</dl>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 If one record for a DNS name is static (non-aging) then no other record for that DNS name will be scavenged. </p>
</dl>
<p> Default: <i>dns zone scavenging</i><i> = </i><i>no</i><i> </i></dl>
<p> domain logons (G) </p>
<dl>
<dd>If set to <code>yes</code>, the Samba server will provide the netlogon service for Windows 9X network logons for the m[blue]<code>workgroup</code>m[] it is in. This will also cause the Samba server to act as a domain controller for NT4 style domain services. For more details on setting up this feature see the Domain Control chapter of the Samba HOWTO Collection. </p>
<p> Default: <i>domain logons</i><i> = </i><i>no</i><i> </i></dl>
<p> domain master (G) </p>
<dl>
<dd>Tell <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) to enable WAN-wide browse list collation. Setting this option causes nmbd to claim a special domain specific NetBIOS name that identifies it as a domain master browser for its given m[blue]<code>workgroup</code>m[]. Local master browsers in the same m[blue]<code>workgroup</code>m[] on broadcast-isolated subnets will give this nmbd their local browse lists, and then ask <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) for a complete copy of the browse list for the whole wide area network. Browser clients will then contact their local master browser, and will receive the domain-wide browse list, instead of just the list for their broadcast-isolated subnet. </p>
<p> Note that Windows NT Primary Domain Controllers expect to be able to claim this m[blue]<code>workgroup</code>m[] specific special NetBIOS name that identifies them as domain master browsers for that m[blue]<code>workgroup</code>m[] by default (i.e. there is no way to prevent a Windows NT PDC from attempting to do this). This means that if this parameter is set and nmbd claims the special name for a m[blue]<code>workgroup</code>m[] before a Windows NT PDC is able to do so then cross subnet browsing will behave strangely and may fail. </p>
<p> If m[blue]<code>domain logons = yes</code>m[], then the default behavior is to enable the m[blue]<code>domain master</code>m[] parameter. If m[blue]<code>domain logons</code>m[] is not enabled (the default setting), then neither will m[blue]<code>domain master</code>m[] be enabled by default. </p>
<p> When m[blue]<code>domain logons = Yes</code>m[] the default setting for this parameter is Yes, with the result that Samba will be a PDC. If m[blue]<code>domain master = No</code>m[], Samba will function as a BDC. In general, this parameter should be set to &#8216;No&#8217; only on a BDC. </p>
<p> Default: <i>domain master</i><i> = </i><i>auto</i><i> </i></dl>
<p> dont descend (S) </p>
<dl>
<dd>There are certain directories on some systems (e.g., the /proc tree under Linux) that are either not of interest to clients or are infinitely deep (recursive). This parameter allows you to specify a comma-delimited list of directories that the server should always show as empty. </p>
<p> Note that Samba can be very fussy about the exact format of the &quot;dont descend&quot; entries. For example you may need ./proc instead of just /proc. Experimentation is the best policy :-) </p>
<p> Default: <i>dont descend</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>dont descend</i><i> = </i><i>/proc,/dev</i><i> </i></dl>
<p> dos charset (G) </p>
<dl>
<dd>DOS SMB clients assume the server has the same charset as they do. This option specifies which charset Samba should talk to DOS clients. </p>
<p> The default depends on which charsets you have installed. Samba tries to use charset 850 but falls back to ASCII in case it is not available. Run <code><a href="/docs/linux/man/1-testparm/">testparm</a></code>(1) to check the default on your system. </p>
<p> <i>No default</i></dl>
<p> dos filemode (S) </p>
<dl>
<dd>The default behavior in Samba is to provide UNIX-like behavior where only the owner of a file/directory is able to change the permissions on it. However, this behavior is often confusing to DOS/Windows users. Enabling this parameter allows a user who has write access to the file (by whatever means, including an ACL permission) to modify the permissions (including ACL) on it. Note that a user belonging to the group owning the file will not be allowed to change permissions if the group is only granted read access. Ownership of the file/directory may also be changed. Note that using the VFS modules acl_xattr or acl_tdb which store native Windows as meta-data will automatically turn this option on for any share for which they are loaded, as they require this option to emulate Windows ACLs correctly. </p>
<p> Default: <i>dos filemode</i><i> = </i><i>no</i><i> </i></dl>
<p> dos filetime resolution (S) </p>
<dl>
<dd>Under the DOS and Windows FAT filesystem, the finest granularity on time resolution is two seconds. Setting this parameter for a share causes Samba to round the reported time down to the nearest two second boundary when a query call that requires one second resolution is made to <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8). </p>
<p> This option is mainly used as a compatibility option for Visual C++ when used against Samba shares. If oplocks are enabled on a share, Visual C++ uses two different time reading calls to check if a file has changed since it was last read. One of these calls uses a one-second granularity, the other uses a two second granularity. As the two second call rounds any odd second down, then if the file has a timestamp of an odd number of seconds then the two timestamps will not match and Visual C++ will keep reporting the file has changed. Setting this option causes the two timestamps to match, and Visual C++ is happy. </p>
<p> Default: <i>dos filetime resolution</i><i> = </i><i>no</i><i> </i></dl>
<p> dos filetimes (S) </p>
<dl>
<dd>Under DOS and Windows, if a user can write to a file they can change the timestamp on it. Under POSIX semantics, only the owner of the file or root may change the timestamp. By default, Samba emulates the DOS semantics and allows one to change the timestamp on a file if the user smbd is acting on behalf has write permissions. Due to changes in Microsoft Office 2000 and beyond, the default for this parameter has been changed from &quot;no&quot; to &quot;yes&quot; in Samba 3.0.14 and above. Microsoft Excel will display dialog box warnings about the file being changed by another user if this parameter is not set to &quot;yes&quot; and files are being shared between users. </p>
<p> Default: <i>dos filetimes</i><i> = </i><i>yes</i><i> </i></dl>
<p> dsdb event notification (G) </p>
<dl>
<dd>When enabled, this option causes Samba (acting as an Active Directory Domain Controller) to stream Samba database events across the internal message bus. Scripts built using Samba&#8217;s python bindings can listen to these events by registering as the service dsdb_event. </p>
<p> This should be considered a developer option (it assists in the Samba testsuite) rather than a facility for external auditing, as message delivery is not guaranteed (a feature that the testsuite works around). </p>
<p> The Samba database events are also logged via the normal logging methods when the m[blue]<code>log level</code>m[] is set appropriately. </p>
<p> Default: <i>dsdb event notification</i><i> = </i><i>no</i><i> </i></dl>
<p> dsdb group change notification (G) </p>
<dl>
<dd>When enabled, this option causes Samba (acting as an Active Directory Domain Controller) to stream group membership change events across the internal message bus. Scripts built using Samba&#8217;s python bindings can listen to these events by registering as the service dsdb_group_event. </p>
<p> This should be considered a developer option (it assists in the Samba testsuite) rather than a facility for external auditing, as message delivery is not guaranteed (a feature that the testsuite works around). </p>
<p> The group events are also logged via the normal logging methods when the m[blue]<code>log level</code>m[] is set appropriately. </p>
<p> Default: <i>dsdb group change notification</i><i> = </i><i>no</i><i> </i></dl>
<p> dsdb password event notification (G) </p>
<dl>
<dd>When enabled, this option causes Samba (acting as an Active Directory Domain Controller) to stream password change and reset events across the internal message bus. Scripts built using Samba&#8217;s python bindings can listen to these events by registering as the service password_event. </p>
<p> This should be considered a developer option (it assists in the Samba testsuite) rather than a facility for external auditing, as message delivery is not guaranteed (a feature that the testsuite works around). </p>
<p> The password events are also logged via the normal logging methods when the m[blue]<code>log level</code>m[] is set appropriately. </p>
<p> Default: <i>dsdb password event notification</i><i> = </i><i>no</i><i> </i></dl>
<p> durable handles (S) </p>
<dl>
<dd>This boolean parameter controls whether Samba can grant SMB2 durable file handles on a share. </p>
<p> Note that durable handles are only enabled if m[blue]<code>kernel oplocks = no</code>m[], m[blue]<code>kernel share modes = no</code>m[], and m[blue]<code>posix locking = no</code>m[], i.e. if the share is configured for CIFS/SMB2 only access, not supporting interoperability features with local UNIX processes or NFS operations. </p>
<p> Also note that, for the time being, durability is not granted for a handle that has the delete on close flag set. </p>
<p> Default: <i>durable handles</i><i> = </i><i>yes</i><i> </i></dl>
<p> ea support (S) </p>
<dl>
<dd>This boolean parameter controls whether <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) will allow clients to attempt to access extended attributes on a share. In order to enable this parameter on a setup with default VFS modules:</p>
<dl>
<dd>
<dl>
<dd>&bull; Samba must have been built with extended attributes support.</dl>
<dl>
<dd>&bull; The underlying filesystem exposed by the share must support extended attributes (e.g. the <a href="/docs/linux/man/1-getfattr/">getfattr</a>(1) / <a href="/docs/linux/man/1-setfattr/">setfattr</a>(1) utilities must work).</dl>
</dl>
<p> Note that the SMB protocol allows setting attributes whose value is 64K bytes long, and that on NTFS, the maximum storage space for extended attributes per file is 64K. On most UNIX systems (Solaris and ZFS file system being the exception), the limits are much lower &#8211; typically 4K. Worse, the same 4K space is often used to store system metadata such as POSIX ACLs, or Samba&#8217;s NT ACLs. Giving clients access to this tight space via extended attribute support could consume all of it by unsuspecting client applications, which would prevent changing system metadata due to lack of space. The default has changed to yes in Samba release 4.9.0 and above to allow better Windows fileserver compatibility in a default install. </p>
<p> Default: <i>ea support</i><i> = </i><i>yes</i><i> </i></dl>
<p> enable asu support (G) </p>
<dl>
<dd>Hosts running the &quot;Advanced Server for Unix (ASU)&quot; product require some special accomodations such as creating a builtin [ADMIN$] share that only supports IPC connections. The has been the default behavior in smbd for many years. However, certain Microsoft applications such as the Print Migrator tool require that the remote server support an [ADMIN$] file share. Disabling this parameter allows for creating an [ADMIN$] file share in smb.conf. </p>
<p> Default: <i>enable asu support</i><i> = </i><i>no</i><i> </i></dl>
<p> enable core files (G) </p>
<dl>
<dd>This parameter specifies whether core dumps should be written on internal exits. Normally set to <code>yes</code>. You should never need to change this. </p>
<p> Default: <i>enable core files</i><i> = </i><i>yes</i><i> </i> </p>
<p> Example: <i>enable core files</i><i> = </i><i>no</i><i> </i></dl>
<p> enable privileges (G) </p>
<dl>
<dd>This deprecated parameter controls whether or not smbd will honor privileges assigned to specific SIDs via either net rpc rights or one of the Windows user and group manager tools. This parameter is enabled by default. It can be disabled to prevent members of the Domain Admins group from being able to assign privileges to users or groups which can then result in certain smbd operations running as root that would normally run under the context of the connected user. </p>
<p> An example of how privileges can be used is to assign the right to join clients to a Samba controlled domain without providing root access to the server via smbd. </p>
<p> Please read the extended description provided in the Samba HOWTO documentation. </p>
<p> Default: <i>enable privileges</i><i> = </i><i>yes</i><i> </i></dl>
<p> enable spoolss (G) </p>
<dl>
<dd>Inverted synonym for m[blue]<code>disable spoolss</code>m[]. </p>
<p> Default: <i>enable spoolss</i><i> = </i><i>yes</i><i> </i></dl>
<p> encrypt passwords (G) </p>
<dl>
<dd>This parameter has been deprecated since Samba 4.11 and support for plaintext (as distinct from NTLM, NTLMv2 or Kerberos authentication) will be removed in a future Samba release. </p>
<p> That is, in the future, the current default of encrypt passwords = yes will be the enforced behaviour. </p>
<p> This boolean controls whether encrypted passwords will be negotiated with the client. Note that Windows NT 4.0 SP3 and above and also Windows 98 will by default expect encrypted passwords unless a registry entry is changed. To use encrypted passwords in Samba see the chapter &quot;User Database&quot; in the Samba HOWTO Collection. </p>
<p> MS Windows clients that expect Microsoft encrypted passwords and that do not have plain text password support enabled will be able to connect only to a Samba server that has encrypted password support enabled and for which the user accounts have a valid encrypted password. Refer to the smbpasswd command man page for information regarding the creation of encrypted passwords for user accounts. </p>
<p> The use of plain text passwords is NOT advised as support for this feature is no longer maintained in Microsoft Windows products. If you want to use plain text passwords you must set this parameter to no. </p>
<p> In order for encrypted passwords to work correctly <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) must either have access to a local <code><a href="/docs/linux/man/5-smbpasswd/">smbpasswd</a></code>(5) file (see the <code><a href="/docs/linux/man/8-smbpasswd/">smbpasswd</a></code>(8) program for information on how to set up and maintain this file), or set the m[blue]<code>security = [domain|ads]</code>m[] parameter which causes smbd to authenticate against another server. </p>
<p> Default: <i>encrypt passwords</i><i> = </i><i>yes</i><i> </i></dl>
<p> enhanced browsing (G) </p>
<dl>
<dd>This option enables a couple of enhancements to cross-subnet browse propagation that have been added in Samba but which are not standard in Microsoft implementations. </p>
<p> The first enhancement to browse propagation consists of a regular wildcard query to a Samba WINS server for all Domain Master Browsers, followed by a browse synchronization with each of the returned DMBs. The second enhancement consists of a regular randomised browse synchronization with all currently known DMBs. </p>
<p> You may wish to disable this option if you have a problem with empty workgroups not disappearing from browse lists. Due to the restrictions of the browse protocols, these enhancements can cause a empty workgroup to stay around forever which can be annoying. </p>
<p> In general you should leave this option enabled as it makes cross-subnet browse propagation much more reliable. </p>
<p> Default: <i>enhanced browsing</i><i> = </i><i>yes</i><i> </i></dl>
<p> enumports command (G) </p>
<dl>
<dd>The concept of a &quot;port&quot; is fairly foreign to UNIX hosts. Under Windows NT/2000 print servers, a port is associated with a port monitor and generally takes the form of a local port (i.e. LPT1:, COM1:, FILE:) or a remote port (i.e. LPD Port Monitor, etc&#8230;). By default, Samba has only one port defined&#8211;<code>&quot;Samba Printer Port&quot;</code>. Under Windows NT/2000, all printers must have a valid port name. If you wish to have a list of ports displayed (smbd does not use a port name for anything) other than the default <code>&quot;Samba Printer Port&quot;</code>, you can define <i>enumports command</i> to point to a program which should generate a list of ports, one per line, to standard output. This listing will then be used in response to the level 1 and 2 EnumPorts() RPC. </p>
<p> Default: <i>enumports command</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>enumports command</i><i> = </i><i>/usr/bin/listports</i><i> </i></dl>
<p> eventlog list (G) </p>
<dl>
<dd>This option defines a list of log names that Samba will report to the Microsoft EventViewer utility. The listed eventlogs will be associated with tdb file on disk in the $(statedir)/eventlog. </p>
<p> The administrator must use an external process to parse the normal Unix logs such as /var/log/messages and write then entries to the eventlog tdb files. Refer to the <a href="/docs/linux/man/8-eventlogadm/">eventlogadm</a>(8) utility for how to write eventlog entries. </p>
<p> Default: <i>eventlog list</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>eventlog list</i><i> = </i><i>Security Application Syslog Apache</i><i> </i></dl>
<p> fake directory create times (S) </p>
<dl>
<dd>NTFS and Windows VFAT file systems keep a create time for all files and directories. This is not the same as the ctime &#8211; status change time &#8211; that Unix keeps, so Samba by default reports the earliest of the various times Unix does keep. Setting this parameter for a share causes Samba to always report midnight 1-1-1980 as the create time for directories. </p>
<p> This option is mainly used as a compatibility option for Visual C++ when used against Samba shares. Visual C++ generated makefiles have the object directory as a dependency for each object file, and a make rule to create the directory. Also, when NMAKE compares timestamps it uses the creation time when examining a directory. Thus the object directory will be created if it does not exist, but once it does exist it will always have an earlier timestamp than the object files it contains. </p>
<p> However, Unix time semantics mean that the create time reported by Samba will be updated whenever a file is created or deleted in the directory. NMAKE finds all object files in the object directory. The timestamp of the last one built is then compared to the timestamp of the object directory. If the directory&#8217;s timestamp if newer, then all object files will be rebuilt. Enabling this option ensures directories always predate their contents and an NMAKE build will proceed as expected. </p>
<p> Default: <i>fake directory create times</i><i> = </i><i>no</i><i> </i></dl>
<p> fake oplocks (S) </p>
<dl>
<dd>Oplocks are the way that SMB clients get permission from a server to locally cache file operations. If a server grants an oplock (opportunistic lock) then the client is free to assume that it is the only one accessing the file and it will aggressively cache file data. With some oplock types the client may even cache file open/close operations. This can give enormous performance benefits. </p>
<p> When you set fake oplocks = yes, <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) will always grant oplock requests no matter how many clients are using the file. </p>
<p> It is generally much better to use the real m[blue]<code>oplocks</code>m[] support rather than this parameter. </p>
<p> If you enable this option on all read-only shares or shares that you know will only be accessed from one client at a time such as physically read-only media like CDROMs, you will see a big performance improvement on many operations. If you enable this option on shares where multiple clients may be accessing the files read-write at the same time you can get data corruption. Use this option carefully! </p>
<p> Default: <i>fake oplocks</i><i> = </i><i>no</i><i> </i></dl>
<p> follow symlinks (S) </p>
<dl>
<dd>This parameter allows the Samba administrator to stop <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) from following symbolic links in a particular share. Setting this parameter to <code>no</code> prevents any file or directory that is a symbolic link from being followed (the user will get an error). This option is very useful to stop users from adding a symbolic link to /etc/passwd in their home directory for instance. However it will slow filename lookups down slightly. </p>
<p> This option is enabled (i.e. smbd will follow symbolic links) by default. </p>
<p> Default: <i>follow symlinks</i><i> = </i><i>yes</i><i> </i></dl>
<p> force create mode (S) </p>
<dl>
<dd>This parameter specifies a set of UNIX mode bit permissions that will <i>always</i> be set on a file created by Samba. This is done by bitwise &#8216;OR&#8217;ing these bits onto the mode bits of a file that is being created. The default for this parameter is (in octal) 000. The modes in this parameter are bitwise &#8216;OR&#8217;ed onto the file mode after the mask set in the <i>create mask</i> parameter is applied. </p>
<p> The example below would force all newly created files to have read and execute permissions set for &#8216;group&#8217; and &#8216;other&#8217; as well as the read/write/execute bits set for the &#8216;user&#8217;. </p>
<p> Default: <i>force create mode</i><i> = </i><i>0000</i><i> </i> </p>
<p> Example: <i>force create mode</i><i> = </i><i>0755</i><i> </i></dl>
<p> force directory mode (S) </p>
<dl>
<dd>This parameter specifies a set of UNIX mode bit permissions that will <i>always</i> be set on a directory created by Samba. This is done by bitwise &#8216;OR&#8217;ing these bits onto the mode bits of a directory that is being created. The default for this parameter is (in octal) 0000 which will not add any extra permission bits to a created directory. This operation is done after the mode mask in the parameter <i>directory mask</i> is applied. </p>
<p> The example below would force all created directories to have read and execute permissions set for &#8216;group&#8217; and &#8216;other&#8217; as well as the read/write/execute bits set for the &#8216;user&#8217;. </p>
<p> Default: <i>force directory mode</i><i> = </i><i>0000</i><i> </i> </p>
<p> Example: <i>force directory mode</i><i> = </i><i>0755</i><i> </i></dl>
<p> force directory security mode (S) </p>
<dl>
<dd>This parameter has been removed for Samba 4.0.0. </p>
<p> <i>No default</i></dl>
<p> group </p>
<dl>
<dd>This parameter is a synonym for force group.</dl>
<p> force group (S) </p>
<dl>
<dd>This specifies a UNIX group name that will be assigned as the default primary group for all users connecting to this service. This is useful for sharing files by ensuring that all access to files on service will use the named group for their permissions checking. Thus, by assigning permissions for this group to the files and directories within this service the Samba administrator can restrict or allow sharing of these files. </p>
<p> In Samba 2.0.5 and above this parameter has extended functionality in the following way. If the group name listed here has a &#8216;+&#8217; character prepended to it then the current user accessing the share only has the primary group default assigned to this group if they are already assigned as a member of that group. This allows an administrator to decide that only users who are already in a particular group will create files with group ownership set to that group. This gives a finer granularity of ownership assignment. For example, the setting force group = +sys means that only users who are already in group sys will have their default primary group assigned to sys when accessing this Samba share. All other users will retain their ordinary primary group. </p>
<p> If the m[blue]<code>force user</code>m[] parameter is also set the group specified in <i>force group</i> will override the primary group set in <i>force user</i>. </p>
<p> Default: <i>force group</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>force group</i><i> = </i><i>agroup</i><i> </i></dl>
<p> force printername (S) </p>
<dl>
<dd>When printing from Windows NT (or later), each printer in smb.conf has two associated names which can be used by the client. The first is the sharename (or shortname) defined in smb.conf. This is the only printername available for use by Windows 9x clients. The second name associated with a printer can be seen when browsing to the &quot;Printers&quot; (or &quot;Printers and Faxes&quot;) folder on the Samba server. This is referred to simply as the printername (not to be confused with the <i>printer name</i> option). </p>
<p> When assigning a new driver to a printer on a remote Windows compatible print server such as Samba, the Windows client will rename the printer to match the driver name just uploaded. This can result in confusion for users when multiple printers are bound to the same driver. To prevent Samba from allowing the printer&#8217;s printername to differ from the sharename defined in smb.conf, set <i>force printername = yes</i>. </p>
<p> Be aware that enabling this parameter may affect migrating printers from a Windows server to Samba since Windows has no way to force the sharename and printername to match. </p>
<p> It is recommended that this parameter&#8217;s value not be changed once the printer is in use by clients as this could cause a user not be able to delete printer connections from their local Printers folder. </p>
<p> Default: <i>force printername</i><i> = </i><i>no</i><i> </i></dl>
<p> force security mode (S) </p>
<dl>
<dd>This parameter has been removed for Samba 4.0.0. </p>
<p> <i>No default</i></dl>
<p> force unknown acl user (S) </p>
<dl>
<dd>If this parameter is set, a Windows NT ACL that contains an unknown SID (security descriptor, or representation of a user or group id) as the owner or group owner of the file will be silently mapped into the current UNIX uid or gid of the currently connected user. </p>
<p> This is designed to allow Windows NT clients to copy files and folders containing ACLs that were created locally on the client machine and contain users local to that machine only (no domain users) to be copied to a Samba server (usually with XCOPY /O) and have the unknown userid and groupid of the file owner map to the current connected user. This can only be fixed correctly when winbindd allows arbitrary mapping from any Windows NT SID to a UNIX uid or gid. </p>
<p> Try using this parameter when XCOPY /O gives an ACCESS_DENIED error. </p>
<p> Default: <i>force unknown acl user</i><i> = </i><i>no</i><i> </i></dl>
<p> force user (S) </p>
<dl>
<dd>This specifies a UNIX user name that will be assigned as the default user for all users connecting to this service. This is useful for sharing files. You should also use it carefully as using it incorrectly can cause security problems. </p>
<p> This user name only gets used once a connection is established. Thus clients still need to connect as a valid user and supply a valid password. Once connected, all file operations will be performed as the &quot;forced user&quot;, no matter what username the client connected as. This can be very useful. </p>
<p> In Samba 2.0.5 and above this parameter also causes the primary group of the forced user to be used as the primary group for all file activity. Prior to 2.0.5 the primary group was left as the primary group of the connecting user (this was a bug). </p>
<p> Default: <i>force user</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>force user</i><i> = </i><i>auser</i><i> </i></dl>
<p> fss: prune stale (G) </p>
<dl>
<dd>When enabled, Samba&#8217;s File Server Remote VSS Protocol (FSRVP) server checks all FSRVP initiated snapshots on startup, and removes any corresponding state (including share definitions) for nonexistent snapshot paths. </p>
<p> Default: <i>fss: prune stale</i><i> = </i><i>no</i><i> </i> </p>
<p> Example: <i>fss: prune stale</i><i> = </i><i>yes</i><i> </i></dl>
<p> fss: sequence timeout (G) </p>
<dl>
<dd>The File Server Remote VSS Protocol (FSRVP) server includes a message sequence timer to ensure cleanup on unexpected client disconnect. This parameter overrides the default timeout between FSRVP operations. FSRVP timeouts can be completely disabled via a value of 0. </p>
<p> Default: <i>fss: sequence timeout</i><i> = </i><i>180 or 1800, depending on operation</i><i> </i> </p>
<p> Example: <i>fss: sequence timeout</i><i> = </i><i>0</i><i> </i></dl>
<p> fstype (S) </p>
<dl>
<dd>This parameter allows the administrator to configure the string that specifies the type of filesystem a share is using that is reported by <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) when a client queries the filesystem type for a share. The default type is <code>NTFS</code> for compatibility with Windows NT but this can be changed to other strings such as <code>Samba</code> or <code>FAT</code> if required. </p>
<p> Default: <i>fstype</i><i> = </i><i>NTFS</i><i> </i> </p>
<p> Example: <i>fstype</i><i> = </i><i>Samba</i><i> </i></dl>
<p> get quota command (G) </p>
<dl>
<dd>The get quota command should only be used whenever there is no operating system API available from the OS that samba can use. </p>
<p> This option is only available Samba was compiled with quotas support. </p>
<p> This parameter should specify the path to a script that queries the quota information for the specified user/group for the partition that the specified directory is on. </p>
<p> Such a script is being given 3 arguments:</p>
<dl>
<dd>
<dl>
<dd>&bull; directory</dl>
<dl>
<dd>&bull; type of query</dl>
<dl>
<dd>&bull; uid of user or gid of group</dl>
</dl>
<p> The directory is actually mostly just &quot;.&quot; &#8211; It needs to be treated relatively to the current working directory that the script can also query. </p>
<p> The type of query can be one of:</p>
<dl>
<dd>
<dl>
<dd>&bull; 1 &#8211; user quotas</dl>
<dl>
<dd>&bull; 2 &#8211; user default quotas (uid = -1)</dl>
<dl>
<dd>&bull; 3 &#8211; group quotas</dl>
<dl>
<dd>&bull; 4 &#8211; group default quotas (gid = -1)</dl>
</dl>
<p> This script should print one line as output with spaces between the columns. The printed columns should be:</p>
<dl>
<dd>
<dl>
<dd>&bull; 1 &#8211; quota flags (0 = no quotas, 1 = quotas enabled, 2 = quotas enabled and enforced)</dl>
<dl>
<dd>&bull; 2 &#8211; number of currently used blocks</dl>
<dl>
<dd>&bull; 3 &#8211; the softlimit number of blocks</dl>
<dl>
<dd>&bull; 4 &#8211; the hardlimit number of blocks</dl>
<dl>
<dd>&bull; 5 &#8211; currently used number of inodes</dl>
<dl>
<dd>&bull; 6 &#8211; the softlimit number of inodes</dl>
<dl>
<dd>&bull; 7 &#8211; the hardlimit number of inodes</dl>
<dl>
<dd>&bull; 8 (optional) &#8211; the number of bytes in a block(default is 1024)</dl>
</dl>
<p> Default: <i>get quota command</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>get quota command</i><i> = </i><i>/usr/local/sbin/query_quota</i><i> </i></dl>
<p> getwd cache (G) </p>
<dl>
<dd>This is a tuning option. When this is enabled a caching algorithm will be used to reduce the time taken for getwd() calls. This can have a significant impact on performance, especially when the m[blue]<code>wide links</code>m[] parameter is set to <code>no</code>. </p>
<p> Default: <i>getwd cache</i><i> = </i><i>yes</i><i> </i></dl>
<p> gpo update command (G) </p>
<dl>
<dd>This option sets the command that is called to apply GPO policies. The samba-gpupdate script applies System Access and Kerberos Policies to the KDC. System Access policies set minPwdAge, maxPwdAge, minPwdLength, and pwdProperties in the samdb. Kerberos Policies set kdc:service ticket lifetime, kdc:user ticket lifetime, and kdc:renewal lifetime in smb.conf. </p>
<p> Default: <i>gpo update command</i><i> = </i><i>/build/samba-1K9o3x/samba-4.11.6+dfsg/source4/scripting/bin/samba-gpupdate</i><i> </i> </p>
<p> Example: <i>gpo update command</i><i> = </i><i>/usr/local/sbin/gpoupdate</i><i> </i></dl>
<p> guest account (G) </p>
<dl>
<dd>This is a username which will be used for access to services which are specified as m[blue]<code>guest ok</code>m[] (see below). Whatever privileges this user has will be available to any client connecting to the guest service. This user must exist in the password file, but does not require a valid login. The user account &quot;ftp&quot; is often a good choice for this parameter. </p>
<p> On some systems the default guest account &quot;nobody&quot; may not be able to print. Use another account in this case. You should test this by trying to log in as your guest user (perhaps by using the su &#8211; command) and trying to print using the system print command such as <a href="/docs/linux/man/1-lpr/">lpr</a>(1) or <a href="/docs/linux/man/1-lp/">lp</a>(1). </p>
<p> This parameter does not accept % macros, because many parts of the system require this value to be constant for correct operation. </p>
<p> Default: <i>guest account</i><i> = </i><i>nobody # default can be changed at compile-time</i><i> </i> </p>
<p> Example: <i>guest account</i><i> = </i><i>ftp</i><i> </i></dl>
<p> public </p>
<dl>
<dd>This parameter is a synonym for guest ok.</dl>
<p> guest ok (S) </p>
<dl>
<dd>If this parameter is <code>yes</code> for a service, then no password is required to connect to the service. Privileges will be those of the m[blue]<code>guest account</code>m[]. </p>
<p> This parameter nullifies the benefits of setting m[blue]<code>restrict anonymous = 2</code>m[] </p>
<p> See the section below on m[blue]<code>security</code>m[] for more information about this option. </p>
<p> Default: <i>guest ok</i><i> = </i><i>no</i><i> </i></dl>
<p> only guest </p>
<dl>
<dd>This parameter is a synonym for guest only.</dl>
<p> guest only (S) </p>
<dl>
<dd>If this parameter is <code>yes</code> for a service, then only guest connections to the service are permitted. This parameter will have no effect if m[blue]<code>guest ok</code>m[] is not set for the service. </p>
<p> See the section below on m[blue]<code>security</code>m[] for more information about this option. </p>
<p> Default: <i>guest only</i><i> = </i><i>no</i><i> </i></dl>
<p> hide dot files (S) </p>
<dl>
<dd>This is a boolean parameter that controls whether files starting with a dot appear as hidden files. </p>
<p> Default: <i>hide dot files</i><i> = </i><i>yes</i><i> </i></dl>
<p> hide files (S) </p>
<dl>
<dd>This is a list of files or directories that are not visible but are accessible. The DOS &#8216;hidden&#8217; attribute is applied to any files or directories that match. </p>
<p> Each entry in the list must be separated by a &#8216;/&#8217;, which allows spaces to be included in the entry. &#8216;*&#8217; and &#8216;?&#8217; can be used to specify multiple files or directories as in DOS wildcards. </p>
<p> Each entry must be a Unix path, not a DOS path and must not include the Unix directory separator &#8216;/&#8217;. </p>
<p> Note that the case sensitivity option is applicable in hiding files. </p>
<p> Setting this parameter will affect the performance of Samba, as it will be forced to check all files and directories for a match as they are scanned. </p>
<p> The example shown above is based on files that the Macintosh SMB client (DAVE) available from Thursby creates for internal use, and also still hides all files beginning with a dot. </p>
<p> An example of us of this parameter is: </p>
<dl>
<dd>
<pre>hide files = /.*/DesktopFolderDB/TrashFor%m/resource.frk/</pre>
</dl>
<p> Default: <i>hide files</i><i> = </i><i> # no file are hidden</i><i> </i></dl>
<p> hide new files timeout (S) </p>
<dl>
<dd>Setting this parameter to something but 0 hides files that have been modified less than N seconds ago. </p>
<p> It can be used for ingest/process queue style workloads. A processing application should only see files that are definitely finished. As many applications do not have proper external workflow control, this can be a way to make sure processing does not interfere with file ingest. </p>
<p> Default: <i>hide new files timeout</i><i> = </i><i>0</i><i> </i></dl>
<p> hide special files (S) </p>
<dl>
<dd>This parameter prevents clients from seeing special files such as sockets, devices and fifo&#8217;s in directory listings. </p>
<p> Default: <i>hide special files</i><i> = </i><i>no</i><i> </i></dl>
<p> hide unreadable (S) </p>
<dl>
<dd>This parameter prevents clients from seeing the existence of files that cannot be read. Defaults to off. </p>
<p> Please note that enabling this can slow down listing large directories significantly. Samba has to evaluate the ACLs of all directory members, which can be a lot of effort. </p>
<p> Default: <i>hide unreadable</i><i> = </i><i>no</i><i> </i></dl>
<p> hide unwriteable files (S) </p>
<dl>
<dd>This parameter prevents clients from seeing the existence of files that cannot be written to. Defaults to off. Note that unwriteable directories are shown as usual. </p>
<p> Please note that enabling this can slow down listing large directories significantly. Samba has to evaluate the ACLs of all directory members, which can be a lot of effort. </p>
<p> Default: <i>hide unwriteable files</i><i> = </i><i>no</i><i> </i></dl>
<p> homedir map (G) </p>
<dl>
<dd>If m[blue]<code>nis homedir</code>m[] is <code>yes</code>, and <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) is also acting as a Win95/98 <i>logon server</i> then this parameter specifies the NIS (or YP) map from which the server for the user&#8217;s home directory should be extracted. At present, only the Sun auto.home map format is understood. The form of the map is: </p>
<dl>
<dd>
<pre>username server:/some/file/system</pre>
</dl>
<p> and the program will extract the servername from before the first &#8216;:&#8217;. There should probably be a better parsing system that copes with different map formats and also Amd (another automounter) maps. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 A working NIS client is required on the system for this option to work. </p>
</dl>
<p> Default: <i>homedir map</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>homedir map</i><i> = </i><i>amd.homedir</i><i> </i></dl>
<p> host msdfs (G) </p>
<dl>
<dd>If set to <code>yes</code>, Samba will act as a Dfs server, and allow Dfs-aware clients to browse Dfs trees hosted on the server. </p>
<p> See also the m[blue]<code>msdfs root</code>m[] share level parameter. For more information on setting up a Dfs tree on Samba, refer to the MSFDS chapter in the book Samba3-HOWTO. </p>
<p> Default: <i>host msdfs</i><i> = </i><i>yes</i><i> </i></dl>
<p> hostname lookups (G) </p>
<dl>
<dd>Specifies whether samba should use (expensive) hostname lookups or use the ip addresses instead. An example place where hostname lookups are currently used is when checking the hosts deny and hosts allow. </p>
<p> Default: <i>hostname lookups</i><i> = </i><i>no</i><i> </i> </p>
<p> Example: <i>hostname lookups</i><i> = </i><i>yes</i><i> </i></dl>
<p> allow hosts </p>
<dl>
<dd>This parameter is a synonym for hosts allow.</dl>
<p> hosts allow (S) </p>
<dl>
<dd>A synonym for this parameter is m[blue]<code>allow hosts</code>m[]. </p>
<p> This parameter is a comma, space, or tab delimited set of hosts which are permitted to access a service. </p>
<p> If specified in the [global] section then it will apply to all services, regardless of whether the individual service has a different setting. </p>
<p> You can specify the hosts by name or IP number. For example, you could restrict access to only the hosts on a Class C subnet with something like allow hosts = 150.203.5.. The full syntax of the list is described in the man page <a href="/docs/linux/man/5-hosts_access/">hosts_access</a>(5). Note that this man page may not be present on your system, so a brief description will be given here also. </p>
<p> Note that the localhost address 127.0.0.1 will always be allowed access unless specifically denied by a m[blue]<code>hosts deny</code>m[] option. </p>
<p> You can also specify hosts by network/netmask pairs and by netgroup names if your system supports netgroups. The <i>EXCEPT</i> keyword can also be used to limit a wildcard list. The following examples may provide some help: </p>
<p> Example 1: allow all IPs in 150.203.*.*; except one </p>
<p> hosts allow = 150.203. EXCEPT 150.203.6.66 </p>
<p> Example 2: allow hosts that match the given network/netmask </p>
<p> hosts allow = 150.203.15.0/255.255.255.0 </p>
<p> Example 3: allow a couple of hosts </p>
<p> hosts allow = lapland, arvidsjaur </p>
<p> Example 4: allow only hosts in NIS netgroup &quot;foonet&quot;, but deny access from one particular host </p>
<p> hosts allow = @foonet </p>
<p> hosts deny = pirate </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 Note that access still requires suitable user-level passwords. </p>
</dl>
<p> See <code><a href="/docs/linux/man/1-testparm/">testparm</a></code>(1) for a way of testing your host access to see if it does what you expect. </p>
<p> Default: <i>hosts allow</i><i> = </i><i> # none (i.e., all hosts permitted access)</i><i> </i> </p>
<p> Example: <i>hosts allow</i><i> = </i><i>150.203.5. myhost.mynet.edu.au</i><i> </i></dl>
<p> deny hosts </p>
<dl>
<dd>This parameter is a synonym for hosts deny.</dl>
<p> hosts deny (S) </p>
<dl>
<dd>The opposite of <i>hosts allow</i> &#8211; hosts listed here are <i>NOT</i> permitted access to services unless the specific services have their own lists to override this one. Where the lists conflict, the <i>allow</i> list takes precedence. </p>
<p> In the event that it is necessary to deny all by default, use the keyword ALL (or the netmask 0.0.0.0/0) and then explicitly specify to the m[blue]<code>hosts allow = hosts allow</code>m[] parameter those hosts that should be permitted access. </p>
<p> Default: <i>hosts deny</i><i> = </i><i> # none (i.e., no hosts specifically excluded)</i><i> </i> </p>
<p> Example: <i>hosts deny</i><i> = </i><i>150.203.4. badhost.mynet.edu.au</i><i> </i></dl>
<p> idmap backend (G) </p>
<dl>
<dd>The idmap backend provides a plugin interface for Winbind to use varying backends to store SID/uid/gid mapping tables. </p>
<p> This option specifies the default backend that is used when no special configuration set, but it is now deprecated in favour of the new spelling m[blue]<code>idmap config * : backend</code>m[]. </p>
<p> Default: <i>idmap backend</i><i> = </i><i>tdb</i><i> </i></dl>
<p> idmap cache time (G) </p>
<dl>
<dd>This parameter specifies the number of seconds that Winbind&#8217;s idmap interface will cache positive SID/uid/gid query results. By default, Samba will cache these results for one week. </p>
<p> Default: <i>idmap cache time</i><i> = </i><i>604800</i><i> </i></dl>
<p> idmap config DOMAIN : OPTION (G) </p>
<dl>
<dd>ID mapping in Samba is the mapping between Windows SIDs and Unix user and group IDs. This is performed by Winbindd with a configurable plugin interface. Samba&#8217;s ID mapping is configured by options starting with the m[blue]<code>idmap config</code>m[] prefix. An idmap option consists of the m[blue]<code>idmap config</code>m[] prefix, followed by a domain name or the asterisk character (*), a colon, and the name of an idmap setting for the chosen domain. </p>
<p> The idmap configuration is hence divided into groups, one group for each domain to be configured, and one group with the asterisk instead of a proper domain name, which specifies the default configuration that is used to catch all domains that do not have an explicit idmap configuration of their own. </p>
<p> There are three general options available: </p>
<p> backend = backend_name</p>
<dl>
<dd>This specifies the name of the idmap plugin to use as the SID/uid/gid backend for this domain. The standard backends are tdb (<code><a href="/docs/linux/man/8-idmap_tdb/">idmap_tdb</a></code>(8)), tdb2 (<code><a href="/docs/linux/man/8-idmap_tdb2/">idmap_tdb2</a></code>(8)), ldap (<code><a href="/docs/linux/man/8-idmap_ldap/">idmap_ldap</a></code>(8)), rid (<code><a href="/docs/linux/man/8-idmap_rid/">idmap_rid</a></code>(8)), hash (<code><a href="/docs/linux/man/8-idmap_hash/">idmap_hash</a></code>(8)), autorid (<code><a href="/docs/linux/man/8-idmap_autorid/">idmap_autorid</a></code>(8)), ad (<code><a href="/docs/linux/man/8-idmap_ad/">idmap_ad</a></code>(8)) and nss (<code><a href="/docs/linux/man/8-idmap_nss/">idmap_nss</a></code>(8)). The corresponding manual pages contain the details, but here is a summary. </p>
<p> The first three of these create mappings of their own using internal unixid counters and store the mappings in a database. These are suitable for use in the default idmap configuration. The rid and hash backends use a pure algorithmic calculation to determine the unixid for a SID. The autorid module is a mixture of the tdb and rid backend. It creates ranges for each domain encountered and then uses the rid algorithm for each of these automatically configured domains individually. The ad backend uses unix ids stored in Active Directory via the standard schema extensions. The nss backend reverses the standard winbindd setup and gets the unix ids via names from nsswitch which can be useful in an ldap setup.</dl>
<p> range = low &#8211; high</p>
<dl>
<dd>Defines the available matching uid and gid range for which the backend is authoritative. For allocating backends, this also defines the start and the end of the range for allocating new unique IDs. </p>
<p> winbind uses this parameter to find the backend that is authoritative for a unix ID to SID mapping, so it must be set for each individually configured domain and for the default configuration. The configured ranges must be mutually disjoint.</dl>
<p> read only = yes|no</p>
<dl>
<dd>This option can be used to turn the writing backends tdb, tdb2, and ldap into read only mode. This can be useful e.g. in cases where a pre-filled database exists that should not be extended automatically.</dl>
<p> The following example illustrates how to configure the <code><a href="/docs/linux/man/8-idmap_ad/">idmap_ad</a></code>(8) backend for the CORP domain and the <code><a href="/docs/linux/man/8-idmap_tdb/">idmap_tdb</a></code>(8) backend for all other domains. This configuration assumes that the admin of CORP assigns unix ids below 1000000 via the SFU extensions, and winbind is supposed to use the next million entries for its own mappings from trusted domains and for local groups for example. </p>
<dl>
<dd>
<pre> idmap config * : backend = tdb
 idmap config * : range = 1000000-1999999
 idmap config CORP : backend = ad
 idmap config CORP : range = 1000-999999</pre>
</dl>
<p> <i>No default</i></dl>
<p> winbind gid </p>
<dl>
<dd>This parameter is a synonym for idmap gid.</dl>
<p> idmap gid (G) </p>
<dl>
<dd>The idmap gid parameter specifies the range of group ids for the default idmap configuration. It is now deprecated in favour of m[blue]<code>idmap config * : range</code>m[]. </p>
<p> See the m[blue]<code>idmap config</code>m[] option. </p>
<p> Default: <i>idmap gid</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>idmap gid</i><i> = </i><i>10000-20000</i><i> </i></dl>
<p> idmap negative cache time (G) </p>
<dl>
<dd>This parameter specifies the number of seconds that Winbind&#8217;s idmap interface will cache negative SID/uid/gid query results. </p>
<p> Default: <i>idmap negative cache time</i><i> = </i><i>120</i><i> </i></dl>
<p> winbind uid </p>
<dl>
<dd>This parameter is a synonym for idmap uid.</dl>
<p> idmap uid (G) </p>
<dl>
<dd>The idmap uid parameter specifies the range of user ids for the default idmap configuration. It is now deprecated in favour of m[blue]<code>idmap config * : range</code>m[]. </p>
<p> See the m[blue]<code>idmap config</code>m[] option. </p>
<p> Default: <i>idmap uid</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>idmap uid</i><i> = </i><i>10000-20000</i><i> </i></dl>
<p> include (S) </p>
<dl>
<dd>This allows you to include one config file inside another. The file is included literally, as though typed in place. </p>
<p> It takes the standard substitutions, except <i>%u</i>, <i>%P</i> and <i>%S</i>. </p>
<p> The parameter <i>include = registry</i> has a special meaning: It does <i>not</i> include a file named <i>registry</i> from the current working directory, but instead reads the global configuration options from the registry. See the section on registry-based configuration for details. Note that this option automatically activates registry shares. </p>
<p> Default: <i>include</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>include</i><i> = </i><i>/usr/local/samba/lib/admin_smb.conf</i><i> </i></dl>
<p> include system krb5 conf (G) </p>
<dl>
<dd>Setting this parameter to no will prevent winbind to include the system /etc/krb5.conf file into the krb5.conf file it creates. See also m[blue]<code>create krb5 conf</code>m[]. This option only applies to Samba built with MIT Kerberos. </p>
<p> Default: <i>include system krb5 conf</i><i> = </i><i>yes</i><i> </i></dl>
<p> inherit acls (S) </p>
<dl>
<dd>This parameter can be used to ensure that if default acls exist on parent directories, they are always honored when creating a new file or subdirectory in these parent directories. The default behavior is to use the unix mode specified when creating the directory. Enabling this option sets the unix mode to 0777, thus guaranteeing that default directory acls are propagated. Note that using the VFS modules acl_xattr or acl_tdb which store native Windows as meta-data will automatically turn this option on for any share for which they are loaded, as they require this option to emulate Windows ACLs correctly. </p>
<p> Default: <i>inherit acls</i><i> = </i><i>no</i><i> </i></dl>
<p> inherit owner (S) </p>
<dl>
<dd>The ownership of new files and directories is normally governed by effective uid of the connected user. This option allows the Samba administrator to specify that the ownership for new files and directories should be controlled by the ownership of the parent directory. </p>
<p> Valid options are:</p>
<dl>
<dd>
<dl>
<dd>&bull; <code>no</code> &#8211; Both the Windows (SID) owner and the UNIX (uid) owner of the file are governed by the identity of the user that created the file.</dl>
<dl>
<dd>&bull; <code>windows and unix</code> &#8211; The Windows (SID) owner and the UNIX (uid) owner of new files and directories are set to the respective owner of the parent directory.</dl>
<dl>
<dd>&bull; <code>yes</code> &#8211; a synonym for <code>windows and unix</code>.</dl>
<dl>
<dd>&bull; <code>unix only</code> &#8211; Only the UNIX owner is set to the UNIX owner of the parent directory.</dl>
</dl>
<p> Common scenarios where this behavior is useful is in implementing drop-boxes, where users can create and edit files but not delete them and ensuring that newly created files in a user&#8217;s roaming profile directory are actually owned by the user. </p>
<p> The <code>unix only</code> option effectively breaks the tie between the Windows owner of a file and the UNIX owner. As a logical consequence, in this mode, setting the the Windows owner of a file does not modify the UNIX owner. Using this mode should typically be combined with a backing store that can emulate the full NT ACL model without affecting the POSIX permissions, such as the acl_xattr VFS module, coupled with m[blue]<code>acl_xattr:ignore system acls = yes</code>m[]. This can be used to emulate folder quotas, when files are exposed only via SMB (without UNIX extensions). The UNIX owner of a directory is locally set and inherited by all subdirectories and files, and they all consume the same quota. </p>
<p> Default: <i>inherit owner</i><i> = </i><i>no</i><i> </i></dl>
<p> inherit permissions (S) </p>
<dl>
<dd>The permissions on new files and directories are normally governed by m[blue]<code>create mask</code>m[], m[blue]<code>directory mask</code>m[], m[blue]<code>force create mode</code>m[] and m[blue]<code>force directory mode</code>m[] but the boolean inherit permissions parameter overrides this. </p>
<p> New directories inherit the mode of the parent directory, including bits such as setgid. </p>
<p> New files inherit their read/write bits from the parent directory. Their execute bits continue to be determined by m[blue]<code>map archive</code>m[], m[blue]<code>map hidden</code>m[] and m[blue]<code>map system</code>m[] as usual. </p>
<p> Note that the setuid bit is <i>never</i> set via inheritance (the code explicitly prohibits this). </p>
<p> This can be particularly useful on large systems with many users, perhaps several thousand, to allow a single [homes] share to be used flexibly by each user. </p>
<p> Default: <i>inherit permissions</i><i> = </i><i>no</i><i> </i></dl>
<p> init logon delay (G) </p>
<dl>
<dd>This parameter specifies a delay in milliseconds for the hosts configured for delayed initial samlogon with m[blue]<code>init logon delayed hosts</code>m[]. </p>
<p> Default: <i>init logon delay</i><i> = </i><i>100</i><i> </i></dl>
<p> init logon delayed hosts (G) </p>
<dl>
<dd>This parameter takes a list of host names, addresses or networks for which the initial samlogon reply should be delayed (so other DCs get preferred by XP workstations if there are any). </p>
<p> The length of the delay can be specified with the m[blue]<code>init logon delay</code>m[] parameter. </p>
<p> Default: <i>init logon delayed hosts</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>init logon delayed hosts</i><i> = </i><i>150.203.5. myhost.mynet.de</i><i> </i></dl>
<p> interfaces (G) </p>
<dl>
<dd>This option allows you to override the default network interfaces list that Samba will use for browsing, name registration and other NetBIOS over TCP/IP (NBT) traffic. By default Samba will query the kernel for the list of all active interfaces and use any interfaces except 127.0.0.1 that are broadcast capable. </p>
<p> The option takes a list of interface strings. Each string can be in any of the following forms:</p>
<dl>
<dd>
<dl>
<dd>&bull; a network interface name (such as eth0). This may include shell-like wildcards so eth* will match any interface starting with the substring &quot;eth&quot;</dl>
<dl>
<dd>&bull; an IP address. In this case the netmask is determined from the list of interfaces obtained from the kernel</dl>
<dl>
<dd>&bull; an IP/mask pair.</dl>
<dl>
<dd>&bull; a broadcast/mask pair.</dl>
</dl>
<p> The &quot;mask&quot; parameters can either be a bit length (such as 24 for a C class network) or a full netmask in dotted decimal form. </p>
<p> The &quot;IP&quot; parameters above can either be a full dotted decimal IP address or a hostname which will be looked up via the OS&#8217;s normal hostname resolution mechanisms. </p>
<p> By default Samba enables all active interfaces that are broadcast capable except the loopback adaptor (IP address 127.0.0.1). </p>
<p> In order to support SMB3 multi-channel configurations, smbd understands some extra data that can be appended after the actual interface with this extended syntax: </p>
<p> interface[;key1=value1[,key2=value2[&#8230;]]] </p>
<p> Known keys are speed, capability, and if_index. Speed is specified in bits per second. Known capabilities are RSS and RDMA. The if_index should be used with care: the values must not coincide with indexes used by the kernel. Note that these options are mainly intended for testing and development rather than for production use. At least on Linux systems, these values should be auto-detected, but the settings can serve as last a resort when autodetection is not working or is not available. </p>
<p> The example below configures three network interfaces corresponding to the eth0 device and IP addresses 192.168.2.10 and 192.168.3.10. The netmasks of the latter two interfaces would be set to 255.255.255.0. </p>
<p> Default: <i>interfaces</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>interfaces</i><i> = </i><i>eth0 192.168.2.10/24 192.168.3.10/255.255.255.0</i><i> </i></dl>
<p> invalid users (S) </p>
<dl>
<dd>This is a list of users that should not be allowed to login to this service. This is really a <i>paranoid</i> check to absolutely ensure an improper setting does not breach your security. </p>
<p> A name starting with a &#8216;@&#8217; is interpreted as an NIS netgroup first (if your system supports NIS), and then as a UNIX group if the name was not found in the NIS netgroup database. </p>
<p> A name starting with &#8216;+&#8217; is interpreted only by looking in the UNIX group database via the NSS getgrnam() interface. A name starting with &#8216;&amp;&#8217; is interpreted only by looking in the NIS netgroup database (this requires NIS to be working on your system). The characters &#8216;+&#8217; and &#8216;&amp;&#8217; may be used at the start of the name in either order so the value <i>+&amp;group</i> means check the UNIX group database, followed by the NIS netgroup database, and the value <i>&amp;+group</i> means check the NIS netgroup database, followed by the UNIX group database (the same as the &#8216;@&#8217; prefix). </p>
<p> The current servicename is substituted for <i>%S</i>. This is useful in the [homes] section. </p>
<p> Default: <i>invalid users</i><i> = </i><i> # no invalid users</i><i> </i> </p>
<p> Example: <i>invalid users</i><i> = </i><i>root fred admin @wheel</i><i> </i></dl>
<p> iprint server (G) </p>
<dl>
<dd>This parameter is only applicable if m[blue]<code>printing</code>m[] is set to <code>iprint</code>. </p>
<p> If set, this option overrides the ServerName option in the CUPS client.conf. This is necessary if you have virtual samba servers that connect to different CUPS daemons. </p>
<p> Default: <i>iprint server</i><i> = </i><i>&quot;&quot;</i><i> </i> </p>
<p> Example: <i>iprint server</i><i> = </i><i>MYCUPSSERVER</i><i> </i></dl>
<p> keepalive (G) </p>
<dl>
<dd>The value of the parameter (an integer) represents the number of seconds between <i>keepalive</i> packets. If this parameter is zero, no keepalive packets will be sent. Keepalive packets, if sent, allow the server to tell whether a client is still present and responding. </p>
<p> Keepalives should, in general, not be needed if the socket has the SO_KEEPALIVE attribute set on it by default. (see m[blue]<code>socket options</code>m[]). Basically you should only use this option if you strike difficulties. </p>
<p> Please note this option only applies to SMB1 client connections, and has no effect on SMB2 clients. </p>
<p> Default: <i>keepalive</i><i> = </i><i>300</i><i> </i> </p>
<p> Example: <i>keepalive</i><i> = </i><i>600</i><i> </i></dl>
<p> kerberos encryption types (G) </p>
<dl>
<dd>This parameter determines the encryption types to use when operating as a Kerberos client. Possible values are <i>all</i>, <i>strong</i>, and <i>legacy</i>. </p>
<p> Samba uses a Kerberos library (MIT or Heimdal) to obtain Kerberos tickets. This library is normally configured outside of Samba, using the krb5.conf file. This file may also include directives to configure the encryption types to be used. However, Samba implements Active Directory protocols and algorithms to locate a domain controller. In order to force the Kerberos library into using the correct domain controller, some Samba processes, such as <code><a href="/docs/linux/man/8-winbindd/">winbindd</a></code>(8) and <code><a href="/docs/linux/man/8-net/">net</a></code>(8), build a private krb5.conf file for use by the Kerberos library while being invoked from Samba. This private file controls all aspects of the Kerberos library operation, and this parameter controls how the encryption types are configured within this generated file, and therefore also controls the encryption types negotiable by Samba. </p>
<p> When set to <code>all</code>, all active directory encryption types are allowed. </p>
<p> When set to <code>strong</code>, only AES-based encryption types are offered. This can be used in hardened environments to prevent downgrade attacks. </p>
<p> When set to <code>legacy</code>, only RC4-HMAC-MD5 is allowed. Avoiding AES this way has one a very specific use. Normally, the encryption type is negotiated between the peers. However, there is one scenario in which a Windows read-only domain controller (RODC) advertises AES encryption, but then proxies the request to a writeable DC which may not support AES encryption, leading to failure of the handshake. Setting this parameter to <code>legacy</code> would cause samba not to negotiate AES encryption. It is assumed of course that the weaker legacy encryption types are acceptable for the setup. </p>
<p> Default: <i>kerberos encryption types</i><i> = </i><i>all</i><i> </i></dl>
<p> kerberos method (G) </p>
<dl>
<dd>Controls how kerberos tickets are verified. </p>
<p> Valid options are:</p>
<dl>
<dd>
<dl>
<dd>&bull; secrets only &#8211; use only the secrets.tdb for ticket verification (default)</dl>
<dl>
<dd>&bull; system keytab &#8211; use only the system keytab for ticket verification</dl>
<dl>
<dd>&bull; dedicated keytab &#8211; use a dedicated keytab for ticket verification</dl>
<dl>
<dd>&bull; secrets and keytab &#8211; use the secrets.tdb first, then the system keytab</dl>
</dl>
<p> The major difference between &quot;system keytab&quot; and &quot;dedicated keytab&quot; is that the latter method relies on kerberos to find the correct keytab entry instead of filtering based on expected principals. </p>
<p> When the kerberos method is in &quot;dedicated keytab&quot; mode, m[blue]<code>dedicated keytab file</code>m[] must be set to specify the location of the keytab file. </p>
<p> Default: <i>kerberos method</i><i> = </i><i>default</i><i> </i></dl>
<p> kernel change notify (G) </p>
<dl>
<dd>This parameter specifies whether Samba should ask the kernel for change notifications in directories so that SMB clients can refresh whenever the data on the server changes. </p>
<p> This parameter is only used when your kernel supports change notification to user programs using the inotify interface. </p>
<p> Default: <i>kernel change notify</i><i> = </i><i>yes</i><i> </i></dl>
<p> kernel oplocks (S) </p>
<dl>
<dd>For UNIXes that support kernel based m[blue]<code>oplocks</code>m[] (currently only Linux), this parameter allows the use of them to be turned on or off. However, this disables Level II oplocks for clients as the Linux kernel does not support them properly. </p>
<p> Kernel oplocks support allows Samba <i>oplocks </i> to be broken whenever a local UNIX process or NFS operation accesses a file that <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) has oplocked. This allows complete data consistency between SMB/CIFS, NFS and local file access (and is a <i>very</i> cool feature :-). </p>
<p> If you do not need this interaction, you should disable the parameter on Linux to get Level II oplocks and the associated performance benefit. </p>
<p> This parameter defaults to <code>no</code> and is translated to a no-op on systems that do not have the necessary kernel support. </p>
<p> Default: <i>kernel oplocks</i><i> = </i><i>no</i><i> </i></dl>
<p> kernel share modes (S) </p>
<dl>
<dd>This parameter controls whether SMB share modes are translated into UNIX flocks. </p>
<p> Kernel share modes provide a minimal level of interoperability with local UNIX processes and NFS operations by preventing access with flocks corresponding to the SMB share modes. Generally, it is very desirable to leave this enabled. </p>
<p> Note that in order to use SMB2 durable file handles on a share, you have to turn kernel share modes off. </p>
<p> This parameter defaults to <code>yes</code> and is translated to a no-op on systems that do not have the necessary kernel flock support. </p>
<p> Default: <i>kernel share modes</i><i> = </i><i>yes</i><i> </i></dl>
<p> kpasswd port (G) </p>
<dl>
<dd>Specifies which ports the Kerberos server should listen on for password changes. </p>
<p> Default: <i>kpasswd port</i><i> = </i><i>464</i><i> </i></dl>
<p> krb5 port (G) </p>
<dl>
<dd>Specifies which port the KDC should listen on for Kerberos traffic. </p>
<p> Default: <i>krb5 port</i><i> = </i><i>88</i><i> </i></dl>
<p> lanman auth (G) </p>
<dl>
<dd>This parameter has been deprecated since Samba 4.11 and support for LanMan (as distinct from NTLM, NTLMv2 or Kerberos authentication) will be removed in a future Samba release. </p>
<p> That is, in the future, the current default of lanman auth = no will be the enforced behaviour. </p>
<p> This parameter determines whether or not <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) will attempt to authenticate users or permit password changes using the LANMAN password hash. If disabled, only clients which support NT password hashes (e.g. Windows NT/2000 clients, smbclient, but not Windows 95/98 or the MS DOS network client) will be able to connect to the Samba host. </p>
<p> The LANMAN encrypted response is easily broken, due to its case-insensitive nature, and the choice of algorithm. Servers without Windows 95/98/ME or MS DOS clients are advised to disable this option. </p>
<p> When this parameter is set to no this will also result in sambaLMPassword in Samba&#8217;s passdb being blanked after the next password change. As a result of that lanman clients won&#8217;t be able to authenticate, even if lanman auth is re-enabled later on. </p>
<p> Unlike the <i>encrypt passwords</i> option, this parameter cannot alter client behaviour, and the LANMAN response will still be sent over the network. See the client lanman auth to disable this for Samba&#8217;s clients (such as smbclient) </p>
<p> This parameter is overriden by <i>ntlm auth</i>, so unless that it is also set to <code>ntlmv1-permitted</code> or <code>yes</code>, then only NTLMv2 logins will be permited and no LM hash will be stored. All modern clients support NTLMv2, and but some older clients require special configuration to use it. </p>
<p> Default: <i>lanman auth</i><i> = </i><i>no</i><i> </i></dl>
<p> large readwrite (G) </p>
<dl>
<dd>This parameter determines whether or not <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) supports the new 64k streaming read and write variant SMB requests introduced with Windows 2000. Note that due to Windows 2000 client redirector bugs this requires Samba to be running on a 64-bit capable operating system such as IRIX, Solaris or a Linux 2.4 kernel. Can improve performance by 10% with Windows 2000 clients. Defaults to on. Not as tested as some other Samba code paths. </p>
<p> Default: <i>large readwrite</i><i> = </i><i>yes</i><i> </i></dl>
<p> ldap admin dn (G) </p>
<dl>
<dd>The m[blue]<code>ldap admin dn</code>m[] defines the Distinguished Name (DN) name used by Samba to contact the ldap server when retreiving user account information. The m[blue]<code>ldap admin dn</code>m[] is used in conjunction with the admin dn password stored in the private/secrets.tdb file. See the <code><a href="/docs/linux/man/8-smbpasswd/">smbpasswd</a></code>(8) man page for more information on how to accomplish this. </p>
<p> The m[blue]<code>ldap admin dn</code>m[] requires a fully specified DN. The m[blue]<code>ldap suffix</code>m[] is not appended to the m[blue]<code>ldap admin dn</code>m[]. </p>
<p> <i>No default</i></dl>
<p> ldap connection timeout (G) </p>
<dl>
<dd>This parameter tells the LDAP library calls which timeout in seconds they should honor during initial connection establishments to LDAP servers. It is very useful in failover scenarios in particular. If one or more LDAP servers are not reachable at all, we do not have to wait until TCP timeouts are over. This feature must be supported by your LDAP library. </p>
<p> This parameter is different from m[blue]<code>ldap timeout</code>m[] which affects operations on LDAP servers using an existing connection and not establishing an initial connection. </p>
<p> Default: <i>ldap connection timeout</i><i> = </i><i>2</i><i> </i></dl>
<p> ldap debug level (G) </p>
<dl>
<dd>This parameter controls the debug level of the LDAP library calls. In the case of OpenLDAP, it is the same bit-field as understood by the server and documented in the <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) manpage. A typical useful value will be <i>1</i> for tracing function calls. </p>
<p> The debug output from the LDAP libraries appears with the prefix [LDAP] in Samba&#8217;s logging output. The level at which LDAP logging is printed is controlled by the parameter <i>ldap debug threshold</i>. </p>
<p> Default: <i>ldap debug level</i><i> = </i><i>0</i><i> </i> </p>
<p> Example: <i>ldap debug level</i><i> = </i><i>1</i><i> </i></dl>
<p> ldap debug threshold (G) </p>
<dl>
<dd>This parameter controls the Samba debug level at which the ldap library debug output is printed in the Samba logs. See the description of <i>ldap debug level</i> for details. </p>
<p> Default: <i>ldap debug threshold</i><i> = </i><i>10</i><i> </i> </p>
<p> Example: <i>ldap debug threshold</i><i> = </i><i>5</i><i> </i></dl>
<p> ldap delete dn (G) </p>
<dl>
<dd>This parameter specifies whether a delete operation in the ldapsam deletes the complete entry or only the attributes specific to Samba. </p>
<p> Default: <i>ldap delete dn</i><i> = </i><i>no</i><i> </i></dl>
<p> ldap deref (G) </p>
<dl>
<dd>This option controls whether Samba should tell the LDAP library to use a certain alias dereferencing method. The default is <i>auto</i>, which means that the default setting of the ldap client library will be kept. Other possible values are <i>never</i>, <i>finding</i>, <i>searching</i> and <i>always</i>. Grab your LDAP manual for more information. </p>
<p> Default: <i>ldap deref</i><i> = </i><i>auto</i><i> </i> </p>
<p> Example: <i>ldap deref</i><i> = </i><i>searching</i><i> </i></dl>
<p> ldap follow referral (G) </p>
<dl>
<dd>This option controls whether to follow LDAP referrals or not when searching for entries in the LDAP database. Possible values are <i>on</i> to enable following referrals, <i>off</i> to disable this, and <i>auto</i>, to use the libldap default settings. libldap&#8217;s choice of following referrals or not is set in /etc/openldap/ldap.conf with the REFERRALS parameter as documented in <a href="/docs/linux/man/5-ldap-conf/">ldap.conf</a>(5). </p>
<p> Default: <i>ldap follow referral</i><i> = </i><i>auto</i><i> </i> </p>
<p> Example: <i>ldap follow referral</i><i> = </i><i>off</i><i> </i></dl>
<p> ldap group suffix (G) </p>
<dl>
<dd>This parameter specifies the suffix that is used for groups when these are added to the LDAP directory. If this parameter is unset, the value of m[blue]<code>ldap suffix</code>m[] will be used instead. The suffix string is pre-pended to the m[blue]<code>ldap suffix</code>m[] string so use a partial DN. </p>
<p> Default: <i>ldap group suffix</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>ldap group suffix</i><i> = </i><i>ou=Groups</i><i> </i></dl>
<p> ldap idmap suffix (G) </p>
<dl>
<dd>This parameters specifies the suffix that is used when storing idmap mappings. If this parameter is unset, the value of m[blue]<code>ldap suffix</code>m[] will be used instead. The suffix string is pre-pended to the m[blue]<code>ldap suffix</code>m[] string so use a partial DN. </p>
<p> Default: <i>ldap idmap suffix</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>ldap idmap suffix</i><i> = </i><i>ou=Idmap</i><i> </i></dl>
<p> ldap machine suffix (G) </p>
<dl>
<dd>It specifies where machines should be added to the ldap tree. If this parameter is unset, the value of m[blue]<code>ldap suffix</code>m[] will be used instead. The suffix string is pre-pended to the m[blue]<code>ldap suffix</code>m[] string so use a partial DN. </p>
<p> Default: <i>ldap machine suffix</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>ldap machine suffix</i><i> = </i><i>ou=Computers</i><i> </i></dl>
<p> ldap max anonymous request size (G) </p>
<dl>
<dd>This parameter specifies the maximum permitted size (in bytes) for an LDAP request received on an anonymous connection. </p>
<p> If the request size exceeds this limit the request will be rejected. </p>
<p> Default: <i>ldap max anonymous request size</i><i> = </i><i>256000</i><i> </i> </p>
<p> Example: <i>ldap max anonymous request size</i><i> = </i><i>500000</i><i> </i></dl>
<p> ldap max authenticated request size (G) </p>
<dl>
<dd>This parameter specifies the maximum permitted size (in bytes) for an LDAP request received on an authenticated connection. </p>
<p> If the request size exceeds this limit the request will be rejected. </p>
<p> Default: <i>ldap max authenticated request size</i><i> = </i><i>16777216</i><i> </i> </p>
<p> Example: <i>ldap max authenticated request size</i><i> = </i><i>4194304</i><i> </i></dl>
<p> ldap max search request size (G) </p>
<dl>
<dd>This parameter specifies the maximum permitted size (in bytes) for an LDAP search request. </p>
<p> If the request size exceeds this limit the request will be rejected. </p>
<p> Default: <i>ldap max search request size</i><i> = </i><i>256000</i><i> </i> </p>
<p> Example: <i>ldap max search request size</i><i> = </i><i>4194304</i><i> </i></dl>
<p> ldap page size (G) </p>
<dl>
<dd>This parameter specifies the number of entries per page. </p>
<p> If the LDAP server supports paged results, clients can request subsets of search results (pages) instead of the entire list. This parameter specifies the size of these pages. </p>
<p> Default: <i>ldap page size</i><i> = </i><i>1000</i><i> </i> </p>
<p> Example: <i>ldap page size</i><i> = </i><i>512</i><i> </i></dl>
<p> ldap password sync </p>
<dl>
<dd>This parameter is a synonym for ldap passwd sync.</dl>
<p> ldap passwd sync (G) </p>
<dl>
<dd>This option is used to define whether or not Samba should sync the LDAP password with the NT and LM hashes for normal accounts (NOT for workstation, server or domain trusts) on a password change via SAMBA. </p>
<p> The m[blue]<code>ldap passwd sync</code>m[] can be set to one of three values:</p>
<dl>
<dd>
<dl>
<dd>&bull; <i>Yes</i> = Try to update the LDAP, NT and LM passwords and update the pwdLastSet time.</dl>
<dl>
<dd>&bull; <i>No</i> = Update NT and LM passwords and update the pwdLastSet time.</dl>
<dl>
<dd>&bull; <i>Only</i> = Only update the LDAP password and let the LDAP server do the rest.</dl>
</dl>
<p> Default: <i>ldap passwd sync</i><i> = </i><i>no</i><i> </i></dl>
<p> ldap replication sleep (G) </p>
<dl>
<dd>When Samba is asked to write to a read-only LDAP replica, we are redirected to talk to the read-write master server. This server then replicates our changes back to the &#8216;local&#8217; server, however the replication might take some seconds, especially over slow links. Certain client activities, particularly domain joins, can become confused by the &#8216;success&#8217; that does not immediately change the LDAP back-end&#8217;s data. </p>
<p> This option simply causes Samba to wait a short time, to allow the LDAP server to catch up. If you have a particularly high-latency network, you may wish to time the LDAP replication with a network sniffer, and increase this value accordingly. Be aware that no checking is performed that the data has actually replicated. </p>
<p> The value is specified in milliseconds, the maximum value is 5000 (5 seconds). </p>
<p> Default: <i>ldap replication sleep</i><i> = </i><i>1000</i><i> </i></dl>
<p> ldapsam:editposix (G) </p>
<dl>
<dd>Editposix is an option that leverages ldapsam:trusted to make it simpler to manage a domain controller eliminating the need to set up custom scripts to add and manage the posix users and groups. This option will instead directly manipulate the ldap tree to create, remove and modify user and group entries. This option also requires a running winbindd as it is used to allocate new uids/gids on user/group creation. The allocation range must be therefore configured. </p>
<p> To use this option, a basic ldap tree must be provided and the ldap suffix parameters must be properly configured. On virgin servers the default users and groups (Administrator, Guest, Domain Users, Domain Admins, Domain Guests) can be precreated with the command net sam provision. To run this command the ldap server must be running, Winbindd must be running and the smb.conf ldap options must be properly configured. The typical ldap setup used with the m[blue]<code>ldapsam:trusted = yes</code>m[] option is usually sufficient to use m[blue]<code>ldapsam:editposix = yes</code>m[] as well. </p>
<p> An example configuration can be the following: </p>
<dl>
<dd>
<pre> encrypt passwords = true
 passdb backend = ldapsam
 ldapsam:trusted=yes
 ldapsam:editposix=yes
 ldap admin dn = cn=admin,dc=samba,dc=org
 ldap delete dn = yes
 ldap group suffix = ou=groups
 ldap idmap suffix = ou=idmap
 ldap machine suffix = ou=computers
 ldap user suffix = ou=users
 ldap suffix = dc=samba,dc=org
 idmap backend = ldap:&quot;<a href="ldap://localhost">ldap://localhost</a>&quot;
 idmap uid = 5000-50000
 idmap gid = 5000-50000</pre>
</dl>
<p> This configuration assumes a directory layout like described in the following ldif: </p>
<dl>
<dd>
<pre> dn: dc=samba,dc=org
 objectClass: top
 objectClass: dcObject
 objectClass: organization
 o: samba.org
 dc: samba
 dn: cn=admin,dc=samba,dc=org
 objectClass: simpleSecurityObject
 objectClass: organizationalRole
 cn: admin
 description: LDAP administrator
 userPassword: secret
 dn: ou=users,dc=samba,dc=org
 objectClass: top
 objectClass: organizationalUnit
 ou: users
 dn: ou=groups,dc=samba,dc=org
 objectClass: top
 objectClass: organizationalUnit
 ou: groups
 dn: ou=idmap,dc=samba,dc=org
 objectClass: top
 objectClass: organizationalUnit
 ou: idmap
 dn: ou=computers,dc=samba,dc=org
 objectClass: top
 objectClass: organizationalUnit
 ou: computers</pre>
</dl>
<p> Default: <i>ldapsam:editposix</i><i> = </i><i>no</i><i> </i></dl>
<p> ldapsam:trusted (G) </p>
<dl>
<dd>By default, Samba as a Domain Controller with an LDAP backend needs to use the Unix-style NSS subsystem to access user and group information. Due to the way Unix stores user information in /etc/passwd and /etc/group this inevitably leads to inefficiencies. One important question a user needs to know is the list of groups he is member of. The plain UNIX model involves a complete enumeration of the file /etc/group and its NSS counterparts in LDAP. UNIX has optimized functions to enumerate group membership. Sadly, other functions that are used to deal with user and group attributes lack such optimization. </p>
<p> To make Samba scale well in large environments, the m[blue]<code>ldapsam:trusted = yes</code>m[] option assumes that the complete user and group database that is relevant to Samba is stored in LDAP with the standard posixAccount/posixGroup attributes. It further assumes that the Samba auxiliary object classes are stored together with the POSIX data in the same LDAP object. If these assumptions are met, m[blue]<code>ldapsam:trusted = yes</code>m[] can be activated and Samba can bypass the NSS system to query user group memberships. Optimized LDAP queries can greatly speed up domain logon and administration tasks. Depending on the size of the LDAP database a factor of 100 or more for common queries is easily achieved. </p>
<p> Default: <i>ldapsam:trusted</i><i> = </i><i>no</i><i> </i></dl>
<p> ldap server require strong auth (G) </p>
<dl>
<dd>The m[blue]<code>ldap server require strong auth</code>m[] defines whether the ldap server requires ldap traffic to be signed or signed and encrypted (sealed). Possible values are <i>no</i>, <i>allow_sasl_over_tls</i> and <i>yes</i>. </p>
<p> A value of <i>no</i> allows simple and sasl binds over all transports. </p>
<p> A value of <i>allow_sasl_over_tls</i> allows simple and sasl binds (without sign or seal) over TLS encrypted connections. Unencrypted connections only allow sasl binds with sign or seal. </p>
<p> A value of <i>yes</i> allows only simple binds over TLS encrypted connections. Unencrypted connections only allow sasl binds with sign or seal. </p>
<p> Default: <i>ldap server require strong auth</i><i> = </i><i>yes</i><i> </i></dl>
<p> ldap ssl (G) </p>
<dl>
<dd>This option is used to define whether or not Samba should use SSL when connecting to the ldap server This is <i>NOT</i> related to Samba&#8217;s previous SSL support which was enabled by specifying the &#8211;with-ssl option to the configure script. </p>
<p> LDAP connections should be secured where possible. This may be done setting <i>either</i> this parameter to <i>start tls</i> <i>or</i> by specifying <i>ldaps://</i> in the URL argument of m[blue]<code>passdb backend</code>m[]. </p>
<p> The m[blue]<code>ldap ssl</code>m[] can be set to one of two values:</p>
<dl>
<dd>
<dl>
<dd>&bull; <i>Off</i> = Never use SSL when querying the directory.</dl>
<dl>
<dd>&bull; <i>start tls</i> = Use the LDAPv3 StartTLS extended operation (RFC2830) for communicating with the directory server.</dl>
</dl>
<p> Please note that this parameter does only affect <i>rpc</i> methods. To enable the LDAPv3 StartTLS extended operation (RFC2830) for <i>ads</i>, set m[blue]<code>ldap ssl = start tls</code>m[] <i>and</i> m[blue]<code>ldap ssl ads = yes</code>m[]. See <a href="/docs/linux/man/5-smb-conf/">smb.conf</a>(5) for more information on m[blue]<code>ldap ssl ads</code>m[]. </p>
<p> Default: <i>ldap ssl</i><i> = </i><i>start tls</i><i> </i></dl>
<p> ldap ssl ads (G) </p>
<dl>
<dd>This option is used to define whether or not Samba should use SSL when connecting to the ldap server using <i>ads</i> methods. Rpc methods are not affected by this parameter. Please note, that this parameter won&#8217;t have any effect if m[blue]<code>ldap ssl</code>m[] is set to <i>no</i>. </p>
<p> See <a href="/docs/linux/man/5-smb-conf/">smb.conf</a>(5) for more information on m[blue]<code>ldap ssl</code>m[]. </p>
<p> Default: <i>ldap ssl ads</i><i> = </i><i>no</i><i> </i></dl>
<p> ldap suffix (G) </p>
<dl>
<dd>Specifies the base for all ldap suffixes and for storing the sambaDomain object. </p>
<p> The ldap suffix will be appended to the values specified for the m[blue]<code>ldap user suffix</code>m[], m[blue]<code>ldap group suffix</code>m[], m[blue]<code>ldap machine suffix</code>m[], and the m[blue]<code>ldap idmap suffix</code>m[]. Each of these should be given only a DN relative to the m[blue]<code>ldap suffix</code>m[]. </p>
<p> Default: <i>ldap suffix</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>ldap suffix</i><i> = </i><i>dc=samba,dc=org</i><i> </i></dl>
<p> ldap timeout (G) </p>
<dl>
<dd>This parameter defines the number of seconds that Samba should use as timeout for LDAP operations. </p>
<p> Default: <i>ldap timeout</i><i> = </i><i>15</i><i> </i></dl>
<p> ldap user suffix (G) </p>
<dl>
<dd>This parameter specifies where users are added to the tree. If this parameter is unset, the value of m[blue]<code>ldap suffix</code>m[] will be used instead. The suffix string is pre-pended to the m[blue]<code>ldap suffix</code>m[] string so use a partial DN. </p>
<p> Default: <i>ldap user suffix</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>ldap user suffix</i><i> = </i><i>ou=people</i><i> </i></dl>
<p> level2 oplocks (S) </p>
<dl>
<dd>This parameter controls whether Samba supports level2 (read-only) oplocks on a share. </p>
<p> Level2, or read-only oplocks allow Windows NT clients that have an oplock on a file to downgrade from a read-write oplock to a read-only oplock once a second client opens the file (instead of releasing all oplocks on a second open, as in traditional, exclusive oplocks). This allows all openers of the file that support level2 oplocks to cache the file for read-ahead only (ie. they may not cache writes or lock requests) and increases performance for many accesses of files that are not commonly written (such as application .EXE files). </p>
<p> Once one of the clients which have a read-only oplock writes to the file all clients are notified (no reply is needed or waited for) and told to break their oplocks to &quot;none&quot; and delete any read-ahead caches. </p>
<p> It is recommended that this parameter be turned on to speed access to shared executables. </p>
<p> For more discussions on level2 oplocks see the CIFS spec. </p>
<p> Currently, if m[blue]<code>kernel oplocks</code>m[] are supported then level2 oplocks are not granted (even if this parameter is set to <code>yes</code>). Note also, the m[blue]<code>oplocks</code>m[] parameter must be set to <code>yes</code> on this share in order for this parameter to have any effect. </p>
<p> Default: <i>level2 oplocks</i><i> = </i><i>yes</i><i> </i></dl>
<p> lm announce (G) </p>
<dl>
<dd>This parameter determines if <code><a href="/docs/linux/man/8-nmbd/">nmbd</a></code>(8) will produce Lanman announce broadcasts that are needed by OS/2 clients in order for them to see the Samba server in their browse list. This parameter can have three values, <code>yes</code>, <code>no</code>, or <code>auto</code>. The default is <code>auto</code>. If set to <code>no</code> Samba will never produce these broadcasts. If set to <code>yes</code> Samba will produce Lanman announce broadcasts at a frequency set by the parameter m[blue]<code>lm interval</code>m[]. If set to <code>auto</code> Samba will not send Lanman announce broadcasts by default but will listen for them. If it hears such a broadcast on the wire it will then start sending them at a frequency set by the parameter m[blue]<code>lm interval</code>m[]. </p>
<p> Default: <i>lm announce</i><i> = </i><i>auto</i><i> </i> </p>
<p> Example: <i>lm announce</i><i> = </i><i>yes</i><i> </i></dl>
<p> lm interval (G) </p>
<dl>
<dd>If Samba is set to produce Lanman announce broadcasts needed by OS/2 clients (see the m[blue]<code>lm announce</code>m[] parameter) then this parameter defines the frequency in seconds with which they will be made. If this is set to zero then no Lanman announcements will be made despite the setting of the m[blue]<code>lm announce</code>m[] parameter. </p>
<p> Default: <i>lm interval</i><i> = </i><i>60</i><i> </i> </p>
<p> Example: <i>lm interval</i><i> = </i><i>120</i><i> </i></dl>
<p> load printers (G) </p>
<dl>
<dd>A boolean variable that controls whether all printers in the printcap will be loaded for browsing by default. See the m[blue]<code>printers</code>m[] section for more details. </p>
<p> Default: <i>load printers</i><i> = </i><i>yes</i><i> </i></dl>
<p> local master (G) </p>
<dl>
<dd>This option allows <code><a href="/docs/linux/man/8-nmbd/">nmbd</a></code>(8) to try and become a local master browser on a subnet. If set to <code>no</code> then nmbd will not attempt to become a local master browser on a subnet and will also lose in all browsing elections. By default this value is set to <code>yes</code>. Setting this value to <code>yes</code> doesn&#8217;t mean that Samba will <i>become</i> the local master browser on a subnet, just that nmbd will <i>participate</i> in elections for local master browser. </p>
<p> Setting this value to <code>no</code> will cause nmbd <i>never</i> to become a local master browser. </p>
<p> Default: <i>local master</i><i> = </i><i>yes</i><i> </i></dl>
<p> lock dir </p>
<dl>
<dd>This parameter is a synonym for lock directory.</dl>
<p> lock directory (G) </p>
<dl>
<dd>This option specifies the directory where lock files will be placed. The lock files are used to implement the m[blue]<code>max connections</code>m[] option. </p>
<p> Note: This option can not be set inside registry configurations. </p>
<p> The files placed in this directory are not required across service restarts and can be safely placed on volatile storage (e.g. tmpfs in Linux) </p>
<p> Default: <i>lock directory</i><i> = </i><i>/run/samba</i><i> </i> </p>
<p> Example: <i>lock directory</i><i> = </i><i>/var/run/samba/locks</i><i> </i></dl>
<p> locking (S) </p>
<dl>
<dd>This controls whether or not locking will be performed by the server in response to lock requests from the client. </p>
<p> If locking = no, all lock and unlock requests will appear to succeed and all lock queries will report that the file in question is available for locking. </p>
<p> If locking = yes, real locking will be performed by the server. </p>
<p> This option <i>may</i> be useful for read-only filesystems which <i>may</i> not need locking (such as CDROM drives), although setting this parameter of <code>no</code> is not really recommended even in this case. </p>
<p> Be careful about disabling locking either globally or in a specific service, as lack of locking may result in data corruption. You should never need to set this parameter. </p>
<p> Default: <i>locking</i><i> = </i><i>yes</i><i> </i></dl>
<p> lock spin time (G) </p>
<dl>
<dd>The time in milliseconds that smbd should keep waiting to see if a failed lock request can be granted. This parameter has changed in default value from Samba 3.0.23 from 10 to 200. The associated m[blue]<code>lock spin count</code>m[] parameter is no longer used in Samba 3.0.24. You should not need to change the value of this parameter. </p>
<p> Default: <i>lock spin time</i><i> = </i><i>200</i><i> </i></dl>
<p> log file (G) </p>
<dl>
<dd>This option allows you to override the name of the Samba log file (also known as the debug file). </p>
<p> This option takes the standard substitutions, allowing you to have separate log files for each user or machine. </p>
<p> <i>No default</i> </p>
<p> Example: <i>log file</i><i> = </i><i>/usr/local/samba/var/log.%m</i><i> </i></dl>
<p> logging (G) </p>
<dl>
<dd>This parameter configures logging backends. Multiple backends can be specified at the same time, with different log levels for each backend. The parameter is a list of backends, where each backend is specified as backend[:option][@loglevel]. </p>
<p> The &#8216;option&#8217; parameter can be used to pass backend-specific options. </p>
<p> The log level for a backend is optional, if it is not set for a backend, all messages are sent to this backend. The parameter m[blue]<code>log level</code>m[] determines overall log levels, while the log levels specified here define what is sent to the individual backends. </p>
<p> When m[blue]<code>logging</code>m[] is set, it overrides the m[blue]<code>syslog</code>m[] and m[blue]<code>syslog only</code>m[] parameters. </p>
<p> Some backends are only available when Samba has been compiled with the additional libraries. The overall list of logging backends:</p>
<dl>
<dd>
<dl>
<dd>&bull; <i>syslog</i></dl>
<dl>
<dd>&bull; <i>file</i></dl>
<dl>
<dd>&bull; <i>systemd</i></dl>
<dl>
<dd>&bull; <i>lttng</i></dl>
<dl>
<dd>&bull; <i>gpfs</i></dl>
<dl>
<dd>&bull; <i>ringbuf</i></dl>
</dl>
<p> The <i>ringbuf</i> backend supports an optional size argument to change the buffer size used, the default is 1 MB: <i>ringbuf:size=NBYTES</i> </p>
<p> Default: <i>logging</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>logging</i><i> = </i><i>syslog@1 file</i><i> </i></dl>
<p> debuglevel </p>
<dl>
<dd>This parameter is a synonym for log level.</dl>
<p> log level (G) </p>
<dl>
<dd>The value of the parameter (a string) allows the debug level (logging level) to be specified in the smb.conf file. </p>
<p> This parameter has been extended since the 2.2.x series, now it allows one to specify the debug level for multiple debug classes and distinct logfiles for debug classes. This is to give greater flexibility in the configuration of the system. The following debug classes are currently implemented:</p>
<dl>
<dd>
<dl>
<dd>&bull; <i>all</i></dl>
<dl>
<dd>&bull; <i>tdb</i></dl>
<dl>
<dd>&bull; <i>printdrivers</i></dl>
<dl>
<dd>&bull; <i>lanman</i></dl>
<dl>
<dd>&bull; <i>smb</i></dl>
<dl>
<dd>&bull; <i>smb2</i></dl>
<dl>
<dd>&bull; <i>smb2_credits</i></dl>
<dl>
<dd>&bull; <i>rpc_parse</i></dl>
<dl>
<dd>&bull; <i>rpc_srv</i></dl>
<dl>
<dd>&bull; <i>rpc_cli</i></dl>
<dl>
<dd>&bull; <i>passdb</i></dl>
<dl>
<dd>&bull; <i>sam</i></dl>
<dl>
<dd>&bull; <i>auth</i></dl>
<dl>
<dd>&bull; <i>winbind</i></dl>
<dl>
<dd>&bull; <i>vfs</i></dl>
<dl>
<dd>&bull; <i>idmap</i></dl>
<dl>
<dd>&bull; <i>quota</i></dl>
<dl>
<dd>&bull; <i>acls</i></dl>
<dl>
<dd>&bull; <i>locking</i></dl>
<dl>
<dd>&bull; <i>msdfs</i></dl>
<dl>
<dd>&bull; <i>dmapi</i></dl>
<dl>
<dd>&bull; <i>registry</i></dl>
<dl>
<dd>&bull; <i>scavenger</i></dl>
<dl>
<dd>&bull; <i>dns</i></dl>
<dl>
<dd>&bull; <i>ldb</i></dl>
<dl>
<dd>&bull; <i>tevent</i></dl>
<dl>
<dd>&bull; <i>auth_audit</i></dl>
<dl>
<dd>&bull; <i>auth_json_audit</i></dl>
<dl>
<dd>&bull; <i>kerberos</i></dl>
<dl>
<dd>&bull; <i>dsdb_audit</i></dl>
<dl>
<dd>&bull; <i>dsdb_json_audit</i></dl>
<dl>
<dd>&bull; <i>dsdb_password_audit</i></dl>
<dl>
<dd>&bull; <i>dsdb_password_json_audit</i></dl>
<dl>
<dd>&bull; <i>dsdb_transaction_audit</i></dl>
<dl>
<dd>&bull; <i>dsdb_transaction_json_audit</i></dl>
</dl>
<p> To configure the logging for specific classes to go into a different file then m[blue]<code>log file</code>m[], you can append <i>@PATH</i> to the class, eg <i>log level = 1 full_audit:1@/var/log/audit.log</i>. </p>
<p> Authentication and authorization audit information is logged under the auth_audit, and if Samba was not compiled with &#8211;without-json, a JSON representation is logged under auth_json_audit. </p>
<p> Support is comprehensive for all authentication and authorisation of user accounts in the Samba Active Directory Domain Controller, as well as the implicit authentication in password changes. In the file server, NTLM authentication, SMB and RPC authorization is covered. </p>
<p> Log levels for auth_audit and auth_audit_json are:</p>
<dl>
<dd>
<dl>
<dd>&bull; 2: Authentication Failure</dl>
<dl>
<dd>&bull; 3: Authentication Success</dl>
<dl>
<dd>&bull; 4: Authorization Success</dl>
<dl>
<dd>&bull; 5: Anonymous Authentication and Authorization Success</dl>
</dl>
<p> Changes to the sam.ldb database are logged under the dsdb_audit and a JSON representation is logged under dsdb_json_audit. </p>
<p> Password changes and Password resets are logged under dsdb_password_audit and a JSON representation is logged under the dsdb_password_json_audit. </p>
<p> Transaction rollbacks and prepare commit failures are logged under the dsdb_transaction_audit and a JSON representation is logged under the password_json_audit. Logging the transaction details allows the identification of password and sam.ldb operations that have been rolled back. </p>
<p> Default: <i>log level</i><i> = </i><i>0</i><i> </i> </p>
<p> Example: <i>log level</i><i> = </i><i>3 passdb:5 auth:10 winbind:2</i><i> </i> </p>
<p> Example: <i>log level</i><i> = </i><i>1 full_audit:1@/var/log/audit.log winbind:2</i><i> </i></dl>
<p> log nt token command (G) </p>
<dl>
<dd>This option can be set to a command that will be called when new nt tokens are created. </p>
<p> This is only useful for development purposes. </p>
<p> Default: <i>log nt token command</i><i> = </i><i></i><i> </i></dl>
<p> logon drive (G) </p>
<dl>
<dd>This parameter specifies the local path to which the home directory will be connected (see m[blue]<code>logon home</code>m[]) and is only used by NT Workstations. </p>
<p> Note that this option is only useful if Samba is set up as a logon server. </p>
<p> Default: <i>logon drive</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>logon drive</i><i> = </i><i>h:</i><i> </i></dl>
<p> logon home (G) </p>
<dl>
<dd>This parameter specifies the home directory location when a Win95/98 or NT Workstation logs into a Samba PDC. It allows you to do </p>
<p> C:\&gt;<code>NET USE H: /HOME</code> </p>
<p> from a command prompt, for example. </p>
<p> This option takes the standard substitutions, allowing you to have separate logon scripts for each user or machine. </p>
<p> This parameter can be used with Win9X workstations to ensure that roaming profiles are stored in a subdirectory of the user&#8217;s home directory. This is done in the following way: </p>
<p> logon home = \%N\%U\profile </p>
<p> This tells Samba to return the above string, with substitutions made when a client requests the info, generally in a NetUserGetInfo request. Win9X clients truncate the info to \server\share when a user does net use /home but use the whole string when dealing with profiles. </p>
<p> Note that in prior versions of Samba, the m[blue]<code>logon path</code>m[] was returned rather than <i>logon home</i>. This broke net use /home but allowed profiles outside the home directory. The current implementation is correct, and can be used for profiles if you use the above trick. </p>
<p> Disable this feature by setting m[blue]<code>logon home = &quot;&quot;</code>m[] &#8211; using the empty string. </p>
<p> This option is only useful if Samba is set up as a logon server. </p>
<p> Default: <i>logon home</i><i> = </i><i>\%N\%U</i><i> </i> </p>
<p> Example: <i>logon home</i><i> = </i><i>\remote_smb_server\%U</i><i> </i></dl>
<p> logon path (G) </p>
<dl>
<dd>This parameter specifies the directory where roaming profiles (Desktop, NTuser.dat, etc) are stored. Contrary to previous versions of these manual pages, it has nothing to do with Win 9X roaming profiles. To find out how to handle roaming profiles for Win 9X system, see the m[blue]<code>logon home</code>m[] parameter. </p>
<p> This option takes the standard substitutions, allowing you to have separate logon scripts for each user or machine. It also specifies the directory from which the &quot;Application Data&quot;, desktop, start menu, network neighborhood, programs and other folders, and their contents, are loaded and displayed on your Windows NT client. </p>
<p> The share and the path must be readable by the user for the preferences and directories to be loaded onto the Windows NT client. The share must be writeable when the user logs in for the first time, in order that the Windows NT client can create the NTuser.dat and other directories. Thereafter, the directories and any of the contents can, if required, be made read-only. It is not advisable that the NTuser.dat file be made read-only &#8211; rename it to NTuser.man to achieve the desired effect (a <i>MAN</i>datory profile). </p>
<p> Windows clients can sometimes maintain a connection to the [homes] share, even though there is no user logged in. Therefore, it is vital that the logon path does not include a reference to the homes share (i.e. setting this parameter to \%N\homes\profile_path will cause problems). </p>
<p> This option takes the standard substitutions, allowing you to have separate logon scripts for each user or machine. </p>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font><br />
 Do not quote the value. Setting this as &#8220;\%N\profile\%U&#8221; will break profile handling. Where the tdbsam or ldapsam passdb backend is used, at the time the user account is created the value configured for this parameter is written to the passdb backend and that value will over-ride the parameter value present in the smb.conf file. Any error present in the passdb backend account record must be editted using the appropriate tool (pdbedit on the command-line, or any other locally provided system tool). </p>
</dl>
<p> Note that this option is only useful if Samba is set up as a domain controller. </p>
<p> Disable the use of roaming profiles by setting the value of this parameter to the empty string. For example, m[blue]<code>logon path = &quot;&quot;</code>m[]. Take note that even if the default setting in the smb.conf file is the empty string, any value specified in the user account settings in the passdb backend will over-ride the effect of setting this parameter to null. Disabling of all roaming profile use requires that the user account settings must also be blank. </p>
<p> An example of use is: </p>
<dl>
<dd>
<pre>logon path = \PROFILESERVER\PROFILE\%U</pre>
</dl>
<p> Default: <i>logon path</i><i> = </i><i>\%N\%U\profile</i><i> </i></dl>
<p> logon script (G) </p>
<dl>
<dd>This parameter specifies the batch file (.bat) or NT command file (.cmd) to be downloaded and run on a machine when a user successfully logs in. The file must contain the DOS style CR/LF line endings. Using a DOS-style editor to create the file is recommended. </p>
<p> The script must be a relative path to the <i>[netlogon]</i> service. If the [netlogon] service specifies a m[blue]<code>path</code>m[] of /usr/local/samba/netlogon, and m[blue]<code>logon script = STARTUP.BAT</code>m[], then the file that will be downloaded is: </p>
<dl>
<dd>
<pre> /usr/local/samba/netlogon/STARTUP.BAT</pre>
</dl>
<p> The contents of the batch file are entirely your choice. A suggested command would be to add NET TIME \SERVER /SET /YES, to force every machine to synchronize clocks with the same time server. Another use would be to add NET USE U: \SERVER
