---
title: "acpihelp(1)"
name: "acpihelp"
section: "1"
letter: "a"
url: "/docs/linux/man/1-acpihelp/"
description: "acpihelp – ACPI help utility"
---

<h2 class="name">NAME</h2>
<p> acpihelp &#8211; ACPI help utility </p>
<h2>SYNOPSIS</h2>
<p> <code>acpihelp</code> &lt;option&gt;<i>&#8230;</i> [&lt;name-prefix&gt;|&lt;hex-value&gt;] </p>
<h2>DESCRIPTION</h2>
<p> This manual page briefly documents the <code>acpihelp</code> command. The option list is taken from the acpihelp interactive help. </p>
<p> <code>acpihelp</code> provides descriptive text for AML and ASL keywords, methods, and opcodes. </p>
<p> Much more detailed documentation may be found at <a rel="nofollow" href="http://www.acpica.org/documentation/.">http://www.acpica.org/documentation/.</a> </p>
<p> If neither a &lt;name-prefix&gt; or a &lt;hex-value&gt; is provided, <code>acpihelp</code> will do the logical equivalent of a &quot;display all.&quot; </p>
<p> A default search (that is, a search with no options) and a &lt;name-prefix&gt; can mean two different things: (1) if &lt;name-prefix&gt; does not start with an underscore, find ASL operator names, or (2) if &lt;name-prefix&gt; does start with an underscore, find ASL predefined method names. </p>
<h2>OPTIONS</h2>
<h3>ACPI Names and Symbols</h3>
<dl>
<dt><code>-k [&lt;name-prefix&gt;]</code></p>
<dd> Find/Display ASL non-operator keyword(s)</p>
<dt><code>-m [&lt;name-prefix&gt;]</code></p>
<dd> Find/Display AML opcode name(s)</p>
<dt><code>-p [&lt;name-prefix&gt;]</code></p>
<dd> Find/Display ASL predefined method name(s)</p>
<dt><code>-s [&lt;name-prefix&gt;]</code></p>
<dd> Find/Display ASL operator name(s) </p>
</dl>
<h3>ACPI Values</h3>
<dl>
<dt><code>-e [&lt;hex-value&gt;]</code></p>
<dd> Decode ACPICA exception code</p>
<dt><code>-i</code></p>
<dd> Display known ACPI Device IDs (_HID)</p>
<dt><code>-i [&lt;hex-value&gt;]</code></p>
<dd> Decode hex AML opcode </p>
</dl>
<h2>AUTHOR</h2>
<p> acpihelp was written by Robert Moore &lt;robert.moore [at] intel.com&gt;. </p>
<p> This manual page was written by Al Stone &lt;ahs3 [at] redhat.com&gt; for the Fedora project (but may be used by others). </p>
<h2>Index</h2>
