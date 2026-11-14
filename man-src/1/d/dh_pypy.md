---
title: "dh_pypy(1)"
name: "dh_pypy"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_pypy/"
description: "dh_pypy – calculates PyPy dependencies, adds maintainer scripts to byte compile files, etc."
---

<h2 class="name">NAME</h2>
<p> dh_pypy &#8211; calculates PyPy dependencies, adds maintainer scripts to byte compile files, etc. </p>
<h2>SYNOPSIS</h2>
<p> dh_pypy -p PACKAGE [-V [X.Y][-][A.B]] DIR [-X REGEXPR]</p>
<h2>DESCRIPTION</h2>
<h3>QUICK GUIDE FOR MAINTAINERS</h3>
<dl>
<dt>&bull;</p>
<dd> build-depend on pypy and dh-python,</p>
<dt>&bull;</p>
<dd> add <i>${pypy:Depends}</i> to Depends</p>
<dt>&bull;</p>
<dd> build module/application using its standard build system,</p>
<dt>&bull;</p>
<dd> install files to the standard locations,</p>
<dt>&bull;</p>
<dd> add <i>pypy</i> to dh&#8217;s &#8211;with option, or:</p>
<dt>&bull;</p>
<dd> call <code>dh_pypy</code> in the <i>binary-*</i> target,</dl>
<h3>NOTES</h3>
<h3>dependencies</h3>
<p> dh_pypy tries to translate Python dependencies from the <i>requires.txt</i> file to Debian dependencies. In many cases, this works without any additional configuration because dh_pypy comes with a build-in mapping of Python module names to Debian packages that is periodically regenerated from the Debian archive. By default, the version information in the Python dependencies is discarded. If you want dh_pypy to generate more strict dependencies (e.g. to avoid ABI problems), or if the automatic mapping does not work correctly for your package, you have to provide dh_pypy with additional rules for the translation of Python module to Debian package dependencies. </p>
<p> For a package <i>pypy-foo</i> that depends on a package <i>pypy-bar</i>, there are two files that may provide such rules:</p>
<dl>
<dt>1.</p>
<dd> If the <i>pypy-foo</i> source package ships with a <i>debian/pypy-overrides</i> file, this file is used by dh_pypy during the build of <i>pypy-foo</i>.</p>
<dt>2.</p>
<dd> If the <i>pypy-bar</i> source package ships with a <i>debian/pypy-bar.pydist</i> file (and uses dh_pypy), this file will be included in the binary package as <i>/usr/share/dh-python/dist/pypy/pypy-bar</i>. During the build of <i>pypy-foo</i>, dh_pypy will then find and use the file. </p>
<p> Both files have the same format described in <i>/usr/share/doc/dh-python/README.PyDist</i>. If all you want is to generate versioned dependencies (and assuming that the <i>pypy-bar</i> package provides the <i>pybar</i> Python module), in most cases it will be sufficient to put the line <code>pybar pypy-bar; PEP386</code> into either of the above files.</dl>
<h3>private dirs</h3>
<p> <i>/usr/share/foo</i>, <i>/usr/share/games/foo</i>, <i>/usr/lib/foo</i> and <i>/usr/lib/games/foo</i> private directories are scanned for Python files by default (where <i>foo</i> is binary package name). If your package is shipping Python files in some other directory, add another dh_pypy call in debian/rules with directory name as an argument &#8211; you can use different set of options in this call. If you need to change options for a private directory that is checked by default, invoke dh_pypy with &#8211;skip-private option and add another call with a path to this directory and new options.</p>
<h3>debug packages</h3>
<p> In binary packages which name ends with <i>-dbg</i>, all files in <i>/usr/lib/pypy/dist-packages/</i> directory that have extensions different than <i>so</i> or <i>h</i> are removed by default. Use &#8211;no-dbg-cleaning option to disable this feature.</p>
<h3>overriding supported / default PyPy versions</h3>
<p> If you want to override system&#8217;s list of supported PyPy versions or the default one (f.e. to build a package that includes symlinks for older version of PyPy or compile .py files only for given interpreter version), you can do that via <i>DEBPYPY_SUPPORTED</i> and/or <i>DEBPYPY_DEFAULT</i> env. variables.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd> show program&#8217;s version number and exit</p>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd> show help message and exit</p>
<dt><code>&#8211;no-guessing-deps</code></p>
<dd> disable guessing dependencies</p>
<dt><code>&#8211;no-dbg-cleaning</code></p>
<dd> do not remove any files from debug packages </p>
<p> &#8211;no-ext-rename do not add magic tags nor multiarch tuples to extension file names</p>
<dt><code>&#8211;no-shebang-rewrite</code></p>
<dd> do not rewrite shebangs</p>
<dt><code>&#8211;skip-private</code></p>
<dd> don&#8217;t check private directories</p>
<dt><code>-v</code>,<code> &#8211;verbose</code></p>
<dd> turn verbose mode on</p>
<dt><code>-i</code>,<code> &#8211;indep</code></p>
<dd> act on architecture independent packages</p>
<dt><code>-a</code>,<code> &#8211;arch</code></p>
<dd> act on architecture dependent packages</p>
<dt><code>-q</code>,<code> &#8211;quiet</code></p>
<dd> be quiet</p>
<dt><code>-p</code><i>&nbsp;PACKAGE</i>,<code>&nbsp;&#8211;package=</code><i>PACKAGE</i></p>
<dd> act on the package named PACKAGE</p>
<dt><code>-N</code><i>&nbsp;NO_PACKAGE</i>,<code>&nbsp;&#8211;no-package=</code><i>NO_PACKAGE</i></p>
<dd> do not act on the specified package</p>
<dt><code>-X</code><i>&nbsp;REGEXPR</i>,<code>&nbsp;&#8211;exclude=</code><i>REGEXPR</i></p>
<dd> exclude items that match given REGEXPR. You may use this option multiple times to build up a list of things to exclude.</p>
<dt><code>&#8211;compile-all</code></p>
<dd> compile all files from given private directory in postinst/rtupdate not just the ones provided by the package (i.e. do not pass the &#8211;package parameter to py3compile/py3clean)</p>
<dt><code>&#8211;accept-upstream-versions</code></p>
<dd> accept upstream versions while translating Python dependencies into Debian ones</p>
<dt><code>&#8211;depends=</code><i>DEPENDS</i></p>
<dd> translate given requirements into Debian dependencies and add them to ${pypy:Depends}. Use it for missing items in requires.txt</p>
<dt><code>&#8211;depends-sections=</code><i>SECTIONS</i></p>
<dd> translate requirements from given sections of requres.txt file into Debian dependencies and add them to ${pypy:Depends}.</p>
<dt><code>&#8211;recommends=</code><i>RECOMMENDS</i></p>
<dd> translate given requirements into Debian dependencies and add them to ${pypy:Recommends}</p>
<dt><code>&#8211;recommends-sections=</code><i>SECTIONS</i></p>
<dd> translate requirements from given sections of requres.txt file into Debian dependencies and add them to ${pypy:Recommends}.</p>
<dt><code>&#8211;suggests=</code><i>SUGGESTS</i></p>
<dd> translate given requirements into Debian dependencies and add them to ${pypy:Suggests}</p>
<dt><code>&#8211;suggests-sections=</code><i>SECTIONS</i></p>
<dd> translate requirements from given sections of requres.txt file into Debian dependencies and add them to ${pypy:Suggests}.</p>
<dt><code>&#8211;requires=</code><i>FILENAME</i></p>
<dd> translate requirements from given file(s) into Debian dependencies and add them to ${pypy:Depends}</p>
<dt><code>&#8211;shebang=</code><i>COMMAND</i></p>
<dd> use given command as shebang in scripts</p>
<dt><code>&#8211;ignore-shebangs</code></p>
<dd> do not translate shebangs into Debian dependencies</dl>
<h2>SEE ALSO</h2>
<dl>
<dt>&bull;</p>
<dd> /usr/share/doc/dh-python/README.PyDist</p>
<dt>&bull;</p>
<dd> <a href="/docs/linux/man/1-pybuild/">pybuild</a>(1)</p>
<dt>&bull;</p>
<dd> <i><a rel="nofollow" href="http://deb.li/dhpy">http://deb.li/dhpy</a></i> &#8211; most recent version of this document</dl>
<h2>AUTHOR</h2>
<p> Piotr Ożarowski, 2013 </p>
<h2>Index</h2>
