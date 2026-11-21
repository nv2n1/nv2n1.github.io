---

title: "blaze-remove(1)"
name: "blaze-remove"
section: "1"
letter: "b"
url: "/docs/linux/man/1-blaze-remove/"
description: "blaze-remove – remove a post/page from the BlazeBlogger repository"
---

<p> blaze-remove &#8211; remove a post/page from the BlazeBlogger repository </p>
<h2>SYNOPSIS</h2>
<p> <code>blaze-remove</code> [<code>-fipqPV</code>] [<code>-b</code> <i>directory</i>] <i>id</i>&#8230; </p>
<p> <code>blaze-remove</code> <code>-h</code> | <code>-v</code></p>
<h2>DESCRIPTION</h2>
<p> <code>blaze-remove</code> deletes the blog posts or pages with given <i>id</i>s from the BlazeBlogger repository.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code>, <code>&#8211;blogdir</code> <i>directory</i></dt>
<dd> Specify the <i>directory</i> where the BlazeBlogger repository is placed. The default option is the current working directory.</dd>
<dt><code>-p</code>, <code>&#8211;page</code>, <code>&#8211;pages</code></dt>
<dd> Remove pages instead of blog posts.</dd>
<dt><code>-P</code>, <code>&#8211;post</code>, <code>&#8211;posts</code></dt>
<dd> Remove blog posts; this is the default option.</dd>
<dt><code>-i</code>, <code>&#8211;interactive</code></dt>
<dd> Prompt before post/page removal.</dd>
<dt><code>-f</code>, <code>&#8211;force</code></dt>
<dd> Do not prompt before post/page removal; this is the default option.</dd>
<dt><code>-q</code>, <code>&#8211;quiet</code></dt>
<dd> Avoid displaying messages that are not necessary.</dd>
<dt><code>-V</code>, <code>&#8211;verbose</code></dt>
<dd> Display all messages. This is the default option.</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Display usage information and exit.</dd>
<dt><code>-v</code>, <code>&#8211;version</code></dt>
<dd> Display version information and exit.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-perl/">perl</a></code>(1).</p>
<h2>BUGS</h2>
<p> To report bug or even send patch, either add new issue to the project bugtracker at &lt;<a rel="nofollow" href="http://code.google.com/p/blazeblogger/issues/">http://code.google.com/p/blazeblogger/issues/</a>&gt;, or visit the discussion group at &lt;<a rel="nofollow" href="http://groups.google.com/group/blazeblogger/">http://groups.google.com/group/blazeblogger/</a>&gt;. You can also contact the author directly via e-mail.</p>
<h2>AUTHOR</h2>
<p> Written by Jaromir Hradilek &lt;jhradilek [at] gmail.com&gt;. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts. </p>
<p> A copy of the license is included as a file called <font SIZE="-1">FDL</font> in the main directory of the BlazeBlogger source package.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2008, 2009 Jaromir Hradilek </p>
<p> This program is free software; see the source for copying conditions. It is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT</font> <font SIZE="-1">ANY</font> <font SIZE="-1">WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS</font> <font SIZE="-1">FOR</font> A <font SIZE="-1">PARTICULAR</font> <font SIZE="-1">PURPOSE</font>. </p>
