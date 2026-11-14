---
title: "wimlib-imagex-split(1)"
name: "wimlib-imagex-split"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wimlib-imagex-split/"
description: "wimlib-imagex-split – Split a WIM into multiple parts"
---

<h2>NAME</h2>
<p> wimlib-imagex-split &#8211; Split a WIM into multiple parts</p>
<h2>SYNOPSIS</h2>
<p> <code>wimlib-imagex split</code> <i>WIMFILE</i> <i>SPLIT_WIM_PART_1</i> <i>PART_SIZE</i> [<i>OPTION&#8230;</i>]</p>
<h2>DESCRIPTION</h2>
<p> Splits <i>WIMFILE</i> into parts with size at most <i>PART_SIZE</i> mebibytes, with the first part having the name <i>SPLIT_WIM_PART_1</i> and the other parts having names numbered in order of the parts. This command is also available as simply <code>wimsplit</code> if the appropriate hard link or batch file has been installed. </p>
<p> <code>wimlib-imagex split</code> can split both non-pipable and pipable WIMs.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;check</code></p>
<dd> When reading <i>WIMFILE</i>, verify its integrity if the integrity table is present; additionally, when writing each split WIM part, write an integrity table. If this option is not specified, integrity tables will be included in the split WIMs if and only if one was present in <i>WIMFILE</i>.</dl>
<h2>EXAMPLES</h2>
<p> Splits the WIM &#8216;windows.wim&#8217; into &#8216;windows.swm&#8217;, &#8216;windows2.swm&#8217;, &#8216;windows3.swm&#8217;, etc. where each part is at most 100 MiB:</p>
<dl>
<dt>
<dd>
<p> wimlib-imagex split windows.wim windows.swm 100</dl>
<h2>LIMITATIONS</h2>
<p> It is possible for the size of the parts to exceed the <i>PART_SIZE</i> given. This is impossible to avoid because the WIM file format provides no way to divide a single file resource in the WIM among multiple split WIM parts. So if you, for example, have a file inside the WIM that is 100 MiB, then an uncompressed split WIM will have at least one part that is 100 MiB in size to contain that file. However, if the WIM resources are compressed then less space would be needed.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-wimlib-imagex/">wimlib-imagex</a></code>(1) </p>
<h2>Index</h2>
