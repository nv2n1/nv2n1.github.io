---
title: "update-fonts-scale(8)"
name: "update-fonts-scale"
section: "8"
letter: "u"
url: "/docs/linux/man/8-update-fonts-scale/"
description: "update-fonts-scale – generate fonts.scale files"
---

<p>update-fonts-scale &#8211; generate fonts.scale files</p>
<h2>Synopsis</h2>
<p><code>update-fonts-scale</code> [<i>OPTION</i>] <i>directory &#8230;</i></p>
<h2>Description</h2>
<p><code>update-fonts-scale</code> assembles a <i>fonts.scale</i> file in an X font directory using one or more scale files found in a subdirectory of <i>/etc/X11/fonts/</i>. It is typically invoked only from the post-installation and post-removal scripts of a package containing scalable fonts usable by the X Window System whose X LFD font names are not in the font files themselves, but may be invoked at any time to reconstruct <i>fonts.scale</i> files. For each <i>directory</i>, which is either an absolute path to an X font directory or (preferably) simply the last component of its path (such as &#8217;75dpi&#8217; or &#8216;misc&#8217;), <code>update-fonts-scale</code> will assemble either <i>/usr/lib/X11/fonts/</i>directory<i>/fonts.scale</i> or <i>/usr/share/fonts/X11/</i>directory<i>/fonts.scale</i> from the index files found at <i>/etc/X11/fonts/</i>directory<i>/</i>package<i>.scale</i>, where <i>package</i> is the name of the package installing the fonts. </p>
<p> This enables multiple packages to provide names for fonts in the same directory. No font package actually provides the <i>fonts.scale</i> file in the X font directory itself, so there is no danger of overwriting one package&#8217;s font names with those of another. </p>
<p> For instance, the two packages &#8216;xfonts-scalable&#8217; (real) and &#8216;xfonts-nifty&#8217; (hypothetical) may both install fonts into the directory <i>/usr/lib/X11/fonts/Type1</i>. They each place their <i>fonts.scale</i> files in <i>/etc/X11/fonts/Type1/xfonts-scalable.scale</i> and <i>/etc/X11/fonts/Type1/xfonts-nifty.scale</i> (respectively). <code>update-fonts-scale</code> concatenates these two files (as well as any others that match <i>/etc/X11/fonts/Type1/*.scale</i>) into <i>/usr/lib/X11/fonts/Type1/fonts.scale</i>. </p>
<p> The format for <i>fonts.scale</i> files is given in the <code><a href="//www.systutorials.com/docs/linux/man/1x-mkfontdir/">mkfontdir</a></code>(1x) manual page. </p>
<p> An example of how to use <code>update-fonts-scale</code> in package maintainer scripts is provided in the Debian Policy Manual.</p>
<h2>Options</h2>
<p><code>-h</code>, <code>&#8211;help</code> displays a brief usage message and exits.</p>
<h2>Operands</h2>
<p><code>update-fonts-scale</code> takes one or more X font directory names to operate on as operands. Only the final path component of the directory name should be specified; e.g.,</p>
<dl>
<dd><code>update-fonts-scale 75dpi</code></dl>
<p> is correct, while &#8216;<code>update-fonts-scale /usr/X11R6/lib/X11/fonts/75dpi</code>&#8216; and &#8216;<code>update-fonts-scale /usr/lib/X11/fonts/75dpi</code>&#8216; are not.</p>
<h2>Environment</h2>
<dl>
<dt><code>COLUMNS</code></p>
<dd>indicates the width of the terminal device in character cells. This value is used for formatting diagnostic messages. If not set, the terminal is queried using <code><a href="/docs/linux/man/1-stty/">stty</a></code>(1) to determine its width. If that fails, a value of &#8217;80&#8217; is assumed.</p>
<dt><code>DEBUG</code></p>
<dd>determines whether low-level diagnostic messages are issued to standard error output. A null (empty) or unset value indicates that they are not, and a non-null value indicates that they are.</dl>
<h2>Diagnostics</h2>
<h3>Errors</h3>
<dl>
<dt><code>usage error: one or more font directories must be provided</code></p>
<dd><code>update-fonts-scale</code> was invoked without operands. Supply one or more X font directory names to operate on.</p>
<dt><code>usage error: unrecognized option</code></p>
<dd><code>update-fonts-scale</code> was invoked with an unrecognized option argument. Use only the options documented in &#8220;OPTIONS&#8221;, above.</p>
<dt><code>fatal error: path to X font directory must be used</code></p>
<dd>A directory name was supplied that was not an X font directory name. Supply X font directory names only.</dl>
<h3>Warnings</h3>
<dl>
<dt><code>warning: absolute path </code><i>directory</i><code> was provided</code></p>
<dd>Usage of absolute paths is deprecated. Use only the final component of the X font directory name for <i>directory</i>.</p>
<dt><code>warning: </code><i>directory</i><code> does not exist or is not a directory</code></p>
<dd>The supplied <i>directory</i> was invalid. <code>update-fonts-scale</code> skipped it.</dl>
<h3>Notes</h3>
<p>Notes are only displayed under special circumstances; see &#8220;ENVIRONMENT&#8221;. above.</p>
<dl>
<dt><code>note: </code><i>index</i><code> references nonexistent font file </code><i>filename</i></p>
<dd>The index file <i>/etc/X11/fonts/</i>directory<i>/</i>package<i>.scale</i>, refers to a nonexistent font file, <i>filename</i>. This is normal when <i>package</i> has been removed, but not purged from the system. In other circumstances, it likely indicates an error in <i>package</i>.</dl>
<h2>Exit Status</h2>
<dl>
<dt>0</p>
<dd><code>update-fonts-scale</code> ran successfully.</p>
<dt>1</p>
<dd><code>update-fonts-scale</code> experienced a fatal error; see the section on diagnostic messages above.</p>
<dt>2</p>
<dd><code>update-fonts-scale</code> was invoked with invalid arguments.</dl>
<h2>Bugs</h2>
<p>See the Debian Bug Tracking System &lt;URL: <a rel="nofollow" href="https://bugs.debian.org/xfonts-utils">https://bugs.debian.org/xfonts-utils</a> &gt;. If you wish to report a bug in <code>update-fonts-scale</code>, please see <i>/usr/share/doc/debian/bug-reporting.txt</i> or the <code><a href="/docs/linux/man/1-reportbug/">reportbug</a></code>(1) command.</p>
<h2>Author</h2>
<p><code>update-fonts-scale</code> was written by Branden Robinson.</p>
<h2>See Also</h2>
<p><code><a href="//www.systutorials.com/docs/linux/man/1x-mkfontdir/">mkfontdir</a></code>(1x) </p>
