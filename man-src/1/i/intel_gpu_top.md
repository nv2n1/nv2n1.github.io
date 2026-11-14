---
title: "intel_gpu_top(1)"
name: "intel_gpu_top"
section: "1"
letter: "i"
url: "/docs/linux/man/1-intel_gpu_top/"
description: "intel_gpu_top – Display a top-like summary of Intel GPU usage"
---

<h2>NAME</h2>
<p> intel_gpu_top &#8211; Display a top-like summary of Intel GPU usage</p>
<h2>SYNOPSIS</h2>
<pre>
<code>intel_gpu_top</code>
<code>intel_gpu_top [ parameters ]</code>
</pre>
<h2>DESCRIPTION</h2>
<p> <code>intel_gpu_top</code> is a tool to display usage information of an Intel GPU. It requires root privilege to map the graphics device.</p>
<h3>Options</h3>
<dl>
<dt><code>-s [samples per second]</code></p>
<dd> number of samples to acquire per second</p>
<dt><code>-o [output file]</code></p>
<dd> collect usage statistics to [file]. If file is &quot;-&quot;, run non-interactively and output statistics to stdout.</p>
<dt><code>-e [command to profile]</code></p>
<dd> execute a command, and leave when it is finished. Note that the entire command with all parameters should be included as one parameter.</p>
<dt><code>-h</code></p>
<dd> show usage notes</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>intel_gpu_top -o &quot;cairo-trace-gvim.log&quot; -s 100 -e &quot;cairo-perf-trace /tmp/gvim&quot;</p>
<dd> will run cairo-perf-trace with /tmp/gvim trace, non-interactively, saving the statistics into cairo-trace-gvim.log file, and collecting 100 samples per second.</dl>
<p> Note that idle units are not displayed, so an entirely idle GPU will only display the ring status and header.</p>
<h2>BUGS</h2>
<p> Some GPUs report some units as busy when they aren&#8217;t, such that even when idle and not hung, it will show up as 100% busy. </p>
<h2>Index</h2>
