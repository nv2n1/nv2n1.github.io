---
title: "blaze-config(1)"
name: "blaze-config"
section: "1"
letter: "b"
url: "/docs/linux/man/1-blaze-config/"
description: "blaze-config – display or set the BlazeBlogger repository options"
---

<h2 class="name">NAME</h2>
<p> blaze-config &#8211; display or set the BlazeBlogger repository options </p>
<h2>SYNOPSIS</h2>
<p> <code>blaze-config</code> [<code>-qV</code>] [<code>-b</code> <i>directory</i>] <i>name</i> [<i>value&#8230;</i>] </p>
<p> <code>blaze-config</code> <code>-e</code> [<code>-b</code> <i>directory</i>] </p>
<p> <code>blaze-config</code> <code>-h</code> | <code>-v</code></p>
<h2>DESCRIPTION</h2>
<p> <code>blaze-config</code> is a simple configuration tool for the BlazeBlogger. Depending on the number of given command-line arguments, it either displays the current value of the specified option, or sets/replaces it with the new one. </p>
<p> The accepted option <i>name</i> is in the form of dot separated section and key (e.g. user.name). For the complete list of available options along with the explanation of their meaning, see the appropriate section below.</p>
<h2>OPTIONS</h2>
<h2>Command-line options</h2>
<dl>
<dt><code>-b</code>, <code>&#8211;blogdir</code> <i>directory</i></dt>
<dd> Specify the <i>directory</i> where the BlazeBlogger repository is placed. The default option is the current working directory.</dd>
<dt><code>-e</code>, <code>&#8211;edit</code></dt>
<dd> Open the configuration file in the external text editor.</dd>
<dt><code>-q</code>, <code>&#8211;quiet</code></dt>
<dd> Avoid displaying messages that are not necessary.</dd>
<dt><code>-V</code>, <code>&#8211;verbose</code></dt>
<dd> Display all messages. This is the default option.</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Display usage information and exit.</dd>
<dt><code>-v</code>, <code>&#8211;version</code></dt>
<dd> Display version information and exit.</dd></dl>
<h2>Available option names</h2>
<dl>
<dt><code>blog.title</code></dt>
<dd> Blog title.</dd>
<dt><code>blog.subtitle</code></dt>
<dd> Blog subtitle, supposedly a brief, single-line description of what should an occasional visitor expect to find.</dd>
<dt><code>blog.theme</code></dt>
<dd> Blog theme; the value should point to an existing file in the .blaze/theme directory.</dd>
<dt><code>blog.style</code></dt>
<dd> Blog stylesheet; the value should point to an existing file, either in <tt>&quot;.blaze/style&quot;</tt> (recommended), or in the destination directory where the static content is to be placed.</dd>
<dt><code>blog.lang</code></dt>
<dd> Blog language; the value should point to an existing file in the <tt>&quot;.blaze/lang&quot;</tt> directory.</dd>
<dt><code>blog.posts</code></dt>
<dd> Number of posts to be listed on a single page; the default value is 10.</dd>
<dt><code>blog.url</code></dt>
<dd> Blog base url; required for <font SIZE="-1">RSS</font> feeds only.</dd>
<dt><code>color.list</code></dt>
<dd> Whether to use coloured post/pages listing; the value has to be either <tt>&quot;true&quot;</tt>, or <tt>&quot;false&quot;</tt>. Colours are turned off by default.</dd>
<dt><code>color.log</code></dt>
<dd> Whether to use coloured log listing; the value has to be either <tt>&quot;true&quot;</tt>, or <tt>&quot;false&quot;</tt>. Colours are turned off by default.</dd>
<dt><code>core.encoding</code></dt>
<dd> Records encoding in the form recognised by the W3C <font SIZE="-1">HTML</font> 4.01 standard (e.g. the default <font SIZE="-1">UTF-8</font>).</dd>
<dt><code>core.extension</code></dt>
<dd> File extension for the generated pages. By default, the <tt>&quot;html&quot;</tt> is used as a reasonable choice.</dd>
<dt><code>core.editor</code></dt>
<dd> Text editor to be used for editing purposes. Unless this option is set, BlazeBlogger tries to use system wide settings by looking for <tt>&quot;EDITOR&quot;</tt> environment variable, and if neither of these options is supplied, <tt>&quot;vi&quot;</tt> is used as a considerably reasonable option.</dd>
<dt><code>core.processor</code></dt>
<dd> Optional external application to be used to process the entries; use <tt>&quot;%in%&quot;</tt> and <tt>&quot;%out%&quot;</tt> in place of input and output file names (e.g. <tt>&quot;markdown --html4tags %in% &gt; %out%&quot;</tt>). Nevertheless, if you intend to write your content in <font SIZE="-1">HTML</font> directly, feel free to leave this option empty (the default setting).</dd>
<dt><code>post.author</code></dt>
<dd> Location of the post author information; available options are <tt>&quot;top&quot;</tt>, <tt>&quot;bottom&quot;</tt>, or <tt>&quot;none&quot;</tt>. Author is placed above the post (below its heading) by default.</dd>
<dt><code>post.date</code></dt>
<dd> Location of the post date of publishing information; available options are <tt>&quot;top&quot;</tt>, <tt>&quot;bottom&quot;</tt>, or <tt>&quot;none&quot;</tt>. Date of publishing is placed above the post (below its heading) by default.</dd>
<dt><code>post.tags</code></dt>
<dd> Location of the post tags; available options are <tt>&quot;top&quot;</tt>, <tt>&quot;bottom&quot;</tt>, or <tt>&quot;none&quot;</tt>. Tags are placed above the post (below its heading) by default.</dd>
<dt><code>user.name</code></dt>
<dd> User&#8217;s name to be used as a default posts&#8217; author and optionally anywhere on the page, depending on the theme (e.g. in the copyright notice).</dd>
<dt><code>user.email</code></dt>
<dd> User&#8217;s e-mail. Depending on the theme, it can be used anywhere on the page (e.g. in the copyright notice). However, non of the official themes actually use it.</dd></dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><font SIZE="-1"><code>EDITOR</code></font></dt>
<dd> Unless the BlazeBlogger specific option <i>core.editor</i> is set, blaze-edit tries to use system wide settings to decide which editor to run. If neither of these options are supplied, the <code>vi</code> is used instead as a considerably reasonable choice.</dd></dl>
<h2>FILES</h2>
<dl>
<dt><i>.blaze/config</i></dt>
<dd> BlazeBlogger configuration file.</dd></dl>
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
<h2>Index</h2>
