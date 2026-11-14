---
title: "snd_ctl_enum_info(9)"
name: "snd_ctl_enum_info"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_ctl_enum_info/"
---

snd_ctl_enum_info - fills the info structure for an enumerated control

<h2>Synopsis</h2>

<pre><code>int snd_ctl_enum_info(struct snd_ctl_elem_info *info, unsigned int channels, unsigned int items, const char *const names[]);</code></pre>

<h2>Arguments</h2>

<i>info</i>
<dl><dd><dd>the structure to be filled</dl>
 

 <i>channels</i>
<dl><dd>the number of the control's channels; often one</dl>
 

 <i>items</i>
<dl><dd>the number of control values; also the size of <i>names</i></dl>
 

 <i>names[]</i>
<dl><dd>an array containing the names of all control values</dl>

<h2>Description</h2>

Sets all required fields in <i>info</i> to their appropriate values. If the control's accessibility is not the default (readable and writable), the caller has to fill <i>info</i>-&gt;access.

<h2>Return</h2>

Zero.

<h2>Copyright</h2>


