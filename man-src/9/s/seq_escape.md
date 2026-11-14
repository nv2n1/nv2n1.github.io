---
title: "seq_escape(9)"
name: "seq_escape"
section: "9"
letter: "s"
url: "/docs/linux/man/9-seq_escape/"
description: "seq_escape – print string into buffer, escaping some characters"
---

<p>seq_escape &#8211; print string into buffer, escaping some characters</p>
<h2>Synopsis</h2>
<pre><code>void seq_escape(struct seq_file *m, const char *s, const char *esc);</code></pre>
<h2>Arguments</h2>
<p><i>m</i></p>
<dl>
<dd>
<dd>target buffer</dl>
<p> <i>s</i></p>
<dl>
<dd>string</dl>
<p> <i>esc</i></p>
<dl>
<dd>set of characters that need escaping</dl>
<h2>Description</h2>
<p>Puts string into buffer, replacing each occurrence of character from <i>esc</i> with usual octal escape. Use <code>seq_has_overflowed</code> to check for errors.</p>
<h2>Copyright</h2>
