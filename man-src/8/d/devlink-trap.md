---
title: "devlink-trap(8)"
name: "devlink-trap"
section: "8"
letter: "d"
url: "/docs/linux/man/8-devlink-trap/"
description: "devlink-trap – devlink trap configuration"
---

<p>devlink-trap &#8211; devlink trap configuration</p>
<h2>Synopsis</h2>
<pre><code>devlink

[ OPTIONS ]

trap

{ COMMAND |

    help }

OPTIONS := {

    -v[erbose] |
    -s[tatistics] }</code></pre>
<p> <code>devlink trap show</code> [ <i>DEV</i> <code>trap</code> <i>TRAP</i> ]<br />
 <code>devlink trap set </code><i>DEV</i><code> trap </code><i>TRAP</i> [ <code>action</code> { <code>trap</code> | <code>drop</code> | <code>mirror</code> } ]<br />
 <code>devlink trap group show</code> [ <i>DEV</i> <code>group</code> <i>GROUP</i> ]<br />
 <code>devlink trap group set </code><i>DEV</i><code> group </code><i>GROUP</i> [ <code>action</code> { <code>trap</code> | <code>drop</code> | <code>mirror</code> } ]<br />
 [ <code>policer</code> <i>POLICER </i><code>]</code> [ <code>nopolicer</code> ]<br />
 <code>devlink trap policer set </code><i>DEV</i><code> policer </code><i>POLICER</i> [ <code>rate</code> <i>RATE </i>] [ <code>burst</code> <i>BURST </i>]<br />
 <code>devlink trap help</code> </p>
<h2>Description</h2>
<h3>devlink trap show &#8211; display available packet traps and their attributes</h3>
<p><i>DEV</i> &#8211; specifies the devlink device from which to show packet traps. If this argument is omitted all packet traps of all devices are listed. <code>trap </code><i>TRAP</i> &#8211; specifies the packet trap. Only applicable if a devlink device is also specified.</p>
<h3>devlink trap set &#8211; set attributes of a packet trap</h3>
<p><i>DEV</i> &#8211; specifies the devlink device the packet trap belongs to. <code>trap </code><i>TRAP</i> &#8211; specifies the packet trap.</p>
<dl>
<dt><code>action</code> { <code>trap</code> | <code>drop</code> | <code>mirror</code> }</p>
<dd>packet trap action. <i>trap</i> &#8211; the sole copy of the packet is sent to the CPU. <i>drop</i> &#8211; the packet is dropped by the underlying device and a copy is not sent to the CPU. <i>mirror</i> &#8211; the packet is forwarded by the underlying device and a copy is sent to the CPU.</dl>
<h3>devlink trap group show &#8211; display available packet trap groups and their attributes</h3>
<p><i>DEV</i> &#8211; specifies the devlink device from which to show packet trap groups. If this argument is omitted all packet trap groups of all devices are listed. <code>group </code><i>GROUP</i> &#8211; specifies the packet trap group. Only applicable if a devlink device is also specified.</p>
<h3>devlink trap group set &#8211; set attributes of a packet trap group</h3>
<p><i>DEV</i> &#8211; specifies the devlink device the packet trap group belongs to. <code>group </code><i>GROUP</i> &#8211; specifies the packet trap group.</p>
<dl>
<dt><code>action</code> { <code>trap</code> | <code>drop</code> | <code>mirror</code> }</p>
<dd>packet trap action. The action is set for all the packet traps member in the trap group. The actions of non-drop traps cannot be changed and are thus skipped.</p>
<dt><code>policer</code><i> POLICER</i></p>
<dd>packet trap policer. The policer to bind to the packet trap group. A value of &quot;0&quot; will unbind the currently bound policer.</p>
<dt><code>nopolicer</code></p>
<dd>Unbind packet trap policer from the packet trap group.</dl>
<h3>devlink trap policer set &#8211; set attributes of packet trap policer</h3>
<p><i>DEV</i> &#8211; specifies the devlink device the packet trap policer belongs to. <code>policer </code><i>POLICER</i> &#8211; specifies the packet trap policer. <code>rate</code><i> RATE </i> &#8211; packet trap policer rate in packets per second. <code>burst</code><i> BURST </i> &#8211; packet trap policer burst size in packets. </p>
<h2>Examples</h2>
<p>devlink trap show</p>
<dl>
<dd>List available packet traps.</dl>
<p> devlink trap group show</p>
<dl>
<dd>List available packet trap groups.</dl>
<p> devlink -vs trap show pci/0000:01:00.0 trap source_mac_is_multicast</p>
<dl>
<dd>Show attributes and statistics of a specific packet trap.</dl>
<p> devlink -s trap group show pci/0000:01:00.0 group l2_drops</p>
<dl>
<dd>Show attributes and statistics of a specific packet trap group.</dl>
<p> devlink trap set pci/0000:01:00.0 trap source_mac_is_multicast action trap</p>
<dl>
<dd>Set the action of a specific packet trap to &#8216;trap&#8217;.</dl>
<p> devlink trap policer show</p>
<dl>
<dd>List available packet trap policers.</dl>
<p> devlink -s trap policer show pci/0000:01:00.0 policer 1</p>
<dl>
<dd>Show attributes and statistics of a specific packet trap policer.</dl>
<p> devlink trap policer set pci/0000:01:00.0 policer 1 rate 1000 burst 128</p>
<dl>
<dd>Set the rate and burst size of a specific packet trap policer.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-devlink/">devlink</a></code>(8), <code><a href="/docs/linux/man/8-devlink-dev/">devlink-dev</a></code>(8), <code><a href="/docs/linux/man/8-devlink-monitor/">devlink-monitor</a></code>(8), </p>
<h2>Author</h2>
<p>Ido Schimmel &lt;idosch [at] mellanox.com&gt;</p>
