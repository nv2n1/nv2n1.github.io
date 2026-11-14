---
title: "lintianreportingresourcemanager(3)"
name: "lintianreportingresourcemanager"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianreportingresourcemanager/"
description: "Lintian::Reporting::ResourceManager — A simple resource manager for html_reports"
---

<p>Lintian::Reporting::ResourceManager &#8212; A simple resource manager for html_reports </p>
<h2>Synopsis</h2>
<pre> use Lintian::Reporting::ResourceManager;
 
 my $resMan = Lintian::Reporting::ResourceManager-&gt;new(
 'html_dir' =&gt; 'path/to/HTML-root',
 );
 # Copy the resource
 $resMan-&gt;install_resource('path/to/my-image.png', { install_method =&gt; 'copy'} );
 # Move the resource
 $resMan-&gt;install_resource('path/to/generated-styles.css');
 print 'Image: ' . $resMan-&gt;resource_URL('my-image.png'), &quot;
&quot;;
 print 'CSS: ' . $resMan-&gt;resource_URL('generated-styles.css'), &quot;
&quot;;</pre>
<h2>Description</h2>
<p>A simple resource manager for Lintian&#8217;s reporting tool, <code>html_reports</code>.</p>
<h2>Class Methods</h2>
<dl COMPACT>
<dt>new(<font SIZE="-1">TYPE, OPTS</font>)</p>
<dd>Instantiates a new resource manager. </p>
<p> <font SIZE="-1">OPTS</font> is a key-value list, which must contain the key &#8220;html_dir&#8221; set to the root of the <font SIZE="-1">HTML</font> path. It is beneath this path that all resources will be installed</dl>
<h2>Instance Methods</h2>
<dl COMPACT>
<dt>install_resource(RESOURCE[, <font SIZE="-1">OPT</font>])</p>
<dd>Installs <font SIZE="-1">RESOURCE</font> into the html root. The resource may be renamed (based on content etc.). </p>
<p> Note that the basename of <font SIZE="-1">RESOURCE</font> must be unique between all resources installed. See &#8220;resource_URL(<font SIZE="-1">RESOURCE_NAME</font>)&#8221;. </p>
<p> If <font SIZE="-1">OPT</font> is given, it must be a hashref with 0 or more of the following keys (and values).</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>install_method</p>
<dd>Can be &#8220;copy&#8221; or &#8220;move&#8221; (default). If set to &#8220;move&#8221;, the original file will be renamed into its new location. Otherwise, a copy is done and the original file is left in place.</p>
<dt>source_file</p>
<dd>By default, the path denoted by <font SIZE="-1">RESOURCE</font> is both the resource name and the source file. This option can be used to install a given file as <font SIZE="-1">RESOURCE</font> regardless of the basename of the source file. </p>
<p> If this is passed, <font SIZE="-1">RESOURCE</font> must be a basename (i.e. without any slashes).</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt>resource_URL(<font SIZE="-1">RESOURCE_NAME</font>)</p>
<dd>Returns the path (relative to the <font SIZE="-1">HTML</font> root) to a resource installed via &#8220;install_resource(<font SIZE="-1">RESOURCE</font>)&#8221;, where <font SIZE="-1">RESOURCE_NAME</font> is the basename of the path given to install_resource.</p>
<dt>resource_integrity_value(<font SIZE="-1">RESOURCE_NAME</font>)</p>
<dd>Return a string that is valid in the &#8220;integrity&#8221; field of a <tt>&quot;&lt;link&gt;&quot;</tt> <font SIZE="-1">HTML</font> tag. (See <a rel="nofollow" href="https://www.w3.org/TR/SRI/)">https://www.w3.org/TR/SRI/)</a></dl>
<h2>Author</h2>
<p>Originally written by Niels Thykier &lt;niels [at] thykier.net&gt; for Lintian.</p>
