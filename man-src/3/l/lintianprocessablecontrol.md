---
title: "lintianprocessablecontrol(3)"
name: "lintianprocessablecontrol"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianprocessablecontrol/"
description: "Lintian::Processable::Control – access to collected control file data"
---

<p>Lintian::Processable::Control &#8211; access to collected control file data </p>
<h2>Synopsis</h2>
<pre>
    use Lintian::Processable;
    my $processable = Lintian::Processable::Binary-&gt;new;
</pre>
<h2>Description</h2>
<p> Lintian::Processable::Control provides an interface to control file data.</p>
<h2>Instance Methods</h2>
<dl COMPACT>
<dt>control</p>
<dd> Returns the index for a binary control file.</p>
<dt>control_index (<font SIZE="-1">FILE</font>)</p>
<dd> Returns a path object to <font SIZE="-1">FILE</font> in the control.tar.gz. <font SIZE="-1">FILE</font> must be relative to the root of the control.tar.gz and must be without leading slash (or &#8220;./&#8221;). If <font SIZE="-1">FILE</font> is not in the control.tar.gz, it returns <tt>&quot;undef&quot;</tt>. </p>
<p> To get a list of entries in the control.tar.gz, see &#8220;sorted_control_index&#8221;. To actually access the underlying file (e.g. the contents), use &#8220;control ([<font SIZE="-1">FILE</font>])&#8221;. </p>
<p> Note that the &#8220;root directory&#8221; (denoted by the empty string) will always be present, even if the underlying tarball omits it. </p>
<p> Needs-Info requirements for using <i>control_index</i>: bin-pkg-control</p>
<dt>sorted_control_index</p>
<dd> Returns a sorted array of file names listed in the control.tar.gz. The names will not have a leading slash (or &#8220;./&#8221;) and can be passed to &#8220;control ([<font SIZE="-1">FILE</font>])&#8221; or &#8220;control_index (<font SIZE="-1">FILE</font>)&#8221; as is. </p>
<p> The array will not contain the entry for the &#8220;root&#8221; of the control.tar.gz. </p>
<p> Needs-Info requirements for using <i>sorted_control_index</i>: Same as control_index</p>
<dt>control_index_resolved_path(<font SIZE="-1">PATH</font>)</p>
<dd> Resolve <font SIZE="-1">PATH</font> (relative to the root of the package) and return the entry denoting the resolved path. </p>
<p> The resolution is done using resolve_path. </p>
<p> Needs-Info requirements for using <i>control_index_resolved_path</i>: Same as control_index</dl>
<h2>Author</h2>
<p> Originally written by Felix Lechner &lt;felix.lechner [at] lease-up.com&gt; for Lintian.</p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1)</p>
