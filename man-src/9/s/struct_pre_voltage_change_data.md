---
title: "struct_pre_voltage_change_data(9)"
name: "struct_pre_voltage_change_data"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_pre_voltage_change_data/"
description: "struct_pre_voltage_change_data – Data sent with PRE_VOLTAGE_CHANGE event"
---

<p>struct_pre_voltage_change_data &#8211; Data sent with PRE_VOLTAGE_CHANGE event</p>
<h2>Synopsis</h2>
<pre><code>struct pre_voltage_change_data {
    unsigned long old_uV;
    unsigned long min_uV;
    unsigned long max_uV;
};</code></pre>
<h2>Members</h2>
<p>old_uV</p>
<dl>
<dd>Current voltage before change.</dl>
<p> min_uV</p>
<dl>
<dd>Min voltage we&#8217;ll change to.</dl>
<p> max_uV</p>
<dl>
<dd>Max voltage we&#8217;ll change to.</dl>
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
