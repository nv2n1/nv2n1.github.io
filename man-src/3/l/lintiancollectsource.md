---
title: "lintiancollectsource(3)"
name: "lintiancollectsource"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintiancollectsource/"
description: "Lintian::Collect::Source – Lintian interface to source package data collection"
---

<p>Lintian::Collect::Source &#8211; Lintian interface to source package data collection </p>
<h2>Synopsis</h2>
<pre> my ($name, $type, $dir) = ('foobar', 'source', '/path/to/lab-entry');
 my $collect = Lintian::Collect-&gt;new ($name, $type, $dir);
 if ($collect-&gt;native) {
 print &quot;Package is native
&quot;;
 }</pre>
<h2>Description</h2>
<p>Lintian::Collect::Source provides an interface to package data for source packages. It implements data collection methods specific to source packages. </p>
<p> This module is in its infancy. Most of Lintian still reads all data from files in the laboratory whenever that data is needed and generates that data via collect scripts. The goal is to eventually access all data about source packages via this module so that the module can cache data where appropriate and possibly retire collect scripts in favor of caching that data in memory.</p>
<h2>Class Methods</h2>
<dl COMPACT>
<dt>new (<font SIZE="-1">PACKAGE</font>)</p>
<dd>Creates a new Lintian::Collect::Source object. Currently, <font SIZE="-1">PACKAGE</font> is ignored. Normally, this method should not be called directly, only via the Lintian::Collect constructor.</dl>
<h2>Instance Methods</h2>
<p>In addition to the instance methods listed below, all instance methods documented in the Lintian::Collect and Lintian::Collect::Package modules are also available.</p>
<dl COMPACT>
<dt>changelog</p>
<dd>Returns the changelog of the source package as a Parse::DebianChangelog object, or <tt>&quot;undef&quot;</tt> if the changelog cannot be resolved safely. </p>
<p> Needs-Info requirements for using <i>changelog</i>: Same as index_resolved_path</p>
<dt>diffstat</p>
<dd>Returns the path to diffstat output run on the Debian packaging diff (a.k.a. the &#8220;diff.gz&#8221;) for 1.0 non-native packages. For source packages without a &#8220;diff.gz&#8221; component, this returns the path to an empty file (this may be a device like /dev/null). </p>
<p> Needs-Info requirements for using <i>diffstat</i>: diffstat</p>
<dt>native</p>
<dd>Returns true if the source package is native and false otherwise. This is generally determined from the source format, though in the 1.0 case the nativeness is determined by looking for the diff.gz (using the name of the source package and its version). </p>
<p> If the source format is 1.0 and the version number is absent, this will return false (as native packages are a lot rarer than non-native ones). </p>
<p> Note if the source format is missing, it is assumed to be a 1.0 package. </p>
<p> Needs-Info requirements for using <i>native</i>: Same as field</p>
<dt>repacked</p>
<dd>Returns true if the source package has been &#8220;repacked&#8221; and false otherwise. This is determined from the version name containing &#8220;dfsg&#8221; or similar. </p>
<p> Needs-Info requirements for using <i>repacked</i>: Same as field</p>
<dt>binaries</p>
<dd>Returns a list of the binary and udeb packages listed in the <i>debian/control</i>. Package names appear the same order in the returned list as they do in the control file. </p>
<p> <i>Note</i>: Package names that are not valid are silently ignored. </p>
<p> Needs-Info requirements for using <i>binaries</i>: Same as binary_package_type</p>
<dt>binary_package_type (<font SIZE="-1">BINARY</font>)</p>
<dd>Returns package type based on value of the Package-Type (or if absent, X-Package-Type) field. If the field is omitted, the default value &#8220;deb&#8221; is used. </p>
<p> If the <font SIZE="-1">BINARY</font> is not a binary listed in the source packages <i>debian/control</i> file, this method return <tt>&quot;undef&quot;</tt>. </p>
<p> Needs-Info requirements for using <i>binary_package_type</i>: Same as binary_field</p>
<dt>source_field([FIELD[, <font SIZE="-1">DEFAULT</font>]])</p>
<dd>Returns the content of the field <font SIZE="-1">FIELD</font> from source package paragraph of the <i>debian/control</i> file, or <font SIZE="-1">DEFAULT</font> (defaulting to <tt>&quot;undef&quot;</tt>) if the field is not present. Only the literal value of the field is returned. </p>
<p> If <font SIZE="-1">FIELD</font> is not given, return a hashref mapping field names to their values (in this case <font SIZE="-1">DEFAULT</font> is ignored). This hashref should not be modified. </p>
<p> <font SIZE="-1">NB:</font> If a field from the &#8220;dsc&#8221; file itself is desired, please use field instead. </p>
<p> Needs-Info requirements for using <i>source_field</i>: Same as index_resolved_path</p>
<dt>orig_index (<font SIZE="-1">FILE</font>)</p>
<dd>Like &#8220;index&#8221; except orig_index is based on the &#8220;orig tarballs&#8221; of the source packages. </p>
<p> For native packages &#8220;index&#8221; and &#8220;orig_index&#8221; are generally identical. </p>
<p> <font SIZE="-1">NB:</font> If sorted_index includes a debian packaging, it is was contained in upstream part of the source package (or the package is native). </p>
<p> Needs-Info requirements for using <i>orig_index</i>: src-orig-index</p>
<dt>sorted_orig_index</p>
<dd>Like sorted_index except sorted_orig_index is based on the &#8220;orig tarballs&#8221; of the source packages. </p>
<p> For native packages sorted_index and &#8220;sorted_orig_index&#8221; are generally identical. </p>
<p> <font SIZE="-1">NB:</font> If sorted_orig_index includes a debian packaging, it is was contained in upstream part of the source package (or the package is native). </p>
<p> Needs-Info requirements for using <i>sorted_orig_index</i>: Same as orig_index</p>
<dt>orig_index_resolved_path(<font SIZE="-1">PATH</font>)</p>
<dd>Resolve <font SIZE="-1">PATH</font> (relative to the root of the package) and return the entry denoting the resolved path. </p>
<p> The resolution is done using resolve_path. </p>
<p> <font SIZE="-1">NB:</font> If orig_index_resolved_path includes a debian packaging, it is was contained in upstream part of the source package (or the package is native). </p>
<p> Needs-Info requirements for using <i>orig_index_resolved_path</i>: Same as orig_index</p>
<dt>binary_field (PACKAGE[, FIELD[, <font SIZE="-1">DEFAULT</font>]])</p>
<dd>Returns the content of the field <font SIZE="-1">FIELD</font> for the binary package <font SIZE="-1">PACKAGE</font> in the <i>debian/control</i> file, or <font SIZE="-1">DEFAULT</font> (defaulting to <tt>&quot;undef&quot;</tt>) if the field is not present. Inheritance of field values from the source section of the control file is not implemented. Only the literal value of the field is returned. </p>
<p> If <font SIZE="-1">FIELD</font> is not given, return a hashref mapping field names to their values (in this case, <font SIZE="-1">DEFAULT</font> is ignored). This hashref should not be modified. </p>
<p> If <font SIZE="-1">PACKAGE</font> is not a binary built from this source, this returns <font SIZE="-1">DEFAULT.</font> </p>
<p> Needs-Info requirements for using <i>binary_field</i>: Same as index_resolved_path</p>
<dt>java_info</p>
<dd>Returns a hashref containing information about <font SIZE="-1">JAR</font> files found in source packages, in the form <i>file name</i> -&gt; <i>info</i>, where <i>info</i> is a hash containing the following keys:</p>
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
<dt>binary_relation (<font SIZE="-1">PACKAGE, FIELD</font>)</p>
<dd>Returns a Lintian::Relation object for the specified <font SIZE="-1">FIELD</font> in the binary package <font SIZE="-1">PACKAGE</font> in the <i>debian/control</i> file. <font SIZE="-1">FIELD</font> should be one of the possible relationship fields of a Debian package or one of the following special values:</p>
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
<p> Any substvars in <i>debian/control</i> will be represented in the returned relation as packages named after the substvar. </p>
<p> Needs-Info requirements for using <i>binary_relation</i>: Same as binary_field</dl>
<dt>relation (<font SIZE="-1">FIELD</font>)</p>
<dd>Returns a Lintian::Relation object for the given build relationship field <font SIZE="-1">FIELD.</font> In addition to the normal build relationship fields, the following special field names are supported:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>build-depends-all</p>
<dd>The concatenation of Build-Depends, Build-Depends-Arch and Build-Depends-Indep.</p>
<dt>build-conflicts-all</p>
<dd>The concatenation of Build-Conflicts, Build-Conflicts-Arch and Build-Conflicts-Indep.</dl>
</dl>
<dl COMPACT>
<dd>If <font SIZE="-1">FIELD</font> isn&#8217;t present in the package, the returned Lintian::Relation object will be empty (always satisfied and implies nothing). </p>
<p> Needs-Info requirements for using <i>relation</i>: Same as field</dl>
<dt>relation_noarch (<font SIZE="-1">FIELD</font>)</p>
<dd>The same as &#8220;relation (<font SIZE="-1">FIELD</font>)&#8221;, but ignores architecture restrictions and build profile restrictions in the <font SIZE="-1">FIELD</font> field. </p>
<p> Needs-Info requirements for using <i>relation_noarch</i>: Same as relation</p>
<dt>debfiles ([<font SIZE="-1">FILE</font>])</p>
<dd><code>This method is deprecated</code>. Consider using index_resolved_path(<font SIZE="-1">PATH</font>) instead, which returns Lintian::Path objects. </p>
<p> Returns the path to <font SIZE="-1">FILE</font> in the debian dir of the extracted source package. <font SIZE="-1">FILE</font> must be relative to the root of the debian dir and should be without leading slash (and without &#8220;./&#8221;). If <font SIZE="-1">FILE</font> is not in the debian dir, it returns the path to a non-existent file entry. </p>
<p> It is not permitted for <font SIZE="-1">FILE</font> to be <tt>&quot;undef&quot;</tt>. If the &#8220;root&#8221; dir is desired either invoke this method without any arguments at all or use the empty string. </p>
<p> The caveats of unpacked also apply to this method. </p>
<p> Needs-Info requirements for using <i>debfiles</i>: debfiles</p>
<dt>index (<font SIZE="-1">FILE</font>)</p>
<dd>For the general documentation of this method, please refer to the documentation of it in Lintian::Collect::Package. </p>
<p> The index of a source package is not very well defined for non-native source packages. This method gives the index of the &#8220;unpacked&#8221; package (with 3.0 (quilt), this implies patches have been applied). </p>
<p> If you want the index of what is listed in the upstream orig tarballs, then there is &#8220;orig_index&#8221;. </p>
<p> For native packages, the two indices are generally the same as they only have one tarball and their debian packaging is included in that tarball. </p>
<p> <font SIZE="-1">IMPLEMENTATION DETAIL/CAVEAT:</font> Lintian currently (2.5.11) generates this by running &#8220;<i><a href="/docs/linux/man/1-find/">find</a></i>(1)&#8221; after unpacking the source package. This has three consequences. </p>
<p> First it means that (original) owner/group data is lost; Lintian inserts &#8220;root/root&#8221; here. This is usually not a problem as owner/group information for source packages do not really follow any standards. </p>
<p> Secondly, permissions are modified by A) umask and B) laboratory set{g,u}id bits (the laboratory on lintian.d.o has setgid). This is *not* corrected/altered. Note Lintian (usually) breaks if any of the &#8220;user&#8221; bits are set in the umask, so that part of the permission bit <i>should</i> be reliable. </p>
<p> Again, this shouldn&#8217;t be a problem as permissions in source packages are usually not important. Though if accuracy is needed here, &#8220;orig_index&#8221; may used instead (assuming it has the file in question). </p>
<p> Third, hardlinking information is lost and no attempt has been made to restore it. </p>
<p> Needs-Info requirements for using <i>index</i>: unpacked</p>
<dt>is_non_free</p>
<dd>Returns a truth value if the package appears to be non-free (based on the section field; &#8220;non-free/*&#8221; and &#8220;restricted/*&#8221;) </p>
<p> Needs-Info requirements for using <i>is_non_free</i>: &#8220;source_field ([FIELD[, <font SIZE="-1">DEFAULT</font>]])&#8221;</dl>
<h2>Author</h2>
<p>Originally written by Russ Allbery &lt;rra [at] debian.org&gt; for Lintian.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-lintian/">lintian</a></i>(1), <i><a href="/docs/linux/man/3-lintian--collect/">Lintian::Collect</a></i>(3), <i><a href="/docs/linux/man/3-lintian--relation/">Lintian::Relation</a></i>(3)</p>
