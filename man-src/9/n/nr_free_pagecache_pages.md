---
title: "nr_free_pagecache_pages(9)"
name: "nr_free_pagecache_pages"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nr_free_pagecache_pages/"
description: "nr_free_pagecache_pages – count number of pages beyond high watermark"
---

<p>nr_free_pagecache_pages &#8211; count number of pages beyond high watermark</p>
<h2>Synopsis</h2>
<pre><code>unsigned long nr_free_pagecache_pages(void);</code></pre>
<h2>Arguments</h2>
<p><i>void</i></p>
<dl>
<dd>
<dd>no arguments</dl>
<h2>Description</h2>
<p><code>nr_free_pagecache_pages</code> counts the number of pages which are beyond the high watermark within all zones.</p>
<h2>Copyright</h2>
