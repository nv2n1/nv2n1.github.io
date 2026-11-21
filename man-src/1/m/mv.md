---
title: "mv(1)"
name: "mv"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mv/"
description: "mv – move (rename) files"
---

<h2 class="name">NAME</h2>
<p> mv &#8211; move (rename) files </p>
<h2>SYNOPSIS</h2>
<p> <code>mv</code> [<i>,OPTION/</i>]&#8230; [<i>,-T/</i>] <i>,SOURCE DEST/</i><br />
 <code>mv</code> [<i>,OPTION/</i>]&#8230; <i>,SOURCE/</i>&#8230; <i>,DIRECTORY/</i><br />
 <code>mv</code> [<i>,OPTION/</i>]&#8230; <i>,-t DIRECTORY SOURCE/</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Rename SOURCE to DEST, or move SOURCE(s) to DIRECTORY. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>&#8211;backup</code>[=<i>,CONTROL/</i>]</dt>
<dd> make a backup of each existing destination file</dd>
<dt><code>-b</code></dt>
<dd> like <code>&#8211;backup</code> but does not accept an argument</dd>
<dt><code>-f</code>, <code>&#8211;force</code></dt>
<dd> do not prompt before overwriting</dd>
<dt><code>-i</code>, <code>&#8211;interactive</code></dt>
<dd> prompt before overwrite</dd>
<dt><code>-n</code>, <code>&#8211;no-clobber</code></dt>
<dd> do not overwrite an existing file</dd></dl>
<p> If you specify more than one of <code>-i</code>, <code>-f</code>, <code>-n</code>, only the final one takes effect.</p>
<dl>
<dt><code>&#8211;strip-trailing-slashes</code></dt>
<dd> remove any trailing slashes from each SOURCE argument</dd>
<dt><code>-S</code>, <code>&#8211;suffix</code>=<i>,SUFFIX/</i></dt>
<dd> override the usual backup suffix</dd>
<dt><code>-t</code>, <code>&#8211;target-directory</code>=<i>,DIRECTORY/</i></dt>
<dd> move all SOURCE arguments into DIRECTORY</dd>
<dt><code>-T</code>, <code>&#8211;no-target-directory</code></dt>
<dd> treat DEST as a normal file</dd>
<dt><code>-u</code>, <code>&#8211;update</code></dt>
<dd> move only when the SOURCE file is newer than the destination file or when the destination file is missing</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> explain what is being done</dd>
<dt><code>-Z</code>, <code>&#8211;context</code></dt>
<dd> set SELinux security context of destination file to default type</dd>
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
<h2>AUTHOR</h2>
<p> Written by Mike Parker, David MacKenzie, and Jim Meyering.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/2-rename/">rename</a>(2) </p>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/mv">https://www.gnu.org/software/coreutils/mv</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) mv invocation&#8217; </p>
