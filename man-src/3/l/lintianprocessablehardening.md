---
title: "lintianprocessablehardening(3)"
name: "lintianprocessablehardening"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianprocessablehardening/"
description: "Lintian::Processable::Hardening – access to collected hardening data"
---

<p>Lintian::Processable::Hardening &#8211; access to collected hardening data </p>
<h2>Synopsis</h2>
<pre>
    use Lintian::Processable;
    my $processable = Lintian::Processable::Binary-&gt;new;
</pre>
<h2>Description</h2>
<p> Lintian::Processable::Hardening provides an interface to collected hardening data.</p>
<h2>Instance Methods</h2>
<dl COMPACT>
<dt>hardening_info</p>
<dd> Returns a hashref mapping a <font SIZE="-1">FILE</font> to its hardening issues. </p>
<p> <font SIZE="-1">NB:</font> This is generally only useful for checks/binaries to emit the hardening-no-* tags. </p>
<p> Needs-Info requirements for using <i>hardening_info</i>: hardening-info</dl>
<h2>Author</h2>
<p> Originally written by Felix Lechner &lt;felix.lechner [at] lease-up.com&gt; for Lintian.</p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1)</p>
