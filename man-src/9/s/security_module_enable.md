---
title: "security_module_enable(9)"
name: "security_module_enable"
section: "9"
letter: "s"
url: "/docs/linux/man/9-security_module_enable/"
---

security_module_enable - Load given security module on boot ?

<h2>Synopsis</h2>

<pre><code>int security_module_enable(const char *module);</code></pre>

<h2>Arguments</h2>

<i>module</i>
<dl><dd><dd>the name of the module</dl>

<h2>Description</h2>

Each LSM must pass this method before registering its own operations to avoid security registration races. This method may also be used to check if your LSM is currently loaded during kernel initialization. 

 Return true if: -The passed LSM is the one chosen by user at boot time, -or the passed LSM is configured as the default and the user did not choose an alternate LSM at boot time. Otherwise, return false.

<h2>Copyright</h2>


