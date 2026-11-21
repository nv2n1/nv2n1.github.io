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
<h3>Usage:</h3>
<dl>
<dt>
</dt><dd> gst-package [OPTION]&#8230; ARGS&#8230;</dd></dl>
<h3>Operation modes:</h3>
<dl>
<dt><code>&#8211;install</code></dt>
<dd> make or install STAR packages (default)</dd>
<dt><code>&#8211;uninstall</code></dt>
<dd> remove the packages mentioned in the FILES</dd>
<dt><code>&#8211;dist</code></dt>
<dd> copy files instead of creating STAR files.</dd>
<dt><code>&#8211;prepare</code></dt>
<dd> create configure.ac or Makefile.am</dd>
<dt><code>&#8211;list-files</code> PKG</dt>
<dd> just output the list of files in the package</dd>
<dt><code>&#8211;list-packages</code></dt>
<dd> just output the list of packages in the files</dd>
<dt><code>&#8211;download</code>, <code>&#8211;update</code></dt>
<dd> download package from smalltalk.gnu.org or from its specified URL</dd>
<dt><code>&#8211;help</code></dt>
<dd> display this message and exit</dd>
<dt><code>&#8211;version</code></dt>
<dd> print version information and exit</dd></dl>
<h3>Common suboptions:</h3>
<dl>
<dt><code>-n</code>, <code>&#8211;dry-run</code></dt>
<dd> print commands without running them</dd>
<dt><code>&#8211;srcdir</code> DIR</dt>
<dd> look for non-built files in directory DIR</dd>
<dt><code>&#8211;distdir</code> DIR</dt>
<dd> for <code>&#8211;dist</code>, place files in directory DIR</dd>
<dt><code>&#8211;destdir</code> DIR</dt>
<dd> prefix the destination directory with DIR</dd>
<dt><code>&#8211;target-directory</code> DIR</dt>
<dd> install the files in DIR (unused for <code>&#8211;dist</code>)</dd>
<dt><code>-I</code>, <code>&#8211;image-file</code>=<i>FILE</i></dt>
<dd> load into the specified image</dd>
<dt><code>&#8211;kernel-dir</code>=<i>PATH</i></dt>
<dd> use the specified kernel directory</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> print extra information while processing</dd></dl>
<h3>&#8211;install suboptions:</h3>
<dl>
<dt><code>&#8211;test</code></dt>
<dd> run unit tests after merging</dd>
<dt><code>&#8211;load</code></dt>
<dd> also load the Smalltalk files in the image</dd></dl>
<h3>&#8211;list-files suboptions:</h3>
<dl>
<dt><code>&#8211;load</code></dt>
<dd> only list files that are filed in when loading</dd>
<dt><code>&#8211;test</code></dt>
<dd> with <code>&#8211;load</code>, also include unit test files</dd>
<dt><code>&#8211;vpath</code></dt>
<dd> Omit path to srcdir for files that are there</dd></dl>
<h3>&#8211;dist suboptions:</h3>
<dl>
<dt><code>&#8211;all-files</code></dt>
<dd> Process all files, not just non-built ones</dd>
<dt><code>&#8211;copy</code></dt>
<dd> Do not create symbolic links</dd></dl>
<p> All operation modes except <code>&#8211;download</code> (or its synonym <code>&#8211;update</code>) accept paths to package.xml files or .star files, including remote URLs. <code>&#8211;download</code> and <code>&#8211;update</code> accept names of packages, which will be searched in the current system or on smalltalk.gnu.org) or URLs to package.xml or .star files. </p>
<p> Except in uninstall and list files mode, gst-package requires write access to the GNU Smalltalk image directory, and merges the XML package files on the command line with that file. </p>
<p> The default target directory is /builddir/build/BUILD/smalltalk-3.2.5</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>gst-package</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>gst-package</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info gst</code></dd></dl>
<p> should give you access to the complete manual. </p>
