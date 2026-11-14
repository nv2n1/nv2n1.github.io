---
title: "sysfs_create_file_ns(9)"
name: "sysfs_create_file_ns"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sysfs_create_file_ns/"
---

sysfs_create_file_ns - create an attribute file for an object with custom ns

<h2>Synopsis</h2>

<pre><code>int sysfs_create_file_ns(struct kobject *kobj, const struct attribute *attr, const void *ns);</code></pre>

<h2>Arguments</h2>

<i>kobj</i>
<dl><dd><dd>object we're creating for</dl>
 

 <i>attr</i>
<dl><dd>attribute descriptor</dl>
 

 <i>ns</i>
<dl><dd>namespace the new file should belong to</dl>

<h2>Copyright</h2>


