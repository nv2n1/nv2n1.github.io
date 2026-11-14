---
title: "struct_regulator_ops(9)"
name: "struct_regulator_ops"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_regulator_ops/"
description: "struct_regulator_ops – regulator operations."
---

<p>struct_regulator_ops &#8211; regulator operations.</p>
<h2>Synopsis</h2>
<pre><code>struct regulator_ops {
    int (*list_voltage)(struct regulator_dev *, unsigned selector);
    int (*set_voltage)(struct regulator_dev *, int min_uV, int max_uV, unsigned *selector);
    int (*map_voltage)(struct regulator_dev *, int min_uV, int max_uV);
    int (*set_voltage_sel)(struct regulator_dev *, unsigned selector);
    int (*get_voltage)(struct regulator_dev *);
    int (*get_voltage_sel)(struct regulator_dev *);
    int (*set_current_limit)(struct regulator_dev *, int min_uA, int max_uA);
    int (*get_current_limit)(struct regulator_dev *);
    int (*set_input_current_limit)(struct regulator_dev *, int lim_uA);
    int (*set_over_current_protection)(struct regulator_dev *);
    int (*set_active_discharge)(struct regulator_dev *, bool enable);
    int (*enable)(struct regulator_dev *);
    int (*disable)(struct regulator_dev *);
    int (*is_enabled)(struct regulator_dev *);
    int (*set_mode)(struct regulator_dev *, unsigned int mode);
    unsigned int (*get_mode)(struct regulator_dev *);
    int (*enable_time)(struct regulator_dev *);
    int (*set_ramp_delay)(struct regulator_dev *, int ramp_delay);
    int (*set_voltage_time)(struct regulator_dev *, int old_uV, int new_uV);
    int (*set_voltage_time_sel)(struct regulator_dev *, unsigned int old_selector, unsigned int new_selector);
    int (*set_soft_start)(struct regulator_dev *);
    int (*get_status)(struct regulator_dev *);
    unsigned int (*get_optimum_mode)(struct regulator_dev *, int input_uV, int output_uV, int load_uA);
    int (*set_load)(struct regulator_dev *, int load_uA);
    int (*set_bypass)(struct regulator_dev *dev, bool enable);
    int (*get_bypass)(struct regulator_dev *dev, bool *enable);
    int (*set_suspend_voltage)(struct regulator_dev *, int uV);
    int (*set_suspend_enable)(struct regulator_dev *);
    int (*set_suspend_disable)(struct regulator_dev *);
    int (*set_suspend_mode)(struct regulator_dev *, unsigned int mode);
    int (*set_pull_down)(struct regulator_dev *);
};</code></pre>
<h2>Members</h2>
<p>list_voltage</p>
<dl>
<dd>Return one of the supported voltages, in microvolts; zero if the selector indicates a voltage that is unusable on this system; or negative errno. Selectors range from zero to one less than regulator_desc.n_voltages. Voltages may be reported in any order.</dl>
<p> set_voltage</p>
<dl>
<dd>Set the voltage for the regulator within the range specified. The driver should select the voltage closest to min_uV.</dl>
<p> map_voltage</p>
<dl>
<dd>Convert a voltage into a selector</dl>
<p> set_voltage_sel</p>
<dl>
<dd>Set the voltage for the regulator using the specified selector.</dl>
<p> get_voltage</p>
<dl>
<dd>Return the currently configured voltage for the regulator.</dl>
<p> get_voltage_sel</p>
<dl>
<dd>Return the currently configured voltage selector for the regulator.</dl>
<p> set_current_limit</p>
<dl>
<dd>Configure a limit for a current-limited regulator. The driver should select the current closest to max_uA.</dl>
<p> get_current_limit</p>
<dl>
<dd>Get the configured limit for a current-limited regulator.</dl>
<p> set_input_current_limit</p>
<dl>
<dd>Configure an input limit.</dl>
<p> set_over_current_protection</p>
<dl>
<dd>Support capability of automatically shutting down when detecting an over current event.</dl>
<p> set_active_discharge</p>
<dl>
<dd>Set active discharge enable/disable of regulators.</dl>
<p> enable</p>
<dl>
<dd>Configure the regulator as enabled.</dl>
<p> disable</p>
<dl>
<dd>Configure the regulator as disabled.</dl>
<p> is_enabled</p>
<dl>
<dd>Return 1 if the regulator is enabled, 0 if not. May also return negative errno.</dl>
<p> set_mode</p>
<dl>
<dd>Set the configured operating mode for the regulator.</dl>
<p> get_mode</p>
<dl>
<dd>Get the configured operating mode for the regulator.</dl>
<p> enable_time</p>
<dl>
<dd>Time taken for the regulator voltage output voltage to stabilise after being enabled, in microseconds.</dl>
<p> set_ramp_delay</p>
<dl>
<dd>Set the ramp delay for the regulator. The driver should select ramp delay equal to or less than(closest) ramp_delay.</dl>
<p> set_voltage_time</p>
<dl>
<dd>Time taken for the regulator voltage output voltage to stabilise after being set to a new value, in microseconds. The function receives the from and to voltage as input, it should return the worst case.</dl>
<p> set_voltage_time_sel</p>
<dl>
<dd>Time taken for the regulator voltage output voltage to stabilise after being set to a new value, in microseconds. The function receives the from and to voltage selector as input, it should return the worst case.</dl>
<p> set_soft_start</p>
<dl>
<dd>Enable soft start for the regulator.</dl>
<p> get_status</p>
<dl>
<dd>Return actual (not as-configured) status of regulator, as a REGULATOR_STATUS value (or negative errno)</dl>
<p> get_optimum_mode</p>
<dl>
<dd>Get the most efficient operating mode for the regulator when running with the specified parameters.</dl>
<p> set_load</p>
<dl>
<dd>Set the load for the regulator.</dl>
<p> set_bypass</p>
<dl>
<dd>Set the regulator in bypass mode.</dl>
<p> get_bypass</p>
<dl>
<dd>Get the regulator bypass mode state.</dl>
<p> set_suspend_voltage</p>
<dl>
<dd>Set the voltage for the regulator when the system is suspended.</dl>
<p> set_suspend_enable</p>
<dl>
<dd>Mark the regulator as enabled when the system is suspended.</dl>
<p> set_suspend_disable</p>
<dl>
<dd>Mark the regulator as disabled when the system is suspended.</dl>
<p> set_suspend_mode</p>
<dl>
<dd>Set the operating mode for the regulator when the system is suspended.</dl>
<p> set_pull_down</p>
<dl>
<dd>Configure the regulator to pull down when the regulator is disabled.</dl>
<h2>Description</h2>
<p>This struct describes regulator operations which can be implemented by regulator chip drivers.</p>
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
