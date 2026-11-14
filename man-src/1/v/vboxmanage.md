---
title: "vboxmanage(1)"
name: "vboxmanage"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vboxmanage/"
description: "VBoxManage – x86 virtualization solution"
---

<h2 class="name">NAME</h2>
<p> VBoxManage &#8211; x86 virtualization solution </p>
<h2>DESCRIPTION</h2>
<p> Oracle VM VirtualBox Command Line Management Interface (C) 2005-2019 Oracle Corporation All rights reserved. </p>
<p> Usage:</p>
<dl>
<dt>
<dd> VBoxManage [&lt;general option&gt;] &lt;command&gt;</dl>
<p> General Options:</p>
<dl>
<dt>[-v|&#8211;version]</p>
<dd> print version number and exit</p>
<dt>[-q|&#8211;nologo]</p>
<dd> suppress the logo</p>
<dt>[&#8211;settingspw &lt;pw&gt;]</p>
<dd> provide the settings password</p>
<dt>
<dd> [&#8211;settingspwfile &lt;file&gt;] provide a file containing the settings password [@&lt;response-file&gt;] load arguments from the given response file (bourne style)</dl>
<p> Commands:</p>
<dl>
<dt>list [&#8211;long|-l] [&#8211;sorted|-s]</p>
<dd> vms|runningvms|ostypes|hostdvds|hostfloppies|</p>
<dt>intnets|bridgedifs|hostonlyifs|natnets|dhcpservers|</p>
<dd> hostinfo|hostcpuids|hddbackends|hdds|dvds|floppies| usbhost|usbfilters|systemproperties|extpacks| groups|webcams|screenshotformats|cloudproviders| cloudprofiles</p>
<dt>showvminfo</p>
<dd> &lt;uuid|vmname&gt; [&#8211;details] [&#8211;machinereadable]</p>
<dt>showvminfo</p>
<dd> &lt;uuid|vmname&gt; <code>&#8211;log</code> &lt;idx&gt;</p>
<dt>registervm</p>
<dd> &lt;filename&gt;</p>
<dt>unregistervm</p>
<dd> &lt;uuid|vmname&gt; [&#8211;delete]</p>
<dt>createvm</p>
<dd> <code>&#8211;name</code> &lt;name&gt; [&#8211;groups &lt;group&gt;, &#8230;] [&#8211;ostype &lt;ostype&gt;] [&#8211;register] [&#8211;basefolder &lt;path&gt;] [&#8211;uuid &lt;uuid&gt;] [&#8211;default]</p>
<dt>modifyvm</p>
<dd> &lt;uuid|vmname&gt; [&#8211;name &lt;name&gt;] [&#8211;groups &lt;group&gt;, &#8230;] [&#8211;description &lt;desc&gt;] [&#8211;ostype &lt;ostype&gt;] [&#8211;iconfile &lt;filename&gt;] [&#8211;memory &lt;memorysize in MB&gt;] [&#8211;pagefusion on|off] [&#8211;vram &lt;vramsize in MB&gt;] [&#8211;acpi on|off] [&#8211;pciattach 03:04.0] [&#8211;pciattach 03:04.0@02:01.0] [&#8211;pcidetach 03:04.0] [&#8211;ioapic on|off] [&#8211;hpet on|off] [&#8211;triplefaultreset on|off] [&#8211;apic on|off] [&#8211;x2apic on|off] [&#8211;paravirtprovider none|default|legacy|minimal|</p>
<dt>hyperv|kvm]</p>
<dd> [&#8211;paravirtdebug &lt;key=value&gt; [,&lt;key=value&gt; &#8230;]] [&#8211;hwvirtex on|off] [&#8211;nestedpaging on|off] [&#8211;largepages on|off] [&#8211;vtxvpid on|off] [&#8211;vtxux on|off] [&#8211;pae on|off] [&#8211;longmode on|off] [&#8211;ibpb-on-vm-exit on|off] [&#8211;ibpb-on-vm-entry on|off] [&#8211;spec-ctrl on|off] [&#8211;l1d-flush-on-sched on|off] [&#8211;l1d-flush-on-vm-entry on|off] [&#8211;nested-hw-virt on|off] [&#8211;cpu-profile &quot;host|Intel 80[86|286|386]&quot;] [&#8211;cpuid-portability-level &lt;0..3&gt; [&#8211;cpuid-set &lt;leaf[:subleaf]&gt; &lt;eax&gt; &lt;ebx&gt; &lt;ecx&gt; &lt;edx&gt;] [&#8211;cpuid-remove &lt;leaf[:subleaf]&gt;] [&#8211;cpuidremoveall] [&#8211;hardwareuuid &lt;uuid&gt;] [&#8211;cpus &lt;number&gt;] [&#8211;cpuhotplug on|off] [&#8211;plugcpu &lt;id&gt;] [&#8211;unplugcpu &lt;id&gt;] [&#8211;cpuexecutioncap &lt;1-100&gt;] [&#8211;rtcuseutc on|off] [&#8211;graphicscontroller none|vboxvga|vmsvga|vboxsvga] [&#8211;monitorcount &lt;number&gt;] [&#8211;accelerate3d on|off] [&#8211;accelerate2dvideo on|off] [&#8211;firmware bios|efi|efi32|efi64] [&#8211;chipset ich9|piix3] [&#8211;bioslogofadein on|off] [&#8211;bioslogofadeout on|off] [&#8211;bioslogodisplaytime &lt;msec&gt;] [&#8211;bioslogoimagepath &lt;imagepath&gt;] [&#8211;biosbootmenu disabled|menuonly|messageandmenu] [&#8211;biosapic disabled|apic|x2apic] [&#8211;biossystemtimeoffset &lt;msec&gt;] [&#8211;biospxedebug on|off] [&#8211;boot&lt;1-4&gt; none|floppy|dvd|disk|net&gt;] [&#8211;nic&lt;1-N&gt; none|null|nat|bridged|intnet|hostonly|</p>
<dt>generic|natnetwork]</p>
<dd> [&#8211;nictype&lt;1-N&gt; Am79C970A|Am79C973|</p>
<dt>82540EM|82543GC|82545EM|</p>
<dd> virtio]</p>
<dt>[&#8211;cableconnected&lt;1-N&gt; on|off]</p>
<dd> [&#8211;nictrace&lt;1-N&gt; on|off] [&#8211;nictracefile&lt;1-N&gt; &lt;filename&gt;] [&#8211;nicproperty&lt;1-N&gt; name=[value]] [&#8211;nicspeed&lt;1-N&gt; &lt;kbps&gt;] [&#8211;nicbootprio&lt;1-N&gt; &lt;priority&gt;] [&#8211;nicpromisc&lt;1-N&gt; deny|allow-vms|allow-all] [&#8211;nicbandwidthgroup&lt;1-N&gt; none|&lt;name&gt;] [&#8211;bridgeadapter&lt;1-N&gt; none|&lt;devicename&gt;] [&#8211;hostonlyadapter&lt;1-N&gt; none|&lt;devicename&gt;] [&#8211;intnet&lt;1-N&gt; &lt;network name&gt;] [&#8211;nat-network&lt;1-N&gt; &lt;network name&gt;] [&#8211;nicgenericdrv&lt;1-N&gt; &lt;driver&gt; [&#8211;natnet&lt;1-N&gt; &lt;network&gt;|default] [&#8211;natsettings&lt;1-N&gt; [&lt;mtu&gt;],[&lt;socksnd&gt;],</p>
<dt>[&lt;sockrcv&gt;],[&lt;tcpsnd&gt;],</p>
<dd> [&lt;tcprcv&gt;]]</p>
<dt>[&#8211;natpf&lt;1-N&gt; [&lt;rulename&gt;],tcp|udp,[&lt;hostip&gt;],</p>
<dd> &lt;hostport&gt;,[&lt;guestip&gt;],&lt;guestport&gt;]</p>
<dt>[&#8211;natpf&lt;1-N&gt; delete &lt;rulename&gt;]</p>
<dd> [&#8211;nattftpprefix&lt;1-N&gt; &lt;prefix&gt;] [&#8211;nattftpfile&lt;1-N&gt; &lt;file&gt;] [&#8211;nattftpserver&lt;1-N&gt; &lt;ip&gt;] [&#8211;natbindip&lt;1-N&gt; &lt;ip&gt; [&#8211;natdnspassdomain&lt;1-N&gt; on|off] [&#8211;natdnsproxy&lt;1-N&gt; on|off] [&#8211;natdnshostresolver&lt;1-N&gt; on|off] [&#8211;nataliasmode&lt;1-N&gt; default|[log],[proxyonly],</p>
<dt>[sameports]]</p>
<dd> [&#8211;macaddress&lt;1-N&gt; auto|&lt;mac&gt;] [&#8211;mouse ps2|usb|usbtablet|usbmultitouch] [&#8211;keyboard ps2|usb [&#8211;uart&lt;1-N&gt; off|&lt;I/O base&gt; &lt;IRQ&gt;] [&#8211;uartmode&lt;1-N&gt; disconnected|</p>
<dt>server &lt;pipe&gt;|</p>
<dd> client &lt;pipe&gt;| tcpserver &lt;port&gt;| tcpclient &lt;hostname:port&gt;| file &lt;file&gt;| &lt;devicename&gt;]</p>
<dt>[&#8211;uarttype&lt;1-N&gt; 16450|16550A|16750</p>
<dd> [&#8211;lpt&lt;1-N&gt; off|&lt;I/O base&gt; &lt;IRQ&gt;] [&#8211;lptmode&lt;1-N&gt; &lt;devicename&gt;] [&#8211;guestmemoryballoon &lt;balloonsize in MB&gt;] [&#8211;audio none|null|oss|alsa|pulse] [&#8211;audioin on|off] [&#8211;audioout on|off] [&#8211;audiocontroller ac97|hda|sb16] [&#8211;audiocodec stac9700|ad1980|stac9221|sb16] [&#8211;clipboard disabled|hosttoguest|guesttohost|</p>
<dt>bidirectional]</p>
<dd> [&#8211;draganddrop disabled|hosttoguest|guesttohost|</p>
<dt>bidirectional]</p>
<dd> [&#8211;vrde on|off] [&#8211;vrdeextpack default|&lt;name&gt; [&#8211;vrdeproperty &lt;name=[value]&gt;] [&#8211;vrdeport &lt;hostport&gt;] [&#8211;vrdeaddress &lt;hostip&gt;] [&#8211;vrdeauthtype null|external|guest] [&#8211;vrdeauthlibrary default|&lt;name&gt; [&#8211;vrdemulticon on|off] [&#8211;vrdereusecon on|off] [&#8211;vrdevideochannel on|off] [&#8211;vrdevideochannelquality &lt;percent&gt;] [&#8211;usbohci on|off] [&#8211;usbehci on|off] [&#8211;usbxhci on|off] [&#8211;usbrename &lt;oldname&gt; &lt;newname&gt;] [&#8211;snapshotfolder default|&lt;path&gt;] [&#8211;teleporter on|off] [&#8211;teleporterport &lt;port&gt;] [&#8211;teleporteraddress &lt;address|empty&gt; [&#8211;teleporterpassword &lt;password&gt;] [&#8211;teleporterpasswordfile &lt;file&gt;|stdin] [&#8211;tracing-enabled on|off] [&#8211;tracing-config &lt;config-string&gt;] [&#8211;tracing-allow-vm-access on|off] [&#8211;usbcardreader on|off] [&#8211;autostart-enabled on|off] [&#8211;autostart-delay &lt;seconds&gt;] [&#8211;recording on|off] [&#8211;recording screens all|&lt;screen ID&gt; [&lt;screen ID&gt; &#8230;]] [&#8211;recording filename &lt;filename&gt;] [&#8211;recording videores &lt;width&gt; &lt;height&gt;] [&#8211;recording videorate &lt;rate&gt;] [&#8211;recording videofps &lt;fps&gt;] [&#8211;recording maxtime &lt;s&gt;] [&#8211;recording maxfilesize &lt;MB&gt;] [&#8211;recording opts &lt;key=value&gt; [,&lt;key=value&gt; &#8230;]] [&#8211;defaultfrontend default|&lt;name&gt;]</p>
<dt>clonevm</p>
<dd> &lt;uuid|vmname&gt; [&#8211;snapshot &lt;uuid&gt;|&lt;name&gt;] [&#8211;mode machine|machineandchildren|all] [&#8211;options link|keepallmacs|keepnatmacs|</p>
<dt>keepdisknames|keephwuuids]</p>
<dd> [&#8211;name &lt;name&gt;] [&#8211;groups &lt;group&gt;, &#8230;] [&#8211;basefolder &lt;basefolder&gt;] [&#8211;uuid &lt;uuid&gt;] [&#8211;register]</p>
<dt>movevm</p>
<dd> &lt;uuid|vmname&gt; <code>&#8211;type</code> basic [&#8211;folder &lt;path&gt;]</p>
<dt>import</p>
<dd> &lt;ovfname/ovaname&gt; [&#8211;dry-run|-n] [&#8211;options keepallmacs|keepnatmacs|importtovdi] [more options] (run with <code>-n</code> to have options displayed</p>
<dt>
<dd> for a particular OVF)</p>
<dt>export</p>
<dd> &lt;machines&gt; <code>&#8211;output</code>|-o &lt;name&gt;.&lt;ovf/ova/tar.gz&gt; [&#8211;legacy09|&#8211;ovf09|&#8211;ovf10|&#8211;ovf20|&#8211;opc10] [&#8211;manifest] [&#8211;iso] [&#8211;options manifest|iso|nomacs|nomacsbutnat] [&#8211;vsys &lt;number of virtual system&gt;]</p>
<dt>[&#8211;vmname &lt;name&gt;]</p>
<dd> [&#8211;product &lt;product name&gt;] [&#8211;producturl &lt;product url&gt;] [&#8211;vendor &lt;vendor name&gt;] [&#8211;vendorurl &lt;vendor url&gt;] [&#8211;version &lt;version info&gt;] [&#8211;description &lt;description info&gt;] [&#8211;eula &lt;license text&gt;] [&#8211;eulafile &lt;filename&gt;]</p>
<dt>[&#8211;cloud &lt;number of virtual system&gt;]</p>
<dd> [&#8211;vmname &lt;name&gt;] [&#8211;cloudprofile &lt;cloud profile name&gt;] [&#8211;cloudshape &lt;shape&gt;] [&#8211;clouddomain &lt;domain&gt;] [&#8211;clouddisksize &lt;disk size in GB&gt;] [&#8211;cloudbucket &lt;bucket name&gt;] [&#8211;cloudocivcn &lt;OCI vcn id&gt;] [&#8211;cloudocisubnet &lt;OCI subnet id&gt;] [&#8211;cloudkeepobject &lt;true/false&gt;] [&#8211;cloudlaunchinstance &lt;true/false&gt;] [&#8211;cloudpublicip &lt;true/false&gt;]</p>
<dt>startvm</p>
<dd> &lt;uuid|vmname&gt;&#8230; [&#8211;type gui|sdl|headless|separate] [-E|&#8211;putenv &lt;NAME&gt;[=&lt;VALUE&gt;]]</p>
<dt>controlvm</p>
<dd> &lt;uuid|vmname&gt; pause|resume|reset|poweroff|savestate| acpipowerbutton|acpisleepbutton| keyboardputscancode &lt;hex&gt; [&lt;hex&gt; &#8230;]| keyboardputstring &lt;string1&gt; [&lt;string2&gt; &#8230;]| keyboardputfile &lt;filename&gt;| setlinkstate&lt;1-N&gt; on|off | nic&lt;1-N&gt; null|nat|bridged|intnet|hostonly|generic|</p>
<dt>natnetwork [&lt;devicename&gt;] |</p>
<dd> nictrace&lt;1-N&gt; on|off | nictracefile&lt;1-N&gt; &lt;filename&gt; | nicproperty&lt;1-N&gt; name=[value] | nicpromisc&lt;1-N&gt; deny|allow-vms|allow-all | natpf&lt;1-N&gt; [&lt;rulename&gt;],tcp|udp,[&lt;hostip&gt;],</p>
<dt>&lt;hostport&gt;,[&lt;guestip&gt;],&lt;guestport&gt; |</p>
<dd> natpf&lt;1-N&gt; delete &lt;rulename&gt; | guestmemoryballoon &lt;balloonsize in MB&gt; | usbattach &lt;uuid&gt;|&lt;address&gt;</p>
<dt>[&#8211;capturefile &lt;filename&gt;] |</p>
<dd> usbdetach &lt;uuid&gt;|&lt;address&gt; | audioin on|off | audioout on|off | clipboard disabled|hosttoguest|guesttohost|</p>
<dt>bidirectional |</p>
<dd> draganddrop disabled|hosttoguest|guesttohost|</p>
<dt>bidirectional |</p>
<dd> vrde on|off | vrdeport &lt;port&gt; | vrdeproperty &lt;name=[value]&gt; | vrdevideochannelquality &lt;percent&gt; | setvideomodehint &lt;xres&gt; &lt;yres&gt; &lt;bpp&gt;</p>
<dt>[[&lt;display&gt;] [&lt;enabled:yes|no&gt; |</p>
<dd> [&lt;xorigin&gt; &lt;yorigin&gt;]]] |</p>
<dt>setscreenlayout &lt;display&gt; on|primary &lt;xorigin&gt; &lt;yorigin&gt; &lt;xres&gt; &lt;yres&gt; &lt;bpp&gt; | off</p>
<dd> screenshotpng &lt;file&gt; [display] | recording on|off | recording screens all|none|&lt;screen&gt;,[&lt;screen&gt;&#8230;] | recording filename &lt;file&gt; | recording videores &lt;width&gt;x&lt;height&gt; | recording videorate &lt;rate&gt; | recording videofps &lt;fps&gt; | recording maxtime &lt;s&gt; | recording maxfilesize &lt;MB&gt; | setcredentials &lt;username&gt;</p>
<dt><code>&#8211;passwordfile</code> &lt;file&gt; | &lt;password&gt;</p>
<dd> &lt;domain&gt; [&#8211;allowlocallogon &lt;yes|no&gt;] |</p>
<dt>teleport <code>&#8211;host</code> &lt;name&gt; <code>&#8211;port</code> &lt;port&gt;</p>
<dd> [&#8211;maxdowntime &lt;msec&gt;] [&#8211;passwordfile &lt;file&gt; |</p>
<dt><code>&#8211;password</code> &lt;password&gt;] |</p>
<dd> plugcpu &lt;id&gt; | unplugcpu &lt;id&gt; | cpuexecutioncap &lt;1-100&gt; webcam &lt;attach [path [settings]]&gt; | &lt;detach [path]&gt; | &lt;list&gt; addencpassword &lt;id&gt;</p>
<dt>&lt;password file&gt;|-</p>
<dd> [&#8211;removeonsuspend &lt;yes|no&gt;]</p>
<dt>removeencpassword &lt;id&gt;</p>
<dd> removeallencpasswords changeuartmode&lt;1-N&gt; disconnected|</p>
<dt>server &lt;pipe&gt;|</p>
<dd> client &lt;pipe&gt;| tcpserver &lt;port&gt;| tcpclient &lt;hostname:port&gt;| file &lt;file&gt;| &lt;devicename&gt;]</p>
<dt>discardstate</p>
<dd> &lt;uuid|vmname&gt;</p>
<dt>adoptstate</p>
<dd> &lt;uuid|vmname&gt; &lt;state_file&gt;</p>
<dt>snapshot</p>
<dd> &lt;uuid|vmname&gt; take &lt;name&gt; [&#8211;description &lt;desc&gt;] [&#8211;live]</p>
<dt>[&#8211;uniquename Number,Timestamp,Space,Force] |</p>
<dd> delete &lt;uuid|snapname&gt; | restore &lt;uuid|snapname&gt; | restorecurrent | edit &lt;uuid|snapname&gt;|&#8211;current</p>
<dt>[&#8211;name &lt;name&gt;]</p>
<dd> [&#8211;description &lt;desc&gt;] |</p>
<dt>list [&#8211;details|&#8211;machinereadable] |</p>
<dd> showvminfo &lt;uuid|snapname&gt;</p>
<dt>closemedium</p>
<dd> [disk|dvd|floppy] &lt;uuid|filename&gt; [&#8211;delete]</p>
<dt>storageattach</p>
<dd> &lt;uuid|vmname&gt; <code>&#8211;storagectl</code> &lt;name&gt; [&#8211;port &lt;number&gt;] [&#8211;device &lt;number&gt;] [&#8211;type dvddrive|hdd|fdd] [&#8211;medium none|emptydrive|additions|</p>
<dt>&lt;uuid|filename&gt;|host:&lt;drive&gt;|iscsi]</p>
<dd> [&#8211;mtype normal|writethrough|immutable|shareable|</p>
<dt>readonly|multiattach]</p>
<dd> [&#8211;comment &lt;text&gt;] [&#8211;setuuid &lt;uuid&gt;] [&#8211;setparentuuid &lt;uuid&gt;] [&#8211;passthrough on|off] [&#8211;tempeject on|off] [&#8211;nonrotational on|off] [&#8211;discard on|off] [&#8211;hotpluggable on|off] [&#8211;bandwidthgroup &lt;name&gt;] [&#8211;forceunmount] [&#8211;server &lt;name&gt;|&lt;ip&gt;] [&#8211;target &lt;target&gt;] [&#8211;tport &lt;port&gt;] [&#8211;lun &lt;lun&gt;] [&#8211;encodedlun &lt;lun&gt;] [&#8211;username &lt;username&gt;] [&#8211;password &lt;password&gt;] [&#8211;passwordfile &lt;file&gt;] [&#8211;initiator &lt;initiator&gt;] [&#8211;intnet]</p>
<dt>storagectl</p>
<dd> &lt;uuid|vmname&gt; <code>&#8211;name</code> &lt;name&gt; [&#8211;add ide|sata|scsi|floppy|sas|usb|pcie] [&#8211;controller LSILogic|LSILogicSAS|BusLogic|</p>
<dt>IntelAHCI|PIIX3|PIIX4|ICH6|I82078|</p>
<dd> [ USB|NVMe] [&#8211;portcount &lt;1-n&gt;] [&#8211;hostiocache on|off] [&#8211;bootable on|off] [&#8211;rename &lt;name&gt;] [&#8211;remove]</p>
<dt>bandwidthctl</p>
<dd> &lt;uuid|vmname&gt; add &lt;name&gt; <code>&#8211;type</code> disk|network</p>
<dt><code>&#8211;limit</code> &lt;megabytes per second&gt;[k|m|g|K|M|G] |</p>
<dd> set &lt;name&gt;</p>
<dt><code>&#8211;limit</code> &lt;megabytes per second&gt;[k|m|g|K|M|G] |</p>
<dd> remove &lt;name&gt; | list [&#8211;machinereadable] (limit units: k=kilobit, m=megabit, g=gigabit,</p>
<dt>
<dd> K=kilobyte, M=megabyte, G=gigabyte)</p>
<dt>showmediuminfo</p>
<dd> [disk|dvd|floppy] &lt;uuid|filename&gt;</p>
<dt>createmedium</p>
<dd> [disk|dvd|floppy] <code>&#8211;filename</code> &lt;filename&gt; [&#8211;size &lt;megabytes&gt;|&#8211;sizebyte &lt;bytes&gt;] [&#8211;diffparent &lt;uuid&gt;|&lt;filename&gt; [&#8211;format VDI|VMDK|VHD] (default: VDI) [&#8211;variant Standard,Fixed,Split2G,Stream,ESX,</p>
<dt>
<dd> Formatted]</p>
<dt>modifymedium</p>
<dd> [disk|dvd|floppy] &lt;uuid|filename&gt; [&#8211;type normal|writethrough|immutable|shareable|</p>
<dt>readonly|multiattach]</p>
<dd> [&#8211;autoreset on|off] [&#8211;property &lt;name=[value]&gt;] [&#8211;compact] [&#8211;resize &lt;megabytes&gt;|&#8211;resizebyte &lt;bytes&gt;] [&#8211;move &lt;path&gt;] [&#8211;setlocation &lt;path&gt;] [&#8211;description &lt;description string&gt;]</p>
<dt>clonemedium</p>
<dd> [disk|dvd|floppy] &lt;uuid|inputfile&gt; &lt;uuid|outputfile&gt; [&#8211;format VDI|VMDK|VHD|RAW|&lt;other&gt;] [&#8211;variant Standard,Fixed,Split2G,Stream,ESX] [&#8211;existing]</p>
<dt>mediumproperty</p>
<dd> [disk|dvd|floppy] set &lt;uuid|filename&gt; &lt;property&gt; &lt;value&gt;</p>
<dt>[disk|dvd|floppy] get &lt;uuid|filename&gt;</p>
<dd> &lt;property&gt;</p>
<dt>[disk|dvd|floppy] delete &lt;uuid|filename&gt;</p>
<dd> &lt;property&gt;</p>
<dt>encryptmedium</p>
<dd> &lt;uuid|filename&gt; [&#8211;newpassword &lt;file&gt;|-] [&#8211;oldpassword &lt;file&gt;|-] [&#8211;cipher &lt;cipher identifier&gt;] [&#8211;newpasswordid &lt;password identifier&gt;]</p>
<dt>checkmediumpwd</p>
<dd> &lt;uuid|filename&gt; &lt;pwd file&gt;|-</p>
<dt>convertfromraw</p>
<dd> &lt;filename&gt; &lt;outputfile&gt; [&#8211;format VDI|VMDK|VHD] [&#8211;variant Standard,Fixed,Split2G,Stream,ESX] [&#8211;uuid &lt;uuid&gt;]</p>
<dt>convertfromraw</p>
<dd> stdin &lt;outputfile&gt; &lt;bytes&gt; [&#8211;format VDI|VMDK|VHD] [&#8211;variant Standard,Fixed,Split2G,Stream,ESX] [&#8211;uuid &lt;uuid&gt;]</p>
<dt>getextradata</p>
<dd> global|&lt;uuid|vmname&gt; &lt;key&gt;|[enumerate]</p>
<dt>setextradata</p>
<dd> global|&lt;uuid|vmname&gt; &lt;key&gt; [&lt;value&gt;] (no value deletes key)</p>
<dt>setproperty</p>
<dd> machinefolder default|&lt;folder&gt; | hwvirtexclusive on|off | vrdeauthlibrary default|&lt;library&gt; | websrvauthlibrary default|null|&lt;library&gt; | vrdeextpack null|&lt;library&gt; | autostartdbpath null|&lt;folder&gt; | loghistorycount &lt;value&gt; defaultfrontend default|&lt;name&gt; logginglevel &lt;log setting&gt; proxymode system|noproxy|manual proxyurl &lt;url&gt;</p>
<dt>usbfilter</p>
<dd> add &lt;index,0-N&gt; <code>&#8211;target</code> &lt;uuid|vmname&gt;|global <code>&#8211;name</code> &lt;string&gt; <code>&#8211;action</code> ignore|hold (global filters only) [&#8211;active yes|no] (yes) [&#8211;vendorid &lt;XXXX&gt;] (null) [&#8211;productid &lt;XXXX&gt;] (null) [&#8211;revision &lt;IIFF&gt;] (null) [&#8211;manufacturer &lt;string&gt;] (null) [&#8211;product &lt;string&gt;] (null) [&#8211;remote yes|no] (null, VM filters only) [&#8211;serialnumber &lt;string&gt;] (null) [&#8211;maskedinterfaces &lt;XXXXXXXX&gt;]</p>
<dt>usbfilter</p>
<dd> modify &lt;index,0-N&gt; <code>&#8211;target</code> &lt;uuid|vmname&gt;|global [&#8211;name &lt;string&gt;] [&#8211;action ignore|hold] (global filters only) [&#8211;active yes|no] [&#8211;vendorid &lt;XXXX&gt;|&quot;&quot;] [&#8211;productid &lt;XXXX&gt;|&quot;&quot;] [&#8211;revision &lt;IIFF&gt;|&quot;&quot;] [&#8211;manufacturer &lt;string&gt;|&quot;&quot;] [&#8211;product &lt;string&gt;|&quot;&quot;] [&#8211;remote yes|no] (null, VM filters only) [&#8211;serialnumber &lt;string&gt;|&quot;&quot;] [&#8211;maskedinterfaces &lt;XXXXXXXX&gt;]</p>
<dt>usbfilter</p>
<dd> remove &lt;index,0-N&gt; <code>&#8211;target</code> &lt;uuid|vmname&gt;|global</p>
<dt>sharedfolder</p>
<dd> add &lt;uuid|vmname&gt; <code>&#8211;name</code> &lt;name&gt; <code>&#8211;hostpath</code> &lt;hostpath&gt; [&#8211;transient] [&#8211;readonly] [&#8211;automount]</p>
<dt>sharedfolder</p>
<dd> remove &lt;uuid|vmname&gt; <code>&#8211;name</code> &lt;name&gt; [&#8211;transient]</p>
<dt>guestproperty</p>
<dd> get &lt;uuid|vmname&gt; &lt;property&gt; [&#8211;verbose]</p>
<dt>guestproperty</p>
<dd> set &lt;uuid|vmname&gt; &lt;property&gt; [&lt;value&gt; [&#8211;flags &lt;flags&gt;]]</p>
<dt>guestproperty</p>
<dd> delete|unset &lt;uuid|vmname&gt; &lt;property&gt;</p>
<dt>guestproperty</p>
<dd> enumerate &lt;uuid|vmname&gt; [&#8211;patterns &lt;patterns&gt;]</p>
<dt>guestproperty</p>
<dd> wait &lt;uuid|vmname&gt; &lt;patterns&gt; [&#8211;timeout &lt;msec&gt;] [&#8211;fail-on-timeout]</p>
<dt>guestcontrol</p>
<dd> &lt;uuid|vmname&gt; [&#8211;verbose|-v] [&#8211;quiet|-q]</p>
<dt>[&#8211;username &lt;name&gt;] [&#8211;domain &lt;domain&gt;]</p>
<dd> [&#8211;passwordfile &lt;file&gt; | <code>&#8211;password</code> &lt;password&gt;]</p>
<dt>run [common-options]</p>
<dd> [&#8211;exe &lt;path to executable&gt;] [&#8211;timeout &lt;msec&gt;] [-E|&#8211;putenv &lt;NAME&gt;[=&lt;VALUE&gt;]] [&#8211;unquoted-args] [&#8211;ignore-operhaned-processes] [&#8211;profile] [&#8211;no-wait-stdout|&#8211;wait-stdout] [&#8211;no-wait-stderr|&#8211;wait-stderr] [&#8211;dos2unix] [&#8211;unix2dos] <code>&#8212;</code> &lt;program/arg0&gt; [argument1] &#8230; [argumentN]]</p>
<dt>start [common-options]</p>
<dd> [&#8211;exe &lt;path to executable&gt;] [&#8211;timeout &lt;msec&gt;] [-E|&#8211;putenv &lt;NAME&gt;[=&lt;VALUE&gt;]] [&#8211;unquoted-args] [&#8211;ignore-operhaned-processes] [&#8211;profile] <code>&#8212;</code> &lt;program/arg0&gt; [argument1] &#8230; [argumentN]]</p>
<dt>copyfrom [common-options]</p>
<dd> [&#8211;follow] [-R|&#8211;recursive] &lt;guest-src0&gt; [guest-src1 [&#8230;]] &lt;host-dst&gt;</p>
<dt>copyfrom [common-options]</p>
<dd> [&#8211;follow] [-R|&#8211;recursive] [&#8211;target-directory &lt;host-dst-dir&gt;] &lt;guest-src0&gt; [guest-src1 [&#8230;]]</p>
<dt>copyto [common-options]</p>
<dd> [&#8211;follow] [-R|&#8211;recursive] &lt;host-src0&gt; [host-src1 [&#8230;]] &lt;guest-dst&gt;</p>
<dt>copyto [common-options]</p>
<dd> [&#8211;follow] [-R|&#8211;recursive] [&#8211;target-directory &lt;guest-dst&gt;] &lt;host-src0&gt; [host-src1 [&#8230;]]</p>
<dt>mkdir|createdir[ectory] [common-options]</p>
<dd> [&#8211;parents] [&#8211;mode &lt;mode&gt;] &lt;guest directory&gt; [&#8230;]</p>
<dt>rmdir|removedir[ectory] [common-options]</p>
<dd> [-R|&#8211;recursive] &lt;guest directory&gt; [&#8230;]</p>
<dt>removefile|rm [common-options] [-f|&#8211;force]</p>
<dd> &lt;guest file&gt; [&#8230;]</p>
<dt>mv|move|ren[ame] [common-options]</p>
<dd> &lt;source&gt; [source1 [&#8230;]] &lt;dest&gt;</p>
<dt>mktemp|createtemp[orary] [common-options]</p>
<dd> [&#8211;secure] [&#8211;mode &lt;mode&gt;] [&#8211;tmpdir &lt;directory&gt;] &lt;template&gt;</p>
<dt>stat [common-options]</p>
<dd> &lt;file&gt; [&#8230;]</p>
<dt>guestcontrol</p>
<dd> &lt;uuid|vmname&gt; [&#8211;verbose|-v] [&#8211;quiet|-q]</p>
<dt>
<dd> list &lt;all|sessions|processes|files&gt; [common-opts]</p>
<dt>closeprocess [common-options]</p>
<dd> &lt; <code>&#8211;session-id</code> &lt;ID&gt;</p>
<dt>| <code>&#8211;session-name</code> &lt;name or pattern&gt;</p>
<dd> &lt;PID1&gt; [PID1 [&#8230;]]</p>
<dt>closesession [common-options]</p>
<dd> &lt; <code>&#8211;all</code> | <code>&#8211;session-id</code> &lt;ID&gt;</p>
<dt>
<dd> | <code>&#8211;session-name</code> &lt;name or pattern&gt; &gt;</p>
<dt>updatega|updateguestadditions|updateadditions</p>
<dd> [&#8211;source &lt;guest additions .ISO&gt;] [&#8211;wait-start] [common-options] [&#8211; [&lt;argument1&gt;] &#8230; [&lt;argumentN&gt;]]</p>
<dt>
<dd> watch [common-options]</p>
<dt>metrics</p>
<dd> list [*|host|&lt;vmname&gt; [&lt;metric_list&gt;]]</p>
<dt>
<dd> (comma-separated)</p>
<dt>metrics</p>
<dd> setup [&#8211;period &lt;seconds&gt;] (default: 1) [&#8211;samples &lt;count&gt;] (default: 1) [&#8211;list] [*|host|&lt;vmname&gt; [&lt;metric_list&gt;]]</p>
<dt>metrics</p>
<dd> query [*|host|&lt;vmname&gt; [&lt;metric_list&gt;]]</p>
<dt>metrics</p>
<dd> enable [&#8211;list] [*|host|&lt;vmname&gt; [&lt;metric_list&gt;]]</p>
<dt>metrics</p>
<dd> disable [&#8211;list] [*|host|&lt;vmname&gt; [&lt;metric_list&gt;]]</p>
<dt>metrics</p>
<dd> collect [&#8211;period &lt;seconds&gt;] (default: 1) [&#8211;samples &lt;count&gt;] (default: 1) [&#8211;list] [&#8211;detach] [*|host|&lt;vmname&gt; [&lt;metric_list&gt;]]</p>
<dt>natnetwork</p>
<dd> add <code>&#8211;netname</code> &lt;name&gt; <code>&#8211;network</code> &lt;network&gt; [&#8211;enable|&#8211;disable] [&#8211;dhcp on|off] [&#8211;port-forward-4 &lt;rule&gt;] [&#8211;loopback-4 &lt;rule&gt;] [&#8211;ipv6 on|off] [&#8211;port-forward-6 &lt;rule&gt;] [&#8211;loopback-6 &lt;rule&gt;]</p>
<dt>natnetwork</p>
<dd> remove <code>&#8211;netname</code> &lt;name&gt;</p>
<dt>natnetwork</p>
<dd> modify <code>&#8211;netname</code> &lt;name&gt; [&#8211;network &lt;network&gt;] [&#8211;enable|&#8211;disable] [&#8211;dhcp on|off] [&#8211;port-forward-4 &lt;rule&gt;] [&#8211;loopback-4 &lt;rule&gt;] [&#8211;ipv6 on|off] [&#8211;port-forward-6 &lt;rule&gt;] [&#8211;loopback-6 &lt;rule&gt;]</p>
<dt>natnetwork</p>
<dd> start <code>&#8211;netname</code> &lt;name&gt;</p>
<dt>natnetwork</p>
<dd> stop <code>&#8211;netname</code> &lt;name&gt;</p>
<dt>natnetwork</p>
<dd> list [&lt;pattern&gt;]</p>
<dt>hostonlyif</p>
<dd> ipconfig &lt;name&gt; [&#8211;dhcp | <code>&#8211;ip</code>&lt;ipv4&gt; [&#8211;netmask&lt;ipv4&gt; (def: 255.255.255.0)] | <code>&#8211;ipv6</code>&lt;ipv6&gt; [&#8211;netmasklengthv6&lt;length&gt; (def: 64)]] create | remove &lt;name&gt;</p>
<dt>dhcpserver</p>
<dd> add|modify <code>&#8211;netname</code> &lt;network_name&gt; |</p>
<dt><code>&#8211;ifname</code> &lt;hostonly_if_name&gt;</p>
<dd> [&#8211;ip &lt;ip_address&gt; <code>&#8211;netmask</code> &lt;network_mask&gt; <code>&#8211;lowerip</code> &lt;lower_ip&gt; <code>&#8211;upperip</code> &lt;upper_ip&gt;] [&#8211;enable | <code>&#8211;disable]</code> [&#8211;options [&#8211;vm &lt;name&gt; <code>&#8211;nic</code> &lt;1-N&gt;]</p>
<dt><code>&#8211;id</code> &lt;number&gt; [&#8211;value &lt;string&gt; | <code>&#8211;remove]]</code></p>
<dd> (multiple options allowed after <code>&#8211;options</code>)</p>
<dt>dhcpserver</p>
<dd> remove <code>&#8211;netname</code> &lt;network_name&gt; |</p>
<dt>
<dd> <code>&#8211;ifname</code> &lt;hostonly_if_name&gt;</p>
<dt>usbdevsource</p>
<dd> add &lt;source name&gt; <code>&#8211;backend</code> &lt;backend&gt; <code>&#8211;address</code> &lt;address&gt;</p>
<dt>usbdevsource</p>
<dd> remove &lt;source name&gt;</p>
<dt>
<dd> Medium content access:</p>
<dt>
<dd> VBoxManage mediumio &lt;[&#8211;disk=uuid|filename] | [&#8211;dvd=uuid|filename] | [&#8211;floppy=uuid|filename]&gt; [&#8211;password-file-|filename] formatfat [&#8211;quick]</p>
<dt>
<dd> VBoxManage mediumio &lt;[&#8211;disk=uuid|filename] | [&#8211;dvd=uuid|filename] | [&#8211;floppy=uuid|filename]&gt; [&#8211;password-file-|filename] cat [&#8211;hex] [&#8211;offset=byte-offset] [&#8211;size=bytes] [&#8211;output=-|filename]</p>
<dt>
<dd> VBoxManage mediumio &lt;[&#8211;disk=uuid|filename] | [&#8211;dvd=uuid|filename] | [&#8211;floppy=uuid|filename]&gt; [&#8211;password-file-|filename] stream [&#8211;format=image-format] [&#8211;variant=image-variant] [&#8211;output=-|filename]</p>
<dt>
<dd> Introspection and guest debugging:</p>
<dt>
<dd> VBoxManage debugvm &lt;uuid|vmname&gt; dumpvmcore [&#8211;filename=name]</p>
<dt>
<dd> VBoxManage debugvm &lt;uuid|vmname&gt; info &lt;item&gt; [args&#8230;]</p>
<dt>
<dd> VBoxManage debugvm &lt;uuid|vmname&gt; injectnmi</p>
<dt>
<dd> VBoxManage debugvm &lt;uuid|vmname&gt; log [[&#8211;release] | [&#8211;debug]] [group-settings&#8230;]</p>
<dt>
<dd> VBoxManage debugvm &lt;uuid|vmname&gt; logdest [[&#8211;release] | [&#8211;debug]] [destinations&#8230;]</p>
<dt>
<dd> VBoxManage debugvm &lt;uuid|vmname&gt; logflags [[&#8211;release] | [&#8211;debug]] [flags&#8230;]</p>
<dt>
<dd> VBoxManage debugvm &lt;uuid|vmname&gt; osdetect</p>
<dt>
<dd> VBoxManage debugvm &lt;uuid|vmname&gt; osinfo</p>
<dt>
<dd> VBoxManage debugvm &lt;uuid|vmname&gt; osdmesg [&#8211;lines=lines]</p>
<dt>
<dd> VBoxManage debugvm &lt;uuid|vmname&gt; getregisters [&#8211;cpu=id] [reg-set.reg-name&#8230;]</p>
<dt>
<dd> VBoxManage debugvm &lt;uuid|vmname&gt; setregisters [&#8211;cpu=id] [reg-set.reg-name=value&#8230;]</p>
<dt>
<dd> VBoxManage debugvm &lt;uuid|vmname&gt; show [[&#8211;human-readable] | [&#8211;sh-export] | [&#8211;sh-eval] | [&#8211;cmd-set]] [settings-item&#8230;]</p>
<dt>
<dd> VBoxManage debugvm &lt;uuid|vmname&gt; stack [&#8211;cpu=id]</p>
<dt>
<dd> VBoxManage debugvm &lt;uuid|vmname&gt; statistics [&#8211;reset] [&#8211;descriptions] [&#8211;pattern=pattern]</p>
<dt>
<dd> Extension package management:</p>
<dt>
<dd> VBoxManage extpack install [&#8211;replace] &lt;tarball&gt;</p>
<dt>
<dd> VBoxManage extpack uninstall [&#8211;force] &lt;name&gt;</p>
<dt>
<dd> VBoxManage extpack cleanup</p>
<dt>
<dd> Unattended guest OS installation:</p>
<dt>
<dd> VBoxManage unattended detect &lt;&#8211;iso=install-iso&gt; [&#8211;machine-readable]</p>
<dt>
<dd> VBoxManage unattended install &lt;uuid|vmname&gt; &lt;&#8211;iso=install-iso&gt; [&#8211;user=login] [&#8211;password=password] [&#8211;password-file=file] [&#8211;full-user-name=name] [&#8211;key=product-key] [&#8211;install-additions]</p>
<dt>
<dd> [&#8211;no-install-additions] [&#8211;additions-iso=add-iso] [&#8211;install-txs] [&#8211;no-install-txs] [&#8211;validation-kit-iso=testing-iso] [&#8211;locale=ll_CC] [&#8211;country=CC] [&#8211;time-zone=tz] [&#8211;hostname=fqdn] [&#8211;package-selection-adjustment=keyword] [&#8211;dry-run] [&#8211;auxiliary-base-path=path] [&#8211;image-index=number] [&#8211;script-template=file] [&#8211;post-install-template=file] [&#8211;post-install-command=command] [&#8211;extra-install-kernel-parameters=params] [&#8211;language=lang] [&#8211;start-vm=session-type] </p>
</dl>
<h2>Index</h2>
