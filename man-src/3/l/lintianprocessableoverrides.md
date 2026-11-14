---
title: "lintianprocessableoverrides(3)"
name: "lintianprocessableoverrides"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianprocessableoverrides/"
description: "Lintian::Processable::Overrides – access to override data"
---

<p>Lintian::Processable::Overrides &#8211; access to override data </p>
<h2>Synopsis</h2>
<pre>
    use Lintian::Processable;
    my $processable = Lintian::Processable::Binary-&gt;new;
</pre>
<h2>Description</h2>
<p> Lintian::Processable::Overrides provides an interface to package data for overrides.</p>
<h2>Instance Methods</h2>
<dl COMPACT>
<dt>add_overrides</p>
<dd>
<dt>overrides(<font SIZE="-1">OVERRIDE-FILE</font>)</p>
<dd> Read OVERRIDE-FILE and add the overrides found there which match the metadata of the current file (package and type). The overrides are added to the overrides hash in the info hash entry for the current file. </p>
<p> <code>file_start()</code> must be called before this method. This method throws an exception if there is no current file and calls <code>fail()</code> if the override file cannot be opened.</dl>
<h2>Author</h2>
<p> Originally written by Felix Lechner &lt;felix.lechner [at] lease-up.com&gt; for Lintian.</p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1)</p>
