---
title: "struct_regulator_linear_range(9)"
name: "struct_regulator_linear_range"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_regulator_linear_range/"
description: "struct_regulator_linear_range – specify linear voltage ranges"
---

<p>struct_regulator_linear_range &#8211; specify linear voltage ranges</p>
<h2>Synopsis</h2>
<pre><code>struct regulator_linear_range {
    unsigned int min_uV;
    unsigned int min_sel;
    unsigned int max_sel;
    unsigned int uV_step;
};</code></pre>
<h2>Members</h2>
<p>min_uV</p>
<dl>
<dd>Lowest voltage in range</dl>
<p> min_sel</p>
<dl>
<dd>Lowest selector for range</dl>
<p> max_sel</p>
<dl>
<dd>Highest selector for range</dl>
<p> uV_step</p>
<dl>
<dd>Step size</dl>
<h2>Description</h2>
<p>Specify a range of voltages for <code>regulator_map_linar_range</code> and <code>regulator_list_linear_range</code>.</p>
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
