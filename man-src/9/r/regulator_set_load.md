---
title: "regulator_set_load(9)"
name: "regulator_set_load"
section: "9"
letter: "r"
url: "/docs/linux/man/9-regulator_set_load/"
description: "regulator_set_load – set regulator load"
---

<p>regulator_set_load &#8211; set regulator load</p>
<h2>Synopsis</h2>
<pre><code>int regulator_set_load(struct regulator *regulator, int uA_load);</code></pre>
<h2>Arguments</h2>
<p><i>regulator</i></p>
<dl>
<dd>
<dd>regulator source</dl>
<p> <i>uA_load</i></p>
<dl>
<dd>load current</dl>
<h2>Description</h2>
<p>Notifies the regulator core of a new device load. This is then used by DRMS (if enabled by constraints) to set the most efficient regulator operating mode for the new regulator loading. </p>
<p> Consumer devices notify their supply regulator of the maximum power they will require (can be taken from device datasheet in the power consumption tables) when they change operational status and hence power state. Examples of operational state changes that can affect power consumption are :- </p>
<p> o Device is opened / closed. o Device I/O is about to begin or has just finished. o Device is idling in between work. </p>
<p> This information is also exported via sysfs to userspace. </p>
<p> DRMS will sum the total requested load on the regulator and change to the most efficient operating mode if platform constraints allow. </p>
<p> On error a negative errno is returned.</p>
<h2>Authors</h2>
<p><code>Liam Girdwood</code> &lt;lrg [at] slimlogic.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Mark Brown</code> &lt;broonie [at] opensource.wolfsonmicro.com&gt;<br />
 Wolfson Microelectronics, </p>
<p>&nbsp;<wbr>&nbsp;<wbr></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
