---
title: "chmem(8)"
name: "chmem"
section: "8"
letter: "c"
url: "/docs/linux/man/8-chmem/"
description: "chmem – configure memory"
---

<p>chmem &#8211; configure memory</p>
<h2>Synopsis</h2>
<p><code>chmem</code> [<code>-h] [</code>-V*] [<code>-v</code>] [<code>-e</code>|<code>-d</code>] [<i>SIZE</i>|<i>RANGE</i> <code>-b</code> <i>BLOCKRANGE</i>] [<code>-z</code> <i>ZONE</i>]</p>
<h2>Description</h2>
<p>The chmem command sets a particular size or range of memory online or offline. </p>
<dl>
<dd>&bull; Specify <i>SIZE</i> as &lt;size&gt;[m|M|g|G]. With m or M, &lt;size&gt; specifies the memory size in MiB (1024 x 1024 bytes). With g or G, &lt;size&gt; specifies the memory size in GiB (1024 x 1024 x 1024 bytes). The default unit is MiB.</dl>
<dl>
<dd>&bull; Specify <i>RANGE</i> in the form 0x&lt;start&gt;-0x&lt;end&gt; as shown in the output of the <code><a href="/docs/linux/man/1-lsmem/">lsmem</a></code>(1) command. &lt;start&gt; is the hexadecimal address of the first byte and &lt;end&gt; is the hexadecimal address of the last byte in the memory range.</dl>
<dl>
<dd>&bull; Specify <i>BLOCKRANGE</i> in the form &lt;first&gt;-&lt;last&gt; or &lt;block&gt; as shown in the output of the <code><a href="/docs/linux/man/1-lsmem/">lsmem</a></code>(1) command. &lt;first&gt; is the number of the first memory block and &lt;last&gt; is the number of the last memory block in the memory range. Alternatively a single block can be specified. <i>BLOCKRANGE</i> requires the <code>&#8211;blocks</code> option.</dl>
<dl>
<dd>&bull; Specify <i>ZONE</i> as the name of a memory zone, as shown in the output of the <code>lsmem -o +ZONES</code> command. The output shows one or more valid memory zones for each memory range. If multiple zones are shown, then the memory range currently belongs to the first zone. By default, <code>chmem</code> will set memory online to the zone Movable, if this is among the valid zones. This default can be changed by specifying the <code>&#8211;zone</code> option with another valid zone. For memory ballooning, it is recommended to select the zone Movable for memory online and offline, if possible. Memory in this zone is much more likely to be able to be offlined again, but it cannot be used for arbitrary kernel allocations, only for migratable pages (e.g., anonymous and page cache pages). Use the <code>&#8211;help</code> option to see all available zones.</dl>
<p> <i>SIZE</i> and <i>RANGE</i> must be aligned to the Linux memory block size, as shown in the output of the <code><a href="/docs/linux/man/1-lsmem/">lsmem</a></code>(1) command. </p>
<p> Setting memory online can fail for various reasons. On virtualized systems it can fail if the hypervisor does not have enough memory left, for example because memory was overcommitted. Setting memory offline can fail if Linux cannot free the memory. If only part of the requested memory can be set online or offline, a message tells you how much memory was set online or offline instead of the requested amount. </p>
<p> When setting memory online <code>chmem</code> starts with the lowest memory block numbers. When setting memory offline <code>chmem</code> starts with the highest memory block numbers.</p>
<h2>Options</h2>
<p><code>-b</code>, <code>&#8211;blocks</code></p>
<dl>
<dd>Use a <i>BLOCKRANGE</i> parameter instead of <i>RANGE</i> or <i>SIZE</i> for the <code>&#8211;enable</code> and <code>&#8211;disable</code> options.</dl>
<p> <code>-d</code>, <code>&#8211;disable</code></p>
<dl>
<dd>Set the specified <i>RANGE</i>, <i>SIZE</i>, or <i>BLOCKRANGE</i> of memory offline.</dl>
<p> <code>-e</code>, <code>&#8211;enable</code></p>
<dl>
<dd>Set the specified <i>RANGE</i>, <i>SIZE</i>, or <i>BLOCKRANGE</i> of memory online.</dl>
<p> <code>-z</code>, <code>&#8211;zone</code></p>
<dl>
<dd>Select the memory <i>ZONE</i> where to set the specified <i>RANGE</i>, <i>SIZE</i>, or <i>BLOCKRANGE</i> of memory online or offline. By default, memory will be set online to the zone Movable, if possible.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Print a short help text, then exit.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dd>Verbose mode. Causes <code>chmem</code> to print debugging messages about it&#8217;s progress.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dd>Print the version number, then exit.</dl>
<h2>Exit Status</h2>
<p><code>chmem</code> has the following exit status values: </p>
<p> <code>0</code></p>
<dl>
<dd>success</dl>
<p> <code>1</code></p>
<dl>
<dd>failure</dl>
<p> <code>64</code></p>
<dl>
<dd>partial success</dl>
<h2>Example</h2>
<p><code>chmem &#8211;enable 1024</code></p>
<dl>
<dd>This command requests 1024 MiB of memory to be set online.</dl>
<p> <code>chmem -e 2g</code></p>
<dl>
<dd>This command requests 2 GiB of memory to be set online.</dl>
<p> <code>chmem &#8211;disable 0x00000000e4000000-0x00000000f3ffffff</code></p>
<dl>
<dd>This command requests the memory range starting with 0x00000000e4000000 and ending with 0x00000000f3ffffff to be set offline.</dl>
<p> <code>chmem -b -d 10</code></p>
<dl>
<dd>This command requests the memory block number 10 to be set offline.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lsmem/">lsmem</a></code>(1)</p>
<h2>Reporting Bugs</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>Availability</h2>
<p>The <code>chmem</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;.</p>
