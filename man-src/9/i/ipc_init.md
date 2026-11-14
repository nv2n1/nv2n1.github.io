---
title: "ipc_init(9)"
name: "ipc_init"
section: "9"
letter: "i"
url: "/docs/linux/man/9-ipc_init/"
---

ipc_init - initialise ipc subsystem

<h2>Synopsis</h2>

<pre><code>int ipc_init(void);</code></pre>

<h2>Arguments</h2>

<i>void</i>
<dl><dd><dd>no arguments</dl>

<h2>Description</h2>

The various sysv ipc resources (semaphores, messages and shared memory) are initialised. 

 A callback routine is registered into the memory hotplug notifier chain: since msgmni scales to lowmem this callback routine will be called upon successful memory add / remove to recompute msmgni.

<h2>Copyright</h2>


