---
title: "wngroups(7)"
name: "wngroups"
section: "7"
letter: "w"
url: "/docs/linux/man/7-wngroups/"
description: "wngroups – discussion of WordNet search code to group similar verb senses"
---

<p>wngroups &#8211; discussion of WordNet search code to group similar verb senses</p>
<h2>Description</h2>
<p>Some similar senses of verbs have been grouped by the lexicographers. This grouping is done statically in the lexicographer source files using the semantic <i>pointer_symbol</i> <code>$</code>. Transitivity is used to combine groups of overlapping senses into the largest sense groups possible.</p>
<h2>Notes</h2>
<p>Coverage of verb groups is incomplete.</p>
<h2>Environment Variables (Unix)</h2>
<dl>
<dt><code>WNHOME</code></dt>
<dd>Base directory for WordNet. Default is <code>/usr/local/WordNet-3.0</code>.</dd>
<dt><code>WNSEARCHDIR</code></dt>
<dd>Directory in which the WordNet database has been installed. Default is <code>WNHOME/dict</code>.</dd></dl>
<h2>Registry (Windows)</h2>
<dl>
<dt><code>HKEY_LOCAL_MACHINE\SOFTWARE\WordNet\3.0\WNHome</code></dt>
<dd>Base directory for WordNet. Default is <code>C:\Program~Files\WordNet\3.0</code>.</dd></dl>
<h2>Files</h2>
<dl>
<dt><code>sentidx.vrb</code></dt>
<dd>verb sense keys and sentence frame numbers</dd>
<dt><code>sents.vrb</code></dt>
<dd>example sentence frames</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-wn/">wn</a></code>(1), <code><a href="/docs/linux/man/1-wnb/">wnb</a></code>(1), <code><a href="/docs/linux/man/5-senseidx/">senseidx</a></code>(5), <code><a href="/docs/linux/man/3-wnsearch/">wnsearch</a></code>(3), <code><a href="/docs/linux/man/5-wndb/">wndb</a></code>(5), <code><a href="/docs/linux/man/7-wnintro/">wnintro</a></code>(7). </p>
