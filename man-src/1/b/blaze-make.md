---

title: "blaze-make(1)"
name: "blaze-make"
section: "1"
letter: "b"
url: "/docs/linux/man/1-blaze-make/"
description: "blaze-make – generate static content from the BlazeBlogger repository"
---

<p> blaze-make &#8211; generate static content from the BlazeBlogger repository </p>
<h2>SYNOPSIS</h2>
<p> <code>blaze-make</code> [<code>-cpqrtIFPV</code>] [<code>-b</code> <i>directory</i>] [<code>-d</code> <i>directory</i>] </p>
<p> <code>blaze-make</code> <code>-h</code> | <code>-v</code></p>
<h2>DESCRIPTION</h2>
<p> <code>blaze-make</code> reads the BlazeBlogger repository and generates a complete directory tree of static pages, optionally including all blog posts, single pages, browsable yearly and monthly archives, tags and even a RSS feed. This way, you can benefit from most of the features other CMS usually have, but without any additional hosting requirements.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code>, <code>&#8211;blogdir</code> <i>directory</i></dt>
<dd> Specify the <i>directory</i> where the BlazeBlogger repository is placed. The default option is the current working directory.</dd>
<dt><code>-d</code>, <code>&#8211;destdir</code> <i>directory</i></dt>
<dd> Specify the <i>directory</i> where the generated static content is to be placed. The default option is the current working directory.</dd>
<dt><code>-c</code>, <code>&#8211;no-css</code></dt>
<dd> Disable creation of stylesheet.</dd>
<dt><code>-I</code>, <code>&#8211;no-index</code></dt>
<dd> Disable creation of index page. This is especially useful for websites with pages only.</dd>
<dt><code>-p</code>, <code>&#8211;no-posts</code></dt>
<dd> Disable creation of posts as well as any related pages, i.e. tags and RSS feed. This is especially useful for websites with pages only.</dd>
<dt><code>-P</code>, <code>&#8211;no-pages</code></dt>
<dd> Disable creation of pages.</dd>
<dt><code>-t</code>, <code>&#8211;no-tags</code></dt>
<dd> Disable support for tags.</dd>
<dt><code>-r</code>, <code>&#8211;no-rss</code></dt>
<dd> Disable creation of RSS feed.</dd>
<dt><code>-F</code>, <code>&#8211;full-paths</code></dt>
<dd> Enable full paths creation, i.e. always include page names in generated links.</dd>
<dt><code>-q</code>, <code>&#8211;quiet</code></dt>
<dd> Avoid displaying messages that are not necessary.</dd>
<dt><code>-V</code>, <code>&#8211;verbose</code></dt>
<dd> Display all messages including the list of created files.</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Display usage information and exit.</dd>
<dt><code>-v</code>, <code>&#8211;version</code></dt>
<dd> Display version information and exit.</dd></dl>
<h2>FILES</h2>
<dl>
<dt><i>.blaze/config</i></dt>
<dd> BlazeBlogger configuration file.</dd>
<dt><i>.blaze/theme/</i></dt>
<dd> BlazeBlogger themes directory.</dd>
<dt><i>.blaze/style/</i></dt>
<dd> BlazeBlogger stylesheets directory.</dd>
<dt><i>.blaze/lang/</i></dt>
<dd> BlazeBlogger language files directory.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-blazetheme/">blazetheme</a></code>(7), <code><a href="/docs/linux/man/1-blaze-config/">blaze-config</a></code>(1), <code><a href="/docs/linux/man/1-perl/">perl</a></code>(1).</p>
<h2>BUGS</h2>
<p> To report bug or even send patch, either add new issue to the project bugtracker at &lt;<a rel="nofollow" href="http://code.google.com/p/blazeblogger/issues/">http://code.google.com/p/blazeblogger/issues/</a>&gt;, or visit the discussion group at &lt;<a rel="nofollow" href="http://groups.google.com/group/blazeblogger/">http://groups.google.com/group/blazeblogger/</a>&gt;. You can also contact the author directly via e-mail.</p>
<h2>AUTHOR</h2>
<p> Written by Jaromir Hradilek &lt;jhradilek [at] gmail.com&gt;. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts. </p>
<p> A copy of the license is included as a file called FDL in the main directory of the BlazeBlogger source package.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2009 Jaromir Hradilek </p>
<p> This program is free software; see the source for copying conditions. It is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
