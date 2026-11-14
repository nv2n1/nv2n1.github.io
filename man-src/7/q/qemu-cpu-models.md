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
<p><font SIZE="-1">QEMU / KVM CPU</font> model configuration</p>
<h2>Description</h2>
<p><font SIZE="-1">QEMU / KVM</font> virtualization supports two ways to configure <font SIZE="-1">CPU</font> models</p>
<dl>
<dt><code>Host passthrough</code></p>
<dd>This passes the host <font SIZE="-1">CPU</font> model features, model, stepping, exactly to the guest. Note that <font SIZE="-1">KVM</font> may filter out some host <font SIZE="-1">CPU</font> model features if they cannot be supported with virtualization. Live migration is unsafe when this mode is used as libvirt / <font SIZE="-1">QEMU</font> cannot guarantee a stable <font SIZE="-1">CPU</font> is exposed to the guest across hosts. This is the recommended <font SIZE="-1">CPU</font> to use, provided live migration is not required.</p>
<dt><code>Named model</code></p>
<dd><font SIZE="-1">QEMU</font> comes with a number of predefined named <font SIZE="-1">CPU</font> models, that typically refer to specific generations of hardware released by Intel and <font SIZE="-1">AMD.</font> These allow the guest VMs to have a degree of isolation from the host <font SIZE="-1">CPU,</font> allowing greater flexibility in live migrating between hosts with differing hardware.</dl>
<p> In both cases, it is possible to optionally add or remove individual <font SIZE="-1">CPU</font> features, to alter what is presented to the guest by default. </p>
<p> Libvirt supports a third way to configure <font SIZE="-1">CPU</font> models known as &#8220;Host model&#8221;. This uses the <font SIZE="-1">QEMU</font> &#8220;Named model&#8221; feature, automatically picking a <font SIZE="-1">CPU</font> model that is similar the host <font SIZE="-1">CPU,</font> and then adding extra features to approximate the host model as closely as possible. This does not guarantee the <font SIZE="-1">CPU</font> family, stepping, etc will precisely match the host <font SIZE="-1">CPU,</font> as they would with &#8220;Host passthrough&#8221;, but gives much of the benefit of passthrough, while making live migration safe. </p>
<p> <i>Recommendations for </i><font SIZE="-1"><i>KVM CPU</i></font><i> model configuration on x86 hosts</i> </p>
<p> The information that follows provides recommendations for configuring <font SIZE="-1">CPU</font> models on x86 hosts. The goals are to maximise performance, while protecting guest <font SIZE="-1">OS</font> against various <font SIZE="-1">CPU</font> hardware flaws, and optionally enabling live migration between hosts with heterogeneous <font SIZE="-1">CPU</font> models. </p>
<p> Preferred <font SIZE="-1">CPU</font> models for Intel x86 hosts </p>
<p> The following <font SIZE="-1">CPU</font> models are preferred for use on Intel hosts. Administrators / applications are recommended to use the <font SIZE="-1">CPU</font> model that matches the generation of the host CPUs in use. In a deployment with a mixture of host <font SIZE="-1">CPU</font> models between machines, if live migration compatibility is required, use the newest <font SIZE="-1">CPU</font> model that is compatible across all desired hosts.</p>
<dl>
<dt>&quot;Skylake-Server&quot;</p>
<dd>
<dt>&quot;Skylake-Server-IBRS&quot;</p>
<dd>Intel Xeon Processor (Skylake, 2016)</p>
<dt>&quot;Skylake-Client&quot;</p>
<dd>
<dt>&quot;Skylake-Client-IBRS&quot;</p>
<dd>Intel Core Processor (Skylake, 2015)</p>
<dt>&quot;Broadwell&quot;</p>
<dd>
<dt>&quot;Broadwell-IBRS&quot;</p>
<dd>
<dt>&quot;Broadwell-noTSX&quot;</p>
<dd>
<dt>&quot;Broadwell-noTSX-IBRS&quot;</p>
<dd>Intel Core Processor (Broadwell, 2014)</p>
<dt>&quot;Haswell&quot;</p>
<dd>
<dt>&quot;Haswell-IBRS&quot;</p>
<dd>
<dt>&quot;Haswell-noTSX&quot;</p>
<dd>
<dt>&quot;Haswell-noTSX-IBRS&quot;</p>
<dd>Intel Core Processor (Haswell, 2013)</p>
<dt>&quot;IvyBridge&quot;</p>
<dd>
<dt>&quot;IvyBridge-IBRS&quot;</p>
<dd>Intel Xeon E3-12xx v2 (Ivy Bridge, 2012)</p>
<dt>&quot;SandyBridge&quot;</p>
<dd>
<dt>&quot;SandyBridge-IBRS&quot;</p>
<dd>Intel Xeon E312xx (Sandy Bridge, 2011)</p>
<dt>&quot;Westmere&quot;</p>
<dd>
<dt>&quot;Westmere-IBRS&quot;</p>
<dd>Westmere E56xx/L56xx/X56xx (Nehalem-C, 2010)</p>
<dt>&quot;Nehalem&quot;</p>
<dd>
<dt>&quot;Nehalem-IBRS&quot;</p>
<dd>Intel Core i7 9xx (Nehalem Class Core i7, 2008)</p>
<dt>&quot;Penryn&quot;</p>
<dd>Intel Core 2 Duo P9xxx (Penryn Class Core 2, 2007)</p>
<dt>&quot;Conroe&quot;</p>
<dd>Intel Celeron_4x0 (Conroe/Merom Class Core 2, 2006)</dl>
<p> Important <font SIZE="-1">CPU</font> features for Intel x86 hosts </p>
<p> The following are important <font SIZE="-1">CPU</font> features that should be used on Intel x86 hosts, when available in the host <font SIZE="-1">CPU.</font> Some of them require explicit configuration to enable, as they are not included by default in some, or all, of the named <font SIZE="-1">CPU</font> models listed above. In general all of these features are included if using &#8220;Host passthrough&#8221; or &#8220;Host model&#8221;.</p>
<dl>
<dt>&quot;pcid&quot;</p>
<dd>Recommended to mitigate the cost of the Meltdown (<font SIZE="-1">CVE-2017-5754</font>) fix </p>
<p> Included by default in Haswell, Broadwell &amp; Skylake Intel <font SIZE="-1">CPU</font> models. </p>
<p> Should be explicitly turned on for Westmere, SandyBridge, and IvyBridge Intel <font SIZE="-1">CPU</font> models. Note that some desktop/mobile Westmere CPUs cannot support this feature.</p>
<dt>&quot;spec-ctrl&quot;</p>
<dd>Required to enable the Spectre v2 (<font SIZE="-1">CVE-2017-5715</font>) fix. </p>
<p> Included by default in Intel <font SIZE="-1">CPU</font> models with -IBRS suffix. </p>
<p> Must be explicitly turned on for Intel <font SIZE="-1">CPU</font> models without -IBRS suffix. </p>
<p> Requires the host <font SIZE="-1">CPU</font> microcode to support this feature before it can be used for guest CPUs.</p>
<dt>&quot;stibp&quot;</p>
<dd>Required to enable stronger Spectre v2 (<font SIZE="-1">CVE-2017-5715</font>) fixes in some operating systems. </p>
<p> Must be explicitly turned on for all Intel <font SIZE="-1">CPU</font> models. </p>
<p> Requires the host <font SIZE="-1">CPU</font> microcode to support this feature before it can be used for guest CPUs.</p>
<dt>&quot;ssbd&quot;</p>
<dd>Required to enable the <font SIZE="-1">CVE-2018-3639</font> fix </p>
<p> Not included by default in any Intel <font SIZE="-1">CPU</font> model. </p>
<p> Must be explicitly turned on for all Intel <font SIZE="-1">CPU</font> models. </p>
<p> Requires the host <font SIZE="-1">CPU</font> microcode to support this feature before it can be used for guest CPUs.</p>
<dt>&quot;pdpe1gb&quot;</p>
<dd>Recommended to allow guest <font SIZE="-1">OS</font> to use 1GB size pages </p>
<p> Not included by default in any Intel <font SIZE="-1">CPU</font> model. </p>
<p> Should be explicitly turned on for all Intel <font SIZE="-1">CPU</font> models. </p>
<p> Note that not all <font SIZE="-1">CPU</font> hardware will support this feature.</p>
<dt>&quot;md-clear&quot;</p>
<dd>Required to confirm the <font SIZE="-1">MDS</font> (<font SIZE="-1">CVE-2018-12126, CVE-2018-12127, CVE-2018-12130, CVE-2019-11091</font>) fixes. </p>
<p> Not included by default in any Intel <font SIZE="-1">CPU</font> model. </p>
<p> Must be explicitly turned on for all Intel <font SIZE="-1">CPU</font> models. </p>
<p> Requires the host <font SIZE="-1">CPU</font> microcode to support this feature before it can be used for guest CPUs.</dl>
<p> Preferred <font SIZE="-1">CPU</font> models for <font SIZE="-1">AMD</font> x86 hosts </p>
<p> The following <font SIZE="-1">CPU</font> models are preferred for use on Intel hosts. Administrators / applications are recommended to use the <font SIZE="-1">CPU</font> model that matches the generation of the host CPUs in use. In a deployment with a mixture of host <font SIZE="-1">CPU</font> models between machines, if live migration compatibility is required, use the newest <font SIZE="-1">CPU</font> model that is compatible across all desired hosts.</p>
<dl>
<dt>&quot;EPYC&quot;</p>
<dd>
<dt>&quot;EPYC-IBPB&quot;</p>
<dd><font SIZE="-1">AMD EPYC</font> Processor (2017)</p>
<dt>&quot;Opteron_G5&quot;</p>
<dd><font SIZE="-1">AMD</font> Opteron 63xx class <font SIZE="-1">CPU</font> (2012)</p>
<dt>&quot;Opteron_G4&quot;</p>
<dd><font SIZE="-1">AMD</font> Opteron 62xx class <font SIZE="-1">CPU</font> (2011)</p>
<dt>&quot;Opteron_G3&quot;</p>
<dd><font SIZE="-1">AMD</font> Opteron 23xx (Gen 3 Class Opteron, 2009)</p>
<dt>&quot;Opteron_G2&quot;</p>
<dd><font SIZE="-1">AMD</font> Opteron 22xx (Gen 2 Class Opteron, 2006)</p>
<dt>&quot;Opteron_G1&quot;</p>
<dd><font SIZE="-1">AMD</font> Opteron 240 (Gen 1 Class Opteron, 2004)</dl>
<p> Important <font SIZE="-1">CPU</font> features for <font SIZE="-1">AMD</font> x86 hosts </p>
<p> The following are important <font SIZE="-1">CPU</font> features that should be used on <font SIZE="-1">AMD</font> x86 hosts, when available in the host <font SIZE="-1">CPU.</font> Some of them require explicit configuration to enable, as they are not included by default in some, or all, of the named <font SIZE="-1">CPU</font> models listed above. In general all of these features are included if using &#8220;Host passthrough&#8221; or &#8220;Host model&#8221;.</p>
<dl>
<dt>&quot;ibpb&quot;</p>
<dd>Required to enable the Spectre v2 (<font SIZE="-1">CVE-2017-5715</font>) fix. </p>
<p> Included by default in <font SIZE="-1">AMD CPU</font> models with -IBPB suffix. </p>
<p> Must be explicitly turned on for <font SIZE="-1">AMD CPU</font> models without -IBPB suffix. </p>
<p> Requires the host <font SIZE="-1">CPU</font> microcode to support this feature before it can be used for guest CPUs.</p>
<dt>&quot;stibp&quot;</p>
<dd>Required to enable stronger Spectre v2 (<font SIZE="-1">CVE-2017-5715</font>) fixes in some operating systems. </p>
<p> Must be explicitly turned on for all <font SIZE="-1">AMD CPU</font> models. </p>
<p> Requires the host <font SIZE="-1">CPU</font> microcode to support this feature before it can be used for guest CPUs.</p>
<dt>&quot;virt-ssbd&quot;</p>
<dd>Required to enable the <font SIZE="-1">CVE-2018-3639</font> fix </p>
<p> Not included by default in any <font SIZE="-1">AMD CPU</font> model. </p>
<p> Must be explicitly turned on for all <font SIZE="-1">AMD CPU</font> models. </p>
<p> This should be provided to guests, even if amd-ssbd is also provided, for maximum guest compatibility. </p>
<p> Note for some <font SIZE="-1">QEMU /</font> libvirt versions, this must be force enabled when when using &#8220;Host model&#8221;, because this is a virtual feature that doesn&#8217;t exist in the physical host CPUs.</p>
<dt>&quot;amd-ssbd&quot;</p>
<dd>Required to enable the <font SIZE="-1">CVE-2018-3639</font> fix </p>
<p> Not included by default in any <font SIZE="-1">AMD CPU</font> model. </p>
<p> Must be explicitly turned on for all <font SIZE="-1">AMD CPU</font> models. </p>
<p> This provides higher performance than virt-ssbd so should be exposed to guests whenever available in the host. virt-ssbd should none the less also be exposed for maximum guest compatibility as some kernels only know about virt-ssbd.</p>
<dt>&quot;amd-no-ssb&quot;</p>
<dd>Recommended to indicate the host is not vulnerable <font SIZE="-1">CVE-2018-3639</font> </p>
<p> Not included by default in any <font SIZE="-1">AMD CPU</font> model. </p>
<p> Future hardware generations of <font SIZE="-1">CPU</font> will not be vulnerable to <font SIZE="-1">CVE-2018-3639,</font> and thus the guest should be told not to enable its mitigations, by exposing amd-no-ssb. This is mutually exclusive with virt-ssbd and amd-ssbd.</p>
<dt>&quot;pdpe1gb&quot;</p>
<dd>Recommended to allow guest <font SIZE="-1">OS</font> to use 1GB size pages </p>
<p> Not included by default in any <font SIZE="-1">AMD CPU</font> model. </p>
<p> Should be explicitly turned on for all <font SIZE="-1">AMD CPU</font> models. </p>
<p> Note that not all <font SIZE="-1">CPU</font> hardware will support this feature.</dl>
<p> Default x86 <font SIZE="-1">CPU</font> models </p>
<p> The default <font SIZE="-1">QEMU CPU</font> models are designed such that they can run on all hosts. If an application does not wish to do perform any host compatibility checks before launching guests, the default is guaranteed to work. </p>
<p> The default <font SIZE="-1">CPU</font> models will, however, leave the guest <font SIZE="-1">OS</font> vulnerable to various <font SIZE="-1">CPU</font> hardware flaws, so their use is strongly discouraged. Applications should follow the earlier guidance to setup a better <font SIZE="-1">CPU</font> configuration, with host passthrough recommended if live migration is not needed.</p>
<dl>
<dt>&quot;qemu32&quot;</p>
<dd>
<dt>&quot;qemu64&quot;</p>
<dd><font SIZE="-1">QEMU</font> Virtual <font SIZE="-1">CPU</font> version 2.5+ (32 &amp; 64 bit variants) </p>
<p> qemu64 is used for x86_64 guests and qemu32 is used for i686 guests, when no -cpu argument is given to <font SIZE="-1">QEMU,</font> or no &lt;cpu&gt; is provided in libvirt <font SIZE="-1">XML.</font></dl>
<p> Other non-recommended x86 CPUs </p>
<p> The following CPUs models are compatible with most <font SIZE="-1">AMD</font> and Intel x86 hosts, but their usage is discouraged, as they expose a very limited featureset, which prevents guests having optimal performance.</p>
<dl>
<dt>&quot;kvm32&quot;</p>
<dd>
<dt>&quot;kvm64&quot;</p>
<dd>Common <font SIZE="-1">KVM</font> processor (32 &amp; 64 bit variants) </p>
<p> Legacy models just for historical compatibility with ancient <font SIZE="-1">QEMU</font> versions.</p>
<dt>486</p>
<dd>
<dt>&quot;athlon&quot;</p>
<dd>
<dt>&quot;phenom&quot;</p>
<dd>
<dt>&quot;coreduo&quot;</p>
<dd>
<dt>&quot;core2duo&quot;</p>
<dd>
<dt>&quot;n270&quot;</p>
<dd>
<dt>&quot;pentium&quot;</p>
<dd>
<dt>&quot;pentium2&quot;</p>
<dd>
<dt>&quot;pentium3&quot;</p>
<dd>Various very old x86 <font SIZE="-1">CPU</font> models, mostly predating the introduction of hardware assisted virtualization, that should thus not be required for running virtual machines.</dl>
<p> <i>Supported </i><font SIZE="-1"><i>CPU</i></font><i> model configurations on </i><font SIZE="-1"><i>MIPS</i></font><i> hosts</i> </p>
<p> <font SIZE="-1">QEMU</font> supports variety of <font SIZE="-1">MIPS CPU</font> models: </p>
<p> Supported <font SIZE="-1">CPU</font> models for <font SIZE="-1">MIPS32</font> hosts </p>
<p> The following <font SIZE="-1">CPU</font> models are supported for use on <font SIZE="-1">MIPS32</font> hosts. Administrators / applications are recommended to use the <font SIZE="-1">CPU</font> model that matches the generation of the host CPUs in use. In a deployment with a mixture of host <font SIZE="-1">CPU</font> models between machines, if live migration compatibility is required, use the newest <font SIZE="-1">CPU</font> model that is compatible across all desired hosts.</p>
<dl>
<dt>&quot;mips32r6-generic&quot;</p>
<dd><font SIZE="-1">MIPS32</font> Processor (Release 6, 2015)</p>
<dt>&quot;P5600&quot;</p>
<dd><font SIZE="-1">MIPS32</font> Processor (P5600, 2014)</p>
<dt>&quot;M14K&quot;</p>
<dd>
<dt>&quot;M14Kc&quot;</p>
<dd><font SIZE="-1">MIPS32</font> Processor (M14K, 2009)</p>
<dt>&quot;74Kf&quot;</p>
<dd><font SIZE="-1">MIPS32</font> Processor (74K, 2007)</p>
<dt>&quot;34Kf&quot;</p>
<dd><font SIZE="-1">MIPS32</font> Processor (34K, 2006)</p>
<dt>&quot;24Kc&quot;</p>
<dd>
<dt>&quot;24KEc&quot;</p>
<dd>
<dt>&quot;24Kf&quot;</p>
<dd><font SIZE="-1">MIPS32</font> Processor (24K, 2003)</p>
<dt>&quot;4Kc&quot;</p>
<dd>
<dt>&quot;4Km&quot;</p>
<dd>
<dt>&quot;4KEcR1&quot;</p>
<dd>
<dt>&quot;4KEmR1&quot;</p>
<dd>
<dt>&quot;4KEc&quot;</p>
<dd>
<dt>&quot;4KEm&quot;</p>
<dd><font SIZE="-1">MIPS32</font> Processor (4K, 1999)</dl>
<p> Supported <font SIZE="-1">CPU</font> models for <font SIZE="-1">MIPS64</font> hosts </p>
<p> The following <font SIZE="-1">CPU</font> models are supported for use on <font SIZE="-1">MIPS64</font> hosts. Administrators / applications are recommended to use the <font SIZE="-1">CPU</font> model that matches the generation of the host CPUs in use. In a deployment with a mixture of host <font SIZE="-1">CPU</font> models between machines, if live migration compatibility is required, use the newest <font SIZE="-1">CPU</font> model that is compatible across all desired hosts.</p>
<dl>
<dt>&quot;I6400&quot;</p>
<dd><font SIZE="-1">MIPS64</font> Processor (Release 6, 2014)</p>
<dt>&quot;Loongson-2F&quot;</p>
<dd><font SIZE="-1">MIPS64</font> Processor (Loongson 2, 2008)</p>
<dt>&quot;Loongson-2E&quot;</p>
<dd><font SIZE="-1">MIPS64</font> Processor (Loongson 2, 2006)</p>
<dt>&quot;mips64dspr2&quot;</p>
<dd><font SIZE="-1">MIPS64</font> Processor (Release 2, 2006)</p>
<dt>&quot;MIPS64R2-generic&quot;</p>
<dd>
<dt>&quot;5KEc&quot;</p>
<dd>
<dt>&quot;5KEf&quot;</p>
<dd><font SIZE="-1">MIPS64</font> Processor (Release 2, 2002)</p>
<dt>&quot;20Kc&quot;</p>
<dd><font SIZE="-1">MIPS64</font> Processor (20K, 2000)</p>
<dt>&quot;5Kc&quot;</p>
<dd>
<dt>&quot;5Kf&quot;</p>
<dd><font SIZE="-1">MIPS64</font> Processor (5K, 1999)</p>
<dt>&quot;VR5432&quot;</p>
<dd><font SIZE="-1">MIPS64</font> Processor (<font SIZE="-1">VR, 1998</font>)</p>
<dt>&quot;R4000&quot;</p>
<dd><font SIZE="-1">MIPS64</font> Processor (<font SIZE="-1">MIPS III, 1991</font>)</dl>
<p> Supported <font SIZE="-1">CPU</font> models for nanoMIPS hosts </p>
<p> The following <font SIZE="-1">CPU</font> models are supported for use on nanoMIPS hosts. Administrators / applications are recommended to use the <font SIZE="-1">CPU</font> model that matches the generation of the host CPUs in use. In a deployment with a mixture of host <font SIZE="-1">CPU</font> models between machines, if live migration compatibility is required, use the newest <font SIZE="-1">CPU</font> model that is compatible across all desired hosts.</p>
<dl>
<dt>&quot;I7200&quot;</p>
<dd><font SIZE="-1">MIPS I7200</font> (nanoMIPS, 2018)</dl>
<p> Preferred <font SIZE="-1">CPU</font> models for <font SIZE="-1">MIPS</font> hosts </p>
<p> The following <font SIZE="-1">CPU</font> models are preferred for use on different <font SIZE="-1">MIPS</font> hosts:</p>
<dl>
<dt>&quot;MIPS III&quot;</p>
<dd>R4000</p>
<dt>&quot;MIPS32R2&quot;</p>
<dd>34Kf</p>
<dt>&quot;MIPS64R6&quot;</p>
<dd>I6400</p>
<dt>&quot;nanoMIPS&quot;</p>
<dd>I7200</dl>
<p> <i>Syntax for configuring </i><font SIZE="-1"><i>CPU</i></font><i> models</i> </p>
<p> The example below illustrate the approach to configuring the various <font SIZE="-1">CPU</font> models / features in <font SIZE="-1">QEMU</font> and libvirt </p>
<p> <font SIZE="-1">QEMU</font> command line</p>
<dl>
<dt><code>Host passthrough</code></p>
<dd>
<pre> $ qemu-system-x86_64 -cpu host</pre>
<p>With feature customization: </p>
<pre> $ qemu-system-x86_64 -cpu host,-vmx,...</pre>
<dt><code>Named </code><font SIZE="-1"><code>CPU</code></font><code> models</code></p>
<dd>
<pre> $ qemu-system-x86_64 -cpu Westmere</pre>
<p>With feature customization: </p>
<pre> $ qemu-system-x86_64 -cpu Westmere,+pcid,...</pre>
</dl>
<p> Libvirt guest <font SIZE="-1">XML</font></p>
<dl>
<dt><code>Host passthrough</code></p>
<dd>
<pre> &lt;cpu mode='host-passthrough'/&gt;</pre>
<p>With feature customization: </p>
<pre> &lt;cpu mode='host-passthrough'&gt;
 &lt;feature name=&quot;vmx&quot; policy=&quot;disable&quot;/&gt;
 ...
 &lt;/cpu&gt;</pre>
<dt><code>Host model</code></p>
<dd>
<pre> &lt;cpu mode='host-model'/&gt;</pre>
<p>With feature customization: </p>
<pre> &lt;cpu mode='host-model'&gt;
 &lt;feature name=&quot;vmx&quot; policy=&quot;disable&quot;/&gt;
 ...
 &lt;/cpu&gt;</pre>
<dt><code>Named model</code></p>
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
</dl>
<h2>See Also</h2>
<p>The <font SIZE="-1">HTML</font> documentation of <font SIZE="-1">QEMU</font> for more precise information and Linux user mode emulator invocation.</p>
<h2>Author</h2>
<p>Daniel P. Berrange</p>
