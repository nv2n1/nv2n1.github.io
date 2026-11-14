---
title: "sysusers(5)"
name: "sysusers"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sysusers/"
description: "sysusers.d – Declarative allocation of system users and groups"
---

<p>sysusers.d &#8211; Declarative allocation of system users and groups</p>
<h2>Synopsis</h2>
<p>/usr/lib/sysusers.d/*.conf</p>
<h2>Description</h2>
<p><code>systemd-sysusers</code> uses the files from sysusers.d directory to create system users and groups at package installation or boot time. This tool may be used to allocate system users and groups only, it is not useful for creating non-system users and groups, as it accesses /etc/passwd and /etc/group directly, bypassing any more complex user databases, for example any database involving NIS or LDAP.</p>
<h2>Configuration Format</h2>
<p>Each configuration file shall be named in the style of <i>package</i>.conf or <i>package</i>&#8211;<i>part</i>.conf. The second variant should be used when it is desirable to make it easy to override just this part of configuration. </p>
<p> The file format is one line per user or group containing name, ID, GECOS field description and home directory: </p>
<dl>
<dd>
<pre># Type Name ID GECOS
u httpd 440 &quot;HTTP User&quot;
u authd /usr/bin/authd &quot;Authorization user&quot;
g input - -
m authd input
u root 0 &quot;Superuser&quot; /root</pre>
</dl>
<h3>Type</h3>
<p>The type consists of a single letter. The following line types are understood: </p>
<p> <i>u</i></p>
<dl>
<dd>Create a system user and group of the specified name should they not exist yet. The user&#8217;s primary group will be set to the group bearing the same name. The user&#8217;s shell will be set to /sbin/nologin, the home directory to the specified home directory, or / if none is given. The account will be created disabled, so that logins are not allowed.</dl>
<p> <i>g</i></p>
<dl>
<dd>Create a system group of the specified name should it not exist yet. Note that <i>u</i> implicitly create a matching group. The group will be created with no password set.</dl>
<p> <i>m</i></p>
<dl>
<dd>Add a user to a group. If the user or group are not existing yet, they will be implicitly created.</dl>
<p> <i>r</i></p>
<dl>
<dd>Add a range of numeric UIDs/GIDs to the pool to allocate new UIDs and GIDs from. If no line of this type is specified the range of UIDs/GIDs is set to some compiled-in default. Note that both UIDs and GIDs are allocated from the same pool, in order to ensure that users and groups of the same name are likely to carry the same numeric UID and GID.</dl>
<h3>Name</h3>
<p>The name field specifies the user or group name. It should be shorter than 31 characters and avoid any non-ASCII characters, and not begin with a numeric character. It is strongly recommended to pick user and group names that are unlikely to clash with normal users created by the administrator. A good scheme to guarantee this is by prefixing all system and group names with the underscore, and avoiding too generic names. </p>
<p> For <i>m</i> lines this field should contain the user name to add to a group. </p>
<p> For lines of type <i>r</i> this field should be set to &quot;-&quot;.</p>
<h3>Id</h3>
<p>For <i>u</i> and <i>g</i> the numeric 32bit UID or GID of the user/group. Do not use IDs 65535 or 4294967295, as they have special placeholder meanings. Specify &quot;-&quot; for automatic UID/GID allocation for the user or group. Alternatively, specify an absolute path in the file system. In this case the UID/GID is read from the path&#8217;s owner/group. This is useful to create users whose UID/GID match the owners of pre-existing files (such as SUID or SGID binaries). </p>
<p> For <i>m</i> lines this field should contain the group name to add to a user to. </p>
<p> For lines of type <i>r</i> this field should be set to a UID/GID range in the format &quot;FROM-TO&quot; where both values are formatted as decimal ASCII numbers. Alternatively, a single UID/GID may be specified formatted as decimal ASCII numbers.</p>
<h3>Gecos</h3>
<p>A short, descriptive string for users to be created, enclosed in quotation marks. Note that this field may not contain colons. </p>
<p> Only applies to lines of type <i>u</i> and should otherwise be left unset, or be set to &quot;-&quot;.</p>
<h3>Home Directory</h3>
<p>The home directory for a new system user. If omitted defaults to the root directory. It is recommended to not unnecessarily specify home directories for system users, unless software strictly requires one to be set. </p>
<p> Only applies to lines of type <i>u</i> and should otherwise be left unset, or be set to &quot;-&quot;.</p>
<h2>Overriding Vendor Configuration</h2>
<p>Note that <code>systemd-sysusers</code> will do nothing if the specified users or groups already exist, so normally there no reason to override sysusers.d vendor configuration, except to block certain users or groups from being created. </p>
<p> Files in /etc/sysusers.d override files with the same name in /usr/lib/sysusers.d and /run/sysusers.d. Files in /run/sysusers.d override files with the same name in /usr/lib/sysusers.d. The scheme is the same as for <code><a href="/docs/linux/man/5-tmpfiles-d/">tmpfiles.d</a></code>(5), except for the directory name. </p>
<p> If the administrator wants to disable a configuration file supplied by the vendor, the recommended way is to place a symlink to /dev/null in /etc/sysusers.d/ bearing the same filename.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/8-systemd-sysusers/">systemd-sysusers</a></code>(8), <code><a href="/docs/linux/man/5-tmpfiles-d/">tmpfiles.d</a></code>(5) </p>
