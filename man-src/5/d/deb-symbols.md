---
title: "deb-symbols(5)"
name: "deb-symbols"
section: "5"
letter: "d"
url: "/docs/linux/man/5-deb-symbols/"
description: "deb-symbols – Debian’s extended shared library information file"
---

<p>deb-symbols &#8211; Debian&#8217;s extended shared library information file</p>
<h2>Synopsis</h2>
<p><code>DEBIAN/symbols</code></p>
<h2>Description</h2>
<p>The symbol files are shipped in Debian binary packages, and its format is a subset of the template symbol files used by <code><a href="/docs/linux/man/1-dpkg-gensymbols/">dpkg-gensymbols</a></code>(1) in Debian source packages. </p>
<p> The format for an extended shared library dependency information entry in these files is: </p>
<p>&nbsp;<i>library-soname main-dependency-template</i><br />
&nbsp;[|&nbsp;<i>alternative-dependency-template</i>]<br />
&nbsp;[&#8230;]<br />
&nbsp;[*&nbsp;<i>field-name</i>:&nbsp;<i>field-value</i>]<br />
&nbsp;[&#8230;]<br />
&nbsp;<wbr>&nbsp;<i>symbol</i>&nbsp;<i>minimal-version</i>&nbsp;[<i>id-of-dependency-template</i>] </p>
<p> The <i>library-soname</i> is exactly the value of the <font SIZE="-1">SONAME</font> field as exported by <code><a href="/docs/linux/man/1-objdump/">objdump</a></code>(1). A <i>dependency-template</i> is a dependency where <i>#MINVER#</i> is dynamically replaced either by a version check like &#8220;(&gt;= <i>minimal-version</i>)&#8221; or by nothing (if an unversioned dependency is deemed sufficient). </p>
<p> Each exported <i>symbol</i> (listed as <i>name</i>@<i>version</i>, with <i>version</i> being &#8220;Base&#8221; if the library is not versioned) is associated to a <i>minimal-version</i> of its dependency template (the main dependency template is always used and will end up being combined with the dependency template referenced by <i>id-of-dependency-template</i> if present). The first alternative dependency template is numbered 1, the second one 2, etc. Each column is separated by exactly a single whitespace. </p>
<p> Each entry for a library can also have some fields of meta-information. Those fields are stored on lines starting with an asterisk. Currently, the only valid fields are:</p>
<dl>
<dt><code>Build-Depends-Package</code></p>
<dd>It indicates the name of the &#8220;-dev&#8221; package associated to the library and is used by <code>dpkg-shlibdeps</code> to make sure that the dependency generated is at least as strict as the corresponding build dependency (since dpkg 1.14.13).</p>
<dt><code>Build-Depends-Packages</code></p>
<dd>The same as <code>Build-Depends-Package</code> but accepts a comma-separated list of package names (since dpkg 1.20.0). This field will override any <code>Build-Depends-Package</code> field present, and is mostly useful with &#8220;-dev&#8221; packages and metapackages depending on these, say for a transition period.</p>
<dt><code>Allow-Internal-Symbol-Groups</code></p>
<dd>It indicates what internal symbol groups should be ignored, as a whitespace separated list, so that the symbols contained in those groups get included in the output file (since dpkg 1.20.1). This should only be necessary for toolchain packages providing those internal symbols. The available groups are system dependent, for <font SIZE="-1">ELF</font> and GNU-based systems these are <code>aeabi</code> and <code>gomp</code>.</p>
<dt><code>Ignore-Blacklist-Groups</code></p>
<dd>A deprecated alias for <code>Allow-Internal-Symbol-Groups</code> (since dpkg 1.20.1, supported since dpkg 1.17.6).</dl>
<h2>Examples</h2>
<h3>Simple symbols file</h3>
<pre> lib<a href="ftp://ftp.so.3">ftp.so.3</a> libftp3 #MINVER#
 DefaultNetbuf [at] Base 3.1-1-6
 FtpAccess [at] Base 3.1-1-6
 [...]</pre>
<h3>Advanced symbols file</h3>
<pre> libGL.so.1 libgl1
 | libgl1-mesa-glx #MINVER#
 * Build-Depends-Package: libgl1-mesa-dev
 publicGlSymbol [at] Base 6.3-1
 [...]
 implementationSpecificSymbol [at] Base 6.5.2-7 1
 [...]</pre>
<h2>See Also</h2>
<p>&lt;<a rel="nofollow" href="https://wiki.debian.org/Projects/ImprovedDpkgShlibdeps">https://wiki.debian.org/Projects/ImprovedDpkgShlibdeps</a>&gt;, <code><a href="/docs/linux/man/1-dpkg-shlibdeps/">dpkg-shlibdeps</a></code>(1), <code><a href="/docs/linux/man/1-dpkg-gensymbols/">dpkg-gensymbols</a></code>(1). </p>
