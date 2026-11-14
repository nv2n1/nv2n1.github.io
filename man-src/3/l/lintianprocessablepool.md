---
title: "lintianprocessablepool(3)"
name: "lintianprocessablepool"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianprocessablepool/"
---

Lintian::ProcessablePool -- Pool of processables 

<h2>Synopsis</h2><pre> use Lintian::ProcessablePool;
 
 my $pool = Lintian::ProcessablePool-&gt;new;
 $pool-&gt;add_file('foo.changes');
 $pool-&gt;add_file('bar.dsc');
 $pool-&gt;add_file('baz.deb');
 $pool-&gt;add_file('qux.buildinfo');
 foreach my $gname ($pool-&gt;get_group_names){
 my $group = $pool-&gt;get_group($gname);
 process($gname, $group);
 }</pre><h2>Methods</h2><dl COMPACT><dt>Lintian::ProcessablePool-&gt;new ([<font SIZE="-1">LAB</font>])
<dd>Creates a new empty pool. 

 If <font SIZE="-1">LAB</font> is given, it is assumed to be a Lintian::Lab. In this case, any processable added to this pool will be stored as a lab entry from <font SIZE="-1">LAB.</font>
<dt>$pool-&gt;add_file($file)
<dd>Adds a file to the pool. The <tt>$file</tt> will be turned into a processable and grouped together with other processables from the same source package (if any).
<dt>$pool-&gt;add_proc ($proc)
<dd>Adds a processable to the pool.
<dt>$pool-&gt;get_group_names
<dd>Returns the name of all the groups in this pool. 

 Do not modify the list nor its contents.
<dt>$pool-&gt;get_group($name)
<dd>Returns the group called <tt>$name</tt> or <tt>&quot;undef&quot;</tt> if there is no group called <tt>$name</tt>.
<dt>$pool-&gt;get_groups
<dd>Returns all the groups in the pool. 

 Do not modify the list nor its contents.
<dt>$pool-&gt;empty
<dd>Returns true if the pool is empty.</dl><h2>Author</h2>Originally written by Niels Thykier &lt;niels [at] thykier.net&gt; for Lintian.
<h2>See Also</h2><i><a HREF="/docs/linux/man/1-lintian/">lintian</a></i>(1) 

 Lintian::Processable 

 Lintian::ProcessableGroup
