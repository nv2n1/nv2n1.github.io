---
title: "update-fonts-alias(8)"
name: "update-fonts-alias"
section: "8"
letter: "u"
url: "/docs/linux/man/8-update-fonts-alias/"
description: "update-fonts-alias – compile fonts.alias files"
---

<p>update-fonts-alias &#8211; compile fonts.alias files</p>
<h2>Synopsis</h2>
<p><code>update-fonts-alias</code> [<i>OPTION</i>] <i>directory &#8230;</i></p>
<h2>Description</h2>
<p><code>update-fonts-alias</code> assembles a <i>fonts.alias</i> file in an X font directory using one or more alias files found in a subdirectory of <i>/etc/X11/fonts/</i>. It is typically invoked only from the post-installation and post-removal scripts of a <i>package</i> containing X Window System fonts that provide aliases for their XLFD names, but may be invoked at any time to reconstruct <i>fonts.alias</i> files. For each <i>directory</i>, which is simply the last component of its path (such as &#8217;75dpi&#8217; or &#8216;misc&#8217;), <code>update-fonts-alias</code> will assemble either <i>/usr/lib/X11/fonts/</i>directory<i>/fonts.alias</i> or <i>/usr/share/fonts/X11/</i>directory<i>/fonts.alias</i> from the files found in <i>/etc/X11/fonts/</i>directory<i>/</i>package<i>.alias</i>. </p>
<p> This enables multiple packages to provide aliases for fonts in the same directory. No font package actually provides the <i>fonts.alias</i> file in the X font directory itself, so there is no danger of overwriting one package&#8217;s aliases with those of another. </p>
<p> For instance, the two packages &#8216;xfonts-base&#8217; and &#8216;xfonts-base-transcoded&#8217; may both install fonts into the directory <i>/usr/lib/X11/fonts/misc</i>. They each place their <i>fonts.alias</i> files in <i>/etc/X11/fonts/misc/xfonts-base.alias</i> and <i>/etc/X11/fonts/misc/xfonts-base-transcoded.alias</i> (respectively). <code>update-fonts-alias</code> concatenates these two files (as well as any others that match <i>/etc/X11/fonts/misc/*.alias</i>) into <i>/usr/lib/X11/fonts/misc/fonts.alias</i>. </p>
<p> The format of <i>fonts.alias</i> files is described in the <code><a href="//www.systutorials.com/docs/linux/man/1x-mkfontdir/">mkfontdir</a></code>(1x) manual page. </p>
<p> An example of how to use <code>update-fonts-alias</code> in package maintainer scripts is provided in the Debian Policy Manual.</p>
<h2>Options</h2>
<p><code>-h</code>, <code>&#8211;help</code> displays a brief usage message and exits.</p>
<h2>Operands</h2>
<p><code>update-fonts-alias</code> takes one or more X font directory names to operate on as operands. Only the final path component of the directory name should be specified; e.g.,</p>
<dl>
<dd><code>update-fonts-alias 75dpi</code></dl>
<p> is correct, while &#8216;<code>update-fonts-alias /usr/X11R6/lib/X11/fonts/75dpi</code>&#8216; and &#8216;<code>update-fonts-alias /usr/lib/X11/fonts/75dpi</code>&#8216; are not.</p>
<h2>Environment</h2>
<dl>
<dt><code>COLUMNS</code></p>
<dd>indicates the width of the terminal device in character cells. This value is used for formatting diagnostic messages. If not set, the terminal is queried using <code><a href="/docs/linux/man/1-stty/">stty</a></code>(1) to determine its width. If that fails, a value of &#8217;80&#8217; is assumed.</dl>
<h2>Diagnostics</h2>
<h3>Errors</h3>
<dl>
<dt><code>usage error: one or more font directories must be provided</code></p>
<dd><code>update-fonts-alias</code> was invoked without operands. Supply one or more X font directory names to operate on.</p>
<dt><code>usage error: unrecognized option</code></p>
<dd><code>update-fonts-alias</code> was invoked with an unrecognized option argument. Use only the options documented in &#8220;OPTIONS&#8221;, above.</p>
<dt><code>fatal error: path to X font directory must be used</code></p>
<dd>A directory name was supplied that was not an X font directory name. Supply X font directory names only.</dl>
<h3>Warnings</h3>
<dl>
<dt><code>warning: absolute path </code><i>directory</i><code> was provided</code></p>
<dd>Usage of absolute paths is deprecated. Use only the final component of the X font directory name for <i>directory</i>.</p>
<dt><code>warning: </code><i>directory</i><code> does not exist or is not a directory</code></p>
<dd>The supplied <i>directory</i> was invalid. <code>update-fonts-alias</code> skipped it.</dl>
<h2>Exit Status</h2>
<dl>
<dt>0</p>
<dd><code>update-fonts-alias</code> ran successfully.</p>
<dt>1</p>
<dd><code>update-fonts-alias</code> experienced a fatal error; see the section on diagnostic messages above.</p>
<dt>2</p>
<dd><code>update-fonts-alias</code> was invoked with invalid arguments.</dl>
<h2>Bugs</h2>
<p>See the Debian Bug Tracking System &lt;URL: <a rel="nofollow" href="https://bugs.debian.org/xfonts-utils">https://bugs.debian.org/xfonts-utils</a> &gt;. If you wish to report a bug in <code>update-fonts-alias</code>, please see <i>/usr/share/doc/debian/bug-reporting.txt</i> or the <code><a href="/docs/linux/man/1-reportbug/">reportbug</a></code>(1) command.</p>
<h2>Author</h2>
<p><code>update-fonts-alias</code> was written by Branden Robinson.</p>
<h2>See Also</h2>
<p><code><a href="//www.systutorials.com/docs/linux/man/1x-mkfontdir/">mkfontdir</a></code>(1x) </p>
