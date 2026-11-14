---
title: "lintianprocessablecontrolconffiles(3)"
name: "lintianprocessablecontrolconffiles"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianprocessablecontrolconffiles/"
description: "Lintian::Processable::Control::Conffiles – access to collected control data for conffiles"
---

<p>Lintian::Processable::Control::Conffiles &#8211; access to collected control data for conffiles </p>
<h2>Synopsis</h2>
<pre>
    use Lintian::Processable;
    my $processable = Lintian::Processable::Binary-&gt;new;
</pre>
<h2>Description</h2>
<p> Lintian::Processable::Control::Conffiles provides an interface to control data for conffiles.</p>
<h2>Instance Methods</h2>
<dl COMPACT>
<dt>conffiles</p>
<dd> Returns a list of absolute filenames found for conffiles. </p>
<p> Needs-Info requirements for using <i>conffiles</i>: Same as control_index_resolved_path</p>
<dt>is_conffile (<font SIZE="-1">FILE</font>)</p>
<dd> Returns a truth value if <font SIZE="-1">FILE</font> is listed in the conffiles control file. If the control file is not present or <font SIZE="-1">FILE</font> is not listed in it, it returns <tt>&quot;undef&quot;</tt>. </p>
<p> Note that <font SIZE="-1">FILE</font> should be the filename relative to the package root (even though the control file uses absolute paths). If the control file does relative paths, they are assumed to be relative to the package root as well (and used without warning). </p>
<p> Needs-Info requirements for using <i>is_conffile</i>: Same as control_index_resolved_path</dl>
<h2>Author</h2>
<p> Originally written by Felix Lechner &lt;felix.lechner [at] lease-up.com&gt; for Lintian.</p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1)</p>
