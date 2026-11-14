---
title: "ibod(4)"
name: "ibod"
section: "4"
letter: "i"
url: "/docs/linux/man/4-ibod/"
---

ibod.cf - configuration file for ibod (ISDN Bandwidth On Demand) 

<h2>Description</h2>

This file contains the initial configuration values for the ibod daemon. Each line contains a keyword and a value. Boolean attributes are set with 0 or 1 which corresponds to false and true respectively. A boolean attribute not specified at all is always false. Lines beginning with # are treated as comments and will be ignored. IMPORTANT RULES! 
 1. Keywords are case sensitive. 
 2. Kewords must begin at the first column. 
 3. Keywords and values must be separated by exactly one (1) space or tab character. This file is re-read every time ibod receives SIGHUP (1) signal.

<h3>Options</h3>

<dl><dt><i>DEVICE &lt;name&gt;</i>
<dd>Name of ISDN PPP device. Default is ippp0.
<dt><i>ENABLE 1|0</i>
<dd>Enable/disable bandwidth-on-demand. Default is enable (1).
<dt><i>INTERVAL &lt;n&gt;</i>
<dd>Specify the sample time interval in ms. Default is 500 ms.
<dt><i>FILTER &lt;n&gt;</i>
<dd>Defines &quot;filtering factor&quot;. A value of 10 means that the average bytes/sec value measured over 10 intervals must pass the limit defined by LIMIT to bring up or down the slave link. Default is 5.
<dt><i>LIMIT &lt;n&gt;</i>
<dd>Transfer rate limit in bytes/sec for bringing up or down ISDN slave channel. Default is 7000.
<dt><i>STAYUP 0|1</i>
<dd>Enable/disable slave channel stay up function. If enabled, the 2:nd cannel (slave link) will stay up even if the average bytes/sec decrease the value defined by LIMIT. In this case the slave link will stay up until hangup time is reached. (Example: isdnctrl huptimeout ippp1 60) If disabled the slave link will be brought down in the same way it was brought up. Default is 0.
<dt><i>STAYUP_TIME &lt;n&gt;</i>
<dd>Defines the minimum time in seconds the 2:nd channel will unconditionally stay up after it has been brought up. Default value is 30. 

<h2>See Also</h2>

<a HREF="/docs/linux/man/1-ibod/">ibod</a>(1) and <a HREF="/docs/linux/man/1-xibod/">xibod</a>(1) 

<h2>Author</h2>

Bjoern Smith, Smith [at] Compound.SE
