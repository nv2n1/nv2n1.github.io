---
title: "ipp-usb(8)"
name: "ipp-usb"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipp-usb/"
description: "ipp-usb – Daemon for IPP over USB printer support"
---

<p><code>ipp-usb</code> &#8211; Daemon for IPP over USB printer support</p>
<h2>Description</h2>
<p><code>ipp-usb</code> daemon enables driver-less printing and scanning on USB-only AirPrint-compatible printers and MFPs. </p>
<p> It works by connecting to the device by USB using IPP-over-USB protocol, and exposing the device to the network, including DNS-SD (ZeroConf) advertising. </p>
<p> IPP printing, eSCL scanning and web console are fully supported.</p>
<h2>Synopsis</h2>
<h3>Usage:</h3>
<p><code>ipp-usb mode [options]</code></p>
<h3>Modes are:</h3>
<dl>
<dt><code>standalone</code></p>
<dd>run forever, automatically discover IPP-over-USB devices and serve them all</p>
<dt><code>udev</code></p>
<dd>like standalone, but exit when last IPP-over-USB device is disconnected</p>
<dt><code>debug</code></p>
<dd>logs duplicated on console, -bg option is ignored</p>
<dt><code>check</code></p>
<dd>check configuration and exit</dl>
<h3>Options are</h3>
<dl>
<dt><code>-bg</code></p>
<dd>run in background (ignored in debug mode)</dl>
<h2>Configuration</h2>
<p><code>ipp-usb</code> searched for its configuration file in two places: 1. <code>/etc/ipp-usb/ipp-usb.conf</code> 2. <code>ipp-usb.conf</code> in the directory where executable file is located </p>
<p> Configuration file syntax is very similar to .INI files syntax. It consist of named sections, and each section contains a set of named variables. Comments are started from # or ; characters and continues until end of line:</p>
<dl>
<dd>
<pre># This is a comment
[section 1]
variable 1 = value 1 ; and another comment
variable 2 = value 2</pre>
<dd></dl>
<h3>Network parameters</h3>
<p>Network parameters are all in the <code>[network]</code> section:</p>
<dl>
<dd>
<pre>[network]
 # TCP ports for HTTP will be automatically allocated in the following range
 http-min-port = 60000
 http-max-port = 65535
 # Enable or disable DNS-SD advertisement
 dns-sd = enable # enable | disable
 # Network interface to use. Set to `all` if you want to expose you
 # printer to the local network. This way you can share your printer
 # with other computers in the network, as well as with iOS and Android
 # devices.
 interface = loopback # all | loopback
 # Enable or disable IPv6
 ipv6 = enable # enable | disable</pre>
<dd></dl>
<h3>Logging configuration</h3>
<p>Logging parameters are all in the <code>[logging]</code> section:</p>
<dl>
<dd>
<pre>[logging]
 # device-log - what logs are generated per device
 # main-log - what common logs are generated
 # console-log - what of generated logs goes to console
 #
 # parameter contains a comma-separated list of
 # the following keywords:
 # error - error messages
 # info - informative messages
 # debug - debug messages
 # trace-ipp, trace-escl, trace-http - very detailed per-protocol traces
 # all - all logs
 # trace-all - alias to all
 #
 # Note, trace-* implies debug, debug implies info, info implies error
 device-log = all
 main-log = debug
 console-log = debug
 # Log rotation parameters:
 # log-file-size - max log file before rotation. Use suffix M
 # for megabytes or K for kilobytes
 # log-backup-files - how many backup files to preserve during rotation
 #
 max-file-size = 256K
 max-backup-files = 5
 # Enable or disable ANSI colors on console
 console-color = enable # enable | disable</pre>
