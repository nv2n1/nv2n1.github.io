---
title: "bio_associate_current(9)"
name: "bio_associate_current"
section: "9"
letter: "b"
url: "/docs/linux/man/9-bio_associate_current/"
description: "bio_associate_current – associate a bio with current"
---

<p>bio_associate_current &#8211; associate a bio with <code>current</code></p>
<h2>Synopsis</h2>
<pre><code>int bio_associate_current(struct bio *bio);</code></pre>
<h2>Arguments</h2>
<p><i>bio</i></p>
<dl>
<dd>
<dd>target bio</dl>
<h2>Description</h2>
<p>Associate <i>bio</i> with <code>current</code> if it hasn&#8217;t been associated yet. Block layer will treat <i>bio</i> as if it were issued by <code>current</code> no matter which task actually issues it. </p>
<p> This function takes an extra reference of <i>task</i>&#8216;s io_context and blkcg which will be put when <i>bio</i> is released. The caller must own <i>bio</i>, ensure <code>current-</code>&gt;io_context exists, and is responsible for synchronizing calls to this function.</p>
<h2>Copyright</h2>
