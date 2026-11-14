---
title: "uhd_images_downloader(1)"
name: "uhd_images_downloader"
section: "1"
letter: "u"
url: "/docs/linux/man/1-uhd_images_downloader/"
description: "uhd_images_downloader – USRP Hardware Driver firmware/FPGA downloader"
---

<h2>NAME</h2>
<p> uhd_images_downloader &#8211; USRP Hardware Driver firmware/FPGA downloader</p>
<h2>DESCRIPTION</h2>
<p> The UHD package is the universal hardware driver for Ettus Research products. The goal of the UHD is to provide a host driver and API for current and future Ettus Research products. Users will be able to use the UHD driver standalone or with 3rd party applications. </p>
<p> This program installs the firmware and FPGA binaries from Ettus Research matching this UHD driver release onto the host system. If the uhd-images package is installed, there is no need to run this installer.</p>
<h2>SYNOPSIS</h2>
<p> <code>uhd_images_downloader</code> Usage: uhd_images_downloader.py [options]</p>
<h2>OPTIONS</h2>
<p> This program works best without any arguments. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-h, &#8211;help&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>show this help message and exit </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211;download-location=DOWNLOAD_LOCATION<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Set custom download location for images,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[default=/usr/share/uhd/images] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211;buffer-size=BUFFER_SIZE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Set download buffer size,&nbsp;<wbr>[default=8192]</p>
<h2>SEE ALSO</h2>
<p> UHD documentation: <code><a rel="nofollow" href="http://files.ettus.com/uhd_docs/manual/html/index.html">http://files.ettus.com/uhd_docs/manual/html/index.html</a></code> </p>
<p> GR-UHD documentation: <code><a rel="nofollow" href="http://gnuradio.org/doc/doxygen/page_uhd.html">http://gnuradio.org/doc/doxygen/page_uhd.html</a></code> </p>
<p> Other UHD programs: </p>
<p> <a href="/docs/linux/man/1-usrp2_card_burner/">usrp2_card_burner</a>(1) <a href="/docs/linux/man/1-usrp_n2xx_simple_net_burner/">usrp_n2xx_simple_net_burner</a>(1)</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Maitland Bottoms and Nicholas Corgan for the Debian project (but may be used by others).</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2012 Ettus Research LLC </p>
<p> This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<h2>Index</h2>
