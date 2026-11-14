---
title: "chown(1)"
name: "chown"
section: "1"
letter: "c"
url: "/docs/linux/man/1-chown/"
description: "chown – change file owner and group"
---

<h2 class="name">NAME</h2>
<p> chown &#8211; change file owner and group </p>
<h2>SYNOPSIS</h2>
<p> <code>chown</code> [<i>,OPTION/</i>]&#8230; [<i>,OWNER/</i>][<i>,:/</i>[<i>,GROUP/</i>]] <i>,FILE/</i>&#8230;<br />
 <code>chown</code> [<i>,OPTION/</i>]&#8230; <i>,&#8211;reference=RFILE FILE/</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents the GNU version of <code>chown</code>. <code>chown</code> changes the user and/or group ownership of each given file. If only an owner (a user name or numeric user ID) is given, that user is made the owner of each given file, and the files&#8217; group is not changed. If the owner is followed by a colon and a group name (or numeric group ID), with no spaces between them, the group ownership of the files is changed as well. If a colon but no group name follows the user name, that user is made the owner of the files and the group of the files is changed to that user&#8217;s login group. If the colon and group are given, but the owner is omitted, only the group of the files is changed; in this case, <code>chown</code> performs the same function as <code>chgrp</code>. If only a colon is given, or if the entire operand is empty, neither the owner nor the group is changed.</p>
<h2>OPTIONS</h2>
<p> Change the owner and/or group of each FILE to OWNER and/or GROUP. With <code>&#8211;reference</code>, change the owner and group of each FILE to those of RFILE.</p>
<dl>
<dt><code>-c</code>, <code>&#8211;changes</code></p>
<dd> like verbose but report only when a change is made</p>
<dt><code>-f</code>, <code>&#8211;silent</code>, <code>&#8211;quiet</code></p>
<dd> suppress most error messages</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> output a diagnostic for every file processed</p>
<dt><code>&#8211;dereference</code></p>
<dd> affect the referent of each symbolic link (this is the default), rather than the symbolic link itself</p>
<dt><code>-h</code>, <code>&#8211;no-dereference</code></p>
<dd> affect symbolic links instead of any referenced file (useful only on systems that can change the ownership of a symlink)</p>
<dt><code>&#8211;from</code>=<i>,CURRENT_OWNER/</i>:CURRENT_GROUP</p>
<dd> change the owner and/or group of each file only if its current owner and/or group match those specified here. Either may be omitted, in which case a match is not required for the omitted attribute</p>
<dt><code>&#8211;no-preserve-root</code></p>
<dd> do not treat &#8216;/&#8217; specially (the default)</p>
<dt><code>&#8211;preserve-root</code></p>
<dd> fail to operate recursively on &#8216;/&#8217;</p>
<dt><code>&#8211;reference</code>=<i>,RFILE/</i></p>
<dd> use RFILE&#8217;s owner and group rather than specifying OWNER:GROUP values</p>
<dt><code>-R</code>, <code>&#8211;recursive</code></p>
<dd> operate on files and directories recursively</dl>
<p> The following options modify how a hierarchy is traversed when the <code>-R</code> option is also specified. If more than one is specified, only the final one takes effect.</p>
<dl>
<dt><code>-H</code></p>
<dd> if a command line argument is a symbolic link to a directory, traverse it</p>
<dt><code>-L</code></p>
<dd> traverse every symbolic link to a directory encountered</p>
<dt><code>-P</code></p>
<dd> do not traverse any symbolic links (default)</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<p> Owner is unchanged if missing. Group is unchanged if missing, but changed to login group if implied by a &#8216;:&#8217; following a symbolic OWNER. OWNER and GROUP may be numeric as well as symbolic.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>chown root /u</p>
<dd> Change the owner of /u to &quot;root&quot;.</p>
<dt>chown root:staff /u</p>
<dd> Likewise, but also change its group to &quot;staff&quot;.</p>
<dt>chown -hR root /u</p>
<dd> Change the owner of /u and subfiles to &quot;root&quot;.</dl>
<h2>AUTHOR</h2>
<p> Written by David MacKenzie and Jim Meyering.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/2-chown/">chown</a>(2) </p>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/chown">https://www.gnu.org/software/coreutils/chown</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) chown invocation&#8217; </p>
<h2>Index</h2>
