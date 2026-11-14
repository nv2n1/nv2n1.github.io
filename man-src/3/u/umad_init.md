---
title: "umad_init(3)"
name: "umad_init"
section: "3"
letter: "u"
url: "/docs/linux/man/3-umad_init/"
description: "umad_init, umad_done – perform library initialization and finalization"
---

<p>umad_init, umad_done &#8211; perform library initialization and finalization</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;infiniband/umad.h&gt;

int umad_init(void);
int umad_done(void);</code></pre>
<h2>Description</h2>
<p><code>umad_init()</code> initializes the umad library for use. Must be called before any other call to this library. </p>
<p> <code>umad_done()</code> finalizes the use of the umad library.</p>
<h2>Return Value</h2>
<p><code>umad_init()</code> and <code>umad_done()</code> return 0 on success, and -1 on error. Error is returned from <code>umad_init()</code> if infiniband umad can&#8217;t be opened, or the abi version doesn&#8217;t match. There are no errors currently returned by <code>umad_done().</code></p>
<h2>Notes</h2>
<p>If an error occurs during the library initialization, no further use of the umad library should be attempted.</p>
<h2>Authors</h2>
<dl>
<dt>Hal Rosenstock &lt;halr [at] voltaire.com&gt;</p>
<dd>
<dt>Dotan Barak &lt;dotanb [at] mellanox.co.il&gt;</p>
<dd></dl>
