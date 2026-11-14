---
title: "tk_unmaintaingeometry(3)"
name: "tk_unmaintaingeometry"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_unmaintaingeometry/"
description: "Tk_MaintainGeometry, Tk_UnmaintainGeometry – maintain geometry of one window relative to another"
---

<p>Tk_MaintainGeometry, Tk_UnmaintainGeometry &#8211; maintain geometry of one window relative to another </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
<code>Tk_MaintainGeometry</code>(<i>slave, master, x, y, width, height</i>)
<code>Tk_UnmaintainGeometry</code>(<i>slave, master</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tk_Window <i>slave</i> (in) Window whose geometry is to be controlled.</p>
<dd>Tk_Window <i>master</i> (in) Window relative to which <i>slave</i>&#8216;s geometry will be controlled.</p>
<dd>int <i>x</i> (in) Desired x-coordinate of <i>slave</i> in <i>master</i>, measured in pixels from the inside of <i>master</i>&#8216;s left border to the outside of <i>slave</i>&#8216;s left border.</p>
<dd>int <i>y</i> (in) Desired y-coordinate of <i>slave</i> in <i>master</i>, measured in pixels from the inside of <i>master</i>&#8216;s top border to the outside of <i>slave</i>&#8216;s top border.</p>
<dd>int <i>width</i> (in) Desired width for <i>slave</i>, in pixels.</p>
<dd>int <i>height</i> (in) Desired height for <i>slave</i>, in pixels. </p>
</dl>
<h2>Description</h2>
<p><code>Tk_MaintainGeometry</code> and <code>Tk_UnmaintainGeometry</code> make it easier for geometry managers to deal with slaves whose masters are not their parents. Three problems arise if the master for a slave is not its parent:</p>
<dl COMPACT>
<dt>[1]</p>
<dd>The x- and y-position of the slave must be translated from the coordinate system of the master to that of the parent before positioning the slave.</p>
<dt>[2]</p>
<dd>If the master window, or any of its ancestors up to the slave&#8217;s parent, is moved, then the slave must be repositioned within its parent in order to maintain the correct position relative to the master.</p>
<dt>[3]</p>
<dd>If the master or one of its ancestors is mapped or unmapped, then the slave must be mapped or unmapped to correspond.</dl>
<p> None of these problems is an issue if the parent and master are the same. For example, if the master or one of its ancestors is unmapped, the slave is automatically removed by the screen by X. </p>
<p> <code>Tk_MaintainGeometry</code> deals with these problems for slaves whose masters are not their parents, as well as handling the simpler case of slaves whose masters are their parents. <code>Tk_MaintainGeometry</code> is typically called by a window manager once it has decided where a slave should be positioned relative to its master. <code>Tk_MaintainGeometry</code> translates the coordinates to the coordinate system of <i>slave</i>&#8216;s parent and then moves and resizes the slave appropriately. Furthermore, it remembers the desired position and creates event handlers to monitor the master and all of its ancestors up to (but not including) the slave&#8217;s parent. If any of these windows is moved, mapped, or unmapped, the slave will be adjusted so that it is mapped only when the master is mapped and its geometry relative to the master remains as specified by <i>x</i>, <i>y</i>, <i>width</i>, and <i>height</i>. </p>
<p> When a window manager relinquishes control over a window, or if it decides that it does not want the window to appear on the screen under any conditions, it calls <code>Tk_UnmaintainGeometry</code>. <code>Tk_UnmaintainGeometry</code> unmaps the window and cancels any previous calls to <code>Tk_MaintainGeometry</code> for the <i>master</i>&#8211;<i>slave</i> pair, so that the slave&#8217;s geometry and mapped state are no longer maintained automatically. <code>Tk_UnmaintainGeometry</code> need not be called by a geometry manager if the slave, the master, or any of the master&#8217;s ancestors is destroyed: Tk will call it automatically. </p>
<p> If <code>Tk_MaintainGeometry</code> is called repeatedly for the same <i>master</i>&#8211;<i>slave</i> pair, the information from the most recent call supersedes any older information. If <code>Tk_UnmaintainGeometry</code> is called for a <i>master</i>&#8211;<i>slave</i> pair that is is not currently managed, the call has no effect.</p>
<h2>Keywords</h2>
<p>geometry manager, map, master, parent, position, slave, unmap</p>
