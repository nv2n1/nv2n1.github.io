---

title: "sgpio(1)"
name: "sgpio"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sgpio/"
description: "sgpio – captive backplane LED control utility"
---

<h2>NAME</h2>
<p> sgpio &#8211; captive backplane LED control utility</p>
<p> <code>sgpio</code> [-h] [-V] [[-d|&#8211;disk &lt;device&gt;[,&lt;device&gt;&#8230;]] | [-p|&#8211;port &lt;port&gt;[,&lt;port&gt;&#8230;]]] [-s|&#8211;status &lt;status&gt;] [-f|&#8211;freq &lt;frequency&gt;]</p>
<p> Serial General Purpose Input Output (SGPIO) is a communication method used between a main board and a variety of internal and external hard disk drive bay enclosures. This utility can be used to control LEDs in an enclosure. For more information about SGPIO, please consult the SFF-8485 Specification.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-h, &#8211;help</dt>
<dd> displays a short help text</dd>
<dt>-V, &#8211;version</dt>
<dd> displays the utility and AHCI SGPIO specification</dd>
<dt>-d, &#8211;disk</dt>
<dd> disk name of LED location. Names are sda,sdb,sdc,&#8230; Multiple names can be provided in a comma-delimited list.</dd>
<dt>-p, &#8211;port</dt>
<dd> SATA port number of LED location, can be used if a disk name is no longer valid. 0,1,2,3,&#8230; Multiple ports can be provided in a comma-delimited list.</dd>
<dt>-s, &#8211;status</dt>
<dd> status of the LED to set. LED status is: locate, fault, rebuild, off</dd>
<dt>-f, &#8211;freq</dt>
<dd> Set the frequency at which the LED should blink (in Hz). Frequency should be an integer between 1 and 10. </dd>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>Set the locate LED on SDA with an Intel Intelligent backplane:</dt>
<dd> <code>sgpio</code> -d sda -s locate</dd></dl>
<dl>
<dt>Set the locate LED on SDA to flash at 3 Hz for non-intelligent backplanes:</dt>
<dd> <code>sgpio</code> -d sda -s locate -f 3</dd></dl>
<dl>
<dt>Set SATA port 2 with fault at a 3 Hz flash rate:</dt>
<dd> <code>sgpio</code> -p 2 -s fault -f 3</dd></dl>
<dl>
<dt>Set disks sda through sdf to fault:</dt>
<dd> <code>sgpio</code> -d sda,sdb,sdc,sdd,sde,sdf -s fault</dd></dl>
<h2>EXIT STATUS</h2>
<p> sgpio should return zero when successful. It will return with a non-zero value if there was a failure.</p>
<h2>AUTHOR</h2>
<p> Eric R. Hall &lt;Eric.R.Hall [at] intel.com&gt; </p>
