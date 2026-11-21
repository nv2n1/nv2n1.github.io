---

title: "blaze-log(1)"
name: "blaze-log"
section: "1"
letter: "b"
url: "/docs/linux/man/1-blaze-log/"
description: "blaze-log – display the BlazeBlogger repository log"
---

<p> blaze-log &#8211; display the BlazeBlogger repository log </p>
<h2>SYNOPSIS</h2>
<p> <code>blaze-log</code> [<code>-cqrsCV</code>] [<code>-b</code> <i>directory</i>] [<code>-n</code> <i>number</i>] </p>
<p> <code>blaze-log</code> <code>-h</code> | <code>-v</code></p>
<h2>DESCRIPTION</h2>
<p> <code>blaze-log</code> displays the content of the BlazeBlogger repository log.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code>, <code>&#8211;blogdir</code> <i>directory</i></dt>
<dd> Specify the <i>directory</i> where the BlazeBlogger repository is placed. The default option is the current working directory.</dd>
<dt><code>-n</code>, <code>&#8211;number</code> <i>number</i></dt>
<dd> List selected number of log records only.</dd>
<dt><code>-s</code>, <code>&#8211;short</code></dt>
<dd> Display each log record on a single line.</dd>
<dt><code>-r</code>, <code>&#8211;reverse</code></dt>
<dd> Display log records in reverse order.</dd>
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
<h2>FILES</h2>
<dl>
<dt><i>.blaze/log</i></dt>
<dd> BlazeBlogger repository log file.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-blaze-config/">blaze-config</a></code>(1), <code><a href="/docs/linux/man/1-perl/">perl</a></code>(1).</p>
<h2>BUGS</h2>
<p> To report bug or even send patch, either add new issue to the project bugtracker at &lt;<a rel="nofollow" href="http://code.google.com/p/blazeblogger/issues/">http://code.google.com/p/blazeblogger/issues/</a>&gt;, or visit the discussion group at &lt;<a rel="nofollow" href="http://groups.google.com/group/blazeblogger/">http://groups.google.com/group/blazeblogger/</a>&gt;. You can also contact the author directly via e-mail.</p>
<h2>AUTHOR</h2>
<p> Written by Jaromir Hradilek &lt;jhradilek [at] gmail.com&gt;. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts. </p>
<p> A copy of the license is included as a file called <font SIZE="-1">FDL</font> in the main directory of the BlazeBlogger source package.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2009 Jaromir Hradilek </p>
<p> This program is free software; see the source for copying conditions. It is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT</font> <font SIZE="-1">ANY</font> <font SIZE="-1">WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS</font> <font SIZE="-1">FOR</font> A <font SIZE="-1">PARTICULAR</font> <font SIZE="-1">PURPOSE</font>. </p>
