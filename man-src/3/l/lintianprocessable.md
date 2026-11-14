---
title: "lintianprocessable(3)"
name: "lintianprocessable"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianprocessable/"
description: "Lintian::Processable — An (abstract) object that Lintian can process"
---

<p>Lintian::Processable &#8212; An (abstract) object that Lintian can process </p>
<h2>Synopsis</h2>
<pre> use Lintian::Processable;
 
 # Instantiate via Lintian::Processable
 my $proc = Lintian::Processable-&gt;new;
 $proc-&gt;init_from_file('lintian_2.5.0_all.deb');
 my $package = $proc-&gt;pkg_name;
 my $version = $proc-&gt;pkg_version;
 # etc.</pre>
<h2>Description</h2>
<p>Instances of this perl class are objects that Lintian can process (e.g. deb files). Multiple objects can then be combined into groups, which Lintian will process together.</p>
<h2>Instance Methods</h2>
<dl COMPACT>
<dt>name =item $proc-&gt;pkg_name</p>
<dd>Returns the name of the package.</p>
<dt>type =item $proc-&gt;pkg_type</p>
<dd>Returns the type of package (e.g. binary, source, udeb &#8230;)</p>
<dt>verbatim =item extra_fields</p>
<dd>Returns a hash to the raw, unedited and verbatim field values.</p>
<dt>unfolded</p>
<dd>Returns a hash to unfolded field values. Continuations lines have been connected.</p>
<dt>shared_storage</p>
<dd>Returns shared_storage.</p>
<dt>$proc-&gt;version =item $proc-&gt;pkg_version</p>
<dd>Returns the version of the package.</p>
<dt>$proc-&gt;path =item $proc-&gt;pkg_path</p>
<dd>Returns the path to the packaged version of actual package. This path is used in case the data needs to be extracted from the package. </p>
<p> Note: This may return the path to a symlink to the package.</p>
<dt>$proc-&gt;architecture =item $proc-&gt;pkg_arch</p>
<dd>Returns the architecture(s) of the package. May return multiple values from changes processables. For source processables it is &#8220;source&#8221;.</p>
<dt>$proc-&gt;source =item $proc-&gt;pkg_src</p>
<dd>Returns the name of the source package.</p>
<dt>$proc-&gt;source_version =item $proc-&gt;pkg_src_version</p>
<dd>Returns the version of the source package.</p>
<dt>$proc-&gt;tainted</p>
<dd>Returns a truth value if one or more fields in this Processable is tainted. On a best effort basis tainted fields will be sanitized to less dangerous (but possibly invalid) values.</p>
<dt>$proc-&gt;pooldir</p>
<dd>Returns a reference to lab this Processable is in.</p>
<dt>$proc-&gt;groupdir</p>
<dd>Returns the base directory of this package inside the lab.</p>
<dt>link_label</p>
<dd>Returns a reference to the extra fields related to this entry.</p>
<dt>saved_link</p>
<dd>Returns a reference to the extra fields related to this entry.</p>
<dt>&quot;identifier&quot;</p>
<dd>Produces an identifier for this processable. The identifier is based on the type, name, version and architecture of the package.</p>
<dt>info</p>
<dd>
<dt>clear_cache</p>
<dd>Overrides clear_cache from Lintian::Processable.</p>
<dt>remove</p>
<dd>Removes all unpacked parts of the package in the lab. Returns a truth value if successful.</p>
<dt>get_group_id</p>
<dd>Calculates an appropriate group id for the package. It is based on the name and the version of the src-pkg.</p>
<dt>clean_field</p>
<dd>Cleans a field of evil characters to prevent traversal or worse.</p>
<dt>link</p>
<dd>Returns the link in the work area to the input data.</p>
<dt>create</p>
<dd>Creates a link to the input file near where all files in that group will be unpacked and analyzed.</p>
<dt>guess_name</p>
<dd>Creates a link to the input file near where all files in that group will be unpacked and analyzed.</p>
<dt>unfolded_field (<font SIZE="-1">FIELD</font>)</p>
<dd>This method returns the unfolded value of the control field <font SIZE="-1">FIELD</font> in the control file for the package. For a source package, this is the *.dsc file; for a binary package, this is the control file in the control section of the package. </p>
<p> If <font SIZE="-1">FIELD</font> is passed but not present, then this method returns undef. </p>
<p> Needs-Info requirements for using <i>unfolded_field</i>: none</p>
<dt>field ([FIELD[, <font SIZE="-1">DEFAULT</font>]])</p>
<dd>If <font SIZE="-1">FIELD</font> is given, this method returns the value of the control field <font SIZE="-1">FIELD</font> in the control file for the package. For a source package, this is the *.dsc file; for a binary package, this is the control file in the control section of the package. </p>
<p> If <font SIZE="-1">FIELD</font> is passed but not present, then this method will return <font SIZE="-1">DEFAULT</font> (if given) or undef. </p>
<p> Otherwise this will return a hash of fields, where the key is the field name (in all lowercase). </p>
<p> Needs-Info requirements for using <i>field</i>: none</dl>
<h2>Author</h2>
<p>Originally written by Niels Thykier &lt;niels [at] thykier.net&gt; for Lintian. Substantial portions written by Russ Allbery &lt;rra [at] debian.org&gt; for Lintian.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1) </p>
<p> Lintian::Processable::Binary </p>
<p> Lintian::Processable::Buildinfo </p>
<p> Lintian::Processable::Changes, </p>
<p> Lintian::Processable::Source </p>
<p> Lintian::Processable::Udeb </p>
<p> Lintian::Group</p>
