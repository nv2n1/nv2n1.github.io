---
title: "sensors-conf(5)"
name: "sensors-conf"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sensors-conf/"
description: "sensors.conf – libsensors configuration file"
---

<p>sensors.conf &#8211; libsensors configuration file</p>
<h2>Description</h2>
<p>sensors.conf describes how libsensors, and so all programs using it, should translate the raw readings from the kernel modules to real-world values. </p>
<h2>Semantics</h2>
<p>On a given system, there may be one or more hardware monitoring chips. Each chip may have several features. For example, the LM78 monitors 7 voltage inputs, 3 fans and one temperature. Feature names are standardized. Typical feature names are in0, in1, in2&#8230; for voltage inputs, fan1, fan2, fan3&#8230; for fans and temp1, temp2, temp3&#8230; for temperature inputs. </p>
<p> Each feature may in turn have one or more sub-features, each representing an attribute of the feature: input value, low limit, high limit, alarm, etc. Sub-feature names are standardized as well. For example, the first voltage input (in0) would typically have sub-features in0_input (measured value), in0_min (low limit), in0_max (high limit) and in0_alarm (alarm flag). Which sub-features are actually present depend on the exact chip type. </p>
<p> The <i>sensors.conf</i> configuration file will let you configure each chip, feature and sub-feature in a way that makes sense for your system. </p>
<p> The rest of this section describes the meaning of each configuration statement.</p>
<h3>Chip Statement</h3>
<p>A <i>chip</i> statement selects for which chips all following <i>compute</i>, <i>label</i>, <i>ignore</i> and <i>set</i> statements are meant. A chip selection remains valid until the next <i>chip</i> statement. Example: </p>
<dl>
<dd>chip &quot;lm78-*&quot; &quot;lm79-*&quot;</dl>
<p> If a chip matches at least one of the chip descriptions, the following configuration lines are examined for it, otherwise they are ignored. </p>
<p> A chip description is built from several elements, separated by dashes. The first element is the chip type, the second element is the name of the bus, and the third element is the hexadecimal address of the chip. Such chip descriptions are printed by <a href="/docs/linux/man/1-sensors/">sensors</a>(1) as the first line for every chip. </p>
<p> The name of the bus is either <i>isa</i>, <i>pci</i>, <i>virtual</i>, <i>spi-*,</i> <i>i2c-N</i> or <i>mdio</i> with <i>N</i> being a bus number as bound with a <i>bus</i> statement. This list isn&#8217;t necessarily exhaustive as support for other bus types may be added in the future. </p>
<p> You may substitute the wildcard operator <i>*</i> for every element. Note however that it wouldn&#8217;t make any sense to specify the address without the bus type, so the address part is plain omitted when the bus type isn&#8217;t specified. Here is how you would express the following matches: </p>
<table>
<tr VALIGN=top>
<td>LM78 chip at address 0x2d on I2C bus 1</td>
<td>lm78-i2c-1-2d
</td>
</tr>
<tr VALIGN=top>
<td>LM78 chip at address 0x2d on any I2C bus</td>
<td>lm78-i2c-*-2d
</td>
</tr>
<tr VALIGN=top>
<td>LM78 chip at address 0x290 on the ISA bus</td>
<td>lm78-isa-0290
</td>
</tr>
<tr VALIGN=top>
<td>Any LM78 chip on I2C bus 1</td>
<td>lm78-i2c-1-*
</td>
</tr>
<tr VALIGN=top>
<td>Any LM78 on any I2C bus</td>
<td>lm78-i2c-*-*
</td>
</tr>
<tr VALIGN=top>
<td>Any LM78 chip on the ISA bus</td>
<td>lm78-isa-*
</td>
</tr>
<tr VALIGN=top>
<td>Any LM78 chip</td>
<td>lm78-*
</td>
</tr>
<tr VALIGN=top>
<td>Any chip at address 0x2d on I2C bus 1</td>
<td>*-i2c-1-2d
</td>
</tr>
<tr VALIGN=top>
<td>Any chip at address 0x290 on the ISA bus</td>
<td>*-isa-0290
</td>
</tr>
</table>
<p> If several chip statements match a specific chip, they are all considered.</p>
<h3>Label Statement</h3>
<p>A <i>label</i> statement describes how a feature should be called. Features without a <i>label</i> statement are just called by their feature name. Applications can use this to label the readings they present. Example: </p>
<dl>
<dd>label in3 &quot;+5V&quot;</dl>
<p> The first argument is the feature name. The second argument is the feature description. </p>
<p> Note that you must use the raw feature name, which is not necessarily the one displayed by &quot;sensors&quot; by default. Use &quot;sensors -u&quot; to see the raw feature names. Same applies to all other statement types below.</p>
<h3>Ignore Statement</h3>
<p>An <i>ignore</i> statement is a hint that a specific feature should be ignored &#8211; probably because it returns bogus values (for example, because a fan or temperature sensor is not connected). Example: </p>
<dl>
<dd>ignore fan1</dl>
<p> The only argument is the feature name. Please note that this does not disable anything in the actual sensor chip; it simply hides the feature in question from libsensors users.</p>
<h3>Compute Statement</h3>
<p>A <i>compute</i> statement describes how a feature&#8217;s raw value should be translated to a real-world value, and how a real-world value should be translated back to a raw value again. This is most useful for voltage sensors, because in general sensor chips have a limited range and voltages outside this range must be divided (using resistors) before they can be monitored. Example: </p>
<dl>
<dd>compute in3 ((6.8/10)+1)*@, @/((6.8/10)+1)</dl>
<p> The example above expresses the fact that the voltage input is divided using two resistors of values 6.8 Ohm and 10 Ohm, respectively. See the <code>VOLTAGE COMPUTATION DETAILS</code> section below for details. </p>
<p> The first argument is the feature name. The second argument is an expression which specifies how a raw value must be translated to a real-world value; `@&#8217; stands here for the raw value. This is the formula which will be applied when reading values from the chip. The third argument is an expression that specifies how a real-world value should be translated back to a raw value; `@&#8217; stands here for the real-world value. This is the formula which will be applied when writing values to the chip. The two formulas are obviously related, and are separated by a comma. </p>
<p> A <i>compute</i> statement applies to all sub-features of the target feature for which it makes sense. For example, the above example would affect sub-features in3_min and in3_max (which are voltage values) but not in3_alarm (which is a boolean flag.) </p>
<p> The following operators are supported in <i>compute</i> statements:</p>
<dl>
<dd>+ &#8211; * / ( ) ^ `</dl>
<p> ^x means exp(x) and `x means ln(x). </p>
<p> You may use the name of sub-features in these expressions; current readings are substituted. You should be careful though to avoid circular references. </p>
<p> If at any moment a translation between a raw and a real-world value is called for, but no <i>compute</i> statement applies, a one-on-one translation is used instead.</p>
<h3>Set Statement</h3>
<p>A <i>set</i> statement is used to write a sub-feature value to the chip. Of course not all sub-feature values can be set that way, in particular input values and alarm flags can not. Valid sub-features are usually min/max limits. Example: </p>
<dl>
<dd>set in3_min 5 * 0.95</dl>
<dl>
<dd>set in3_max 5 * 1.05</dl>
<p> The example above basically configures the chip to allow a 5% deviance for the +5V power input. </p>
<p> The first argument is the feature name. The second argument is an expression which determines the written value. If there is an applying <i>compute</i> statement, this value is fed to its third argument to translate it to a raw value. </p>
<p> You may use the name of sub-features in these expressions; current readings are substituted. You should be careful though to avoid circular references. </p>
<p> Please note that <i>set</i> statements are only executed by <a href="/docs/linux/man/1-sensors/">sensors</a>(1) when you use the <code>-s</code> option. Typical graphical sensors applications do not care about these statements at all.</p>
<h3>Bus Statement</h3>
<p>A <i>bus</i> statement binds the description of an I2C or SMBus adapter to a bus number. This makes it possible to refer to an adapter in the configuration file, independent of the actual correspondence of bus numbers and actual adapters (which may change from moment to moment). Example: </p>
<dl>
<dd>bus &quot;i2c-0&quot; &quot;SMBus PIIX4 adapter at e800&quot;</dl>
<p> The first argument is the bus number. It is the literal text <i>i2c-</i>, followed by a number. As there is a dash in this argument, it must always be quoted. </p>
<p> The second argument is the adapter name, it must match exactly the adapter name as it appears in <i>/sys/class/i2c-adapter/i2c-*/name</i>. It should always be quoted as well as it will most certainly contain spaces or dashes. </p>
<p> The <i>bus</i> statements may be scattered randomly throughout the configuration file; there is no need to place the bus line before the place where its binding is referred to. Still, as a matter of good style, we suggest you place all <i>bus</i> statements together at the top of your configuration file. </p>
<p> Running <code>sensors &#8211;bus-list</code> will generate these lines for you. </p>
<p> In the case where multiple configuration files are used, the scope of each <i>bus</i> statement is the configuration file it was defined in. This makes it possible to have bus statements in all configuration files which will not unexpectedly interfere with each other.</p>
<h3>Statement Order</h3>
<p>Statements can go in any order, however it is recommended to put `set fanX_div&#8217; statements before `set fanX_min&#8217; statements, in case a driver doesn&#8217;t preserve the fanX_min setting when the fanX_div value is changed. Even if the driver does, it&#8217;s still better to put the statements in this order to avoid accuracy loss.</p>
<h2>Voltage Computation Details</h2>
<p>Most voltage sensors in sensor chips have a range of 0 to 4.08 V. This is generally sufficient for the +3.3V and CPU supply voltages, so the sensor chip reading is the actual voltage. </p>
<p> Other supply voltages must be scaled with an external resistor network. The driver reports the value at the chip&#8217;s pin (0 &#8211; 4.08 V), and the userspace application must convert this raw value to an actual voltage. The <i>compute</i> statements provide this facility. </p>
<p> Unfortunately the resistor values vary among motherboard types. Therefore you have to figure out the correct resistor values for your own motherboard. </p>
<p> For positive voltages (typically +5V and +12V), two resistors are used, with the following formula:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;R1&nbsp;=&nbsp;R2&nbsp;*&nbsp;(Vs/Vin &#8211; 1) </p>
<p> where:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;R1 and R2 are the resistor values<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Vs is the actual voltage being monitored<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Vin is the voltage at the pin </p>
<p> This leads to the following compute formula:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compute inX&nbsp;@*((R1/R2)+1),&nbsp;<wbr>&nbsp;@/(((R1/R2)+1) </p>
<p> Real-world formula for +5V and +12V would look like:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compute in3&nbsp;@*((6.8/10)+1),&nbsp;@/((6.8/10)+1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compute in4&nbsp;@*((28/10)+1),&nbsp;<wbr>&nbsp;@/((28/10)+1) </p>
<p> For negative voltages (typically -5V and -12V), two resistors are used as well, but different boards use different strategies to bring the voltage value into the 0 &#8211; 4.08 V range. Some use an inverting amplifier, others use a positive reference voltage. This leads to different computation formulas. Note that most users won&#8217;t have to care because most modern motherboards make little use of -12V and no use of -5V so they do not bother monitoring these voltage inputs. </p>
<p> Real-world examples for the inverting amplifier case:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compute in5 -@*(240/60), -@/(240/60)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compute in6 -@*(100/60), -@/(100/60) </p>
<p> Real-world examples for the positive voltage reference case:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compute in5&nbsp;@*(1+232/56)&nbsp;&#8211; 4.096*232/56,&nbsp;(@&nbsp;+&nbsp;4.096*232/56)/(1+232/56)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compute in6&nbsp;@*(1+120/56)&nbsp;&#8211; 4.096*120/56,&nbsp;(@&nbsp;+&nbsp;4.096*120/56)/(1+120/56) </p>
<p> Many recent monitoring chips have a 0 &#8211; 2.04 V range, so scaling resistors are even more needed, and resistor values are different. </p>
<p> There are also a few chips out there which have internal scaling resistors, meaning that their value is known and doesn&#8217;t change from one motherboard to the next. For these chips, the driver usually handles the scaling so it is transparent to the user and no <i>compute</i> statements are needed.</p>
<h2>Temperature Configuration</h2>
<p>On top of the usual features, temperatures can have two specific sub-features: temperature sensor type (tempX_type) and hysteresis values (tempX_max_hyst, tempX_crit_hyst etc.).</p>
<h3>Thermal Sensor Types</h3>
<p>Available thermal sensor types: </p>
<table>
<tr VALIGN=top>
<td ALIGN=right>1</td>
<td>PII/Celeron Diode
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>2</td>
<td>3904 transistor
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>3</td>
<td>thermal diode
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>4</td>
<td>thermistor
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>5</td>
<td>AMD AMDSI
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>6</td>
<td>Intel PECI
</td>
</tr>
</table>
<p> For example, to set temp1 to thermistor type, use: </p>
<dl>
<dd>set temp1_type 4</dl>
<p> Only certain chips support thermal sensor type change, and even these usually only support some of the types above. Please refer to the specific driver documentation to find out which types are supported by your chip. </p>
<p> In theory, the BIOS should have configured the sensor types correctly, so you shouldn&#8217;t have to touch them, but sometimes it isn&#8217;t the case.</p>
<h3>Thermal Hysteresis Mechanism</h3>
<p>Many monitoring chips do not handle the high and critical temperature limits as simple limits. Instead, they have two values for each limit, one which triggers an alarm when the temperature rises and another one which clears the alarm when the temperature falls. The latter is typically a few degrees below the former. This mechanism is known as hysteresis. </p>
<p> The reason for implementing things that way is that high temperature alarms typically trigger an action to attempt to cool the system down, either by scaling down the CPU frequency, or by kicking in an extra fan. This should normally let the temperature fall in a timely manner. If this was clearing the alarm immediately, then the system would be back to its original state where the temperature rises and the alarm would immediately trigger again, causing an undesirable tight fan on, fan off loop. The hysteresis mechanism ensures that the system is really cool before the fan stops, so that it will not have to kick in again immediately. </p>
<p> So, in addition to tempX_max, many chips have a tempX_max_hyst sub-feature. Likewise, tempX_crit often comes with tempX_crit_hyst. tempX_emerg_hyst, tempX_min_hyst and tempX_lcrit_hyst exist too but aren&#8217;t as common. Example: </p>
<dl>
<dd>set temp1_max 60</dl>
<dl>
<dd>set temp1_max_hyst 56</dl>
<p> The hysteresis mechanism can be disabled by giving both limits the same value. </p>
<p> Note that it is strongly recommended to set the hysteresis value after the limit value it relates to in the configuration file. Implementation details on the hardware or driver side may cause unexpected results if the hysteresis value is set first.</p>
<h2>Beeps</h2>
<p>Some chips support alarms with beep warnings. When an alarm is triggered you can be warned by a beeping signal through your computer speaker. On top of per-feature beep flags, there is usually a master beep control switch to enable or disable beeping globally. Enable beeping using: </p>
<dl>
<dd>set beep_enable 1</dl>
<p> or disable it using: </p>
<dl>
<dd>set beep_enable 0</dl>
<h2>Which Statement Applies</h2>
<p>If more than one statement of the same kind applies at a certain moment, the last one in the configuration file is used. So usually, you should put more general <i>chip</i> statements at the top, so you can overrule them below.</p>
<h2>Syntax</h2>
<p>Comments are introduced by hash marks. A comment continues to the end of the line. Empty lines, and lines containing only whitespace or comments are ignored. Other lines have one of the below forms. There must be whitespace between each element, but the amount of whitespace is unimportant. A line may be continued on the next line by ending it with a backslash; this does not work within a comment, <code>NAME</code> or <code>NUMBER</code>. </p>
<dl>
<dd>bus <code>NAME NAME NAME</code> </p>
<p> chip <code>NAME-LIST</code> </p>
<p> label <code>NAME NAME</code> </p>
<p> compute <code>NAME EXPR</code> , <code>EXPR</code> </p>
<p> ignore <code>NAME</code> </p>
<p> set <code>NAME EXPR</code></dl>
<p> A <code>NAME</code> is a string. If it only contains letters, digits and underscores, it does not have to be quoted; in all other cases, you must use double quotes around it. Within quotes, you can use the normal escape-codes from C. </p>
<p> A <code>NAME-LIST</code> is one or more <code>NAME</code> items behind each other, separated by whitespace. </p>
<p> A <code>EXPR</code> is of one of the below forms: </p>
<dl>
<dd><code>NUMBER</code> </p>
<p> <code>NAME</code> </p>
<p> @ </p>
<p> <code>EXPR</code> + <code>EXPR</code> </p>
<p> <code>EXPR</code> &#8211; <code>EXPR</code> </p>
<p> <code>EXPR</code> * <code>EXPR</code> </p>
<p> <code>EXPR</code> / <code>EXPR</code> </p>
<p> &#8211; <code>EXPR</code> </p>
<p> ^ <code>EXPR</code> </p>
<p> ` <code>EXPR</code> </p>
<p> ( <code>EXPR</code> )</dl>
<p> A <code>NUMBER</code> is a floating-point number. `10&#8242;, `10.4&#8242; and `.4&#8242; are examples of valid floating-point numbers; `10.&#8217; or `10E4&#8242; are not valid.</p>
<h2>Files</h2>
<p><i>/etc/sensors3.conf</i><br />
 <i>/etc/sensors.conf</i></p>
<dl>
<dd>The system-wide <code><a href="/docs/linux/man/3-libsensors/">libsensors</a></code>(3) configuration file. /etc/sensors3.conf is tried first, and if it doesn&#8217;t exist, /etc/sensors.conf is used instead.</dl>
<p> <i>/etc/sensors.d</i></p>
<dl>
<dd>A directory where you can put additional libsensors configuration files. Files found in this directory will be processed in alphabetical order after the default configuration file. Files with names that start with a dot are ignored.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-libsensors/">libsensors</a>(3) </p>
<h2>Author</h2>
<p>Frodo Looijaard and the lm_sensors group <a rel="nofollow" href="https://hwmon.wiki.kernel.org/lm_sensors">https://hwmon.wiki.kernel.org/lm_sensors</a></p>
