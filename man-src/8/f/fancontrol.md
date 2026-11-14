---
title: "fancontrol(8)"
name: "fancontrol"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fancontrol/"
description: "fancontrol – automated software based fan speed regulation"
---

<p>fancontrol &#8211; automated software based fan speed regulation </p>
<h2>Synopsis</h2>
<p><code>fancontrol</code> <i>[configfile]</i> </p>
<h2>Description</h2>
<p><code>fancontrol</code> is a shell script for use with lm_sensors. It reads its configuration from a file, then calculates fan speeds from temperatures and sets the corresponding PWM outputs to the computed values. </p>
<h2>Warning</h2>
<p>Please be careful when using the fan control features of your mainboard, in addition to the risk of burning your CPU, at higher temperatures there will be a higher wearout of your other hardware components, too. So if you plan to use these components in 50 years, <code>maybe</code> you shouldn&#8217;t use fancontrol at all. Also please keep in mind most fans aren&#8217;t designed to be powered by a PWMed voltage. </p>
<p> In practice it doesn&#8217;t seem to be a major issue, the fans will get slightly warmer, just be sure to have a temperature alarm and/or shutdown call, in case some fan fails, because you probably won&#8217;t hear it anymore ;)</p>
<h2>Configuration</h2>
<p>For easy configuration, there&#8217;s a script named <code><a href="/docs/linux/man/8-pwmconfig/">pwmconfig</a></code>(8) which lets you interactively write your configuration file for <code>fancontrol</code>. Alternatively you can write this file yourself using the information from this manpage. </p>
<p> Since most of you are going to use <code><a href="/docs/linux/man/8-pwmconfig/">pwmconfig</a></code>(8) script, the config file syntax will be discussed last. First I&#8217;m going to describe the various variables available for changing <code>fancontrol</code>&#8216;s behaviour: </p>
<dl>
<dt><code>INTERVAL</code></p>
<dd>This variable defines at which interval in seconds the main loop of <code>fancontrol</code> will be executed</p>
<dt><code>DEVPATH</code></p>
<dd>Maps hwmon class devices to physical devices. This lets <code>fancontrol</code> check that the configuration file is still up-to-date.</p>
<dt><code>DEVNAME</code></p>
<dd>Records hwmon class device names. This lets <code>fancontrol</code> check that the configuration file is still up-to-date.</p>
<dt><code>FCTEMPS</code></p>
<dd>Maps PWM outputs to temperature sensors so <code>fancontrol</code> knows which temperature sensors should be used for calculation of new values for the corresponding PWM outputs.</p>
<dt><code>FCFANS</code></p>
<dd>Records the association between a PWM output and a fan input. Then <code>fancontrol</code> can check the fan speed and restart it if it stops unexpectedly.</p>
<dt><code>MINTEMP</code></p>
<dd>The temperature below which the fan gets switched to minimum speed.</p>
<dt><code>MAXTEMP</code></p>
<dd>The temperature over which the fan gets switched to maximum speed.</p>
<dt><code>MINSTART</code></p>
<dd>Sets the minimum speed at which the fan begins spinning. You should use a safe value to be sure it works, even when the fan gets old.</p>
<dt><code>MINSTOP</code></p>
<dd>The minimum speed at which the fan still spins. Use a safe value here, too.</p>
<dt><code>MINPWM</code></p>
<dd>The PWM value to use when the temperature is below MINTEMP. Typically, this will be either 0 if it is OK for the fan to plain stop, or the same value as MINSTOP if you don&#8217;t want the fan to ever stop. If this value isn&#8217;t defined, it defaults to 0 (stopped fan).</p>
<dt><code>MAXPWM</code></p>
<dd>The PWM value to use when the temperature is over MAXTEMP. If this value isn&#8217;t defined, it defaults to 255 (full speed).</dl>
<p> The configuration file format is a bit strange:</p>
<dl>
<dd>
<pre>VARIABLE=chip/pwmdev=value chip/pwmdev2=value2
VARIABLE2=...</pre>
</dl>
<p> Each variable has its own line. The variable name is followed by an equal sign and the device=value pairs. These consist of the path to the pwm output for which the value is valid, equal sign followed by the value and are separated by a blank. Path can be absolute or relative (from /sys/bus/i2c/devices or /sys/class/hwmon depending on the kernel version). Example:</p>
<dl>
<dd>MINTEMP=hwmon0/device/pwm1=40 hwmon0/device/pwm2=54</dl>
<p> You have to play with the temperature values a bit to get happy. For initial setup I recommend using the <code>pwmconfig</code> script. Small changes can be made by editing the config file directly following the rules above. </p>
<p> Upon starting, fancontrol will make sure that all referenced devices do exist and match what they were at configuration time, and that all referenced sysfs files do exist. If not, it will quit immediately, upon the assumption that the configuration file may be out-of-sync with the loaded kernel drivers.</p>
<h2>The Algorithm</h2>
<p><code>fancontrol</code> first reads its configuration, writes it to arrays and loops its main function. This function gets the temperatures and fanspeeds from kernel driver files and calculates new speeds depending on temperature changes, but only if the temp is between MINTEMP and MAXTEMP. After that, the new values are written to the PWM outputs. Currently the speed increases quadratically with rising temperature. This way you won&#8217;t hear your fans most of the time at best.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-pwmconfig/">pwmconfig</a>(8), <a href="/docs/linux/man/1-sensors/">sensors</a>(1). </p>
<h2>Author</h2>
<p>Marius Reiner &lt;marius.reiner [at] hdev.de&gt;</p>
