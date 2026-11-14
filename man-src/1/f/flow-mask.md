---
title: "flow-mask(1)"
name: "flow-mask"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flow-mask/"
description: "flow-mask – Apply tags to flow files."
---

<h2>NAME</h2>
<p> flow-mask &#8211; Apply tags to flow files.</p>
<h2>SYNOPSIS</h2>
<p> <code>flow-mask</code> [ <code>-hk</code> ] [ <code>-b</code><i> big</i><code>|</code><i>little</i> ] [ <code>-C</code><i> comment</i> ] [ <code>-d</code><i> debug_level</i> ] [ <code>-m</code><i> mask_fname</i> ] [ <code>-M</code><i> active_def</i><i>&#8230;</i> ]</p>
<h2>DESCRIPTION</h2>
<p> The <code>flow-mask</code> utility is used to modify the source and destination mask length&#8217;s in flow records.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code><i> big</i><code>|</code><i>little</i></p>
<dd> Byte order of output.</p>
<dt><code>-C</code><i> Comment</i></p>
<dd> Add a comment.</p>
<dt><code>-d</code><i> debug_level</i></p>
<dd> Enable debugging.</p>
<dt><code>-h</code></p>
<dd> Display help.</p>
<dt><code>-k</code></p>
<dd> Keep time from input.</p>
<dt><code>-m</code><i> mask_fname</i></p>
<dd> Load masks from <i>mask_name</i>. Defaults to <i>/etc/flow-tools/cfg/mask</i></p>
<dt><code>-M</code><i> mask_def</i></p>
<dd> Use <i>active_def</i> as the active tag definition(s).</dl>
<p> The configuration file is a collection of definitions. A definition lists a sequence of prefixes and the mask length to replace the matching prefix with. Lines begining with # are treated as comments and ignored. </p>
<pre><code>
mask - definition command Description-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --mask - definition Begin mask - definition section mask - definition foo prefix List the prefix to match on and the replacement mask.prefix 128.146 / 16 24
</code></pre>
<h2>EXAMPLES</h2>
<pre>
#
#file: masks
#
mask-definition foo
# All networks in 128.146/16 are /24's.
 prefix 128.146/16 24
# except for 128.146.214/24, which are /32's.
 prefix 128.146.214/24 32
</pre>
<p> <code>flow-cat </code><i>flows</i><code> | flow-mask -mfoo -Fmasks | flow-print -f4</code></p>
<h2>FILES</h2>
<p> Configuration files: Mask &#8211; <i>/etc/flow-tools/cfg/mask.cfg</i>.</p>
<h2>BUGS</h2>
<p> None known.</p>
<h2>AUTHOR</h2>
<p> Mark Fullmer &lt;maf [at] splintered.net&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flow-tools/">flow-tools</a></code>(1) </p>
<h2>Index</h2>
