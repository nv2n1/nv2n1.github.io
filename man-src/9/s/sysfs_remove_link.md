---
title: "sysfs_remove_link(9)"
name: "sysfs_remove_link"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sysfs_remove_link/"
---

sysfs_remove_link - remove symlink in object's directory.

<h2>Synopsis</h2>

<pre><code>void sysfs_remove_link(struct kobject *kobj, const char *name);</code></pre>

<h2>Arguments</h2>

<i>kobj</i>
<dl><dd><dd>object we're acting for.</dl>
 

 <i>name</i>
<dl><dd>name of the symlink to remove.</dl>

<h2>Copyright</h2>


