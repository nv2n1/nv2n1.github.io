---
title: "nutdrv_qx(8)"
name: "nutdrv_qx"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nutdrv_qx/"
description: "nutdrv_qx – Driver for Q* protocol serial and USB based UPS equipment"
---

<p>nutdrv_qx &#8211; Driver for Q* protocol serial and USB based UPS equipment</p>
<h2>Note</h2>
<p>This man page only documents the hardware-specific features of the <code>nutdrv_qx</code> driver. For information about the core driver, see <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8).</p>
<h2>Supported Hardware</h2>
<p>The <code>nutdrv_qx</code> driver is known to work with various UPSes from <i>Blazer</i>, <i>Energy Sistem</i>, <i>Fenton Technologies</i>, <i>General Electric</i>, <i>Mustek</i>, <i>Voltronic Power</i> (rebranded by many, many &#8211; have I said many? &#8211; others.. Long story short: if your UPS came with a software called <i>Viewpower</i>, chances are high that it works with this driver with one of the <i>voltronic*</i> protocols or with the <i>mecer</i> one) and many others. </p>
<p> The NUT compatibility table lists all the known supported models. Keep in mind, however, that other models not listed there may also be supported, but haven&#8217;t been tested. </p>
<p> All devices with a serial interface and many with a USB interface are supported.</p>
<h2>Extra Arguments</h2>
<p>You may need to override or provide defaults for some values, depending on the make and model of your UPS. </p>
<p> The following are the ones that most likely will need changing (see <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5)): </p>
<p> <code>ondelay =</code> <i>value</i></p>
<dl>
<dd>Time to wait before switching on the UPS (seconds). This value is truncated to units of 60 seconds. </p>
<p> Note that a value below 3 minutes, may cause earlier firmware versions to not switch on automatically, so it defaults to 3 minutes (i.e. 180 seconds). </p>
<p> This option provides a default value for <code>ups.delay.start</code> that will then be used by the driver in the automatic shutdown sequence (i.e. calling the driver with the <code>-k</code> option, calling <code><a href="/docs/linux/man/8-upsdrvctl/">upsdrvctl</a></code>(8) with the <code>shutdown</code> option or when the FSD flag is set and <code><a href="/docs/linux/man/8-upsmon/">upsmon</a></code>(8) enters its shutdown sequence): however you can change this value &#8216;on the fly&#8217; for the actual session, only for the use with instant commands, setting <code>ups.delay.start</code> with <code><a href="/docs/linux/man/8-upsrw/">upsrw</a></code>(8).</dl>
<p> <code>offdelay =</code> <i>value</i></p>
<dl>
<dd>Time to wait before shutting down the UPS (seconds). This value is truncated to units of 6 seconds (less than 60 seconds) or 60 seconds (more than 60 seconds). Defaults to 30 seconds. </p>
<p> This option provides a default value for <code>ups.delay.shutdown</code> that will then be used by the driver in the automatic shutdown sequence (i.e. calling the driver with the <code>-k</code> option, calling <code><a href="/docs/linux/man/8-upsdrvctl/">upsdrvctl</a></code>(8) with the <code>shutdown</code> option or when the FSD flag is set and <code><a href="/docs/linux/man/8-upsmon/">upsmon</a></code>(8) enters its shutdown sequence): however you can change this value &#8216;on the fly&#8217; for the actual session, only for the use with instant commands, setting <code>ups.delay.shutdown</code> with <code><a href="/docs/linux/man/8-upsrw/">upsrw</a></code>(8).</dl>
<p> <code>stayoff</code></p>
<dl>
<dd>If you set stayoff in <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5) when FSD arises the UPS will call a <code>shutdown.stayoff</code> shutting down after <code>ups.delay.shutdown</code> seconds and won&#8217;t return (see KNOWN PROBLEMS), otherwise (standard behaviour) the UPS will call <code>shutdown.return</code> shutting down after <code>ups.delay.shutdown</code> seconds and then turn on after <code>ups.delay.start</code> seconds (if mains meanwhile returned).</dl>
<p> <code>protocol =</code> <i>string</i></p>
<dl>
<dd>Skip autodetection of the protocol to use and only use the one specified. Supported values: <i>mecer</i>, <i>megatec</i>, <i>megatec/old</i>, <i>mustek</i>, <i>q1</i>, <i>voltronic</i>, <i>voltronic-qs</i> and <i>zinto</i>. </p>
<p> Note that if you end up using the <i>q1</i> protocol, you may want to give a try to the <i>mecer</i>, <i>megatec</i> and <i>zinto</i> ones setting the <code>novendor</code>/<code>norating</code> flags (only one, or both).</dl>
<p> <code>pollfreq =</code> <i>value</i></p>
<dl>
<dd>Set polling frequency, in seconds, to reduce the data flow. Between two polling requests the driver will do &#8216;quick polls&#8217; dealing just with ups.status. The default value is 30 (in seconds).</dl>
<p> If your UPS doesn&#8217;t report either <code>battery.charge</code> or <code>battery.runtime</code> you may want to add the following ones in order to have guesstimated values: </p>
<p> <code>default.battery.voltage.high =</code> <i>value</i></p>
<dl>
<dd>Maximum battery voltage that is reached after about 12 to 24 hours charging. If you want the driver to report a guesstimated <code>battery.charge</code>, you need to specify this (see BATTERY CHARGE).</dl>
<p> <code>default.battery.voltage.low =</code> <i>value</i></p>
<dl>
<dd>Minimum battery voltage just before the UPS automatically shuts down. If you want the driver to report a guesstimated <code>battery.charge</code>, you need to specify this (see BATTERY CHARGE).</dl>
<p> <code>default.battery.voltage.nominal =</code> <i>value</i>, <code>override.battery.voltage.nominal =</code> <i>value</i></p>
<dl>
<dd>Some devices show a wrong nominal battery voltage (or none at all), so you may need to override or set a default value.</dl>
<p> <code>override.battery.packs =</code> <i>value</i></p>
<dl>
<dd>Some devices report a part of the total battery voltage. For instance, if <code>battery.voltage.nominal</code> is 24 V, but it reports a <code>battery.voltage</code> of around 2 V, the number of <code>battery.packs</code> to correct this reading would be 12. The driver will attempt to detect this automatically, but if this fails somehow, you may want to override this value.</dl>
<p> <code>runtimecal =</code> <i>value,value,value,value</i></p>
<dl>
<dd>Parameter used in the (optional) runtime estimation. This takes two runtimes at different loads. Typically, this uses the runtime at full load and the runtime at half load. For instance, if your UPS has a rated runtime of 240 seconds at full load and 720 seconds at half load, you would enter </p>
<dl>
<dd>
<pre>runtimecal = 240,100,720,50</pre>
</dl>
<p> The first load should always be higher than the second. If you have values available for loads other than 100 and 50 % respectively, you can use those too, but keep them spaced apart as far as reasonably possible. Just don&#8217;t get too close to no load (prediction of runtime depends more on idle load for the battery then).</dl>
<p> <code>chargetime =</code> <i>value</i></p>
<dl>
<dd>The time needed to fully recharge the battery after being fully discharged. If not specified, the driver defaults to 43200 seconds (12 hours). Only used if <code>runtimecal</code> is also specified.</dl>
<p> <code>idleload =</code> <i>value</i></p>
<dl>
<dd>Minimum battery load used by the driver to estimate the runtime. If not specified, the driver defaults to 10%. Only used if <code>runtimecal</code> is also specified.</dl>
<h3>Mecer, Megataec, Megatec/Old, Mustek, Zinto Protocols</h3>
<p><code>ondelay</code></p>
<dl>
<dd>The acceptable range is 0..599940 seconds.</dl>
<p> <code>offdelay</code></p>
<dl>
<dd>The acceptable range is 12..600 seconds.</dl>
<p> <code>norating</code></p>
<dl>
<dd>Some UPSes will lock up if you attempt to read rating information from them. Setting this flag will make the driver skip this step.</dl>
<p> <code>novendor</code></p>
<dl>
<dd>Some UPSes will lock up if you attempt to read vendor information from them. Setting this flag will make the driver skip this step.</dl>
<h3>Q1 Protocol</h3>
<p><code>ondelay</code></p>
<dl>
<dd>The acceptable range is 0..599940 seconds.</dl>
<p> <code>offdelay</code></p>
<dl>
<dd>The acceptable range is 12..600 seconds.</dl>
<h3>Voltronic-Qs Protocol</h3>
<p><code>ondelay</code></p>
<dl>
<dd>The acceptable range is 60..599940 seconds.</dl>
<p> <code>offdelay</code></p>
<dl>
<dd>The acceptable range is 12..540 seconds.</dl>
<h3>Voltronic Protocol</h3>
<p>The following options are supported only by the <i>voltronic</i> protocol. Not all of them are available on all the UPSes supported by this protocol. </p>
<p> <code>ondelay</code></p>
<dl>
<dd>The acceptable range is 0..599940 seconds.</dl>
<p> <code>offdelay</code></p>
<dl>
<dd>The acceptable range is 12..5940 seconds.</dl>
<p> <code>battery_number =</code> <i>value</i></p>
<dl>
<dd>Set number of batteries that make a pack to <i>value</i> [1..9]. This setting will change the charge and runtime estimation reported by the UPS.</dl>
<p> <code>output_phase_angle =</code> <i>value</i></p>
<dl>
<dd>Changes output phase angle to the provided value [000, 120, 180, 240]&#176;.</dl>
<p> <font SIZE="+1"> <code>UPS CAPABILITY SETTINGS</code></p>
<dl>
<dd><code>reset_to_default</code></p>
<dl>
<dd>Reset capability options and their voltage and frequency limits to safe default values. (<code>Doable only when the UPS is in Standby Mode</code>) </p>
<p> Note that setting this option will reset also <code>ups.start.auto</code>, <code>battery.protection</code>, <code>battery.energysave</code>, <code>ups.start.battery</code>, <code>outlet.0.switchable</code>, <code>input.transfer.high</code>, <code>input.transfer.low</code>, <code>input.frequency.high</code> and <code>input.frequency.low</code>.</dl>
<p> These UPSes can be fine-tuned to suit your needs enabling or disabling the following options (the driver should tell you which one the UPS is capable of on startup: the settable ones will be reported either ar <i>enabled</i> or <i>disabled</i> in the logs): </p>
<p> <code>alarm_control =</code> <i>string</i></p>
<dl>
<dd>Enable or disable alarm (BEEP!) [enabled/disabled]. Settable also &#8216;on the fly&#8217; with <code>beeper.enable</code> and <code>beeper.disable</code> instant commands.</dl>
<p> <code>bypass_alarm =</code> <i>string</i></p>
<dl>
<dd>Enable or disable alarm (BEEP!) at Bypass Mode [enabled/disabled].</dl>
<p> <code>battery_alarm =</code> <i>string</i></p>
<dl>
<dd>Enable or disable alarm (BEEP!) at Battery Mode [enabled/disabled].</dl>
<p> <code>bypass_when_off =</code> <i>string</i></p>
<dl>
<dd>Enable or disable bypass when the UPS is Off [enabled/disabled]. If enabled, AC will directly provide power to connected devices when the UPS is off.</dl>
<p> <code>bypass_forbidding =</code> <i>string</i></p>
<dl>
<dd>Enable or disable Bypass Forbidding [enabled/disabled]. If enabled, the UPS will not transfer to bypass mode under any condition.</dl>
<p> <code>converter_mode =</code> <i>string</i></p>
<dl>
<dd>Enable or disable Converter Mode [enabled/disabled]. When input frequency is within 40 Hz to 70 Hz, the UPS can be set at a constant output frequency, 50 Hz or 60 Hz. The UPS will still charge battery under this mode.</dl>
<p> <code>eco_mode =</code> <i>string</i></p>
<dl>
<dd>Enable or disable ECO Mode [enabled/disabled]. When input voltage/frequency are within acceptable range, the UPS will bypass voltage to output for energy saving. PFC and INVERTER are still active at this mode. Settable also &#8216;on the fly&#8217; with <code>bypass.start</code> and <code>bypass.stop</code> instant commands.</dl>
<p> <code>advanced_eco_mode =</code> <i>string</i></p>
<dl>
<dd>Enable or disable Advanced ECO Mode [enabled/disabled]. When input voltage/frequency are within acceptable range, the UPS will bypass voltage to output for energy saving. PFC and INVERTER are off at this mode.</dl>
<p> <code>battery_open_status_check =</code> <i>string</i></p>
<dl>
<dd>Enable or disable Battery Open Status Check [enabled/disabled]. If enabled, when the UPS is turned on, it will check if the battery is connected or not.</dl>
<p> <code>site_fault_detection =</code> <i>string</i></p>
<dl>
<dd>Enable or disable site fault detection [enabled/disabled]. If enabled, the UPS will beep when the input neutral and hot wires are reversed.</dl>
<p> <code>costant_phase_angle =</code> <i>string</i></p>
<dl>
<dd>Enable or disable Constant Phase Angle Function (output and input phase angles are not equal) [enabled/disabled].</dl>
<p> <code>limited_runtime_on_battery =</code> <i>string</i></p>
<dl>
<dd>Enable or disable limited runtime on battery mode [enabled/disabled].</dl>
</dl>
<p> </font><font SIZE="+2"> <code>BYPASS MODE VOLTAGE/FREQUENCY LIMITS</code></p>
<dl>
<dd>Variables to fine-tune voltage and frequency limits for Bypass mode. These limits are reset to safe default values by <code>reset_to_default</code>. </p>
<p> If AC voltage and frequency are within acceptable range, Bypass mode will be used (If the UPS is capable of and it&#8217;s enabled). </p>
<p> Since these values are device-specific, if your UPS support them, you will get their settable limits printed in the logs on startup. </p>
<p> <code>max_bypass_volt =</code> <i>value</i></p>
<dl>
<dd>Maximum voltage for Bypass Mode (V).</dl>
<p> <code>min_bypass_volt =</code> <i>value</i></p>
<dl>
<dd>Minimum voltage for Bypass Mode (V).</dl>
<p> <code>max_bypass_freq =</code> <i>value</i></p>
<dl>
<dd>Maximum frequency for Bypass Mode (Hz).</dl>
<p> <code>min_bypass_freq =</code> <i>value</i></p>
<dl>
<dd>Minimum frequency for Bypass Mode (Hz).</dl>
</dl>
<p> </font><font SIZE="+3"> <code>OPTIONS SPECIFIC FOR P31 UPSES</code></p>
<dl>
<dd>The following options are available only on P31 UPSes. </p>
<p> <code>work_range_type =</code> <i>string</i></p>
<dl>
<dd>Device grid working range for P31 UPSes [Appliance/UPS].</dl>
</dl>
<p> </font><font SIZE="+4"> <code>TESTING</code></p>
<dl>
<dd>This protocol comes with a couple of functions that are not enabled by default because of the lack of knowledge of some part of the communication protocol used by these UPSes by your friendly neighborhood developer. Since these functions are supposed to be queries to the UPS for some kind of informations, they <i>should</i> not make your UPS go boom. So if you are brave enough to risk your UPS and attached devices&#8217; life to help the developers, this will be very appreciated.. <code>Do it at your own risk</code>. </p>
<p> <code>testing</code></p>
<dl>
<dd>If invoked the driver will exec also commands that still need testing.</dl>
</dl>
<p> </font></p>
<h3>Serial Interface Only</h3>
<p><code>cablepower =</code> <i>string</i></p>
<dl>
<dd>By default the driver will set DTR and clear RTS (<i>normal</i>). If you find that your UPS isn&#8217;t detected or the communication with the UPS is unreliable, you may try if clear DTR and set RTS (<i>reverse</i>), set DTR and RTS (<i>both</i>) or clear DTR and RTS (<i>none</i>) improves this situation.</dl>
<h3>Usb Interface Only</h3>
<p><code>port =</code> <i>string</i></p>
<dl>
<dd>You must set <i>value</i> to <code>auto</code>.</dl>
<p> <code>vendorid =</code> <i>regex</i>, <code>productid =</code> <i>regex</i>, <code>vendor =</code> <i>regex</i>, <code>product =</code> <i>regex</i>, <code>serial =</code> <i>regex</i></p>
<dl>
<dd>Select a specific UPS, in case there is more than one connected via USB. Each option specifies an extended regular expression (see <code><a href="/docs/linux/man/7-regex/">regex</a>(7)</code>) that must match the UPS&#8217;s entire vendor/product/serial string (minus any surrounding whitespace), or the whole 4-digit hexadecimal code for vendorid and productid. Try <code>-DD</code> for finding out the strings to match. </p>
<p> Examples: </p>
<dl>
<dd>&bull; </p>
<p> -x vendor=&quot;Foo.Corporation.*&quot;</dl>
<dl>
<dd>&bull; </p>
<p> -x vendorid=051d* (APC)</dl>
<dl>
<dd>&bull; </p>
<p> -x product=&quot;.*(Smart|Back)-?UPS.*&quot;</dl>
</dl>
<p> <code>bus =</code> <i>regex</i></p>
<dl>
<dd>Select a UPS on a specific USB bus or group of busses. The argument is a regular expression that must match the bus name where the UPS is connected (e.g. bus=&quot;002&quot;, bus=&quot;00[2-3]&quot;).</dl>
<p> <code>subdriver =</code> <i>string</i></p>
<dl>
<dd>Select a serial-over-USB subdriver to use. You have a choice between <code>phoenix</code>, <code>ippon</code>, <code>cypress</code>, and <code>krauler</code>. When using this option, it is mandatory to also specify the <code>vendorid</code> and <code>productid</code>.</dl>
<p> <code>langid_fix =</code> <i>value</i></p>
<dl>
<dd>Apply the language ID workaround to the <code>krauler</code> subdriver. This is mandatory for some devices to work (LDLC, Dynamix and others). You must provide <code>value</code> (0x409 or 0x4095), according to your device entry in NUT hardware compatibility list (HCL).</dl>
<h2>Ups Commands</h2>
<p>This driver supports some instant commands (see <code><a href="/docs/linux/man/8-upscmd/">upscmd</a></code>(8)): </p>
<p> <code>beeper.toggle</code></p>
<dl>
<dd>Toggle the UPS beeper. (Not available on some hardware)</dl>
<p> <code>load.on</code></p>
<dl>
<dd>Turn on the load immediately.</dl>
<p> <code>load.off</code></p>
<dl>
<dd>Turn off the load immediately (see KNOWN PROBLEMS).</dl>
<p> <code>shutdown.return</code></p>
<dl>
<dd>Turn off the load and return when power is back. Uses the timers defined by <code>ups.delay.start</code> and <code>ups.delay.shutdown</code>.</dl>
<p> <code>shutdown.stayoff</code></p>
<dl>
<dd>Turn off the load and remain off (see KNOWN PROBLEMS). Uses the timer defined by <code>ups.delay.shutdown</code>.</dl>
<p> <code>shutdown.stop</code></p>
<dl>
<dd>Stop a shutdown in progress.</dl>
<p> <code>test.battery.start.deep</code></p>
<dl>
<dd>Perform a long battery test. (Not available on some hardware)</dl>
<p> <code>test.battery.start.quick</code></p>
<dl>
<dd>Perform a quick (10 second) battery test.</dl>
<p> <code>test.battery.stop</code></p>
<dl>
<dd>Stop a running battery test. (Not available on some hardware)</dl>
<h3>Mecer, Megatec, Megatec/Old, Mustek, Q1, Zinto Protocols</h3>
<p><code>test.battery.start</code> <i>value</i></p>
<dl>
<dd>Perform a battery test for the duration of <i>value</i> seconds (truncated to 60 seconds) [60..5940].</dl>
<p> <font SIZE="+1"> <code>VOLTRONIC POWER P98 UNITS (WITH MECER PROTOCOL)</code></p>
<dl>
<dd><code>test.battery.start</code> <i>value</i></p>
<dl>
<dd>Perform a battery test for the duration of <i>value</i> seconds (truncated to 60 seconds) [12..5940]. This value is truncated to units of 6 seconds (less than 60 seconds) or 60 seconds (more than 60 seconds).</dl>
</dl>
<p> </font></p>
<h3>Voltronic Protocol</h3>
<p>The following instant commands are available for the <i>voltronic</i> protocol. Not all of them are available on all the UPSes supported by this protocol. </p>
<p> <code>beeper.enable</code></p>
<dl>
<dd>Enable the UPS beeper.</dl>
<p> <code>beeper.disable</code></p>
<dl>
<dd>Disable the UPS beeper.</dl>
<p> <code>test.battery.start</code> <i>value</i></p>
<dl>
<dd>Perform a battery test for the duration of <i>value</i> seconds [12..5940]. This value is truncated to units of 6 seconds (less than 60 seconds) or 60 seconds (more than 60 seconds).</dl>
<p> <code>outlet.1.load.off</code></p>
<dl>
<dd>Turn off outlet 1 load immediately.</dl>
<p> <code>outlet.1.load.on</code></p>
<dl>
<dd>Turn on outlet 1 load immediately.</dl>
<p> <code>outlet.2.load.off</code></p>
<dl>
<dd>Turn off outlet 2 load immediately.</dl>
<p> <code>outlet.2.load.on</code></p>
<dl>
<dd>Turn on outlet 2 load immediately.</dl>
<p> <code>outlet.3.load.off</code></p>
<dl>
<dd>Turn off outlet 3 load immediately.</dl>
<p> <code>outlet.3.load.on</code></p>
<dl>
<dd>Turn on outlet 3 load immediately.</dl>
<p> <code>outlet.4.load.off</code></p>
<dl>
<dd>Turn off outlet 4 load immediately.</dl>
<p> <code>outlet.4.load.on</code></p>
<dl>
<dd>Turn on outlet 4 load immediately.</dl>
<p> <code>bypass.start</code></p>
<dl>
<dd>Put the UPS in ECO Mode.</dl>
<p> <code>bypass.stop</code></p>
<dl>
<dd>Take the UPS out of ECO Mode.</dl>
<h2>Battery Charge</h2>
<p>Due to popular demand, this driver will report a guesstimated <code>battery.charge</code> and optionally <code>battery.runtime</code>, provided you specified a couple of the EXTRA ARGUMENTS listed above. </p>
<p> If you specify both <code>battery.voltage.high</code> and <code>battery.voltage.low</code> in <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5), but don&#8217;t enter <code>runtimecal</code>, it will guesstimate the state of charge by looking at the battery voltage alone. This is not reliable under load, as this only gives reasonably accurate readings if you disconnect the load, let the battery rest for a couple of minutes and then measure the open cell voltage. This just isn&#8217;t practical if the power went out and the UPS is providing power for your systems. </p>
<dl>
<dd>
<pre> battery.voltage - battery.voltage.low
battery.charge = ------------------------------------------ x 100 %
 battery.voltage.high - battery.voltage.low</pre>
