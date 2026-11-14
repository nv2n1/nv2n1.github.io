---
title: "blaze-add(1)"
name: "blaze-add"
section: "1"
letter: "b"
url: "/docs/linux/man/1-blaze-add/"
description: "blaze-add – add a blog post or a page to the BlazeBlogger repository"
---

<h2 class="name">NAME</h2>
<p> blaze-add &#8211; add a blog post or a page to the BlazeBlogger repository </p>
<h2>SYNOPSIS</h2>
<p> <code>blaze-add</code> [<code>-pqCPV</code>] [<code>-b</code> <i>directory</i>] [<code>-a</code> <i>author</i>] [<code>-d</code> <i>date</i>] [<code>-t</code> <i>title</i>] [<code>-T</code> <i>tags</i>] [<code>-u</code> <i>url</i>] [<i>file</i>&#8230;] </p>
<p> <code>blaze-add</code> <code>-h</code> | <code>-v</code></p>
<h2>DESCRIPTION</h2>
<p> <code>blaze-add</code> adds new blog posts or pages to the BlazeBlogger repository. If supplied, it tries to read data from the existing <i>file</i>s, otherwise an external editor is opened to let you create a new content. </p>
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
<dt><code>-t</code>, <code>&#8211;title</code> <i>title</i></p>
<dd> Specify the post/page <i>title</i>.</p>
<dt><code>-a</code>, <code>&#8211;author</code> <i>author</i></p>
<dd> Specify the post/page <i>author</i>.</p>
<dt><code>-d</code>, <code>&#8211;date</code> <i>date</i></p>
<dd> Specify the post/page date of publishing; the <i>date</i> has to be in the YYYY-MM-DD form.</p>
<dt><code>-T</code>, <code>&#8211;tags</code> <i>tags</i></p>
<dd> Specify the comma separated list of <i>tags</i> attached to the blog post; pages ignore these.</p>
<dt><code>-u</code>, <code>&#8211;url</code> <i>url</i></p>
<dd> Specify the post/page <i>url</i> to be used instead of the one based on the post/page title. It should consist of alphanumeric characters, hyphens and underscores only, and it is especially useful if non-ASCII characters are present in the title.</p>
<dt><code>-p</code>, <code>&#8211;page</code>, <code>&#8211;pages</code></p>
<dd> Add page instead of blog post.</p>
<dt><code>-P</code>, <code>&#8211;post</code>, <code>&#8211;posts</code></p>
<dd> Add blog post; this is the default option.</p>
<dt><code>-C</code>, <code>&#8211;no-processor</code></p>
<dd> Disable the use of external processor. Unless the <tt>&quot;core.processor&quot;</tt> is enabled in the configuration, this is the default behaviour.</p>
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
