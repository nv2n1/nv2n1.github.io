---
title: "usrp2_card_burner(1)"
name: "usrp2_card_burner"
section: "1"
letter: "u"
url: "/docs/linux/man/1-usrp2_card_burner/"
description: "usrp2_card_burner – USRP N-Series FPGA/Firmware Burner"
---

<h2>NAME</h2>
<p> usrp2_card_burner &#8211; USRP N-Series FPGA/Firmware Burner</p>
<h2>DESCRIPTION</h2>
<p> Burn USRP2 firmware and FPGA images onto an SD card plugged into the host machine.</p>
<h2>SYNOPSIS</h2>
<p> <code>usrp2_card_burner [OPTIONS]</code></p>
<h2>OPTIONS</h2>
<dl>
<dt>Raw device path:</p>
<dd> &#8211;addr=<i>&quot;Address&quot;</i> (default: 192.168.10.2)</p>
<dt>This help information:</p>
<dd> &#8211;help</p>
<dt>Firmware Filepath:</p>
<dd> &#8211;fw=<i>&quot;filepath&quot;</i></p>
<dt>FPGA Filepath:</p>
<dd> &#8211;fpga=<i>&quot;filepath&quot;</i></p>
<dt>List all USRP devices without burning</p>
<dd> &#8211;list</p>
<dt>Override safety check</p>
<dd> &#8211;force</dl>
<h2>EXAMPLES</h2>
<h3>Standard burning procedure</h3>
<p> usrp2_card_burner &#8211;dev=/dev/sdd1 &#8211;fw=usrp2_fw.bin &#8211;fpga=usrp2_fpga.bin</p>
<h2>SEE ALSO</h2>
<p> UHD documentation: <code><a rel="nofollow" href="http://files.ettus.com/uhd_docs/manual/html/index.html">http://files.ettus.com/uhd_docs/manual/html/index.html</a></code> </p>
<p> GR-UHD documentation: <code><a rel="nofollow" href="http://gnuradio.org/doc/doxygen/page_uhd.html">http://gnuradio.org/doc/doxygen/page_uhd.html</a></code> </p>
<p> Other UHD programs: </p>
<p> <a href="/docs/linux/man/1-uhd_images_downloader/">uhd_images_downloader</a>(1) <a href="/docs/linux/man/1-usrp_n2xx_simple_net_burner/">usrp_n2xx_simple_net_burner</a>(1)</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Nicholas Corgan for the Debian project (but may be used by others).</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2012 Ettus Research LLC </p>
<p> This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<h2>Index</h2>
