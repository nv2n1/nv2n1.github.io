---
title: "rm-2(1)"
name: "rm-2"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rm-2/"
description: "rm – remove files or directories"
---

<p>rm &#8211; remove files or directories </p>
<h2>Synopsis</h2>
<p><code>rm</code> [<i>,OPTION/</i>]&#8230; [<i>,FILE/</i>]&#8230;</p>
<h2>Description</h2>
<p>This manual page documents the GNU version of <code>rm</code>. <code>rm</code> removes each specified file. By default, it does not remove directories. </p>
<p> If the <i>-I</i> or <i>&#8211;interactive=once</i> option is given, and there are more than three files or the <i>-r</i>, <i>-R</i>, or <i>&#8211;recursive</i> are given, then <code>rm</code> prompts the user for whether to proceed with the entire operation. If the response is not affirmative, the entire command is aborted. </p>
<p> Otherwise, if a file is unwritable, standard input is a terminal, and the <i>-f</i> or <i>&#8211;force</i> option is not given, or the <i>-i</i> or <i>&#8211;interactive=always</i> option is given, <code>rm</code> prompts the user for whether to remove the file. If the response is not affirmative, the file is skipped.</p>
<h2>Options</h2>
<p>Remove (unlink) the FILE(s).</p>
<dl>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd>ignore nonexistent files and arguments, never prompt</p>
<dt><code>-i</code></p>
<dd>prompt before every removal</p>
<dt><code>-I</code></p>
<dd>prompt once before removing more than three files, or when removing recursively; less intrusive than <code>-i</code>, while still giving protection against most mistakes</p>
<dt><code>&#8211;interactive</code>[=<i>,WHEN/</i>]</p>
<dd>prompt according to WHEN: never, once (<code>-I</code>), or always (<code>-i</code>); without WHEN, prompt always</p>
<dt><code>&#8211;one-file-system</code></p>
<dd>when removing a hierarchy recursively, skip any directory that is on a file system different from that of the corresponding command line argument</p>
<dt><code>&#8211;no-preserve-root</code></p>
<dd>do not treat &#8216;/&#8217; specially</p>
<dt><code>&#8211;preserve-root</code>[=<i>,all/</i>]</p>
<dd>do not remove &#8216;/&#8217; (default); with &#8216;all&#8217;, reject any command line argument on a separate device from its parent</p>
<dt><code>-r</code>, <code>-R</code>, <code>&#8211;recursive</code></p>
<dd>remove directories and their contents recursively</p>
<dt><code>-d</code>, <code>&#8211;dir</code></p>
<dd>remove empty directories</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>explain what is being done</p>
<dt><code>&#8211;help</code></p>
<dd>display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd>output version information and exit</dl>
<p> By default, rm does not remove directories. Use the <code>&#8211;recursive</code> (<code>-r</code> or <code>-R</code>) option to remove each listed directory, too, along with all of its contents. </p>
<p> To remove a file whose name starts with a &#8216;-&#8216;, for example &#8216;-foo&#8217;, use one of these commands:</p>
<dl>
<dd>rm <code>&#8212;</code> <code>-foo</code></p>
<dd>rm ./-foo</dl>
<p> Note that if you use rm to remove a file, it might be possible to recover some of its contents, given sufficient expertise and/or time. For greater assurance that the contents are truly unrecoverable, consider using shred.</p>
<h2>Author</h2>
<p>Written by Paul Rubin, David MacKenzie, Richard M. Stallman, and Jim Meyering.</p>
<h2>Reporting Bugs</h2>
<p>GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-unlink/">unlink</a>(1), <a href="/docs/linux/man/2-unlink/">unlink</a>(2), <a href="/docs/linux/man/1-chattr/">chattr</a>(1), <a href="/docs/linux/man/1-shred/">shred</a>(1) </p>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/rm">https://www.gnu.org/software/coreutils/rm</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) rm invocation&#8217;</p>
