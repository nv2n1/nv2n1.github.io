---
title: "amtape(8)"
name: "amtape"
section: "8"
letter: "a"
url: "/docs/linux/man/8-amtape/"
description: "amtape – Control Amanda changers"
---

<p>amtape &#8211; Control Amanda changers</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>amtape</code> [<code>-o</code>&nbsp;<wbr><i>configoption</i>&#8230;] <i>config</i> <i>subcommand</i> [<i>subcommand_options</i>&#8230;]</dl>
<h2>Description</h2>
<p><code>Amtape</code></p>
<dd>is the command-line interface to Amanda&#8217;s tape changers (<code><a href="/docs/linux/man/7-amanda-changers/">amanda-changers</a></code>(7)) and to the taperscan algorithm (<code><a href="/docs/linux/man/7-amanda-taperscan/">amanda-taperscan</a></code>(7)). </p>
<p> Tape changers maintain a notion of the <i>current</i> slot for each configuration. This may or may not correspond to an actual physical state of the device, but is used by some taperscan algorithms to minimize searching through the slots. </p>
<p> Amtape uses the default changer. To use a different changer, use the config override option, e.g., <code>-otpchanger=otherchanger</code>.</p>
<h2>Subcommands</h2>
<p><code>label</code> <i>label</i></p>
<dl>
<dd>Search for and load the Amanda tape with label [label], also setting the current slot.</dl>
<p> <code>slot</code> <i>slot</i></p>
<dl>
<dd>Load the volume in the given slot, also setting the current slot. The slot names <code>current</code>, <code>next</code>, <code>first</code>, and <code>last</code> have special meaning.</dl>
<p> <code>current</code></p>
<dl>
<dd>Shorthand for <code>slot</code> current.</dl>
<p> <code>inventory</code></p>
<dl>
<dd>Show the contents of all slots, based on the changer&#8217;s cached metadata. This is a quick operation as it does not load or unload any volumes, but is not supported by all changers.</dl>
<p> <code>show</code> [slots]</p>
<dl>
<dd>Show the contents of all slots (or listed slots) by loading each slot and reading its label. This can be very slow. The slots arguments is of the form 1,3-5,7.</dl>
<p> <code>reset</code></p>
<dl>
<dd>Reset the changer to a known state. This subcommand is intended to clear any unknown and potentially incorrect state the changer may have stored.</dl>
<p> <code>eject</code> [<i>drive</i>]</p>
<dl>
<dd>Eject the tape currently in the drive. This only applies to some changers. Specify a drive (by drive number) if more than one drive is available.</dl>
<p> <code>clean</code> [<i>drive</i>]</p>
<dl>
<dd>If a cleaning tape is defined for the changer, used it to clean the specified drive. The [drive] is optional if the changer only has one drive.</dl>
<p> <code>taper</code></p>
<dl>
<dd>Run the taperscan algorithm (see <code><a href="/docs/linux/man/7-amanda-taperscan/">amanda-taperscan</a></code>(7)), displaying information about the progress of the scan.</dl>
<p> <code>update</code> [what]</p>
<dl>
<dd>Update changer state. Consult <code><a href="/docs/linux/man/7-amanda-changers/">amanda-changers</a></code>(7) for changer-specific details on the format of what.</dl>
<p> <code>-o </code><i>configoption</i></p>
<dl>
<dd>See the &quot;CONFIGURATION OVERRIDE&quot; section in <code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8).</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/7-amanda-changers/">amanda-changers</a></code>(7), <code><a href="/docs/linux/man/7-amanda-taperscan/">amanda-taperscan</a></code>(7), <code><a href="/docs/linux/man/7-amanda-devices/">amanda-devices</a></code>(7) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Authors</h2>
<p><code>Dustin J. Mitchell</code> &lt;dustin [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>
<p> <code>James da Silva</code> &lt;jds [at] amanda.org&gt; </p>
<p> <code>Stefan G. Weichinger</code> &lt;sgw [at] amanda.org&gt;</p>