</dl>
<p> There is a way to get better readings without disconnecting the load but this requires one to keep track on how much (and how fast) current is going in and out of the battery. If you specified the <code>runtimecal</code>, the driver will attempt to do this. Note however, that this heavily relies on the values you enter and that the UPS must be able to report the load as well. There are quite a couple of devices that report 0 % (or any other fixed value) at all times, in which case this obviously doesn&#8217;t work. </p>
<p> The driver also has no way of determining the degradation of the battery capacity over time, so you&#8217;ll have to deal with this yourself (by adjusting the values in <code>runtimecal</code>). Also note that the driver guesses the initial state of charge based on the battery voltage, so this may be less than 100 %, even when you are certain that they are full. There is just no way to reliably measure this between 0 and 100 % full charge. </p>
<p> This is better than nothing (but not by much). If any of the above calculations is giving you incorrect readings, you are the one that put in the values in <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5), so don&#8217;t complain with the author. If you need something better, buy a UPS that reports <code>battery.charge</code> and <code>battery.runtime</code> all by itself without the help of a NUT driver.</p>
<h2>Notes For The Previous User Of Megatec Drivers</h2>
<p>The <code>nutdrv_qx</code> driver having replaced the megatec ones, some configuration changes may be required by users switching to <code>nutdrv_qx</code>. </p>
<p> Part of this, the following megatec options, in <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5), have to be changed: </p>
<p> <code>battvolts</code></p>
<dl>
<dd>You need to use <i>default.battery.voltage.high</i> and <i>default.battery.voltage.low</i></dl>
<p> <code>dtr</code> and <code>rts</code></p>
<dl>
<dd>You need to use <i>cablepower</i></dl>
<p> <code>ignoreoff</code></p>
<dl>
<dd>This parameter can simply be discarded, since it was a wrong understanding of the specification.</dl>
<h2>Notes For The Previous User Of Blazer Drivers</h2>
<p>The <code>nutdrv_qx</code> driver having replaced the blazer ones, some configuration changes may be required by users switching to <code>nutdrv_qx</code>. </p>
<p> Part of this, the following blazer options, in <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5), have to be changed: </p>
<p> <code>ondelay</code></p>
<dl>
<dd>While the previous blazer drivers expected minutes, the new <code>nutdrv_qx</code> driver wants seconds.</dl>
<p> The following instant command has also been changed: </p>
<p> <code>test.battery.start</code> <i>value</i></p>
<dl>
<dd>While the old blazer drivers expected a <i>value</i> in minutes, the <code>nutdrv_qx</code> driver wants a <i>value</i> in seconds.</dl>
<h2>Notes For The Previous User Of Voltronic Drivers</h2>
<p>The <code>nutdrv_qx</code> driver having replaced the voltronic ones, some configuration changes may be required by users switching to <code>nutdrv_qx</code>. </p>
<p> Part of this, the following voltronic options, in <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5), have to be changed: </p>
<p> <code>ondelay</code></p>
<dl>
<dd>While the previous voltronic drivers expected minutes, the new <code>nutdrv_qx</code> driver wants seconds. It no longer defaults to 0 minutes but to 3 minutes (i.e. 180 seconds) for compatibility with the users switching from the old blazer drivers.</dl>
<p> <code>battnumb</code></p>
<dl>
<dd>This option has been renamed to <code>battery_number</code>.</dl>
<p> The following options are no longer supported by this driver, you can now change them more conveniently &#8216;on the fly&#8217; calling <code><a href="/docs/linux/man/8-upsrw/">upsrw</a></code>(8) with the appropriate NUT variable &#8211; provided that your UPS supports them. </p>
<table>
<tr VALIGN=top>
<td>
<p> <code>battpacks</code> </td>
<td>
<p> → <code>battery.packs</code> </p>
<p> Set number of battery packs in parallel [1..99]. This setting will change the charge and runtime estimation reported by the UPS.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>battlow</code> </td>
<td>
<p> → <code>battery.voltage.low</code> </p>
<p> Set minimum battery voltage just before the UPS automatically shuts down. This setting will change the charge and runtime estimation reported by the UPS.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>auto_reboot</code> </td>
<td>
<p> → <code>ups.start.auto</code> </p>
<p> Enable or disable auto reboot [enabled/disabled]. If enabled, the UPS will auto recover when AC power returns.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>battery_protection</code> </td>
<td>
<p> → <code>battery.protection</code> </p>
<p> Enable or disable battery deep discharge protection [enabled/disabled].
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>energy_saving</code> </td>
<td>
<p> → <code>battery.energysave</code> </p>
<p> Enable or disable Green power function [enabled/disabled]. If enabled, for energy saving, the UPS will auto off when there is no load.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>cold_start</code> </td>
<td>
<p> → <code>ups.start.battery</code> </p>
<p> Enable or disable Cold Start [enabled/disabled]. If enabled, the UPS can be turned on also if AC is not connected to the UPS.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>outlet_control</code> </td>
<td>
<p> → <code>outlet.0.switchable</code> </p>
<p> Enable or disable programmable outlets control at battery mode [enabled/disabled]. If enabled, the UPS will cut off programmable outlets after backup time (set through <code>outlet.</code>{<code>1</code>,<code>2</code>,<code>3</code>,<code>4</code>}<code>.delay.shutdown</code>) arrives. If disabled, the UPS will provide continuous power to programmable outlets until the battery is running out.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>max_eco_volt</code> </td>
<td>
<p> → <code>input.transfer.high</code> </p>
<p> Maximum voltage for ECO Mode (V). If AC voltage is within acceptable range, ECO mode will be used (If the UPS is capable of and it&#8217;s enabled).
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>min_eco_volt</code> </td>
<td>
<p> → <code>input.transfer.low</code> </p>
<p> Minimum voltage for ECO Mode (V). If AC voltage is within acceptable range, ECO mode will be used (If the UPS is capable of and it&#8217;s enabled).
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>max_eco_freq</code> </td>
<td>
<p> → <code>input.frequency.high</code> </p>
<p> Maximum frequency for ECO Mode (Hz). If AC frequency is within acceptable range, ECO mode will be used (If the UPS is capable of and it&#8217;s enabled).
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>min_eco_freq</code> </td>
<td>
<p> → <code>input.frequency.low</code> </p>
<p> Minimum frequency for ECO Mode (Hz). If AC frequency is within acceptable range, ECO mode will be used (If the UPS is capable of and it&#8217;s enabled).
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>outlet1_delay</code> </td>
<td>
<p> → <code>outlet.1.delay.shutdown</code> </p>
<p> Delay time before programmable outlet 1 shuts down the load when on battery mode [0..59940] (seconds).
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>outlet2_delay</code> </td>
<td>
<p> → <code>outlet.2.delay.shutdown</code> </p>
<p> Delay time before programmable outlet 2 shuts down the load when on battery mode [0..59940] (seconds).
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>outlet3_delay</code> </td>
<td>
<p> → <code>outlet.3.delay.shutdown</code> </p>
<p> Delay time before programmable outlet 3 shuts down the load when on battery mode [0..59940] (seconds).
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>outlet4_delay</code> </td>
<td>
<p> → <code>outlet.4.delay.shutdown</code> </p>
<p> Delay time before programmable outlet 4 shuts down the load when on battery mode [0..59940] (seconds).
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>batt_type</code> </td>
<td>
<p> → <code>battery.type</code> </p>
<p> Battery type (for P31 UPSes only) [Li/Flooded/AGM].
</td>
</tr>
</table>
<h2>Known Problems</h2>
<p>Some UPS commands aren&#8217;t supported by all models. In most cases, the driver will send a message to the system log when the user tries to execute an unsupported command. Unfortunately, some models don&#8217;t even provide a way for the driver to check for this, so the unsupported commands will silently fail. </p>
<p> Both the <code>load.off</code> and <code>shutdown.stayoff</code> instant commands are meant to turn the load off indefinitely. However, some UPS models don&#8217;t allow this. </p>
<p> Some models report a bogus value for the beeper status (will always be <i>enabled</i> or <i>disabled</i>). So, the <code>beeper.toggle</code> command may appear to have no effect in the status reported by the driver when, in fact, it is working fine. </p>
<p> The temperature and load value is known to be bogus in some models.</p>
<h3>Voltronic-Qs Units</h3>
<p>Both <code>load.off</code> and <code>shutdown.stayoff</code> instant commands are known to work as expected (i.e. turn the load off indefinitely) only if mains is present, otherwise, as soon as mains returns the load will be powered. </p>
<p> After issuing a <code>shutdown.return</code> instant command, the UPS won&#8217;t wait <code>ondelay</code> before powering on the load, provided the following conditions are met: </p>
<dl>
<dd>&bull; if the load has been previously (no matter how long before) powered off through <code>load.off</code>/<code>shutdown.stayoff</code> <i>and</i> powered on through <code>load.on</code>/<code>shutdown.stop</code> <i>and</i></dl>
<dl>
<dd>&bull; if AC wasn&#8217;t cut after issuing the <code>load.off</code>/<code>shutdown.stayoff</code> (i.e. the UPS didn&#8217;t turn itself off) <i>and</i></dl>
<dl>
<dd>&bull; if there&#8217;s a power outage after issuing the <code>shutdown.return</code> command</dl>
<p> In this case, as soon as mains returns the load will be powered.</p>
<h2>Ups Warnings (Voltronic Protocol)</h2>
<p>The UPSes supported by <i>voltronic</i> protocol report warnings through a 64bit flag (bit1bit2&#8230;bit63bit64) where 1 means that a warning arose, while 0 means no warning. Since more than one warning at a time can be signaled, and because of the limited space in the ups.alarm variable, if the length of the warnings exceeds that of ups.alarms variable, they will be reported as bits. If you want to know the explanation of that bit you can either watch the log or see the next table (unlisted bits equal to unknown warnings). </p>
<p> <code>Table 1. UPS Warnings for </code><i>voltronic</i> UPSes </p>
<table BORDER>
<tr VALIGN=top>
<td ALIGN=right><code> # </code></td>
<td><code> Corresponding Warning </code>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 1 </td>
<td>
<p> Battery disconnected
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 2 </td>
<td>
<p> Neutral not connected
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 3 </td>
<td>
<p> Site fault
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 4 </td>
<td>
<p> Phase sequence incorrect
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 5 </td>
<td>
<p> Phase sequence incorrect in bypass
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 6 </td>
<td>
<p> Input frequency unstable in bypass
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 7 </td>
<td>
<p> Battery overcharged
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 8 </td>
<td>
<p> Low battery
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 9 </td>
<td>
<p> Overload alarm
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 10 </td>
<td>
<p> Fan alarm
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 11 </td>
<td>
<p> EPO enabled
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 12 </td>
<td>
<p> Unable to turn on UPS
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 13 </td>
<td>
<p> Over temperature alarm
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 14 </td>
<td>
<p> Charger alarm
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 15 </td>
<td>
<p> Remote auto shutdown
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 16 </td>
<td>
<p> L1 input fuse not working
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 17 </td>
<td>
<p> L2 input fuse not working
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 18 </td>
<td>
<p> L3 input fuse not working
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 19 </td>
<td>
<p> Positive PFC abnormal in L1
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 20 </td>
<td>
<p> Negative PFC abnormal in L1
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 21 </td>
<td>
<p> Positive PFC abnormal in L2
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 22 </td>
<td>
<p> Negative PFC abnormal in L2
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 23 </td>
<td>
<p> Positive PFC abnormal in L3
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 24 </td>
<td>
<p> Negative PFC abnormal in L3
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 25 </td>
<td>
<p> Abnormal in CAN-bus communication
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 26 </td>
<td>
<p> Abnormal in synchronous signal circuit
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 27 </td>
<td>
<p> Abnormal in synchronous pulse signal circuit
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 28 </td>
<td>
<p> Abnormal in host signal circuit
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 29 </td>
<td>
<p> Male connector of parallel cable not connected well
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 30 </td>
<td>
<p> Female connector of parallel cable not connected well
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 31 </td>
<td>
<p> Parallel cable not connected well
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 32 </td>
<td>
<p> Battery connection not consistent in parallel systems
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 33 </td>
<td>
<p> AC connection not consistent in parallel systems
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 34 </td>
<td>
<p> Bypass connection not consistent in parallel systems
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 35 </td>
<td>
<p> UPS model types not consistent in parallel systems
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 36 </td>
<td>
<p> Capacity of UPSs not consistent in parallel systems
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 37 </td>
<td>
<p> Auto restart setting not consistent in parallel systems
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 38 </td>
<td>
<p> Battery cell over charge
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 39 </td>
<td>
<p> Battery protection setting not consistent in parallel systems
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 40 </td>
<td>
<p> Battery detection setting not consistent in parallel systems
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 41 </td>
<td>
<p> Bypass not allowed setting not consistent in parallel systems
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 42 </td>
<td>
<p> Converter setting not consistent in parallel systems
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 43 </td>
<td>
<p> High loss point for frequency in bypass mode not consistent in parallel systems
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 44 </td>
<td>
<p> Low loss point for frequency in bypass mode not consistent in parallel systems
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 45 </td>
<td>
<p> High loss point for voltage in bypass mode not consistent in parallel systems
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 46 </td>
<td>
<p> Low loss point for voltage in bypass mode not consistent in parallel systems
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 47 </td>
<td>
<p> High loss point for frequency in AC mode not consistent in parallel systems
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 48 </td>
<td>
<p> Low loss point for frequency in AC mode not consistent in parallel systems
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 49 </td>
<td>
<p> High loss point for voltage in AC mode not consistent in parallel systems
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 50 </td>
<td>
<p> Low loss point for voltage in AC mode not consistent in parallel systems
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 51 </td>
<td>
<p> Warning for locking in bypass mode after 3 consecutive overloads within 30 min
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 52 </td>
<td>
<p> Warning for three-phase AC input current unbalance
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 53 </td>
<td>
<p> Warning for a three-phase input current unbalance detected in battery mode
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 54 </td>
<td>
<p> Warning for Inverter inter-current unbalance
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 55 </td>
<td>
<p> Programmable outlets cut off pre-alarm
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 56 </td>
<td>
<p> Warning for Battery replace
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 57 </td>
<td>
<p> Abnormal warning on input phase angle
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 58 </td>
<td>
<p> Warning!! Cover of maintain switch is open
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>
<p> 62 </td>
<td>
<p> EEPROM operation error
</td>
</tr>
</table>
<h2>Authors</h2>
<p>Daniele Pezzini &lt;hyouko [at] gmail.com&gt;, Arnaud Quette &lt;arnaud.quette [at] gmail.com&gt;, John Stamp &lt;kinsayder [at] hotmail.com&gt;, Peter Selinger &lt;selinger [at] users.sourceforge.net&gt;, Arjen de Korte &lt;adkorte-guest [at] alioth.debian.org&gt;, Alexander Gordeev &lt;lasaine [at] lvk.cs.msu.su&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-blazer_ser/">blazer_ser</a></code>(8), <code><a href="/docs/linux/man/8-blazer_usb/">blazer_usb</a></code>(8), <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8), <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5), <code><a href="/docs/linux/man/8-upsc/">upsc</a></code>(8), <code><a href="/docs/linux/man/8-upscmd/">upscmd</a></code>(8), <code><a href="/docs/linux/man/8-upsdrvctl/">upsdrvctl</a></code>(8), <code><a href="/docs/linux/man/8-upsmon/">upsmon</a></code>(8), <code><a href="/docs/linux/man/8-upsrw/">upsrw</a></code>(8)</p>
<h3>Internet Resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> The NUT HCL: <a rel="nofollow" href="http://www.networkupstools.org/stable-hcl.html">http://www.networkupstools.org/stable-hcl.html</a> </p>
