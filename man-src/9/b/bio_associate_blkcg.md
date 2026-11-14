---
title: "bio_associate_blkcg(9)"
name: "bio_associate_blkcg"
section: "9"
letter: "b"
url: "/docs/linux/man/9-bio_associate_blkcg/"
---

bio_associate_blkcg - associate a bio with the specified blkcg

<h2>Synopsis</h2>

<pre><code>int bio_associate_blkcg(struct bio *bio, struct cgroup_subsys_state *blkcg_css);</code></pre>

<h2>Arguments</h2>

<i>bio</i>
<dl><dd><dd>target bio</dl>
 

 <i>blkcg_css</i>
<dl><dd>css of the blkcg to associate</dl>

<h2>Description</h2>

Associate <i>bio</i> with the blkcg specified by <i>blkcg_css</i>. Block layer will treat <i>bio</i> as if it were issued by a task which belongs to the blkcg. 

 This function takes an extra reference of <i>blkcg_css</i> which will be put when <i>bio</i> is released. The caller must own <i>bio</i> and is responsible for synchronizing calls to this function.

<h2>Copyright</h2>


