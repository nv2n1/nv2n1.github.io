---
title: "tuna(8)"
name: "tuna"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tuna/"
description: "tuna – program for tuning running processes"
---

<p>tuna &#8211; program for tuning running processes</p>
<h2>Synopsis</h2>
<p><code>tuna</code> [<i>OPTIONS</i>]</p>
<h2>Description</h2>
<p>This manual page explains the <code>tuna</code> program. The program can be used to change the attributes of application and kernel threads. <code>tuna</code> can operate on IRQs by name or number, and tasks or threads by process ID or command-line. CPUs and sets of CPUs can be specified by CPU or socket number. IRQ names and process command-lines can include wildcards. </p>
<p> <code>tuna</code> can change scheduling policy, scheduler priority and processor affinity for processes and process threads. <code>tuna</code> can also change the processor affinity for interrupts. When <code>tuna</code> is invoked without any options it starts up in its graphical interface mode. This manual page explains only the command-line options for <code>tuna</code></p>
<h2>Options</h2>
<p><code>tuna</code> has both <i>action</i> options and <i>modifier</i> options. Modifier options must be specified on the command-line before the actions they are intended to modify. Any modifier option applies to following actions on the same command-line until it is over-ridden.</p>
<dl>
<dt><i>Actions</i></dt>
<dd>
</dd><dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd>Print a list of options. <code>tuna</code> will exit after this action, ignoring the remainder of the command-line.</dd>
<dt><code>-g</code>, <code>&#8211;gui</code></dt>
<dd>Start the GUI. Actions that follow this on the command-line will be processed without waiting for the GUI to complete.</dd>
<dt><code>-a</code>, <code>&#8211;config_file_apply=profilename</code></dt>
<dd>Apply changes described in profile</dd>
<dt><code>-l</code>, <code>&#8211;config_file_list</code></dt>
<dd>List preloaded profiles</dd>
<dt><code>-i</code>, <code>&#8211;isolate</code></dt>
<dd>Move all threads away from CPU-LIST. Requires <code>-c</code> or <code>-S</code>.</dd>
<dt><code>-I</code>, <code>&#8211;include</code></dt>
<dd>Allow all threads to run on CPU-LIST. Requires <code>-c</code> or <code>-S</code>.</dd>
<dt><code>-m</code>, <code>&#8211;move</code></dt>
<dd>Move selected entities to CPU-LIST. Requires <code>-c</code> and either <code>-t</code> or <code>-q</code>.</dd>
<dt><code>-p</code>, <code>&#8211;priority</code>=<i>[POLICY:]</i>RTPRIO</dt>
<dd>Set thread scheduler tunables: POLICY and RTPRIO. POLICY is one of OTHER, FIFO, RR, or BATCH. If <code>-t</code> is not set, <code>-p</code> will act as a Modifier saving the sched tunables for future Actions, for example <code>-r</code>.</dd>
<dt><code>-P</code>, <code>&#8211;show_threads</code></dt>
<dd>Show thread list.</dd>
<dt><code>-s</code>, <code>&#8211;save</code>=<i>FILENAME</i></dt>
<dd>Save kthreads sched tunables to FILENAME.</dd>
<dt><code>-r</code>, <code>&#8211;run</code>=<i>&quot;COMMAND&quot;</i></dt>
<dd>Run the COMMAND. If arguments are passed, the entire command line must be provided inside &quot;quotes&quot;. Modifiers <code>-c</code> and <code>-p</code> can be used to set the affinity and scheduler tunables of the given COMMAND. The arg[0] (i.e. the command) will be set in THREAD-LIST. Likewise the <code>-t</code>, the COMMAND accepts the prefix <code>+</code> and <code>&#8211;</code> as wildcards in order to be appended or removed from THREAD-LIST, respectively.</dd>
<dt><code>-v</code>, <code>&#8211;version</code></dt>
<dd>Show version</dd>
<dt><code>-W</code>, <code>&#8211;what_is</code></dt>
<dd>Provides help about selected entities. Requires <code>-t</code>.</dd>
<dt><code>-x</code>, <code>&#8211;spread</code></dt>
<dd>Spread selected entities over CPU-LIST. Requires at least one of <code>-t</code> or <code>-q</code>. The specified threads and IRQs are each assigned to one cpu in CPU-LIST.</dd>
<dt><i>Modifiers</i></dt>
<dd>
</dd><dt><code>-c</code>, <code>&#8211;cpus</code>=<i>CPU-LIST</i></dt>
<dd>CPU-LIST affected by commands. Requires a CPU number or a comma-separated list of CPU numbers.</dd>
<dt><code>-C</code>, <code>&#8211;affect_children</code></dt>
<dd>Operation will affect children threads.</dd>
<dt><code>-f</code>, <code>&#8211;filter</code></dt>
<dd>Disable display of selected CPUs in <code>&#8211;gui</code>. Requires <code>-cR.</dd>
<dt>-G</code>, <code>&#8211;cgroup</code></dt>
<dd>Display the processes with the type of cgroups they are in. Requires <code>-PR.</dd>
<dt>-K</code>, <code>&#8211;no_kthreads</code></dt>
<dd>Operations will not affect kernel threads.</dd>
<dt><code>-q</code>, <code>&#8211;irqs</code>=<i>IRQ-LIST</i></dt>
<dd>IRQ-LIST affected by commands. Requires an IRQ number or a comma-separated list of IRQ numbers.</dd>
<dt><code>-S</code>, <code>&#8211;sockets</code>=<i>CPU-SOCKET-LIST</i></dt>
<dd>CPU-SOCKET-LIST affected by commands. Requires a socket number or a comma-separated list of socket numbers.</dd>
<dt><code>-t</code>, <code>&#8211;threads</code>=<i>THREAD-LIST</i></dt>
<dd>THREAD-LIST affected by commands. Requires a thread number or thread name, or a comma-separated list of thread numbers and/or names. Thread names may contain wildcards. Be sure to quote or escape any wildcard specifications. If only <code>&#8211;</code> is passed as argument, the THREAD-LIST will be cleared.</dd>
<dt><code>-U</code>, <code>&#8211;no_uthreads</code></dt>
<dd>Operations will not affect user threads.</dd></dl>
<h2>Usage Examples</h2>
<p>If for instance the Ethernet NICs have multiple queues for both receive and transmit, each with its own IRQ, the Ethernet IRQs can be associated with a CPU socket:</p>
<dl>
<dt><code>tuna -S 2 -i -q &#8216;eth*&#8217; -x</code></dt>
<dd>Move everything off the CPUs in socket 2, then spread the IRQs for the Ethernet devices across those same CPUs. </dd>
</dl>
