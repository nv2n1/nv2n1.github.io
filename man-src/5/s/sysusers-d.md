---
title: "sysusers-d(5)"
name: "sysusers-d"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sysusers-d/"
description: "sysusers.d – Declarative allocation of system users and groups"
---

<p>sysusers.d &#8211; Declarative allocation of system users and groups</p>
<h2>Synopsis</h2>
<p>/etc/sysusers.d/*.conf </p>
<p> /run/sysusers.d/*.conf </p>
<p> /usr/lib/sysusers.d/*.conf </p>
<pre>#Type Name ID GECOS Home directory Shell
u user_name uid &quot;User Description&quot; /home/dir /path/to/shell
u user_name uid:gid &quot;User Description&quot; /home/dir /path/to/shell
u user_name /file/owned/by/user &quot;User Description&quot; /home/dir /path/to/shell
g group_name gid
g group_name /file/owned/by/group
m user_name group_name
r - lowest-highest</pre>
<h2>Description</h2>
<p><code>systemd-sysusers</code> uses the files from sysusers.d directory to create system users and groups and to add users to groups, at package installation or boot time. This tool may be used to allocate system users and groups only, it is not useful for creating non-system (i.e. regular, &quot;human&quot;) users and groups, as it accesses /etc/passwd and /etc/group directly, bypassing any more complex user databases, for example any database involving NIS or LDAP.</p>
<h2>Configuration Directories And Precedence</h2>
<p>Each configuration file shall be named in the style of <i>package</i>.conf or <i>package</i>&#8211;<i>part</i>.conf. The second variant should be used when it is desirable to make it easy to override just this part of configuration. </p>
<p> Files in /etc/sysusers.d override files with the same name in /usr/lib/sysusers.d and /run/sysusers.d. Files in /run/sysusers.d override files with the same name in /usr/lib/sysusers.d. Packages should install their configuration files in /usr/lib/sysusers.d. Files in /etc/sysusers.d are reserved for the local administrator, who may use this logic to override the configuration files installed by vendor packages. All configuration files are sorted by their filename in lexicographic order, regardless of which of the directories they reside in. If multiple files specify the same path, the entry in the file with the lexicographically earliest name will be applied. All later entries for the same user and group names will be logged as warnings. </p>
<p> If the administrator wants to disable a configuration file supplied by the vendor, the recommended way is to place a symlink to /dev/null in /etc/sysusers.d/ bearing the same filename.</p>
<h2>Configuration File Format</h2>
<p>The file format is one line per user or group containing name, ID, GECOS field description, home directory, and login shell: </p>
<dl>
<dd>
<pre>#Type Name ID GECOS Home directory Shell
u httpd 404 &quot;HTTP User&quot;
u _authd /usr/bin/authd &quot;Authorization user&quot;
u postgres - &quot;Postgresql Database&quot; /var/lib/pgsql /libexec/postgresdb
g input - -
m _authd input
u root 0 &quot;Superuser&quot; /root /bin/zsh
r - 500-900</pre>
</dl>
<p> Empty lines and lines beginning with the &quot;#&quot; character are ignored, and may be used for commenting.</p>
<h3>Type</h3>
<p>The type consists of a single letter. The following line types are understood: </p>
<p> <i>u</i></p>
<dl>
<dd>Create a system user and group of the specified name should they not exist yet. The user&#8217;s primary group will be set to the group bearing the same name unless the ID field specifies it. The account will be created disabled, so that logins are not allowed.</dl>
<p> <i>g</i></p>
<dl>
<dd>Create a system group of the specified name should it not exist yet. Note that <i>u</i> implicitly creates a matching group. The group will be created with no password set.</dl>
<p> <i>m</i></p>
<dl>
<dd>Add a user to a group. If the user or group do not exist yet, they will be implicitly created.</dl>
<p> <i>r</i></p>
<dl>
<dd>Add a range of numeric UIDs/GIDs to the pool to allocate new UIDs and GIDs from. If no line of this type is specified, the range of UIDs/GIDs is set to some compiled-in default. Note that both UIDs and GIDs are allocated from the same pool, in order to ensure that users and groups of the same name are likely to carry the same numeric UID and GID.</dl>
<h3>Name</h3>
<p>The name field specifies the user or group name. The specified name must consist only of the characters a-z, A-Z, 0-9, &quot;_&quot; and &quot;-&quot;, except for the first character which must be one of a-z, A-Z or &quot;_&quot; (i.e. numbers and &quot;-&quot; are not permitted as first character). The user/group name must have at least one character, and at most 31. </p>
<p> For further details about the syntax of user/group names, see m[blue]<code>User/Group Name Syntax</code>m[]<font SIZE="-2">[1]</font>. </p>
<p> It is strongly recommended to pick user and group names that are unlikely to clash with normal users created by the administrator. A good scheme to guarantee this is by prefixing all system and group names with the underscore, and avoiding too generic names. </p>
<p> For <i>m</i> lines, this field should contain the user name to add to a group. </p>
<p> For lines of type <i>r</i>, this field should be set to &quot;-&quot;.</p>
<h3>Id</h3>
<p>For <i>u</i> and <i>g</i>, the numeric 32-bit UID or GID of the user/group. Do not use IDs 65535 or 4294967295, as they have special placeholder meanings. Specify &quot;-&quot; for automatic UID/GID allocation for the user or group (this is strongly recommended unless it is strictly necessary to use a specific UID or GID). Alternatively, specify an absolute path in the file system. In this case, the UID/GID is read from the path&#8217;s owner/group. This is useful to create users whose UID/GID match the owners of pre-existing files (such as SUID or SGID binaries). The syntaxes &quot;<i>uid</i>:<i>gid</i>&quot; and &quot;<i>uid</i>:<i>groupname</i>&quot; are supported to allow creating users with specific primary groups. The given group must be created explicitly, or it must already exist. Specifying &quot;-&quot; for the UID in these syntaxes is also supported. </p>
<p> For <i>m</i> lines, this field should contain the group name to add to a user to. </p>
<p> For lines of type <i>r</i>, this field should be set to a UID/GID range in the format &quot;FROM-TO&quot;, where both values are formatted as decimal ASCII numbers. Alternatively, a single UID/GID may be specified formatted as decimal ASCII numbers.</p>
<h3>Gecos</h3>
<p>A short, descriptive string for users to be created, enclosed in quotation marks. Note that this field may not contain colons. </p>
<p> Only applies to lines of type <i>u</i> and should otherwise be left unset (or &quot;-&quot;).</p>
<h3>Home Directory</h3>
<p>The home directory for a new system user. If omitted, defaults to the root directory. </p>
<p> Only applies to lines of type <i>u</i> and should otherwise be left unset (or &quot;-&quot;). It is recommended to omit this, unless software strictly requires a home directory to be set. </p>
<p> <code>systemd-sysusers</code> only sets the home directory record in the user database. To actually create the directory, consider adding a corresponding <code><a href="/docs/linux/man/5-tmpfiles-d/">tmpfiles.d</a></code>(5) fragment.</p>
<h3>Shell</h3>
<p>The login shell of the user. If not specified, this will be set to /usr/sbin/nologin, except if the UID of the user is 0, in which case /bin/sh will be used. </p>
<p> Only applies to lines of type <i>u</i> and should otherwise be left unset (or &quot;-&quot;). It is recommended to omit this, unless a shell different /usr/sbin/nologin must be used.</p>
<h2>Specifiers</h2>
<p>Specifiers can be used in the &quot;Name&quot;, &quot;ID&quot;, &quot;GECOS&quot;, &quot;Home directory&quot;, and &quot;Shell&quot; fields. An unknown or unresolvable specifier is treated as invalid configuration. The following expansions are understood: </p>
<p> <code>Table 1. Specifiers available</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Specifier </code></td>
<td><code> Meaning </code></td>
<td><code> Details </code>
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%a&quot; </td>
<td> Architecture </td>
<td> A short string identifying the architecture of the local system. A string such as <code>x86</code>, <code>x86-64</code> or <code>arm64</code>. See the architectures defined for <i>ConditionArchitecture=</i> in <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for a full list.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%A&quot; </td>
<td> Operating system image version </td>
<td> The operating system image version identifier of the running system, as read from the <i>IMAGE_VERSION=</i> field of /etc/os-release. If not set, resolves to an empty string. See <code><a href="/docs/linux/man/5-os-release/">os-release</a></code>(5) for more information.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%b&quot; </td>
<td> Boot ID </td>
<td> The boot ID of the running system, formatted as string. See <code><a href="/docs/linux/man/4-random/">random</a></code>(4) for more information.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%B&quot; </td>
<td> Operating system build ID </td>
<td> The operating system build identifier of the running system, as read from the <i>BUILD_ID=</i> field of /etc/os-release. If not set, resolves to an empty string. See <code><a href="/docs/linux/man/5-os-release/">os-release</a></code>(5) for more information.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%H&quot; </td>
<td> Host name </td>
<td> The hostname of the running system.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%l&quot; </td>
<td> Short host name </td>
<td> The hostname of the running system, truncated at the first dot to remove any domain component.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%m&quot; </td>
<td> Machine ID </td>
<td> The machine ID of the running system, formatted as string. See <code><a href="/docs/linux/man/5-machine-id/">machine-id</a></code>(5) for more information.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%M&quot; </td>
<td> Operating system image identifier </td>
<td> The operating system image identifier of the running system, as read from the <i>IMAGE_ID=</i> field of /etc/os-release. If not set, resolves to an empty string. See <code><a href="/docs/linux/man/5-os-release/">os-release</a></code>(5) for more information.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%o&quot; </td>
<td> Operating system ID </td>
<td> The operating system identifier of the running system, as read from the <i>ID=</i> field of /etc/os-release. See <code><a href="/docs/linux/man/5-os-release/">os-release</a></code>(5) for more information.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%T&quot; </td>
<td> Directory for temporary files </td>
<td> This is either /tmp or the path &quot;$TMPDIR&quot;, &quot;$TEMP&quot; or &quot;$TMP&quot; are set to. (Note that the directory may be specified without a trailing slash.)
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%v&quot; </td>
<td> Kernel release </td>
<td> Identical to <code>uname -r</code> output.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%V&quot; </td>
<td> Directory for larger and persistent temporary files </td>
<td> This is either /var/tmp or the path &quot;$TMPDIR&quot;, &quot;$TEMP&quot; or &quot;$TMP&quot; are set to. (Note that the directory may be specified without a trailing slash.)
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%w&quot; </td>
<td> Operating system version ID </td>
<td> The operating system version identifier of the running system, as read from the <i>VERSION_ID=</i> field of /etc/os-release. If not set, resolves to an empty string. See <code><a href="/docs/linux/man/5-os-release/">os-release</a></code>(5) for more information.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%W&quot; </td>
<td> Operating system variant ID </td>
<td> The operating system variant identifier of the running system, as read from the <i>VARIANT_ID=</i> field of /etc/os-release. If not set, resolves to an empty string. See <code><a href="/docs/linux/man/5-os-release/">os-release</a></code>(5) for more information.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%%&quot; </td>
<td> Single percent sign </td>
<td> Use &quot;%%&quot; in place of &quot;%&quot; to specify a single percent sign.
</td>
</tr>
</table>
<h2>Idempotence</h2>
<p>Note that <code>systemd-sysusers</code> will do nothing if the specified users or groups already exist or the users are members of specified groups, so normally there is no reason to override sysusers.d vendor configuration, except to block certain users or groups from being created.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/8-systemd-sysusers/">systemd-sysusers</a></code>(8)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>User/Group Name Syntax</p>
<dl>
<dd><a rel="nofollow" href="https://systemd.io/USER_NAMES">https://systemd.io/USER_NAMES</a></dl>
