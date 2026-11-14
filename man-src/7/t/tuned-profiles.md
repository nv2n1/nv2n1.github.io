---
title: "tuned-profiles(7)"
name: "tuned-profiles"
section: "7"
letter: "t"
url: "/docs/linux/man/7-tuned-profiles/"
description: "tuned-profiles – description of basic tuned profiles"
---

<p>tuned-profiles &#8211; description of basic tuned profiles </p>
<h2>Description</h2>
<p>These are the base profiles which are mostly shipped in the base tuned package. They are targeted to various goals. Mostly they provide performance optimizations but there are also profiles targeted to low power consumption, low latency and others. You can mostly deduce the purpose of the profile by its name or you can see full description bellow. The profiles are stored in subdirectories below <i>/usr/lib/tuned</i>. If you need to customize the profiles, you can copy them to <i>/etc/tuned</i> and modify them as you need. When loading profiles with the same name, the /etc/tuned takes precedence. In such case you will not lose your customized profiles between tuned updates. The power saving profiles contain settings that are typically not enabled by default as they will noticeably impact the latency/performance of your system as opposed to the power saving mechanisms that are enabled by default. On the other hand the performance profiles disable the additional power saving mechanisms of tuned as they would negatively impact throughput or latency. </p>
<h2>Profiles</h2>
<p>At the moment we&#8217;re providing the following pre-defined profiles: </p>
<dl>
<dt><code>balanced</code></p>
<dd>It is the default profile. It provides balanced power saving and performance. At the moment it enables CPU and disk plugins of tuned and it makes sure the ondemand governor is active (if supported by the current cpufreq driver). It enables ALPM power saving for SATA host adapters and sets the link power management policy to medium_power. It also sets the CPU energy performance bias to normal. It also enables AC97 audio power saving or (it depends on your system) HDA-Intel power savings with 10 seconds timeout. In case your system contains supported Radeon graphics card (with enabled KMS) it configures it to automatic power saving. </p>
<dt><code>powersave</code></p>
<dd>Maximal power saving, at the moment it enables USB autosuspend (in case environment variable USB_AUTOSUSPEND is set to 1), enables ALPM power saving for SATA host adapters and sets the link power manamgent policy to min_power. It also enables WiFi power saving, enables multi core power savings scheduler for low wakeup systems and makes sure the ondemand governor is active (if supported by the current cpufreq driver). It sets the CPU energy performance bias to powersave. It also enables AC97 audio power saving or (it depends on your system) HDA-Intel power savings (with 10 seconds timeout). In case your system contains supported Radeon graphics card (with enabled KMS) it configures it to automatic power saving. On Asus Eee PCs dynamic Super Hybrid Engine is enabled. </p>
<dt><code>throughput-performance</code></p>
<dd>Profile for typical throughput performance tuning. Disables power saving mechanisms and enables sysctl settings that improve the throughput performance of your disk and network IO. CPU governor is set to performance and CPU energy performance bias is set to performance. Disk readahead values are increased. </p>
<dt><code>latency-performance</code></p>
<dd>Profile for low latency performance tuning. Disables power saving mechanisms. CPU governor is set to performance andlocked to the low C states (by PM QoS). CPU energy performance bias to performance. </p>
<dt><code>network-throughput</code></p>
<dd>Profile for throughput network tuning. It is based on the throughput-performance profile. It additionaly increases kernel network buffers. </p>
<dt><code>network-latency</code></p>
<dd>Profile for low latency network tuning. It is based on the latency-performance profile. It additionaly disables transparent hugepages, NUMA balancing and tunes several other network related sysctl parameters. </p>
<dt><code>desktop</code></p>
<dd>Profile optimized for desktops based on balanced profile. It additionaly enables scheduler autogroups for better response of interactive applications. </p>
<dt><code>virtual-guest</code></p>
<dd>Profile optimized for virtual guests based on throughput-performance profile. It additionally decreases virtual memory swappiness and increases dirty_ratio settings. </p>
<dt><code>virtual-host</code></p>
<dd>Profile optimized for virtual hosts based on throughput-performance profile. It additionally enables more aggresive writeback of dirty pages. </p>
</dl>
<h2>Files</h2>
<p><i>/etc/tuned/*</i> <i>/usr/lib/tuned/*</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tuned/">tuned</a></code>(8) <code><a href="/docs/linux/man/8-tuned-adm/">tuned-adm</a></code>(8) <code><a href="/docs/linux/man/7-tuned-profiles-atomic/">tuned-profiles-atomic</a></code>(7) <code><a href="/docs/linux/man/7-tuned-profiles-sap/">tuned-profiles-sap</a></code>(7) <code><a href="/docs/linux/man/7-tuned-profiles-sap-hana/">tuned-profiles-sap-hana</a></code>(7) <code><a href="/docs/linux/man/7-tuned-profiles-oracle/">tuned-profiles-oracle</a></code>(7) <code><a href="/docs/linux/man/7-tuned-profiles-realtime/">tuned-profiles-realtime</a></code>(7) <code><a href="/docs/linux/man/7-tuned-profiles-nfv-host/">tuned-profiles-nfv-host</a></code>(7) <code><a href="/docs/linux/man/7-tuned-profiles-nfv-guest/">tuned-profiles-nfv-guest</a></code>(7) <code><a href="/docs/linux/man/7-tuned-profiles-cpu-partitioning/">tuned-profiles-cpu-partitioning</a></code>(7) <code><a href="/docs/linux/man/7-tuned-profiles-compat/">tuned-profiles-compat</a></code>(7)</p>
<h2>Author</h2>
<p>Jaroslav Škarvada &lt;jskarvad [at] redhat.com&gt; Jan Kaluža &lt;jkaluza [at] redhat.com&gt; Jan Včelák &lt;jvcelak [at] redhat.com&gt; Marcela Mašláňová &lt;mmaslano [at] redhat.com&gt; Phil Knirsch &lt;pknirsch [at] redhat.com&gt;</p>
