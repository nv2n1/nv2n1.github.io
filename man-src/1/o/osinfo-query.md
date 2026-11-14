---
title: "osinfo-query(1)"
name: "osinfo-query"
section: "1"
letter: "o"
url: "/docs/linux/man/1-osinfo-query/"
description: "osinfo-query – Query information in the database"
---

<h2 class="name">NAME</h2>
<p> osinfo-query &#8211; Query information in the database </p>
<h2>SYNOPSIS</h2>
<p> osinfo-query [<font SIZE="-1">OPTIONS&#8230;</font>] <font SIZE="-1">TYPE</font> [<font SIZE="-1">CONDITION-1</font> [<font SIZE="-1">CONDITION-2 &#8230;</font>]]</p>
<h2>DESCRIPTION</h2>
<p> The <tt>&quot;osinfo-query&quot;</tt> command allows extraction of information from the database. <font SIZE="-1"><code>TYPE</code></font> can be one of <tt>&quot;os&quot;</tt>, <tt>&quot;platform&quot;</tt>, <tt>&quot;device&quot;</tt>, or <tt>&quot;deployment&quot;</tt>. With no conditions specified, all entities of the given type will be listed. </p>
<pre><code>
#List all operating systems
$ osinfo - query os
               Short ID |
    Name... -- -- -- -- -- -- -- -- -- -- --+-- -- -- -- -- -centos - 6.0 | CentOS 6.0 ... centos - 6.1 | CentOS 6.1 ......
</code></pre>
<p> Conditions allow filtering based on specific properties of an entity. For example, to filter only distros from the Fedora Project, use </p>
<p>#List all operating systems<br />
$ osinfo &#8211; query os vendor = &#8220;Fedora Project&#8221; Short ID | Name&#8230; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;fedora1 | Fedora Core 1 &#8230; fedora2 | Fedora Core 2 &#8230;&#8230;</p>
<p> The set of fields which are printed can be controlled using the <tt>&quot;--fields&quot;</tt> command line argument: </p>
<pre><code>
#List all operating systems
$ osinfo - query-- fields = short - id, version os vendor = "Fedora Project" Short ID | Version-- -- -- -- -- -- -- -- -- -- --+-- -- -- -- --fedora1 | 1 fedora2 | 2 ...
</code></pre>
<h2>OPTIONS</h2>
<dl>
<dt><code>-s </code><font SIZE="-1"><code>PROPERTY</code></font>, <code>&#8211;sort-key </code><font SIZE="-1"><code>PROPERTY</code></font></p>
<dd> Set the data sorting key. Defaults sorting the first column</p>
<dt><code>-f </code><font SIZE="-1"><code>PROPERTY1,PROPERTY2,&#8230;</code></font>, <code>&#8211;fields </code><font SIZE="-1"><code>PROPERTY1,PROPERTY2,&#8230;</code></font></p>
<dd> Set the visibility of properties in output</dl>
<h2>PROPERTY NAMES</h2>
<h3><font SIZE="-1">OS</font></h3>
<p> Valid property names for the <tt>&quot;os&quot;</tt> type are:</p>
<dl>
<dt><code>short-id</code></p>
<dd> The short <font SIZE="-1">OS</font> identifier</p>
<dt><code>name</code></p>
<dd> The long <font SIZE="-1">OS</font> name</p>
<dt><code>version</code></p>
<dd> The <font SIZE="-1">OS</font> version string</p>
<dt><code>family</code></p>
<dd> The <font SIZE="-1">OS</font> kernel family</p>
<dt><code>vendor</code></p>
<dd> The <font SIZE="-1">OS</font> vendor</p>
<dt><code>release-date</code></p>
<dd> The <font SIZE="-1">OS</font> release date</p>
<dt><code>eol-date</code></p>
<dd> The <font SIZE="-1">OS</font> end-of-life date</p>
<dt><code>codename</code></p>
<dd> The <font SIZE="-1">OS</font> code name</p>
<dt><code>id</code></p>
<dd> The <font SIZE="-1">OS</font> identifier</dl>
<h3><font SIZE="-1">PLATFORM</font></h3>
<p> Valid property names for the <tt>&quot;platform&quot;</tt> type are:</p>
<dl>
<dt><code>short-id</code></p>
<dd> The short platform identifier</p>
<dt><code>name</code></p>
<dd> The long platform name</p>
<dt><code>version</code></p>
<dd> The platform version string</p>
<dt><code>vendor</code></p>
<dd> The platform vendor</p>
<dt><code>release-date</code></p>
<dd> The platform release date</p>
<dt><code>eol-date</code></p>
<dd> The platform end-of-life date</p>
<dt><code>codename</code></p>
<dd> The platform code name</p>
<dt><code>id</code></p>
<dd> The platform identifier</dl>
<h3><font SIZE="-1">DEVICE</font></h3>
<p> Valid property names for the <tt>&quot;device&quot;</tt> type are:</p>
<dl>
<dt><code>name</code></p>
<dd> The device name</p>
<dt><code>product</code></p>
<dd> The device product name</p>
<dt><code>product-id</code></p>
<dd> The device product <font SIZE="-1">ID</font> string</p>
<dt><code>vendor</code></p>
<dd> The device vendor name</p>
<dt><code>vendor-id</code></p>
<dd> The device vendor <font SIZE="-1">ID</font> string</p>
<dt><code>class</code></p>
<dd> The device type class</p>
<dt><code>bus</code></p>
<dd> The device bus type</p>
<dt><code>id</code></p>
<dd> The device identifier</dl>
<h3><font SIZE="-1">DEPLOYMENT</font></h3>
<p> Valid property names for the <tt>&quot;deployment&quot;</tt> type are:</p>
<dl>
<dt><code>id</code></p>
<dd> The deployment identifier</dl>
<h2>EXIT STATUS</h2>
<p> The exit status will be 0 if matching entries were found, or 1 if not matches were found</p>
<h2>SEE ALSO</h2>
<p> <tt>&quot;<a href="/docs/linux/man/1-osinfo-db-validate/">osinfo-db-validate</a>(1)&quot;</tt>, <tt>&quot;<a href="/docs/linux/man/1-osinfo-detect/">osinfo-detect</a>(1)&quot;</tt></p>
<h2>AUTHORS</h2>
<p> Daniel P. Berrange &lt;berrange [at] redhat.com&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2012, 2014 Red Hat, Inc.</p>
<h2>LICENSE</h2>
<p> <tt>&quot;osinfo-query&quot;</tt> is distributed under the termsof the <font SIZE="-1">GNU LGPL</font> v2+ license. This is free software; see the source for copying conditions. There is <font SIZE="-1">NO</font> warranty; not even for <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE</font> </p>
<h2>Index</h2>
<dt><a href="#lbAK">EXIT STATUS</a></p>
<dd>
<dt><a href="#lbAL">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAM">AUTHORS</a></p>
<dd>
<dt><a href="#lbAN">COPYRIGHT</a></p>
<dd>
<dt><a href="#lbAO">LICENSE</a></p>
<dd></dl>
