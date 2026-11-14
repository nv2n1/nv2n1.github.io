---
title: "blaze-make(1)"
name: "blaze-make"
section: "1"
letter: "b"
url: "/docs/linux/man/1-blaze-make/"
description: "blaze-make – generate static content from the BlazeBlogger repository"
---

<h2 class="name">NAME</h2>
<p> blaze-make &#8211; generate static content from the BlazeBlogger repository </p>
<h2>SYNOPSIS</h2>
<p> <code>blaze-make</code> [<code>-cpqrtIFPV</code>] [<code>-b</code> <i>directory</i>] [<code>-d</code> <i>directory</i>] </p>
<p> <code>blaze-make</code> <code>-h</code> | <code>-v</code></p>
<h2>DESCRIPTION</h2>
<p> <code>blaze-make</code> reads the BlazeBlogger repository and generates a complete directory tree of static pages, optionally including all blog posts, single pages, browsable yearly and monthly archives, tags and even a <font SIZE="-1">RSS</font> feed. This way, you can benefit from most of the features other <font SIZE="-1">CMS</font> usually have, but without any additional hosting requirements.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code>, <code>&#8211;blogdir</code> <i>directory</i></p>
<dd> Specify the <i>directory</i> where the BlazeBlogger repository is placed. The default option is the current working directory.</p>
<dt><code>-d</code>, <code>&#8211;destdir</code> <i>directory</i></p>
<dd> Specify the <i>directory</i> where the generated static content is to be placed. The default option is the current working directory.</p>
<dt><code>-c</code>, <code>&#8211;no-css</code></p>
<dd> Disable creation of stylesheet.</p>
<dt><code>-I</code>, <code>&#8211;no-index</code></p>
<dd> Disable creation of index page. This is especially useful for websites with pages only.</p>
<dt><code>-p</code>, <code>&#8211;no-posts</code></p>
<dd> Disable creation of posts as well as any related pages, i.e. tags and <font SIZE="-1">RSS</font> feed. This is especially useful for websites with pages only.</p>
<dt><code>-P</code>, <code>&#8211;no-pages</code></p>
<dd> Disable creation of pages.</p>
<dt><code>-t</code>, <code>&#8211;no-tags</code></p>
<dd> Disable support for tags.</p>
<dt><code>-r</code>, <code>&#8211;no-rss</code></p>
<dd> Disable creation of <font SIZE="-1">RSS</font> feed.</p>
<dt><code>-F</code>, <code>&#8211;full-paths</code></p>
<dd> Enable full paths creation, i.e. always include page names in generated links.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> Avoid displaying messages that are not necessary.</p>
<dt><code>-V</code>, <code>&#8211;verbose</code></p>
<dd> Display all messages including the list of created files.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Display usage information and exit.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Display version information and exit.</dl>
<h2>FILES</h2>
<dl>
<dt><i>.blaze/config</i></p>
<dd> BlazeBlogger configuration file.</p>
<dt><i>.blaze/theme/</i></p>
<dd> BlazeBlogger themes directory.</p>
<dt><i>.blaze/style/</i></p>
<dd> BlazeBlogger stylesheets directory.</p>
<dt><i>.blaze/lang/</i></p>
<dd> BlazeBlogger language files directory.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-blazetheme/">blazetheme</a></code>(7), <code><a href="/docs/linux/man/1-blaze-config/">blaze-config</a></code>(1), <code><a href="/docs/linux/man/1-perl/">perl</a></code>(1).</p>
<h2>BUGS</h2>
<p> To report bug or even send patch, either add new issue to the project bugtracker at &lt;<a rel="nofollow" href="http://code.google.com/p/blazeblogger/issues/">http://code.google.com/p/blazeblogger/issues/</a>&gt;, or visit the discussion group at &lt;<a rel="nofollow" href="http://groups.google.com/group/blazeblogger/">http://groups.google.com/group/blazeblogger/</a>&gt;. You can also contact the author directly via e-mail.</p>
<h2>AUTHOR</h2>
<p> Written by Jaromir Hradilek &lt;jhradilek [at] gmail.com&gt;. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts. </p>
<p> A copy of the license is included as a file called <font SIZE="-1">FDL</font> in the main directory of the BlazeBlogger source package.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2009 Jaromir Hradilek </p>
<p> This program is free software; see the source for copying conditions. It is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT</font> <font SIZE="-1">ANY</font> <font SIZE="-1">WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS</font> <font SIZE="-1">FOR</font> A <font SIZE="-1">PARTICULAR</font> <font SIZE="-1">PURPOSE</font>. </p>
<h2>Index</h2>
