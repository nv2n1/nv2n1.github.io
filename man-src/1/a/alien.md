---
title: "alien(1)"
name: "alien"
section: "1"
letter: "a"
url: "/docs/linux/man/1-alien/"
description: "alien – Convert or install an alien binary package"
---

<h2 class="name">NAME</h2>
<p> alien &#8211; Convert or install an alien binary package </p>
<h2>SYNOPSIS</h2>
<pre><code>
alien[--to - deb][--to - rpm][--to - tgz][--to - slp][options] file[...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>alien</code> is a program that converts between Red Hat rpm, Debian deb, Stampede slp, Slackware tgz, and Solaris pkg file formats. If you want to use a package from another linux distribution than the one you have installed on your system, you can use <code>alien</code> to convert it to your preferred package format and install it. It also supports <font SIZE="-1">LSB</font> packages.</p>
<h2>WARNING</h2>
<p> <code>alien</code> should not be used to replace important system packages, like init, libc, or other things that are essential for the functioning of your system. Many of these packages are set up differently by the different distributions, and packages from the different distributions cannot be used interchangeably. In general, if you can&#8217;t remove a package without breaking your system, don&#8217;t try to replace it with an alien version.</p>
<h2>PACKAGE FORMAT NOTES</h2>
<dl>
<dt>rpm</p>
<dd> For converting to and from rpm format the Red Hat Package Manager must be installed.</p>
<dt>lsb</p>
<dd> Unlike the other package formats, <code>alien</code> can handle the depenendencies of lsb packages if the destination package format supports dependencies. Note that this means that the package generated from a lsb package will depend on a package named &#8220;lsb&#8221; &#8212; your distribution should provide a package by that name, if it is lsb compliant. The scripts in the lsb package will be converted by default as well. </p>
<p> To generate lsb packages, the Red Hat Package Manager must be installed, and <code>alien</code> will use by preference a program named lsb-rpm, if it exists. No guarantees are made that the generated lsb packages will be fully <font SIZE="-1">LSB</font> compliant, and it&#8217;s rather unlikely they will unless you build them in the lsbdev environment. </p>
<p> Note that unlike other package formats, converting an <font SIZE="-1">LSB</font> package to another format will not cause its minor version number to be changed.</p>
<dt>deb</p>
<dd> For converting to (but not from) deb format, the gcc, make, debhelper, dpkg-dev, and dpkg packages must be installed.</p>
<dt>tgz</p>
<dd> Note that when converting from the tgz format, <code>alien</code> will simply generate an output package that has the same files in it as are in the tgz file. This only works well if the tgz file has precompiled binaries in it in a standard linux directory tree. Do <font SIZE="-1">NOT</font> run <code>alien</code> on tar files with source code in them, unless you want this source code to be installed in your root directory when you install the package! </p>
<p> When using <code>alien</code> to convert a tgz package, all files in /etc in are assumed to be configuration files.</p>
<dt>pkg</p>
<dd> To manipulate packages in the Solaris pkg format (which is really the <font SIZE="-1">SV </font> datastream package format), you will need the Solaris pkginfo and pkgtrans tools.</dl>
<h2>OPTIONS</h2>
<p> <code>alien</code> will convert all the files you pass into it into all the output types you specify. If no output type is specified, it defaults to converting to deb format.</p>
<dl>
<dt>file [&#8230;]</p>
<dd> The list of package files to convert.</p>
<dt><code>-d</code>, <code>&#8211;to-deb</code></p>
<dd> Make debian packages. This is the default.</p>
<dt><code>-r</code>, <code>&#8211;to-rpm</code></p>
<dd> Make rpm packages.</p>
<dt><code>-t</code>, <code>&#8211;to-tgz</code></p>
<dd> Make tgz packages.</p>
<dt><code>&#8211;to-slp</code></p>
<dd> Make slp packages.</p>
<dt><code>-p</code>, <code>&#8211;to-pkg</code></p>
<dd> Make Solaris pkg packages.</p>
<dt><code>-i</code>, <code>&#8211;install</code></p>
<dd> Automatically install each generated package, and remove the package file after it has been installed.</p>
<dt><code>-g</code>, <code>&#8211;generate</code></p>
<dd> Generate a temporary directory suitable for building a package from, but do not actually create the package. This is useful if you want to move files around in the package before building it. The package can be built from this temporary directory by running &#8220;debian/rules binary&#8221;, if you were creating a Debian package, or by running &#8220;rpmbuild -bb &lt;packagename&gt;.spec&#8221; if you were creating a Red Hat package.</p>
<dt><code>-s</code>, <code>&#8211;single</code></p>
<dd> Like <code>-g</code>, but do not generate the packagename.orig directory. This is only useful when you are very low on disk space and are generating a debian package.</p>
<dt><code>-c</code>, <code>&#8211;scripts</code></p>
<dd> Try to convert the scripts that are meant to be run when the package is installed and removed. Use this with caution, because these scripts might be designed to work on a system unlike your own, and could cause problems. It is recommended that you examine the scripts by hand and check to see what they do before using this option. </p>
<p> This is enabled by default when converting from lsb packages.</p>
<dt><code>&#8211;patch=</code><i>patch</i></p>
<dd> Specify the patch to be used instead of automatically looking the patch up in <code>/var/lib/alien</code>. This has no effect unless a debian package is being built.</p>
<dt><code>&#8211;anypatch</code></p>
<dd> Be less strict about which patch file is used, perhaps attempting to use a patch file for an older version of the package. This is not guaranteed to always work; older patches may not necessarily work with newer packages.</p>
<dt><code>&#8211;nopatch</code></p>
<dd> Do not use any patch files.</p>
<dt><code>&#8211;description=</code><i>desc</i></p>
<dd> Specifiy a description for the package. This only has an effect when converting from the tgz package format, which lacks descriptions.</p>
<dt><code>&#8211;version=</code><i>version</i></p>
<dd> Specifiy a version for the package. This only has an effect when converting from the tgz package format, which may lack version information. </p>
<p> Note that without an argument, this displays the version of <code>alien</code> instead.</p>
<dt><code>-T</code>, <code>&#8211;test</code></p>
<dd> Test the generated packages. Currently this is only supported for debian packages, which, if lintian is installed, will be tested with lintian and lintian&#8217;s output displayed.</p>
<dt><code>-k</code>, <code>&#8211;keep-version</code></p>
<dd> By default, <code>alien</code> adds one to the minor version number of each package it converts. If this option is given, <code>alien</code> will not do this.</p>
<dt><code>&#8211;bump=</code><i>number</i></p>
<dd> Instead of incrementing the version number of the converted package by 1, increment it by the given number.</p>
<dt><code>&#8211;fixperms</code></p>
<dd> Sanitize all file owners and permissions when building a deb. This may be useful if the original package is a mess. On the other hand, it may break some things to mess with their permissions and owners to the degree this does, so it defaults to off. This can only be used when converting to debian packages.</p>
<dt><code>&#8211;target=</code><i>architecture</i></p>
<dd> Force the architecture of the generated package to the given string.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Be verbose: Display each command <code>alien</code> runs in the process of converting a package.</p>
<dt><code>&#8211;veryverbose</code></p>
<dd> Be verbose as with &#8211;verbose, but also display the output of each command run. Some commands may generate a lot of output.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Display a short usage summary.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Display the version of <code>alien</code>.</dl>
<h2>EXAMPLES</h2>
<p> Here are some examples of the use of <code>alien</code>:</p>
<dl>
<dt>alien &#8211;to-deb package.rpm</p>
<dd> Convert the package.rpm into a package.deb</p>
<dt>alien &#8211;to-rpm package.deb</p>
<dd> Convert the package.deb into a package.rpm</p>
<dt>alien -i package.rpm</p>
<dd> Convert the package.rpm into a package.deb (converting to a .deb package is default, so you need not specify &#8211;to-deb), and install the generated package.</p>
<dt>alien &#8211;to-deb &#8211;to-rpm &#8211;to-tgz &#8211;to-slp foo.deb bar.rpm baz.tgz</p>
<dd> Creates 9 new packages. When it is done, foo bar and baz are available in all 4 package formats.</dl>
<h2>ENVIRONMENT</h2>
<p> <code>alien</code> recognizes the following environment variables:</p>
<dl>
<dt><font SIZE="-1">RPMBUILDOPT</font></p>
<dd> Options to pass to rpm when it is building a package.</p>
<dt><font SIZE="-1">RPMINSTALLOPT</font></p>
<dd> Options to pass to rpm when it is installing a package.</p>
<dt><font SIZE="-1">EMAIL</font></p>
<dd> If set, <code>alien</code> assumes this is your email address. Email addresses are included in generated debian packages.</dl>
<h2>AUTHOR</h2>
<p> <code>alien</code> was written by Christoph Lameter, <code>&lt;clameter [at] debian.org</code>&gt;. </p>
<p> deb to rpm conversion code was taken from the martian program by Randolph Chung, <code>&lt;tausq [at] debian.org</code>&gt;. </p>
<p> The Solaris pkg code was written by Mark A. Hershberger <code>&lt;mah [at] everybody.org</code>&gt;. </p>
<p> alien has been extensively rewritten (3 times) and is now maintained by Joey Hess, <code>&lt;joeyh [at] debian.org</code>&gt;.</p>
<h2>COPYRIGHT</h2>
<p> alien may be copied and modified under the terms of the <font SIZE="-1">GNU</font> General Public License. </p>
<h2>Index</h2>
