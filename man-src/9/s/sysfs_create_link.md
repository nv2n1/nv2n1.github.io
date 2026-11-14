---
title: "sysfs_create_link(9)"
name: "sysfs_create_link"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sysfs_create_link/"
---

sysfs_create_link - create symlink between two objects.

<h2>Synopsis</h2>

<pre><code>int sysfs_create_link(struct kobject *kobj, struct kobject *target, const char *name);</code></pre>

<h2>Arguments</h2>

<i>kobj</i>
<dl><dd><dd>object whose directory we're creating the link in.</dl>
 

 <i>target</i>
<dl><dd>object we're pointing to.</dl>
 

 <i>name</i>
<dl><dd>name of the symlink.</dl>

<h2>Copyright</h2>


