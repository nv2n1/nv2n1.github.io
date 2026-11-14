---
title: "xmlcatalog(1)"
name: "xmlcatalog"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xmlcatalog/"
description: "xmlcatalog – Command line tool to parse and manipulate XML or SGML catalog files."
---

<h2 class="name">NAME</h2>
<p> xmlcatalog &#8211; Command line tool to parse and manipulate XML or SGML catalog files. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>xmlcatalog</code> [<code>&#8211;sgml</code> | <code>&#8211;shell</code> | <code>&#8211;create</code> | <code>&#8211;del&nbsp;</code><i>VALUE(S)</i> | [&nbsp;<code>&#8211;add&nbsp;</code><i>TYPE</i><code>&nbsp;</code><i>ORIG</i><code>&nbsp;</code><i>REPLACE</i><code>&nbsp;</code>&nbsp;|&nbsp;<code>&#8211;add&nbsp;</code><i>FILENAME</i>] | <code>&#8211;noout</code> | <code>&#8211;no-super-update</code> | [<code>-v</code>&nbsp;|&nbsp;<code>&#8211;verbose</code>]] {<i>CATALOGFILE</i>} {<i>ENTITIES</i>&#8230;}</dl>
<h2>DESCRIPTION</h2>
<p> <code>xmlcatalog</code></p>
<dd>is a command line application allowing users to monitor and manipulate XML and SGML catalogs. It is included in <code><a href="/docs/linux/man/3-libxml/">libxml</a></code>(3). </p>
<p> Its functions can be invoked from a single command from the command line, or it can perform multiple functions in interactive mode. It can operate on both XML and SGML files.</p>
<h2>OPTIONS</h2>
<p> <code>xmlcatalog</code> accepts the following options (in alphabetical order): </p>
<p> <code>&#8211;add </code><i>TYPE</i><i>ORIG</i><i>REPLACE</i></p>
<dl>
<dt>
<dd> Add an entry to CATALOGFILE. <i>TYPE</i> indicates the type of entry. Possible types are: <i>public</i>, <i>system</i>, <i>uri</i>, <i>rewriteSystem</i>, <i>rewriteURI</i>, <i>delegatePublic</i>, <i>delegateSystem</i>, <i>delegateURI</i>, <i>nextCatalog</i>. <i>ORIG</i> is the original reference to be replaced, and <i>REPLACE</i> is the URI of the replacement entity to be used. The <code>&#8211;add</code> option will not overwrite CATALOGFILE, outputting to stdout, unless <code>&#8211;noout</code> is used. The <code>&#8211;add</code> will always take three parameters even if some of the XML catalog constructs will have only a single argument.</dl>
<p> <code>&#8211;add </code><i>FILENAME</i></p>
<dl>
<dt>
<dd> If the <code>&#8211;add</code> option is used following the <code>&#8211;sgml</code> option, only a single argument, a <i>FILENAME</i>, is used. This is used to add the name of a catalog file to an SGML supercatalog, a file that contains references to other included SGML catalog files.</dl>
<p> <code>&#8211;create</code></p>
<dl>
<dt>
<dd> Create a new XML catalog. Outputs to stdout, ignoring <i>filename</i> unless <code>&#8211;noout</code> is used, in which case it creates a new catalog file <i>filename</i>.</dl>
<p> <code>&#8211;del </code><i>VALUE(S)</i></p>
<dl>
<dt>
<dd> Remove entries from <i>CATALOGFILE</i> matching <i>VALUE(S)</i>. The <code>&#8211;del</code> option will not overwrite <i>CATALOGFILE</i>, outputting to stdout, unless <code>&#8211;noout</code> is used.</dl>
<p> <code>&#8211;noout</code></p>
<dl>
<dt>
<dd> Save output to the named file rather than outputting to stdout.</dl>
<p> <code>&#8211;no-super-update</code></p>
<dl>
<dt>
<dd> Do not update the SGML super catalog.</dl>
<p> <code>&#8211;shell</code></p>
<dl>
<dt>
<dd> Run a shell allowing interactive queries on catalog file <i>CATALOGFILE</i>. For the set of available commands see the section called &#8220;SHELL COMMANDS&#8221;.</dl>
<p> <code>&#8211;sgml</code></p>
<dl>
<dt>
<dd> Uses SGML super catalogs for <code>&#8211;add</code> and <code>&#8211;del</code> options.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Output debugging information.</dl>
<p> Invoking <code>xmlcatalog</code> non-interactively without a designated action (imposed with options like <code>&#8211;add</code>) will result in a lookup of the catalog entry for <i>ENTITIES</i> in the catalog denoted with <i>CATALOGFILE</i>. The corresponding entries will be output to the command line. This mode of operation, together with <code>&#8211;shell</code> mode and non-modifying (i.e. without <code>&#8211;noout</code>) direct actions, allows for a special shortcut of the void <i>CATALOGFILE</i> specification (possibly expressed as &quot;&quot; in the shell environment) appointing the default system catalog. That simplifies the handling when its exact location is irrelevant but the respective built-in still needs to be consulted.</p>
<h2>SHELL COMMANDS</h2>
<p> Invoking <code>xmlcatalog</code> with the <code>&#8211;shell </code><i>CATALOGFILE</i> option opens a command line shell allowing interactive access to the catalog file identified by <i>CATALOGFILE</i>. Invoking the shell provides a command line prompt after which the following commands (described in alphabetical order) can be entered. </p>
<p> <code>add </code><i>TYPE</i><i>ORIG</i><i>REPLACE</i></p>
<dl>
<dt>
<dd> Add an entry to the catalog file. <i>TYPE</i> indicates the type of entry. Possible types are: <i>public</i>, <i>system</i>, <i>uri</i>, <i>rewriteSystem</i>, <i>rewriteURI</i>, <i>delegatePublic</i>, <i>delegateSystem</i>, <i>delegateURI</i>, <i>nextCatalog</i>. <i>ORIG</i> is the original reference to be replaced, and <i>REPLACE</i> is the URI of the replacement entity to be used. The <code>&#8211;add</code> option will not overwrite CATALOGFILE, outputting to stdout, unless <code>&#8211;noout</code> is used. The <code>&#8211;add</code> will always take three parameters even if some of the XML catalog constructs will have only a single argument.</dl>
<p> <code>debug</code></p>
<dl>
<dt>
<dd> Print debugging statements showing the steps <code>xmlcatalog</code> is executing.</dl>
<p> <code>del </code><i>VALUE(S)</i></p>
<dl>
<dt>
<dd> Remove the catalog entry corresponding to <i>VALUE(S)</i>.</dl>
<p> <code>dump</code></p>
<dl>
<dt>
<dd> Print the current catalog.</dl>
<p> <code>exit</code></p>
<dl>
<dt>
<dd> Quit the shell.</dl>
<p> <code>public </code><i>PUBLIC-ID</i></p>
<dl>
<dt>
<dd> Execute a Formal Public Identifier lookup of the catalog entry for <i>PUBLIC-ID</i>. The corresponding entry will be output to the command line.</dl>
<p> <code>quiet</code></p>
<dl>
<dt>
<dd> Stop printing debugging statements.</dl>
<p> <code>system </code><i>SYSTEM-ID</i></p>
<dl>
<dt>
<dd> Execute a Formal Public Identifier lookup of the catalog entry for <i>SYSTEM-ID</i>. The corresponding entry will be output to the command line.</dl>
<h2>ENVIRONMENT</h2>
<p> <code>XML_CATALOG_FILES</code></p>
<dl>
<dt>
<dd> XML catalog behavior can be changed by redirecting queries to the user&#8217;s own set of catalogs. This can be done by setting the <code>XML_CATALOG_FILES</code> environment variable to a list of catalogs. An empty one should deactivate loading the default /etc/xml/catalog catalog.</dl>
<h2>DIAGNOSTICS</h2>
<p> <code>xmlcatalog</code> return codes provide information that can be used when calling it from scripts. </p>
<p> <code>0</code></p>
<dl>
<dt>
<dd> No error</dl>
<p> <code>1</code></p>
<dl>
<dt>
<dd> Failed to remove an entry from the catalog</dl>
<p> <code>2</code></p>
<dl>
<dt>
<dd> Failed to save to the catalog, check file permissions</dl>
<p> <code>3</code></p>
<dl>
<dt>
<dd> Failed to add an entry to the catalog</dl>
<p> <code>4</code></p>
<dl>
<dt>
<dd> Failed to look up an entry in the catalog</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libxml/">libxml</a></code>(3) </p>
<p> More information can be found at </p>
<dl>
<dt>
<dd> &bull; <code><a href="/docs/linux/man/3-libxml/">libxml</a></code>(3) web page m[blue]<code><a rel="nofollow" href="http://www.xmlsoft.org/">http://www.xmlsoft.org/</a></code>m[]</dl>
<dl>
<dt>
<dd> &bull; <code><a href="/docs/linux/man/3-libxml/">libxml</a></code>(3) catalog support web page at m[blue]<code><a rel="nofollow" href="http://www.xmlsoft.org/catalog.html">http://www.xmlsoft.org/catalog.html</a></code>m[]</dl>
<dl>
<dt>
<dd> &bull; James Clark&#8217;s SGML catalog page m[blue]<code><a rel="nofollow" href="http://www.jclark.com/sp/catalog.htm">http://www.jclark.com/sp/catalog.htm</a></code>m[]</dl>
<dl>
<dt>
<dd> &bull; OASIS XML catalog specification m[blue]<code><a rel="nofollow" href="http://www.oasis-open.org/committees/entity/spec.html">http://www.oasis-open.org/committees/entity/spec.html</a></code>m[]</dl>
<h2>AUTHOR</h2>
<p> <code>John Fleck</code> &lt;jfleck [at] inkstain.net&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001, 2004 </p>
<h2>Index</h2>
