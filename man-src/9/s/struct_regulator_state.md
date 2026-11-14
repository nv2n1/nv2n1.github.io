---
title: "struct_regulator_state(9)"
name: "struct_regulator_state"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_regulator_state/"
description: "struct_regulator_state – regulator state during low power system states"
---

<p>struct_regulator_state &#8211; regulator state during low power system states</p>
<h2>Synopsis</h2>
<pre><code>struct regulator_state {
    int uV;
    unsigned int mode;
    int enabled;
    int disabled;
};</code></pre>
<h2>Members</h2>
<p>uV</p>
<dl>
<dd>Operating voltage during suspend.</dl>
<p> mode</p>
<dl>
<dd>Operating mode during suspend.</dl>
<p> enabled</p>
<dl>
<dd>Enabled during suspend.</dl>
<p> disabled</p>
<dl>
<dd>Disabled during suspend.</dl>
<h2>Description</h2>
<p>This describes a regulators state during a system wide low power state. One of enabled or disabled must be set for the configuration to be applied.</p>
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
