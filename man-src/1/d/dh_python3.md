---
title: "dh_python3(1)"
name: "dh_python3"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_python3/"
description: "dh_python3 – calculates Python dependencies, adds maintainer scripts to byte compile files, etc."
---

<h2 class="name">NAME</h2>
<p> dh_python3 &#8211; calculates Python dependencies, adds maintainer scripts to byte compile files, etc. </p>
<h2>SYNOPSIS</h2>
<p> dh_python3 -p PACKAGE [-V [X.Y][-][A.B]] DIR [-X REGEXPR]</p>
<h2>DESCRIPTION</h2>
<h3>QUICK GUIDE FOR MAINTAINERS</h3>
<dl>
<dt>&bull;</p>
<dd> if necessary, describe supported Python 3 versions via X-Python3-Version field in debian/control,</p>
<dt>&bull;</p>
<dd> build depend on dh-python</p>
<dt>&bull;</p>
<dd> build-depend on python3 or python3-all or python3-all-dev,</p>
<dt>&bull;</p>
<dd> build module/application using its standard build system, remember to build extensions for all supported Python 3 versions (loop over <code>py3versions -vr</code>),</p>
<dt>&bull;</p>
<dd> install files to the <i>standard</i> locations, add <i>&#8211;install-layout=deb</i> to setup.py&#8217;s install command if your package is using distutils,</p>
<dt>&bull;</p>
<dd> add <i>python3</i> to dh&#8217;s &#8211;with option, or:</p>
<dt>&bull;</p>
<dd> <i>include /usr/share/cdbs/1/class/python-distutils.mk</i> in debian/rules and depend on <i>cdbs (&gt;= 0.4.90)</i>, or:</p>
<dt>&bull;</p>
<dd> call <code>dh_python3</code> in the <i>binary-*</i> target,</p>
<dt>&bull;</p>
<dd> add <i>${python3:Depends}</i> to Depends</dl>
<h3>NOTES</h3>
<h3>dependencies</h3>
<p> dh_python3 tries to translate Python dependencies from the <i>requires.txt</i> file to Debian dependencies. In many cases, this works without any additional configuration because dh_python3 comes with a build-in mapping of Python module names to Debian packages that is periodically regenerated from the Debian archive. By default, the version information in the Python dependencies is discarded. If you want dh_python3 to generate more strict dependencies (e.g. to avoid ABI problems), or if the automatic mapping does not work correctly for your package, you have to provide dh_python3 with additional rules for the translation of Python module to Debian package dependencies. </p>
<p> For a package <i>python3-foo</i> that depends on a package <i>python3-bar</i>, there are two files that may provide such rules:</p>
<dl>
<dt>1.</p>
<dd> If the <i>python3-foo</i> source package ships with a <i>debian/py3dist-overrides</i> file, this file is used by dh_python3 during the build of <i>python3-foo</i>.</p>
<dt>2.</p>
<dd> If the <i>python3-bar</i> source package ships with a <i>debian/python3-bar.pydist</i> file (and uses dh_python3), this file will be included in the binary package as <i>/usr/share/dh-python/dist/cpython3/python3-bar</i>. During the build of <i>python3-foo</i>, dh_python3 will then find and use the file. </p>
<p> Both files have the same format described in <i>/usr/share/doc/dh-python/README.PyDist</i>. If all you want is to generate versioned dependencies (and assuming that the <i>python3-bar</i> package provides the <i>pybar</i> Python module), in most cases it will be sufficient to put the line <code>pybar python3-bar; PEP386</code> into either of the above files.</dl>
<h3>private dirs</h3>
<p> <i>/usr/share/foo</i>, <i>/usr/share/games/foo</i>, <i>/usr/lib/foo</i> and <i>/usr/lib/games/foo</i> private directories are scanned for Python files by default (where <i>foo</i> is binary package name). If your package is shipping Python files in some other directory, add another dh_python3 call in debian/rules with directory name as an argument &#8211; you can use different set of options in this call. If you need to change options (f.e. a list of supported Python 3 versions) for a private directory that is checked by default, invoke dh_python3 with &#8211;skip-private option and add another call with a path to this directory and new options.</p>
<h3>debug packages</h3>
<p> In binary packages which name ends with <i>-dbg</i>, all files in <i>/usr/lib/python3/dist-packages/</i> directory that have extensions different than <i>so</i> or <i>h</i> are removed by default. Use &#8211;no-dbg-cleaning option to disable this feature.</p>
<h3>pyinstall files</h3>
<p> Files listed in debian/pkg.pyinstall file will be installed as public modules (i.e. into &#8230;/dist-packages/ directory) for all requested Python versions. </p>
<p> Syntax: <code>path/to/file [VERSION_RANGE] [NAMESPACE]</code> </p>
<p> debian directory is automatically removed from the path, so you can place your files in debian/ directory and install them from this location (if you want to install them in &quot;debian&quot; namespace, set NAMESPACE to debian). If NAMESPACE is set, all listed files will be installed in &#8230;/dist-packages/NAMESPACE/ directory.</p>
<dl>
<dt><code>Examples:</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>foo.py</code> installs &#8230;/dist-packages/foo.py for all supported Python versions</p>
<dt>&bull;</p>
<dd> <code>foo/bar.py 3.3-</code> installs &#8230;/dist-packages/foo/bar.py for versions &gt;= 3.3</p>
<dt>&bull;</p>
<dd> <code>foo/bar.py spam</code> installs &#8230;/dist-packages/spam/bar.py</p>
<dt>&bull;</p>
<dd> <code>debian/*.py spam.egg 3.2</code> installs &#8230;/python3.2/dist-packages/spam/egg/*.py files</dl>
<h3>pyremove files</h3>
<p> If you want to remove some public modules (i.e. files in &#8230;/dist-packages/ directory) installed by build system (from all supported Python versions or only from a subset of these versions), add them to debian/pkg.pyremove file.</p>
<dl>
<dt><code>Examples:</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>*.pth</code> removes .pth files from &#8230;/dist-packages/</p>
<dt>&bull;</p>
<dd> <code>bar/baz.py 3.2</code> removes &#8230;/python3.2/dist-packages/bar/baz.py</dl>
<h3>overriding supported / default Python versions</h3>
<p> If you want to override system&#8217;s list of supported Python versions or the default one (f.e. to build a package that includes symlinks for older version of Python or compile .py files only for given interpreter version), you can do that via <i>DEBPYTHON3_SUPPORTED</i> and/or <i>DEBPYTHON3_DEFAULT</i> env. variables. </p>
<p> Example: <code>3.2,3.3</code> limits the list of supported Python versions to Python 3.2 and Python 3.3.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd> show program&#8217;s version number and exit</p>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd> show help message and exit</p>
<dt><code>&#8211;no-guessing-deps</code></p>
<dd> disable guessing dependencies</p>
<dt><code>&#8211;no-dbg-cleaning</code></p>
<dd> do not remove any files from debug packages</p>
<dt><code>&#8211;no-ext-rename</code></p>
<dd> do not add magic tags nor multiarch tuples to extension file names</p>
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
<dt><code>-V</code><i>&nbsp;VRANGE</i></p>
<dd> specify list of supported Python 3 versions. See <a href="/docs/linux/man/1-py3compile/">py3compile</a>(1) for examples</p>
<dt><code>-X</code><i>&nbsp;REGEXPR</i>,<code>&nbsp;&#8211;exclude=</code><i>REGEXPR</i></p>
<dd> exclude items that match given REGEXPR. You may use this option multiple times to build up a list of things to exclude.</p>
<dt><code>&#8211;compile-all</code></p>
<dd> compile all files from given private directory in postinst/rtupdate not just the ones provided by the package (i.e. do not pass the &#8211;package parameter to py3compile/py3clean)</p>
<dt><code>&#8211;accept-upstream-versions</code></p>
<dd> accept upstream versions while translating Python dependencies into Debian ones</p>
<dt><code>&#8211;depends=</code><i>DEPENDS</i></p>
<dd> translate given requirements into Debian dependencies and add them to ${python3:Depends}. Use it for missing items in requires.txt</p>
<dt><code>&#8211;depends-section=</code><i>SECTION</i></p>
<dd> translate requirements from given sections of requres.txt file into Debian dependencies and add them to ${python3:Depends}.</p>
<dt><code>&#8211;recommends=</code><i>RECOMMENDS</i></p>
<dd> translate given requirements into Debian dependencies and add them to ${python3:Recommends}</p>
<dt><code>&#8211;recommends-section=</code><i>SECTION</i></p>
<dd> translate requirements from given sections of requres.txt file into Debian dependencies and add them to ${python3:Recommends}.</p>
<dt><code>&#8211;suggests=</code><i>SUGGESTS</i></p>
<dd> translate given requirements into Debian dependencies and add them to ${python3:Suggests}</p>
<dt><code>&#8211;suggests-section=</code><i>SECTION</i></p>
<dd> translate requirements from given sections of requres.txt file into Debian dependencies and add them to ${python3:Suggests}.</p>
<dt><code>&#8211;requires=</code><i>FILENAME</i></p>
<dd> translate requirements from given file(s) into Debian dependencies and add them to ${python3:Depends}</p>
<dt><code>&#8211;shebang=</code><i>COMMAND</i></p>
<dd> use given command as shebang in scripts</p>
<dt><code>&#8211;ignore-shebangs</code></p>
<dd> do not translate shebangs into Debian dependencies</dl>
<h2>SEE ALSO</h2>
<dl>
<dt>&bull;</p>
<dd> /usr/share/doc/python/python-policy.txt.gz</p>
<dt>&bull;</p>
<dd> /usr/share/doc/dh-python/README.PyDist</p>
<dt>&bull;</p>
<dd> <a href="/docs/linux/man/1-pybuild/">pybuild</a>(1)</p>
<dt>&bull;</p>
<dd> <a href="/docs/linux/man/1-py3compile/">py3compile</a>(1), <a href="/docs/linux/man/1-py3clean/">py3clean</a>(1)</p>
<dt>&bull;</p>
<dd> <a href="/docs/linux/man/1-dh_python2/">dh_python2</a>(1), <a href="/docs/linux/man/1-pycompile/">pycompile</a>(1), <a href="/docs/linux/man/1-pyclean/">pyclean</a>(1)</p>
<dt>&bull;</p>
<dd> <i><a rel="nofollow" href="http://deb.li/dhp3">http://deb.li/dhp3</a></i> &#8211; most recent version of this document</dl>
<h2>AUTHOR</h2>
<p> Piotr Ożarowski, 2012-2013 </p>
<h2>Index</h2>
