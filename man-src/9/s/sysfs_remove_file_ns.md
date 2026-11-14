---
title: "sysfs_remove_file_ns(9)"
name: "sysfs_remove_file_ns"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sysfs_remove_file_ns/"
---

sysfs_remove_file_ns - remove an object attribute with a custom ns tag

<h2>Synopsis</h2>

<pre><code>void sysfs_remove_file_ns(struct kobject *kobj, const struct attribute *attr, const void *ns);</code></pre>

<h2>Arguments</h2>

<i>kobj</i>
<dl><dd><dd>object we're acting for</dl>
 

 <i>attr</i>
<dl><dd>attribute descriptor</dl>
 

 <i>ns</i>
<dl><dd>namespace tag of the file to remove</dl>

<h2>Description</h2>

Hash the attribute name and namespace tag and kill the victim.

<h2>Copyright</h2>


