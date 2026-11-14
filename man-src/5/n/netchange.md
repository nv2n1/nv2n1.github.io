---
title: "netchange(5)"
name: "netchange"
section: "5"
letter: "n"
url: "/docs/linux/man/5-netchange/"
description: "netchange – format of netchange files read by irsim."
---

<p>netchange &#8211; format of netchange files read by irsim.</p>
<h2>Description</h2>
<p>A <code>netchange</code> file consists of a series of lines, each of which begins with a key letter. The key letter beginning a line determines how the remainder of the line is interpreted. The following are the list of key letters understood.</p>
<dl>
<dt><code>| </code><i>any text</i></p>
<dd>Lines beginning with a vertical bar are treated as comments and ignored by the program.</p>
<dt><code>a</code>dd<i> type gate source drain length width [area]</i></p>
<dd>Add a new transistor of <i>type</i> to the network. Currently, <i>type</i> may be:</p>
<dl>
<dd>
<dl>
<dd>
<dl>
<dt><code>n</code></p>
<dd>n-channel enhancement transistor.</p>
<dt><code>p</code></p>
<dd>p-channel enhancement transistor.</p>
<dt><code>d</code></p>
<dd>depletion transistor (for NMOS).</dl>
</dl>
<p> The names of the nodes to which the gate, source, and drain of the transistor are connected are given by <i>gate,</i> <i>source,</i> and <i>drain</i> respectively. The length and width of the transistor are given by <i>length</i> and <i>width</i> respectively. The <i>area</i> parameter, if given, will use that number as the area for calculating the gate capacitance. <i>Length</i> and <i>width</i> should be given in lambda units, <i>area</i> should be in lambda `units, these&#8217; will internally be multiplied by the LAMBDA factor from the configuration (.prm) file.</dl>
<dt><code>d</code>elete<i> type gate source drain length width [area]</i></p>
<dd>Delete an existing transistor from the net. All the parameters have the same meaning as for the <code>a</code>dd command.</p>
<dt><code>m</code>ove <i>type gate source drain length width [area] g s d</i></p>
<dd>Move an existing transistor to a new location the net. <i>type, gate, source, drain, length, width, and area</i> have the same meaning as for the <code>a</code>dd command. <i>g, s,</i> and <i>d</i> are the names of nodes to which the gate, source and drain should be connected. If a particular terminal(s) is not to be re-connected, the name can be specified using an &quot;*&quot;. Any or all of <i>g, s,</i> and <i>d</i> may be &quot;*&quot;. For example, to move the gate of an n-channel transistor from node <i>old</i> to <i>new</i> the following command would be used:</p>
<dt> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>m n old src_node drn_node 4 2.2 new * *</code></p>
<dd>
<dd>Note that the <i>drain</i> and <i>source</i> terminals, and the <i>g</i> and <i>s</i> terminals are interchangeable; the simulator will know if these are swapped. So the last example could also have been written:</p>
<dt> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>m n old drn_node src_node 4 2.2 new * *</code></p>
<dt><code>c</code>apacitance <i>node value</i></p>
<dd>
<dd>Change the capacitance of a node by <i>value</i> picofarads. <i>Value</i> may be negative, thereby decreasing the node&#8217;s capacitance. <i>Node</i> is the node name.</p>
<dt><code>N </code><i>node metal-area poly-area diff-area diff-perimeter</i></p>
<dd>Change the capacitance of <i>node</i> using the area and perimeter information of the metal, polysilicon, and diffusion layers. All the parameters should be in lambda (or lambda `for areas) units, they will internally&#8217; be converted to the appropriate capacitance as defined in the configuration file. The values can be negative to decrease the capacitance.</p>
<dt><code>M </code><i>node M2A M2P MA MP PA PP DA DP PDA PDP</i></p>
<dd>Change the capacitance of <i>node,</i> using the following geometrical information:</dl>
<dl>
<dd>
<dl>
<dd>
<dl>
<dt><i>M2A</i></p>
<dd>area of 2nd-level metal</p>
<dt><i>M2P</i></p>
<dd>perimeter of 2nd-level metal</p>
<dt><i>MA</i></p>
<dd>area of 1st-level metal</p>
<dt><i>MP</i></p>
<dd>perimeter of 1st-level metal</p>
<dt><i>PA</i></p>
<dd>area of polysilicon</p>
<dt><i>PP</i></p>
<dd>perimeter of polysilicon</p>
<dt><i>DA</i></p>
<dd>area of n-diffusion</p>
<dt><i>DP</i></p>
<dd>perimeter of n-diffusion</p>
<dt><i>PDA</i></p>
<dd>area of p-diffusion</p>
<dt><i>PDP</i></p>
<dd>perimeter of p-diffusion</dl>
</dl>
<p> All perimeter values should be in lambda units, area values should be in lambda `units.&#8217; The perimeter measures are half of the actual total perimeter (i.e., they are the sum of the lengths of the top and one side). Again, the values may be negative to decrease the capacitance of the node.</dl>
<dl>
<dt><code>t</code>hreshold <i>node low high</i></p>
<dd>Change the threhsold voltages of <i>node.</i> <i>Low</i> and <i>high</i> should be in normalized voltage units (i.e. floating-point numbers in the range 0.0 to 1.0).</p>
<dt><code>D</code>elay <i>node tplh tphl</i></p>
<dd>Change the delays for <i>node</i> to be <i>tplh</i> nanoseconds for low-to-high transistions, and <i>tphl</i> ns. for high-to-low transistions. These should be absolute numbers, not relative increments/dercrements.</p>
<dt><code>NOTE:</code></p>
<dd>For all commands, only the first letter is significant, the rest of the string will be ignored. They are only shown here for clarity. </p>
<h2>Bugs</h2>
<p>This is an experimental interface for the incremental simulator and is very likely to change in the future. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-irsim/">irsim</a>(5) <a href="/docs/linux/man/5-sim/">sim</a>(5) <a href="/docs/linux/man/1-presim/">presim</a>(1) </p>
