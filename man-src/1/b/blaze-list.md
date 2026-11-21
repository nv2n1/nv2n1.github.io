---
title: "blaze-list(1)"
name: "blaze-list"
section: "1"
letter: "b"
url: "/docs/linux/man/1-blaze-list/"
description: "blaze-list – browse the content of the BlazeBlogger repository"
---

<h2>SYNOPSIS</h2>
<p> <code>blaze-list</code> [<code>-cpqrsCPSV</code>] [<code>-b</code> <i>directory</i>] [<code>-I</code> <i>id</i>] [<code>-a</code> <i>author</i>] [<code>-t</code> <i>title</i>] [<code>-T</code> <i>tag</i>] [<code>-d</code> <i>day</i>] [<code>-m</code> <i>month</i>] [<code>-y</code> <i>year</i>] [<code>-n</code> <i>number</i>] </p>
<p> <code>blaze-list</code> <code>-h</code> | <code>-v</code></p>
<h2>DESCRIPTION</h2>
<p> <code>blaze-list</code> displays the content of the BlazeBlogger repository. All items are listed by default, but desired subset can be easily selected via additional options.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code>, <code>&#8211;blogdir</code> <i>directory</i></dt>
<dd> Specify the <i>directory</i> where the BlazeBlogger repository is placed. The default option is the current working directory.</dd>
<dt><code>-I</code>, <code>&#8211;id</code> <i>id</i></dt>
<dd> Display the record with specified <i>id</i> only.</dd>
<dt><code>-a</code>, <code>&#8211;author</code> <i>author</i></dt>
<dd> List records by specified <i>author</i> only.</dd>
<dt><code>-t</code>, <code>&#8211;title</code> <i>title</i></dt>
<dd> List records with matching <i>title</i>.</dd>
<dt><code>-T</code>, <code>&#8211;tag</code> <i>tag</i></dt>
<dd> List records tagged as <i>tag</i>.</dd>
<dt><code>-d</code>, <code>&#8211;day</code> <i>day</i></dt>
<dd> List records from the specified day where <i>day</i> is in the <font SIZE="-1">DD</font> format. Do not forget to specify the month and year as well, unless you, for example, want to list all records from the first day of every month.</dd>
<dt><code>-m</code>, <code>&#8211;month</code> <i>month</i></dt>
<dd> List records from the specified month where <i>month</i> is in the <font SIZE="-1">MM</font> format. Do not forget to specify the year as well, unless you, for example, want to list all july records.</dd>
<dt><code>-y</code>, <code>&#8211;year</code> <i>year</i></dt>
<dd> List records from the specified year where <i>year</i> is in the <font SIZE="-1">YYYY</font> format.</dd>
<dt><code>-n</code>, <code>&#8211;number</code> <i>number</i></dt>
<dd> List selected <i>number</i> of records only.</dd>
<dt><code>-p</code>, <code>&#8211;pages</code></dt>
<dd> List pages instead of blog posts.</dd>
<dt><code>-P</code>, <code>&#8211;posts</code></dt>
<dd> List blog posts; this is the default option.</dd>
<dt><code>-S</code>, <code>&#8211;stats</code></dt>
<dd> Show repository statistics instead of blog posts.</dd>
<dt><code>-s</code>, <code>&#8211;short</code></dt>
<dd> Display each record on a single line.</dd>
<dt><code>-r</code>, <code>&#8211;reverse</code></dt>
<dd> Display records in reverse order.</dd>
<dt><code>-c</code>, <code>&#8211;color</code>, <code>&#8211;colour</code></dt>
<dd> Enable coloured output, no matter what is set in the configuration.</dd>
<dt><code>-C</code>, <code>&#8211;no-color</code>, <code>&#8211;no-colour</code></dt>
<dd> Disable coloured output, no matter what is set in the configuration.</dd>
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
<p> Copyright (C) 2009 Jaromir Hradilek </p>
<p> This program is free software; see the source for copying conditions. It is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT</font> <font SIZE="-1">ANY</font> <font SIZE="-1">WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS</font> <font SIZE="-1">FOR</font> A <font SIZE="-1">PARTICULAR</font> <font SIZE="-1">PURPOSE</font>. </p>
