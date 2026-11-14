---
title: "struct_regulator_config(9)"
name: "struct_regulator_config"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_regulator_config/"
description: "struct_regulator_config – Dynamic regulator descriptor"
---

<p>struct_regulator_config &#8211; Dynamic regulator descriptor</p>
<h2>Synopsis</h2>
<pre><code>struct regulator_config {
    struct device *dev;
    const struct regulator_init_data *init_data;
    void *driver_data;
    struct device_node *of_node;
    struct regmap *regmap;
    bool ena_gpio_initialized;
    int ena_gpio;
    unsigned int ena_gpio_invert : 1;
    unsigned int ena_gpio_flags;
};</code></pre>
<h2>Members</h2>
<p>dev</p>
<dl>
<dd>struct device for the regulator</dl>
<p> init_data</p>
<dl>
<dd>platform provided init data, passed through by driver</dl>
<p> driver_data</p>
<dl>
<dd>private regulator data</dl>
<p> of_node</p>
<dl>
<dd>OpenFirmware node to parse for device tree bindings (may be NULL).</dl>
<p> regmap</p>
<dl>
<dd>regmap to use for core regmap helpers if <code>dev_get_regmap</code> is insufficient.</dl>
<p> ena_gpio_initialized</p>
<dl>
<dd>GPIO controlling regulator enable was properly initialized, meaning that &gt;= 0 is a valid gpio identifier and &lt; 0 is a non existent gpio.</dl>
<p> ena_gpio</p>
<dl>
<dd>GPIO controlling regulator enable.</dl>
<p> ena_gpio_invert</p>
<dl>
<dd>Sense for GPIO enable control.</dl>
<p> ena_gpio_flags</p>
<dl>
<dd>Flags to use when calling <code>gpio_request_one</code></dl>
<h2>Description</h2>
<p>Each regulator registered with the core is described with a structure of this type and a struct regulator_desc. This structure contains the runtime variable parts of the regulator description.</p>
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
