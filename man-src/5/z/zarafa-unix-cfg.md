---
title: "zarafa-unix-cfg(5)"
name: "zarafa-unix-cfg"
section: "5"
letter: "z"
url: "/docs/linux/man/5-zarafa-unix-cfg/"
description: "zarafa-unix.cfg – The Zarafa Unix user plugin configuration file"
---

<p>zarafa-unix.cfg &#8211; The Zarafa Unix user plugin configuration file</p>
<h2>Synopsis</h2>
<p><code>unix.cfg</code></p>
<h2>Description</h2>
<p>The unix.cfg is a configuration file for the unix user plugin. All options to correctly retrieve user and group information can be set here.</p>
<h2>File Format</h2>
<p>The file consists of one big section, but parameters can be grouped by functionality. </p>
<p> The parameters are written in the form: </p>
<p> <code>name</code> = <i>value</i> </p>
<p> The file is line-based. Each newline-terminated line represents either a comment, nothing, a parameter or a directive. A line beginning with `#&#8217; is considered a comment, and will be ignored by Zarafa. Parameter names are case sensitive. Lines beginning with `!&#8217; are directives. </p>
<p> Directives are written in the form: </p>
<p> !<code>directive</code><i>[argument(s)] </i> </p>
<p> The following directives exist: </p>
<p> <code>include</code></p>
<dl>
<dd>Include and process <i>argument</i> </p>
<p> Example: !include common.cfg</dl>
<h2>Explanation Of Each Parameter</h2>
<p><code>fullname_charset</code></p>
<dl>
<dd>The charset that is used in /etc/passwd for the fullname of a user. In most setups, us-ascii is used, but may also be iso-8859-15. All charsets supported by the system iconv() are supported here. Since iso-8859-15 is an extension on us-ascii, this is used as the default to support high characters for most latin languages. If your default shell is in UTF-8 (see your locales settings), enter utf-8 here. </p>
<p> Default: <i>iso-8859-15</i></dl>
<p> <code>default_domain</code></p>
<dl>
<dd>The default domain name to set as e-mail address. When a user is created, it&#8217;s email address will be set to <i>username [at] default_domain</i>. </p>
<p> Default: <i>no default present</i>.</dl>
<p> <code>min_user_uid</code></p>
<dl>
<dd>This is the minimal uid a user must have to be created as a Zarafa user. This is to skip system users present in the /etc/passwd file. Normally, users start at 1000. </p>
<p> Default: <i>1000</i></dl>
<p> <code>max_user_uid</code></p>
<dl>
<dd>This is the maximum uid a user may have to be created as a Zarafa user. This is to skip system users present in the /etc/passwd file with a high uid, as user nobody does. </p>
<p> Default: <i>10000</i></dl>
<p> <code>except_user_uids</code></p>
<dl>
<dd>A whitespace seperated list of uids that are within the min_user_uid and max_user_uid range, but shouldn&#8217;t be considered as users. </p>
<p> Default: <i>empty</i></dl>
<p> <code>min_group_gid</code></p>
<dl>
<dd>This is the minimal gid a group must have to be created as a Zarafa group. This is to skip system groups present in the /etc/group file. Normally, groups start at 1000. </p>
<p> Default: <i>1000</i></dl>
<p> <code>max_group_gid</code></p>
<dl>
<dd>This is the maximum gid a group may have to be created as a Zarafa group. This is to skip system groups present in the /etc/group file with a high gid, as group nogroup does. </p>
<p> Default: <i>10000</i></dl>
<p> <code>except_group_gids</code></p>
<dl>
<dd>A whitespace seperated list of gids that are within the min_group_gid and max_group_gid range, but shouldn&#8217;t be considered as groups. </p>
<p> Default: <i>empty</i></dl>
<p> <code>non_login_shell</code></p>
<dl>
<dd>This this the shell a user has to be created as a non-login box. Mail can be delivered to this box, but you cannot directly login with this username. The uid must be within the defined limits. </p>
<p> Default: <i>/bin/false</i></dl>
<h2>User Attributes</h2>
<p>Not all Zarafa attributes can be used from the system files. The following attibutes are used from the system files: </p>
<p> username</p>
<dl>
<dd>The login name of the user.</dl>
<p> fullname</p>
<dl>
<dd>The fullname of the user.</dl>
<p> password</p>
<dl>
<dd>The password is in the /etc/shadow file. Zarafa needs reads access to this file to correctly work with the Unix plugin.</dl>
<p> Other attributes like quota settings, admin setting and e-mail address are kept in the database like the db user plugin does.</p>
<h2>Files</h2>
<p>/etc/zarafa/server.cfg</p>
<dl>
<dd>The server configuration file.</dl>
<p> /etc/zarafa/unix.cfg</p>
<dl>
<dd>The Zarafa Unix user plugin configuration file.</dl>
<h2>Author</h2>
<p>Written by Zarafa.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-zarafa-server/">zarafa-server</a></code>(1)<code><a href="/docs/linux/man/5-zarafa-server-cfg/">zarafa-server.cfg</a></code>(5) </p>
