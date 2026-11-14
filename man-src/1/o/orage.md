---
title: "orage(1)"
name: "orage"
section: "1"
letter: "o"
url: "/docs/linux/man/1-orage/"
description: "orage – Calendar for the Xfce Desktop Environment"
---

<h2 class="name">NAME</h2>
<p> orage &#8211; Calendar for the Xfce Desktop Environment </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>orage</code> [options] [[FILE]&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>orage</code></p>
<dd>is a fast and easy to use graphical calendar for the Xfce Desktop Environment. It uses portable ical format and includes common calendar features like repeating appointments and multiple alarming possibilities. <code>orage</code> does not have group calendar features, but can only be used for single user. </p>
<p> <code>orage</code> takes a list of <i>FILE</i>s for ical files that should be imported. Contents of those files are read and converted into <code>orage</code>, but those files are left untouched. </p>
<p> For a more detailed explanation of <code>orage</code>, please see the Help menu.</p>
<h2>OPTIONS</h2>
<p> <code>-v</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print version information and exit.</dl>
<p> <code>-?</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print brief help and exit.</dl>
<p> <code>-p</code>, <code>&#8211;preferences</code></p>
<dl>
<dt>
<dd> Open the preferences setting window.</dl>
<p> <code>-t</code>, <code>&#8211;toggle</code></p>
<dl>
<dt>
<dd> Hide <code>orage</code> if it is visible and show it if it is hidden.</dl>
<p> <code>-a</code>, <code>&#8211;add-foreign file [RW]</code></p>
<dl>
<dt>
<dd> Add a foreign file into <code>orage</code>. By default this file is read-only but adding RW after the filename makes it writeable.</dl>
<p> <code>-r</code>, <code>&#8211;remove-foreign file</code></p>
<dl>
<dt>
<dd> Remove foreign file from <code>orage</code>. The file itself is not removed or modified. If you want to remove it, you need to do that separately using proper operating system command.</dl>
<h2>FILES</h2>
<p> All <code>orage</code> datafiles are by default in <i>~/.local/share/orage</i> and all configuration files are in <i>~/.config/orage</i>. (Note that you can change these locations, so if you do not find them, check from the UI.)</p>
<h2>BUGS</h2>
<p> Please report any bugs and enhancement requests to <i><a rel="nofollow" href="http://bugzilla.xfce.org/">http://bugzilla.xfce.org/</a></i>. Usage related questions can be sent to <i>xfce [at] xfce.org</i> email list.</p>
<h2>HOMEPAGE</h2>
<p> <i><a rel="nofollow" href="http://www.xfce.org/projects/orage/">http://www.xfce.org/projects/orage/</a></i></p>
<h2>AUTHOR</h2>
<p> <code>orage</code> was originally written by Mickael Graf and is now being maintained by Juha Kautto &lt;juha [at] xfce.org&gt;. </p>
<p> This manual page was written by Juha Kautto &lt;juha [at] xfce.org&gt;. </p>
<h2>Index</h2>
