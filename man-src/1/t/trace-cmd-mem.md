---
title: "trace-cmd-mem(1)"
name: "trace-cmd-mem"
section: "1"
letter: "t"
url: "/docs/linux/man/1-trace-cmd-mem/"
description: "trace-cmd-mem – show memory usage of certain kmem events"
---

<h2 class="name">NAME</h2>
<p> trace-cmd-mem &#8211; show memory usage of certain kmem events </p>
<h2>SYNOPSIS</h2>
<p> <code>trace-cmd mem</code> [<i>OPTIONS</i>][<i>input-file</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <a href="/docs/linux/man/1-trace-cmd/">trace-cmd</a>(1) mem requires a trace-cmd record that enabled the following events: </p>
<dl>
<dt>
<dd>
<pre>
kmalloc
kmalloc_node
kfree
kmem_cache_alloc
kmem_cache_alloc_node
kmem_cache_alloc_free
</pre>
</dl>
<p> It then reads the amount requested and the ammount freed as well as the functions that called the allocation. It then reports the final amount of bytes requested and allocated, along with the total amount allocated and requested, as well as the max allocation and requested during the run. It reports the amount of wasted bytes (allocated &#8211; requested) that was not freed, as well as the max wasted amount during the run. The list is sorted by descending order of wasted bytes after the run. </p>
<dl>
<dt>
<dd>
<pre><code>
Function Waste Alloc req TotAlloc TotReq MaxAlloc MaxReq MaxWaste-- -- -- -- -- -- - -- -- - -- - -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --rb_allocate_cpu_buffer 768 2304 1536 2304 1536 2304 1536 768 alloc_pipe_info 400 1152 752 1152 752 1152 752 400 instance_mkdir 252 544 292 544 292 544 292 252 __d_alloc 215 1086560 1086345 1087208 1086993 1086560 1086345 215 get_empty_filp 72 2304 2232 4864 4712 4864 4712 152 mm_alloc 40 960 920 960 920 960 920 40 prepare_creds 32 192 160 1728 1440 1728 1440 288 tracing_buffers_open 8 32 24 32 24 32 24 8 do_brk 0 0 0 368 368 368 368 0 journal_add_journal_head 0 6048 6048 6048 6048 6048 6048 0 journal_start 0 0 0 1224 1224 48 48 0 __rb_allocate_pages 0 3289856 3289856 3289856 3289856 3289856 3289856 0 anon_vma_alloc 0 0 0 936 936 864 864 0
    [...]
</code></pre>
</dl>
<h2>OPTIONS</h2>
<p> <code>-i</code> <i>input-file</i></p>
<dl>
<dt>
<dd> By default, trace-cmd hist will read the file <i>trace.dat</i>. But the <code>-i</code> option open up the given <i>input-file</i> instead. Note, the input file may also be specified as the last item on the command line.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-trace-cmd/">trace-cmd</a>(1), <a href="/docs/linux/man/1-trace-cmd-record/">trace-cmd-record</a>(1), <a href="/docs/linux/man/1-trace-cmd-report/">trace-cmd-report</a>(1), <a href="/docs/linux/man/1-trace-cmd-start/">trace-cmd-start</a>(1), <a href="/docs/linux/man/1-trace-cmd-stop/">trace-cmd-stop</a>(1), <a href="/docs/linux/man/1-trace-cmd-extract/">trace-cmd-extract</a>(1), <a href="/docs/linux/man/1-trace-cmd-reset/">trace-cmd-reset</a>(1), <a href="/docs/linux/man/1-trace-cmd-hist/">trace-cmd-hist</a>(1), <a href="/docs/linux/man/1-trace-cmd-split/">trace-cmd-split</a>(1), <a href="/docs/linux/man/1-trace-cmd-listen/">trace-cmd-listen</a>(1)</p>
<h2>AUTHOR</h2>
<p> Written by Steven Rostedt, &lt;m[blue]<code>rostedt [at] goodmis.org</code>m[]<font SIZE="-2">[1]</font>&gt;</p>
<h2>RESOURCES</h2>
<p> <a href="git://git.kernel.org/pub/scm/linux/kernel/git/rostedt/trace-cmd.git">git://git.kernel.org/pub/scm/linux/kernel/git/rostedt/trace-cmd.git</a></p>
<h2>COPYING</h2>
<p> Copyright (C) 2013 Red Hat, Inc. Free use of this software is granted under the terms of the GNU Public License (GPL).</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> rostedt [at] goodmis.org</p>
<dl>
<dt>
<dd> mailto:rostedt [at] goodmis.org</dl>
</dl>
<h2>Index</h2>
