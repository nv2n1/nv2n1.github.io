---

title: "osinfo-query(1)"
name: "osinfo-query"
section: "1"
letter: "o"
url: "/docs/linux/man/1-osinfo-query/"
description: "osinfo-query – Query information in the database"
---

<p> osinfo-query [<font SIZE="-1">OPTIONS&#8230;</font>] <font SIZE="-1">TYPE</font> [<font SIZE="-1">CONDITION-1</font> [<font SIZE="-1">CONDITION-2 &#8230;</font>]]</p>
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
<dt><code>-s </code><font SIZE="-1"><code>PROPERTY</code></font>, <code>&#8211;sort-key </code><font SIZE="-1"><code>PROPERTY</code></font></dt>
<dd> Set the data sorting key. Defaults sorting the first column</dd>
<dt><code>-f </code><font SIZE="-1"><code>PROPERTY1,PROPERTY2,&#8230;</code></font>, <code>&#8211;fields </code><font SIZE="-1"><code>PROPERTY1,PROPERTY2,&#8230;</code></font></dt>
<dd> Set the visibility of properties in output</dd></dl>
<h2>PROPERTY NAMES</h2>
<h3><font SIZE="-1">OS</font></h3>
<p> Valid property names for the <tt>&quot;os&quot;</tt> type are:</p>
<dl>
<dt><code>short-id</code></dt>
<dd> The short <font SIZE="-1">OS</font> identifier</dd>
<dt><code>name</code></dt>
<dd> The long <font SIZE="-1">OS</font> name</dd>
<dt><code>version</code></dt>
<dd> The <font SIZE="-1">OS</font> version string</dd>
<dt><code>family</code></dt>
<dd> The <font SIZE="-1">OS</font> kernel family</dd>
<dt><code>vendor</code></dt>
<dd> The <font SIZE="-1">OS</font> vendor</dd>
<dt><code>release-date</code></dt>
<dd> The <font SIZE="-1">OS</font> release date</dd>
<dt><code>eol-date</code></dt>
<dd> The <font SIZE="-1">OS</font> end-of-life date</dd>
<dt><code>codename</code></dt>
<dd> The <font SIZE="-1">OS</font> code name</dd>
<dt><code>id</code></dt>
<dd> The <font SIZE="-1">OS</font> identifier</dd></dl>
<h3><font SIZE="-1">PLATFORM</font></h3>
<p> Valid property names for the <tt>&quot;platform&quot;</tt> type are:</p>
<dl>
<dt><code>short-id</code></dt>
<dd> The short platform identifier</dd>
<dt><code>name</code></dt>
<dd> The long platform name</dd>
<dt><code>version</code></dt>
<dd> The platform version string</dd>
<dt><code>vendor</code></dt>
<dd> The platform vendor</dd>
<dt><code>release-date</code></dt>
<dd> The platform release date</dd>
<dt><code>eol-date</code></dt>
<dd> The platform end-of-life date</dd>
<dt><code>codename</code></dt>
<dd> The platform code name</dd>
<dt><code>id</code></dt>
<dd> The platform identifier</dd></dl>
<h3><font SIZE="-1">DEVICE</font></h3>
<p> Valid property names for the <tt>&quot;device&quot;</tt> type are:</p>
<dl>
<dt><code>name</code></dt>
<dd> The device name</dd>
<dt><code>product</code></dt>
<dd> The device product name</dd>
<dt><code>product-id</code></dt>
<dd> The device product <font SIZE="-1">ID</font> string</dd>
<dt><code>vendor</code></dt>
<dd> The device vendor name</dd>
<dt><code>vendor-id</code></dt>
<dd> The device vendor <font SIZE="-1">ID</font> string</dd>
<dt><code>class</code></dt>
<dd> The device type class</dd>
<dt><code>bus</code></dt>
<dd> The device bus type</dd>
<dt><code>id</code></dt>
<dd> The device identifier</dd></dl>
<h3><font SIZE="-1">DEPLOYMENT</font></h3>
<p> Valid property names for the <tt>&quot;deployment&quot;</tt> type are:</p>
<dl>
<dt><code>id</code></dt>
<dd> The deployment identifier</dd></dl>
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
