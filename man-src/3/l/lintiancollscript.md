---
title: "lintiancollscript(3)"
name: "lintiancollscript"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintiancollscript/"
---

Lintian::CollScript - Collection script handle 

<h2>Synopsis</h2><pre> use Lintian::CollScript;
 my $cs = Lintian::CollScript-&gt;new (&quot;$ENV{'LINTIAN_ROOT'}/collection/index.desc&quot;);
 my $name = $cs-&gt;name;
 foreach my $needs ($cs-&gt;needs_info) {
 print &quot;$name needs $needs\n&quot;;
 }</pre><h2>Description</h2>Instances of this class represents the data in the collection ``.desc'' files. It allows access to the common meta data of the collection (such as Needs-Info).
<h2>Class Methods</h2><dl COMPACT><dt>new (<font SIZE="-1">FILE</font>)
<dd>Parse <font SIZE="-1">FILE</font> as a collection desc file.</dl><h2>Instance Methods</h2><dl COMPACT><dt>name
<dd>Returns the ``name'' of the collection script. This is the value in the Collector-Script field in the file.
<dt>type
<dd>Returns the value stored in the ``Type'' field of the file. For the purpose of testing if the collection applies to a given package type, the ``is_type'' method can be used instead.
<dt>version
<dd>Returns the value of the ``Version'' field of the file. This should be an integer describing the version of the collector script.
<dt>auto_remove
<dd>Returns a truth value if the collection has the ``auto-remove'' flag.
<dt>script_path
<dd>Returns the absolute path to the collection script.
<dt>interface
<dd>The call interface for this collection script.
<dl COMPACT><dd><dl COMPACT><dt>exec
<dd>The collection is run by invoking the script denoted by script_path with the proper arguments. 

 This is the default value.
<dt>perl-coll
<dd>The collection is implemented in Perl in such a way that it can be loaded into perl and run via the ``collect (<font SIZE="-1">PKG, TASK, DIR</font>)'' method. 

 Collections that have the ``perl-coll'' can also be run as if they had the ``exec'' interface (see above).</dl></dl><dl COMPACT><dd></dl><dt>needs_info ([<font SIZE="-1">COND</font>])
<dd>Returns a list of all items listed in the Needs-Info field. Neither the list nor its contents should be modified. 

 <font SIZE="-1">COND</font> is optional and used to determine what conditions are true. If omitted, all ``extra'' dependencies are returned. Otherwise, only the dependencies required by <font SIZE="-1">COND</font> are included. <font SIZE="-1">COND</font> is a hashref and with the following key/values:
<dl COMPACT><dd><dl COMPACT><dt>type
<dd>The value is a package type that determines which package type is being unpacked. This is used to determine if the condition for ``&lt;dep&gt; [&lt;type&gt;]'' relations are true or not.</dl></dl><dl COMPACT><dd></dl><dt>is_type (<font SIZE="-1">TYPE</font>)
<dd>Returns a truth value if this collection can be applied to a <font SIZE="-1">TYPE</font> package.
<dt>collect (<font SIZE="-1">PKG, TASK, DIR</font>)
<dd></dl><h2>Author</h2>Originally written by Niels Thykier &lt;niels [at] thykier.net&gt; for Lintian.
<h2>See Also</h2><i><a HREF="/docs/linux/man/1-lintian/">lintian</a></i>(1), <i><a HREF="/docs/linux/man/3-lintian--profile/">Lintian::Profile</a></i>(3), <i><a HREF="/docs/linux/man/3-lintian--tag--info/">Lintian::Tag::Info</a></i>(3)
