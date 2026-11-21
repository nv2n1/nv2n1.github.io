---
title: "uhd_cal_rx_iq_balance(1)"
name: "uhd_cal_rx_iq_balance"
section: "1"
letter: "u"
url: "/docs/linux/man/1-uhd_cal_rx_iq_balance/"
description: "uhd_cal_rx_iq_balance – Generate RX IQ Balance Calibration Table for a UHD Device"
---

<h2>NAME</h2>
<p> uhd_cal_rx_iq_balance &#8211; Generate RX IQ Balance Calibration Table for a UHD Device</p>
<h2>DESCRIPTION</h2>
<p> The Universal Software Radio Peripheral Hardware Drivers handle calibration information. This application reduces RX IQ imbalance within the specified frequency range using transmit leakage into the receive path. Remove all external hardware from the RF antenna ports before using this application. This can take up to several minutes with default settings. </p>
<p> NOTE: This application can only be used with the WBX, SBX, XCVR2450, and RFX daughterboards.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></dt>
<dd> help message</dd>
<dt><code>&#8211;verbose</code></dt>
<dd> enable some verbose</dd>
<dt><code>&#8211;args</code> arg</dt>
<dd> device address args [default = &quot;&quot;]</dd>
<dt><code>&#8211;tx_wave_freq</code> arg (=507123)</dt>
<dd> Transmit wave frequency in Hz</dd>
<dt><code>&#8211;tx_wave_ampl</code> arg (=0.69999999999999996)</dt>
<dd> Transmit wave amplitude in counts</dd>
<dt><code>&#8211;tx_offset</code> arg (=934400)</dt>
<dd> TX LO offset from the RX LO in Hz</dd>
<dt><code>&#8211;freq_start</code> arg</dt>
<dd> Frequency start in Hz (will use beginning of frequency range if unspecified)</dd>
<dt><code>&#8211;freq_stop</code> arg</dt>
<dd> Frequency stop in Hz (will use end of frequency range if unspecified)</dd>
<dt><code>&#8211;freq_step</code> arg (=7300000)</dt>
<dd> Step size for LO sweep in Hz</dd>
<dt><code>&#8211;nsamps</code> arg (=10000)</dt>
<dd> Samples per data capture</dd></dl>
<h2>SEE ALSO</h2>
<p> UHD documentation: <code><a rel="nofollow" href="http://files.ettus.com/uhd_docs/manual/html/index.html">http://files.ettus.com/uhd_docs/manual/html/index.html</a></code> </p>
<p> GR-UHD documentation: <code><a rel="nofollow" href="http://gnuradio.org/doc/doxygen/page_uhd.html">http://gnuradio.org/doc/doxygen/page_uhd.html</a></code> </p>
<p> Other UHD programs: </p>
<p> <a href="/docs/linux/man/1-uhd_cal_tx_dc_offset/">uhd_cal_tx_dc_offset</a>(1) <a href="/docs/linux/man/1-uhd_cal_tx_iq_balance/">uhd_cal_tx_iq_balance</a>(1)</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Maitland Bottoms and Nicholas Corgan for the Debian project (but may be used by others).</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2012 Ettus Research LLC </p>
<p> This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
