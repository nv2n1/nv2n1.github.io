---
title: "dh_installdocs(1)"
name: "dh_installdocs"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_installdocs/"
description: "dh_installdocs – install documentation into package build directories"
---

<h2 class="name">NAME</h2>
<p> dh_installdocs &#8211; install documentation into package build directories </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_installdocs</code> [<i>debhelper options</i>] [<code>-A</code>] [<code>-X</code><i>item</i>] [<i>file</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_installdocs</code> is a debhelper program that is responsible for installing documentation into <i>usr/share/doc/package</i> in package build directories. </p>
<p> In compat 10 and earlier, <i><a href="/docs/linux/man/1-dh_install/">dh_install</a></i>(1) may be a better tool for handling the upstream documentation, when upstream&#8217;s own build system installs all the desired documentation correctly. In this case, <code>dh_installdocs</code> is still useful for installing packaging related documentation (e.g. the <i>debian/copyright</i> file). </p>
<p> From debhelper compatibility level 11 on, <code>dh_install</code> will fall back to looking in <i>debian/tmp</i> for files, if it does not find them in the current directory (or wherever you&#8217;ve told it to look using <code>&#8211;sourcedir</code>). </p>
<p> In compat 11 and later, <code>dh_installdocs</code> offers many of the features that <i><a href="/docs/linux/man/1-dh_install/">dh_install</a></i>(1) also have. Furthermore, <code>dh_installdocs</code> also supports the <code>nodoc</code> build profile to exclude documentation (regardless of compat level).</p>
<h2>FILES</h2>
<dl>
<dt>debian/<i>package</i>.docs</p>
<dd> List documentation files to be installed into <i>package</i>.</p>
<dt><i>debian/copyright</i></p>
<dd> The copyright file is installed into all packages, unless a more specific copyright file is available.</p>
<dt>debian/<i>package</i>.copyright</p>
<dd>
<dt>debian/<i>package</i>.README.Debian</p>
<dd>
<dt>debian/<i>package</i>.TODO</p>
<dd> Each of these files is automatically installed if present for a <i>package</i>.</p>
<dt><i>debian/README.Debian</i></p>
<dd>
<dt><i>debian/TODO</i></p>
<dd> These files are installed into the first binary package listed in debian/control. </p>
<p> Note that <i></i><font SIZE="-1"><i>README</i></font><i>.debian</i> files are also installed as <i></i><font SIZE="-1"><i>README</i></font><i>.Debian</i>, and <i></i><font SIZE="-1"><i>TODO</i></font><i></i> files will be installed as <i></i><font SIZE="-1"><i>TODO</i></font><i>.Debian</i> in non-native packages.</p>
<dt>debian/<i>package</i>.doc-base</p>
<dd> Installed as doc-base control files. Note that the doc-id will be determined from the <code>Document:</code> entry in the doc-base control file in question. In the event that multiple doc-base files in a single source package share the same doc-id, they will be installed to usr/share/doc-base/package instead of usr/share/doc-base/doc-id.</p>
<dt>debian/<i>package</i>.doc-base.*</p>
<dd> If your package needs to register more than one document, you need multiple doc-base files, and can name them like this. In the event that multiple doc-base files of this style in a single source package share the same doc-id, they will be installed to usr/share/doc-base/package-* instead of usr/share/doc-base/doc-id.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-A</code>, <code>&#8211;all</code></p>
<dd> Install all files specified by command line parameters in <font SIZE="-1">ALL</font> packages acted on.</p>
<dt><code>-X</code><i>item</i>, <code>&#8211;exclude=</code><i>item</i></p>
<dd> Exclude files that contain <i>item</i> anywhere in their filename from being installed. Note that this includes doc-base files.</p>
<dt><code>&#8211;sourcedir=</code><i>dir</i></p>
<dd> Look in the specified directory for files to be installed. This option requires compat 11 or later (it is silently ignored in compat 10 or earlier). </p>
<p> Note that this is not the same as the <code>&#8211;sourcedirectory</code> option used by the <code>dh_auto_</code><i>*</i> commands. You rarely need to use this option, since <code>dh_installman</code> automatically looks for files in <i>debian/tmp</i> in debhelper compatibility level 11 and above.</p>
<dt><code>&#8211;doc-main-package=</code><i>main-package</i></p>
<dd> Set the main package for a documentation package. This is used to install the documentation of the documentation package in <i>/usr/share/doc/main-package</i> as recommended by the Debian policy manual 3.9.7 in §12.3. </p>
<p> In compat 11 (or later), this option is only useful if debhelper&#8217;s auto-detection of the main package is wrong. The option can also be used to silence a warning from debhelper when the auto-detection fails but the default happens to be correct. </p>
<p> This option cannot be used when <code>dh_installdocs</code> is instructed to act on multiple packages. If you need this option, you will generally need to combine it with <code>-p</code> to ensure exactly one package is acted on. </p>
<p> Please keep in mind that some documentation (the copyright file, <font SIZE="-1">README</font>.Debian, etc.) will be unaffected by this option.</p>
<dt><code>&#8211;link-doc=</code><i>package</i></p>
<dd> Make the documentation directory of all packages acted on be a symlink to the documentation directory of <i>package</i>. This has no effect when acting on <i>package</i> itself, or if the documentation directory to be created already exists when <code>dh_installdocs</code> is run. To comply with policy, <i>package</i> must be a binary package that comes from the same source package. </p>
<p> debhelper will try to avoid installing files into linked documentation directories that would cause conflicts with the linked package. The <code>-A</code> option will have no effect on packages with linked documentation directories, and <i>copyright</i>, <i>changelog</i>, <i></i><font SIZE="-1"><i>README</i></font><i>.Debian</i>, and <i></i><font SIZE="-1"><i>TODO</i></font><i></i> files will not be installed. </p>
<p> (An older method to accomplish the same thing, which is still supported, is to make the documentation directory of a package be a dangling symlink, before calling <code>dh_installdocs</code>.) </p>
<p> Please note that this option only applies to the documentation directory for the package itself. When the package ships documentation for another package (e.g. see <code>&#8211;doc-main-package</code>), it will not use a symlink for the documentation of the other package. </p>
<p> <font SIZE="-1"><code>CAVEAT 1</code></font>: If a previous version of the package was built without this option and is now built with it (or vice-versa), it requires a &#8220;dir to symlink&#8221; (or &#8220;symlink to dir&#8221;) migration. Since debhelper has no knowledge of previous versions, you have to enable this migration itself. </p>
<p> This can be done by providing a &quot;debian/<i>package</i>.maintscript&quot; file and using <i><a href="/docs/linux/man/1-dh_installdeb/">dh_installdeb</a></i>(1) to provide the relevant maintainer script snippets. </p>
<p> <font SIZE="-1"><code>CAVEAT 2</code></font>: The use of <code>&#8211;link-doc</code> should only be done when the packages have same &#8220;architecture&#8221; type. A link from a architecture independent package to a architecture dependent package (or vice versa) will not work. Since compat 10, debhelper will actively reject unsupported combinations.</p>
<dt><i>file</i> &#8230;</p>
<dd> Install these files as documentation into the first package acted on. (Or in all packages if <code>-A</code> is specified).</dl>
<h2>EXAMPLES</h2>
<p> This is an example of a <i>debian/package.docs</i> file: </p>
<pre>
  README
  TODO
  debian/notes-for-maintainers.txt
  docs/manual.txt
  docs/manual.pdf
  docs/manual-html/
</pre>
<h2>NOTES</h2>
<p> Note that <code>dh_installdocs</code> will happily copy entire directory hierarchies if you ask it to (similar to <code>cp -a</code>). If it is asked to install a directory, it will install the complete contents of the directory.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Joey Hess &lt;joeyh [at] debian.org&gt; </p>
<h2>Index</h2>
