---
title: "blaze-init(1)"
name: "blaze-init"
section: "1"
letter: "b"
url: "/docs/linux/man/1-blaze-init/"
description: "blaze-init – create or recover a BlazeBlogger repository"
---

<h2 class="name">NAME</h2>
<p> blaze-init &#8211; create or recover a BlazeBlogger repository </p>
<h2>SYNOPSIS</h2>
<p> <code>blaze-init</code> [<code>-fqV</code>] [<code>-b</code> <i>directory</i>] </p>
<p> <code>blaze-init</code> <code>-h</code> | <code>-v</code></p>
<h2>DESCRIPTION</h2>
<p> <code>blaze-init</code>&#8216;s job is either to create a fresh new BlazeBlogger repository, or to recover an existing one, optionally changing the configuration and template files back to their original state while leaving the user data (i.e. both pages and blog posts) untouched.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code>, <code>&#8211;blogdir</code> <i>directory</i></p>
<dd> Specify the <i>directory</i> where the BlazeBlogger repository is to be placed. The default option is the current working directory.</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd> Force rewrite of already existing configuration, style, theme and language files.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> Avoid displaying messages that are not necessary.</p>
<dt><code>-V</code>, <code>&#8211;verbose</code></p>
<dd> Display all messages including the list of created files.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Display usage information and exit.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Display version information and exit.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-blaze-config/">blaze-config</a></code>(1), <code><a href="/docs/linux/man/1-perl/">perl</a></code>(1).</p>
<h2>BUGS</h2>
<p> To report bug or even send patch, either add new issue to the project bugtracker at &lt;<a rel="nofollow" href="http://code.google.com/p/blazeblogger/issues/">http://code.google.com/p/blazeblogger/issues/</a>&gt;, or visit the discussion group at &lt;<a rel="nofollow" href="http://groups.google.com/group/blazeblogger/">http://groups.google.com/group/blazeblogger/</a>&gt;. You can also contact the author directly via e-mail.</p>
<h2>AUTHOR</h2>
<p> Written by Jaromir Hradilek &lt;jhradilek [at] gmail.com&gt;. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts. </p>
<p> A copy of the license is included as a file called <font SIZE="-1">FDL</font> in the main directory of the BlazeBlogger source package.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2008, 2009 Jaromir Hradilek </p>
<p> This program is free software; see the source for copying conditions. It is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT</font> <font SIZE="-1">ANY</font> <font SIZE="-1">WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS</font> <font SIZE="-1">FOR</font> A <font SIZE="-1">PARTICULAR</font> <font SIZE="-1">PURPOSE</font>. </p>
<h2>Index</h2>
