---
title: "cp(1)"
name: "cp"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cp/"
description: "cp – copy files and directories"
---

<h2 class="name">NAME</h2>
<p> cp &#8211; copy files and directories </p>
<h2>SYNOPSIS</h2>
<p> <code>cp</code> [<i>,OPTION/</i>]&#8230; [<i>,-T/</i>] <i>,SOURCE DEST/</i><br />
 <code>cp</code> [<i>,OPTION/</i>]&#8230; <i>,SOURCE/</i>&#8230; <i>,DIRECTORY/</i><br />
 <code>cp</code> [<i>,OPTION/</i>]&#8230; <i>,-t DIRECTORY SOURCE/</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Copy SOURCE to DEST, or multiple SOURCE(s) to DIRECTORY. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>-a</code>, <code>&#8211;archive</code></p>
<dd> same as <code>-dR</code> <code>&#8211;preserve</code>=<i>,all/</i></p>
<dt><code>&#8211;attributes-only</code></p>
<dd> don&#8217;t copy the file data, just the attributes</p>
<dt><code>&#8211;backup</code>[=<i>,CONTROL/</i>]</p>
<dd> make a backup of each existing destination file</p>
<dt><code>-b</code></p>
<dd> like <code>&#8211;backup</code> but does not accept an argument</p>
<dt><code>&#8211;copy-contents</code></p>
<dd> copy contents of special files when recursive</p>
<dt><code>-d</code></p>
<dd> same as <code>&#8211;no-dereference</code> <code>&#8211;preserve</code>=<i>,links/</i></p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd> if an existing destination file cannot be opened, remove it and try again (this option is ignored when the <code>-n</code> option is also used)</p>
<dt><code>-i</code>, <code>&#8211;interactive</code></p>
<dd> prompt before overwrite (overrides a previous <code>-n</code> option)</p>
<dt><code>-H</code></p>
<dd> follow command-line symbolic links in SOURCE</p>
<dt><code>-l</code>, <code>&#8211;link</code></p>
<dd> hard link files instead of copying</p>
<dt><code>-L</code>, <code>&#8211;dereference</code></p>
<dd> always follow symbolic links in SOURCE</p>
<dt><code>-n</code>, <code>&#8211;no-clobber</code></p>
<dd> do not overwrite an existing file (overrides a previous <code>-i</code> option)</p>
<dt><code>-P</code>, <code>&#8211;no-dereference</code></p>
<dd> never follow symbolic links in SOURCE</p>
<dt><code>-p</code></p>
<dd> same as <code>&#8211;preserve</code>=<i>,mode/</i>,ownership,timestamps</p>
<dt><code>&#8211;preserve</code>[=<i>,ATTR_LIST/</i>]</p>
<dd> preserve the specified attributes (default: mode,ownership,timestamps), if possible additional attributes: context, links, xattr, all</p>
<dt><code>&#8211;no-preserve</code>=<i>,ATTR_LIST/</i></p>
<dd> don&#8217;t preserve the specified attributes</p>
<dt><code>&#8211;parents</code></p>
<dd> use full source file name under DIRECTORY</p>
<dt><code>-R</code>, <code>-r</code>, <code>&#8211;recursive</code></p>
<dd> copy directories recursively</p>
<dt><code>&#8211;reflink</code>[=<i>,WHEN/</i>]</p>
<dd> control clone/CoW copies. See below</p>
<dt><code>&#8211;remove-destination</code></p>
<dd> remove each existing destination file before attempting to open it (contrast with <code>&#8211;force</code>)</p>
<dt><code>&#8211;sparse</code>=<i>,WHEN/</i></p>
<dd> control creation of sparse files. See below</p>
<dt><code>&#8211;strip-trailing-slashes</code></p>
<dd> remove any trailing slashes from each SOURCE argument</p>
<dt><code>-s</code>, <code>&#8211;symbolic-link</code></p>
<dd> make symbolic links instead of copying</p>
<dt><code>-S</code>, <code>&#8211;suffix</code>=<i>,SUFFIX/</i></p>
<dd> override the usual backup suffix</p>
<dt><code>-t</code>, <code>&#8211;target-directory</code>=<i>,DIRECTORY/</i></p>
<dd> copy all SOURCE arguments into DIRECTORY</p>
<dt><code>-T</code>, <code>&#8211;no-target-directory</code></p>
<dd> treat DEST as a normal file</p>
<dt><code>-u</code>, <code>&#8211;update</code></p>
<dd> copy only when the SOURCE file is newer than the destination file or when the destination file is missing</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> explain what is being done</p>
<dt><code>-x</code>, <code>&#8211;one-file-system</code></p>
<dd> stay on this file system</p>
<dt><code>-Z</code></p>
<dd> set SELinux security context of destination file to default type</p>
<dt><code>&#8211;context</code>[=<i>,CTX/</i>]</p>
<dd> like <code>-Z</code>, or if CTX is specified then set the SELinux or SMACK security context to CTX</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<p> By default, sparse SOURCE files are detected by a crude heuristic and the corresponding DEST file is made sparse as well. That is the behavior selected by <code>&#8211;sparse</code>=<i>,auto/</i>. Specify <code>&#8211;sparse</code>=<i>,always/</i> to create a sparse DEST file whenever the SOURCE file contains a long enough sequence of zero bytes. Use <code>&#8211;sparse</code>=<i>,never/</i> to inhibit creation of sparse files. </p>
<p> When <code>&#8211;reflink</code>[=<i>,always/</i>] is specified, perform a lightweight copy, where the data blocks are copied only when modified. If this is not possible the copy fails, or if <code>&#8211;reflink</code>=<i>,auto/</i> is specified, fall back to a standard copy. Use <code>&#8211;reflink</code>=<i>,never/</i> to ensure a standard copy is performed. </p>
<p> The backup suffix is &#8216;~&#8217;, unless set with <code>&#8211;suffix</code> or SIMPLE_BACKUP_SUFFIX. The version control method may be selected via the <code>&#8211;backup</code> option or through the VERSION_CONTROL environment variable. Here are the values:</p>
<dl>
<dt>none, off</p>
<dd> never make backups (even if <code>&#8211;backup</code> is given)</p>
<dt>numbered, t</p>
<dd> make numbered backups</p>
<dt>existing, nil</p>
<dd> numbered if numbered backups exist, simple otherwise</p>
<dt>simple, never</p>
<dd> always make simple backups</dl>
<p> As a special case, cp makes a backup of SOURCE when the force and backup options are given and SOURCE and DEST are the same name for an existing, regular file.</p>
<h2>AUTHOR</h2>
<p> Written by Torbjorn Granlund, David MacKenzie, and Jim Meyering.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/cp">https://www.gnu.org/software/coreutils/cp</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) cp invocation&#8217; </p>
<h2>Index</h2>
