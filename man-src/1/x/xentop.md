---
title: "xentop(1)"
name: "xentop"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xentop/"
description: "xentop – displays real-time information about a Xen system and domains"
---

<h2>NAME</h2>
<p> <code>xentop</code> &#8211; displays real-time information about a Xen system and domains </p>
<h2>SYNOPSIS</h2>
<p> <code>xentop</code> [<code>-h</code>] [<code>-V</code>] [<code>-d</code>SECONDS] [<code>-n</code>] [<code>-r</code>] [<code>-v</code>] [<code>-b</code>] [<code>-i</code>ITERATIONS] </p>
<h2>DESCRIPTION</h2>
<p> <code>xentop</code> displays information about the Xen system and domains, in a continually-updating manner. Command-line options and interactive commands can change the detail and format of the information displayed by <code>xentop</code>. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> display help and exit</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> output version information and exit</p>
<dt><code>-d</code>, <code>&#8211;delay</code>=<i>SECONDS</i></p>
<dd> seconds between updates (default 3)</p>
<dt><code>-n</code>, <code>&#8211;networks</code></p>
<dd> output network information</p>
<dt><code>-x</code>, <code>&#8211;vbds</code></p>
<dd> output vbd block device data</p>
<dt><code>-r</code>, <code>&#8211;repeat-header</code></p>
<dd> repeat table header before each domain</p>
<dt><code>-v</code>, <code>&#8211;vcpus</code></p>
<dd> output VCPU data</p>
<dt><code>-b</code>, <code>&#8211;batch</code></p>
<dd> output data in batch mode (to stdout)</p>
<dt><code>-i</code>, <code>&#8211;iterations</code>=<i>ITERATIONS</i></p>
<dd> maximum number of iterations xentop should produce before ending </p>
</dl>
<h2>INTERACTIVE COMMANDS</h2>
<p> All interactive commands are case-insensitive.</p>
<dl>
<dt><code>D</code></p>
<dd> set delay between updates</p>
<dt><code>N</code></p>
<dd> toggle display of network information</p>
<dt><code>Q, Esc</code></p>
<dd> quit</p>
<dt><code>R</code></p>
<dd> toggle table header before each domain</p>
<dt><code>S</code></p>
<dd> cycle sort order</p>
<dt><code>V</code></p>
<dd> toggle display of VCPU information</p>
<dt><code>Arrows</code></p>
<dd> scroll domain display </p>
</dl>
<h2>AUTHORS</h2>
<p> Written by Judy Fischbach, David Hendricks, and Josh Triplett </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;xen-tools [at] lists.xensource.com&gt;. </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2005 International Business Machines Corp<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>Index</h2>
