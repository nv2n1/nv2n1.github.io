---
title: "powercom(8)"
name: "powercom"
section: "8"
letter: "p"
url: "/docs/linux/man/8-powercom/"
description: "powercom – UPS driver for serial Powercom/Trust/Advice UPS equipment"
---

<p>powercom &#8211; UPS driver for serial Powercom/Trust/Advice UPS equipment</p>
<h2>Note</h2>
<p>This man page only documents the hardware-specific features of the powercom driver. For information about the core driver, see <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8).</p>
<h2>Supported Hardware</h2>
<p>This driver supports many similar kinds of serial UPS hardware (as well as a few USB UPS models with USB-to-serial adapters). The most common ones are the Trust 425/625, Powercom, and Advice Partner/King PR750. Others using the same protocol may also work. For USB connections, you might need <code><a href="/docs/linux/man/8-usbhid-ups/">usbhid-ups</a></code>(8). </p>
<p> For more specific guidance on which driver is applicable for a USB connection, see the NUT Hardware Compatibility List (HCL).</p>
<h2>Extra Arguments</h2>
<p>This driver supports the following optional settings in the <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5) file: </p>
<p> <code>linevoltage</code>=<i>value</i></p>
<dl>
<dd>An integer specifying the line voltage. It can&#8217;t be auto detected. Acceptable values are in the range of 110-120 or 220-240. The default is <i>230</i>.</dl>
<p> <code>manufacturer</code>=<i>name</i></p>
<dl>
<dd>Specify the manufacturer name, which also can&#8217;t be auto detected. This is a user defined string, so any name is acceptable. The default is <i>PowerCom</i>.</dl>
<p> <code>modelname</code>=<i>name</i></p>
<dl>
<dd>Specify the model name, which also can&#8217;t be auto detected. This is a user defined string, so any name is acceptable. The default is <i>Unknown</i>.</dl>
<p> <code>serialnumber</code>=<i>value</i></p>
<dl>
<dd>Like modelname above, but for the serial number. The default is <i>Unknown</i>.</dl>
<p> <code>type</code>=<i>name</i></p>
<dl>
<dd>The exact type of the communication protocol within the powercom family, that will be used to communicate with the UPS. The type is named after the first modelname that was coded with that protocol. The acceptable names are <i>Trust</i>, <i>Egys</i>, <i>KP625AP</i>, <i>IMP</i>, <i>KIN</i>, <i>BNT</i>, <i>BNT-other</i> and <i>OPTI</i>. The default is <i>Trust</i>. </p>
<p> <i>BNT-other</i> is a special type for other BNT models (such as the 1500A at 120V and can be used to override ALL models using ALL of the following values.</dl>
<p> <code>shutdownArguments</code>=&#123;&#123;<i>minutes</i>,<i>seconds</i>},<i>whether_minutes_should_be_used</i>}</p>
<dl>
<dd>The minutes and seconds that the UPS should wait between receiving the shutdown command and actually shutting off. The other argument should be set to the character <i>n</i> only when the minutes value should be skipped and not sent to the UPS. The default is type-dependent and is given below. The braces and commas are mandatory. Note that there should be no whitespace characters.</dl>
<p> <code>numOfBytesFromUPS</code>=<i>value</i></p>
<dl>
<dd>The number of bytes in a UPS frame: 16 is common, 11 for <i>Trust</i>. The default is type-dependent and is given below.</dl>
<p> <code>methodOfFlowControl</code>=<i>name</i></p>
<dl>
<dd>The method of serial communication flow control that is engaged by the UPS. The default is type-dependent and is given below. Acceptable names are <i>dtr0rts1</i>, <i>dtr1</i> or <i>no_flow_control</i>.</dl>
<p> <code>validationSequence</code>=&#123;&#123;<i>index1</i>,<i>value1</i>},{<i>index2</i>,<i>value2</i>},{<i>index3</i>,<i>value3</i>}}</p>
<dl>
<dd>(Only for types KP625AP, Trust, Egys.) 3 pairs to be used for validating the UPS by comparing bytes of the raw data with constant values. The index selects the byte from the UPS (see numOfBytesFromUPS) and the value is for matching to the byte. The default is type-dependent and is given below. The braces and commas are mandatory, as the lack of white space characters.</dl>
<p> <code>frequency</code>={<i>A</i>,<i>B</i>}</p>
<dl>
<dd>(Only for types KP625AP, Trust, Egys.) A pair to convert the raw frequency data to a human-readable frequency reading using the function 1/(A*x+B). If the raw value x IS the frequency, then set A=1/(x^2) and B=0. The default is type-dependent and is given below. Do note that the braces and commas are mandatory as well, as the lack of whitespace characters.</dl>
<p> <code>loadPercentage</code>={<i>BatteryA</i>,<i>BatteryB</i>,<i>LineA</i>,<i>LineB</i>}</p>
<dl>
<dd>(Only for types KP625AP, Trust, Egys.) A quad to convert the raw load data to human readable load percentage reading using the function A*x+B. If the raw value x IS the Load Percent, then set A=1 and B=0. The default is type-dependent and is given below. Do note that the braces and commas are mandatory, as the lack of white space characters.</dl>
<p> <code>batteryPercentage</code>={<i>Battery1</i>,<i>Battery2</i>,<i>Battery3</i>,<i>Line4</i>,<i>Line5</i>}</p>
<dl>
<dd>(Only for KP625AP, Trust, Egys.) A 5 tuple to convert the raw battery and line data to a human-readable battery and line percentage reading using the functions (Battery) A*x+B*y+C and (Line) D*x+E. If the raw value x IS the Battery Percent, then set A=1, B=0, C=0, D=1, E=0. The default is type-dependent and is given below. Do note that the braces and commas are mandatory, as the lack of white space characters.</dl>
<p> <code>voltage</code>={<i>240A</i>,<i>240B</i>,<i>120A</i>,<i>120B</i>}</p>
<dl>
<dd>(Only for types KP625AP, Trust, Egys.) A quad that is used convert the raw voltage data to a human-readable voltage reading using the function A*x+B. If the raw value x IS HALF the Voltage, then set A=2, B=0. The default is type-dependent and is given below. Do note that the braces and commas are mandatory, as well as the lack of whitespace characters.</dl>
<h2>Default Values For The Extra Arguments</h2>
<dl>
<dd>
<pre>linevoltage = 230
manufacturer = PowerCom
modelname = Unknown
serialnumber = Unknown
type = Trust</pre>
</dl>
<p> The rest of the default values for the extra arguments are type-dependent. However, <i>BNT-other</i> is a special type that can be used to override ALL values for ALL models.</p>
<h3>Trust</h3>
<dl>
<dd>
<pre>numOfBytesFromUPS = 11
methodOfFlowControl = dtr0rts1
validationSequence = &#123;&#123;5,0},{7,0},{8,0}}
shutdownArguments = &#123;&#123;0,10},n}
frequency = {0.00020997,0.00020928}
loadPercentage = {6.1343,-0.3808,4.3110,0.1811}
batteryPercentage = {5.0000,0.3268,-825.00,4.5639,-835.82}
voltage = {1.9216,-0.0977,0.9545,0.0000}</pre>
</dl>
<h3>Kp625Ap</h3>
<dl>
<dd>
<pre>numOfBytesFromUPS = 16
methodOfFlowControl = dtr0rts1
validationSequence = &#123;&#123;5,0x80},{7,0},{8,0}}
shutdownArguments = &#123;&#123;0,10},n}
frequency = {0.00020997,0.00020928}
loadPercentage = {6.1343,-0.3808,4.3110,0.1811}
batteryPercentage = {5.0000,0.3268,-825.00,4.5639,-835.82}
voltage = {1.9216,-0.0977,0.9545,0.0000}</pre>
</dl>
<h3>Egys</h3>
<dl>
<dd>
<pre>numOfBytesFromUPS = 16
methodOfFlowControl = no_flow_control
validationSequence = &#123;&#123;5,0x80},{7,0},{8,0}}
shutdownArguments = &#123;&#123;0,10},n}
frequency = {0.00020997,0.00020928}
loadPercentage = {6.1343,-0.3808,1.3333,0.6667}
batteryPercentage = {5.0000,0.3268,-825.00,2.2105,-355.37}
voltage = {1.9216,-0.0977,0.9545,0.0000}</pre>
</dl>
<h3>Imp</h3>
<dl>
<dd>
<pre>numOfBytesFromUPS = 16
methodOfFlowControl = no_flow_control
validationSequence = &#123;&#123;5,0xFF},{7,0},{8,0}}
shutdownArguments = &#123;&#123;1,30},y}</pre>
</dl>
<h3>Kin</h3>
<dl>
<dd>
<pre>numOfBytesFromUPS = 16
methodOfFlowControl = no_flow_control
validationSequence = &#123;&#123;11,0x4b},{8,0},{8,0}}
shutdownArguments = &#123;&#123;1,30},y}</pre>
</dl>
<h3>Bnt</h3>
<dl>
<dd>
<pre>numOfBytesFromUPS = 16
methodOfFlowControl = no_flow_control
validationSequence = &#123;&#123;11,0x42},{8,0},{8,0}}
shutdownArguments = &#123;&#123;1,30},y}</pre>
</dl>
<h3>BNT-other</h3>
<dl>
<dd>
<pre>numOfBytesFromUPS = 16
methodOfFlowControl = no_flow_control
validationSequence = &#123;&#123;8,0},{8,0},{8,0}}
shutdownArguments = &#123;&#123;1,30},y}
frequency = {0.00027778,0.0000}
loadPercentage = {1.0000,0.0,1.0000,0.0}
batteryPercentage = {1.0000,0.0000,0.0000,1.0000,0.0000}
voltage = {2.0000,0.0000,2.0000,0.0000}</pre>
</dl>
<h3>Opti</h3>
<dl>
<dd>
<pre>numOfBytesFromUPS = 16
methodOfFlowControl = no_flow_control
validationSequence = &#123;&#123;5,0xFF},{7,0},{8,0}}
shutdownArguments = &#123;&#123;1,30},y}</pre>
</dl>
<h2>Author</h2>
<p>Peter Bieringer &lt;pb [at] bieringer.de&gt;, Alexey Sidorov &lt;alexsid [at] altlinux.org&gt;, Keven L. Ates &lt;atescomp [at] gmail.com&gt;</p>
<h2>See Also</h2>
<h3>The core driver:</h3>
<p><code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8)</p>
<h3>Internet resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>
