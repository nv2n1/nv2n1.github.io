---
title: "systool(1)"
name: "systool"
section: "1"
letter: "s"
url: "/docs/linux/man/1-systool/"
description: "systool – view system device information by bus, class, and topology"
---

<h2>NAME</h2>
<p> systool &#8211; view system device information by bus, class, and topology </p>
<h2>SYNOPSIS</h2>
<p> <code>systool</code> [<i>options </i>[<i>device</i>]] </p>
<h2>DESCRIPTION</h2>
<p> Calling <code>systool</code> without parameters will present all available bus types, device classes, and root devices. </p>
<p> When <i>device</i> is supplied, the information requested by <i>options</i> is shown only for the specified device, otherwise all present devices are displayed. </p>
<p> <code>systool</code> uses APIs provided by <code>libsysfs</code> to gather information. <code>systool</code> runs only on Linux systems running kernels 2.5 or later, with the sysfs filesystem mounted. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></dt>
<dd> Show attributes of the requested resource</dd>
<dt><code>-b </code><i>bus</i></dt>
<dd> Show information for a specific bus</dd>
<dt><code>-c </code><i>class</i></dt>
<dd> Show information for a specific class</dd>
<dt><code>-d</code></dt>
<dd> Show only devices</dd>
<dt><code>-h</code></dt>
<dd> Show usage</dd>
<dt><code>-m </code><i>module_name</i></dt>
<dd> Show information for a specific module</dd>
<dt><code>-p</code></dt>
<dd> Show absolute sysfs path to the resource</dd>
<dt><code>-v</code></dt>
<dd> Show all attributes with values</dd>
<dt><code>-A </code><i>attribute</i></dt>
<dd> Show attribute value for the requested resource</dd>
<dt><code>-D</code></dt>
<dd> Show only drivers</dd>
<dt><code>-P</code></dt>
<dd> Show device&#8217;s parent </dd>
</dl>
<h2>SEE ALSO</h2>
<p> The web page of <code>libsysfs</code> at <a rel="nofollow" href="http://linux-diag.sourceforge.net/Sysfsutils.html">http://linux-diag.sourceforge.net/Sysfsutils.html</a> </p>
<h2>AUTHOR</h2>
<p> <code>systool</code> was written by Ananth Mavinakayanahalli &lt;ananth [at] in.ibm.com&gt; and Daniel Stekloff &lt;dsteklof [at] us.ibm.com&gt;. </p>
<p> This man page was contributed by Martin Pitt &lt;mpitt [at] debian.org&gt; for the Debian GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>
