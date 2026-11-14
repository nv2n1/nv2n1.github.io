---
title: "dh_installman(1)"
name: "dh_installman"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_installman/"
description: "dh_installman – install man pages into package build directories"
---

<h2 class="name">NAME</h2>
<p> dh_installman &#8211; install man pages into package build directories </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_installman</code> [<i>debhelper options</i>] [<i>manpage</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_installman</code> is a debhelper program that handles installing man pages into the correct locations in package build directories. </p>
<p> In compat 10 and earlier, this program was primarily for when upstream&#8217;s build system does not properly install them as a part of its install step (or it does not have an install step). In compat 11 and later, it supports the same features of <i><a href="/docs/linux/man/1-dh_install/">dh_install</a></i>(1) and has the advantage that it respects the <code>nodoc</code> build profile (unlike <i><a href="/docs/linux/man/1-dh_install/">dh_install</a></i>(1)). </p>
<p> Even if you prefer to use <i><a href="/docs/linux/man/1-dh_install/">dh_install</a></i>(1) for installing the manpages, <code>dh_installman</code> can still be useful for converting the manpage encoding to <font SIZE="-1">UTF-8</font> and for converting <i>.so</i> links (as described below). However, that part happens automatically without any explicit configuration. </p>
<p> You tell <code>dh_installman</code> what man pages go in your packages, and it figures out where to install them based on the section field in their <code>.TH</code> or <code>.Dt</code> line. If you have a properly formatted <code>.TH</code> or <code>.Dt</code> line, your man page will be installed into the right directory, with the right name (this includes proper handling of pages with a subsection, like <code>3perl</code>, which are placed in <i>man3</i>, and given an extension of <i>.3perl</i>). If your <code>.TH</code> or <code>.Dt</code> line is incorrect or missing, the program may guess wrong based on the file extension. </p>
<p> It also supports translated man pages, by looking for extensions like <i>.ll.8</i> and <i>.ll_LL.8</i>, or by use of the <code>&#8211;language</code> switch. </p>
<p> If <code>dh_installman</code> seems to install a man page into the wrong section or with the wrong extension, this is because the man page has the wrong section listed in its <code>.TH</code> or <code>.Dt</code> line. Edit the man page and correct the section, and <code>dh_installman</code> will follow suit. See <i><a href="/docs/linux/man/7-man/">man</a></i>(7) for details about the <code>.TH</code> section, and <i><a href="/docs/linux/man/7-mdoc/">mdoc</a></i>(7) for the <code>.Dt</code> section. If <code>dh_installman</code> seems to install a man page into a directory like <i>/usr/share/man/pl/man1/</i>, that is because your program has a name like <i>foo.pl</i>, and <code>dh_installman</code> assumes that means it is translated into Polish. Use <code>&#8211;language=C</code> to avoid this. </p>
<p> After the man page installation step, <code>dh_installman</code> will check to see if any of the man pages in the temporary directories of any of the packages it is acting on contain <i>.so</i> links. If so, it changes them to symlinks. </p>
<p> Also, <code>dh_installman</code> will use man to guess the character encoding of each manual page and convert it to <font SIZE="-1">UTF-8.</font> If the guesswork fails for some reason, you can override it using an encoding declaration. See <i><a href="/docs/linux/man/1-manconv/">manconv</a></i>(1) for details. </p>
<p> From debhelper compatibility level 11 on, <code>dh_install</code> will fall back to looking in <i>debian/tmp</i> for files, if it does not find them in the current directory (or wherever you&#8217;ve told it to look using <code>&#8211;sourcedir</code>).</p>
<h2>FILES</h2>
<dl>
<dt>debian/<i>package</i>.manpages</p>
<dd> Lists man pages to be installed.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-A</code>, <code>&#8211;all</code></p>
<dd> Install all files specified by command line parameters in <font SIZE="-1">ALL</font> packages acted on.</p>
<dt><code>&#8211;language=</code><i>ll</i></p>
<dd> Use this to specify that the man pages being acted on are written in the specified language.</p>
<dt><code>&#8211;sourcedir=</code><i>dir</i></p>
<dd> Look in the specified directory for files to be installed. This option requires compat 11 or later (it is silently ignored in compat 10 or earlier). </p>
<p> Note that this is not the same as the <code>&#8211;sourcedirectory</code> option used by the <code>dh_auto_</code><i>*</i> commands. You rarely need to use this option, since <code>dh_installman</code> automatically looks for files in <i>debian/tmp</i> in debhelper compatibility level 11 and above.</p>
<dt><i>manpage</i> &#8230;</p>
<dd> Install these man pages into the first package acted on. (Or in all packages if <code>-A</code> is specified).</dl>
<h2>EXAMPLES</h2>
<p> An example <i>debian/manpages</i> file could look like this: </p>
<pre>
  doc/man/foo.1
  # Translations
  doc/man/foo.da.1
  doc/man/foo.de.1
  doc/man/foo.fr.1
  # NB: The following line is considered a polish translation
  # of &quot;foo.1&quot; (and not a manpage written in perl called &quot;foo.pl&quot;)
  doc/man/foo.pl.1
  # ...
</pre>
<h2>NOTES</h2>
<p> An older version of this program, <i><a href="/docs/linux/man/1-dh_installmanpages/">dh_installmanpages</a></i>(1), is still used by some packages, and so is still included in debhelper. It is, however, deprecated, due to its counterintuitive and inconsistent interface. Use this program instead.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Joey Hess &lt;joeyh [at] debian.org&gt; </p>
<h2>Index</h2>
