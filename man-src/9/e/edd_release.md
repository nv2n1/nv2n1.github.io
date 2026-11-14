---
title: "edd_release(9)"
name: "edd_release"
section: "9"
letter: "e"
url: "/docs/linux/man/9-edd_release/"
---

edd_release - free edd structure

<h2>Synopsis</h2>

<pre><code>void edd_release(struct kobject *kobj);</code></pre>

<h2>Arguments</h2>

<i>kobj</i>
<dl><dd><dd>kobject of edd structure</dl>

<h2>Description</h2>

This is called when the refcount of the edd structure reaches 0. This should happen right after we unregister, but just in case, we use the release callback anyway.

<h2>Copyright</h2>


