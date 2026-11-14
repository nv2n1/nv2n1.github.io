---
title: "choom(1)"
name: "choom"
section: "1"
letter: "c"
url: "/docs/linux/man/1-choom/"
description: "choom – display and adjust OOM-killer score."
---

<h2 class="name">NAME</h2>
<p> choom &#8211; display and adjust OOM-killer score. </p>
<p> <code>choom</code> <code>-p</code> <i>PID</i> </p>
<p> <code>choom</code> <code>-p</code> <i>PID</i> <code>-n</code> <i>number</i> </p>
<p> <code>choom</code> <code>-n</code> <i>number</i> [&#8211;] <i>command</i> [<i>argument</i> &#8230;] </p>
<h2>DESCRIPTION</h2>
<p> The <code>choom</code> command displays and adjusts Out-Of-Memory killer score setting.</p>
<h2>OPTIONS</h2>
<p> <code>-p</code>, <code>&#8211;pid</code> <i>pid</i></p>
<dl>
<dt>
<dd> Specifies process ID.</dl>
<p> <code>-n</code>, <code>&#8211;adjust</code> <i>value</i></p>
<dl>
<dt>
<dd> Specify the adjust score value.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help text and exit.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display version information and exit.</dl>
<h2>NOTES</h2>
<p> Linux kernel uses the badness heuristic to select which process gets killed in out of memory conditions. </p>
<p> The badness heuristic assigns a value to each candidate task ranging from 0 (never kill) to 1000 (always kill) to determine which process is targeted. The units are roughly a proportion along that range of allowed memory the process may allocate from based on an estimation of its current memory and swap use. For example, if a task is using all allowed memory, its badness score will be 1000. If it is using half of its allowed memory, its score will be 500. </p>
<p> There is an additional factor included in the badness score: the current memory and swap usage is discounted by 3% for root processes. </p>
<p> The amount of &quot;allowed&quot; memory depends on the context in which the oom killer was called. If it is due to the memory assigned to the allocating task&#8217;s cpuset being exhausted, the allowed memory represents the set of mems assigned to that cpuset. If it is due to a mempolicy&#8217;s node(s) being exhausted, the allowed memory represents the set of mempolicy nodes. If it is due to a memory limit (or swap limit) being reached, the allowed memory is that configured limit. Finally, if it is due to the entire system being out of memory, the allowed memory represents all allocatable resources. </p>
<p> The adjust score value is added to the badness score before it is used to determine which task to kill. Acceptable values range from -1000 to +1000. This allows userspace to polarize the preference for oom killing either by always preferring a certain task or completely disabling it. The lowest possible value, -1000, is equivalent to disabling oom killing entirely for that task since it will always report a badness score of 0. </p>
<p> Setting an adjust score value of +500, for example, is roughly equivalent to allowing the remainder of tasks sharing the same system, cpuset, mempolicy, or memory controller resources to use at least 50% more memory. A value of -500, on the other hand, would be roughly equivalent to discounting 50% of the task&#8217;s allowed memory from being considered as scoring against the task.</p>
<h2>AUTHORS</h2>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5)</p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>AVAILABILITY</h2>
<p> The <code>choom</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
