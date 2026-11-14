---
title: "modemtest(1)"
name: "modemtest"
section: "1"
letter: "m"
url: "/docs/linux/man/1-modemtest/"
---

<h2 class="name">NAME</h2>
 

 modemtest - Tool to examining your modem through Perl's Device::SerialPort 

<h2>SYNOPSIS</h2>

 modemtest [<font SIZE="-1">OPTS</font>] [<font SIZE="-1">DEVICE</font> [<font SIZE="-1">BAUD</font> [<font SIZE="-1">DATA</font> [<font SIZE="-1">PARITY</font> [<font SIZE="-1">STOP</font> [<font SIZE="-1">FLOW</font>]]]]]] 

 <pre>
 DEVICE    Device to use as a serial port (default: &quot;/dev/modem&quot;)
 BAUD      Serial speed to use            (default: 9600)
 DATA      Number of databits to use      (default: 8)
 PARITY    Type of parity to use          (default: &quot;none&quot;)
 STOP      Number of stop bits to use     (default: 1)
 FLOW      Kind of flow control to use    (default: &quot;none&quot;)
 -h, --help           Help report
     --skip-status    Skip modem status bit tests
     --hide-possible  Don't show all possible settings
</pre>

<h2>DESCRIPTION</h2>

 Some systems, serial ports, and modem behave in strange ways. To test the capabilities of Perl's Device::SerialPort, this tool queries the system settings for the given <font SIZE="-1">DEVICE,</font> and attempts to set up the port and send the initialization string ``<font SIZE="-1">ATE1''</font> to the modem, reporting the results seen.

<h2>SEE ALSO</h2>

 <i><a HREF="/docs/linux/man/3-device--serialport/">Device::SerialPort</a></i>(3) 

 <i><a HREF="/docs/linux/man/1-perl/">perl</a></i>(1)

<h2>AUTHOR</h2>

 Kees Cook &lt;kees [at] outflux.net&gt;.

<h2>COPYRIGHT AND LICENSE</h2>

 Copyright 2000-2004 by Kees Cook &lt;kees [at] outflux.net&gt;. 

 This program is free software; you may redistribute it and/or modify it under the same terms ans Perl itself. 

<h2>Index</h2>


