---
title: "install-catalog(8)"
name: "install-catalog"
section: "8"
letter: "i"
url: "/docs/linux/man/8-install-catalog/"
description: "install-catalog – Manage a SGML or XML centralized catalog"
---

<p>install-catalog &#8211; Manage a SGML or XML centralized catalog</p>
<h2>Synopsis</h2>
<p><code>install-catalog</code> [ <code>option </code>] <code>action </code><i> &#8230;</i> [ <code> [ -d] [ &#8211;delegate] </code>] [ <code> [ -a </code><i>centralized</i><i>ordinary</i><code>] [ &#8211;add </code><i>centralized</i><i>ordinary</i><code>]<br />
&nbsp;<wbr>[&nbsp;<wbr>-r&nbsp;<wbr></code><i>centralized</i><code>&nbsp;<wbr></code><i>ordinary</i><code>]&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr>&#8211;remove&nbsp;<wbr></code><i>centralized</i><code>&nbsp;<wbr></code><i>ordinary</i><code>]&nbsp;<wbr><br />
&nbsp;<wbr>[&nbsp;<wbr>-h]&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr>&#8211;help]&nbsp;<wbr><br />
&nbsp;<wbr>[&nbsp;<wbr>-v]&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr>&#8211;version]&nbsp;<wbr></code>]&nbsp;<wbr> </p>
<h2>Description</h2>
<p>This shell script allows to handle a centralized catalog referencing other &quot;ordinary&quot; SGML or XML Open Catalogs. </p>
<p> An <i>Open Catalog</i> contains a set of directives defined by OASIS, mostly used for defining equivalences between FPIs (Formal Public Identifiers) and real file names (see TR9401:1997 on <a rel="nofollow" href="http://www.oasis-open.org">http://www.oasis-open.org</a> &lt;URL:<a href="http://www.oasis-open.org">http://www.oasis-open.org</a>&gt;). The Open Catalogs usually reside in <i>/usr/share/sgml</i>. </p>
<p> A <i>centralized catalog</i> is a special Open Catalog that includes only comments and CATALOG directives pointing to other catalogs (or DELEGATE directives if supported). The centralized catalog can be the key to all other SGML resources. It usually resides in <i>/etc/sgml</i>. </p>
<p> The centralized catalog can be edited manually or through the <code>install-catalog</code> script to add or remove references to other ordinary catalogs. This script is mainly destined to software package post-installation scripts. </p>
<p> An example of a typical call to install-catalog is: </p>
<pre> install-catalog --add \
 /usr/share/sgml/docbook/dsssl-stylesheets-1.54/catalog \
 /etc/sgml/sgml-docbook-4.0.cat</pre>
<p>This call will install in <i>/etc/sgml/sgml-docbook-4.0.cat</i> a reference to <i>/usr/share/sgml/docbook/dsssl-stylesheets-1.54/catalog</i>.</p>
<h2>Options</h2>
<p>Here is the list of options that can influence the way <code>install-catalog</code> works: </p>
<p>&nbsp;<wbr>[&nbsp;<wbr><code>&nbsp;<wbr>[&nbsp;<wbr>-d]&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr>&#8211;delegate]&nbsp;<wbr></code>]&nbsp;<wbr> </p>
<p> Use DELEGATE instead of CATALOG directives to specify a pointer</p>
<h2>Actions</h2>
<p>Here is the list of actions that can be requested to <code>install-catalog</code>: </p>
<p>&nbsp;<wbr>[&nbsp;<wbr><code>&nbsp;<wbr>[&nbsp;<wbr>-a&nbsp;<wbr></code><i>centralized</i><code>&nbsp;<wbr></code><i>ordinary</i><code>]&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr>&#8211;add&nbsp;<wbr></code><i>centralized</i><code>&nbsp;<wbr></code><i>ordinary</i><code>]&nbsp;<wbr></code>]&nbsp;<wbr> </p>
<p> Declare a new SGML package. </p>
<p>&nbsp;<wbr>[&nbsp;<wbr><code>&nbsp;<wbr>[&nbsp;<wbr>-r&nbsp;<wbr></code><i>centralized</i><code>&nbsp;<wbr></code><i>ordinary</i><code>]&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr>&#8211;remove&nbsp;<wbr></code><i>centralized</i><code>&nbsp;<wbr></code><i>ordinary</i><code>]&nbsp;<wbr></code>]&nbsp;<wbr> </p>
<p> Remove a previously installed SGML package. </p>
<p>&nbsp;<wbr>[&nbsp;<wbr><code>&nbsp;<wbr>[&nbsp;<wbr>-h]&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr>&#8211;help]&nbsp;<wbr></code>]&nbsp;<wbr> </p>
<p> Print a short help message and exit </p>
<p>&nbsp;<wbr>[&nbsp;<wbr><code>&nbsp;<wbr>[&nbsp;<wbr>-v]&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr>&#8211;version]&nbsp;<wbr></code>]&nbsp;<wbr> </p>
<p> Print the version identifier and exit</p>
<h2>Files</h2>
<p><i>/etc/sgml/*</i> </p>
<p> The SGML centralized catalogs</p>
<h2>Authors</h2>
<p>Eric Bischoff &lt;ebisch [at] cybercable.tm.fr&gt; </p>
<p> Developper of install-catalog.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-jw/">jw</a></code>(1) conversion from DocBook to other file formats <code><a href="/docs/linux/man/1-nsgmls/">nsgmls</a></code>(1) a base component of <code>Jade</code> DSSSL engine <a rel="nofollow" href="http://sourceware.cygnus.com/docbook-tools/">http://sourceware.cygnus.com/docbook-tools/</a> &lt;URL:<a href="http://sourceware.cygnus.com/docbook-tools/">http://sourceware.cygnus.com/docbook-tools/</a>&gt; the home page of the DocBook tools, a compendium of all tools necessary to process DocBook files, including the SGML-common stuff. </p>
