---
title: "jbd2_journal_check_used_features(9)"
name: "jbd2_journal_check_used_features"
section: "9"
letter: "j"
url: "/docs/linux/man/9-jbd2_journal_check_used_features/"
description: "jbd2_journal_check_used_features – Check if features specified are used."
---

<p>jbd2_journal_check_used_features &#8211; Check if features specified are used.</p>
<h2>Synopsis</h2>
<pre><code>int jbd2_journal_check_used_features(journal_t *journal, unsigned long compat, unsigned long ro, unsigned long incompat);</code></pre>
<h2>Arguments</h2>
<p><i>journal</i></p>
<dl>
<dd>
</dd><dd>Journal to check.</dd></dl>
<p> <i>compat</i></p>
<dl>
<dd>bitmask of compatible features</dd></dl>
<p> <i>ro</i></p>
<dl>
<dd>bitmask of features that force read-only mount</dd></dl>
<p> <i>incompat</i></p>
<dl>
<dd>bitmask of incompatible features</dd></dl>
<h2>Description</h2>
<p>Check whether the journal uses all of a given set of features. Return true (non-zero) if it does.</p>
<h2>Authors</h2>
<p><code>Roger Gammans</code> &lt;rgammans [at] computer-surgery.co.uk&gt;</p>
<dl>
<dd>Author.</dd></dl>
<p> <code>Stephen Tweedie</code> &lt;sct [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dd></dl>
<h2>Copyright</h2>
