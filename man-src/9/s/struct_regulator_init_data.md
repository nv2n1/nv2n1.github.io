---
title: "struct_regulator_init_data(9)"
name: "struct_regulator_init_data"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_regulator_init_data/"
description: "struct_regulator_init_data – regulator platform initialisation data."
---

<p>struct_regulator_init_data &#8211; regulator platform initialisation data.</p>
<h2>Synopsis</h2>
<pre><code>struct regulator_init_data {
    const char *supply_regulator;
    struct regulation_constraints constraints;
    int num_consumer_supplies;
    struct regulator_consumer_supply *consumer_supplies;
    int (*regulator_init)(void *driver_data);
    void *driver_data;
};</code></pre>
<h2>Members</h2>
<p>supply_regulator</p>
<dl>
<dd>Parent regulator. Specified using the regulator name as it appears in the name field in sysfs, which can be explicitly set using the constraints field &#8216;name&#8217;.</dl>
<p> constraints</p>
<dl>
<dd>Constraints. These must be specified for the regulator to be usable.</dl>
<p> num_consumer_supplies</p>
<dl>
<dd>Number of consumer device supplies.</dl>
<p> consumer_supplies</p>
<dl>
<dd>Consumer device supply configuration.</dl>
<p> regulator_init</p>
<dl>
<dd>Callback invoked when the regulator has been registered.</dl>
<p> driver_data</p>
<dl>
<dd>Data passed to regulator_init.</dl>
<h2>Description</h2>
<p>Initialisation constraints, our supply and consumers supplies.</p>
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
