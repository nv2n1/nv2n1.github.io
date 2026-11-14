---
title: "struct_regulation_constraints(9)"
name: "struct_regulation_constraints"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_regulation_constraints/"
description: "struct_regulation_constraints – regulator operating constraints."
---

<p>struct_regulation_constraints &#8211; regulator operating constraints.</p>
<h2>Synopsis</h2>
<pre><code>struct regulation_constraints {
    const char *name;
    int min_uV;
    int max_uV;
    int uV_offset;
    int min_uA;
    int max_uA;
    int ilim_uA;
    int system_load;
    unsigned int valid_modes_mask;
    unsigned int valid_ops_mask;
    int input_uV;
    struct regulator_state state_disk;
    struct regulator_state state_mem;
    struct regulator_state state_standby;
    suspend_state_t initial_state;
    unsigned int initial_mode;
    unsigned int ramp_delay;
    unsigned int enable_time;
    unsigned int active_discharge;
    unsigned always_on : 1;
    unsigned boot_on : 1;
    unsigned apply_uV : 1;
    unsigned ramp_disable : 1;
    unsigned soft_start : 1;
    unsigned pull_down : 1;
    unsigned over_current_protection : 1;
};</code></pre>
<h2>Members</h2>
<p>name</p>
<dl>
<dd>Descriptive name for the constraints, used for display purposes.</dl>
<p> min_uV</p>
<dl>
<dd>Smallest voltage consumers may set.</dl>
<p> max_uV</p>
<dl>
<dd>Largest voltage consumers may set.</dl>
<p> uV_offset</p>
<dl>
<dd>Offset applied to voltages from consumer to compensate for voltage drops.</dl>
<p> min_uA</p>
<dl>
<dd>Smallest current consumers may set.</dl>
<p> max_uA</p>
<dl>
<dd>Largest current consumers may set.</dl>
<p> ilim_uA</p>
<dl>
<dd>Maximum input current.</dl>
<p> system_load</p>
<dl>
<dd>Load that isn&#8217;t captured by any consumer requests.</dl>
<p> valid_modes_mask</p>
<dl>
<dd>Mask of modes which may be configured by consumers.</dl>
<p> valid_ops_mask</p>
<dl>
<dd>Operations which may be performed by consumers.</dl>
<p> input_uV</p>
<dl>
<dd>Input voltage for regulator when supplied by another regulator.</dl>
<p> state_disk</p>
<dl>
<dd>State for regulator when system is suspended in disk mode.</dl>
<p> state_mem</p>
<dl>
<dd>State for regulator when system is suspended in mem mode.</dl>
<p> state_standby</p>
<dl>
<dd>State for regulator when system is suspended in standby mode.</dl>
<p> initial_state</p>
<dl>
<dd>Suspend state to set by default.</dl>
<p> initial_mode</p>
<dl>
<dd>Mode to set at startup.</dl>
<p> ramp_delay</p>
<dl>
<dd>Time to settle down after voltage change (unit: uV/us)</dl>
<p> enable_time</p>
<dl>
<dd>Turn-on time of the rails (unit: microseconds)</dl>
<p> active_discharge</p>
<dl>
<dd>Enable/disable active discharge. The enum regulator_active_discharge values are used for initialisation.</dl>
<p> always_on</p>
<dl>
<dd>Set if the regulator should never be disabled.</dl>
<p> boot_on</p>
<dl>
<dd>Set if the regulator is enabled when the system is initially started. If the regulator is not enabled by the hardware or bootloader then it will be enabled when the constraints are applied.</dl>
<p> apply_uV</p>
<dl>
<dd>Apply the voltage constraint when initialising.</dl>
<p> ramp_disable</p>
<dl>
<dd>Disable ramp delay when initialising or when setting voltage.</dl>
<p> soft_start</p>
<dl>
<dd>Enable soft start so that voltage ramps slowly.</dl>
<p> pull_down</p>
<dl>
<dd>Enable pull down when regulator is disabled.</dl>
<p> over_current_protection</p>
<dl>
<dd>Auto disable on over current event.</dl>
<h2>Description</h2>
<p>This struct describes regulator and board/machine specific constraints.</p>
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
