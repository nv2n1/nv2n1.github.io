---
title: "qemu-cpu-models(7)"
name: "qemu-cpu-models"
section: "7"
letter: "q"
url: "/docs/linux/man/7-qemu-cpu-models/"
description: "qemu-cpu-models – QEMU / KVM CPU model configuration"
---

<p>qemu-cpu-models &#8211; QEMU / KVM CPU model configuration</p>
<h2>Synopsis</h2>
<p>QEMU / KVM CPU model configuration</p>
<h2>Description</h2>
<p>QEMU / KVM virtualization supports two ways to configure CPU models</p>
<dl>
<dt><code>Host passthrough</code></dt>
<dd>This passes the host CPU model features, model, stepping, exactly to the guest. Note that KVM may filter out some host CPU model features if they cannot be supported with virtualization. Live migration is unsafe when this mode is used as libvirt / QEMU cannot guarantee a stable CPU is exposed to the guest across hosts. This is the recommended CPU to use, provided live migration is not required.</dd>
<dt><code>Named model</code></dt>
<dd>QEMU comes with a number of predefined named CPU models, that typically refer to specific generations of hardware released by Intel and AMD. These allow the guest VMs to have a degree of isolation from the host CPU, allowing greater flexibility in live migrating between hosts with differing hardware.</dd></dl>
<p> In both cases, it is possible to optionally add or remove individual CPU features, to alter what is presented to the guest by default. </p>
<p> Libvirt supports a third way to configure CPU models known as &#8220;Host model&#8221;. This uses the QEMU &#8220;Named model&#8221; feature, automatically picking a CPU model that is similar the host CPU, and then adding extra features to approximate the host model as closely as possible. This does not guarantee the CPU family, stepping, etc will precisely match the host CPU, as they would with &#8220;Host passthrough&#8221;, but gives much of the benefit of passthrough, while making live migration safe. </p>
<p> <i>Recommendations for </i><i>KVM CPU</i><i> model configuration on x86 hosts</i> </p>
<p> The information that follows provides recommendations for configuring CPU models on x86 hosts. The goals are to maximise performance, while protecting guest OS against various CPU hardware flaws, and optionally enabling live migration between hosts with heterogeneous CPU models. </p>
<p> Preferred CPU models for Intel x86 hosts </p>
<p> The following CPU models are preferred for use on Intel hosts. Administrators / applications are recommended to use the CPU model that matches the generation of the host CPUs in use. In a deployment with a mixture of host CPU models between machines, if live migration compatibility is required, use the newest CPU model that is compatible across all desired hosts.</p>
<dl>
<dt>&quot;Skylake-Server&quot;</dt>
<dd>
</dd><dt>&quot;Skylake-Server-IBRS&quot;</dt>
<dd>Intel Xeon Processor (Skylake, 2016)</dd>
<dt>&quot;Skylake-Client&quot;</dt>
<dd>
</dd><dt>&quot;Skylake-Client-IBRS&quot;</dt>
<dd>Intel Core Processor (Skylake, 2015)</dd>
<dt>&quot;Broadwell&quot;</dt>
<dd>
</dd><dt>&quot;Broadwell-IBRS&quot;</dt>
<dd>
</dd><dt>&quot;Broadwell-noTSX&quot;</dt>
<dd>
</dd><dt>&quot;Broadwell-noTSX-IBRS&quot;</dt>
<dd>Intel Core Processor (Broadwell, 2014)</dd>
<dt>&quot;Haswell&quot;</dt>
<dd>
</dd><dt>&quot;Haswell-IBRS&quot;</dt>
<dd>
</dd><dt>&quot;Haswell-noTSX&quot;</dt>
<dd>
</dd><dt>&quot;Haswell-noTSX-IBRS&quot;</dt>
<dd>Intel Core Processor (Haswell, 2013)</dd>
<dt>&quot;IvyBridge&quot;</dt>
<dd>
</dd><dt>&quot;IvyBridge-IBRS&quot;</dt>
<dd>Intel Xeon E3-12xx v2 (Ivy Bridge, 2012)</dd>
<dt>&quot;SandyBridge&quot;</dt>
<dd>
</dd><dt>&quot;SandyBridge-IBRS&quot;</dt>
<dd>Intel Xeon E312xx (Sandy Bridge, 2011)</dd>
<dt>&quot;Westmere&quot;</dt>
<dd>
</dd><dt>&quot;Westmere-IBRS&quot;</dt>
<dd>Westmere E56xx/L56xx/X56xx (Nehalem-C, 2010)</dd>
<dt>&quot;Nehalem&quot;</dt>
<dd>
</dd><dt>&quot;Nehalem-IBRS&quot;</dt>
<dd>Intel Core i7 9xx (Nehalem Class Core i7, 2008)</dd>
<dt>&quot;Penryn&quot;</dt>
<dd>Intel Core 2 Duo P9xxx (Penryn Class Core 2, 2007)</dd>
<dt>&quot;Conroe&quot;</dt>
<dd>Intel Celeron_4x0 (Conroe/Merom Class Core 2, 2006)</dd></dl>
<p> Important CPU features for Intel x86 hosts </p>
<p> The following are important CPU features that should be used on Intel x86 hosts, when available in the host CPU. Some of them require explicit configuration to enable, as they are not included by default in some, or all, of the named CPU models listed above. In general all of these features are included if using &#8220;Host passthrough&#8221; or &#8220;Host model&#8221;.</p>
<dl>
<dt>&quot;pcid&quot;</dt>
<dd>Recommended to mitigate the cost of the Meltdown (CVE-2017-5754) fix </dd>
<p> Included by default in Haswell, Broadwell &amp; Skylake Intel CPU models. </p>
<p> Should be explicitly turned on for Westmere, SandyBridge, and IvyBridge Intel CPU models. Note that some desktop/mobile Westmere CPUs cannot support this feature.</p>
<dt>&quot;spec-ctrl&quot;</dt>
<dd>Required to enable the Spectre v2 (CVE-2017-5715) fix. </dd>
<p> Included by default in Intel CPU models with -IBRS suffix. </p>
<p> Must be explicitly turned on for Intel CPU models without -IBRS suffix. </p>
<p> Requires the host CPU microcode to support this feature before it can be used for guest CPUs.</p>
<dt>&quot;stibp&quot;</dt>
<dd>Required to enable stronger Spectre v2 (CVE-2017-5715) fixes in some operating systems. </dd>
<p> Must be explicitly turned on for all Intel CPU models. </p>
<p> Requires the host CPU microcode to support this feature before it can be used for guest CPUs.</p>
<dt>&quot;ssbd&quot;</dt>
<dd>Required to enable the CVE-2018-3639 fix </dd>
<p> Not included by default in any Intel CPU model. </p>
<p> Must be explicitly turned on for all Intel CPU models. </p>
<p> Requires the host CPU microcode to support this feature before it can be used for guest CPUs.</p>
<dt>&quot;pdpe1gb&quot;</dt>
<dd>Recommended to allow guest OS to use 1GB size pages </dd>
<p> Not included by default in any Intel CPU model. </p>
<p> Should be explicitly turned on for all Intel CPU models. </p>
<p> Note that not all CPU hardware will support this feature.</p>
<dt>&quot;md-clear&quot;</dt>
<dd>Required to confirm the MDS (CVE-2018-12126, CVE-2018-12127, CVE-2018-12130, CVE-2019-11091) fixes. </dd>
<p> Not included by default in any Intel CPU model. </p>
<p> Must be explicitly turned on for all Intel CPU models. </p>
<p> Requires the host CPU microcode to support this feature before it can be used for guest CPUs.</dl>
<p> Preferred CPU models for AMD x86 hosts </p>
<p> The following CPU models are preferred for use on Intel hosts. Administrators / applications are recommended to use the CPU model that matches the generation of the host CPUs in use. In a deployment with a mixture of host CPU models between machines, if live migration compatibility is required, use the newest CPU model that is compatible across all desired hosts.</p>
<dl>
<dt>&quot;EPYC&quot;</dt>
<dd>
</dd><dt>&quot;EPYC-IBPB&quot;</dt>
<dd>AMD EPYC Processor (2017)</dd>
<dt>&quot;Opteron_G5&quot;</dt>
<dd>AMD Opteron 63xx class CPU (2012)</dd>
<dt>&quot;Opteron_G4&quot;</dt>
<dd>AMD Opteron 62xx class CPU (2011)</dd>
<dt>&quot;Opteron_G3&quot;</dt>
<dd>AMD Opteron 23xx (Gen 3 Class Opteron, 2009)</dd>
<dt>&quot;Opteron_G2&quot;</dt>
<dd>AMD Opteron 22xx (Gen 2 Class Opteron, 2006)</dd>
<dt>&quot;Opteron_G1&quot;</dt>
<dd>AMD Opteron 240 (Gen 1 Class Opteron, 2004)</dd></dl>
<p> Important CPU features for AMD x86 hosts </p>
<p> The following are important CPU features that should be used on AMD x86 hosts, when available in the host CPU. Some of them require explicit configuration to enable, as they are not included by default in some, or all, of the named CPU models listed above. In general all of these features are included if using &#8220;Host passthrough&#8221; or &#8220;Host model&#8221;.</p>
<dl>
<dt>&quot;ibpb&quot;</dt>
<dd>Required to enable the Spectre v2 (CVE-2017-5715) fix. </dd>
<p> Included by default in AMD CPU models with -IBPB suffix. </p>
<p> Must be explicitly turned on for AMD CPU models without -IBPB suffix. </p>
<p> Requires the host CPU microcode to support this feature before it can be used for guest CPUs.</p>
<dt>&quot;stibp&quot;</dt>
<dd>Required to enable stronger Spectre v2 (CVE-2017-5715) fixes in some operating systems. </dd>
<p> Must be explicitly turned on for all AMD CPU models. </p>
<p> Requires the host CPU microcode to support this feature before it can be used for guest CPUs.</p>
<dt>&quot;virt-ssbd&quot;</dt>
<dd>Required to enable the CVE-2018-3639 fix </dd>
<p> Not included by default in any AMD CPU model. </p>
<p> Must be explicitly turned on for all AMD CPU models. </p>
<p> This should be provided to guests, even if amd-ssbd is also provided, for maximum guest compatibility. </p>
<p> Note for some QEMU / libvirt versions, this must be force enabled when when using &#8220;Host model&#8221;, because this is a virtual feature that doesn&#8217;t exist in the physical host CPUs.</p>
<dt>&quot;amd-ssbd&quot;</dt>
<dd>Required to enable the CVE-2018-3639 fix </dd>
<p> Not included by default in any AMD CPU model. </p>
<p> Must be explicitly turned on for all AMD CPU models. </p>
<p> This provides higher performance than virt-ssbd so should be exposed to guests whenever available in the host. virt-ssbd should none the less also be exposed for maximum guest compatibility as some kernels only know about virt-ssbd.</p>
<dt>&quot;amd-no-ssb&quot;</dt>
<dd>Recommended to indicate the host is not vulnerable CVE-2018-3639 </dd>
<p> Not included by default in any AMD CPU model. </p>
<p> Future hardware generations of CPU will not be vulnerable to CVE-2018-3639, and thus the guest should be told not to enable its mitigations, by exposing amd-no-ssb. This is mutually exclusive with virt-ssbd and amd-ssbd.</p>
<dt>&quot;pdpe1gb&quot;</dt>
<dd>Recommended to allow guest OS to use 1GB size pages </dd>
<p> Not included by default in any AMD CPU model. </p>
<p> Should be explicitly turned on for all AMD CPU models. </p>
<p> Note that not all CPU hardware will support this feature.</dl>
<p> Default x86 CPU models </p>
<p> The default QEMU CPU models are designed such that they can run on all hosts. If an application does not wish to do perform any host compatibility checks before launching guests, the default is guaranteed to work. </p>
<p> The default CPU models will, however, leave the guest OS vulnerable to various CPU hardware flaws, so their use is strongly discouraged. Applications should follow the earlier guidance to setup a better CPU configuration, with host passthrough recommended if live migration is not needed.</p>
<dl>
<dt>&quot;qemu32&quot;</dt>
<dd>
</dd><dt>&quot;qemu64&quot;</dt>
<dd>QEMU Virtual CPU version 2.5+ (32 &amp; 64 bit variants) </dd>
<p> qemu64 is used for x86_64 guests and qemu32 is used for i686 guests, when no -cpu argument is given to QEMU, or no &lt;cpu&gt; is provided in libvirt XML.</dl>
<p> Other non-recommended x86 CPUs </p>
<p> The following CPUs models are compatible with most AMD and Intel x86 hosts, but their usage is discouraged, as they expose a very limited featureset, which prevents guests having optimal performance.</p>
<dl>
<dt>&quot;kvm32&quot;</dt>
<dd>
</dd><dt>&quot;kvm64&quot;</dt>
<dd>Common KVM processor (32 &amp; 64 bit variants) </dd>
<p> Legacy models just for historical compatibility with ancient QEMU versions.</p>
<dt>486</dt>
<dd>
</dd><dt>&quot;athlon&quot;</dt>
<dd>
</dd><dt>&quot;phenom&quot;</dt>
<dd>
</dd><dt>&quot;coreduo&quot;</dt>
<dd>
</dd><dt>&quot;core2duo&quot;</dt>
<dd>
</dd><dt>&quot;n270&quot;</dt>
<dd>
</dd><dt>&quot;pentium&quot;</dt>
<dd>
</dd><dt>&quot;pentium2&quot;</dt>
<dd>
</dd><dt>&quot;pentium3&quot;</dt>
<dd>Various very old x86 CPU models, mostly predating the introduction of hardware assisted virtualization, that should thus not be required for running virtual machines.</dd></dl>
<p> <i>Supported </i><i>CPU</i><i> model configurations on </i><i>MIPS</i><i> hosts</i> </p>
<p> QEMU supports variety of MIPS CPU models: </p>
<p> Supported CPU models for MIPS32 hosts </p>
<p> The following CPU models are supported for use on MIPS32 hosts. Administrators / applications are recommended to use the CPU model that matches the generation of the host CPUs in use. In a deployment with a mixture of host CPU models between machines, if live migration compatibility is required, use the newest CPU model that is compatible across all desired hosts.</p>
<dl>
<dt>&quot;mips32r6-generic&quot;</dt>
<dd>MIPS32 Processor (Release 6, 2015)</dd>
<dt>&quot;P5600&quot;</dt>
<dd>MIPS32 Processor (P5600, 2014)</dd>
<dt>&quot;M14K&quot;</dt>
<dd>
</dd><dt>&quot;M14Kc&quot;</dt>
<dd>MIPS32 Processor (M14K, 2009)</dd>
<dt>&quot;74Kf&quot;</dt>
<dd>MIPS32 Processor (74K, 2007)</dd>
<dt>&quot;34Kf&quot;</dt>
<dd>MIPS32 Processor (34K, 2006)</dd>
<dt>&quot;24Kc&quot;</dt>
<dd>
</dd><dt>&quot;24KEc&quot;</dt>
<dd>
</dd><dt>&quot;24Kf&quot;</dt>
<dd>MIPS32 Processor (24K, 2003)</dd>
<dt>&quot;4Kc&quot;</dt>
<dd>
</dd><dt>&quot;4Km&quot;</dt>
<dd>
</dd><dt>&quot;4KEcR1&quot;</dt>
<dd>
</dd><dt>&quot;4KEmR1&quot;</dt>
<dd>
</dd><dt>&quot;4KEc&quot;</dt>
<dd>
</dd><dt>&quot;4KEm&quot;</dt>
<dd>MIPS32 Processor (4K, 1999)</dd></dl>
<p> Supported CPU models for MIPS64 hosts </p>
<p> The following CPU models are supported for use on MIPS64 hosts. Administrators / applications are recommended to use the CPU model that matches the generation of the host CPUs in use. In a deployment with a mixture of host CPU models between machines, if live migration compatibility is required, use the newest CPU model that is compatible across all desired hosts.</p>
<dl>
<dt>&quot;I6400&quot;</dt>
<dd>MIPS64 Processor (Release 6, 2014)</dd>
<dt>&quot;Loongson-2F&quot;</dt>
<dd>MIPS64 Processor (Loongson 2, 2008)</dd>
<dt>&quot;Loongson-2E&quot;</dt>
<dd>MIPS64 Processor (Loongson 2, 2006)</dd>
<dt>&quot;mips64dspr2&quot;</dt>
<dd>MIPS64 Processor (Release 2, 2006)</dd>
<dt>&quot;MIPS64R2-generic&quot;</dt>
<dd>
</dd><dt>&quot;5KEc&quot;</dt>
<dd>
</dd><dt>&quot;5KEf&quot;</dt>
<dd>MIPS64 Processor (Release 2, 2002)</dd>
<dt>&quot;20Kc&quot;</dt>
<dd>MIPS64 Processor (20K, 2000)</dd>
<dt>&quot;5Kc&quot;</dt>
<dd>
</dd><dt>&quot;5Kf&quot;</dt>
<dd>MIPS64 Processor (5K, 1999)</dd>
<dt>&quot;VR5432&quot;</dt>
<dd>MIPS64 Processor (VR, 1998)</dd>
<dt>&quot;R4000&quot;</dt>
<dd>MIPS64 Processor (MIPS III, 1991)</dd></dl>
<p> Supported CPU models for nanoMIPS hosts </p>
<p> The following CPU models are supported for use on nanoMIPS hosts. Administrators / applications are recommended to use the CPU model that matches the generation of the host CPUs in use. In a deployment with a mixture of host CPU models between machines, if live migration compatibility is required, use the newest CPU model that is compatible across all desired hosts.</p>
<dl>
<dt>&quot;I7200&quot;</dt>
<dd>MIPS I7200 (nanoMIPS, 2018)</dd></dl>
<p> Preferred CPU models for MIPS hosts </p>
<p> The following CPU models are preferred for use on different MIPS hosts:</p>
<dl>
<dt>&quot;MIPS III&quot;</dt>
<dd>R4000</dd>
<dt>&quot;MIPS32R2&quot;</dt>
<dd>34Kf</dd>
<dt>&quot;MIPS64R6&quot;</dt>
<dd>I6400</dd>
<dt>&quot;nanoMIPS&quot;</dt>
<dd>I7200</dd></dl>
<p> <i>Syntax for configuring </i><i>CPU</i><i> models</i> </p>
<p> The example below illustrate the approach to configuring the various CPU models / features in QEMU and libvirt </p>
<p> QEMU command line</p>
<dl>
<dt><code>Host passthrough</code></dt>
<dd>
<pre> $ qemu-system-x86_64 -cpu host</pre>
<p>With feature customization: </p>
<pre> $ qemu-system-x86_64 -cpu host,-vmx,...</pre>
</dd><dt><code>Named </code><code>CPU</code><code> models</code></dt>
<dd>
<pre> $ qemu-system-x86_64 -cpu Westmere</pre>
<p>With feature customization: </p>
<pre> $ qemu-system-x86_64 -cpu Westmere,+pcid,...</pre>
</dd></dl>
<p> Libvirt guest XML</p>
<dl>
<dt><code>Host passthrough</code></dt>
<dd>
<pre> &lt;cpu mode='host-passthrough'/&gt;</pre>
<p>With feature customization: </p>
<pre> &lt;cpu mode='host-passthrough'&gt;
 &lt;feature name=&quot;vmx&quot; policy=&quot;disable&quot;/&gt;
 ...
 &lt;/cpu&gt;</pre>
</dd><dt><code>Host model</code></dt>
<dd>
<pre> &lt;cpu mode='host-model'/&gt;</pre>
<p>With feature customization: </p>
<pre> &lt;cpu mode='host-model'&gt;
 &lt;feature name=&quot;vmx&quot; policy=&quot;disable&quot;/&gt;
 ...
 &lt;/cpu&gt;</pre>
</dd><dt><code>Named model</code></dt>
<dd>
<pre> &lt;cpu mode='custom'&gt;
 &lt;model name=&quot;Westmere&quot;/&gt;
 &lt;/cpu&gt;</pre>
<p>With feature customization: </p>
<pre> &lt;cpu mode='custom'&gt;
 &lt;model name=&quot;Westmere&quot;/&gt;
 &lt;feature name=&quot;pcid&quot; policy=&quot;require&quot;/&gt;
 ...
 &lt;/cpu&gt;</pre>
</dd></dl>
<h2>See Also</h2>
<p>The HTML documentation of QEMU for more precise information and Linux user mode emulator invocation.</p>
<h2>Author</h2>
<p>Daniel P. Berrange</p>
