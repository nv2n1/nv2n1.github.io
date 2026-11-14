---
title: "site-lib(5)"
name: "site-lib"
section: "5"
letter: "s"
url: "/docs/linux/man/5-site-lib/"
description: "site-lib – [Location of package directories]"
---

<p>site-lib &#8211; [Location of package directories]</p>
<h2>Standard Layout</h2>
<pre>...somewhere in the filesystem hierarchy...
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>\&nbsp;<wbr>
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>site-lib
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>+-&nbsp;<wbr>(optional)&nbsp;<wbr>stublibs
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>+-&nbsp;<wbr>(optional)&nbsp;<wbr>postinstall
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>+-&nbsp;<wbr>(optional)&nbsp;<wbr>postremove
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>+-&nbsp;<wbr><i>package1</i><code>
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>|
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>+- META
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>+-&nbsp;<wbr></code><i>archive files</i><code>
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>+-&nbsp;<wbr></code><i>interface definitions</i><code>
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>+-&nbsp;<wbr></code><i>package2</i><code>
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>+
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>:
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>:
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>\
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code><i>packageN</i></pre>
<h2>Description</h2>
<p>Every installation of &quot;findlib&quot; has a default location for package directories, which is normally a directory called &quot;site-lib&quot;. The location can be set by the configuration variables path (used to look up packages), and destdir (used to install new packages); see findlib.conf.</p>
<p> The name of a package is the name of the package directory. For example, if destdir=/usr/local/lib/ocaml/site-lib, the package p will be installed in the subdirectory /usr/local/lib/ocaml/site-lib/p. This subdirectory must contain the META file and all other files belonging to the package. Package names must not contain the &#8216;.&#8217; character.</p>
<p> The variable destdir specifies the directory for new packages. You can only have one such directory at a time; but of course you can change this directory in findlib.conf. The command ocamlfind install puts new packages into this directory; it is recommended to use this command for installation because it ensures that the directory layout is right.</p>
<p> For searching packages, findlib uses (only) the variable path which may name several locations to look at.</p>
<p> For systems with DLL support another directory may exist: stublibs. If present, findlib will install DLLs into this directory that is shared by all packages at the same site-lib location. Findlib remembers which DLL belongs to which package by special files with the suffix &quot;.owner&quot;; e.g. for the DLL &quot;dllpcre.so&quot; there is another file &quot;dllpcre.so.owner&quot; containing the string &quot;pcre&quot;, so findlib knows that the package &quot;pcre&quot; owns this DLL. It is not possible that a DLL is owned by several packages.</p>
<p> If the stublibs directory does not exist, DLLs are installed regularly in the package directories like any other file.</p>
<p> For special needs, a postinstall and/or a postremove script may be installed in the site-lib directory. These scripts are invoked after installation or removal of a package, respectively.</p>
<h2>Alternate Layout</h2>
<pre>...somewhere in the filesystem hierarchy...
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>\&nbsp;<wbr>
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>site-lib
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>+-&nbsp;<wbr>(optional)&nbsp;<wbr>stublibs
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>+-&nbsp;<wbr>(optional)&nbsp;<wbr>postinstall
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>+-&nbsp;<wbr>(optional)&nbsp;<wbr>postremove
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>+-&nbsp;<wbr><i>package1</i><code>
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>|
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>+-&nbsp;<wbr></code><i>archive files</i><code>
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>+-&nbsp;<wbr></code><i>interface definitions</i><code>
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>+-&nbsp;<wbr></code><i>package2</i><code>
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>+
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>:
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>:
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>\
<br>
&nbsp;<wbr>&nbsp;<wbr>:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code><i>packageN</i><code>
<br>
&nbsp;<wbr>&nbsp;<wbr>|
<br>
&nbsp;<wbr>&nbsp;<wbr>\
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>metaregistry
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>+- META.package1
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>+- META.package2
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>+
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>:
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>\
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>META.packageN</code></pre>
<p>This is an alternate directory layout collecting all META files in one directory. You can configure this layout by setting path to the absolute location of metaregistry. Findlib recognizes that there are META files in this directory and uses them; it is not necessary to include site-lib into the path.</p>
<p> In order to work, the META files must contain a directory directive pointing to the corresponding package directory that resides below site-lib.</p>
<p> The command ocamlfind install copes with this layout, too. The variable destdir must contain the absolute location of site-lib, and the variable metadir must contain the absolute location of metaregistry. Note that ocamlfind install automatically adds a directory directive to the META file, so you need not do it manually.</p>
