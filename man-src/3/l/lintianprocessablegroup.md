---
title: "lintianprocessablegroup(3)"
name: "lintianprocessablegroup"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianprocessablegroup/"
---

Lintian::ProcessableGroup -- A group of objects that Lintian can process 

<h2>Synopsis</h2><pre> use Lintian::ProcessableGroup;
 my $group = Lintian::ProcessableGroup-&gt;new('lintian_2.5.0_i386.changes');
 foreach my $proc ($group-&gt;get_processables){
 printf &quot;%s %s (%s)\n&quot;, $proc-&gt;pkg_name,
 $proc-&gt;pkg_version, $proc-&gt;pkg_type;
 }
 # etc.</pre><h2>Description</h2>Instances of this perl class are sets of processables. It allows at most one source and one changes or buildinfo package per set, but multiple binary packages (provided that the binary is not already in the set).
<h2>Methods</h2><dl COMPACT><dt>Lintian::ProcessableGroup-&gt;new ([LAB[, <font SIZE="-1">FILE</font>]])
<dd>Creates a group and optionally add all processables from .changes or .buildinfo file <font SIZE="-1">FILE.</font> 

 If the <font SIZE="-1">LAB</font> parameter is given, all processables added to this group will be stored as a lab entry from <font SIZE="-1">LAB.</font>
<dt>$group-&gt;add_new_processable ($pkg_path[, $pkg_type])
<dd>Adds a new processable of type <tt>$pkg_type</tt> from <tt>$pkg_path</tt>. If <tt>$pkg_type</tt> is not given, it will be determined by the file extension. 

 This is short hand for: 

 <pre> $group-&gt;add_processable(
 Lintian::Processable-&gt;new ($pkg_path, $pkg_type));</pre><dt>$group-&gt;add_processable($proc)
<dd>Adds <tt>$proc</tt> to <tt>$group</tt>. At most one source and one changes <tt>$proc</tt> can be in a <tt>$group</tt>. There can be multiple binary <tt>$proc</tt>'s, as long as they are all unique. 

 This will error out if an additional source or changes <tt>$proc</tt> is added to the group. Otherwise it will return a truth value if <tt>$proc</tt> was added.
<dt>$group-&gt;get_processables([$type])
<dd>Returns an array of all processables in <tt>$group</tt>. The processables are returned in the following order: changes (if any), source (if any), all binaries (if any) and all udebs (if any). 

 This order is based on the original order that Lintian processed packages in and some parts of the code relies on this order. 

 Note if <tt>$type</tt> is given, then only processables of that type is returned.
<dt>$group-&gt;remove_processable($proc)
<dd>Removes <tt>$proc</tt> from <tt>$group</tt>
<dt>$group-&gt;get_source_processable
<dd>Returns the processable identified as the ``source'' package (e.g. the dsc). 

 If <tt>$group</tt> does not have a source processable, this method returns <tt>&quot;undef&quot;</tt>.
<dt>$group-&gt;get_buildinfo_processable
<dd>Returns the processable identified as the ``buildinfo'' processable (e.g. the buildinfo file). 

 If <tt>$group</tt> does not have a buildinfo processable, this method returns <tt>&quot;undef&quot;</tt>.
<dt>$group-&gt;get_changes_processable
<dd>Returns the processable identified as the ``changes'' processable (e.g. the changes file). 

 If <tt>$group</tt> does not have a changes processable, this method returns <tt>&quot;undef&quot;</tt>.
<dt>$group-&gt;get_binary_processables
<dd>Returns all binary (and udeb) processables in <tt>$group</tt>. 

 If <tt>$group</tt> does not have any binary processables then an empty list is returned.
<dt>$group-&gt;info
<dd>Returns <tt>$info</tt> element for this group.
<dt>$group-&gt;init_shared_cache
<dd>Prepare a shared memory cache for all current members of the group. This is solely a memory saving optimization and is not required for correct performance.
<dt>$group-&gt;clear_cache
<dd>Discard the info element of all members of this group, so the memory used by it can be reclaimed. Mostly useful when checking a lot of packages (e.g. on lintian.d.o).</dl><h2>Author</h2>Originally written by Niels Thykier &lt;niels [at] thykier.net&gt; for Lintian.
<h2>See Also</h2><i><a HREF="/docs/linux/man/1-lintian/">lintian</a></i>(1) 

 Lintian::Processable
