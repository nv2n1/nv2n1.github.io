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
<h2>Class Methods</h2><dl COMPACT><dt>new (FILE)
</dt><dd>Parse FILE as a collection desc file.</dd></dl><h2>Instance Methods</h2><dl COMPACT><dt>name
</dt><dd>Returns the ``name'' of the collection script. This is the value in the Collector-Script field in the file.
</dd><dt>type
</dt><dd>Returns the value stored in the ``Type'' field of the file. For the purpose of testing if the collection applies to a given package type, the ``is_type'' method can be used instead.
</dd><dt>version
</dt><dd>Returns the value of the ``Version'' field of the file. This should be an integer describing the version of the collector script.
</dd><dt>auto_remove
</dt><dd>Returns a truth value if the collection has the ``auto-remove'' flag.
</dd><dt>script_path
</dt><dd>Returns the absolute path to the collection script.
</dd><dt>interface
</dt><dd>The call interface for this collection script.
</dd><dl COMPACT><dd></dd><dl COMPACT><dt>exec
</dt><dd>The collection is run by invoking the script denoted by script_path with the proper arguments. 
 This is the default value.
</dd><dt>perl-coll
</dt><dd>The collection is implemented in Perl in such a way that it can be loaded into perl and run via the ``collect (PKG, TASK, DIR)'' method. 
 Collections that have the ``perl-coll'' can also be run as if they had the ``exec'' interface (see above).</dd></dl></dl><dl COMPACT><dd></dd></dl><dt>needs_info ([COND])
</dt><dd>Returns a list of all items listed in the Needs-Info field. Neither the list nor its contents should be modified. 

 COND is optional and used to determine what conditions are true. If omitted, all ``extra'' dependencies are returned. Otherwise, only the dependencies required by COND are included. COND is a hashref and with the following key/values:
</dd><dl COMPACT><dd></dd><dl COMPACT><dt>type
</dt><dd>The value is a package type that determines which package type is being unpacked. This is used to determine if the condition for ``&lt;dep&gt; [&lt;type&gt;]'' relations are true or not.</dd></dl></dl><dl COMPACT><dd></dd></dl><dt>is_type (TYPE)
</dt><dd>Returns a truth value if this collection can be applied to a TYPE package.
</dd><dt>collect (PKG, TASK, DIR)
</dt><dd></dd></dl><h2>Author</h2>Originally written by Niels Thykier &lt;niels [at] thykier.net&gt; for Lintian.
<h2>See Also</h2><i><a HREF="/docs/linux/man/1-lintian/">lintian</a></i>(1), <i>Lintian::Profile</i>(3), <i>Lintian::Tag::Info</i>(3)
