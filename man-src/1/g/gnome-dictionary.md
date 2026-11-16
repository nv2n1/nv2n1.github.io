---
title: "gnome-dictionary(1)"
name: "gnome-dictionary"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gnome-dictionary/"
description: "gnome-dictionary – Look up words on dictionaries"
---

<h2>NAME</h2>
<p> gnome-dictionary &#8211; Look up words on dictionaries</p>
<h2>SYNOPSIS</h2>
<pre>
<code>gnome-dictionary</code>
<br>
<code>gnome-dictionary</code><i> [options]</i>
</pre>
<p> or select <code>Dictionary</code> from the <code>Accessories</code> submenu of the Applications menu.</p>
<h2>DESCRIPTION</h2>
<p> <code>GNOME Dictionary</code> provides dictionary definitions of words, using a dictionary source. </p>
<p> For full documentation see the <code>GNOME Dictionary</code> online help. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;look-up</code><i> word</i></dt>
<dd> Looks up the specified word using the pre-defined dictionary source.</dd>
<dt><code>&#8211;match</code><i> word</i></dt>
<dd> Matches one or more words using the pre-defined dictionary source.</dd>
<dt><code>-s</code><i> source</i> or <code>&#8211;source</code><i> source</i></dt>
<dd> Uses the specified source for looking up words. This does not affect the global settings.</dd>
<dt><code>-D</code><i> database</i> or <code>&#8211;database</code><i> database</i></dt>
<dd> Use the specified database for looking up words. This does not affect the global settings.</dd>
<dt><code>-S</code><i> strategy</i> or <code>&#8211;strategy</code><i> strategy</i></dt>
<dd> Use the specified strategy for looking up words. This does not affect the global settings.</dd>
<dt><code>&#8211;help</code></dt>
<dd> Display help information.</dd></dl>
<h2>CONFIGURATION</h2>
<p> All the configuration is handled using GConf.</p>
<h2>AUTHOR</h2>
<p> <code>GNOME Dictionary</code> was originally written by Spiros Papadimitriou (&lt;spapadim+ [at] cs.cmu.edu&gt;), Mike Hughes (&lt;mfh [at] psilord.com&gt;) and Bradford Hovinen (&lt;hovinen [at] udel.edu&gt;). </p>
<p> Emmanuele Bassi (&lt;ebassi [at] gmail.com&gt;) rewrote it from scratch. </p>
<p> This manual page was originally written by Jochen Voss &lt;voss [at] mathematik.uni-kl.de&gt;. </p>
<h2>SEE ALSO</h2>
<p> <code>dict</code>(1), <code>dictd</code>(8), <code><a rel="nofollow" href="http://www.dict.org/">http://www.dict.org/</a></code>, <code>RFC 2229</code> </p>
<h2>Index</h2>
