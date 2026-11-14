---
title: "smb(5)"
name: "smb"
section: "5"
letter: "s"
url: "/docs/linux/man/5-smb/"
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
<p> Some modifications are then made to the newly created share: </p>
<dl>
<dd>&bull; The share name is changed from homes to the located username.</dl>
<dl>
<dd>&bull; If no path was given, the path is set to the user&#8217;s home directory.</dl>
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
<p> A few modifications are then made to the newly created share: </p>
<dl>
<dd>&bull; The share name is set to the located printer name</dl>
<dl>
<dd>&bull; If no printer name was given, the printer name is set to the located printer name</dl>
<dl>
<dd>&bull; If the share does not permit guest access and no username was given, the username is set to the located printer name.</dl>
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
<dd>the selected protocol level after protocol negotiation. It can be one of CORE, COREPLUS, LANMAN1, LANMAN2, NT1, SMB2_02, SMB2_10, SMB2_22, SMB2_24, SMB3_00 or SMB2_FF.</dl>
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
<p> %i</p>
<dl>
<dd>the local IP address to which a client connected. </p>
<p> Before 4.0.0 it could contain IPv4 mapped IPv6 addresses, now it only contains IPv4 or IPv6 addresses.</dl>
<p> %T</p>
<dl>
<dd>the current date and time.</dl>
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
<p>Starting with Samba version 3.2.0, the capability to store Samba configuration in the registry is available. The configuration is stored in the registry key <i>HKLM\Software\Samba\smbconf</i>. There are two levels of registry configuration: </p>
<dl>
<dd>1. Share definitions stored in registry are used. This is triggered by setting the global parameter <i>registry shares</i> to &#8220;yes&#8221; in <i>smb.conf</i>. </p>
<p> The registry shares are loaded not at startup but on demand at runtime by <i>smbd</i>. Shares defined in <i>smb.conf</i> take priority over shares of the same name defined in registry.</dl>
<dl>
<dd>2. Global <i>smb.conf</i> options stored in registry are used. This can be activated in two different ways: </p>
<p> Firstly, a registry only configuration is triggered by setting m[blue]<code>config backend = registry</code>m[] in the [global] section of <i>smb.conf</i>. This resets everything that has been read from config files to this point and reads the content of the global configuration section from the registry. This is the recommended method of using registry based configuration. </p>
<p> Secondly, a mixed configuration can be activated by a special new meaning of the parameter m[blue]<code>include = registry</code>m[] in the [global] section of <i>smb.conf</i>. This reads the global options from registry with the same priorities as for an include of a text file. This may be especially useful in cases where an initial configuration is needed to access the registry. </p>
<p> Activation of global registry options automatically activates registry shares. So in the registry only case, shares are loaded on demand only.</dl>
<p> Note: To make registry-based configurations foolproof at least to a certain extent, the use of <i>lock directory</i> and <i>config backend</i> inside the registry configuration has been disabled: Especially by changing the <i>lock directory</i> inside the registry configuration, one would create a broken setup where the daemons do not see the configuration they loaded once it is active. </p>
<p> The registry configuration can be accessed with tools like <i>regedit</i> or <i>net (rpc) registry</i> in the key <i>HKLM\Software\Samba\smbconf</i>. More conveniently, the <i>conf</i> subcommand of the <code><a href="/docs/linux/man/8-net/">net</a></code>(8) utility offers a dedicated interface to read and write the registry based configuration locally, i.e. directly accessing the database file, circumventing the server.</p>
<h2>Explanation Of Each Parameter</h2>
<p>bind interfaces only (G) </p>
<dl>
<dd>This global parameter allows the Samba admin to limit what interfaces on a machine will serve SMB requests. It affects file service <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) and name service <code><a href="/docs/linux/man/8-nmbd/">nmbd</a></code>(8) in a slightly different ways. </p>
<p> For name service it causes nmbd to bind to ports 137 and 138 on the interfaces listed in the m[blue]<code>interfaces</code>m[] parameter. nmbd also binds to the &quot;all addresses&quot; interface (0.0.0.0) on ports 137 and 138 for the purposes of reading broadcast messages. If this option is not set then nmbd will service name requests on all of these sockets. If m[blue]<code>bind interfaces only</code>m[] is set then nmbd will check the source address of any packets coming in on the broadcast sockets and discard any that don&#8217;t match the broadcast addresses of the interfaces in the m[blue]<code>interfaces</code>m[] parameter list. As unicast packets are received on the other sockets it allows nmbd to refuse to serve names to machines that send packets that arrive through any interfaces not listed in the m[blue]<code>interfaces</code>m[] list. IP Source address spoofing does defeat this simple check, however, so it must not be used seriously as a security feature for nmbd. </p>
<p> For file service it causes <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) to bind only to the interface list given in the m[blue]<code>interfaces</code>m[] parameter. This restricts the networks that smbd will serve, to packets coming in on those interfaces. Note that you should not use this parameter for machines that are serving PPP or other intermittent or non-broadcast network interfaces as it will not cope with non-permanent interfaces. </p>
<p> If m[blue]<code>bind interfaces only</code>m[] is set and the network address <i>127.0.0.1</i> is not added to the m[blue]<code>interfaces</code>m[] parameter list <code><a href="/docs/linux/man/8-smbpasswd/">smbpasswd</a></code>(8) may not work as expected due to the reasons covered below. </p>
<p> To change a users SMB password, the smbpasswd by default connects to the <i>localhost &#8211; 127.0.0.1</i> address as an SMB client to issue the password change request. If m[blue]<code>bind interfaces only</code>m[] is set then unless the network address <i>127.0.0.1</i> is added to the m[blue]<code>interfaces</code>m[] parameter list then smbpasswd will fail to connect in it&#8217;s default mode. smbpasswd can be forced to use the primary IP interface of the local host by using its <code><a href="/docs/linux/man/8-smbpasswd/">smbpasswd</a></code>(8)<i>-r </i><i>remote machine</i> parameter, with <i>remote machine</i> set to the IP name of the primary interface of the local host. </p>
<p> Default: <i>bind interfaces only</i><i> = </i><i>no</i><i> </i></dl>
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
<p> dos charset (G) </p>
<dl>
<dd>DOS SMB clients assume the server has the same charset as they do. This option specifies which charset Samba should talk to DOS clients. </p>
<p> The default depends on which charsets you have installed. Samba tries to use charset 850 but falls back to ASCII in case it is not available. Run <code><a href="/docs/linux/man/1-testparm/">testparm</a></code>(1) to check the default on your system. </p>
<p> <i>No default</i></dl>
<p> enable core files (G) </p>
<dl>
<dd>This parameter specifies whether core dumps should be written on internal exits. Normally set to <code>yes</code>. You should never need to change this. </p>
<p> Default: <i>enable core files</i><i> = </i><i>yes</i><i> </i> </p>
<p> Example: <i>enable core files</i><i> = </i><i>no</i><i> </i></dl>
<p> interfaces (G) </p>
<dl>
<dd>This option allows you to override the default network interfaces list that Samba will use for browsing, name registration and other NetBIOS over TCP/IP (NBT) traffic. By default Samba will query the kernel for the list of all active interfaces and use any interfaces except 127.0.0.1 that are broadcast capable. </p>
<p> The option takes a list of interface strings. Each string can be in any of the following forms: </p>
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
<p> The example below configures three network interfaces corresponding to the eth0 device and IP addresses 192.168.2.10 and 192.168.3.10. The netmasks of the latter two interfaces would be set to 255.255.255.0. </p>
<p> Default: <i>interfaces</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>interfaces</i><i> = </i><i>eth0 192.168.2.10/24 192.168.3.10/255.255.255.0</i><i> </i> </p>
<p> multicast dns register (G) </p>
<dl>
<dd>If compiled with proper support for it, Samba will announce itself with multicast DNS services like for example provided by the Avahi daemon. </p>
<p> This parameter allows disabling Samba to register itself. </p>
<p> Default: <i>multicast dns register</i><i> = </i><i>yes</i><i> </i></dl>
<p> netbios aliases (G) </p>
<dl>
<dd>This is a list of NetBIOS names that nmbd will advertise as additional names by which the Samba server is known. This allows one machine to appear in browse lists under multiple names. If a machine is acting as a browse server or logon server none of these names will be advertised as either browse server or logon servers, only the primary name of the machine will be advertised with these capabilities. </p>
<p> Default: <i>netbios aliases</i><i> = </i><i> # empty string (no additional names)</i><i> </i> </p>
<p> Example: <i>netbios aliases</i><i> = </i><i>TEST TEST1 TEST2</i><i> </i></dl>
<p> netbios name (G) </p>
<dl>
<dd>This sets the NetBIOS name by which a Samba server is known. By default it is the same as the first component of the host&#8217;s DNS name. If a machine is a browse server or logon server this name (or the first component of the hosts DNS name) will be the name that these services are advertised under. </p>
<p> There is a bug in Samba-3 that breaks operation of browsing and access to shares if the netbios name is set to the literal name PIPE. To avoid this problem, do not name your Samba-3 server PIPE. </p>
<p> Default: <i>netbios name</i><i> = </i><i> # machine DNS name</i><i> </i> </p>
<p> Example: <i>netbios name</i><i> = </i><i>MYNAME</i><i> </i></dl>
<p> netbios scope (G) </p>
<dl>
<dd>This sets the NetBIOS scope that Samba will operate under. This should not be set unless every machine on your LAN also sets this value. </p>
<p> Default: <i>netbios scope</i><i> = </i><i></i><i> </i></dl>
<p> directory </p>
<dl>
<dd>This parameter is a synonym for path.</dl>
<p> path (S) </p>
<dl>
<dd>This parameter specifies a directory to which the user of the service is to be given access. In the case of printable services, this is where print data will spool prior to being submitted to the host for printing. </p>
<p> For a printable service offering guest access, the service should be readonly and the path should be world-writeable and have the sticky bit set. This is not mandatory of course, but you probably won&#8217;t get the results you expect if you do otherwise. </p>
<p> Any occurrences of <i>%u</i> in the path will be replaced with the UNIX username that the client is using on this connection. Any occurrences of <i>%m</i> will be replaced by the NetBIOS name of the machine they are connecting from. These replacements are very useful for setting up pseudo home directories for users. </p>
<p> Note that this path will be based on m[blue]<code>root dir</code>m[] if one was specified. </p>
<p> Default: <i>path</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>path</i><i> = </i><i>/home/fred</i><i> </i></dl>
<p> realm (G) </p>
<dl>
<dd>This option specifies the kerberos realm to use. The realm is used as the ADS equivalent of the NT4 domain. It is usually set to the DNS name of the kerberos server. </p>
<p> Default: <i>realm</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>realm</i><i> = </i><i>mysambabox.mycompany.com</i><i> </i></dl>
<p> server services (G) </p>
<dl>
<dd>This option contains the services that the Samba daemon will run. </p>
<p> An entry in the smb.conf file can either override the previous value completely or entries can be removed from or added to it by prefixing them with <code>+</code> or <code>&#8211;</code>. </p>
<p> Default: <i>server services</i><i> = </i><i>s3fs rpc nbt wrepl ldap cldap kdc drepl winbind ntp_signd kcc dnsupdate dns</i><i> </i> </p>
<p> Example: <i>server services</i><i> = </i><i>-s3fs +smb</i><i> </i></dl>
<p> server string (G) </p>
<dl>
<dd>This controls what string will show up in the printer comment box in print manager and next to the IPC connection in net view. It can be any string that you wish to show to your users. </p>
<p> It also sets what will appear in browse lists next to the machine name. </p>
<p> A <i>%v</i> will be replaced with the Samba version number. </p>
<p> A <i>%h</i> will be replaced with the hostname. </p>
<p> Default: <i>server string</i><i> = </i><i>Samba %v</i><i> </i> </p>
<p> Example: <i>server string</i><i> = </i><i>University of GNUs Samba Server</i><i> </i></dl>
<p> share backend (G) </p>
<dl>
<dd>This option specifies the backend that will be used to access the configuration of file shares. </p>
<p> Traditionally, Samba file shares have been configured in the <code>smb.conf</code> file and this is still the default. </p>
<p> At the moment there are no other supported backends. </p>
<p> Default: <i>share backend</i><i> = </i><i>classic</i><i> </i></dl>
<p> unix charset (G) </p>
<dl>
<dd>Specifies the charset the unix machine Samba runs on uses. Samba needs to know this in order to be able to convert text to the charsets other SMB clients use. </p>
<p> This is also the charset Samba will use when specifying arguments to scripts that it invokes. </p>
<p> Default: <i>unix charset</i><i> = </i><i>UTF8</i><i> </i> </p>
<p> Example: <i>unix charset</i><i> = </i><i>ASCII</i><i> </i></dl>
<p> workgroup (G) </p>
<dl>
<dd>This controls what workgroup your server will appear to be in when queried by clients. Note that this parameter also controls the Domain name used with the m[blue]<code>security = domain</code>m[] setting. </p>
<p> Default: <i>workgroup</i><i> = </i><i>WORKGROUP</i><i> </i> </p>
<p> Example: <i>workgroup</i><i> = </i><i>MYGROUP</i><i> </i></dl>
<p> administrative share (S) </p>
<dl>
<dd>If this parameter is set to <code>yes</code> for a share, then the share will be an administrative share. The Administrative Shares are the default network shares created by all Windows NT-based operating systems. These are shares like C$, D$ or ADMIN$. The type of these shares is STYPE_DISKTREE_HIDDEN. </p>
<p> See the section below on m[blue]<code>security</code>m[] for more information about this option. </p>
<p> Default: <i>administrative share</i><i> = </i><i>no</i><i> </i></dl>
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
<p> domain master (G) </p>
<dl>
<dd>Tell <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) to enable WAN-wide browse list collation. Setting this option causes nmbd to claim a special domain specific NetBIOS name that identifies it as a domain master browser for its given m[blue]<code>workgroup</code>m[]. Local master browsers in the same m[blue]<code>workgroup</code>m[] on broadcast-isolated subnets will give this nmbd their local browse lists, and then ask <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) for a complete copy of the browse list for the whole wide area network. Browser clients will then contact their local master browser, and will receive the domain-wide browse list, instead of just the list for their broadcast-isolated subnet. </p>
<p> Note that Windows NT Primary Domain Controllers expect to be able to claim this m[blue]<code>workgroup</code>m[] specific special NetBIOS name that identifies them as domain master browsers for that m[blue]<code>workgroup</code>m[] by default (i.e. there is no way to prevent a Windows NT PDC from attempting to do this). This means that if this parameter is set and nmbd claims the special name for a m[blue]<code>workgroup</code>m[] before a Windows NT PDC is able to do so then cross subnet browsing will behave strangely and may fail. </p>
<p> If m[blue]<code>domain logons = yes</code>m[], then the default behavior is to enable the m[blue]<code>domain master</code>m[] parameter. If m[blue]<code>domain logons</code>m[] is not enabled (the default setting), then neither will m[blue]<code>domain master</code>m[] be enabled by default. </p>
<p> When m[blue]<code>domain logons = Yes</code>m[] the default setting for this parameter is Yes, with the result that Samba will be a PDC. If m[blue]<code>domain master = No</code>m[], Samba will function as a BDC. In general, this parameter should be set to &#8216;No&#8217; only on a BDC. </p>
<p> Default: <i>domain master</i><i> = </i><i>auto</i><i> </i></dl>
<p> enhanced browsing (G) </p>
<dl>
<dd>This option enables a couple of enhancements to cross-subnet browse propagation that have been added in Samba but which are not standard in Microsoft implementations. </p>
<p> The first enhancement to browse propagation consists of a regular wildcard query to a Samba WINS server for all Domain Master Browsers, followed by a browse synchronization with each of the returned DMBs. The second enhancement consists of a regular randomised browse synchronization with all currently known DMBs. </p>
<p> You may wish to disable this option if you have a problem with empty workgroups not disappearing from browse lists. Due to the restrictions of the browse protocols, these enhancements can cause a empty workgroup to stay around forever which can be annoying. </p>
<p> In general you should leave this option enabled as it makes cross-subnet browse propagation much more reliable. </p>
<p> Default: <i>enhanced browsing</i><i> = </i><i>yes</i><i> </i></dl>
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
<p> local master (G) </p>
<dl>
<dd>This option allows <code><a href="/docs/linux/man/8-nmbd/">nmbd</a></code>(8) to try and become a local master browser on a subnet. If set to <code>no</code> then nmbd will not attempt to become a local master browser on a subnet and will also lose in all browsing elections. By default this value is set to <code>yes</code>. Setting this value to <code>yes</code> doesn&#8217;t mean that Samba will <i>become</i> the local master browser on a subnet, just that nmbd will <i>participate</i> in elections for local master browser. </p>
<p> Setting this value to <code>no</code> will cause nmbd<i>never</i> to become a local master browser. </p>
<p> Default: <i>local master</i><i> = </i><i>yes</i><i> </i></dl>
<p> os level (G) </p>
<dl>
<dd>This integer value controls what level Samba advertises itself as for browse elections. The value of this parameter determines whether <code><a href="/docs/linux/man/8-nmbd/">nmbd</a></code>(8) has a chance of becoming a local master browser for the m[blue]<code>workgroup</code>m[] in the local broadcast area. </p>
<p> <i> Note:</i> By default, Samba will win a local master browsing election over all Microsoft operating systems except a Windows NT 4.0/2000 Domain Controller. This means that a misconfigured Samba host can effectively isolate a subnet for browsing purposes. This parameter is largely auto-configured in the Samba-3 release series and it is seldom necessary to manually override the default setting. Please refer to the chapter on Network Browsing in the Samba-3 HOWTO document for further information regarding the use of this parameter. <i>Note:</i> The maximum value for this parameter is 255. If you use higher values, counting will start at 0! </p>
<p> Default: <i>os level</i><i> = </i><i>20</i><i> </i> </p>
<p> Example: <i>os level</i><i> = </i><i>65</i><i> </i></dl>
<p> prefered master </p>
<dl>
<dd>This parameter is a synonym for preferred master.</dl>
<p> preferred master (G) </p>
<dl>
<dd>This boolean parameter controls if <code><a href="/docs/linux/man/8-nmbd/">nmbd</a></code>(8) is a preferred master browser for its workgroup. </p>
<p> If this is set to <code>yes</code>, on startup, nmbd will force an election, and it will have a slight advantage in winning the election. It is recommended that this parameter is used in conjunction with m[blue]<code>domain master = yes</code>m[], so that nmbd can guarantee becoming a domain master. </p>
<p> Use this option with caution, because if there are several hosts (whether Samba servers, Windows 95 or NT) that are preferred master browsers on the same subnet, they will each periodically and continuously attempt to become the local master browser. This will result in unnecessary broadcast traffic and reduced browsing capabilities. </p>
<p> Default: <i>preferred master</i><i> = </i><i>auto</i><i> </i></dl>
<p> allow dns updates (G) </p>
<dl>
<dd>This option determines what kind of updates to the DNS are allowed. </p>
<p> DNS updates can either be disallowed completely by setting it to <code>disabled</code>, enabled over secure connections only by setting it to <code>secure only</code> or allowed in all cases by setting it to <code>nonsecure</code>. </p>
<p> Default: <i>allow dns updates</i><i> = </i><i>secure only</i><i> </i> </p>
<p> Example: <i>allow dns updates</i><i> = </i><i>disabled</i><i> </i></dl>
<p> dns forwarder (G) </p>
<dl>
<dd>This option specifies the DNS server that DNS requests will be forwarded to if they can not be handled by Samba itself. </p>
<p> The DNS forwarder is only used if the internal DNS server in Samba is used. </p>
<p> Default: <i>dns forwarder</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>dns forwarder</i><i> = </i><i>192.168.0.1</i><i> </i></dl>
<p> dns update command (G) </p>
<dl>
<dd>This option sets the command that is called when there are DNS updates. It should update the local machines DNS names using TSIG-GSS. </p>
<p> Default: <i>dns update command</i><i> = </i><i>$prefix/sbin/samba_dnsupdate</i><i> </i> </p>
<p> Example: <i>dns update command</i><i> = </i><i>/usr/local/sbin/dnsupdate</i><i> </i></dl>
<p> machine password timeout (G) </p>
<dl>
<dd>If a Samba server is a member of a Windows NT Domain (see the m[blue]<code>security = domain</code>m[] parameter) then periodically a running smbd process will try and change the MACHINE ACCOUNT PASSWORD stored in the TDB called private/secrets.tdb (or private/secrets.ntdb). This parameter specifies how often this password will be changed, in seconds. The default is one week (expressed in seconds), the same as a Windows NT Domain member server. </p>
<p> See also <code><a href="/docs/linux/man/8-smbpasswd/">smbpasswd</a></code>(8), and the m[blue]<code>security = domain</code>m[] parameter. </p>
<p> Default: <i>machine password timeout</i><i> = </i><i>604800</i><i> </i></dl>
<p> nsupdate command (G) </p>
<dl>
<dd>This option sets the path to the nsupdate command which is used for GSS-TSIG dynamic DNS updates. </p>
<p> Default: <i>nsupdate command</i><i> = </i><i>$prefix/sbin/nsupdate -g</i><i> </i></dl>
<p> rndc command (G) </p>
<dl>
<dd>This option specifies the path to the name server control utility. </p>
<p> The rndc utility should be a part of the bind installation. </p>
<p> Default: <i>rndc command</i><i> = </i><i>/usr/sbin/rndc</i><i> </i> </p>
<p> Example: <i>rndc command</i><i> = </i><i>/usr/local/bind9/sbin/rndc</i><i> </i></dl>
<p> spn update command (G) </p>
<dl>
<dd>This option sets the command that for updating servicePrincipalName names from spn_update_list. </p>
<p> Default: <i>spn update command</i><i> = </i><i>$prefix/sbin/samba_spnupdate</i><i> </i> </p>
<p> Example: <i>spn update command</i><i> = </i><i>/usr/local/sbin/spnupdate</i><i> </i></dl>
<p> casesignames </p>
<dl>
<dd>This parameter is a synonym for case sensitive.</dl>
<p> case sensitive (S) </p>
<dl>
<dd>See the discussion in the section m[blue]<code>name mangling</code>m[]. </p>
<p> Default: <i>case sensitive</i><i> = </i><i>auto</i><i> </i></dl>
<p> default case (S) </p>
<dl>
<dd>See the section on m[blue]<code>name mangling</code>m[]. Also note the m[blue]<code>short preserve case</code>m[] parameter. </p>
<p> Default: <i>default case</i><i> = </i><i>lower</i><i> </i></dl>
<p> delete veto files (S) </p>
<dl>
<dd>This option is used when Samba is attempting to delete a directory that contains one or more vetoed directories (see the m[blue]<code>veto files</code>m[] option). If this option is set to <code>no</code> (the default) then if a vetoed directory contains any non-vetoed files or directories then the directory delete will fail. This is usually what you want. </p>
<p> If this option is set to <code>yes</code>, then Samba will attempt to recursively delete any files and directories within the vetoed directory. This can be useful for integration with file serving systems such as NetAtalk which create meta-files within directories you might normally veto DOS/Windows users from seeing (e.g. .AppleDouble) </p>
<p> Setting m[blue]<code>delete veto files = yes</code>m[] allows these directories to be transparently deleted when the parent directory is deleted (so long as the user has permissions to do so). </p>
<p> Default: <i>delete veto files</i><i> = </i><i>no</i><i> </i></dl>
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
<p> hide special files (S) </p>
<dl>
<dd>This parameter prevents clients from seeing special files such as sockets, devices and fifo&#8217;s in directory listings. </p>
<p> Default: <i>hide special files</i><i> = </i><i>no</i><i> </i></dl>
<p> hide unreadable (S) </p>
<dl>
<dd>This parameter prevents clients from seeing the existance of files that cannot be read. Defaults to off. </p>
<p> Please note that enabling this can slow down listing large directories significantly. Samba has to evaluate the ACLs of all directory members, which can be a lot of effort. </p>
<p> Default: <i>hide unreadable</i><i> = </i><i>no</i><i> </i></dl>
<p> hide unwriteable files (S) </p>
<dl>
<dd>This parameter prevents clients from seeing the existance of files that cannot be written to. Defaults to off. Note that unwriteable directories are shown as usual. </p>
<p> Please note that enabling this can slow down listing large directories significantly. Samba has to evaluate the ACLs of all directory members, which can be a lot of effort. </p>
<p> Default: <i>hide unwriteable files</i><i> = </i><i>no</i><i> </i></dl>
<p> mangled names (S) </p>
<dl>
<dd>This controls whether non-DOS names under UNIX should be mapped to DOS-compatible names (&quot;mangled&quot;) and made visible, or whether non-DOS names should simply be ignored. </p>
<p> See the section on m[blue]<code>name mangling</code>m[] for details on how to control the mangling process. </p>
<p> If mangling is used then the mangling method is as follows: </p>
<dl>
<dd>&bull; The first (up to) five alphanumeric characters before the rightmost dot of the filename are preserved, forced to upper case, and appear as the first (up to) five characters of the mangled name.</dl>
<dl>
<dd>&bull; A tilde &quot;~&quot; is appended to the first part of the mangled name, followed by a two-character unique sequence, based on the original root name (i.e., the original filename minus its final extension). The final extension is included in the hash calculation only if it contains any upper case characters or is longer than three characters. </p>
<p> Note that the character to use may be specified using the m[blue]<code>mangling char</code>m[] option, if you don&#8217;t like &#8216;~&#8217;.</dl>
<dl>
<dd>&bull; Files whose UNIX name begins with a dot will be presented as DOS hidden files. The mangled name will be created as for other filenames, but with the leading dot removed and &quot;___&quot; as its extension regardless of actual original extension (that&#8217;s three underscores).</dl>
</dl>
<p> The two-digit hash value consists of upper case alphanumeric characters. </p>
<p> This algorithm can cause name collisions only if files in a directory share the same first five alphanumeric characters. The probability of such a clash is 1/1300. </p>
<p> The name mangling (if enabled) allows a file to be copied between UNIX directories from Windows/DOS while retaining the long UNIX filename. UNIX files can be renamed to a new extension from Windows/DOS and will retain the same basename. Mangled names do not change between sessions. </p>
<p> Default: <i>mangled names</i><i> = </i><i>yes</i><i> </i> </p>
<p> mangle prefix (G) </p>
<dl>
<dd>controls the number of prefix characters from the original name used when generating the mangled names. A larger value will give a weaker hash and therefore more name collisions. The minimum value is 1 and the maximum value is 6. </p>
<p> mangle prefix is effective only when mangling method is hash2. </p>
<p> Default: <i>mangle prefix</i><i> = </i><i>1</i><i> </i> </p>
<p> Example: <i>mangle prefix</i><i> = </i><i>4</i><i> </i></dl>
<p> mangling char (S) </p>
<dl>
<dd>This controls what character is used as the <i>magic</i> character in m[blue]<code>name mangling</code>m[]. The default is a &#8216;~&#8217; but this may interfere with some software. Use this option to set it to whatever you prefer. This is effective only when mangling method is hash. </p>
<p> Default: <i>mangling char</i><i> = </i><i>~</i><i> </i> </p>
<p> Example: <i>mangling char</i><i> = </i><i>^</i><i> </i></dl>
<p> mangling method (G) </p>
<dl>
<dd>controls the algorithm used for the generating the mangled names. Can take two different values, &quot;hash&quot; and &quot;hash2&quot;. &quot;hash&quot; is the algorithm that was used in Samba for many years and was the default in Samba 2.2.x &quot;hash2&quot; is now the default and is newer and considered a better algorithm (generates less collisions) in the names. Many Win32 applications store the mangled names and so changing to algorithms must not be done lightly as these applications may break unless reinstalled. </p>
<p> Default: <i>mangling method</i><i> = </i><i>hash2</i><i> </i> </p>
<p> Example: <i>mangling method</i><i> = </i><i>hash</i><i> </i></dl>
<p> map archive (S) </p>
<dl>
<dd>This controls whether the DOS archive attribute should be mapped to the UNIX owner execute bit. The DOS archive bit is set when a file has been modified since its last backup. One motivation for this option is to keep Samba/your PC from making any file it touches from becoming executable under UNIX. This can be quite annoying for shared source code, documents, etc&#8230; </p>
<p> Note that this parameter will be ignored if the m[blue]<code>store dos attributes</code>m[] parameter is set, as the DOS archive attribute will then be stored inside a UNIX extended attribute. </p>
<p> Note that this requires the m[blue]<code>create mask</code>m[] parameter to be set such that owner execute bit is not masked out (i.e. it must include 100). See the parameter m[blue]<code>create mask</code>m[] for details. </p>
<p> Default: <i>map archive</i><i> = </i><i>yes</i><i> </i></dl>
<p> map hidden (S) </p>
<dl>
<dd>This controls whether DOS style hidden files should be mapped to the UNIX world execute bit. </p>
<p> Note that this parameter will be ignored if the m[blue]<code>store dos attributes</code>m[] parameter is set, as the DOS hidden attribute will then be stored inside a UNIX extended attribute. </p>
<p> Note that this requires the m[blue]<code>create mask</code>m[] to be set such that the world execute bit is not masked out (i.e. it must include 001). See the parameter m[blue]<code>create mask</code>m[] for details. </p>
<p> <i>No default</i></dl>
<p> map readonly (S) </p>
<dl>
<dd>This controls how the DOS read only attribute should be mapped from a UNIX filesystem. </p>
<p> This parameter can take three different values, which tell <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) how to display the read only attribute on files, where either m[blue]<code>store dos attributes</code>m[] is set to <code>No</code>, or no extended attribute is present. If m[blue]<code>store dos attributes</code>m[] is set to <code>yes</code> then this parameter is <i>ignored</i>. This is a new parameter introduced in Samba version 3.0.21. </p>
<p> The three settings are : </p>
<dl>
<dd>&bull; <code>Yes</code> &#8211; The read only DOS attribute is mapped to the inverse of the user or owner write bit in the unix permission mode set. If the owner write bit is not set, the read only attribute is reported as being set on the file. If the read only DOS attribute is set, Samba sets the owner, group and others write bits to zero. Write bits set in an ACL are ignored by Samba. If the read only DOS attribute is unset, Samba simply sets the write bit of the owner to one.</dl>
<dl>
<dd>&bull; <code>Permissions</code> &#8211; The read only DOS attribute is mapped to the effective permissions of the connecting user, as evaluated by <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) by reading the unix permissions and POSIX ACL (if present). If the connecting user does not have permission to modify the file, the read only attribute is reported as being set on the file.</dl>
<dl>
<dd>&bull; <code>No</code> &#8211; The read only DOS attribute is unaffected by permissions, and can only be set by the m[blue]<code>store dos attributes</code>m[] method. This may be useful for exporting mounted CDs.</dl>
</dl>
<p> Note that this parameter will be ignored if the m[blue]<code>store dos attributes</code>m[] parameter is set, as the DOS &#8216;read-only&#8217; attribute will then be stored inside a UNIX extended attribute. </p>
<p> Default: <i>map readonly</i><i> = </i><i>yes</i><i> </i> </p>
<p> map system (S) </p>
<dl>
<dd>This controls whether DOS style system files should be mapped to the UNIX group execute bit. </p>
<p> Note that this parameter will be ignored if the m[blue]<code>store dos attributes</code>m[] parameter is set, as the DOS system attribute will then be stored inside a UNIX extended attribute. </p>
<p> Note that this requires the m[blue]<code>create mask</code>m[] to be set such that the group execute bit is not masked out (i.e. it must include 010). See the parameter m[blue]<code>create mask</code>m[] for details. </p>
<p> Default: <i>map system</i><i> = </i><i>no</i><i> </i></dl>
<p> max stat cache size (G) </p>
<dl>
<dd>This parameter limits the size in memory of any <i>stat cache</i> being used to speed up case insensitive name mappings. It represents the number of kilobyte (1024) units the stat cache can use. A value of zero, meaning unlimited, is not advisable due to increased memory usage. You should not need to change this parameter. </p>
<p> Default: <i>max stat cache size</i><i> = </i><i>256</i><i> </i> </p>
<p> Example: <i>max stat cache size</i><i> = </i><i>100</i><i> </i></dl>
<p> preserve case (S) </p>
<dl>
<dd>This controls if new filenames are created with the case that the client passes, or if they are forced to be the m[blue]<code>default case</code>m[]. </p>
<p> See the section on NAME MANGLING for a fuller discussion. </p>
<p> Default: <i>preserve case</i><i> = </i><i>yes</i><i> </i></dl>
<p> short preserve case (S) </p>
<dl>
<dd>This boolean parameter controls if new files which conform to 8.3 syntax, that is all in upper case and of suitable length, are created upper case, or if they are forced to be the m[blue]<code>default case</code>m[]. This option can be use with m[blue]<code>preserve case = yes</code>m[] to permit long filenames to retain their case, while short names are lowered. </p>
<p> See the section on NAME MANGLING. </p>
<p> Default: <i>short preserve case</i><i> = </i><i>yes</i><i> </i></dl>
<p> stat cache (G) </p>
<dl>
<dd>This parameter determines if <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) will use a cache in order to speed up case insensitive name mappings. You should never need to change this parameter. </p>
<p> Default: <i>stat cache</i><i> = </i><i>yes</i><i> </i></dl>
<p> store dos attributes (S) </p>
<dl>
<dd>If this parameter is set Samba attempts to first read DOS attributes (SYSTEM, HIDDEN, ARCHIVE or READ-ONLY) from a filesystem extended attribute, before mapping DOS attributes to UNIX permission bits (such as occurs with m[blue]<code>map hidden</code>m[] and m[blue]<code>map readonly</code>m[]). When set, DOS attributes will be stored onto an extended attribute in the UNIX filesystem, associated with the file or directory. When this parameter is set it will override the parameters m[blue]<code>map hidden</code>m[], m[blue]<code>map system</code>m[], m[blue]<code>map archive</code>m[] and m[blue]<code>map readonly</code>m[] and they will behave as if they were set to off. This parameter writes the DOS attributes as a string into the extended attribute named &quot;user.DOSATTRIB&quot;. This extended attribute is explicitly hidden from smbd clients requesting an EA list. On Linux the filesystem must have been mounted with the mount option user_xattr in order for extended attributes to work, also extended attributes must be compiled into the Linux kernel. In Samba 3.5.0 and above the &quot;user.DOSATTRIB&quot; extended attribute has been extended to store the create time for a file as well as the DOS attributes. This is done in a backwards compatible way so files created by Samba 3.5.0 and above can still have the DOS attribute read from this extended attribute by earlier versions of Samba, but they will not be able to read the create time stored there. Storing the create time separately from the normal filesystem meta-data allows Samba to faithfully reproduce NTFS semantics on top of a POSIX filesystem. </p>
<p> Default: <i>store dos attributes</i><i> = </i><i>no</i><i> </i></dl>
<p> veto files (S) </p>
<dl>
<dd>This is a list of files and directories that are neither visible nor accessible. Each entry in the list must be separated by a &#8216;/&#8217;, which allows spaces to be included in the entry. &#8216;*&#8217; and &#8216;?&#8217; can be used to specify multiple files or directories as in DOS wildcards. </p>
<p> Each entry must be a unix path, not a DOS path and must <i>not</i> include the unix directory separator &#8216;/&#8217;. </p>
<p> Note that the m[blue]<code>case sensitive</code>m[] option is applicable in vetoing files. </p>
<p> One feature of the veto files parameter that it is important to be aware of is Samba&#8217;s behaviour when trying to delete a directory. If a directory that is to be deleted contains nothing but veto files this deletion will <i>fail</i> unless you also set the m[blue]<code>delete veto files</code>m[] parameter to <i>yes</i>. </p>
<p> Setting this parameter will affect the performance of Samba, as it will be forced to check all files and directories for a match as they are scanned. </p>
<p> Examples of use include: </p>
<dl>
<dd>
<pre>; Veto any files containing the word Security,
; any ending in .tmp, and any directory containing the
; word root.
veto files = /*Security*/*.tmp/*root*/
; Veto the Apple specific files that a NetAtalk server
; creates.
veto files = /.AppleDouble/.bin/.AppleDesktop/Network Trash Folder/</pre>
</dl>
<p> Default: <i>veto files</i><i> = </i><i>No files or directories are vetoed.</i><i> </i></dl>
<p> veto oplock files (S) </p>
<dl>
<dd>This parameter is only valid when the m[blue]<code>oplocks</code>m[] parameter is turned on for a share. It allows the Samba administrator to selectively turn off the granting of oplocks on selected files that match a wildcarded list, similar to the wildcarded list used in the m[blue]<code>veto files</code>m[] parameter. </p>
<p> You might want to do this on files that you know will be heavily contended for by clients. A good example of this is in the NetBench SMB benchmark program, which causes heavy client contention for files ending in .SEM. To cause Samba not to grant oplocks on these files you would use the line (either in the [global] section or in the section for the particular NetBench share. </p>
<p> An example of use is: </p>
<dl>
<dd>
<pre>veto oplock files = /.*SEM/</pre>
</dl>
<p> Default: <i>veto oplock files</i><i> = </i><i> # No files are vetoed for oplock grants</i><i> </i></dl>
<p> client ldap sasl wrapping (G) </p>
<dl>
<dd>The m[blue]<code>client ldap sasl wrapping</code>m[] defines whether ldap traffic will be signed or signed and encrypted (sealed). Possible values are <i>plain</i>, <i>sign</i> and <i>seal</i>. </p>
<p> The values <i>sign</i> and <i>seal</i> are only available if Samba has been compiled against a modern OpenLDAP version (2.3.x or higher). </p>
<p> This option is needed in the case of Domain Controllers enforcing the usage of signed LDAP connections (e.g. Windows 2000 SP3 or higher). LDAP sign and seal can be controlled with the registry key &quot;HKLM\System\CurrentControlSet\Services\NTDS\Parameters\LDAPServerIntegrity&quot; on the Windows server side. </p>
<p> Depending on the used KRB5 library (MIT and older Heimdal versions) it is possible that the message &quot;integrity only&quot; is not supported. In this case, <i>sign</i> is just an alias for <i>seal</i>. </p>
<p> The default value is <i>plain</i> which is not irritable to KRB5 clock skew errors. That implies synchronizing the time with the KDC in the case of using <i>sign</i> or <i>seal</i>. </p>
<p> Default: <i>client ldap sasl wrapping</i><i> = </i><i>plain</i><i> </i></dl>
<p> ldap admin dn (G) </p>
<dl>
<dd>The m[blue]<code>ldap admin dn</code>m[] defines the Distinguished Name (DN) name used by Samba to contact the ldap server when retreiving user account information. The m[blue]<code>ldap admin dn</code>m[] is used in conjunction with the admin dn password stored in the private/secrets.tdb (or private/secrets.ntdb) file. See the <code><a href="/docs/linux/man/8-smbpasswd/">smbpasswd</a></code>(8) man page for more information on how to accomplish this. </p>
<p> The m[blue]<code>ldap admin dn</code>m[] requires a fully specified DN. The m[blue]<code>ldap suffix</code>m[] is not appended to the m[blue]<code>ldap admin dn</code>m[]. </p>
<p> <i>No default</i></dl>
<p> ldap connection timeout (G) </p>
<dl>
<dd>This parameter tells the LDAP library calls which timeout in seconds they should honor during initial connection establishments to LDAP servers. It is very useful in failover scenarios in particular. If one or more LDAP servers are not reachable at all, we do not have to wait until TCP timeouts are over. This feature must be supported by your LDAP library. </p>
<p> This parameter is different from m[blue]<code>ldap timeout</code>m[] which affects operations on LDAP servers using an existing connection and not establishing an initial connection. </p>
<p> Default: <i>ldap connection timeout</i><i> = </i><i>2</i><i> </i></dl>
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
<p> ldap page size (G) </p>
<dl>
<dd>This parameter specifies the number of entries per page. </p>
<p> If the LDAP server supports paged results, clients can request subsets of search results (pages) instead of the entire list. This parameter specifies the size of these pages. </p>
<p> Default: <i>ldap page size</i><i> = </i><i>1024</i><i> </i> </p>
<p> Example: <i>ldap page size</i><i> = </i><i>512</i><i> </i></dl>
<p> ldap password sync </p>
<dl>
<dd>This parameter is a synonym for ldap passwd sync.</dl>
<p> ldap passwd sync (G) </p>
<dl>
<dd>This option is used to define whether or not Samba should sync the LDAP password with the NT and LM hashes for normal accounts (NOT for workstation, server or domain trusts) on a password change via SAMBA. </p>
<p> The m[blue]<code>ldap passwd sync</code>m[] can be set to one of three values: </p>
<dl>
<dd>&bull; <i>Yes</i> = Try to update the LDAP, NT and LM passwords and update the pwdLastSet time.</dl>
<dl>
<dd>&bull; <i>No</i> = Update NT and LM passwords and update the pwdLastSet time.</dl>
<dl>
<dd>&bull; <i>Only</i> = Only update the LDAP password and let the LDAP server do the rest.</dl>
</dl>
<p> Default: <i>ldap passwd sync</i><i> = </i><i>no</i><i> </i> </p>
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
<p> ldap ssl (G) </p>
<dl>
<dd>This option is used to define whether or not Samba should use SSL when connecting to the ldap server This is <i>NOT</i> related to Samba&#8217;s previous SSL support which was enabled by specifying the &#8211;with-ssl option to the configure script. </p>
<p> LDAP connections should be secured where possible. This may be done setting <i>either</i> this parameter to <i>Start_tls</i><i>or</i> by specifying <i>ldaps://</i> in the URL argument of m[blue]<code>passdb backend</code>m[]. </p>
<p> The m[blue]<code>ldap ssl</code>m[] can be set to one of two values: </p>
<dl>
<dd>&bull; <i>Off</i> = Never use SSL when querying the directory.</dl>
<dl>
<dd>&bull; <i>start tls</i> = Use the LDAPv3 StartTLS extended operation (RFC2830) for communicating with the directory server.</dl>
</dl>
<p> Please note that this parameter does only affect <i>rpc</i> methods. To enable the LDAPv3 StartTLS extended operation (RFC2830) for <i>ads</i>, set m[blue]<code>ldap ssl = yes</code>m[]<i>and</i>m[blue]<code>ldap ssl ads = yes</code>m[]. See <a href="/docs/linux/man/5-smb-conf/">smb.conf</a>(5) for more information on m[blue]<code>ldap ssl ads</code>m[]. </p>
<p> Default: <i>ldap ssl</i><i> = </i><i>start tls</i><i> </i> </p>
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
<p> blocking locks (S) </p>
<dl>
<dd>This parameter controls the behavior of <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) when given a request by a client to obtain a byte range lock on a region of an open file, and the request has a time limit associated with it. </p>
<p> If this parameter is set and the lock range requested cannot be immediately satisfied, samba will internally queue the lock request, and periodically attempt to obtain the lock until the timeout period expires. </p>
<p> If this parameter is set to <code>no</code>, then samba will behave as previous versions of Samba would and will fail the lock request immediately if the lock range cannot be obtained. </p>
<p> Default: <i>blocking locks</i><i> = </i><i>yes</i><i> </i></dl>
<p> csc policy (S) </p>
<dl>
<dd>This stands for <i>client-side caching policy</i>, and specifies how clients capable of offline caching will cache the files in the share. The valid values are: manual, documents, programs, disable. </p>
<p> These values correspond to those used on Windows servers. </p>
<p> For example, shares containing roaming profiles can have offline caching disabled using m[blue]<code>csc policy = disable</code>m[]. </p>
<p> Default: <i>csc policy</i><i> = </i><i>manual</i><i> </i> </p>
<p> Example: <i>csc policy</i><i> = </i><i>programs</i><i> </i></dl>
<p> fake oplocks (S) </p>
<dl>
<dd>Oplocks are the way that SMB clients get permission from a server to locally cache file operations. If a server grants an oplock (opportunistic lock) then the client is free to assume that it is the only one accessing the file and it will aggressively cache file data. With some oplock types the client may even cache file open/close operations. This can give enormous performance benefits. </p>
<p> When you set fake oplocks = yes, <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) will always grant oplock requests no matter how many clients are using the file. </p>
<p> It is generally much better to use the real m[blue]<code>oplocks</code>m[] support rather than this parameter. </p>
<p> If you enable this option on all read-only shares or shares that you know will only be accessed from one client at a time such as physically read-only media like CDROMs, you will see a big performance improvement on many operations. If you enable this option on shares where multiple clients may be accessing the files read-write at the same time you can get data corruption. Use this option carefully! </p>
<p> Default: <i>fake oplocks</i><i> = </i><i>no</i><i> </i></dl>
<p> kernel oplocks (S) </p>
<dl>
<dd>For UNIXes that support kernel based m[blue]<code>oplocks</code>m[] (currently only IRIX and the Linux 2.4 kernel), this parameter allows the use of them to be turned on or off. However, this disables Level II oplocks for clients as the Linux and IRIX kernels do not support them properly. </p>
<p> Kernel oplocks support allows Samba <i>oplocks </i> to be broken whenever a local UNIX process or NFS operation accesses a file that <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) has oplocked. This allows complete data consistency between SMB/CIFS, NFS and local file access (and is a <i>very</i> cool feature :-). </p>
<p> If you do not need this interaction, you should disable the parameter on Linux and IRIX to get Level II oplocks and the associated performance benefit. </p>
<p> This parameter defaults to <code>no</code> and is translated to a no-op on systems that do not have the necessary kernel support. </p>
<p> Default: <i>kernel oplocks</i><i> = </i><i>no</i><i> </i></dl>
<p> kernel share modes (S) </p>
<dl>
<dd>This parameter controls whether SMB share modes are translated into UNIX flocks. </p>
<p> Kernel share modes provide a minimal level of interoperability with local UNIX processes and NFS operations by preventing access with flocks corresponding to the SMB share modes. Generally, it is very desirable to leave this enabled. </p>
<p> Note that in order to use SMB2 durable file handles on a share, you have to turn kernel share modes off. </p>
<p> This parameter defaults to <code>yes</code> and is translated to a no-op on systems that do not have the necessary kernel flock support. </p>
<p> Default: <i>kernel share modes</i><i> = </i><i>yes</i><i> </i></dl>
<p> level2 oplocks (S) </p>
<dl>
<dd>This parameter controls whether Samba supports level2 (read-only) oplocks on a share. </p>
<p> Level2, or read-only oplocks allow Windows NT clients that have an oplock on a file to downgrade from a read-write oplock to a read-only oplock once a second client opens the file (instead of releasing all oplocks on a second open, as in traditional, exclusive oplocks). This allows all openers of the file that support level2 oplocks to cache the file for read-ahead only (ie. they may not cache writes or lock requests) and increases performance for many accesses of files that are not commonly written (such as application .EXE files). </p>
<p> Once one of the clients which have a read-only oplock writes to the file all clients are notified (no reply is needed or waited for) and told to break their oplocks to &quot;none&quot; and delete any read-ahead caches. </p>
<p> It is recommended that this parameter be turned on to speed access to shared executables. </p>
<p> For more discussions on level2 oplocks see the CIFS spec. </p>
<p> Currently, if m[blue]<code>kernel oplocks</code>m[] are supported then level2 oplocks are not granted (even if this parameter is set to <code>yes</code>). Note also, the m[blue]<code>oplocks</code>m[] parameter must be set to <code>yes</code> on this share in order for this parameter to have any effect. </p>
<p> Default: <i>level2 oplocks</i><i> = </i><i>yes</i><i> </i></dl>
<p> locking (S) </p>
<dl>
<dd>This controls whether or not locking will be performed by the server in response to lock requests from the client. </p>
<p> If locking = no, all lock and unlock requests will appear to succeed and all lock queries will report that the file in question is available for locking. </p>
<p> If locking = yes, real locking will be performed by the server. </p>
<p> This option <i>may</i> be useful for read-only filesystems which <i>may</i> not need locking (such as CDROM drives), although setting this parameter of <code>no</code> is not really recommended even in this case. </p>
<p> Be careful about disabling locking either globally or in a specific service, as lack of locking may result in data corruption. You should never need to set this parameter. </p>
<p> <i>No default</i></dl>
<p> lock spin time (G) </p>
<dl>
<dd>The time in milliseconds that smbd should keep waiting to see if a failed lock request can be granted. This parameter has changed in default value from Samba 3.0.23 from 10 to 200. The associated m[blue]<code>lock spin count</code>m[] parameter is no longer used in Samba 3.0.24. You should not need to change the value of this parameter. </p>
<p> Default: <i>lock spin time</i><i> = </i><i>200</i><i> </i></dl>
<p> oplock break wait time (G) </p>
<dl>
<dd>This is a tuning parameter added due to bugs in both Windows 9x and WinNT. If Samba responds to a client too quickly when that client issues an SMB that can cause an oplock break request, then the network client can fail and not respond to the break request. This tuning parameter (which is set in milliseconds) is the amount of time Samba will wait before sending an oplock break request to such (broken) clients. </p>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font><br />
 DO NOT CHANGE THIS PARAMETER UNLESS YOU HAVE READ AND UNDERSTOOD THE SAMBA OPLOCK CODE. </p>
