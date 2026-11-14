---
title: "lintiancollectgroup(3)"
name: "lintiancollectgroup"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintiancollectgroup/"
---

Lintian::Collect::Group - Lintian interface to group data collection 

<h2>Synopsis</h2><pre> my $group = Lintian::ProcessableGroup-&gt;new ('lintian_2.5.0_i386.changes');
 my $ginfo = Lintian::Collect::Group-&gt;new ($group);
 
 foreach my $bin ($group-&gt;get_binary_processables) {
 my $pkg_name = $bin-&gt;pkg_name;
 foreach my $dirdep ($ginfo-&gt;direct_dependencies ($bin)) {
 print &quot;$pkg_name (pre-)depends on $dirdep (which is also in this group)\n&quot;;
 }
 }</pre><h2>Description</h2>Lintian::Collect::Group is a ``group'' variant of the Lintian::Collect modules. It attempts to expose a similar interface as these and provide useful information about the processable group (or members of it).
<h2>Class Methods</h2><dl COMPACT><dt>Lintian::Collect::Group-&gt;new ($group)
<dd>Creates a new object to provide information about <tt>$group</tt>.
<dt>direct_dependencies (<font SIZE="-1">PROC</font>)
<dd>If <font SIZE="-1">PROC</font> is a part of the underlying processable group, this method returns a listref containing all the direct dependencies of <font SIZE="-1">PROC.</font> If <font SIZE="-1">PROC</font> is not a part of the group, this returns undef. 

 Note: Only strong dependencies (Pre-Depends and Depends) are considered. 

 Note: Self-dependencies (if any) are <i>not</i> included in the result.
<dt>$ginfo-&gt;type
<dd>Return the type of this collect object (which is the string 'group').
<dt>spelling_exceptions
<dd>Returns a hashref of words, which the spell checker should ignore. These words are generally based on the package names in the group to avoid false-positive ``spelling error'' when packages have ``fun'' names. 

 Example: Package alot-doc (#687464)</dl><h2>Author</h2>Originally written by Niels Thykier &lt;niels [at] thykier.net&gt; for Lintian.
<h2>See Also</h2><i><a HREF="/docs/linux/man/1-lintian/">lintian</a></i>(1), <i><a HREF="/docs/linux/man/3-lintian--collect--binary/">Lintian::Collect::Binary</a></i>(3), <i><a HREF="/docs/linux/man/3-lintian--collect--changes/">Lintian::Collect::Changes</a></i>(3), <i><a HREF="/docs/linux/man/3-lintian--collect--source/">Lintian::Collect::Source</a></i>(3)
