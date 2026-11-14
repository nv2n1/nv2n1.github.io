---
title: "sysfs_rename_link_ns(9)"
name: "sysfs_rename_link_ns"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sysfs_rename_link_ns/"
---

sysfs_rename_link_ns - rename symlink in object's directory.

<h2>Synopsis</h2>

<pre><code>int sysfs_rename_link_ns(struct kobject *kobj, struct kobject *targ, const char *old, const char *new, const void *new_ns);</code></pre>

<h2>Arguments</h2>

<i>kobj</i>
<dl><dd><dd>object we're acting for.</dl>
 

 <i>targ</i>
<dl><dd>object we're pointing to.</dl>
 

 <i>old</i>
<dl><dd>previous name of the symlink.</dl>
 

 <i>new</i>
<dl><dd>new name of the symlink.</dl>
 

 <i>new_ns</i>
<dl><dd>new namespace of the symlink.</dl>

<h2>Description</h2>

A helper function for the common rename symlink idiom.

<h2>Copyright</h2>


