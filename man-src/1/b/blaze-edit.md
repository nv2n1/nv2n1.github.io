---
title: "blaze-edit(1)"
name: "blaze-edit"
section: "1"
letter: "b"
url: "/docs/linux/man/1-blaze-edit/"
description: "blaze-edit – edit a blog post or a page in the BlazeBlogger repository"
---

<h2 class="name">NAME</h2>
<p> blaze-edit &#8211; edit a blog post or a page in the BlazeBlogger repository </p>
<h2>SYNOPSIS</h2>
<p> <code>blaze-edit</code> [<code>-fpqCPV</code>] [<code>-b</code> <i>directory</i>] <i>id</i> </p>
<p> <code>blaze-edit</code> <code>-h</code> | <code>-v</code></p>
<h2>DESCRIPTION</h2>
<p> <code>blaze-edit</code> enables you to edit a blog post or a page in your favourite text editor. </p>
<p> Note that inside your posts and pages, you can use several special placeholders to be replaced by appropriate data later, when the static content is being generated; the case is not significant, and supported placeholders are as follows:</p>
<dl>
<dt><code>%root%</code></p>
<dd> Relative path to the root directory of the blog; to be used inside links.</p>
<dt><code>%home%</code></p>
<dd> Relative path to the website home (index) page; to be used inside links.</p>
<dt><code>%page[</code><i>id</i><code>]%</code></p>
<dd> Relative path to the page with given <i>id</i>; to be used inside links.</p>
<dt><code>%post[</code><i>id</i><code>]%</code></p>
<dd> Relative path to the post with given <i>id</i>; to be used inside links.</p>
<dt><code>%tag[</code><i>name</i><code>]%</code></p>
<dd> Relative path to the tag with given <i>name</i>; to be used inside links.</dl>
<p> You can also use a special form, <code>&lt;!&#8211; break &#8211;&gt;</code>, to mark the end of a part to be displayed on index page.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code>, <code>&#8211;blogdir</code> <i>directory</i></p>
<dd> Specify the <i>directory</i> where the BlazeBlogger repository is placed. The default option is the current working directory.</p>
<dt><code>-p</code>, <code>&#8211;page</code></p>
<dd> Edit page instead of blog post.</p>
<dt><code>-P</code>, <code>&#8211;post</code></p>
<dd> Edit blog post; this is the default option.</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd> Force creating a new, empty raw file when it does not already exist, although the <tt>&quot;core.processor&quot;</tt> is enabled in the configuration; just be warned that this will rewrite whatever content is in the existing target file.</p>
<dt><code>-C</code>, <code>&#8211;no-processor</code></p>
<dd> Disable the use of external processor; just be warned that you will be editing the target (i.e. potentially previously processed) file instead of the raw source. Unless the <tt>&quot;core.processor&quot;</tt> is enabled in the configuration, this is the default behaviour.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> Avoid displaying messages that are not necessary.</p>
<dt><code>-V</code>, <code>&#8211;verbose</code></p>
<dd> Display all messages. This is the default option.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Display usage information and exit.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Display version information and exit.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><font SIZE="-1"><code>EDITOR</code></font></p>
<dd> Unless the BlazeBlogger specific option <i>core.editor</i> is set, blaze-edit tries to use system wide settings to decide which editor to run. If neither of these options are supplied, the <code>vi</code> is used instead as a considerably reasonable choice.</dl>
<h2>FILES</h2>
<dl>
<dt><i>.blaze/config</i></p>
<dd> BlazeBlogger configuration file.</dl>
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
