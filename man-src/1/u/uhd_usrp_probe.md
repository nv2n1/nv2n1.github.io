---
title: "uhd_usrp_probe(1)"
name: "uhd_usrp_probe"
section: "1"
letter: "u"
url: "/docs/linux/man/1-uhd_usrp_probe/"
description: "uhd_usrp_probe – USRP Hardware Driver Peripheral Report Utility"
---

<h2>NAME</h2>
<p> uhd_usrp_probe &#8211; USRP Hardware Driver Peripheral Report Utility</p>
<h2>DESCRIPTION</h2>
<p> Report detailed information on UHD-supported Software Radio Peripherals attached by USB, network, or embedded configuration. </p>
<p> The UHD package is the universal hardware driver for Ettus Research products. The goal is to provide a host driver and API for current and future Ettus Research products. Users will be able to use the UHD driver standalone or with 3rd party applications. </p>
<p> Details include unit names, revision numbers, and available sensors on all attached USRP motherboards and daughterboards.</p>
<h2>SYNOPSIS</h2>
<p> <code>uhd_usrp_probe [OPTIONS]</code></p>
<h2>OPTIONS</h2>
<dl>
<dt>Device Address Arguments:</p>
<dd> &#8211;args <i>arg</i></p>
<dt>Print a complete property tree:</p>
<dd> &#8211;tree</p>
<dt>Query a string value from the properties tree:</p>
<dd> &#8211;string <i>arg</i></p>
<dt>Print the version string and exit:</p>
<dd> &#8211;version</p>
<dt>This help information:</p>
<dd> &#8211;help</dl>
<h2>IDENTIFYING USRP DEVICES</h2>
<p> Devices are addressed through key/value string pairs. These string pairs can be used to narrow down the search for a specific device or group of devices. Most UHD utility applications and examples have a &#8211;args parameter that takes a device address, where the device address is expressed as a delimited string. See the documentation in types/device_addr.hpp for reference. </p>
<p> Every device has several ways of identifying it on the host system.</p>
<h3>Identifying by hardware identifier</h3>
<p> All USRP devices can be found through their hardware series identifier, which match to USRP devices as follows: </p>
<p> Argument | Device </p>
<p> type=usrp1 | USRP1 </p>
<p> type=usrp2 | USRP2, USRP N200, USRP N210 </p>
<p> type=b100 | USRP B100 </p>
<p> type=e100 | USRP E100, USRP E110 </p>
<h3>Identifying by serial number</h3>
<p> All USRP devices are given a unique serial number, which can be used to identify a device as follows: </p>
<p> serial=12345678 </p>
<h3>Identifying by IP address</h3>
<p> USRP2, USRP N200, and USRP N210 devices connected to the host machine can all be found through their IP addresses, as follows: </p>
<p> addr=192.168.10.2 </p>
<h3>Identifying by name</h3>
<p> Users have the option of giving their USRP devices short names using the usrp_burn_mb_eeprom utility in lib/uhd/utils. Devices that have been given a name can be identified as follows: </p>
<p> name=foo </p>
<h2>EXAMPLES</h2>
<h3>Device discovery via command line</h3>
<p> Device address arguments can be supplied to narrow the scope of the search. </p>
<pre><code>
uhd_usrp_probe-- args = "type=usrp1" --OR-- uhd_usrp_probe-- args = "serial=12345678"
</code></pre>
<dl>
<dt>Find all devices available to this system:</p>
<dd> uhd_usrp_probe</dl>
<h2>SEE ALSO</h2>
<p> UHD documentation: <code><a rel="nofollow" href="http://files.ettus.com/uhd_docs/manual/html/index.html">http://files.ettus.com/uhd_docs/manual/html/index.html</a></code> </p>
<p> GR-UHD documentation: <code><a rel="nofollow" href="http://gnuradio.org/doc/doxygen/page_uhd.html">http://gnuradio.org/doc/doxygen/page_uhd.html</a></code> </p>
<p> Other UHD programs: </p>
<p> <a href="/docs/linux/man/1-uhd_find_devices/">uhd_find_devices</a>(1)</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Maitland Bottoms and Nicholas Corgan for the Debian project (but may be used by others).</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2010 Ettus Research LLC </p>
<p> This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<h2>Index</h2>
