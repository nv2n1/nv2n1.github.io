---
title: "gv-update-userconfig(1)"
name: "gv-update-userconfig"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gv-update-userconfig/"
description: "gv-update-userconfig – update ~/.gv config file"
---

<h2>NAME</h2>
<p> gv-update-userconfig &#8211; update ~/.gv config file</p>
<h2>SYNOPSIS</h2>
<p> <code>gv-update-userconfig</code> [<i>filename</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>gv-update-userconfig</code> is a simple script to update an <code>.gv</code> config file to the current version of <code><a href="/docs/linux/man/1-gv/">gv</a></code>(1). </p>
<p> You can specify a file which is used instead of <code>.gv</code> by using the optional filename argument. This is useful if the environment variable XUSERSEARCHPATH is used. </p>
<p> This is done by removing all entries known to cause problems with the current version of GNU gv (i.e. the one the version of this program belongs to) and updating the version information in that file. This resets all problematic items back to the default values. </p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code>, <code>&#8211;usage</code></p>
<dd> displays a short help message</p>
<dt><code>-r</code></p>
<dd> removes all resources from <i>~</i><code>/.gv</code> that equal the default resources being shipped with GNU gv (ignoring whitespaces).</p>
<dt><code>-n</code></p>
<dd> switches to alternative navigation by adding resp. updating navigation resources to <i>~</i><code>/.gv</code>, i. e. after each page switch (except if selected by the page number) the page is scrolled to top (if switching forward) resp. to the bottom (if switching backward).</p>
<dt><code>-N</code></p>
<dd> switches to standard navigation by adding resp. updating navigation resources to <i>~</i><code>/.gv</code>.</p>
<dt><code>-s</code></p>
<dd> removes navigation resources from <i>~</i><code>/.gv</code> and therefore enables standard navigation.</p>
<dt><code>-i</code></p>
<dd> updates translation file. Using the optional filename parameter is strongly recommended for using this option. This option cannot be used together with any of the other options. </p>
</dl>
<h2>BACKGROUND</h2>
<p> The <i>$(HOME)</i><code>/.gv</code> file is written by GNU gv when activating the <code>Save</code> button in one of the configuration dialogs. </p>
<p> The values in there are used, if there is no display-specific resource value (loaded from <i>$(HOME)</i><code>/.Xresources</code> at login time or manually <code><a href="/docs/linux/man/1-xrdb/">xrdb</a></code>(1)). </p>
<p> Sometimes older values miss things needed by the new GNU gv to work properly. This GNU gv will notice old (or missing) version information in this file and refuse to start until fixed. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gv/">gv</a></code>(1), <code><a href="/docs/linux/man/1-xrdb/">xrdb</a></code>(1). </p>
<h2>COPYRIGHT</h2>
<p> This manpage is Copyright &#169; 2008 Bernhard R. Link and can be used, copied, distributed and/or modified without restrictions.<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>Index</h2>
