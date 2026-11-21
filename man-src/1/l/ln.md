---
title: "ln(1)"
name: "ln"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ln/"
description: "ln – make links between files"
---

<h2 class="name">NAME</h2>
<p> ln &#8211; make links between files </p>
<h2>SYNOPSIS</h2>
<p> <code>ln</code> [<i>,OPTION/</i>]&#8230; [<i>,-T/</i>] <i>,TARGET LINK_NAME/</i><br />
 <code>ln</code> [<i>,OPTION/</i>]&#8230; <i>,TARGET/</i><br />
 <code>ln</code> [<i>,OPTION/</i>]&#8230; <i>,TARGET/</i>&#8230; <i>,DIRECTORY/</i><br />
 <code>ln</code> [<i>,OPTION/</i>]&#8230; <i>,-t DIRECTORY TARGET/</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> In the 1st form, create a link to TARGET with the name LINK_NAME. In the 2nd form, create a link to TARGET in the current directory. In the 3rd and 4th forms, create links to each TARGET in DIRECTORY. Create hard links by default, symbolic links with <code>&#8211;symbolic</code>. By default, each destination (name of new link) should not already exist. When creating hard links, each TARGET must exist. Symbolic links can hold arbitrary text; if later resolved, a relative link is interpreted in relation to its parent directory. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>&#8211;backup</code>[=<i>,CONTROL/</i>]</dt>
<dd> make a backup of each existing destination file</dd>
<dt><code>-b</code></dt>
<dd> like <code>&#8211;backup</code> but does not accept an argument</dd>
<dt><code>-d</code>, <code>-F</code>, <code>&#8211;directory</code></dt>
<dd> allow the superuser to attempt to hard link directories (note: will probably fail due to system restrictions, even for the superuser)</dd>
<dt><code>-f</code>, <code>&#8211;force</code></dt>
<dd> remove existing destination files</dd>
<dt><code>-i</code>, <code>&#8211;interactive</code></dt>
<dd> prompt whether to remove destinations</dd>
<dt><code>-L</code>, <code>&#8211;logical</code></dt>
<dd> dereference TARGETs that are symbolic links</dd>
<dt><code>-n</code>, <code>&#8211;no-dereference</code></dt>
<dd> treat LINK_NAME as a normal file if it is a symbolic link to a directory</dd>
<dt><code>-P</code>, <code>&#8211;physical</code></dt>
<dd> make hard links directly to symbolic links</dd>
<dt><code>-r</code>, <code>&#8211;relative</code></dt>
<dd> create symbolic links relative to link location</dd>
<dt><code>-s</code>, <code>&#8211;symbolic</code></dt>
<dd> make symbolic links instead of hard links</dd>
<dt><code>-S</code>, <code>&#8211;suffix</code>=<i>,SUFFIX/</i></dt>
<dd> override the usual backup suffix</dd>
<dt><code>-t</code>, <code>&#8211;target-directory</code>=<i>,DIRECTORY/</i></dt>
<dd> specify the DIRECTORY in which to create the links</dd>
<dt><code>-T</code>, <code>&#8211;no-target-directory</code></dt>
<dd> treat LINK_NAME as a normal file always</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> print name of each linked file</dd>
<dt><code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>&#8211;version</code></dt>
<dd> output version information and exit</dd></dl>
<p> The backup suffix is &#8216;~&#8217;, unless set with <code>&#8211;suffix</code> or SIMPLE_BACKUP_SUFFIX. The version control method may be selected via the <code>&#8211;backup</code> option or through the VERSION_CONTROL environment variable. Here are the values:</p>
<dl>
<dt>none, off</dt>
<dd> never make backups (even if <code>&#8211;backup</code> is given)</dd>
<dt>numbered, t</dt>
<dd> make numbered backups</dd>
<dt>existing, nil</dt>
<dd> numbered if numbered backups exist, simple otherwise</dd>
<dt>simple, never</dt>
<dd> always make simple backups</dd></dl>
<p> Using <code>-s</code> ignores <code>-L</code> and <code>-P</code>. Otherwise, the last option specified controls behavior when a TARGET is a symbolic link, defaulting to <code>-P</code>.</p>
<h2>AUTHOR</h2>
<p> Written by Mike Parker and David MacKenzie.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/2-link/">link</a>(2), <a href="/docs/linux/man/2-symlink/">symlink</a>(2) </p>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/ln">https://www.gnu.org/software/coreutils/ln</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) ln invocation&#8217; </p>
