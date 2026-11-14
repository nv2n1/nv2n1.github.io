---
title: "systemd-boot-system-token-service(8)"
name: "systemd-boot-system-token-service"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-boot-system-token-service/"
description: "systemd-boot-system-token.service – Generate an initial boot loader system token and random seed"
---

<p>systemd-boot-system-token.service &#8211; Generate an initial boot loader system token and random seed</p>
<h2>Synopsis</h2>
<p>systemd-boot-system-token.service</p>
<h2>Description</h2>
<p>systemd-boot-system-token.service is a system service that automatically generates a &#8216;system token&#8217; to store in an EFI variable in the system&#8217;s NVRAM and a random seed to store on the EFI System Partition ESP on disk. The boot loader may then combine these two randomized data fields by cryptographic hashing, and pass it to the OS it boots as initialization seed for its entropy pool. The random seed stored in the ESP is refreshed on each reboot ensuring that multiple subsequent boots will boot with different seeds. The &#8216;system token&#8217; is generated randomly once, and then persistently stored in the system&#8217;s EFI variable storage. </p>
<p> The systemd-boot-system-token.service unit invokes the <code>bootctl random-seed</code> command, which updates the random seed in the ESP, and initializes the &#8216;system token&#8217; if it&#8217;s not initialized yet. The service is conditionalized so that it is run only when all of the below apply: </p>
<dl>
<dd>&bull; A boot loader is used that implements the m[blue]<code>Boot Loader Interface</code>m[]<font SIZE="-2">[1]</font> (which defines the &#8216;system token&#8217; concept).</dl>
<dl>
<dd>&bull; Either a &#8216;system token&#8217; was not set yet, or the boot loader has not passed the OS a random seed yet (and thus most likely has been missing the random seed file in the ESP).</dl>
<dl>
<dd>&bull; The system is not running in a VM environment. This case is explicitly excluded since on VM environments the ESP backing storage and EFI variable storage is typically not physically separated and hence booting the same OS image in multiple instances would replicate both, thus reusing the same random seed and &#8216;system token&#8217; among all instances, which defeats its purpose. Note that it&#8217;s still possible to use boot loader random seed provisioning in this mode, but the automatic logic implemented by this service has no effect then, and the user instead has to manually invoke the <code>bootctl random-seed</code> acknowledging these restrictions.</dl>
<p> For further details see <code><a href="/docs/linux/man/1-bootctl/">bootctl</a></code>(1), regarding the command this service invokes.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-bootctl/">bootctl</a></code>(1), <code><a href="/docs/linux/man/7-systemd-boot/">systemd-boot</a></code>(7)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>Boot Loader Interface</p>
<dl>
<dd><a rel="nofollow" href="https://systemd.io/BOOT_LOADER_INTERFACE">https://systemd.io/BOOT_LOADER_INTERFACE</a></dl>
