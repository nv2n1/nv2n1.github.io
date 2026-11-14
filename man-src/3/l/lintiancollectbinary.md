---
title: "lintiancollectbinary(3)"
name: "lintiancollectbinary"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintiancollectbinary/"
description: "Lintian::Collect::Binary – Lintian interface to binary package data collection"
---

<p>Lintian::Collect::Binary &#8211; Lintian interface to binary package data collection </p>
<h2>Synopsis</h2>
<pre> my ($name, $type, $dir) = ('foobar', 'binary', '/path/to/lab-entry');
 my $collect = Lintian::Collect-&gt;new ($name, $type, $dir);
 if ($collect-&gt;native) {
 print &quot;Package is native
&quot;;
 }</pre>
<h2>Description</h2>
<p>Lintian::Collect::Binary provides an interface to package data for binary packages. It implements data collection methods specific to binary packages. </p>
<p> This module is in its infancy. Most of Lintian still reads all data from files in the laboratory whenever that data is needed and generates that data via collect scripts. The goal is to eventually access all data about binary packages via this module so that the module can cache data where appropriate and possibly retire collect scripts in favor of caching that data in memory.</p>
<h2>Class Methods</h2>
<dl COMPACT>
<dt>new (<font SIZE="-1">PACKAGE</font>)</p>
<dd>Creates a new Lintian::Collect::Binary object. Currently, <font SIZE="-1">PACKAGE</font> is ignored. Normally, this method should not be called directly, only via the Lintian::Collect constructor.</dl>
<h2>Instance Methods</h2>
<p>In addition to the instance methods listed below, all instance methods documented in the Lintian::Collect and the Lintian::Collect::Package modules are also available.</p>
<dl COMPACT>
<dt>native</p>
<dd>Returns true if the binary package is native and false otherwise. Nativeness will be judged by the source version number. </p>
<p> If the version number is absent, this will return false (as native packages are a lot rarer than non-native ones). </p>
<p> Needs-Info requirements for using <i>native</i>: Same as field</p>
<dt>changelog</p>
<dd>Returns the changelog of the binary package as a Parse::DebianChangelog object, or undef if the changelog doesn&#8217;t exist. The changelog-file collection script must have been run to create the changelog file, which this method expects to find in <i>changelog</i>. </p>
<p> Needs-Info requirements for using <i>changelog</i>: changelog-file</p>
<dt>control ([<font SIZE="-1">FILE</font>])</p>
<dd><code>This method is deprecated</code>. Consider using &#8220;control_index_resolved_path(<font SIZE="-1">PATH</font>)&#8221; instead, which returns Lintian::Path objects. </p>
<p> Returns the path to <font SIZE="-1">FILE</font> in the control.tar.gz. <font SIZE="-1">FILE</font> must be either a Lintian::Path object (&gt;= 2.5.13~) or a string denoting the requested path. In the latter case, the path must be relative to the root of the control.tar.gz member and should be normalized. </p>
<p> It is not permitted for <font SIZE="-1">FILE</font> to be <tt>&quot;undef&quot;</tt>. If the &#8220;root&#8221; dir is desired either invoke this method without any arguments at all, pass it the correct Lintian::Path or the empty string. </p>
<p> To get a list of entries in the control.tar.gz or the file meta data of the entries (as path objects), see &#8220;sorted_control_index&#8221; and &#8220;control_index (<font SIZE="-1">FILE</font>)&#8221;. </p>
<p> The caveats of unpacked also apply to this method. However, as the control.tar.gz is not known to contain symlinks, a simple file type check is usually enough. </p>
<p> Needs-Info requirements for using <i>control</i>: bin-pkg-control</p>
<dt>control_index (<font SIZE="-1">FILE</font>)</p>
<dd>Returns a path object to <font SIZE="-1">FILE</font> in the control.tar.gz. <font SIZE="-1">FILE</font> must be relative to the root of the control.tar.gz and must be without leading slash (or &#8220;./&#8221;). If <font SIZE="-1">FILE</font> is not in the control.tar.gz, it returns <tt>&quot;undef&quot;</tt>. </p>
<p> To get a list of entries in the control.tar.gz, see &#8220;sorted_control_index&#8221;. To actually access the underlying file (e.g. the contents), use &#8220;control ([<font SIZE="-1">FILE</font>])&#8221;. </p>
<p> Note that the &#8220;root directory&#8221; (denoted by the empty string) will always be present, even if the underlying tarball omits it. </p>
<p> Needs-Info requirements for using <i>control_index</i>: bin-pkg-control</p>
<dt>sorted_control_index</p>
<dd>Returns a sorted array of file names listed in the control.tar.gz. The names will not have a leading slash (or &#8220;./&#8221;) and can be passed to &#8220;control ([<font SIZE="-1">FILE</font>])&#8221; or &#8220;control_index (<font SIZE="-1">FILE</font>)&#8221; as is. </p>
<p> The array will not contain the entry for the &#8220;root&#8221; of the control.tar.gz. </p>
<p> Needs-Info requirements for using <i>sorted_control_index</i>: Same as control_index</p>
<dt>control_index_resolved_path(<font SIZE="-1">PATH</font>)</p>
<dd>Resolve <font SIZE="-1">PATH</font> (relative to the root of the package) and return the entry denoting the resolved path. </p>
<p> The resolution is done using resolve_path. </p>
<p> Needs-Info requirements for using <i>control_index_resolved_path</i>: Same as control_index</p>
<dt>strings (<font SIZE="-1">FILE</font>)</p>
<dd>Returns an open handle, which will read the data from coll/strings for <font SIZE="-1">FILE.</font> If coll/strings did not collect any strings about <font SIZE="-1">FILE,</font> this returns an open read handle with no content. </p>
<p> Caller is responsible for closing the handle either way. </p>
<p> Needs-Info requirements for using <i>strings</i>: strings</p>
<dt>scripts</p>
<dd>Returns a hashref mapping a <font SIZE="-1">FILE</font> to its script/interpreter information (if <font SIZE="-1">FILE</font> is a script). If <font SIZE="-1">FILE</font> is not a script, it is not in the hash (and callers should use exists to test membership to ensure this invariant holds). </p>
<p> The value for a given <font SIZE="-1">FILE</font> consists of a table with the following keys (and associated value):</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>calls_env</p>
<dd>Returns a truth value if the script uses env (/usr/bin/env or /bin/env) in the &#8220;#!&#8221;. Otherwise it is <tt>&quot;undef&quot;</tt>.</p>
<dt>interpreter</p>
<dd>This is the interpreter used. If calls_env is true, this will be the first argument to env. Otherwise it will be the command listed after the &#8220;#!&#8221;. </p>
<p> <font SIZE="-1">NB:</font> Some template files have &#8220;#!&#8221; lines like &#8220;#!@PERL@&#8221; or &#8220;#!perl&#8221;. In this case, this value will be <tt>@PERL</tt>@ or perl (respectively).</p>
<dt>name</p>
<dd>Return the file name of the script. This will be identical to key to look up this table.</dl>
</dl>
<dl COMPACT>
<dd>Needs-Info requirements for using <i>scripts</i>: scripts</dl>
<dt>objdump_info</p>
<dd>Returns a hashref mapping a <font SIZE="-1">FILE</font> to the data collected by objdump-info or <tt>&quot;undef&quot;</tt> if no data is available for that <font SIZE="-1">FILE.</font> Data is generally only collected for <font SIZE="-1">ELF</font> files. </p>
<p> Needs-Info requirements for using <i>objdump_info</i>: objdump-info</p>
<dt>hardening_info</p>
<dd>Returns a hashref mapping a <font SIZE="-1">FILE</font> to its hardening issues. </p>
<p> <font SIZE="-1">NB:</font> This is generally only useful for checks/binaries to emit the hardening-no-* tags. </p>
<p> Needs-Info requirements for using <i>hardening_info</i>: hardening-info</p>
<dt>java_info</p>
<dd>Returns a hashref containing information about <font SIZE="-1">JAR</font> files found in binary packages, in the form <i>file name</i> -&gt; <i>info</i>, where <i>info</i> is a hash containing the following keys:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>manifest</p>
<dd>A hash containing the contents of the <font SIZE="-1">JAR</font> file manifest. For instance, to find the classpath of <i></i>$file<i></i>, you could use: </p>
<pre> if (exists $info-&gt;java_info-&gt;{$file}{'manifest'}) {
 my $cp = $info-&gt;java_info-&gt;{$file}{'manifest'}{'Class-Path'};
 # ...
 }</pre>
<p><font SIZE="-1">NB:</font> Not all jar files have a manifest. For those without, this will value will not be available. Use exists (rather than defined) to check for it.</p>
<dt>files</p>
<dd>A table of the files in the <font SIZE="-1">JAR.</font> Each key is a file name and its value is its &#8220;Major class version&#8221; for Java or &#8220;-&#8221; if it is not a class file.</p>
<dt>error</p>
<dd>If it exists, this is an error that occurred during reading of the zip file. If it exists, it is unlikely that the other fields will be present.</dl>
</dl>
<dl COMPACT>
<dd>Needs-Info requirements for using <i>java_info</i>: java-info</dl>
<dt>relation (<font SIZE="-1">FIELD</font>)</p>
<dd>Returns a Lintian::Relation object for the specified <font SIZE="-1">FIELD,</font> which should be one of the possible relationship fields of a Debian package or one of the following special values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>all</p>
<dd>The concatenation of Pre-Depends, Depends, Recommends, and Suggests.</p>
<dt>strong</p>
<dd>The concatenation of Pre-Depends and Depends.</p>
<dt>weak</p>
<dd>The concatenation of Recommends and Suggests.</dl>
</dl>
<dl COMPACT>
<dd>If <font SIZE="-1">FIELD</font> isn&#8217;t present in the package, the returned Lintian::Relation object will be empty (always satisfied and implies nothing). </p>
<p> Needs-Info requirements for using <i>relation</i>: Same as field</dl>
<dt>is_pkg_class ([<font SIZE="-1">TYPE</font>])</p>
<dd>Returns a truth value if the package is the given <font SIZE="-1">TYPE</font> of special package. <font SIZE="-1">TYPE</font> can be one of &#8220;transitional&#8221;, &#8220;debug&#8221; or &#8220;any-meta&#8221;. If omitted it defaults to &#8220;any-meta&#8221;. The semantics for these values are:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>transitional</p>
<dd>The package is (probably) a transitional package (e.g. it is probably empty, just depend on stuff will eventually disappear.) </p>
<p> Guessed from package description.</p>
<dt>any-meta</p>
<dd>This package is (probably) some kind of meta or task package. A meta package is usually empty and just depend on stuff. It will also return a truth value for &#8220;tasks&#8221; (i.e. tasksel &#8220;tasks&#8221;). </p>
<p> A transitional package will also match this. </p>
<p> Guessed from package description, section or package name.</p>
<dt>debug</p>
<dd>The package is (probably) a package containing debug symbols. </p>
<p> Guessed from the package name.</p>
<dt>auto-generated</p>
<dd>The package is (probably) a package generated automatically (e.g. a dbgsym package) </p>
<p> Guessed from the &#8220;Auto-Built-Package&#8221; field.</dl>
</dl>
<dl COMPACT>
<dd>Needs-Info requirements for using <i>is_pkg_class</i>: Same as field</dl>
<dt>is_conffile (<font SIZE="-1">FILE</font>)</p>
<dd>Returns a truth value if <font SIZE="-1">FILE</font> is listed in the conffiles control file. If the control file is not present or <font SIZE="-1">FILE</font> is not listed in it, it returns <tt>&quot;undef&quot;</tt>. </p>
<p> Note that <font SIZE="-1">FILE</font> should be the filename relative to the package root (even though the control file uses absolute paths). If the control file does relative paths, they are assumed to be relative to the package root as well (and used without warning). </p>
<p> Needs-Info requirements for using <i>is_conffile</i>: Same as control_index_resolved_path</dl>
<h2>Author</h2>
<p>Originally written by Frank Lichtenheld &lt;djpig [at] debian.org&gt; for Lintian.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-lintian/">lintian</a></i>(1), Lintian::Collect, Lintian::Relation</p>