<dd></dl>
<h3>Quirks</h3>
<p>Some devices, due to their firmware bugs, require special handling, called device-specific <code>quirks</code>. <code>ipp-usb</code> loads quirks from the <code>/usr/share/ipp-usb/quirks/*.conf</code> files and from the <code>/etc/ipp-usb/quirks/*.conf</code> files. The <code>/etc/ipp-usb/quirks</code> directory is for system quirks overrides or admin changes. These files have .INI-file syntax with the content that looks like this:</p>
<dl>
<dd>
<pre>[HP LaserJet MFP M28-M31]
 http-connection = keep-alive
[HP OfficeJet Pro 8730]
 http-connection = close
[HP Inc. HP Laser MFP 135a]
 blacklist = true
# Default configuration
[*]
 http-connection = &quot;&quot;</pre>
<dd></dl>
<p> For each discovered device, its model name is matched against sections of the quirks files. The section name contains an exact model name, which contains <code>iManufacturer</code>+<code>iProduct</code> entries from <code>lsusb -v</code> command output, or it may contain glob-style wildcards: <code>*</code> that matches any sequence of characters and <code>?</code> , that matches any single character. To match one of these characters (<code>*</code> and <code>?</code>) literally, use backslash as escape. </p>
<p> All matching sections from all quirks files are taken in consideration, and applied in priority order. Priority is computed using the following algorithm:</p>
<dl>
<dt>&#x25cb;</p>
<dd>When matching model name against section name, amount of non-wildcard matched characters is counted, and the longer match wins</p>
<dt>&#x25cb;</p>
<dd>Otherwise, section loaded first wins. Files are loaded in alphabetical order, sections read sequentially</p>
<dd></dl>
<p> If some parameter exist in multiple sections, used its value from the most priority section </p>
<p> The following parameters are defined:</p>
<dl>
<dt><code>blacklist = true | false</code></p>
<dd>If <code>true</code>, the matching device is ignored by the <code>ipp-usb</code></p>
<dt><code>http-XXX = YYY</code></p>
<dd>Set XXX header of the HTTP requests forwarded to device to YYY. If YYY is empty string, XXX header is removed</p>
<dt><code>usb-max-interfaces = N</code></p>
<dd>Don&#8217;t use more that N USB interfaces, even if more is available</dl>
<p> In case of you found out about your device needs a quirk to work properly or it does not work with <code>ipp-usb</code> at all, although it provides IPP-over-USB interface, please report the isues at <a rel="nofollow" href="https://github.com/OpenPrinting/ipp-usb.">https://github.com/OpenPrinting/ipp-usb.</a> The possible quirk for the device can be added to the project itself and fix the situation for all device&#8217;s owners.</p>
<h2>Files</h2>
<dl>
<dt>&#x25cb;</p>
<dd><code>/etc/ipp-usb/ipp-usb.conf</code>: the daemon configuration file</p>
<dt>&#x25cb;</p>
<dd><code>/var/log/ipp-usb/main.log</code>: the main log file</p>
<dt>&#x25cb;</p>
<dd><code>/var/log/ipp-usb/&lt;DEVICE&gt;.log</code>: per-device log files</p>
<dt>&#x25cb;</p>
<dd><code>/var/ipp-usb/dev/&lt;DEVICE&gt;.state</code>: device state (HTTP port allocation, DNS-SD name)</p>
<dt>&#x25cb;</p>
<dd><code>/var/ipp-usb/lock/ipp-usb.lock</code>: lock file, that helps to prevent multiple copies of daemon to run simultaneously</p>
<dt>&#x25cb;</p>
<dd><code>/usr/share/ipp-usb/quirks/*.conf</code>: device-specific quirks (see above)</p>
<dt>&#x25cb;</p>
<dd><code>/etc/ipp-usb/quirks/*.conf</code>: device-specific quirks defined by sysadmin (see above)</p>
<dd></dl>
<h2>Copyright</h2>
<p>Copyright (c) by Alexander Pevzner (pzz [at] apevzner.com)<br />
 All rights reserved. </p>
<p> This program is licensed under 2-Clause BSD license. See LICENSE file for details.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-cups/">cups</a>(1) </p>
