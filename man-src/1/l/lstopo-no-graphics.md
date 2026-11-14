---
title: "lstopo-no-graphics(1)"
name: "lstopo-no-graphics"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lstopo-no-graphics/"
description: "lstopo, lstopo-no-graphics, hwloc-ls – Show the topology of the system"
---

<h2>NAME</h2>
<p> lstopo, lstopo-no-graphics, hwloc-ls &#8211; Show the topology of the system</p>
<h2>SYNOPSIS</h2>
<p> <code>lstopo</code> [ <i>options </i>]&#8230; [ <i>filename </i>] </p>
<p> <code>lstopo-no-graphics</code> [ <i>options </i>]&#8230; [ <i>filename </i>] </p>
<p> <code>hwloc-ls</code> [ <i>options </i>]&#8230; [ <i>filename </i>] </p>
<p> Note that <a href="/docs/linux/man/7-hwloc/">hwloc</a>(7) provides a detailed explanation of the hwloc system; it should be read before reading this man page</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;of</code> &lt;format&gt;, <code>&#8211;output-format</code> &lt;format&gt;</p>
<dd> Enforce the output in the given format. See the OUTPUT FORMATS section below.</p>
<dt><code>-i</code> &lt;file&gt;, <code>&#8211;input</code> &lt;file&gt;</p>
<dd> Read topology from XML file &lt;file&gt; (instead of discovering the topology on the local machine). If &lt;file&gt; is &quot;-&quot;, the standard input is used. XML support must have been compiled in to hwloc for this option to be usable.</p>
<dt><code>-i</code> &lt;directory&gt;, <code>&#8211;input</code> &lt;directory&gt;</p>
<dd> Read topology from the chroot specified by &lt;directory&gt; (instead of discovering the topology on the local machine). This option is generally only available on Linux. The chroot was usually created by gathering another machine topology with hwloc-gather-topology.</p>
<dt><code>-i</code> &lt;specification&gt;, <code>&#8211;input</code> &lt;specification&gt;</p>
<dd> Simulate a fake hierarchy (instead of discovering the topology on the local machine). If &lt;specification&gt; is &quot;node:2 pu:3&quot;, the topology will contain two NUMA nodes with 3 processing units in each of them. The &lt;specification&gt; string must end with a number of PUs.</p>
<dt><code>&#8211;if</code> &lt;format&gt;, <code>&#8211;input-format</code> &lt;format&gt;</p>
<dd> Enforce the input in the given format, among <code>xml</code>, <code>fsroot</code> and <code>synthetic</code>.</p>
<dt><code>&#8211;export-synthetic-flags</code> &lt;flags&gt;</p>
<dd> Enforce flags when exporting to the synthetic format. These flags are passed to <i>hwloc_topology_export_synthetic()</i>. A value of 2 reverts to the format of hwloc v1.9. A value of 3 reverts to the original minimalistic format (before v1.9).</p>
<dt><code>-v</code> <code>&#8211;verbose</code></p>
<dd> Include additional detail. The hwloc-info tool may be used to display even more information about specific objects.</p>
<dt><code>-s</code> <code>&#8211;silent</code></p>
<dd> Reduce the amount of details to show.</p>
<dt><code>-f</code> <code>&#8211;force</code></p>
<dd> If the destination file already exists, overwrite it.</p>
<dt><code>-l</code> <code>&#8211;logical</code></p>
<dd> Display hwloc logical indexes instead of physical/OS indexes (default for console output). These indexes are prefixed with &quot;L#&quot;. The physical indexes of some objects (PU and Node by default, all objects if verbose) will appear as object attribute &quot;P#&#8230;&quot;.</p>
<dt><code>-p</code> <code>&#8211;physical</code></p>
<dd> Display OS/physical indexes instead of hwloc logical indexes (default for graphical output). These indexes are prefixed with &quot;P#&quot; instead of &quot;L#&quot; in the console output.</p>
<dt><code>-c</code> <code>&#8211;cpuset</code></p>
<dd> Display the cpuset of each object.</p>
<dt><code>-C</code> <code>&#8211;cpuset-only</code></p>
<dd> Only display the cpuset of each object; do not display anything else about the object.</p>
<dt><code>&#8211;taskset</code></p>
<dd> Show CPU set strings in the format recognized by the taskset command-line program instead of hwloc-specific CPU set string format. This option should be combined with <code>&#8211;cpuset</code> or <code>&#8211;cpuset-only</code>, otherwise it will imply <code>&#8211;cpuset</code>.</p>
<dt><code>&#8211;only</code> &lt;type&gt;</p>
<dd> Only show objects of the given type in the textual output.</p>
<dt><code>&#8211;ignore</code> &lt;type&gt;</p>
<dd> Ignore all objects of type &lt;type&gt; in the topology. hwloc supports ignoring any type except PUs and I/O devices. However lstopo still offers PU ignoring by hiding PU objects in the graphical and textual outputs. Note that PU may not be ignored in the XML output. Note also that the top-level object type cannot be ignored (usually Machine or System).</p>
<dt><code>&#8211;no-caches</code></p>
<dd> Do not show caches.</p>
<dt><code>&#8211;no-useless-caches</code></p>
<dd> Do not show caches which do not have a hierarchical impact. This calls hwloc_topology_ignore_type_keep_structure() for cache objects.</p>
<dt><code>&#8211;no-icaches</code></p>
<dd> Do not show Instruction caches, only Data and Unified caches are displayed.</p>
<dt><code>&#8211;whole-system</code></p>
<dd> Do not consider administration limitations.</p>
<dt><code>&#8211;merge</code></p>
<dd> Do not show levels that do not have a hierarchical impact. This calls hwloc_topology_ignore_all_keep_structure().</p>
<dt><code>&#8211;no-collapse</code></p>
<dd> Do not collapse identical PCI devices. By default, identical sibling PCI devices (such as many virtual functions inside a single physical device) are collapsed.</p>
<dt><code>&#8211;restrict</code> &lt;cpuset&gt;</p>
<dd> Restrict the topology to the given cpuset.</p>
<dt><code>&#8211;restrict</code> binding</p>
<dd> Restrict the topology to the current process binding. This option requires the use of the actual current machine topology (or any other topology with <code>&#8211;thissystem</code> or with HWLOC_THISSYSTEM set to 1 in the environment).</p>
<dt><code>&#8211;restrict-flags</code> &lt;flags&gt;</p>
<dd> Enforce flags when restricting the topology. The default is <code>0</code>. These flags are passed to <i>hwloc_topology_restrict()</i>.</p>
<dt><code>&#8211;no-io</p>
<dd> Do not show any I/O device or bridge. By default, common devices (GPUs, NICs, block devices, &#8230;) and interesting bridges are shown.</p>
<dt>&#8211;no-bridges</p>
<dd> Do not show any I/O bridge except hostbridges. By default, common devices (GPUs, NICs, block devices, &#8230;) and interesting bridges are shown.</p>
<dt>&#8211;whole-io</p>
<dd> Show all I/O devices and bridges. By default, only common devices (GPUs, NICs, block devices, &#8230;) and interesting bridges are shown.</p>
<dt>&#8211;thissystem</code></p>
<dd> Assume that the selected backend provides the topology for the system on which we are running. This is useful when using <code>&#8211;restrict</code> binding and loading a custom topology such as an XML file.</p>
<dt><code>&#8211;pid</code> &lt;pid&gt;</p>
<dd> Detect topology as seen by process &lt;pid&gt;, i.e. as if process &lt;pid&gt; did the discovery itself. Note that this can for instance change the set of allowed processors. Also show this process current CPU binding by marking the corresponding PUs (in Green in the graphical output, see the COLORS section below, or by appending <i>(binding)</i> to the verbose text output). If 0 is given as pid, the current binding for the lstopo process will be shown.</p>
<dt><code>&#8211;ps</code> <code>&#8211;top</code></p>
<dd> Show existing processes as misc objects in the output. To avoid uselessly cluttering the output, only processes that are restricted to some part of the machine are shown. On Linux, kernel threads are not shown. If many processes appear, the output may become hard to read anyway, making the hwloc-ps program more practical.</p>
<dt><code>&#8211;fontsize</code> &lt;size&gt;</p>
<dd> Set size of text font.</p>
<dt><code>&#8211;gridsize</code> &lt;size&gt;</p>
<dd> Set size of margin between elements.</p>
<dt><code>&#8211;horiz</code>, <code>&#8211;horiz</code>=&lt;type1,&#8230;&gt;</p>
<dd> Horizontal graphical layout instead of nearly 4/3 ratio. If a comma-separated list of types is given, the layout only applies to the corresponding containers.</p>
<dt><code>&#8211;vert</code>, <code>&#8211;vert</code>=&lt;type1,&#8230;&gt;</p>
<dd> Vertical graphical layout instead of nearly 4/3 ratio. If a comma-separated list of types is given, the layout only applies to the corresponding containers.</p>
<dt><code>&#8211;rect</code>, <code>&#8211;rect</code>=&lt;type1,&#8230;&gt;</p>
<dd> Rectangular graphical layout with nearly 4/3 ratio, including when placing NUMA nodes. If a comma-separated list of types is given, the layout only applies to the corresponding containers.</p>
<dt><code>&#8211;no-legend</code></p>
<dd> Remove the text legend at the bottom.</p>
<dt><code>&#8211;append-legend &lt;line&gt;</p>
<dd> Append the line of text to the bottom of the legend in graphical mode. If the line is too long, it will be truncated in the output. If adding multiple lines, each line should be given separately by passing this option multiple times.</p>
<dt>&#8211;version</code></p>
<dd> Report version and exit.</dl>
<h2>DESCRIPTION</h2>
<p> lstopo and lstopo-no-graphics are capable of displaying a topological map of the system in a variety of different output formats. The only difference between lstopo and lstopo-no-graphics is that graphical outputs are only supported by lstopo, to reduce dependencies on external libraries. hwloc-ls is identical to lstopo-no-graphics. </p>
<p> The filename specified directly implies the output format that will be used; see the OUTPUT FORMATS section, below. Output formats that support color will indicate specific characteristics about individual CPUs by their color; see the COLORS section, below.</p>
<h2>OUTPUT FORMATS</h2>
<p> By default, if no output filename is specific, the output is sent to a graphical window if possible in the current environment (DISPLAY environment variable set on Unix, etc.). Otherwise, a text summary is displayed in the console. </p>
<p> The filename on the command line usually determines the format of the output. There are a few filenames that indicate specific output formats and devices (e.g., a filename of &quot;-&quot; will output a text summary to stdout), but most filenames indicate the desired output format by their suffix (e.g., &quot;topo.png&quot; will output a PNG-format file). </p>
<p> The format of the output may also be changed with &quot;&#8211;of&quot;. For instance, &quot;&#8211;of pdf&quot; will generate a PDF-format file on the standard output, while &quot;&#8211;of fig toto&quot; will output a Xfig-format file named &quot;toto&quot;. </p>
<p> The list of currently supported formats is given below. Any of them may be used with &quot;&#8211;of&quot; or as a filename suffix.</p>
<dl>
<dt><code>default</code></p>
<dd> Send the output to a window or to the console depending on the environment.</p>
<dt><code>console</code></p>
<dd> Send a text summary to stdout. Binding, unallowed or offline processors are only annotated in this mode if verbose; see the COLORS section, below.</p>
<dt><code>ascii</code></p>
<dd> Output an ASCII art representation of the map (formerly called <code>txt</code>). If outputting to stdout and if colors are supported on the terminal, the output will be colorized.</p>
<dt><code>fig</code></p>
<dd> Output a representation of the map that can be loaded in Xfig.</p>
<dt><code>pdf</code></p>
<dd> If lstopo was compiled with the proper support, lstopo outputs a PDF representation of the map.</p>
<dt><code>ps</code></p>
<dd> If lstopo was compiled with the proper support, lstopo outputs a Postscript representation of the map.</p>
<dt><code>png</code></p>
<dd> If lstopo was compiled with the proper support, lstopo outputs a PNG representation of the map.</p>
<dt><code>svg</code></p>
<dd> If lstopo was compiled with the proper support, lstopo outputs an SVG representation of the map.</p>
<dt><code>synthetic</code></p>
<dd> If the topology is symmetric (which requires that the root object has its symmetric_subtree field set), lstopo outputs a synthetic description string. This output may be reused as an input synthetic topology description later. Note that I/O devices often cause topology asymmetry. Adding &#8211;no-io may then be useful when the synthetic export fails. See also the Synthetic topologies section in the documentation.</p>
<dt><code>xml</code></p>
<dd> If lstopo was compiled with the proper support, lstopo outputs an XML representation of the map. It may be reused later, even on another machine, with lstopo &#8211;input, the HWLOC_XMLFILE environment variable, or the hwloc_topology_set_xml() function. </p>
</dl>
<p> The following special names may be used:</p>
<dl>
<dt><code>&#8211;</code></p>
<dd> Send a text summary to stdout.</p>
<dt><code>/dev/stdout</code></p>
<dd> Send a text summary to stdout. It is effectively the same as specifying &quot;-&quot;.</p>
<dt><code>-.&lt;format&gt;</code></p>
<dd> If the entire filename is &quot;-.&lt;format&gt;&quot;, lstopo behaves as if &quot;&#8211;of &lt;format&gt; -&quot; was given, which means a file of the given format is sent to the standard output. </p>
</dl>
<p> See the output of &quot;lstopo &#8211;help&quot; for a specific list of what graphical output formats are supported in your hwloc installation.</p>
<h2>COLORS</h2>
<p> Individual CPUs are colored in the graphical output formats to indicate different characteristics:</p>
<dl>
<dt>Green</p>
<dd> The topology is reported as seen by a specific process (see <code>&#8211;pid</code>), and the given CPU is in this process CPU binding mask.</p>
<dt>White</p>
<dd> The CPU is in the allowed set (see below). If the topology is reported as seen by a specific process (see <code>&#8211;pid</code>), the given CPU is also not in this process CPU binding mask.</p>
<dt>Red</p>
<dd> The CPU is not in the allowed set (see below).</p>
<dt>Black</p>
<dd> The CPU is offline (not all OS&#8217;s support displaying offline CPUs).</dl>
<p> The &quot;allowed set&quot; is the set of CPUs to which the current process is allowed to bind. The allowed set is usually either inherited from the parent process or set by administrative qpolicies on the system. Linux cpusets are one example of limiting the allowed set for a process and its children to be less than the full set of CPUs on the system. </p>
<p> Different processes may therefore have different CPUs in the allowed set. Hence, invoking lstopo in different contexts and/or as different users may display different colors for the same individual CPUs (e.g., running lstopo in one context may show a specific CPU as red, but running lstopo in a different context may show the same CPU as white). </p>
<p> Some lstopo output modes, e.g. the console mode (default non-graphical output), do not support colors at all. The console mode displays the above characteristics by appending text to each PU line if verbose messages are enabled.</p>
<h2>CUSTOM COLORS</h2>
<p> The color of each object in the graphical output may be enforced by specifying a &quot;lstopoStyle&quot; info attribute in that object. Its value should be a semi-colon separated list of &quot;&lt;attribute&gt;=#rrggbb&quot; where rr, gg and bb are the RGB components of a color, each between 0 and 255, in hexadecimal (00 to ff). &lt;attribute&gt; may be</p>
<dl>
<dt><code>Background</code></p>
<dd> Sets the background color of the main object box.</p>
<dt><code>Background2</code></p>
<dd> Sets the background color of the additional box for the object, for instance the memory box inside a NUMA node box.</p>
<dt><code>Text</code></p>
<dd> Sets the color of the text showing the object name, type, index, etc.</p>
<dt><code>Text2</p>
<dd> Sets the color of the additional text near the object, for instance the link speed behind a PCI bridge.</dl>
<p> The &quot;lstopoStyle&quot; info may be added to a temporarily-saved XML topologies with hwloc-annotate, or with hwloc_obj_add_info(). For instance, to display all core objects in blue (with white names): </p>
<p>&nbsp;<wbr>lstopo save.xml<br />
&nbsp;<wbr>hwloc-annotate save.xml save.xml core:all info lstopoStyle&nbsp;<wbr>&quot;Background=#0000ff;Text=#ffffff&quot;<br />
&nbsp;<wbr>lstopo -i save.xml </code></p>
<h2>LAYOUT</h2>
<p> In its graphical output, lstopo uses simple rectangular heuristics to try to achieve a 4/3 ratio between width and height. However, in the particular case of NUMA nodes, the layout is always a flat rectangle, to avoid letting the user believe any particular NUMA topology (lstopo is not able to render that yet). The layout of a level may be changed with &#8211;vert, &#8211;horiz, and &#8211;rect.</p>
<h2>EXAMPLES</h2>
<p> To display the machine topology in textual mode: </p>
<p>&nbsp;<wbr>lstopo-no-graphics </p>
<p> To display the machine topology in ascii-art mode: </p>
<p>&nbsp;<wbr>lstopo-no-graphics -.ascii </p>
<p> To display in graphical mode (assuming that the DISPLAY environment variable is set to a relevant value): </p>
<p>&nbsp;<wbr>lstopo </p>
<p> To export the topology to a PNG file: </p>
<p>&nbsp;<wbr>lstopo file.png </p>
<p> To export an XML file on a machine and later display the corresponding graphical output on another machine: </p>
<p>&nbsp;<wbr>machine1$&nbsp;<wbr>lstopo file.xml<br />
&nbsp;<wbr>&lt;transfer file.xml from machine1 to machine2&gt;<br />
&nbsp;<wbr>machine2$&nbsp;<wbr>lstopo &#8211;input file.xml </p>
<p> To save the current machine topology to XML and later reload it faster while still considering it as the current machine: </p>
<p>$&nbsp;<wbr>lstopo file.xml<br />
&lt;&#8230;&gt;<br />
$&nbsp;<wbr>lstopo &#8211;input file.xml &#8211;thissystem </p>
<p> To restrict an XML topology to only physical processors 0, 1, 4 and 5: </p>
<p>&nbsp;<wbr>lstopo &#8211;input file.xml &#8211;restrict 0x33 newfile.xml </p>
<p> To restrict an XML topology to only numa node whose logical index is 1: </p>
<p>&nbsp;<wbr>lstopo &#8211;input file.xml &#8211;restrict&nbsp;<wbr>$(hwloc-calc &#8211;input file.xml node:1)&nbsp;<wbr>newfile.xml </p>
<p> To display a summary of the topology: </p>
<p>&nbsp;<wbr>lstopo -s </p>
<p> To get more details about the topology: </p>
<p>&nbsp;<wbr>lstopo -v </p>
<p> To only show cores: </p>
<p>&nbsp;<wbr>lstopo &#8211;only core </p>
<p> To show cpusets: </p>
<p>&nbsp;<wbr>lstopo &#8211;cpuset </p>
<p> To only show the cpusets of package: </p>
<p>&nbsp;<wbr>lstopo &#8211;only package &#8211;cpuset-only </p>
<p> Simulate a fake hierarchy; this example shows with 2 NUMA nodes of 2 processor units: </p>
<p>&nbsp;<wbr>lstopo &#8211;input&nbsp;<wbr>&quot;n:2 2&quot; </p>
<p> To count the number of logical processors in the system </p>
<p>lstopo &#8211;only pu | wc -l </p>
<p> To append the kernel release and version to the graphical legend: </p>
<p>lstopo &#8211;append-legend&nbsp;<wbr>&quot;Kernel release:&nbsp;<wbr>$(uname -r)&quot;&nbsp;<wbr>&#8211;append-legend&nbsp;<wbr>&quot;Kernel version:&nbsp;<wbr>$(uname -v)&quot; </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-hwloc/">hwloc</a>(7), <a href="/docs/linux/man/1-hwloc-info/">hwloc-info</a>(1), <a href="/docs/linux/man/1-hwloc-bind/">hwloc-bind</a>(1), <a href="/docs/linux/man/1-hwloc-annotate/">hwloc-annotate</a>(1), <a href="/docs/linux/man/1-hwloc-ps/">hwloc-ps</a>(1), <a href="/docs/linux/man/1-hwloc-gather-topology/">hwloc-gather-topology</a>(1) </p>
<h2>Index</h2>
