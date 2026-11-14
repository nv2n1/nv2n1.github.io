---
title: "thunar(1)"
name: "thunar"
section: "1"
letter: "t"
url: "/docs/linux/man/1-thunar/"
description: "Thunar – File Manager for the Xfce Desktop Environment"
---

<h2 class="name">NAME</h2>
<p> Thunar &#8211; File Manager for the Xfce Desktop Environment </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>Thunar</code> [options] [[URI]&#8230;]</p>
<dt> <code>Thunar</code> [options] &#8211;bulk-rename [[URI]&#8230;]</p>
<dt> <code>Thunar</code> [options] &#8211;quit</dl>
<h2>DESCRIPTION</h2>
<p> <code>Thunar</code></p>
<dd>is a fast and easy to use file manager for the Xfce Desktop Environment. It has been designed from the ground up to be lighweight with special focus on usability. Its user interface is clean and intuitive, and does not include any confusing or useless options.</p>
<h2>INVOCATION</h2>
<p> <code>Thunar</code> takes a list of <i>URI</i>s for folders that should be opened in new file manager windows or files that should be run using the default application for their types. The <i>URI</i>s may be specified as either <code>file:</code> or <code>trash:</code> URIs, absolute paths or paths relative to the current directory from which <code>Thunar</code> is being invoked. If no <i>URI</i>s are specified, the current folder will be opened in a new file manager window. </p>
<p> When the <code>&#8211;bulk-rename</code> option is specified no file managers windows will be opened, but instead the <i>URI</i>s will be passed to the bulk renamer. The bulk renamer allows to rename several files or folders at once using different renamer modules.</p>
<h3>Options</h3>
<p> <code>-?</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print brief help and exit.</dl>
<p> <code>-v</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print version information and exit.</dl>
<p> <code>-B</code>, <code>&#8211;bulk-rename</code></p>
<dl>
<dt>
<dd> Open the <i>URI</i>s in a standalone window of the bulk renamer.</dl>
<p> <code>&#8211;daemon</code></p>
<dl>
<dt>
<dd> Do not terminate the <code>Thunar</code> instance when the last window is closed, but keep it running to speed up opening new windows later on. This is the default when spawning <code>Thunar</code> as part of the default Xfce session or when using D-Bus activation.</dl>
<p> <code>&#8211;display=DISPLAY</code></p>
<dl>
<dt>
<dd> Use the specified X <code>DISPLAY</code> for the user interface.</dl>
<p> <code>-q</code>, <code>&#8211;quit</code></p>
<dl>
<dt>
<dd> Terminate any <code>Thunar</code> instance running in the background (spawned using the <code>&#8211;daemon</code> option). This command should be used whenever <code>Thunar</code> is upgraded to a new version to ensure that no old instance is reused.</dl>
<h2>AUTHOR</h2>
<p> <code>Thunar</code> was written by Benedikt Meurer &lt;benny [at] xfce.org&gt;. </p>
<p> This manual page was written by Benedikt Meurer &lt;benny [at] xfce.org&gt;. </p>
<h2>Index</h2>
