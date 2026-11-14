---
title: "submit_bio(9)"
name: "submit_bio"
section: "9"
letter: "s"
url: "/docs/linux/man/9-submit_bio/"
description: "submit_bio – submit a bio to the block device layer for I/O"
---

<p>submit_bio &#8211; submit a bio to the block device layer for I/O</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>blk_qc_t submit_bio(struct bio&nbsp;<wbr>*&nbsp;<wbr></code><i>bio</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>bio</i></p>
<dl>
<dd>
<dd>The struct bio which describes the I/O</dl>
<h2>Description</h2>
<p><code>submit_bio</code> is very similar in purpose to <code>generic_make_request</code>, and uses that function to do most of the work. Both are fairly rough interfaces; <i>bio</i> must be presetup and ready for I/O.</p>
<h2>Copyright</h2>
