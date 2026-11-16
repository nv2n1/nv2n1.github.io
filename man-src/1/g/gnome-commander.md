---
title: "gnome-commander(1)"
name: "gnome-commander"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gnome-commander/"
description: "gnome-commander – a GNOME file manager"
---

<h2 class="name">NAME</h2>
<p> gnome-commander &#8211; a GNOME file manager </p>
<h2>SYNOPSIS</h2>
<p> <code>gnome-commander</code> [-d STRING] [options] [gtk,gnome,bonobo options] </p>
<h2>DESCRIPTION</h2>
<p> <code>GNOME Commander</code> is a fast and powerful graphical filemanager for the GNOME desktop environment, it has a &quot;two-pane&quot; interface in the tradition of Norton and Midnight Commander.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></dt>
<dd> Show summary of options.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Show version of program.</dd>
<dt><code>-l, &#8211;start-left-dir=STRING</code></dt>
<dd> Specify the start directory for the left pane</dd>
<dt><code>-r, &#8211;start-right-dir=STRING</code></dt>
<dd> Specify the start directory for the right pane</dd>
<dt><code>&nbsp;<wbr> &#8211;config-dir=STRING</code></dt>
<dd> Specify the directory for configuration files</dd>
<dt><code>-d, &#8211;debug=STRING</code></dt>
<dd> Specify debug flags to use. Debug output will be written to STDOUT.<br />
 Possible flags:<br />
 a: set all debug flags<br />
 c: file and directory counting<br />
 d: directory ref-counting<br />
 f: file ref-counting<br />
 g: run_command debugging<br />
 i: imageloader<br />
 k: directory pool<br />
 l: directory listings<br />
 m: connection debugging<br />
 n: directory monitoring<br />
 p: python plugins<br />
 s: SMB network browser<br />
 t: metadata tags<br />
 u: user actions debugging<br />
 v: internal viewer<br />
 w: widget_lookup<br />
 x: xfer<br />
 y: brief MIME based imageload<br />
 z: detailed MIME based imageload </dd>
<dt><code>[gtk,gnome,bonobo options]</code></dt>
<dd> Standard gtk, gnome, bonobo options are supported. Use <code>&#8211;help</code> to see possible options.</dd></dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>gnome-commander -d nvl</code></dt>
<dd> Starts <code>GNOME Commander</code> with debugging of directory listings, internal viewer and directory monitoring facilities.</dd></dl>
<h2>FILES</h2>
<dl>
<dt><code>~/.gnome-commander/gnome-commander.xml</code></dt>
<dd>
</dd><dt>
</dt><dt><code>~/.gnome-commander/devices</code></dt>
<dd>
</dd><dd> List of user defined devices (see &quot;Devices&quot; tab in the &quot;Options&quot; dialog).</dd>
<dt><code>~/.gnome-commander/fav-apps</code></dt>
<dd> List of user defined applications (see &quot;Programs&quot; tab in the &quot;Options&quot; dialog).</dd>
<dt><code>~/.gnome-commander/plugins</code></dt>
<dd> User specific plugins.</dd>
<dt><code>/usr/lib/gnome-commander/plugins</code></dt>
<dd> System-wide plugins.</dd></dl>
<h2>BUGS</h2>
<p> If you find any bugs, please report them (or better yet, fix them and send a patch). See the <code>GNOME Commander</code> home page for more information:<br />
 <a rel="nofollow" href="http://gcmd.github.io/">http://gcmd.github.io/</a></p>
<h2>AUTHOR</h2>
<p> <code>GNOME Commander</code> was originally developed by Marcus Bjurman from 2001 till 2004. Assaf Gordon added the internal viewer code and other features. Piotr Eljasiak was the project manager from 2006 until 2012. Since 2013 till now, Uwe Scholz &lt;u.scholz83 [at] gmx.de&gt; is the current project manager.<br />
 Translations and other contributions where made by numerous people. See the <code>AUTHORS</code> file in the source tarball for the detailed list. </p>
<p> The original manual page was written by Michael Vogt &lt;mvo [at] debian.org&gt;, for the Debian GNU/Linux system. Current manual page is maintained as the part of the <code>GNOME Commander</code> project. </p>
<h2>Index</h2>
