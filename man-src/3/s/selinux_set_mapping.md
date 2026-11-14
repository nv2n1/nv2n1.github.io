---
title: "selinux_set_mapping(3)"
name: "selinux_set_mapping"
section: "3"
letter: "s"
url: "/docs/linux/man/3-selinux_set_mapping/"
description: "selinux_set_mapping – establish dynamic object class and permission mapping"
---

<p>selinux_set_mapping &#8211; establish dynamic object class and permission mapping</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;selinux/selinux.h&gt;
struct security_class_mapping {
    const char *name;
    const char *perms[];
};
int selinux_set_mapping(struct security_class_mapping *map);</code></pre>
<h2>Description</h2>
<p><code>selinux_set_mapping</code>() establishes a mapping from a user-provided ordering of object classes and permissions to the numbers actually used by the loaded system policy. Use of this function is highly preferred over the generated constants in the libselinux header files, as this method allows the policy&#8217;s class and permission values to change over time. </p>
<p> After the mapping is established, all libselinux functions that operate on class and permission values take the user-provided numbers, which are determined as follows: </p>
<p> The <i>map</i> argument consists of an array of <code>security_class_mapping</code> structures, which must be terminated by a structure having a NULL name field. Except for this last structure, the <i>name </i> field should refer to the string name of an object class, and the corresponding <i>perms</i> field should refer to an array of permission bit names terminated by a NULL string. </p>
<p> The object classes named in the mapping and the bit indexes of each set of permission bits named in the mapping are numbered in order starting from 1. These numbers are the values that should be passed to subsequent libselinux calls.</p>
<h2>Return Value</h2>
<p>Zero is returned on success. On error, -1 is returned and <i>errno</i> is set appropriately.</p>
<h2>Errors</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd>One of the class or permission names requested in the mapping is not present in the loaded policy.</p>
<dt><code>ENOMEM</code></p>
<dd>An attempt to allocate memory failed.</dl>
<h2>Example</h2>
<pre><code>struct security_class_mapping map[] = {
    {&quot;file&quot;, {&quot;create&quot;, &quot;unlink&quot;, &quot;read&quot;, &quot;write&quot;, NULL}},
    {&quot;socket&quot;, {&quot;bind&quot;, NULL}},
    {&quot;process&quot;, {&quot;signal&quot;, NULL}},
    {NULL}};

if (selinux_set_mapping(map) &lt; 0)
    exit(1);</code></pre>
<p> In this example, after the call has succeeded, classes <code>file</code>, <code>socket</code>, and <code>process</code> will be identified by 1, 2 and 3, respectively. Permissions <i>create</i>, <i>unlink</i>, <i>read</i>, and <i>write</i> (for the <code>file</code> class) will be identified by 1, 2, 4, and 8 respectively. Classes and permissions not listed in the mapping cannot be used.</p>
<h2>Author</h2>
<p>Eamon Walsh &lt;ewalsh [at] tycho.nsa.gov&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-avc_open/">avc_open</a></code>(8), <code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8) </p>