</dl>
<p> Default: <i>oplock break wait time</i><i> = </i><i>0</i><i> </i></dl>
<p> oplock contention limit (S) </p>
<dl>
<dd>This is a <i>very</i> advanced <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) tuning option to improve the efficiency of the granting of oplocks under multiple client contention for the same file. </p>
<p> In brief it specifies a number, which causes <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8)not to grant an oplock even when requested if the approximate number of clients contending for an oplock on the same file goes over this limit. This causes smbd to behave in a similar way to Windows NT. </p>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font><br />
 DO NOT CHANGE THIS PARAMETER UNLESS YOU HAVE READ AND UNDERSTOOD THE SAMBA OPLOCK CODE. </p>
</dl>
<p> Default: <i>oplock contention limit</i><i> = </i><i>2</i><i> </i></dl>
<p> oplocks (S) </p>
<dl>
<dd>This boolean option tells smbd whether to issue oplocks (opportunistic locks) to file open requests on this share. The oplock code can dramatically (approx. 30% or more) improve the speed of access to files on Samba servers. It allows the clients to aggressively cache files locally and you may want to disable this option for unreliable network environments (it is turned on by default in Windows NT Servers). </p>
<p> Oplocks may be selectively turned off on certain files with a share. See the m[blue]<code>veto oplock files</code>m[] parameter. On some systems oplocks are recognized by the underlying operating system. This allows data synchronization between all access to oplocked files, whether it be via Samba or NFS or a local UNIX process. See the m[blue]<code>kernel oplocks</code>m[] parameter for details. </p>
<p> Default: <i>oplocks</i><i> = </i><i>yes</i><i> </i></dl>
<p> posix locking (S) </p>
<dl>
<dd>The <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) daemon maintains an database of file locks obtained by SMB clients. The default behavior is to map this internal database to POSIX locks. This means that file locks obtained by SMB clients are consistent with those seen by POSIX compliant applications accessing the files via a non-SMB method (e.g. NFS or local file access). It is very unlikely that you need to set this parameter to &quot;no&quot;, unless you are sharing from an NFS mount, which is not a good idea in the first place. </p>
<p> Default: <i>posix locking</i><i> = </i><i>yes</i><i> </i></dl>
<p> strict locking (S) </p>
<dl>
<dd>This is an enumerated type that controls the handling of file locking in the server. When this is set to <code>yes</code>, the server will check every read and write access for file locks, and deny access if locks exist. This can be slow on some systems. </p>
<p> When strict locking is set to Auto (the default), the server performs file lock checks only on non-oplocked files. As most Windows redirectors perform file locking checks locally on oplocked files this is a good trade off for improved performance. </p>
<p> When strict locking is disabled, the server performs file lock checks only when the client explicitly asks for them. </p>
<p> Well-behaved clients always ask for lock checks when it is important. So in the vast majority of cases, strict locking = Auto or strict locking = no is acceptable. </p>
<p> Default: <i>strict locking</i><i> = </i><i>Auto</i><i> </i></dl>
<p> debug class (G) </p>
<dl>
<dd>With this boolean parameter enabled, the debug class (DBGC_CLASS) will be displayed in the debug header. </p>
<p> For more information about currently available debug classes, see section about m[blue]<code>log level</code>m[]. </p>
<p> Default: <i>debug class</i><i> = </i><i>no</i><i> </i></dl>
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
<p> timestamp logs </p>
<dl>
<dd>This parameter is a synonym for debug timestamp.</dl>
<p> debug timestamp (G) </p>
<dl>
<dd>Samba debug log messages are timestamped by default. If you are running at a high m[blue]<code>debug level</code>m[] these timestamps can be distracting. This boolean parameter allows timestamping to be turned off. </p>
<p> Default: <i>debug timestamp</i><i> = </i><i>yes</i><i> </i></dl>
<p> debug uid (G) </p>
<dl>
<dd>Samba is sometimes run as root and sometime run as the connected user, this boolean parameter inserts the current euid, egid, uid and gid to the timestamp message headers in the log file if turned on. </p>
<p> Note that the parameter m[blue]<code>debug timestamp</code>m[] must be on for this to have an effect. </p>
<p> Default: <i>debug uid</i><i> = </i><i>no</i><i> </i></dl>
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
<p> log file (G) </p>
<dl>
<dd>This option allows you to override the name of the Samba log file (also known as the debug file). </p>
<p> This option takes the standard substitutions, allowing you to have separate log files for each user or machine. </p>
<p> <i>No default</i> </p>
<p> Example: <i>log file</i><i> = </i><i>/usr/local/samba/var/log.%m</i><i> </i></dl>
<p> debuglevel </p>
<dl>
<dd>This parameter is a synonym for log level.</dl>
<p> log level (G) </p>
<dl>
<dd>The value of the parameter (a astring) allows the debug level (logging level) to be specified in the smb.conf file. </p>
<p> This parameter has been extended since the 2.2.x series, now it allows to specify the debug level for multiple debug classes. This is to give greater flexibility in the configuration of the system. The following debug classes are currently implemented: </p>
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
</dl>
<p> Default: <i>log level</i><i> = </i><i>0</i><i> </i> </p>
<p> Example: <i>log level</i><i> = </i><i>3 passdb:5 auth:10 winbind:2</i><i> </i> </p>
<p> max log size (G) </p>
<dl>
<dd>This option (an integer in kilobytes) specifies the max size the log file should grow to. Samba periodically checks the size and if it is exceeded it will rename the file, adding a .old extension. </p>
<p> A size of 0 means no limit. </p>
<p> Default: <i>max log size</i><i> = </i><i>5000</i><i> </i> </p>
<p> Example: <i>max log size</i><i> = </i><i>1000</i><i> </i></dl>
<p> syslog (G) </p>
<dl>
<dd>This parameter maps how Samba debug messages are logged onto the system syslog logging levels. Samba debug level zero maps onto syslog <code>LOG_ERR</code>, debug level one maps onto <code>LOG_WARNING</code>, debug level two maps onto <code>LOG_NOTICE</code>, debug level three maps onto LOG_INFO. All higher levels are mapped to <code>LOG_DEBUG</code>. </p>
<p> This parameter sets the threshold for sending messages to syslog. Only messages with debug level less than this value will be sent to syslog. There still will be some logging to log.[sn]mbd even if <i>syslog only</i> is enabled. </p>
<p> Default: <i>syslog</i><i> = </i><i>1</i><i> </i></dl>
<p> syslog only (G) </p>
<dl>
<dd>If this parameter is set then Samba debug messages are logged into the system syslog only, and not to the debug log files. There still will be some logging to log.[sn]mbd even if <i>syslog only</i> is enabled. </p>
<p> Default: <i>syslog only</i><i> = </i><i>no</i><i> </i></dl>
<p> abort shutdown script (G) </p>
<dl>
<dd>This a full path name to a script called by <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) that should stop a shutdown procedure issued by the m[blue]<code>shutdown script</code>m[]. </p>
<p> If the connected user possesses the <code>SeRemoteShutdownPrivilege</code>, right, this command will be run as root. </p>
<p> Default: <i>abort shutdown script</i><i> = </i><i>&quot;&quot;</i><i> </i> </p>
<p> Example: <i>abort shutdown script</i><i> = </i><i>/sbin/shutdown -c</i><i> </i></dl>
<p> add group script (G) </p>
<dl>
<dd>This is the full pathname to a script that will be run <i>AS ROOT</i> by <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) when a new group is requested. It will expand any <i>%g</i> to the group name passed. This script is only useful for installations using the Windows NT domain administration tools. The script is free to create a group with an arbitrary name to circumvent unix group name restrictions. In that case the script must print the numeric gid of the created group on stdout. </p>
<p> Default: <i>add group script</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>add group script</i><i> = </i><i>/usr/sbin/groupadd %g</i><i> </i></dl>
<p> add machine script (G) </p>
<dl>
<dd>This is the full pathname to a script that will be run by <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) when a machine is added to Samba&#8217;s domain and a Unix account matching the machine&#8217;s name appended with a &quot;$&quot; does not already exist. </p>
<p> This option is very similar to the m[blue]<code>add user script</code>m[], and likewise uses the %u substitution for the account name. Do not use the %m substitution. </p>
<p> Default: <i>add machine script</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>add machine script</i><i> = </i><i>/usr/sbin/adduser -n -g machines -c Machine -d /var/lib/nobody -s /bin/false %u</i><i> </i></dl>
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
<dd>Full path to the script that will be called when a user is added to a group using the Windows NT domain administration tools. It will be run by <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8)<i>AS ROOT</i>. Any <i>%g</i> will be replaced with the group name and any <i>%u</i> will be replaced with the user name. </p>
<p> Note that the adduser command used in the example below does not support the used syntax on all systems. </p>
<p> Default: <i>add user to group script</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>add user to group script</i><i> = </i><i>/usr/sbin/adduser %u %g</i><i> </i></dl>
<p> delete group script (G) </p>
<dl>
<dd>This is the full pathname to a script that will be run <i>AS ROOT</i><code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) when a group is requested to be deleted. It will expand any <i>%g</i> to the group name passed. This script is only useful for installations using the Windows NT domain administration tools. </p>
<p> Default: <i>delete group script</i><i> = </i><i></i><i> </i></dl>
<p> delete user from group script (G) </p>
<dl>
<dd>Full path to the script that will be called when a user is removed from a group using the Windows NT domain administration tools. It will be run by <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8)<i>AS ROOT</i>. Any <i>%g</i> will be replaced with the group name and any <i>%u</i> will be replaced with the user name. </p>
<p> Default: <i>delete user from group script</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>delete user from group script</i><i> = </i><i>/usr/sbin/deluser %u %g</i><i> </i></dl>
<p> delete user script (G) </p>
<dl>
<dd>This is the full pathname to a script that will be run by <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) when managing users with remote RPC (NT) tools. </p>
<p> This script is called when a remote client removes a user from the server, normally using &#8216;User Manager for Domains&#8217; or rpcclient. </p>
<p> This script should delete the given UNIX username. </p>
<p> Default: <i>delete user script</i><i> = </i><i></i><i> </i> </p>
<p> Example: <i>delete user script</i><i> = </i><i>/usr/local/samba/bin/del_user %u</i><i> </i></dl>
<p> domain logons (G) </p>
<dl>
<dd>If set to <code>yes</code>, the Samba server will provide the netlogon service for Windows 9X network logons for the m[blue]<code>workgroup</code>m[] it is in. This will also cause the Samba server to act as a domain controller for NT4 style domain services. For more details on setting up this feature see the Domain Control chapter of the Samba HOWTO Collection. </p>
<p> Default: <i>domain logons</i><i> = </i><i>no</i><i> </i></dl>
<p> enable privileges (G) </p>
<dl>
<dd>This deprecated parameter controls whether or not smbd will honor privileges assigned to specific SIDs via either net rpc rights or one of the Windows user and group manager tools. This parameter is enabled by default. It can be disabled to prevent members of the Domain Admins group from being able to assign privileges to users or groups which can then result in certain smbd operations running as root that would normally run under the context of the connected user. </p>
<p> An example of how privileges can be used is to assign the right to join clients to a Samba controlled domain without providing root access to the server via smbd. </p>
<p> Please read the extended description provided in the Samba HOWTO documentation. </p>
<p> Default: <i>enable privileges</i><i> = </i><i>yes</i><i> </i></dl>
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
