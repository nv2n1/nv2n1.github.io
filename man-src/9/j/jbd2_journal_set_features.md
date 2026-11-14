---
title: "jbd2_journal_set_features(9)"
name: "jbd2_journal_set_features"
section: "9"
letter: "j"
url: "/docs/linux/man/9-jbd2_journal_set_features/"
description: "jbd2_journal_set_features – Mark a given journal feature in the superblock"
---

<p>jbd2_journal_set_features &#8211; Mark a given journal feature in the superblock</p>
<h2>Synopsis</h2>
<pre><code>int jbd2_journal_set_features(journal_t *journal, unsigned long compat, unsigned long ro, unsigned long incompat);</code></pre>
<h2>Arguments</h2>
<p><i>journal</i></p>
<dl>
<dd>
<dd>Journal to act on.</dl>
<p> <i>compat</i></p>
<dl>
<dd>bitmask of compatible features</dl>
<p> <i>ro</i></p>
<dl>
<dd>bitmask of features that force read-only mount</dl>
<p> <i>incompat</i></p>
<dl>
<dd>bitmask of incompatible features</dl>
<h2>Description</h2>
<p>Mark a given journal feature as present on the superblock. Returns true if the requested features could be set.</p>
<h2>Authors</h2>
<p><code>Roger Gammans</code> &lt;rgammans [at] computer-surgery.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Stephen Tweedie</code> &lt;sct [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
