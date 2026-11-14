---
title: "tuned-profiles-compat(7)"
name: "tuned-profiles-compat"
section: "7"
letter: "t"
url: "/docs/linux/man/7-tuned-profiles-compat/"
description: "tuned-profiles-compat – description of profiles provided for backward compatibility"
---

<p>tuned-profiles-compat &#8211; description of profiles provided for backward compatibility </p>
<h2>Description</h2>
<p>These profiles are provided for backward compatibility with the tuned-1x. They are no longer mainained and may be dropped anytime in the future. It&#8217;s not recommended to use them for purposes other than backward compatibility. Some of them are only aliases to base tuned profiles. Please do not use the compat profiles on new installations and rather use profiles from base tuned package or other tuned subpackages. </p>
<h2>Profiles</h2>
<p>The following profiles are considered compatibility profiles: </p>
<dl>
<dt><code>default</code></p>
<dd>It is the lowest of the available profiles in regard to power saving and only enables CPU and disk plugins of tuned. </p>
<dt><code>desktop-powersave</code></p>
<dd>A power saving profile directed at desktop systems. Enables ALPM power saving for SATA host adapters as well as the CPU, ethernet and disk plugins of tuned. </p>
<dt><code>server-powersave</code></p>
<dd>A power saving profile directed at server systems. Enables ALPM power saving for SATA host adapters, and activates the CPU and disk plugins of tuned. </p>
<dt><code>laptop-ac-powersave</code></p>
<dd>Medium power saving profile directed at laptops running on AC. Enables ALPM power saving for SATA host adapters, WiFi power saving as well as CPU, ethernet and disk plugins of tuned. </p>
<dt><code>laptop-battery-powersave</code></p>
<dd>Strong power saving profile directed at laptops running on battery. Currently an alias to powersave profile. </p>
<dt><code>spindown-disk</code></p>
<dd>Strong power saving profile directed at machines with classic HDDs. It enables aggressive disk spin-down. Disk writeback values are increased and disk swappiness is lowered. Log syncing is disabled. All partitions are remounted with &#8216;noatime&#8217; option. All tuned plugins are disabled. </p>
<dt><code>enterprise-storage</code></p>
<dd>Server profile for high disk throughput performace tuning. Disables power saving mechanisms and enables deadline IO scheduler. Enables hugepages and disables disk barriers. Disk readahead values are increased. CPU governor is set to performance. </p>
</dl>
<h2>Files</h2>
<p><i>/etc/tuned/*</i> <i>/usr/lib/tuned/*</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tuned/">tuned</a></code>(8) <code><a href="/docs/linux/man/8-tuned-adm/">tuned-adm</a></code>(8) <code><a href="/docs/linux/man/7-tuned-profiles/">tuned-profiles</a></code>(7) <code><a href="/docs/linux/man/7-tuned-profiles-atomic/">tuned-profiles-atomic</a></code>(7) <code><a href="/docs/linux/man/7-tuned-profiles-sap/">tuned-profiles-sap</a></code>(7) <code><a href="/docs/linux/man/7-tuned-profiles-sap-hana/">tuned-profiles-sap-hana</a></code>(7) <code><a href="/docs/linux/man/7-tuned-profiles-oracle/">tuned-profiles-oracle</a></code>(7) <code><a href="/docs/linux/man/7-tuned-profiles-realtime/">tuned-profiles-realtime</a></code>(7) <code><a href="/docs/linux/man/7-tuned-profiles-nfv/">tuned-profiles-nfv</a></code>(7)</p>
<h2>Author</h2>
<p>Jaroslav Škarvada &lt;jskarvad [at] redhat.com&gt; Jan Kaluža &lt;jkaluza [at] redhat.com&gt; Jan Včelák &lt;jvcelak [at] redhat.com&gt; Marcela Mašláňová &lt;mmaslano [at] redhat.com&gt; Phil Knirsch &lt;pknirsch [at] redhat.com&gt;</p>
