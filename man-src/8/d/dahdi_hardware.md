---
title: "dahdi_hardware(8)"
name: "dahdi_hardware"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dahdi_hardware/"
---

dahdi_hardware - Shows Dahdi hardware devices.

<h2>Synopsis</h2>

dahdi_hardware [-v][-x]

<h2>Options</h2>

<dl><dt>-v
<dd>Verbose ouput - show spans used by each device etc. Currently only implemented for the Xorcom Astribank.
<dt>-x
<dd>Show disconnected Astribank unit, if any.</dl>

<h2>Description</h2>

Show all dahdi hardware devices. Devices are recognized according to lists of <font SIZE="-1">PCI</font> and <font SIZE="-1">USB</font> IDs in Dahdi::Hardware::PCI.pm and Dahdi::Hardware::USB.pm . For <font SIZE="-1">PCI</font> it is possible to detect by sub-vendor and sub-product <font SIZE="-1">ID</font> as well. The first output column is the connector: a bus specific field that shows where this device is. The second field shows which driver should handle the device. a ``-'' sign marks that the device is not yet handled by this driver. A ``+'' sign means that the device is handled by the driver. For the Xorcom Astribank (and in the future: for other Dahdi devices) some further information is provided from the driver. Those extra lines always begin with spaces. Example output: Without drivers loaded: <pre> usb:001/002 xpp_usb- e4e4:1152 Astribank-multi FPGA-firmware
 usb:001/003 xpp_usb- e4e4:1152 Astribank-multi FPGA-firmware
 pci:0000:01:0b.0 wctdm- e159:0001 Wildcard TDM400P REV H</pre>With drivers loaded, without -v: 
&nbsp;<wbr>&nbsp;<wbr>usb:001/002&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>xpp_usb+&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>e4e4:1152 Astribank-multi FPGA-firmware 
&nbsp;<wbr>&nbsp;<wbr>usb:001/003&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>xpp_usb+&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>e4e4:1152 Astribank-multi FPGA-firmware 
&nbsp;<wbr>&nbsp;<wbr>pci:0000:01:0b.0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>wctdm+&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>e159:0001&nbsp;<wbr>&nbsp;<wbr>Wildcard&nbsp;<wbr><font SIZE="-1">TDM400P</font>&nbsp;<wbr><font SIZE="-1">REV</font>&nbsp;<wbr>E/F With drivers loaded, with -v: 
&nbsp;<wbr>&nbsp;<wbr>usb:001/002&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>xpp_usb+&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>e4e4:1152 Astribank-multi FPGA-firmware 
LABEL=[usb:123]&nbsp;<wbr>CONNECTOR=usb-0000:00:1d.7-1&nbsp;<wbr>&nbsp;<wbr> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><font SIZE="-1">XBUS-00/XPD-00:</font>&nbsp;<wbr><font SIZE="-1">FXS</font>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Span 2&nbsp;<wbr> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><font SIZE="-1">XBUS-00/XPD-10:</font>&nbsp;<wbr><font SIZE="-1">FXS</font>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Span 3&nbsp;<wbr> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><font SIZE="-1">XBUS-00/XPD-20:</font>&nbsp;<wbr><font SIZE="-1">FXS</font>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Span 4&nbsp;<wbr> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><font SIZE="-1">XBUS-00/XPD-30:</font>&nbsp;<wbr><font SIZE="-1">FXS</font>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Span 5&nbsp;<wbr> 
&nbsp;<wbr>&nbsp;<wbr>usb:001/003&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>xpp_usb+&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>e4e4:1152 Astribank-multi FPGA-firmware 
LABEL=[usb:4567]&nbsp;<wbr>CONNECTOR=usb-0000:00:1d.7-4&nbsp;<wbr>&nbsp;<wbr> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><font SIZE="-1">XBUS-01/XPD-00:</font>&nbsp;<wbr><font SIZE="-1">FXS</font>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Span 6 XPP-SYNC 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><font SIZE="-1">XBUS-01/XPD-10:</font>&nbsp;<wbr><font SIZE="-1">FXO</font>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Span 7&nbsp;<wbr> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><font SIZE="-1">XBUS-01/XPD-20:</font>&nbsp;<wbr><font SIZE="-1">FXO</font>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Span 8&nbsp;<wbr> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><font SIZE="-1">XBUS-01/XPD-30:</font>&nbsp;<wbr><font SIZE="-1">FXO</font>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Span 9&nbsp;<wbr> 
&nbsp;<wbr>&nbsp;<wbr>pci:0000:01:0b.0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>wctdm+&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>e159:0001&nbsp;<wbr>&nbsp;<wbr>Wildcard&nbsp;<wbr><font SIZE="-1">TDM400P</font>&nbsp;<wbr><font SIZE="-1">REV</font>&nbsp;<wbr>E/F 
