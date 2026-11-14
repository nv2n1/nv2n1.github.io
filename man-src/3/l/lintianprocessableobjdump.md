---
title: "lintianprocessableobjdump(3)"
name: "lintianprocessableobjdump"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianprocessableobjdump/"
description: "Lintian::Processable::Objdump – access to collected binary object data"
---

<p>Lintian::Processable::Objdump &#8211; access to collected binary object data </p>
<h2>Synopsis</h2>
<pre>
    use Lintian::Processable;
    my $processable = Lintian::Processable::Binary-&gt;new;
</pre>
<h2>Description</h2>
<p> Lintian::Processable::Objdump provides an interface to collected binary object data.</p>
<h2>Instance Methods</h2>
<dl COMPACT>
<dt>objdump_info</p>
<dd> Returns a hashref mapping a <font SIZE="-1">FILE</font> to the data collected by objdump-info or <tt>&quot;undef&quot;</tt> if no data is available for that <font SIZE="-1">FILE.</font> Data is generally only collected for <font SIZE="-1">ELF</font> files. </p>
<p> Needs-Info requirements for using <i>objdump_info</i>: objdump-info</dl>
<h2>Author</h2>
<p> Originally written by Felix Lechner &lt;felix.lechner [at] lease-up.com&gt; for Lintian.</p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1)</p>
