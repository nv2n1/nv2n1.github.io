---
title: "dh_python2(1)"
name: "dh_python2"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_python2/"
description: "dh_python2 – calculates Python dependencies, adds maintainer scripts to byte compile files, etc."
---

<h2 class="name">NAME</h2>
<p> dh_python2 &#8211; calculates Python dependencies, adds maintainer scripts to byte compile files, etc. </p>
<h2>SYNOPSIS</h2>
<p> dh_python2 -p PACKAGE [-V [X.Y][-][A.B]] DIR_OR_FILE [-X REGEXPR]</p>
<h2>DESCRIPTION</h2>
<h3>QUICK GUIDE FOR MAINTAINERS</h3>
<dl>
<dt>&bull;</p>
<dd> if necessary, describe supported Python versions via X-Python-Version field in debian/control,</p>
<dt>&bull;</p>
<dd> build-depend on python or python-all or python-all-dev (&gt;= 2.6.6-3~),</p>
<dt>&bull;</p>
<dd> build module/application using its standard build system, remember to build extensions for all supported Python versions (loop over <code>pyversions -vr</code>),</p>
<dt>&bull;</p>
<dd> install files to the <i>standard</i> locations, add <i>&#8211;install-layout=deb</i> to setup.py&#8217;s install command if your package is using distutils,</p>
<dt>&bull;</p>
<dd> add <i>python2</i> to dh&#8217;s &#8211;with option, or:</p>
<dt>&bull;</p>
<dd> <i>include /usr/share/cdbs/1/class/python-distutils.mk</i> in debian/rules and depend on <i>cdbs (&gt;= 0.4.90)</i>, or:</p>
<dt>&bull;</p>
<dd> call <code>dh_python2</code> in the <i>binary-*</i> target,</p>
<dt>&bull;</p>
<dd> add <i>${python:Depends}</i> to Depends</dl>
<h3>NOTES</h3>
<p> In order to support more than one Python version in the same binary package, dh_python2 (unlike dh_pycentral and dh_pysupport) creates symlinks to all supported Python versions at build time. It means binNMU (or sourceful upload in case of architecture independent packages) is required once a list of supported Python version is changed. It&#8217;s faster and more robust than its competitors, though.</p>
<h3>dependencies</h3>
<p> dh_python2 tries to translate Python dependencies from requires.txt file to Debian dependencies. Use debian/pydist-overrides or &#8211;no-guessing-deps option to override it if the guess is incorrect. If you want dh_python2 to generate more strict dependencies (f.e. to avoid ABI problems) create debian/python-foo.pydist file. See /usr/share/doc/python-doc/README.PyDist (provided by python-doc package) for more information. If the pydist file contains PEP386 flag or set of (uscan like) rules, dh_python2 will make the dependency versioned (version requirements are ignored by default).</p>
<h3>namespace feature</h3>
<p> dh_python2 parses Egg&#8217;s namespace_packages.txt files (in addition to &#8211;namespace command line argument(s)) and drops empty __init__.py files from binary package. pycompile will regenerate them at install time and pyclean will remove them at uninstall time (if they&#8217;re no longer used in installed packages). It&#8217;s still a good idea to provide __init__.py file in one of binary packages (even if all other packages use this feature).</p>
<h3>private dirs</h3>
<p> <i>/usr/share/foo</i>, <i>/usr/share/games/foo</i>, <i>/usr/lib/foo</i> and <i>/usr/lib/games/foo</i> private directories are scanned for Python files by default (where <i>foo</i> is binary package name). If your package is shipping Python files in some other directory, add another dh_python2 call in debian/rules with directory name as an argument &#8211; you can use different set of options in this call. If you need to change options (f.e. a list of supported Python versions) for a private directory that is checked by default, invoke dh_python2 with &#8211;skip-private option and add another call with a path to this directory and new options.</p>
<h3>debug packages</h3>
<p> In binary packages which name ends with <i>-dbg</i>, all files in <i>/usr/lib/python2.X/{site,dist}-packages/</i> directory that have extensions different than <i>so</i> or <i>h</i> are removed by default. Use &#8211;no-dbg-cleaning option to disable this feature.</p>
<h3>pyinstall files</h3>
<p> Files listed in debian/pkg.pyinstall file will be installed as public modules for all requested Python versions (dh_install doesn&#8217;t know about python&#8217;s site- vs. dist-packages issue). </p>
<p> Syntax: <code>path/to/file [VERSION_RANGE] [NAMESPACE]</code> </p>
<p> debian directory is automatically removed from the path, so you can place your files in debian/ directory and install them from this location (if you want to install them in &quot;debian&quot; namespace, set NAMESPACE to debian). If NAMESPACE is set, all listed files will be installed in &#8230;/dist-packages/NAMESPACE/ directory.</p>
<dl>
<dt><code>Examples:</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>foo.py</code> installs &#8230;/dist-packages/foo.py for all supported Python versions</p>
<dt>&bull;</p>
<dd> <code>foo/bar.py 2.6-</code> installs &#8230;/dist-packages/foo/bar.py for versions &gt;= 2.6</p>
<dt>&bull;</p>
<dd> <code>foo/bar.py spam</code> installs &#8230;/dist-packages/spam/bar.py</p>
<dt>&bull;</p>
<dd> <code>debian/*.py spam.egg 2.5</code> installs &#8230;/python2.5/site-packages/spam/egg/*.py files</dl>
<h3>pyremove files</h3>
<p> If you want to remove some files installed by build system (from all supported Python versions or only from a subset of these versions), add them to debian/pkg.pyremove file.</p>
<dl>
<dt><code>Examples:</code></p>
<dd>
<dt>&bull;</p>
<dd> <code>*.pth</code> removes .pth files from &#8230;/dist-packages/</p>
<dt>&bull;</p>
<dd> <code>bar/baz.py 2.5</code> removes &#8230;/python2.5/site-packages/bar/baz.py</dl>
<h3>overriding supported / default Python versions</h3>
<p> If you want to override system&#8217;s list of supported Python versions or the default one (f.e. to build a package that includes symlinks for older version of Python or compile .py files only for given interpreter version), you can do that via <i>DEBPYTHON_SUPPORTED</i> and/or <i>DEBPYTHON_DEFAULT</i> env. variables. </p>
<p> Example: <code>2.5,2.7</code> limits the list of supported Python versions to Python 2.5 and Python 2.7.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd> show program&#8217;s version number and exit</p>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd> show help message and exit</p>
<dt><code>&#8211;no-guessing-versions</code></p>
<dd> disable guessing other supported Python versions</p>
<dt><code>&#8211;no-guessing-deps</code></p>
<dd> disable guessing dependencies</p>
<dt><code>&#8211;no-dbg-cleaning</code></p>
<dd> do not remove any files from debug packages</p>
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
<dd> specify list of supported Python versions. See <a href="/docs/linux/man/1-pycompile/">pycompile</a>(1) for examples</p>
<dt><code>-X</code><i>&nbsp;REGEXPR</i>,<code>&nbsp;&#8211;exclude=</code><i>REGEXPR</i></p>
<dd> exclude items that match given REGEXPR. You may use this option multiple times to build up a list of things to exclude.</p>
<dt><code>&#8211;compile-all</code></p>
<dd> compile all files from given private directory in postinst/rtupdate not just the ones provided by the package (i.e. do not pass the &#8211;package parameter to pycompile/pyclean)</p>
<dt><code>&#8211;depends=</code><i>DEPENDS</i></p>
<dd> translate given requirements into Debian dependencies and add them to ${python:Depends}. Use it for missing items in requires.txt</p>
<dt><code>&#8211;recommends=</code><i>RECOMMENDS</i></p>
<dd> translate given requirements into Debian dependencies and add them to ${python:Recommends}</p>
<dt><code>&#8211;suggests=</code><i>SUGGESTS</i></p>
<dd> translate given requirements into Debian dependencies and add them to ${python:Suggests}</p>
<dt><code>&#8211;namespace</code></p>
<dd> use this option (multiple time if necessary) if namespace_packages.txt is not complete</p>
<dt><code>&#8211;ignore-namespace</code></p>
<dd> ignore Egg&#8217;s namespace declaration and &#8211;namespace option. This option will disable removing (and recreating at install time) empty __init__.py files. Removing namespace_packages.txt from egg-info directory has the same effect.</p>
<dt><code>&#8211;clean-pycentral</code></p>
<dd> generate maintainer script that will remove byte code generated by python-central helper</p>
<dt><code>&#8211;shebang=</code><i>COMMAND</i></p>
<dd> use given command as shebang in scripts</p>
<dt><code>&#8211;ignore-shebangs</code></p>
<dd> do not translate shebangs into Debian dependencies</dl>
<h2>SEE ALSO</h2>
<dl>
<dt>&bull;</p>
<dd> /usr/share/doc/python/python-policy.txt.gz</p>
<dt>&bull;</p>
<dd> /usr/share/doc/python-doc/README.PyDist (python-doc package)</p>
<dt>&bull;</p>
<dd> <a href="/docs/linux/man/1-pycompile/">pycompile</a>(1), <a href="/docs/linux/man/1-pyclean/">pyclean</a>(1)</p>
<dt>&bull;</p>
<dd> <a href="/docs/linux/man/1-dh_python3/">dh_python3</a>(1), <a href="/docs/linux/man/1-py3compile/">py3compile</a>(1), <a href="/docs/linux/man/1-py3clean/">py3clean</a>(1)</p>
<dt>&bull;</p>
<dd> Wiki page about converting package to dh_python2: <i><a rel="nofollow" href="http://wiki.debian.org/Python/TransitionToDHPython2">http://wiki.debian.org/Python/TransitionToDHPython2</a></i></dl>
<h2>AUTHOR</h2>
<p> Piotr Ożarowski, 2012-2013 </p>
<h2>Index</h2>
