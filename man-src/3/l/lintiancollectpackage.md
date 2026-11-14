---
title: "lintiancollectpackage(3)"
name: "lintiancollectpackage"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintiancollectpackage/"
description: "Lintian::Collect::Package – Lintian base interface to binary and source package data collection"
---

<p>Lintian::Collect::Package &#8211; Lintian base interface to binary and source package data collection </p>
<h2>Synopsis</h2>
<pre> use autodie;
 use Lintian::Collect;
 
 my ($name, $type, $dir) = ('foobar', 'source', '/path/to/lab-entry');
 my $info = Lintian::Collect-&gt;new ($name, $type, $dir);
 my $filename = &quot;etc/conf.d/$name.conf&quot;;
 my $file = $info-&gt;index_resolved_path($filename);
 if ($file and $file-&gt;is_open_ok) {
 my $fd = $info-&gt;open;
 # Use $fd ...
 close($fd);
 } elsif ($file) {
 print &quot;$file is available, but is not a file or unsafe to open
&quot;;
 } else {
 print &quot;$file is missing
&quot;;
 }</pre>
<h2>Description</h2>
<p>Lintian::Collect::Package provides part of an interface to package data for source and binary packages. It implements data collection methods specific to all packages that can be unpacked (or can contain files) </p>
<p> This module is in its infancy. Most of Lintian still reads all data from files in the laboratory whenever that data is needed and generates that data via collect scripts. The goal is to eventually access all data about source packages via this module so that the module can cache data where appropriate and possibly retire collect scripts in favor of caching that data in memory.</p>
<h2>Instance Methods</h2>
<p>In addition to the instance methods listed below, all instance methods documented in the Lintian::Collect module are also available.</p>
<dl COMPACT>
<dt>unpacked ([<font SIZE="-1">FILE</font>])</p>
<dd>Returns the path to the directory in which the package has been unpacked. <font SIZE="-1">FILE</font> must be either a Lintian::Path object (&gt;= 2.5.13~) or a string denoting the requested path. In the latter case, the path must be relative to the root of the package and should be normalized. </p>
<p> It is not permitted for <font SIZE="-1">FILE</font> to be <tt>&quot;undef&quot;</tt>. If the &#8220;root&#8221; dir is desired either invoke this method without any arguments at all, pass it the correct Lintian::Path or the empty string. </p>
<p> If <font SIZE="-1">FILE</font> is not in the package, it returns the path to a non-existent file entry. </p>
<p> The path returned is not guaranteed to be inside the Lintian Lab as the package may have been unpacked outside the Lab (e.g. as optimization). </p>
<p> Caveat with symlinks: Package is extracted as is and the path returned by this method points to the extracted file object. If this is a symlink, it may &#8220;escape the root&#8221; and point to a file outside the lab (and a path traversal). </p>
<p> The following code may be helpful in checking for path traversal: </p>
<pre> use Lintian::Util qw(is_ancestor_of);
 my $collect = ... ;
 my $file = '../../../etc/passwd';
 my $uroot = $collect-&gt;unpacked;
 my $ufile = $collect-&gt;unpacked($file);
 # $uroot will exist, but $ufile might not.
 if ( -e $ufile &amp;&amp; is_ancestor_of($uroot, $ufile)) {
 # has not escaped $uroot
 do_stuff($ufile);
 } elsif ( -e $ufile) {
 # escaped $uroot
 die &quot;Possibly path traversal ($file)&quot;;
 } else {
 # Does not exists
 }</pre>
<p>Alternatively one can use normalize_pkg_path in Lintian::Util or link_normalized. </p>
<p> To get a list of entries in the package or the file meta data of the entries (as path objects), see &#8220;sorted_index&#8221; and &#8220;index (<font SIZE="-1">FILE</font>)&#8221;. </p>
<p> Needs-Info requirements for using <i>unpacked</i>: unpacked</p>
<dt>file_info (<font SIZE="-1">FILE</font>)</p>
<dd>Returns the output of <i><a href="/docs/linux/man/1-file/">file</a></i>(1) -e ascii for <font SIZE="-1">FILE</font> (if it exists) or <tt>&quot;undef&quot;</tt>. </p>
<p> <font SIZE="-1"><code>CAVEAT</code></font>: As <i><a href="/docs/linux/man/1-file/">file</a></i>(1) is passed &#8220;-e ascii&#8221;, all text files will be considered &#8220;data&#8221; rather than &#8220;text&#8221;, &#8220;Java code&#8221; etc. </p>
<p> <font SIZE="-1">NB:</font> The value may have been calibrated by Lintian. A notorious example is gzip files, where <i><a href="/docs/linux/man/1-file/">file</a></i>(1) can be unreliable at times (see #620289) </p>
<p> Needs-Info requirements for using <i>file_info</i>: file-info</p>
<dt>md5sums</p>
<dd>Returns a hashref mapping a <font SIZE="-1">FILE</font> to its md5sum. The md5sum is computed by Lintian during extraction and is not guaranteed to match the md5sum in the &#8220;md5sums&#8221; control file. </p>
<p> Needs-Info requirements for using <i>md5sums</i>: md5sums</p>
<dt>index (<font SIZE="-1">FILE</font>)</p>
<dd>Returns a path object to <font SIZE="-1">FILE</font> in the package. <font SIZE="-1">FILE</font> must be relative to the root of the unpacked package and must be without leading slash (or &#8220;./&#8221;). If <font SIZE="-1">FILE</font> is not in the package, it returns <tt>&quot;undef&quot;</tt>. If <font SIZE="-1">FILE</font> is supposed to be a directory, it must be given with a trailing slash. Example: </p>
<pre> my $file = $info-&gt;index (&quot;usr/bin/lintian&quot;);
 my $dir = $info-&gt;index (&quot;usr/bin/&quot;);</pre>
<p>To get a list of entries in the package, see &#8220;sorted_index&#8221;. To actually access the underlying file (e.g. the contents), use &#8220;unpacked ([<font SIZE="-1">FILE</font>])&#8221;. </p>
<p> Note that the &#8220;root directory&#8221; (denoted by the empty string) will always be present, even if the underlying tarball omits it. </p>
<p> Needs-Info requirements for using <i>index</i>: unpacked</p>
<dt>sorted_index</p>
<dd>Returns a sorted array of file names listed in the package. The names will not have a leading slash (or &#8220;./&#8221;) and can be passed to &#8220;unpacked ([<font SIZE="-1">FILE</font>])&#8221; or &#8220;index (<font SIZE="-1">FILE</font>)&#8221; as is. </p>
<p> The array will not contain the entry for the &#8220;root&#8221; of the package. </p>
<p> <font SIZE="-1">NB:</font> For source packages, please see the &#8220;index&#8221;-caveat. </p>
<p> Needs-Info requirements for using <i>sorted_index</i>: Same as index</p>
<dt>index_resolved_path(<font SIZE="-1">PATH</font>)</p>
<dd>Resolve <font SIZE="-1">PATH</font> (relative to the root of the package) and return the entry denoting the resolved path. </p>
<p> The resolution is done using resolve_path. </p>
<p> <font SIZE="-1">NB:</font> For source packages, please see the &#8220;index&#8221;-caveat. </p>
<p> Needs-Info requirements for using <i>index_resolved_path</i>: Same as index</dl>
<h2>Author</h2>
<p>Originally written by Niels Thykier &lt;niels [at] thykier.net&gt; for Lintian.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-lintian/">lintian</a></i>(1), Lintian::Collect, Lintian::Collect::Binary, Lintian::Collect::Source</p>
