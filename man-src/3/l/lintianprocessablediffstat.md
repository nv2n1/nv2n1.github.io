---
title: "lintianprocessablediffstat(3)"
name: "lintianprocessablediffstat"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianprocessablediffstat/"
description: "Lintian::Processable::Diffstat – access to collected diffstat data"
---

<p>Lintian::Processable::Diffstat &#8211; access to collected diffstat data </p>
<h2>Synopsis</h2>
<pre>
    use Lintian::Processable;
    my $processable = Lintian::Processable::Binary-&gt;new;
</pre>
<h2>Description</h2>
<p> Lintian::Processable::Diffstat provides an interface to diffstat data.</p>
<h2>Instance Methods</h2>
<dl COMPACT>
<dt>diffstat</p>
<dd> Returns the path to diffstat output run on the Debian packaging diff (a.k.a. the &#8220;diff.gz&#8221;) for 1.0 non-native packages. For source packages without a &#8220;diff.gz&#8221; component, this returns the path to an empty file (this may be a device like /dev/null). </p>
<p> Needs-Info requirements for using <i>diffstat</i>: diffstat</p>
<dt>saved_diffstat</p>
<dd> Returns the cached diffstat information.</dl>
<h2>Author</h2>
<p> Originally written by Felix Lechner &lt;felix.lechner [at] lease-up.com&gt; for Lintian.</p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1)</p>
