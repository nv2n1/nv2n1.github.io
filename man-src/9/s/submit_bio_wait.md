---
title: "submit_bio_wait(9)"
name: "submit_bio_wait"
section: "9"
letter: "s"
url: "/docs/linux/man/9-submit_bio_wait/"
description: "submit_bio_wait – submit a bio, and wait until it completes"
---

<p>submit_bio_wait &#8211; submit a bio, and wait until it completes</p>
<h2>Synopsis</h2>
<pre><code>int submit_bio_wait(struct bio *bio);</code></pre>
<h2>Arguments</h2>
<p><i>bio</i></p>
<dl>
<dd>
<dd>The struct bio which describes the I/O</dl>
<h2>Description</h2>
<p>Simple wrapper around <code>submit_bio</code>. Returns 0 on success, or the error from <code>bio_endio</code> on failure.</p>
<h2>Copyright</h2>
