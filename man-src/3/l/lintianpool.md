---
title: "lintianpool(3)"
name: "lintianpool"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianpool/"
description: "Lintian::Pool — Pool of processables"
---

<p>Lintian::Pool &#8212; Pool of processables </p>
<h2>Synopsis</h2>
<pre> use Lintian::Pool;
 
 my $pool = Lintian::Pool-&gt;new;
 $pool-&gt;add_file('foo.changes');
 $pool-&gt;add_file('bar.dsc');
 $pool-&gt;add_file('baz.deb');
 $pool-&gt;add_file('qux.buildinfo');
 foreach my $gname ($pool-&gt;get_group_names){
 my $group = $pool-&gt;get_group($gname);
 process($gname, $group);
 }</pre>
<h2>Methods</h2>
<dl COMPACT>
<dt>$pool-&gt;groups</p>
<dd>Returns a hash reference to the list of processable groups that are currently in the pool. The key is a unique identifier based on name and version.</p>
<dt>&quot;savedir&quot;</p>
<dd>
<dt>$pool-&gt;basedir</p>
<dd>Returns the base directory for the pool. Most likely it&#8217;s a temporary directory.</p>
<dt>$pool-&gt;keep</p>
<dd>Returns or accepts a boolean value that indicates whether the lab should be removed when Lintian finishes. Used for debugging.</p>
<dt>$pool-&gt;add_group($group)</p>
<dd>Adds a group to the pool.</p>
<dt>$pool-&gt;process</p>
<dd>Process the pool.</p>
<dt>$pool-&gt;get_group_names</p>
<dd>Returns the name of all the groups in this pool. </p>
<p> Do not modify the list nor its contents.</p>
<dt>$pool-&gt;get_group($name)</p>
<dd>Returns the group called <tt>$name</tt> or <tt>&quot;undef&quot;</tt> if there is no group called <tt>$name</tt>.</p>
<dt>$pool-&gt;empty</p>
<dd>Returns true if the pool is empty.</p>
<dt><font SIZE="-1">DEMOLISH</font></p>
<dd>Removes the lab and everything in it. Any reference to an entry returned from this lab will immediately become invalid.</dl>
<h2>Author</h2>
<p>Originally written by Niels Thykier &lt;niels [at] thykier.net&gt; for Lintian.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1) </p>
<p> Lintian::Processable </p>
<p> Lintian::Group</p>
