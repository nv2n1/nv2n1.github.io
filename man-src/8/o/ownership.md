---
title: "ownership(8)"
name: "ownership"
section: "8"
letter: "o"
url: "/docs/linux/man/8-ownership/"
description: "ownership – Compaq ownership tag retriever"
---

<p>ownership &#8211; Compaq ownership tag retriever</p>
<h2>Synopsis</h2>
<p><code>ownership</code> [<code>OPTIONS</code>]</p>
<h2>Description</h2>
<p><code>ownership</code> retrieves and prints the &quot;ownership tag&quot; that can be set on Compaq computers. Contrary to all other programs of the <code>dmidecode</code> package, <code>ownership</code> doesn&#8217;t print any version information, nor labels, but only the raw ownership tag. This should help its integration in scripts.</p>
<h2>Options</h2>
<dl>
<dt><code>-d</code>, <code>&#8211;dev-mem FILE</code></p>
<dd>Read memory from device <code>FILE</code> (default: <code>/dev/mem</code>)</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Display usage information and exit</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Display the version and exit</dl>
<h2>Files</h2>
<p><i>/dev/mem</i></p>
<h2>Author</h2>
<p>Jean Delvare</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-biosdecode/">biosdecode</a></code>(8), <code><a href="/docs/linux/man/8-dmidecode/">dmidecode</a></code>(8), <code><a href="/docs/linux/man/4-mem/">mem</a></code>(4), <code><a href="/docs/linux/man/8-vpddecode/">vpddecode</a></code>(8) </p>
