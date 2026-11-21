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
<p> <code>xentop</code> [<code>-h</code>] [<code>-V</code>] [<code>-d</code>SECONDS] [<code>-n</code>] [<code>-r</code>] [<code>-v</code>] [<code>-b</code>] [<code>-i</code>ITERATIONS] </p>
<p> <code>xentop</code> displays information about the Xen system and domains, in a continually-updating manner. Command-line options and interactive commands can change the detail and format of the information displayed by <code>xentop</code>. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> display help and exit</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> output version information and exit</dd>
<dt><code>-d</code>, <code>&#8211;delay</code>=<i>SECONDS</i></dt>
<dd> seconds between updates (default 3)</dd>
<dt><code>-n</code>, <code>&#8211;networks</code></dt>
<dd> output network information</dd>
<dt><code>-x</code>, <code>&#8211;vbds</code></dt>
<dd> output vbd block device data</dd>
<dt><code>-r</code>, <code>&#8211;repeat-header</code></dt>
<dd> repeat table header before each domain</dd>
<dt><code>-v</code>, <code>&#8211;vcpus</code></dt>
<dd> output VCPU data</dd>
<dt><code>-b</code>, <code>&#8211;batch</code></dt>
<dd> output data in batch mode (to stdout)</dd>
<dt><code>-i</code>, <code>&#8211;iterations</code>=<i>ITERATIONS</i></dt>
<dd> maximum number of iterations xentop should produce before ending </dd>
</dl>
<h2>INTERACTIVE COMMANDS</h2>
<p> All interactive commands are case-insensitive.</p>
<dl>
<dt><code>D</code></dt>
<dd> set delay between updates</dd>
<dt><code>N</code></dt>
<dd> toggle display of network information</dd>
<dt><code>Q, Esc</code></dt>
<dd> quit</dd>
<dt><code>R</code></dt>
<dd> toggle table header before each domain</dd>
<dt><code>S</code></dt>
<dd> cycle sort order</dd>
<dt><code>V</code></dt>
<dd> toggle display of VCPU information</dd>
<dt><code>Arrows</code></dt>
<dd> scroll domain display </dd>
</dl>
<h2>AUTHORS</h2>
<p> Written by Judy Fischbach, David Hendricks, and Josh Triplett </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;xen-tools [at] lists.xensource.com&gt;. </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2005 International Business Machines Corp<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
