---
title: "sysfs_remove_file_from_group(9)"
name: "sysfs_remove_file_from_group"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sysfs_remove_file_from_group/"
---

sysfs_remove_file_from_group - remove an attribute file from a group.

<h2>Synopsis</h2>

<pre><code>void sysfs_remove_file_from_group(struct kobject *kobj, const struct attribute *attr, const char *group);</code></pre>

<h2>Arguments</h2>

<i>kobj</i>
<dl><dd><dd>object we're acting for.</dl>
 

 <i>attr</i>
<dl><dd>attribute descriptor.</dl>
 

 <i>group</i>
<dl><dd>group name.</dl>

<h2>Copyright</h2>


