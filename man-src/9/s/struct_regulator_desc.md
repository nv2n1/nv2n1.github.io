---
title: "struct_regulator_desc(9)"
name: "struct_regulator_desc"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_regulator_desc/"
description: "struct_regulator_desc – Static regulator descriptor"
---

<p>struct_regulator_desc &#8211; Static regulator descriptor</p>
<h2>Synopsis</h2>
<pre><code>struct regulator_desc {
    const char *name;
    const char *supply_name;
    const char *of_match;
    const char *regulators_node;
    int (*of_parse_cb)(struct device_node *, const struct regulator_desc *, struct regulator_config *);
    int id;
    unsigned int continuous_voltage_range : 1;
    unsigned n_voltages;
    const struct regulator_ops *ops;
    int irq;
    enum regulator_type type;
    struct module *owner;
    unsigned int min_uV;
    unsigned int uV_step;
    unsigned int linear_min_sel;
    int fixed_uV;
    unsigned int ramp_delay;
    int min_dropout_uV;
    const struct regulator_linear_range *linear_ranges;
    int n_linear_ranges;
    const unsigned int *volt_table;
    unsigned int vsel_reg;
    unsigned int vsel_mask;
    unsigned int csel_reg;
    unsigned int csel_mask;
    unsigned int apply_reg;
    unsigned int apply_bit;
    unsigned int enable_reg;
    unsigned int enable_mask;
    unsigned int enable_val;
    unsigned int disable_val;
    bool enable_is_inverted;
    unsigned int bypass_reg;
    unsigned int bypass_mask;
    unsigned int bypass_val_on;
    unsigned int bypass_val_off;
    unsigned int active_discharge_on;
    unsigned int active_discharge_off;
    unsigned int active_discharge_mask;
    unsigned int active_discharge_reg;
    unsigned int enable_time;
    unsigned int off_on_delay;
    unsigned int (*of_map_mode)(unsigned int mode);
};</code></pre>
<h2>Members</h2>
<p>name</p>
<dl>
<dd>Identifying name for the regulator.</dl>
<p> supply_name</p>
<dl>
<dd>Identifying the regulator supply</dl>
<p> of_match</p>
<dl>
<dd>Name used to identify regulator in DT.</dl>
<p> regulators_node</p>
<dl>
<dd>Name of node containing regulator definitions in DT.</dl>
<p> of_parse_cb</p>
<dl>
<dd>Optional callback called only if of_match is present. Will be called for each regulator parsed from DT, during init_data parsing. The regulator_config passed as argument to the callback will be a copy of config passed to regulator_register, valid only for this particular call. Callback may freely change the config but it cannot store it for later usage. Callback should return 0 on success or negative ERRNO indicating failure.</dl>
<p> id</p>
<dl>
<dd>Numerical identifier for the regulator.</dl>
<p> continuous_voltage_range</p>
<dl>
<dd>Indicates if the regulator can set any voltage within constrains range.</dl>
<p> n_voltages</p>
<dl>
<dd>Number of selectors available for ops.<code>list_voltage</code>.</dl>
<p> ops</p>
<dl>
<dd>Regulator operations table.</dl>
<p> irq</p>
<dl>
<dd>Interrupt number for the regulator.</dl>
<p> type</p>
<dl>
<dd>Indicates if the regulator is a voltage or current regulator.</dl>
<p> owner</p>
<dl>
<dd>Module providing the regulator, used for refcounting.</dl>
<p> min_uV</p>
<dl>
<dd>Voltage given by the lowest selector (if linear mapping)</dl>
<p> uV_step</p>
<dl>
<dd>Voltage increase with each selector (if linear mapping)</dl>
<p> linear_min_sel</p>
<dl>
<dd>Minimal selector for starting linear mapping</dl>
<p> fixed_uV</p>
<dl>
<dd>Fixed voltage of rails.</dl>
<p> ramp_delay</p>
<dl>
<dd>Time to settle down after voltage change (unit: uV/us)</dl>
<p> min_dropout_uV</p>
<dl>
<dd>The minimum dropout voltage this regulator can handle</dl>
<p> linear_ranges</p>
<dl>
<dd>A constant table of possible voltage ranges.</dl>
<p> n_linear_ranges</p>
<dl>
<dd>Number of entries in the <i>linear_ranges</i> table.</dl>
<p> volt_table</p>
<dl>
<dd>Voltage mapping table (if table based mapping)</dl>
<p> vsel_reg</p>
<dl>
<dd>Register for selector when using regulator_regmap_X_voltage_</dl>
<p> vsel_mask</p>
<dl>
<dd>Mask for register bitfield used for selector</dl>
<p> csel_reg</p>
<dl>
<dd>Register for TPS65218 LS3 current regulator</dl>
<p> csel_mask</p>
<dl>
<dd>Mask for TPS65218 LS3 current regulator</dl>
<p> apply_reg</p>
<dl>
<dd>Register for initiate voltage change on the output when using regulator_set_voltage_sel_regmap</dl>
<p> apply_bit</p>
<dl>
<dd>Register bitfield used for initiate voltage change on the output when using regulator_set_voltage_sel_regmap</dl>
<p> enable_reg</p>
<dl>
<dd>Register for control when using regmap enable/disable ops</dl>
<p> enable_mask</p>
<dl>
<dd>Mask for control when using regmap enable/disable ops</dl>
<p> enable_val</p>
<dl>
<dd>Enabling value for control when using regmap enable/disable ops</dl>
<p> disable_val</p>
<dl>
<dd>Disabling value for control when using regmap enable/disable ops</dl>
<p> enable_is_inverted</p>
<dl>
<dd>A flag to indicate set enable_mask bits to disable when using regulator_enable_regmap and friends APIs.</dl>
<p> bypass_reg</p>
<dl>
<dd>Register for control when using regmap set_bypass</dl>
<p> bypass_mask</p>
<dl>
<dd>Mask for control when using regmap set_bypass</dl>
<p> bypass_val_on</p>
<dl>
<dd>Enabling value for control when using regmap set_bypass</dl>
<p> bypass_val_off</p>
<dl>
<dd>Disabling value for control when using regmap set_bypass</dl>
<p> active_discharge_on</p>
<dl>
<dd>Disabling value for control when using regmap set_active_discharge</dl>
<p> active_discharge_off</p>
<dl>
<dd>Enabling value for control when using regmap set_active_discharge</dl>
<p> active_discharge_mask</p>
<dl>
<dd>Mask for control when using regmap set_active_discharge</dl>
<p> active_discharge_reg</p>
<dl>
<dd>Register for control when using regmap set_active_discharge</dl>
<p> enable_time</p>
<dl>
<dd>Time taken for initial enable of regulator (in uS).</dl>
<p> off_on_delay</p>
<dl>
<dd>guard time (in uS), before re-enabling a regulator</dl>
<p> of_map_mode</p>
<dl>
<dd>Maps a hardware mode defined in a DeviceTree to a standard mode</dl>
<h2>Description</h2>
<p>Each regulator registered with the core is described with a structure of this type and a struct regulator_config. This structure contains the non-varying parts of the regulator description.</p>
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
