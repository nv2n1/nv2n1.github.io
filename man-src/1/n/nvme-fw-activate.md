---
title: "nvme-fw-activate(1)"
name: "nvme-fw-activate"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nvme-fw-activate/"
---

<h2 class="name">NAME</h2>
 

 nvme-fw-activate - Used to verify and commit a firmware image. 

<h2>SYNOPSIS</h2>

 

 <pre><code>
nvme fw - activate&lt;device&gt;[--slot = &lt;slot&gt; | -s&lt;slot&gt;]
                          [--action = &lt;action&gt; | -a&lt;action&gt;]
</code></pre>

<h2>DESCRIPTION</h2>

 

 For the NVMe device given, send an nvme Firmware Activate admin command and provides the results. 

 The Firmware Activate command is used to verify that a valid firmware image has been downloaded and to commit that revision to a specific firmware slot. The host may select the firmware image to activate on the next controller reset (CC.EN transitions from '1' to '0', a PCI function level reset, and/or other Controller or NVM Subsystem Reset) as part of this command. The currently executing firmware revision may be determined from the Firmware Revision field of the Identify Controller data structure as indicated in the Firmware Slot Information log page. 

 No further action is automatically taken to reset the device, which is usually required to complete the activation process. If your kernel and driver are recent enough, you can activate the firmware by issuing a reset through Linux sysfs, for example: 

<dl>
<dt>
<dd> <pre>
 # echo 1 &gt; /sys/class/misc/nvme0/device/reset
</pre></dl>
 

 If your kernel is not recent enough, you will need to remove and add the device some other way.

<h2>OPTIONS</h2>

 

 -a &lt;action&gt;, --action=&lt;action&gt;
<dl>
<dt>
<dd> Activate Action: This field specifies the action that is taken on the image downloaded with the Firmware Image Download command or on a previously downloaded and placed image. <table BORDER> <tr VALIGN=top><td> Value </td><td> Definition 
</td></tr> <tr VALIGN=top><td> 0 </td><td> Downloaded image replaces the image indicated by the Firmware Slot field. This image is not activated. 
</td></tr> <tr VALIGN=top><td> 1 </td><td> Downloaded image replaces the image indicated by the Firmware Slot field. This image is activated at the next reset. 
</td></tr> <tr VALIGN=top><td> 2 </td><td> The image indicated by the Firmware Slot field is activated at the next reset. 
</td></tr> <tr VALIGN=top><td> 3 </td><td> Reserved. 
</td></tr> </table> 

</dl>
 

 -s &lt;slot&gt;, --slot=&lt;slot&gt;
<dl>
<dt>
<dd> Firmware Slot: Specifies the firmware slot that shall be used for the Activate Action, if applicable. If the value specified is 0h, then the controller shall choose the firmware slot (slot 1 - 7) to use for the operation.</dl>

<h2>EXAMPLES</h2>

 

<dl>
<dt>
<dd> &bull; Activate the last downloaded fw to slot 1. 

<dl>
<dt>
<dd> <pre>
# nvme fw-activate /dev/nvme0 --slot=1 --action=2
</pre></dl>
</dl>

<h2>NVME</h2>

 

 Part of the nvme-user suite 

<h2>Index</h2>


