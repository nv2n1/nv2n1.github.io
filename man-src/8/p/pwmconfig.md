---
title: "pwmconfig(8)"
name: "pwmconfig"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pwmconfig/"
description: "pwmconfig – tests the PWM outputs of sensors and configures fancontrol"
---

<p>pwmconfig &#8211; tests the PWM outputs of sensors and configures fancontrol </p>
<h2>Synopsis</h2>
<p><code>pwmconfig</code> </p>
<h2>Warning</h2>
<p><code>pwmconfig</code> will attempt to stop your fans, one at a time, for approximately 5 seconds each. This may cause your processor temperature to rise. Verify that all fans are running at normal speed after this program has exited. <code>pwmconfig</code> does its best to check that the fans are spinning when they are supposed to, but due to the diversity of available motherboards and fans, it shouldn&#8217;t be blindly trusted. Always verify by yourself. </p>
<p> It is strongly recommended to run <code>pwmconfig</code> at a time when there is no significant system load, to minimize the risk of overheating.</p>
<h2>Description</h2>
<p><code>pwmconfig</code> searches your sensors for pulse width modulation (PWM) controls, and tests each one to see if it controls a fan on your motherboard. Note that many motherboards do not have PWM circuitry installed, even if your sensor chip supports PWM. When a connection is established between a PWM control and a fan, <code>pwmconfig</code> can generate a detailed correlation, to show how a given fan is responding to various PWM duty cycles. Lastly, <code>pwmconfig</code> will enter in <code>fancontrol</code> configuration mode (unless you decide to skip that part.) In this mode, you are invited to enter several parameters which will determine how the <code>fancontrol</code> daemon regulates the speed of one or more fans in your system based on temperature measurements. In particular, you will have the opportunity to establish mappings between fans and temperature inputs, define the temperature range over which the speed of the fan should be adjusted dynamically, the minimum speed at which the fan should spin, etc. See <a href="/docs/linux/man/8-fancontrol/">fancontrol</a>(8) for additional information. </p>
<h2>Bugs</h2>
<p>The term &quot;PWM&quot; is used because most fan control systems in computers are based on pulse width modulation. Some motherboards however use DC variation instead. So, the term &quot;PWM&quot; should be seen as a generic term for &quot;fan speed control&quot;, regardless of the actual method used. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-fancontrol/">fancontrol</a>(8), <a href="/docs/linux/man/1-sensors/">sensors</a>(1). </p>
<h2>Authors</h2>
<p>Marius Reiner &lt;marius.reiner [at] hdev.de&gt;, Jean Delvare &lt;jdelvare [at] suse.de&gt;</p>
