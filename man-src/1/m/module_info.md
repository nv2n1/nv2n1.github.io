---
title: "module_info(1)"
name: "module_info"
section: "1"
letter: "m"
url: "/docs/linux/man/1-module_info/"
description: "module_info – find information about modules"
---

<h2 class="name">NAME</h2>
<p> module_info &#8211; find information about modules </p>
<h2>SYNOPSIS</h2>
<pre><code>
module_info[B&lt;-a&gt;][B&lt;-s&gt;][B&lt;-p&gt;][B&lt;-m&gt;] MODULE | FILE...
</code></pre>
<h2>DESCRIPTION</h2>
<p> List information about the arguments (either module names in the form <tt>&quot;Module::Name&quot;</tt> or paths in the form <tt>&quot;Foo/Bar.pm&quot;</tt> or <tt>&quot;foo/bar.pl&quot;</tt>). </p>
<p> By default only shows module name, version, directory, absolute path and a flag indicating if it is a core module. Additional information can be requested through command line switches.</p>
<dl>
<dt><code>-s</code></p>
<dd> Show subroutines created by the module.</p>
<dt><code>-p</code></p>
<dd> Show packages created by the module.</p>
<dt><code>-m</code></p>
<dd> Show modules <tt>&quot;use()&quot;</tt>d by the module.</p>
<dt><code>-a</code></p>
<dd> Equivalent to <tt>&quot;-s -p -m&quot;</tt>.</dl>
<h2>AUTHOR</h2>
<p> Mattia Barbon &lt;mbarbon [at] cpan.org&gt;</p>
<h2>SEE ALSO</h2>
<p> Module::Info </p>
<h2>Index</h2>
