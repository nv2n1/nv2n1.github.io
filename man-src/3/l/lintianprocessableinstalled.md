---
title: "lintianprocessableinstalled(3)"
name: "lintianprocessableinstalled"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianprocessableinstalled/"
description: "Lintian::Processable::Installed – access to collected data about the upstream (orig) sources"
---

<p>Lintian::Processable::Installed &#8211; access to collected data about the upstream (orig) sources </p>
<h2>Synopsis</h2>
<pre>
    use Lintian::Processable;
    my $processable = Lintian::Processable::Binary-&gt;new;
</pre>
<h2>Description</h2>
<p> Lintian::Processable::Installed provides an interface to collected data about the upstream (orig) sources.</p>
<h2>Instance Methods</h2>
<dl COMPACT>
<dt>installed</p>
<dd> Returns a index object representing installed files from a binary package.</p>
<dt>index (<font SIZE="-1">FILE</font>)</p>
<dd> Returns a path object to <font SIZE="-1">FILE</font> in the package. <font SIZE="-1">FILE</font> must be relative to the root of the unpacked package and must be without leading slash (or &#8220;./&#8221;). If <font SIZE="-1">FILE</font> is not in the package, it returns <tt>&quot;undef&quot;</tt>. If <font SIZE="-1">FILE</font> is supposed to be a directory, it must be given with a trailing slash. Example: </p>
<pre>
  my $file = $info-&gt;index (&quot;usr/bin/lintian&quot;);
  my $dir = $info-&gt;index (&quot;usr/bin/&quot;);
</pre>
<p> To get a list of entries in the package, see &#8220;sorted_index&#8221;. To actually access the underlying file (e.g. the contents), use &#8220;unpacked ([<font SIZE="-1">FILE</font>])&#8221;. </p>
<p> Note that the &#8220;root directory&#8221; (denoted by the empty string) will always be present, even if the underlying tarball omits it. </p>
<p> Needs-Info requirements for using <i>index</i>: unpacked</p>
<dt>sorted_index</p>
<dd> Returns a sorted array of file names listed in the package. The names will not have a leading slash (or &#8220;./&#8221;) and can be passed to &#8220;unpacked ([<font SIZE="-1">FILE</font>])&#8221; or &#8220;index (<font SIZE="-1">FILE</font>)&#8221; as is. </p>
<p> The array will not contain the entry for the &#8220;root&#8221; of the package.</p>
<dt>index_resolved_path(<font SIZE="-1">PATH</font>)</p>
<dd> Resolve <font SIZE="-1">PATH</font> (relative to the root of the package) and return the entry denoting the resolved path. </p>
<p> The resolution is done using resolve_path.</dl>
<h2>Author</h2>
<p> Originally written by Felix Lechner &lt;felix.lechner [at] lease-up.com&gt; for Lintian.</p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1)</p>
