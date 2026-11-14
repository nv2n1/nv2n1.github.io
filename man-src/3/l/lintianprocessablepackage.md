---
title: "lintianprocessablepackage(3)"
name: "lintianprocessablepackage"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianprocessablepackage/"
---

Lintian::Processable::Package -- An object that Lintian can process 

<h2>Synopsis</h2>
 <pre>
 use Lintian::Processable::Package;
 
 my $proc = Lintian::Processable::Package-&gt;new ('lintian_2.5.0_all.deb');
 my $pkg_name = $proc-&gt;pkg_name;
 my $pkg_version = $proc-&gt;pkg_version;
 # etc.
</pre>
<h2>Description</h2>
 Instances of this perl class are objects that Lintian can process (e.g. deb files). Multiple objects can then be combined into groups, which Lintian will process together.
<h2>Class Methods</h2>
<dl COMPACT>
<dt>new (FILE[, <font SIZE="-1">TYPE</font>])
<dd> Creates a processable from <font SIZE="-1">FILE.</font> If <font SIZE="-1">TYPE</font> is given, the <font SIZE="-1">FILE</font> is assumed to be that <font SIZE="-1">TYPE</font> otherwise the type is determined by the file extension. 

 <font SIZE="-1">TYPE</font> is one of ``binary'' (.deb), ``udeb'' (.udeb), ``source'' (.dsc) or ``changes'' (.changes).</dl>

<h2>Author</h2>
 Originally written by Niels Thykier &lt;niels [at] thykier.net&gt; for Lintian.
<h2>See Also</h2>
 <i><a HREF="/docs/linux/man/1-lintian/">lintian</a></i>(1) 

 Lintian::Processable 

 Lintian::ProcessableGroup
