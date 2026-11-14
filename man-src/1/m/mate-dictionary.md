---
title: "mate-dictionary(1)"
name: "mate-dictionary"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mate-dictionary/"
description: "mate-dictionary – Look up words on dictionaries"
---

<h2>NAME</h2>
<p> mate-dictionary &#8211; Look up words on dictionaries</p>
<h2>SYNOPSIS</h2>
<pre>
<code>mate-dictionary</code>
<br>
<code>mate-dictionary</code><i> [options]</i>
</pre>
<p> or select <code>Dictionary</code> from the <code>Accessories</code> submenu of the Applications menu.</p>
<h2>DESCRIPTION</h2>
<p> <code>MATE Dictionary</code> provides dictionary definitions of words, using a dictionary source. </p>
<p> For full documentation see the <code>MATE Dictionary</code> online help. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;look-up</code><i> word</i></p>
<dd> Looks up the specified word using the pre-defined dictionary source.</p>
<dt><code>&#8211;match</code><i> word</i></p>
<dd> Matches one or more words using the pre-defined dictionary source.</p>
<dt><code>-s</code><i> source</i> or <code>&#8211;source</code><i> source</i></p>
<dd> Uses the specified source for looking up words. This does not affect the global settings.</p>
<dt><code>-n</code> or <code>&#8211;no-window</code></p>
<dd> Using this switch with the &#8211;look-up will print the definitions found on the console without launching the GUI.</p>
<dt><code>-D</code><i> database</i> or <code>&#8211;database</code><i> database</i></p>
<dd> Use the specified database for looking up words. This does not affect the global settings.</p>
<dt><code>&#8211;help</code></p>
<dd> Display help information.</dl>
<h2>CONFIGURATION</h2>
<p> All the configuration is handled using GSettings.</p>
<h2>AUTHOR</h2>
<p> <code>MATE Dictionary</code> was originally written by Spiros Papadimitriou (&lt;spapadim+ [at] cs.cmu.edu&gt;), Mike Hughes (&lt;mfh [at] psilord.com&gt;) and Bradford Hovinen (&lt;hovinen [at] udel.edu&gt;). </p>
<p> Emmanuele Bassi (&lt;ebassi [at] gmail.com&gt;) rewrote it from scratch. </p>
<p> This manual page was originally written by Jochen Voss &lt;voss [at] mathematik.uni-kl.de&gt;. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dict/">dict</a></code>(1), <code><a href="/docs/linux/man/8-dictd/">dictd</a></code>(8), <code><a rel="nofollow" href="http://www.dict.org/">http://www.dict.org/</a></code>, <code>RFC 2229</code> </p>
<h2>Index</h2>
