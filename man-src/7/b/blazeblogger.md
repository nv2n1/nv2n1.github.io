---
title: "blazeblogger(7)"
name: "blazeblogger"
section: "7"
letter: "b"
url: "/docs/linux/man/7-blazeblogger/"
description: "BlazeBlogger – a CMS without boundaries"
---

<p>BlazeBlogger &#8211; a CMS without boundaries</p>
<h2>Synopsis</h2>
<p><code>blaze-init</code> [<code>-fqV</code>] [<code>-b</code> <i>directory</i>] </p>
<p> <code>blaze-config</code> [<code>-qV</code>] [<code>-b</code> <i>directory</i>] <i>name</i> [<i>value</i>&#8230;] </p>
<p> <code>blaze-add</code> [<code>-pqCPV</code>] [<code>-b</code> <i>directory</i>] [<code>-a</code> <i>author</i>] [<code>-d</code> <i>date</i>] [<code>-t</code> <i>title</i>] [<code>-T</code> <i>tags</i>] [<code>-u</code> <i>url</i>] [<i>file</i>&#8230;] </p>
<p> <code>blaze-edit</code> [<code>-fpqCPV</code>] [<code>-b</code> <i>directory</i>] <i>id</i> </p>
<p> <code>blaze-remove</code> [<code>-fipqPV</code>] [<code>-b</code> <i>directory</i>] <i>id</i>&#8230; </p>
<p> <code>blaze-list</code> [<code>-cpqrsCPSV</code>] [<code>-b</code> <i>directory</i>] [<code>-I</code> <i>id</i>] [<code>-a</code> <i>author</i>] [<code>-t</code> <i>title</i>] [<code>-T</code> <i>tag</i>] [<code>-d</code> <i>day</i>] [<code>-m</code> <i>month</i>] [<code>-y</code> <i>year</i>] [<code>-n</code> <i>number</i>] </p>
<p> <code>blaze-make</code> [<code>-cpqrtIFPV</code>] [<code>-b</code> <i>directory</i>] [<code>-d</code> <i>directory</i>] </p>
<p> <code>blaze-log</code> [<code>-cqrsCV</code>] [<code>-b</code> <i>directory</i>] [<code>-n</code> <i>number</i>]</p>
<h2>Description</h2>
<p><code>BlazeBlogger</code> is a simple to use but capable <font SIZE="-1">CMS</font> for the command line. Being written in Perl as a cross-platform application and producing the static content without the need of database servers or server side scripting, it is literally a <font SIZE="-1">CMS</font> without boundaries suitable for a wide variety of web presentations, from personal weblog to a project page or even a company presentation.</p>
<h2>See Also</h2>
<dl>
<dt><code><a href="/docs/linux/man/7-blazeintro/">blazeintro</a></code>(7)</p>
<dd>An introduction to BlazeBlogger.</p>
<dt><code><a href="/docs/linux/man/7-blazetheme/">blazetheme</a></code>(7)</p>
<dd>An introduction to BlazeBlogger theme creation.</p>
<dt><code><a href="/docs/linux/man/1-blaze-init/">blaze-init</a></code>(1)</p>
<dd>Create or recover a BlazeBlogger repository.</p>
<dt><code><a href="/docs/linux/man/1-blaze-config/">blaze-config</a></code>(1)</p>
<dd>Display or set the BlazeBlogger repository options.</p>
<dt><code><a href="/docs/linux/man/1-blaze-add/">blaze-add</a></code>(1)</p>
<dd>Add a blog post or a page to the BlazeBlogger repository.</p>
<dt><code><a href="/docs/linux/man/1-blaze-edit/">blaze-edit</a></code>(1)</p>
<dd>Edit a blog post or a page in the BlazeBlogger repository.</p>
<dt><code><a href="/docs/linux/man/1-blaze-remove/">blaze-remove</a></code>(1)</p>
<dd>Remove a blog post or a page from the BlazeBlogger repository.</p>
<dt><code><a href="/docs/linux/man/1-blaze-list/">blaze-list</a></code>(1)</p>
<dd>Browse the content of the BlazeBlogger repository.</p>
<dt><code><a href="/docs/linux/man/1-blaze-make/">blaze-make</a></code>(1)</p>
<dd>Generate static content from the BlazeBlogger repository.</p>
<dt><code><a href="/docs/linux/man/1-blaze-log/">blaze-log</a></code>(1)</p>
<dd>Display the BlazeBlogger repository log.</dl>
<h2>Bugs</h2>
<p>To report bug or even send patch, either add new issue to the project bugtracker at &lt;<a rel="nofollow" href="http://code.google.com/p/blazeblogger/issues/">http://code.google.com/p/blazeblogger/issues/</a>&gt;, or visit the discussion group at &lt;<a rel="nofollow" href="http://groups.google.com/group/blazeblogger/">http://groups.google.com/group/blazeblogger/</a>&gt;. You can also contact the author directly via e-mail.</p>
<h2>Author</h2>
<p>Written by Jaromir Hradilek &lt;jhradilek [at] gmail.com&gt; </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts. </p>
<p> A copy of the license is included as a file called <font SIZE="-1">FDL</font> in the main directory of the BlazeBlogger source package.</p>
<h2>Copyright</h2>
<p>Copyright (C) 2008, 2009 Jaromir Hradilek </p>
<p> This program is free software; see the source for copying conditions. It is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT</font> <font SIZE="-1">ANY</font> <font SIZE="-1">WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS</font> <font SIZE="-1">FOR</font> A <font SIZE="-1">PARTICULAR</font> <font SIZE="-1">PURPOSE</font>.</p>
