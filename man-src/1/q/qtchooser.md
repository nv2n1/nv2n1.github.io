---
title: "qtchooser(1)"
name: "qtchooser"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qtchooser/"
description: "qtchooser – a wrapper used to select between Qt development binary versions"
---

<h2 class="name">NAME</h2>
<p> qtchooser &#8211; a wrapper used to select between Qt development binary versions </p>
<h2>SYNOPSIS</h2>
<p> <code>qtchooser</code> <code>-list-versions</code><br />
 <code>qtchooser</code> <code>-print-env</code> [<code>-qt=</code><i>version</i>]<br />
 <code>qtchooser</code> <code>-run-tool=</code><i>tool</i> [<code>-qt=</code><i>version</i>] [<i>program_arguments</i>]<br />
 <code>&lt;executable_name&gt;</code> [<code>-qt=</code><i>version</i>] [<i>program_arguments</i>] </p>
<h2>DESCRIPTION</h2>
<p> Qt is a cross-platform C++ application framework. Qt&#8217;s primary feature is its rich set of widgets that provide standard GUI functionality. </p>
<p> The Qt Chooser provides a wrapper to switch between versions of Qt development binaries when multiple versions like 4 and 5 are installed or local Qt builds are to be used. </p>
<p> It is commonly used via a symlink from an <i>executable_name</i> like qmake.</p>
<h2>OPTIONS</h2>
<p> The options which apply to the <code>qtchooser</code> command are: </p>
<p> <code>-list-versions</code></p>
<dl>
<dt>
<dd> Lists available Qt versions from the configuration files</dl>
<p> <code>-print-env</code></p>
<dl>
<dt>
<dd> Prints environment information</dl>
<p> <code>-qt=</code><i>version</i></p>
<dl>
<dt>
<dd> Selects <i>version</i> as the Qt version to be used</dl>
<p> <code>-run-tool=</code><i>tool</i></p>
<dl>
<dt>
<dd> Runs the selected <i>tool</i>.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>QTCHOOSER_NO_GLOBAL_DIR</code></p>
<dd> If qtchooser has been built with <code>QTCHOOSER_GLOBAL_DIR</code> (predefined search paths for qtchooser&#8217;s configuration files, useful in some distros), setting this variable will override its effect.</p>
<dt><code>QT_SELECT</code></p>
<dd> Same as <code>-qt=</code><i>version</i>. If set, the selected configuration is used and binaries symlinked to qtchooser will be executed without additional parameters.</p>
<dt><code>XDG_CONFIG_HOME</code></p>
<dd>
<dt><code>XDG_CONFIG_DIRS</code></p>
<dd> Used as specified in &lt;<code><a rel="nofollow" href="http://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html">http://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html</a></code>&gt;</dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/xdg/qtchooser/*.conf</i></p>
<dd> System-wide configuration files. Each has two lines, the first is the path to the binaries and the second is the path to the Qt libraries. If a <i>default.conf</i> is provided, the settings from it will be automatically used in case nothing else is selected.</p>
<dt><i></i><code>$HOME</code>/.config/qtchooser/*.conf</p>
<dd> User configuration files. </p>
</dl>
<h2>AUTHOR</h2>
<p> qtchooser was written by Thiago Macieira from Intel. </p>
<p> This manual page was written by Timo Jyrinki &lt;timo [at] debian.org&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
