---
title: "do_splice_direct(9)"
name: "do_splice_direct"
section: "9"
letter: "d"
url: "/docs/linux/man/9-do_splice_direct/"
description: "do_splice_direct – splices data directly between two files"
---

<p>do_splice_direct &#8211; splices data directly between two files</p>
<h2>Synopsis</h2>
<pre><code>long do_splice_direct(struct file *in, loff_t *ppos, struct file *out, loff_t *opos, size_t len, unsigned int flags);</code></pre>
<h2>Arguments</h2>
<p><i>in</i></p>
<dl>
<dd>
<dd>file to splice from</dl>
<p> <i>ppos</i></p>
<dl>
<dd>input file offset</dl>
<p> <i>out</i></p>
<dl>
<dd>file to splice to</dl>
<p> <i>opos</i></p>
<dl>
<dd>output file offset</dl>
<p> <i>len</i></p>
<dl>
<dd>number of bytes to splice</dl>
<p> <i>flags</i></p>
<dl>
<dd>splice modifier flags</dl>
<h2>Description</h2>
<p>For use by <code>do_sendfile</code>. splice can easily emulate sendfile, but doing it in the application would incur an extra system call (splice in + splice out, as compared to just <code>sendfile</code>). So this helper can splice directly through a process-private pipe.</p>
<h2>Copyright</h2>
