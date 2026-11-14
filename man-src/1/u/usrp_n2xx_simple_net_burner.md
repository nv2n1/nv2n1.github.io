---
title: "usrp_n2xx_simple_net_burner(1)"
name: "usrp_n2xx_simple_net_burner"
section: "1"
letter: "u"
url: "/docs/linux/man/1-usrp_n2xx_simple_net_burner/"
description: "usrp_n2xx_simple_net_burner – USRP N-Series FPGA/Firmware Burner"
---

<h2>NAME</h2>
<p> usrp_n2xx_simple_net_burner &#8211; USRP N-Series FPGA/Firmware Burner</p>
<h2>DESCRIPTION</h2>
<p> Burn firmware and FPGA images onto connected USRP N-Series devices. The program takes an IP address as an argument, queries the USRP device to identify which model and revision it is, and burns the appropriate images over Ethernet.</p>
<h2>SYNOPSIS</h2>
<p> <code>usrp_n2xx_simple_net_burner [OPTIONS]</code></p>
<h2>OPTIONS</h2>
<p> This program works best when only an IP address is specified.</p>
<dl>
<dt>Device IP Address:</p>
<dd> &#8211;addr=<i>&quot;Address&quot;</i> (default: 192.168.10.2)</p>
<dt>This help information:</p>
<dd> &#8211;help</p>
<dt>Custom Firmware Filepath:</p>
<dd> &#8211;fw=<i>&quot;filepath&quot;</i></p>
<dt>Custom FPGA Filepath:</p>
<dd> &#8211;fpga=<i>&quot;filepath&quot;</i></p>
<dt>Don&#8217;t burn firmware:</p>
<dd> &#8211;no_fw</p>
<dt>Don&#8217;t burn FPGA:</p>
<dd> &#8211;no_fpga</p>
<dt>Automatically reboot USRP device after burning</p>
<dd> &#8211;auto_reboot</p>
<dt>List all USRP devices without burning</p>
<dd> &#8211;list</dl>
<h2>EXAMPLES</h2>
<h3>Selecting a USRP device with a non-standard IP address</h3>
<p> usrp_n2xx_simple_net_burner &#8211;addr=192.168.10.3</p>
<h2>SEE ALSO</h2>
<p> UHD documentation: <code><a rel="nofollow" href="http://files.ettus.com/uhd_docs/manual/html/index.html">http://files.ettus.com/uhd_docs/manual/html/index.html</a></code> </p>
<p> GR-UHD documentation: <code><a rel="nofollow" href="http://gnuradio.org/doc/doxygen/page_uhd.html">http://gnuradio.org/doc/doxygen/page_uhd.html</a></code> </p>
<p> Other UHD programs: </p>
<p> <a href="/docs/linux/man/1-uhd_images_downloader/">uhd_images_downloader</a>(1) <a href="/docs/linux/man/1-usrp2_card_burner/">usrp2_card_burner</a>(1)</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Nicholas Corgan for the Debian project (but may be used by others).</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2012 Ettus Research LLC </p>
<p> This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<h2>Index</h2>
