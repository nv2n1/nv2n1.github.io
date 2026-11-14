---
title: "lintiancheckscript(3)"
name: "lintiancheckscript"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintiancheckscript/"
---

Lintian::CheckScript - Check script meta data 

<h2>Synopsis</h2><pre> use Lintian::CheckScript;
 
 my $cs = Lintian::CheckScript-&gt;new (&quot;$ENV{'LINTIAN_ROOT'}/checks/&quot;,
 'files');
 my $name = $cs-&gt;name;
 foreach my $tag ($cs-&gt;tags) {
 # $ti is an instance of Lintian::Tag::Info
 my $ti = $cs-&gt;get_tag ($tag);
 print &quot;$tag is a part of the check $name\n&quot;;
 # Do something with $ti / $tag
 }
 foreach my $needs ($cs-&gt;needs_info) {
 print &quot;$name needs $needs\n&quot;;
 }
 if ($cs-&gt;is_check_type ('binary') &amp;&amp; $cs-&gt;is_check_type ('source')) {
 # Check applies to binary pkgs AND source pkgs
 }</pre><h2>Description</h2>Instances of this class represents the data in the check ``.desc'' files. It allows access to the tags (as Lintian::Tag::Info) and the common meta data of the check (such as Needs-Info).
<h2>Class Methods</h2><dl COMPACT><dt>Lintian::CheckScript-&gt;new($basedir, $checkname)
<dd>Parses the <tt>$file</tt> as a check desc file.
<dt>$cs-&gt;name
<dd>Returns the ``name'' of the check script. This is the value in the Check-Script field in the file.
<dt>$cs-&gt;type
<dd>Returns the value stored in the ``Type'' field of the file. For the purpose of testing if the check applies to a given package type, the ``is_check_type'' method can be used instead. 

 Note in rare cases this may return undef. This is the case for the lintian.desc, where this field is simply not present.
<dt>$cs-&gt;abbrev
<dd>Returns the value of the Abbrev field from the desc file.
<dt>$cs-&gt;script_path
<dd>Returns the (expected) path to the script implementing this check.
<dt>needs_info
<dd>Returns a list of all items listed in the Needs-Info field. Neither the list nor its contents should be modified.
<dt>$cs-&gt;is_check_type ($type)
<dd>Returns a truth value if this check can be applied to a <tt>$type</tt> package. 

 Note if <tt>$cs</tt>-&gt;type return undef, this will return a truth value for all inputs.
<dt>$cs-&gt;get_tag ($tagname)
<dd>Return the tag or undef (if the tag is not in this check).
<dt>$cs-&gt;tags
<dd>Returns the list of tag names in the check. The list nor its contents should be modified.
<dt>$cs-&gt;load_check
<dd>Attempts to load the check. On failure, the load error will be propagated to the caller. On success it returns normally.
<dt>$cs-&gt;run_check ($proc, $group)
<dd>Run the check on <tt>$proc</tt>, which is in the group <tt>$group</tt>. <tt>$proc</tt> should be a lab entry and must have the proper collections run on it prior to calling this method (See Lintian::Unpacker). 

 The method may error out if loading the check failed or if the check itself calls die/croak/fail/etc. 

 Returns normally on success; the return value has no semantic meaning and is currently <tt>&quot;undef&quot;</tt>. 

 <font SIZE="-1">NB:</font> load_check can be used to determine if the check itself is loadable.</dl><h2>Author</h2>Originally written by Niels Thykier &lt;niels [at] thykier.net&gt; for Lintian.
<h2>See Also</h2><i><a HREF="/docs/linux/man/1-lintian/">lintian</a></i>(1), <i><a HREF="/docs/linux/man/3-lintian--profile/">Lintian::Profile</a></i>(3), <i><a HREF="/docs/linux/man/3-lintian--tag--info/">Lintian::Tag::Info</a></i>(3)
