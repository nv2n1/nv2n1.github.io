---
title: "gpt-query(8)"
name: "gpt-query"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gpt-query/"
description: "gpt-query – Queries an installation for packages"
---

<p><code>gpt-query</code> &#8211; Queries an installation for packages</p>
<h2>Synopsis</h2>
<p>gpt-query [-name=Name -flavor=Flavor -pkgtype=Type &#8211;help -file=name -man -deps=run|sdk] [pkgname-flavor-pkgtype+]</p>
<h2>Description</h2>
<p><code>gpt-query</code> searches installed packages for matches to the query. <i>Name</i> is the name of the package. <i>Flavor</i> is the information about linking and compile options used on package. <i>Type</i> is the type of the package. <i>?</i> will alow the use to access system help. </p>
<p> The user may enter a value for any of the options. These options can be used in combination or not at all. The script will take the options being used and try to find all matching items. </p>
<p> An alternate form is to use the pkgname-flavor-pkgtype tuples. Multiple of instances of these tuples can be used in a query.</p>
<h2>Options</h2>
<dl>
<dt><code>-name=NAME</code></dt>
<dd>
<pre> Returns all of the packages matching NAME.</pre>
</dd><dt><code>-flavor=FLAVOR</code></dt>
<dd>Returns all of the packages matching FLAVOR.</dd>
<dt><code>-pkgtype=TYPE</code></dt>
<dd>Returns all of the packages matching TYPE.</dd>
<dt><code>-file=FILE</code></dt>
<dd>Returns the package owning the FILE. FILE needs to be either an absolute path or referenced to <tt>$GLOBUS_LOCATION</tt>.</dd>
<dt><code>-deps=run|sdk</code></dt>
<dd>Returns the runtime or build dependencies of a package.</dd>
<dt><code>-help</code></dt>
<dd>Print a brief help message and exits.</dd>
<dt><code>-man</code></dt>
<dd>Prints the manual page and exits.</dd>
<dt><code>-version</code></dt>
<dd>Prints the version of GPT and exits.</dd>
<dt><code>-what-bundles</code></dt>
<dd>Prints a list of the installed bundles.</dd>
<dt><code>-verify-bundle=BUNDLE</code></dt>
<dd>Takes a bundle defintion and checks to see if it matches the installation.</dd>
<dt><code>-bundle-packages=BUNDLE</code></dt>
<dd>List the packages that belong to the desired bundle.</dd>
<dt><code>-bundle </code><code>BUNDLE</code><code> 1 [</code><code>BUNDLE</code><code> 2]</code></dt>
<dd>If two bundles are given, the bundles will be compared to one another for equality. If only one bundle is given, the bundle will be checked against the installation. This command works on tar bundles.</dd></dl>
<h2>Examples</h2>
<pre> gpt-query</pre>
<p>Returns a listing of all of the installed packages. </p>
<pre> gpt-query -name=foo</pre>
<p>Returns all flavors and package types with the name &#8220;foo&#8221;. </p>
<pre> gpt-query foo</pre>
<p>Also returns all flavors and package types with the name &#8220;foo&#8221;. </p>
<pre> gpt-query 'foo-*-*'</pre>
<p>A third way of typing the same query. Note the single quotes. </p>
<pre> gpt-query '*-noflavor-*'</pre>
<p>List all of the packages with a &#8216;noflavor&#8217; build flavor. </p>
<pre> gpt-query -file=libexec/globus-build-env-gcc32.sh</pre>
<p>Returns &#8220;/libexec/globus-build-env-gcc32.sh is owned by globus_core-gcc32-rtl&#8221; </p>
<pre> gpt-query -file=$GLOBUS_LOCATION/libexec/globus-build-env-gcc32.sh</pre>
<p>Returns the same. </p>
<pre> gpt-query -file=globus-build-env-gcc32.sh</pre>
<p>Returns an error because the path is incorrect.</p>
<h2>Output</h2>
<p>Here is an example output: </p>
<pre> gpt-query '*-noflavor-*'
 4 packages were found in /home/mbletzin/work/install that matched your query:
 packages found that matched your query 
 globus_core-noflavor-data ver: 2.1 cmp id: 2.1.0
 globus_core_setup-noflavor-pgm ver: 2.0 cmp id: 2.0.0
 globus_ssl_utils-noflavor-data ver: 2.1 cmp id: 2.1.0
 kca_setup-noflavor-pgm ver: 3.0.2p1 cmp id: 1.0.0</pre>
<p>For each package name, flavor, package type, version, and the compatibility identifier is return. The compatibility identifier is what is used to resolve dependencies.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-gpt-install/">gpt-install</a></i>(8) <i><a href="/docs/linux/man/8-gpt-uninstall/">gpt-uninstall</a></i>(8) <i><a href="/docs/linux/man/8-gpt-verify/">gpt-verify</a></i>(8) <i><a href="/docs/linux/man/8-gpt-postinstall/">gpt-postinstall</a></i>(8)</p>
<h2>Author</h2>
<p>Michael Bletzinger &lt;mbletzin.ncsa.uiuc.edu&gt; and Eric Blau &lt;eblau.ncsa.uiuc.edu&gt;</p>
