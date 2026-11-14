---
title: "sysfs_add_file_to_group(9)"
name: "sysfs_add_file_to_group"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sysfs_add_file_to_group/"
---

sysfs_add_file_to_group - add an attribute file to a pre-existing group.

<h2>Synopsis</h2>

<pre><code>int sysfs_add_file_to_group(struct kobject *kobj, const struct attribute *attr, const char *group);</code></pre>

<h2>Arguments</h2>

<i>kobj</i>
<dl><dd><dd>object we're acting for.</dl>
 

 <i>attr</i>
<dl><dd>attribute descriptor.</dl>
 

 <i>group</i>
<dl><dd>group name.</dl>

<h2>Copyright</h2>


