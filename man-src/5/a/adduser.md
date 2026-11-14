---
title: "adduser(5)"
name: "adduser"
section: "5"
letter: "a"
url: "/docs/linux/man/5-adduser/"
description: "/etc/adduser.conf – configuration file for"
---

<p>/etc/adduser.conf &#8211; configuration file for <code></p>
<p><a href="/docs/linux/man/8-adduser/">adduser</a>(8) </code> and <code><a href="/docs/linux/man/8-addgroup/">addgroup</a>(8)</code>.</p>
<h2>Description</h2>
<p>The file <i>/etc/adduser.conf</i> contains defaults for the programs <code><a href="/docs/linux/man/8-adduser/">adduser</a>(8)</code> , <code><a href="/docs/linux/man/8-addgroup/">addgroup</a>(8)</code> , <code><a href="/docs/linux/man/8-deluser/">deluser</a>(8)</code> and <code><a href="/docs/linux/man/8-delgroup/">delgroup</a>(8)</code>. Each line holds a single value pair in the form <i>option</i> = <i>value</i>. Double or single quotes are allowed around the value, as is whitespace around the equals sign. Comment lines must have a hash sign (#) in the first column. </p>
<p> The valid configuration options are:</p>
<dl>
<dt><code>DSHELL</code></p>
<dd>The login shell to be used for all new users. Defaults to <i>/bin/bash</i>.</p>
<dt><code>DHOME</code></p>
<dd>The directory in which new home directories should be created. Defaults to <i>/home</i>.</p>
<dt><code>GROUPHOMES</code></p>
<dd>If this is set to <i>yes</i>, the home directories will be created as <i>/home/[groupname]/user</i>. Defaults to <i>no</i>.</p>
<dt><code>LETTERHOMES</code></p>
<dd>If this is set to <i>yes</i>, then the home directories created will have an extra directory inserted which is the first letter of the loginname. For example: <i>/home/u/user</i>. Defaults to <i>no</i>.</p>
<dt><code>SKEL</code></p>
<dd>The directory from which skeletal user configuration files should be copied. Defaults to <i>/etc/skel</i>.</p>
<dt><code>FIRST_SYSTEM_UID</code> and <code>LAST_SYSTEM_UID</code></p>
<dd>specify an inclusive range of UIDs from which system UIDs can be dynamically allocated. Default to <i>100</i> &#8211; <i>999</i>. Please note that system software, such as the users allocated by the base-passwd package, may assume that UIDs less than 100 are unallocated.</p>
<dt><code>FIRST_UID</code> and <code>LAST_UID</code></p>
<dd>specify an inclusive range of UIDs from which normal user&#8217;s UIDs can be dynamically allocated. Default to <i>1000</i> &#8211; <i>29999</i>.</p>
<dt><code>FIRST_SYSTEM_GID</code> and <code>LAST_SYSTEM_GID</code></p>
<dd>specify an inclusive range of GIDs from which system GIDs can be dynamically allocated. Default to <i>100</i> &#8211; <i>999.</i></p>
<dt><code>FIRST_GID</code> and <code>LAST_GID</code></p>
<dd>specify an inclusive range of GIDs from which normal group&#8217;s GIDs can be dynamically allocated. Default to <i>1000</i> &#8211; <i>29999</i>.</p>
<dt><code>USERGROUPS</code></p>
<dd>If this is set to <i>yes</i>, then each created user will be given their own group to use. If this is <i>no</i>, then each created user will be placed in the group whose GID is <code>USERS_GID</code> (see below). The default is <i>yes</i>.</p>
<dt><code>USERS_GID</code></p>
<dd>If <code>USERGROUPS</code> is <i>no</i>, then <code>USERS_GID</code> is the GID given to all newly-created users. The default value is <i>100</i>.</p>
<dt><code>DIR_MODE</code></p>
<dd>If set to a valid value (e.g. 0755 or 755), directories created will have the specified permissions as umask. Otherwise 0755 is used as default.</p>
<dt><code>SETGID_HOME</code></p>
<dd>If this is set to <i>yes</i>, then home directories for users with their own group ( <i>USERGROUPS=yes</i> ) will have the setgid bit set. This was the default setting for adduser versions &lt;&lt; 3.13. Unfortunately it has some bad side effects, so we no longer do this per default. If you want it nevertheless you can still activate it here.</p>
<dt><code>QUOTAUSER</code></p>
<dd>If set to a nonempty value, new users will have quotas copied from that user. The default is empty.</p>
<dt><code>NAME_REGEX</p>
<dd>User and group names are checked against this regular expression. If the name doesn&#8217;t match this regexp, user and group creation in adduser is refused unless &#8211;force-badname is set. With &#8211;force-badname set, only weak checks are performed. The default is the most conservative ^[a-z][-a-z0-9]*$. When &#8211;system is specified, NAME_REGEX_SYSTEM is used instead.</p>
<dt>NAME_REGEX_SYSTEM</p>
<dd>Names of system users are checked against this regular expression. If &#8211;system is supplied and the name doesn&#8217;t match this regexp, user creation in adduser is refused unless &#8211;force-badname is set. With &#8211;force-badname set, only weak checks are performed. The default is as for the default NAME_REGEX but also allowing uppercase letters.</p>
<dt>SKEL_IGNORE_REGEX</p>
<dd>Files in /etc/skel/ are checked against this regex, and not copied to the newly created home directory if they match. This is by default set to the regular expression matching files left over from unmerged config files (dpkg-(old|new|dist)).</p>
<dt>ADD_EXTRA_GROUPS</p>
<dd>Setting this to something other than 0 (the default) will cause adduser to add newly created non-system users to the list of groups defined by EXTRA_GROUPS (below).</p>
<dt>EXTRA_GROUPS</p>
<dd>This is the list of groups that new non-system users will be added to. By default, this list is &#8216;dialout cdrom floppy audio video plugdev users games&#8217;</dl>
<p> </code></p>
<h2>Notes</h2>
<dl>
<dt><code>VALID NAMES</p>
<dd>adduser and addgroup enforce conformity to IEEE Std 1003.1-2001, which allows only the following characters to appear in group and user names: letters, digits, underscores, periods, at signs (@) and dashes. The name may no start with a dash. The &quot;$&quot; sign is allowed at the end of usernames (to conform to samba). An additional check can be adjusted via the configuration parameter NAME_REGEX to enforce a local policy. </p>
<h2>Files</h2>
<p><i>/etc/adduser.conf</i></p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-adduser/">adduser</a>(8), <a href="/docs/linux/man/8-addgroup/">addgroup</a>(8), <a href="/docs/linux/man/8-deluser/">deluser</a>(8), <a href="/docs/linux/man/8-delgroup/">delgroup</a>(8), <a href="/docs/linux/man/5-deluser-conf/">deluser.conf</a>(5) </p>
