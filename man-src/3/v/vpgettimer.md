---
title: "vpgettimer(3)"
name: "vpgettimer"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vpgettimer/"
description: "vpGetTimer, vpClearTimer – interval timer facility"
---

<p>vpGetTimer, vpClearTimer &#8211; interval timer facility</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpGetTimer(</code><i>vpc, option, iptr</i><code>)</code></p>
<dd>
<dd>vpContext *<i>vpc;</i></p>
<dd>int <i>option;</i></p>
<dd>int *<i>iptr;</i>;  vpResult</p>
<dl>
<dt> <code>vpClearTimer(</code><i>vpc, option</i><code>)</code></p>
<dd>
<dd>vpContext *<i>vpc;</i></p>
<dd>int <i>option;</i></dl>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></p>
<dd>VolPack context from <code>vpCreateContext.</code></p>
<dt><i>option</i></p>
<dd>Constant that specifies a particular timer.</p>
<dt><i>iptr</i></p>
<dd>Location for storing the timer value.</dl>
<h2>Description</h2>
<p>These functions are used for measuring the performance of the VolPack library. To use them, the library must be compiled with a special flag: either -DHAVE_LORES_TIMER (for machine that support the gettimeofday C library call) or -DHAVE_HIRES_TIMER (for SGI machines that support high-resolution memory-mapped I/O timers; on a Challenge or ONYX, the -DHAVE_64BIT_TIMER must also be specified). If one of these flags is specified at compile time then VolPack maintains a table recording the accumulated time spent in various operations. Note that some of the operations can only be timed with a high-resolution timer; time values will not be recorded and will appear to be zero if a low resolution timer is specified at compile time. </p>
<p> <code>vpGetTimer</code> retrieves the accumulated time for a particular operation. The <i>option</i> argument specifies which operation:</p>
<dl>
<dt>VPTIMER_SHADE</p>
<dd>Time the routine that computes the contents of the shading lookup table.</p>
<dt>VPTIMER_RENDER</p>
<dd>Time the routine that renders a volume (includes VPTIMER_CLSFY_OCTREE, VPTIMER_COMPOSITE, VPTIMER_DEPTHCUE, and VPTIMER_WARP).</p>
<dt>VPTIMER_COMPOSITE</p>
<dd>Time the routine that computes the intermediate image from the volume (includes VPTIMER_CLEAR, VPTIMER_TRAVERSE_OCTREE, VPTIMER_ERT, VPTIMER_TRAVERSE_RUNS, and VPTIMER_PROCESS_VOXELS).</p>
<dt>VPTIMER_DEPTHCUE</p>
<dd>Time the routine that performs the depth cueing fixup on the intermediate image.</p>
<dt>VPTIMER_WARP</p>
<dd>Time the routine that warps the intermediate image into the final image.</p>
<dt>VPTIMER_TRAVERSE_RUNS</p>
<dd>Time the portion of the compositing routine devoted to traversing the volume data structures.</p>
<dt>VPTIMER_PROCESS_VOXELS</p>
<dd>Time the portion of the compositing routine devoted to compositing voxels into the intermediate image.</p>
<dt>VPTIMER_ERT</p>
<dd>Time the early-ray termination checks during compositing.</p>
<dt>VPTIMER_CLSFY_OCTREE</p>
<dd>Time the octree classification stage.</p>
<dt>VPTIMER_TRAVERSE_OCTREE</p>
<dd>Time the portion of the compositing routine devoted to traversing the octree.</p>
<dt>VPTIMER_CLEAR</p>
<dd>Time the routine that clears the intermediate image at the beginning of compositing.</dl>
<p> The routine stores the accumulated time since the last call to <i>vpClearTimer</i> (or since the beginning of the program) in the location specified by <i>iptr.</i> The units of the value are microseconds. </p>
<p> <i>vpClearTimer</i> sets the specified timer value back to zero.</p>
<h2>Errors</h2>
<p>The normal return value is VP_OK. The following error return value is possible:</p>
<dl>
<dt>VPERROR_BAD_OPTION</p>
<dd>The <i>option</i> argument is invalid.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpcreatecontext/">vpCreateContext</a>(3) </p>
