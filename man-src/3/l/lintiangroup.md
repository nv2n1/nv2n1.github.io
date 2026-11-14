---
title: "lintiangroup(3)"
name: "lintiangroup"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintiangroup/"
description: "Lintian::Group — A group of objects that Lintian can process"
---

<p>Lintian::Group &#8212; A group of objects that Lintian can process </p>
<h2>Synopsis</h2>
<pre> use Lintian::Group;
 my $group = Lintian::Group-&gt;new('lintian_2.5.0_i386.changes');</pre>
<h2>Description</h2>
<p>Instances of this perl class are sets of processables. It allows at most one source and one changes or buildinfo package per set, but multiple binary packages (provided that the binary is not already in the set).</p>
<h2>Methods</h2>
<dl COMPACT>
<dt>$group-&gt;pooldir</p>
<dd>Returns or sets the pool directory used by this group.</p>
<dt>$group-&gt;name</p>
<dd>Returns a unique identifier for the group based on source and version.</p>
<dt>$group-&gt;binary</p>
<dd>Returns a hash reference to the binary processables in this group.</p>
<dt>$group-&gt;buildinfo</p>
<dd>Returns the buildinfo processable in this group.</p>
<dt>$group-&gt;changes</p>
<dd>Returns the changes processable in this group.</p>
<dt>$group-&gt;source</p>
<dd>Returns the source processable in this group.</p>
<dt>$group-&gt;udeb</p>
<dd>Returns a hash reference to the udeb processables in this group.</p>
<dt>jobs</p>
<dd>Returns or sets the max number of jobs to be processed in parallel. </p>
<p> If the limit is 0, then there is no limit for the number of parallel jobs.</p>
<dt>cache</p>
<dd>Cache for some items.</p>
<dt>profile</p>
<dd>Hash with active jobs.</p>
<dt>&quot;saved_direct_dependencies&quot;</p>
<dd>
<dt>&quot;saved_direct_reliants&quot;</p>
<dd>
<dt>&quot;saved_spelling_exceptions&quot;</p>
<dd>
<dt>&quot;shared_storage&quot;</p>
<dd>
<dt>Lintian::Group-&gt;init_from_file (<font SIZE="-1">FILE</font>)</p>
<dd>Add all processables from .changes or .buildinfo file <font SIZE="-1">FILE.</font></p>
<dt>unpack</p>
<dd>Unpack this group.</p>
<dt>process</p>
<dd>Process group.</p>
<dt>clean_lab</p>
<dd>Removes the lab files to conserve disk space. Global destruction will also get these unless we are keeping the lab.</p>
<dt>$group-&gt;add_processable($proc)</p>
<dd>Adds <tt>$proc</tt> to <tt>$group</tt>. At most one source and one changes <tt>$proc</tt> can be in a <tt>$group</tt>. There can be multiple binary <tt>$proc</tt>&#8216;s, as long as they are all unique. Successive buildinfo <tt>$proc</tt>&#8216;s are silently ignored. </p>
<p> This will error out if an additional source or changes <tt>$proc</tt> is added to the group. Otherwise it will return a truth value if <tt>$proc</tt> was added.</p>
<dt>$group-&gt;get_processables([$type])</p>
<dd>Returns an array of all processables in <tt>$group</tt>. The processables are returned in the following order: changes (if any), source (if any), all binaries (if any) and all udebs (if any). </p>
<p> This order is based on the original order that Lintian processed packages in and some parts of the code relies on this order. </p>
<p> Note if <tt>$type</tt> is given, then only processables of that type is returned.</p>
<dt>$group-&gt;get_binary_processables</p>
<dd>Returns all binary (and udeb) processables in <tt>$group</tt>. </p>
<p> If <tt>$group</tt> does not have any binary processables then an empty list is returned.</p>
<dt>$group-&gt;info</p>
<dd>
<dt>direct_dependencies (<font SIZE="-1">PROC</font>)</p>
<dd>If <font SIZE="-1">PROC</font> is a part of the underlying processable group, this method returns a listref containing all the direct dependencies of <font SIZE="-1">PROC.</font> If <font SIZE="-1">PROC</font> is not a part of the group, this returns undef. </p>
<p> Note: Only strong dependencies (Pre-Depends and Depends) are considered. </p>
<p> Note: Self-dependencies (if any) are <i>not</i> included in the result.</p>
<dt>direct_reliants (<font SIZE="-1">PROC</font>)</p>
<dd>If <font SIZE="-1">PROC</font> is a part of the underlying processable group, this method returns a listref containing all the packages in the group that rely on <font SIZE="-1">PROC.</font> If <font SIZE="-1">PROC</font> is not a part of the group, this returns undef. </p>
<p> Note: Only strong dependencies (Pre-Depends and Depends) are considered. </p>
<p> Note: Self-dependencies (if any) are <i>not</i> included in the result.</p>
<dt>$ginfo-&gt;type</p>
<dd>Return the type of this collect object (which is the string &#8216;group&#8217;).</p>
<dt>spelling_exceptions</p>
<dd>Returns a hashref of words, which the spell checker should ignore. These words are generally based on the package names in the group to avoid false-positive &#8220;spelling error&#8221; when packages have &#8220;fun&#8221; names. </p>
<p> Example: Package alot-doc (#687464)</p>
<dt>$group-&gt;clear_cache</p>
<dd>Discard the info element of all members of this group, so the memory used by it can be reclaimed. Mostly useful when checking a lot of packages (e.g. on lintian.d.o).</dl>
<h2>Author</h2>
<p>Originally written by Niels Thykier &lt;niels [at] thykier.net&gt; for Lintian.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1) </p>
<p> Lintian::Processable</p>
