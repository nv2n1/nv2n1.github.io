---
title: "dlys(5)"
name: "dlys"
section: "5"
letter: "d"
url: "/docs/linux/man/5-dlys/"
description: "dlys – format of .dlys files read by the SCALD simulator and timing verifier"
---

<p>dlys &#8211; format of .dlys files read by the SCALD simulator and timing verifier </p>
<h2>Description</h2>
<p>The SCALD simulator and timing verifier can accept information about the actual delays of wires in a circuit. This delay information is described in a <code>.dlys</code> file, which consists of a sequence of records, one for each electrical net. Each record begins with the signal name for the net (note that this is the SCALD signal name, i.e, the name given by the user to the entire net, and not usually the name of one of the pins in the net), followed by an <code>=</code>, then a comma-separated list of the terminals in the net and their associated delay, with the list terminated by a semicolon. The end of the file is marked with a second semicolon. The elements of the comma-separated list for each net take the form<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> <i>location</i><code> [</code><i>min</i><code>:</code><i>max</i><code>]</code> where <i>location</i> is the full hierarchical SCALD name of the physical pin to which the delay is computed, and <i>min</i> and <i>max</i> are the best-case and worst-case wire delay in nanoseconds (both are floating-point numbers). The assumption is that only a single driver exists per net, so all delays are computed from this driver. If a net has multiple drivers, then the interpretation of delays is up to the program reading this file (e.g, <i>min</i> delays are taken from the fastest driver, <i>max</i> from the slowest). Here is an example <code>.dlys</code> file:  Although it is not good practice, it is possible to omit the actual pin names from the <i>location</i> names and only give the path to the part; the example above shows several cases where the final pin name is missing. Since the timing verifier and simulator have the original SCALD netlist available, they are usually able to use the signal name to determine the net, and then use the part&#8217;s path to identify which pin of the net is meant. This is accurate when a net connects to at most one pin per part; if it connects to more than one pin per part then there is ambiguity over which pin is meant. Usually, though, this ambiguity results in only a small inaccuracy, since the delay to different pins on the same part is usually similar. Also, if delay is capacitive, the delay to all pins in a net will be the same anyway, so there is no inaccuracy. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-ext2dlys/">ext2dlys</a>(1), <a href="/docs/linux/man/5-ext/">ext</a>(5), <a href="/docs/linux/man/5-sim/">sim</a>(5) </p>
<h2>Bugs</h2>
<p>There should be some way to specify which pins are drivers and which are receivers in a net. The ability to omit pin names is dangerous; although it usually works it can introduce large inaccuracies when the parts are large compared to the sizes of the wires used to connect them, as might be the case on a silicon PCB. </p>
