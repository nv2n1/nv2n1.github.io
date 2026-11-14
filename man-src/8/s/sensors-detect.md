---
title: "sensors-detect(8)"
name: "sensors-detect"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sensors-detect/"
description: "sensors-detect – detect hardware monitoring chips"
---

<p>sensors-detect &#8211; detect hardware monitoring chips</p>
<h2>Synopsis</h2>
<p><code>sensors-detect [</code> <i>&#8211;auto</i> <code>]</code> </p>
<h2>Description</h2>
<p>sensors-detect is an interactive program that will walk you through the process of scanning your system for various hardware monitoring chips, or sensors, supported by <a href="/docs/linux/man/3-libsensors/">libsensors</a>(3), or more generally by the lm_sensors tool suite. sensors-detect will look for the following devices, in order:</p>
<dl>
<dt>&bull;</p>
<dd>Sensors embedded in CPUs, south bridges and memory controllers.</p>
<dt>&bull;</p>
<dd>Sensors embedded in Super I/O chips.</p>
<dt>&bull;</p>
<dd>Hardware monitoring chips accessed through ISA I/O ports.</p>
<dt>&bull;</p>
<dd>Hardware monitoring chips reachable over the SMBus or more generally any I2C bus on your system.</dl>
<p> As the last two detection steps can cause trouble on some systems, they are normally not attempted if the second detection step led to the discovery of a Super I/O chip with complete hardware monitoring features. However, the user is always free to ask for all detection steps if so is his/her wish. This can be useful if a given system has more than one hardware monitoring chip. Some vendors are known to do this, most notably Asus and Tyan. </p>
<h2>Options</h2>
<dl>
<dt>&#8211;auto</p>
<dd>Run in automatic, non-interactive mode. Assume default answers to all questions. Note that this isn&#8217;t necessarily safe as the internal logic may lead to potentially dangerous probes being attempted. See the WARNING section below. </p>
</dl>
<h2>Warning</h2>
<p>sensors-detect needs to access the hardware for most of the chip detections. By definition, it doesn&#8217;t know which chips are there before it manages to identify them. This means that it can access chips in a way these chips do not like, causing problems ranging from SMBus lockup to permanent hardware damage (a rare case, thankfully.) </p>
<p> The authors made their best to make the detection as safe as possible, and it turns out to work just fine in most cases, however it is impossible to guarantee that sensors-detect will not lock or kill a specific system. So, as a rule of thumb, you should not run sensors-detect on production servers, and you should not run sensors-detect if can&#8217;t afford replacing a random part of your system. Also, it is recommended to not force a detection step which would have been skipped by default, unless you know what you are doing.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-sensors/">sensors</a>(1), <a href="/docs/linux/man/3-libsensors/">libsensors</a>(3) </p>
<h2>Author</h2>
<p>Frodo Looijaard and Jean Delvare</p>
