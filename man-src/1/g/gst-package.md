---
title: "gst-package(1)"
name: "gst-package"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gst-package/"
description: "gst-package – create and install GNU Smalltalk .star package files"
---

<h2>NAME</h2>
<p> gst-package &#8211; create and install GNU Smalltalk .star package files</p>
<h2>DESCRIPTION</h2>
<h3>Usage:</h3>
<dl>
<dt>
<dd> gst-package [OPTION]&#8230; ARGS&#8230;</dl>
<h3>Operation modes:</h3>
<dl>
<dt><code>&#8211;install</code></p>
<dd> make or install STAR packages (default)</p>
<dt><code>&#8211;uninstall</code></p>
<dd> remove the packages mentioned in the FILES</p>
<dt><code>&#8211;dist</code></p>
<dd> copy files instead of creating STAR files.</p>
<dt><code>&#8211;prepare</code></p>
<dd> create configure.ac or Makefile.am</p>
<dt><code>&#8211;list-files</code> PKG</p>
<dd> just output the list of files in the package</p>
<dt><code>&#8211;list-packages</code></p>
<dd> just output the list of packages in the files</p>
<dt><code>&#8211;download</code>, <code>&#8211;update</code></p>
<dd> download package from smalltalk.gnu.org or from its specified URL</p>
<dt><code>&#8211;help</code></p>
<dd> display this message and exit</p>
<dt><code>&#8211;version</code></p>
<dd> print version information and exit</dl>
<h3>Common suboptions:</h3>
<dl>
<dt><code>-n</code>, <code>&#8211;dry-run</code></p>
<dd> print commands without running them</p>
<dt><code>&#8211;srcdir</code> DIR</p>
<dd> look for non-built files in directory DIR</p>
<dt><code>&#8211;distdir</code> DIR</p>
<dd> for <code>&#8211;dist</code>, place files in directory DIR</p>
<dt><code>&#8211;destdir</code> DIR</p>
<dd> prefix the destination directory with DIR</p>
<dt><code>&#8211;target-directory</code> DIR</p>
<dd> install the files in DIR (unused for <code>&#8211;dist</code>)</p>
<dt><code>-I</code>, <code>&#8211;image-file</code>=<i>FILE</i></p>
<dd> load into the specified image</p>
<dt><code>&#8211;kernel-dir</code>=<i>PATH</i></p>
<dd> use the specified kernel directory</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> print extra information while processing</dl>
<h3>&#8211;install suboptions:</h3>
<dl>
<dt><code>&#8211;test</code></p>
<dd> run unit tests after merging</p>
<dt><code>&#8211;load</code></p>
<dd> also load the Smalltalk files in the image</dl>
<h3>&#8211;list-files suboptions:</h3>
<dl>
<dt><code>&#8211;load</code></p>
<dd> only list files that are filed in when loading</p>
<dt><code>&#8211;test</code></p>
<dd> with <code>&#8211;load</code>, also include unit test files</p>
<dt><code>&#8211;vpath</code></p>
<dd> Omit path to srcdir for files that are there</dl>
<h3>&#8211;dist suboptions:</h3>
<dl>
<dt><code>&#8211;all-files</code></p>
<dd> Process all files, not just non-built ones</p>
<dt><code>&#8211;copy</code></p>
<dd> Do not create symbolic links</dl>
<p> All operation modes except <code>&#8211;download</code> (or its synonym <code>&#8211;update</code>) accept paths to package.xml files or .star files, including remote URLs. <code>&#8211;download</code> and <code>&#8211;update</code> accept names of packages, which will be searched in the current system or on smalltalk.gnu.org) or URLs to package.xml or .star files. </p>
<p> Except in uninstall and list files mode, gst-package requires write access to the GNU Smalltalk image directory, and merges the XML package files on the command line with that file. </p>
<p> The default target directory is /builddir/build/BUILD/smalltalk-3.2.5</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>gst-package</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>gst-package</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info gst</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
