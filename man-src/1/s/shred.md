---
title: "shred(1)"
name: "shred"
section: "1"
letter: "s"
url: "/docs/linux/man/1-shred/"
description: "shred – overwrite a file to hide its contents, and optionally delete it"
---

<h2 class="name">NAME</h2>
<p> shred &#8211; overwrite a file to hide its contents, and optionally delete it </p>
<h2>SYNOPSIS</h2>
<p> <code>shred</code> [<i>,OPTION/</i>]&#8230; <i>,FILE/</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Overwrite the specified FILE(s) repeatedly, in order to make it harder for even very expensive hardware probing to recover the data. </p>
<p> If FILE is -, shred standard output. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd> change permissions to allow writing if necessary</p>
<dt><code>-n</code>, <code>&#8211;iterations</code>=<i>,N/</i></p>
<dd> overwrite N times instead of the default (3)</p>
<dt><code>&#8211;random-source</code>=<i>,FILE/</i></p>
<dd> get random bytes from FILE</p>
<dt><code>-s</code>, <code>&#8211;size</code>=<i>,N/</i></p>
<dd> shred this many bytes (suffixes like K, M, G accepted)</p>
<dt><code>-u</code></p>
<dd> deallocate and remove file after overwriting</p>
<dt><code>&#8211;remove</code>[=<i>,HOW/</i>]</p>
<dd> like <code>-u</code> but give control on HOW to delete; See below</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> show progress</p>
<dt><code>-x</code>, <code>&#8211;exact</code></p>
<dd> do not round file sizes up to the next full block;</p>
<dt>
<dd> this is the default for non-regular files</p>
<dt><code>-z</code>, <code>&#8211;zero</code></p>
<dd> add a final overwrite with zeros to hide shredding</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<p> Delete FILE(s) if <code>&#8211;remove</code> (<code>-u</code>) is specified. The default is not to remove the files because it is common to operate on device files like <i>,/dev/hda/</i>, and those files usually should not be removed. The optional HOW parameter indicates how to remove a directory entry: &#8216;unlink&#8217; =&gt; use a standard unlink call. &#8216;wipe&#8217; =&gt; also first obfuscate bytes in the name. &#8216;wipesync&#8217; =&gt; also sync each obfuscated byte to disk. The default mode is &#8216;wipesync&#8217;, but note it can be expensive. </p>
<p> CAUTION: shred assumes the file system and hardware overwrite data in place. Although this is common, many platforms operate otherwise. Also, backups and mirrors may contain unremovable copies that will let a shredded file be recovered later. See the GNU coreutils manual for details.</p>
<h2>AUTHOR</h2>
<p> Written by Colin Plumb.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/shred">https://www.gnu.org/software/coreutils/shred</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) shred invocation&#8217; </p>
<h2>Index</h2>
