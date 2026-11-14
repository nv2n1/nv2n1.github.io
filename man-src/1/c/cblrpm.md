---
title: "cblrpm(1)"
name: "cblrpm"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cblrpm/"
description: "cblrpm – a RPM packaging tool for Haskell Cabal packages"
---

<h2>NAME</h2>
<p> cblrpm &#8211; a RPM packaging tool for Haskell Cabal packages</p>
<h2>SYNOPSIS</h2>
<p> cblrpm [options] spec [path-or-pkg] cblrpm [options] local [path-or-pkg] cblrpm [options] srpm [path-or-pkg] cblrpm [options] prep [path-or-pkg] cblrpm [options] builddep [path-or-pkg] cblrpm [options] install [path-or-pkg] cblrpm [options] depends [path-or-pkg] cblrpm [options] requires [path-or-pkg] cblrpm [options] missingdeps [path-or-pkg] cblrpm [options] diff [path-or-pkg] cblrpm [options] update [path-or-pkg]</p>
<h2>DESCRIPTION</h2>
<p> cblrpm generates RPM packages and .spec files from Haskell Cabal package. </p>
<p> If no path-or-pkg is specified, cblrpm looks for a .spec or Otherwise, it will look for path-or-pkg. If the argument is a directory then it will look there for a .spec or If the argument is a path to a .cabal file then it will use it. Otherwise if there is no &#8216;/&#8217; in the argument and it does not exist then cblrpm will try to unpack the package and use its .cabal file. cblrpm uses a temporary directory for unpackaging tarballs or packages. cblrpm then parses the .cabal file and uses it to generate a .spec file that can be built. </p>
<p> If a .spec already exists, cblrpm outputs to .spec.cblrpm instead.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Show the help text.</p>
<dl>
<dt>
<dd></dl>
<dt><code>-b, &#8211;binary</code></p>
<dd> Force the base package name to be the Hackage package name.</p>
<dl>
<dt>
<dd></dl>
</dl>
<p> -f FLAGS, &#8211;flags=FLAGS : Override one or more Cabal build configuration flags. </p>
<p> &#8211;release=RELEASE : Override the release number in the .spec file. </p>
<p> -v N, &#8211;verbose=N : Set verbosity to N. </p>
<p> &#8211;version=VERSION : Override the version number in the .spec file.</p>
<h2>EXAMPLES</h2>
<p> Below CMD can be one of: spec, srpm, prep, local, install, diff, builddep, depends, requires, missingdeps, update </p>
<p> Do CMD for the package in current directory:</p>
<dl>
<dt>
<dd>
<pre>
cblrpm CMD
</pre>
</dl>
<p> Do CMD for package (directory or package name):</p>
<dl>
<dt>
<dd>
<pre>
cblrpm CMD&nbsp;<wbr>[package]
</pre>
</dl>
<p> Do CMD for package-version (directory or package name):</p>
<dl>
<dt>
<dd>
<pre>
cblrpm CMD&nbsp;<wbr>[package-version]
</pre>
</dl>
<p> Do CMD on a .cabal file:</p>
<dl>
<dt>
<dd>
<pre>
cblrpm CMD path/to/some.cabal
</pre>
</dl>
<h2>HISTORY</h2>
<p> Cabal-rpm was originally written by Bryan O&#8217;Sullivan in 2007-2008 and resurrected by Jens Petersen in 2012 to replace cabal2spec.</p>
<h2>SEE ALSO</h2>
<p> &lt;<a rel="nofollow" href="http://github.com/juhp/cabal-rpm/">http://github.com/juhp/cabal-rpm/</a>&gt;</p>
<h2>AUTHORS</h2>
<p> This manpage was written by Jens Petersen. </p>
<h2>Index</h2>
