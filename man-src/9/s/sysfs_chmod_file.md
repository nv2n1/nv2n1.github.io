---
title: "sysfs_chmod_file(9)"
name: "sysfs_chmod_file"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sysfs_chmod_file/"
---

sysfs_chmod_file - update the modified mode value on an object attribute.

<h2>Synopsis</h2>

<pre><code>int sysfs_chmod_file(struct kobject *kobj, const struct attribute *attr, umode_t mode);</code></pre>

<h2>Arguments</h2>

<i>kobj</i>
<dl><dd><dd>object we're acting for.</dl>
 

 <i>attr</i>
<dl><dd>attribute descriptor.</dl>
 

 <i>mode</i>
<dl><dd>file permissions.</dl>

<h2>Copyright</h2>


