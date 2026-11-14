---
title: "srcpd-conf(5)"
name: "srcpd-conf"
section: "5"
letter: "s"
url: "/docs/linux/man/5-srcpd-conf/"
description: "srcpd.conf – The configuration file for the srcpd deamon"
---

<p>srcpd.conf &#8211; The configuration file for the srcpd deamon</p>
<h2>Description</h2>
<p>The file <i>/etc/srcpd.conf</i> is used by the <code> srcpd (8)</code>. This file contains the runtime configuration for the deamon and it&#8217;s connection(s) to model railroad system. See <code>srcpd&nbsp;<wbr>(8)</code> for instruction how to use the daemon. </p>
<h2>Default Configuration File</h2>
<p>The default file is shipped as with the srcpd and contains both default settings and an example bus configuration. </p>
<dl>
<dd>
<pre>&lt;?xml version=&quot;1.0&quot;?&gt;
&lt;srcpd version=&quot;2.0&quot;&gt;
 &lt;bus&gt;
 &lt;server&gt;
 &lt;tcp-port&gt;4303&lt;/tcp-port&gt;
 &lt;pid-file&gt;/var/run/srcpd.pid&lt;/pid-file&gt;
 &lt;username&gt;nobody&lt;/username&gt;
 &lt;groupname&gt;nogroup&lt;/groupname&gt;
 &lt;/server&gt;
 &lt;verbosity&gt;5&lt;/verbosity&gt;
 &lt;/bus&gt;
 &lt;bus&gt;
 &lt;loopback&gt;
 &lt;number_fb&gt;3&lt;/number_fb&gt;
 &lt;/loopback&gt;
 &lt;use_watchdog&gt;no&lt;/use_watchdog&gt;
 &lt;verbosity&gt;5&lt;/verbosity&gt;
 &lt;auto_power_on&gt;yes&lt;/auto_power_on&gt;
 &lt;/bus&gt;
&lt;/srcpd&gt;</pre>
</dl>
<h2>File Format</h2>
<p>The configuration file for srcpd is stored in XML format. As XML files are plain text, experienced users can manipulate such files with the help of a text editor. Less experienced users should select an external configuration tool to ensure a syntactically correct format. </p>
<p> If there are errors during configuration file reading the daemon will send appropriate notifications to the syslog daemon. These messages can be watched using with the syslog facility user.info. This facility is usually sent to the file <i>/var/log/messages</i> (or <i>/var/log/syslog</i>). On some systems the <i>/etc/syslog.conf</i> may need to be edited to access the user.info facility: </p>
<pre> user.info /var/adm/user-info.log</pre>
<p>Currently there is no document type definition (DTD) available, to validate the format of a user created configuration file. </p>
<p> Each configuration file must provide the following base structure: </p>
<pre> &lt;?xml version=&quot;1.0&quot;?&gt;
 &lt;srcpd&gt;
 ...
 &lt;/srcpd&gt;</pre>
<p>Within this structure (&#8230;) the necessary buses are configured, each using a separate substructure: </p>
<pre> &lt;bus&gt;
 ...
 &lt;/bus&gt;
 &lt;bus&gt;
 ...
 &lt;/bus&gt;</pre>
<h3>General hints</h3>
<p>The first configured bus should always be the server-bus. Sequence and number of the following buses are any desired. Numbering of each single bus is done according to the sequence in this configuration file. The server bus itself gets number 0, all following buses are numbered continuously starting with 1 up to a maximum limit of 20. </p>
<p> Only buses that are actually used with the daemon should be filed. Not used buses can be commented out: </p>
<pre> &lt;!--
 &lt;bus&gt;
 ...
 &lt;/bus&gt;
 --&gt;</pre>
<p>Please bear in mind the numbering of the following buses will be changed accordingly.</p>
<h3>Universal options</h3>
<p>The following options are usable for all used bus sections. Universal options must be specified after bus specific options.</p>
<dl>
<dt>verbosity</p>
<dd>Depending on this number (valid range: 0..5) the bus will tell you less or more about what is happening. The 0 value gives a minimum output. This option is mainly used for debugging reasons. You can watch these messages using the syslog daemon file <i>/var/log/messages</i> (or <i>/var/log/messages</i>); see <i><a href="/docs/linux/man/8-srcpd/">srcpd</a></i>(8) for more information. The default value is <i>4</i>.</p>
<dt>use_watchdog</p>
<dd>Some buses provide a watchdog feature to cancel a blocked bus thread. Valid input values are <i>yes</i> or <i>no</i>. The default value is <i>no</i>.</p>
<dt>restore_device_settings</p>
<dd>Some buses provide a feature to restore serial device settings. Valid input values are <code>yes</code> or <code>no</code>. The default value is <i>no</i>.</p>
<dt>device</p>
<dd>This is the name of the connected device (like /dev/ttyS0). If bus is <code>server</code> or <code>loopback</code> no assignment is necessary. The default value is <i>/dev/null</i>.</p>
<dt>auto_power_on</p>
<dd>This option enables/disables automatical power on for a bus on server daemon start. This option is not necessary for <code>server</code> and <code>loopback</code> buses. The default value is <i>no</i>.</p>
<dt>speed</p>
<dd>Buses using serial devices with a not fixed transfer speed allow to adjust this parameter. Possible values are 2400, 4800, 9600, 19200, 38400, 57600 and 115200 baud. For buses with variable interface speed the default value is <i>2400</i>.</dl>
<h3>server</h3>
<p>This bus is needed every time. The following options can be used for individual setup.</p>
<dl>
<dt>tcp-port</p>
<dd>This is the TCP/IP port for communication between <i>srcpd</i> and his clients. Default is <i>4303</i> (this port number is assigned to SRCP by IANA).</p>
<dt>pid-file</p>
<dd>File, where srcpd is storing it&#8217;s process-id. According to FHS the default is <i>/var/run/srcpd.pid</i>.</p>
<dt>username</p>
<dd>srcpd runs under this user. Default is <i>nobody</i>.</p>
<dt>groupname</p>
<dd>srcpd runs under this group. Default is <i>nogroup</i>.</dl>
<h3>dccar</h3>
<p>This driver supports <i>DC-Car Infrared Remote Control</i>. This mode supports remote control of cars (e.g. Faller Car-System) with a DC-Car decoder or Infracar decoder. A sender must be connected to your PC&#8217;s seriall port. Some USB/Serial Adapter also work, e.g. Prolifi PL 2303 based adapter. </p>
<p> A description of the sender is available at <a rel="nofollow" href="http://www.dc-car.de/DC-Car_PC_Sender.htm">http://www.dc-car.de/DC-Car_PC_Sender.htm</a></p>
<dl>
<dt>mode</p>
<dd>This option specifies whether DC-Car or Infracar decoders are controled. Currently it is not possible to combine both modes. Possile values are dccar and infracar.</p>
<dt>number_gl</p>
<dd>This value specifies the address range of the used vehicles (GL). Up to 1024 DC-Cars or 4096 Infracars can be controlled. Default values are 1024 (dccar) and 4096 (infracar).</p>
<dt>pause_between_commands</p>
<dd>This value specifies the time between two commands The default value is 10 ms.</p>
<dt>Example</p>
<dd>
<pre>&lt;bus&gt;
 &lt;dccar&gt;
 &lt;mode&gt;dccar&lt;/mode&gt;
 &lt;number_gl&gt;1024&lt;/number_gl&gt;
 &lt;pause_between_commands&gt;10&lt;/pause_between_commands&gt;
 &lt;/dccar&gt;
 &lt;auto_power_on&gt;yes&lt;/auto_power_on&gt;
 &lt;verbosity&gt;4&lt;/verbosity&gt;
 &lt;device&gt;/dev/ttyUSB0&lt;/device&gt;
&lt;/bus&gt;</pre>
</dl>
<h3>ddl</h3>
<p>Digital Direct for Linux (DDL) via serial line (RS232). With this module the PC is enabled to generate a digital control voltage for Maerklin/Motorola (MM) and/or NMRA/DCC using the serial interface (RS232) hardware. Output lines TxD and GND are used by this feature and must be connected to booster inputs properly. </p>
<p> This module exposes optimal signal performance if special user rights for the <i>srcpd</i> are applied. It is recommended especially for Maerklin/Motorola users to configure a system user <i>srcpd</i> and a group <i>srcpd</i> with these command lines: </p>
<p>$&nbsp;<wbr>addgroup &#8211;system srcpd<br />
$&nbsp;<wbr>adduser &#8211;system &#8211;no-create-home &#8211;ingroup srcpd srcpd </p>
<p> In order to increase the realtime priority for this user the system file <i>/etc/security/limits.conf</i> must be edited to add following line: </p>
<p>&nbsp;<wbr>srcpd&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rtprio&nbsp;<wbr>&nbsp;<wbr>99 </p>
<p> According to these measures the configuration file must be adapted as follows: </p>
<p>&nbsp;<wbr>&lt;server&gt;<br />
&#8230;<br />
&lt;username&gt;srcpd&lt;/username&gt;<br />
&lt;groupname&gt;srcpd&lt;/groupname&gt;<br />
&#8230;<br />
&nbsp;<wbr>&lt;/server&gt; </p>
<dl>
<dt>number_ga</p>
<dd>Maximum usable decoder address number for generic accessory devices (GA). The default value is <i>324</i>. </p>
<p> please note that there is an offset of 4 between the DDL addresses and the addresses according to the documentation from maerklin. The equation ddl-address = maerklin docu address + 4 is used. This is due to some interpretation differences what the trits mean. Details can be found at <a rel="nofollow" href="http://vogt-it.com/OpenSource/DDL/Addrestable.html">http://vogt-it.com/OpenSource/DDL/Addrestable.html</a> </p>
<dt>number_gl</p>
<dd>Maximum usable decoder address number for generic locomotive devices (GL). The default value is <i>81</i>.</p>
<dt>enable_ringindicator_checking</p>
<dd>The ring indicator (RI) is a line of the serial interface RS232. This line can be used to switch off digital signal power, e.g. by pushing a connected emergency stop button. Signal power is switched off if RI line input voltage changes from -12V (-5V) to +12V (+5V). If this feature is used, the parameter must be set to <i>yes</i>, if not used, it must be set to <i>no</i>. The default value is <i>no</i>.</p>
<dt>enable_checkshort_checking</p>
<dd>The DSR line of the serial interface RS232 can be used to switch off digital power as response to shortcut detection. The connected booster must provide support for this kind of feature and must be wired to this line accordingly. If used the parameter must be set to <i>yes</i>, if not used, it must be set to <i>no</i>. The default value is <i>no</i>.</p>
<dt>inverse_dsr_handling</p>
<dd>Some boosters provide inverted output voltage for shortcut detection. If such a booster is used this parameter must be set to <i>yes</i>. The default value is <i>no</i>.</p>
<dt>enable_maerklin</p>
<dd>This parameter must be set to <i>yes</i>, if decoders for the old (not mfx) Maerklin/Motorola (MM) format are used. If not used, it should be set to <i>no</i>. The default value is <i>yes</i>.</p>
<dt>enable_nmradcc</p>
<dd>This parameter must be set to <i>yes</i>, if decoders for NMRA/DCC format are used. If not used, it should be set to <i>no</i>. The default value is <i>yes</i>.</dl>
<p> It is also possible to enable both digital protocol formats, to drive decoders of both digital systems attached to the same power line. In order to minimize CPU load, the not used protocol should always be disabled.</p>
<dl>
<dt>improve_nmradcc_timing</p>
<dd>The default baudrate of DDL is 19200 baud, which is slightly higher than allowed by NMRA DCC standard. With a UART 16550A you can change the baudrate to 16457 baud, which is within the specification. This is only needed if you have timing problems with the default. Valid input values are <code>yes</code> or <code>no</code>. The default value is <code>no</code>, which corresponds to 19200 baud.</p>
<dt>nmra_ga_offset</p>
<dd>This parameter is for backward compatibility to <i>erddcd</i> and alternate usage of different central units, due to the fact there are two ways to handle NMRA/DCC decoder addresses. This parameter allows to add an offset to all used address values. E.g., if all GA decoder addresses are shifted by 4 (i.e. you want to change switch 1, and you have to change switch 5 to do this), then this parameter should be set to <i>1</i>. Valid values are 0 and 1. Default value is <i>0</i>.</p>
<dt>shortcut_failure_delay</p>
<dd>Number of micro seconds <i>srcpd</i> waits to switch off digital power, after a shortcut is detected. The default value is <i>0</i>.</p>
<dt>nmradcc_translation_routine</p>
<dd>There are 3 implementations for converting the logical command bits into serial line commands, considering the start and stop bits of the serial line. Valid values are 1, 2 and 3. Default value is <i>3</i>.</p>
<dt>enable_usleep_patch</p>
<dd>Due to certain issues of the MM protocol its usage results in a significant amount of CPU load for <i>srcpd</i>, caused by busy waiting. This parameter gives the possibility to improve this situation by introducing a process wait state for a certain amount of time. Normally this does not result in any trouble controlling the attached decoders, so the parameter should be set to <i>yes</i>. Valid values are <i>yes</i> and <i>no</i>. The default value is <i>yes</i>.</p>
<dt>usleep_usec</p>
<dd>Number of micro seconds the signal generating process pauses. This value should be as small as possible; a bigger value can result in improper digital signal generation. There have been good results using values between 100 and 250 usecs. This parameter is only used, if <i>enable_usleep_patch</i> is set to <i>yes</i>. The default value is <i>100</i>.</p>
<dt>program_track</p>
<dd>This parameter allows you to suppress commands which are issued for a program track. This parameter should only be used on your main. Valid input values are <code>yes</code> or <code>no</code>. The default value is <code>yes</code>, i.e. all program track commands will be executed by default.</p>
<dt>Example Maerklin/Motorola</p>
<dd>
<pre>&lt;bus&gt;
 &lt;ddl&gt;
 &lt;number_ga&gt;200&lt;/number_ga&gt;
 &lt;number_gl&gt;81&lt;/number_gl&gt;
 &lt;enable_maerklin&gt;yes&lt;/enable_maerklin&gt;
 &lt;enable_nmradcc&gt;no&lt;/enable_nmradcc&gt;
 &lt;enable_usleep_patch&gt;yes&lt;/enable_usleep_patch&gt;
 &lt;usleep_usec&gt;200&lt;/usleep_usec&gt;
 &lt;/ddl&gt;
 &lt;auto_power_on&gt;no&lt;/auto_power_on&gt;
 &lt;verbosity&gt;4&lt;/verbosity&gt;
 &lt;device&gt;/dev/ttyS0&lt;/device&gt;
&lt;/bus&gt;</pre>
<dt>Example NMRA/DCC</p>
<dd>
<pre>&lt;bus&gt;
 &lt;ddl&gt;
 &lt;number_ga&gt;160&lt;/number_ga&gt;
 &lt;number_gl&gt;60&lt;/number_gl&gt;
 &lt;enable_maerklin&gt;no&lt;/enable_maerklin&gt;
 &lt;enable_nmradcc&gt;yes&lt;/enable_nmradcc&gt;
 &lt;nmradcc_translation_routine&gt;3&lt;/nmradcc_translation_routine&gt;
 &lt;/ddl&gt;
 &lt;auto_power_on&gt;no&lt;/auto_power_on&gt;
 &lt;verbosity&gt;4&lt;/verbosity&gt;
 &lt;device&gt;/dev/ttyS0&lt;/device&gt;
&lt;/bus&gt;</pre>
</dl>
<h3>ddl-s88</h3>
<p>Digital Direct for Linux S88 via parport (IEEE 1284). This bus provides up to four S88 data links attached to the parallel port to connect S88-feedback modules. Usage of one S88 line is possible by simply wiring modules to the parallel port connectors; for advanced applications involving more than one line the wiring scheme is equivalent to the one from the DDL daemon <i>erddcd</i> (<a rel="nofollow" href="http://www.vogt-it.com/OpenSource/DDL)">http://www.vogt-it.com/OpenSource/DDL)</a> as shown in the circuit of Martin Wolf. The four S88 data links are managed as separate buses. </p>
<p> The maximum count of modules (with 16 contacts) which can be connected to a data link is 31; so maximal 496 contacts are supported per link. When using modules with 8 contacts two modules count as one. </p>
<p> For each data link a separate bus is initialized where the sequence of the feedback contacts of the modules is increasing as the modules are connected to the data link. If there are no modules connected to a data link the respective value of <i>number_fb_x</i> must be set to <i>0</i>. Nevertheless this bus is initialized, that means also if only one bus is used, all four buses are initialized.</p>
<dl>
<dt>ioport</p>
<dd>Input/output address of the printer port. The default value is <i>0x0378</i>. The value for <i>ioport</i> must be given in hexadecimal format (starting with 0x). Valid values for a typical Linux system are 0x0378, 0x0278 and 0x03BC. The right value can easily be detected searching through the kernel start-up messages: </p>
<pre> dmesg | grep parport</pre>
<dt>clockscale</p>
<dd>Parameter to adjust the clock rate for reading the modules. In the case of the default value 35 the original S88 clock rate of approximately 8 KHz would be achieved. Smaller values increasing the clock rate but not each module can work with this. In maximum there is approximately 125 KHz possible.</p>
<dt>refresh</p>
<dd>Delay time in milliseconds after witch the feedback modules are read again. In case of the default value 100 the data is refreshed each 100 ms. </p>
<p> The higher this value the less often the attached modules are read and the less is the resulting system load. Useful values are between 100 and 250.</p>
<dt>fb_delay_time_0</p>
<dd>This value in milliseconds determines how long the signal on a feedback contact must be on zero level before it is accepted as valid and will be forwarded to all clients. With this parameter it is in a limited range possible to debounce bad feedback contacts (bouncing contacts). The default value is <i>0</i>.</p>
<dt>number_fb_1</p>
<dd>This statement defines the count of feedback modules connected to the data link number <i>1</i>.</p>
<dt>number_fb_2</p>
<dd>This statement defines the count of to data link number <i>2</i> connected feedback modules.</p>
<dt>number_fb_3</p>
<dd>This statement defines the count of to data link number <i>3</i> connected feedback modules.</p>
<dt>number_fb_4</p>
<dd>This statement defines the count of to the data link number <i>4</i> connected feedback modules.</dl>
<p> Inside of the configuration the common values should be arranged before the bus specific values.</p>
<dl>
<dt>Example</p>
<dd>
<pre>&lt;bus&gt;
 &lt;auto_power_on&gt;yes&lt;/auto_power_on&gt;
 &lt;verbosity&gt;5&lt;/verbosity&gt;
 &lt;ddl-s88&gt;
 &lt;ioport&gt;0x378&lt;/ioport&gt;
 &lt;number_fb_1&gt;9&lt;/number_fb_1&gt;
 &lt;number_fb_2&gt;0&lt;/number_fb_2&gt;
 &lt;number_fb_3&gt;0&lt;/number_fb_3&gt;
 &lt;number_fb_4&gt;0&lt;/number_fb_4&gt;
 &lt;/ddl-s88&gt;
&lt;/bus&gt;</pre>
</dl>
<h3>hsi-88</h3>
<p>This driver supports the HSI-88 device from Littfinski connected via serial line. An USB2Serial converter should work fine. The serial line speed setting is fixed to 9600 baud and cannot be changed. </p>
<p> The HSI-88 device provides three lines for feedback modules. To each line a maximum of 31 modules (each with 16 inputs) can be attached. If modules with 8 inputs are used, two modules count as one.</p>
<dl>
<dt>number_fb_left</p>
<dd>This value is the number of feedback-modules (with 16 inputs) connected to the line called <i>left</i>.</p>
<dt>number_fb_center</p>
<dd>This value is number of feedback-modules (with 16 inputs) connected to the line called <i>center</i>.</p>
<dt>number_fb_right</p>
<dd>This value is number of feedback-modules (with 16 inputs) connected to the line called <i>right</i>.</p>
<dt>fb_delay_time_0</p>
<dd>This is the time in milliseconds a feedback input must be zero, before zero is delivered to the attaches SRCP clients. With this feature it is possible to compensate bad feedback bounces in a certain range. The default value is <i>0</i>.</p>
<dt>refresh</p>
<dd>The time in microseconds (us) after srcpd will read feedback again from HSI-88. The default value is 10000 us. The lower this value the higher the resulting CPU load.</p>
<dt>Example</p>
<dd>
<pre>&lt;bus&gt;
 &lt;hsi-88&gt;
 &lt;number_fb_left&gt;8&lt;/number_fb_left&gt;
 &lt;number_fb_center&gt;5&lt;/number_fb_center&gt;
 &lt;number_fb_right&gt;0&lt;/number_fb_right&gt;
 &lt;refresh&gt;10000&lt;/refresh&gt;
 &lt;/hsi-88&gt;
 &lt;auto_power_on&gt;yes&lt;/auto_power_on&gt;
 &lt;verbosity&gt;4&lt;/verbosity&gt;
 &lt;device&gt;/dev/ttyS0&lt;/device&gt;
&lt;/bus&gt;</pre>
</dl>
<h3>i2c-dev</h3>
<p>Bus driver for i2c-dev interface of the Linux kernel, can be used to access hardware found on <a rel="nofollow" href="http://www.matronix.de/.">http://www.matronix.de/.</a></p>
<dl>
<dt>multiplex_buses</p>
<dd>TODO</p>
<dt>ga_hardware_inverters</p>
<dd>TODO</p>
<dt>ga_reset_device</p>
<dd>TODO</dl>
<h3>intellibox</h3>
<p>This driver supports the Intellibox device from Uhlenbrock (IB) connected via the serial port. Only extended mode commands are used (P50X binary protocol); this should be taken into account if protocol compatible devices (e.g. OpenDCC, DiCoStation, EasyControl) are used. Programming decoders is currently implemented for DCC only. Possible values for speed of serial port are depending from device and interface type 2400 baud, 4800 baud, 9600 baud, 19200 baud, 38400 bau and 57600 baud.</p>
<dl>
<dt>fb_delay_time_0</p>
<dd>This is the time in milliseconds a feedback input must be zero, before this value is delivered to clients. With this feature you can compensate bad feedback in a specific range. The default value is 0 ms.</p>
<dt>pause_between_commands</p>
<dd>This is the time in milliseconds between two commands the driver must wait. The exact value should be hand tuned. If the system does not respond or drops commands try to increase this value. Default is 250 ms.</p>
<dt>number_ga</p>
<dd>This is the maximal address number of Generic Accessory decoders (GA). Supported range is 0..1024. A value of 0 means no GA available. Default is 256.</p>
<dt>number_gl</p>
<dd>Like the number of GA this number limits the maximum address of the Generic Locomotive decoders (GL). Supported range is 0..10239. A value of 0 means no GL available. Default is 80.</p>
<dt>number_fb</p>
<dd>This is the number of S88 modules attached to the Intellibox device. The maximum valid number is 31. The default is 0 (no modules are attached). Please note that Loconet is currently not supported.</p>
<dt>auto_speed_detection</p>
<dd>This option activates an automatical baudrate detection of the connected Intellibox (BABI, Break and Automatic Baud-rate Identification). This procedure takes several seconds but if enabled it is not necessary to specify a value for the <i>speed</i> parameter. If disabled the connection initialization is much faster but the given <i>speed</i> value must comply to the actual Intellibox setting. Valid values are <i>yes</i> and <i>no</i>. The default value is <i>yes</i>.</p>
<dt>Example</p>
<dd>
<pre>&lt;bus&gt;
 &lt;intellibox&gt;
 &lt;number_ga&gt;250&lt;/number_ga&gt;
 &lt;number_gl&gt;100&lt;/number_gl&gt;
 &lt;number_fb&gt;4&lt;/number_fb&gt;
 &lt;fb_delay_time_0&gt;0&lt;/fb_delay_time_0&gt;
 &lt;pause_between_commands&gt;0&lt;/pause_between_commands&gt;
 &lt;/intellibox&gt;
 &lt;speed&gt;19200&lt;/speed&gt;
 &lt;auto_speed_detection&gt;no&lt;/auto_speed_detection&gt;
 &lt;auto_power_on&gt;no&lt;/auto_power_on&gt;
 &lt;verbosity&gt;4&lt;/verbosity&gt;
 &lt;device&gt;/dev/ttyUSB0&lt;/device&gt;
&lt;/bus&gt;</pre>
</dl>
<h3>li100, li100usb</h3>
<p>This driver connects with the LI100, LI100F, LI101F or LI-USB devices from Lenz connected via the serial port/USB-interface. An USB2Serial converter should not be used. The serial line settings are depending on type of interface. For LI-USB it&#8217;s fixed to 57600 baud with no chance to change. Autodetection of serial port interface speed is currently under construction. If connection fails, try restart of srcpd with an other speed. Possible values are 9600 baud, 19200 baud, 38400 baud, 57600 baud and 115200 baud, depending on your interface.</p>
<dl>
<dt>fb_delay_time_0</p>
<dd>This is the time in milliseconds an feedback input must be zero, before this value is delivered to clients. With this feature you can compensate bad feedback in a specific range. The default value is 0 ms.</p>
<dt>number_ga</p>
<dd>This is the number of GA. Supported range is 0..1024. A value of 0 means no GA available. Default is 99 (LI-USB 9999).</p>
<dt>number_gl</p>
<dd>Like the number of GA this number gives the maximum address. Supported range is 0..9999. A value of 0 means no GL available. Default is 99 (LI-USB 9999).</p>
<dt>number_fb</p>
<dd>This is the number of RS modules attached to the Lenz device. It can be as large as 512. It&#8217;s assumed, that one module has 8 inputs. A value of 0 means no FB available. Default is 256 (LI-USB 512).</dl>
<p> For Lenz USB interfaces It is very important to have the kernel module <i>ftdi_sio</i> available. Due to the Lenz concept, the interface unit returns different values after start.</p>
<dl>
<dt><code>0</code></p>
<dd>everything is OK</p>
<dt><code>-1</code></p>
<dd>Central Unit not found. Unable to read version of central unit.</p>
<dt><code>-2</code></p>
<dd>Central Unit not found. Unable to read version of central unit.</p>
<dt><code>-3</code></p>
<dd>Interface not found. Unable to read version of interface. This can also happen, if no central unit is connected to interface.</p>
<dt><code>-4</code></p>
<dd>device not found</dl>
<h3>loconet</h3>
<p>This bus provides a driver for the Loconet system by Digitrax. The device settings may be either serial connections (e.g. MS100, LocoBuffer) or TCP/IP network links (e.g. LbServer, <a rel="nofollow" href="http://loconetovertcp.sourceforge.net/">http://loconetovertcp.sourceforge.net/</a>).</p>
<dl>
<dt>sync-time-from-loconet</p>
<dd>Decode time messages from the loconet and set the SRCP TIME device. Valid values are <i>yes</i> or <i>no</i>. Default is <i>no</i>.</p>
<dt>loconet-id</p>
<dd>Default is 0x50.</p>
<dt>ms100</p>
<dd>Support for the MS100/RS232 device of Digitrax. Valid values are <i>yes</i> and <i>no</i>. Default is <i>no</i>.</p>
<dt>Example</p>
<dd>
<pre>&lt;bus&gt;
 &lt;loconet&gt;
 &lt;loconet-id&gt;80&lt;/loconet-id&gt;
 &lt;sync-time-from-loconet&gt;no&lt;/sync-time-from-loconet&gt;
 &lt;ms100&gt;no&lt;/ms100&gt;
 &lt;/loconet&gt;
 &lt;device type=&quot;network&quot; port=&quot;1234&quot;&gt;127.0.0.1&lt;/device&gt;
 &lt;!--
 &lt;device type=&quot;file&quot;&gt;/dev/ttyS0&lt;/device&gt;
 --&gt;
 
&lt;/bus&gt;</pre>
</dl>
<h3>loopback</h3>
<p>This bus does not connect to real hardware. It is used primarily for development tasks but may be useful for real installations too. Every command on this bus does only have an echo effect on the INFO sessions. This device may be used as virtual device for communication tasks.</p>
<dl>
<dt>number_ga</p>
<dd>This is the maximal address number of Generic Accessory (GA) devices. Default is 256.</p>
<dt>number_gl</p>
<dd>This number gives the maximum valid address number of the Generic Locomotive (GL) devices. Default is 80</p>
<dt>number_fb</p>
<dd>Different to other buses this parameter takes the number of feedback contacts, not modules. Simulation of two feedback modules, each providing 16 contacts, accordingly needs a parameter value of 32. Default is 0 (no contact).</p>
<dt>Example</p>
<dd>
<pre>&lt;bus&gt;
 &lt;loopback&gt;
 &lt;number_ga&gt;120&lt;/number_fb&gt;
 &lt;number_gl&gt;100&lt;/number_fb&gt;
 &lt;number_fb&gt;64&lt;/number_fb&gt;
 &lt;/loopback&gt;
 &lt;verbosity&gt;2&lt;/verbosity&gt;
 &lt;auto_power_on&gt;no&lt;/auto_power_on&gt;
&lt;/bus&gt;</pre>
</dl>
<h3>m605x</h3>
<p>This supports communication with the 6051 or 6050 devices from Maerklin connected via the serial port. An USB2Serial converter should work fine. The serial line settings are fixed to 2400 baud 8N2 and cannot be changed.</p>
<dl>
<dt>m6020mode</p>
<dd>In this mode the srcpd does not sent the 4 functions. This is a feature of the 6021 only. Valid values are <i>yes</i> and <i>no</i>. Default value is <i>no.</i></p>
<dt>fb_delay_time_0</p>
<dd>This is the time the driver code waits until it recognized the input change in milliseconds. This feature may support a debounce found in the hardware. The default value is 0 ms.</p>
<dt>ga_min_activetime</p>
<dd>The time in milliseconds a GA device needs to be in active state. The absolute minimum is 75 ms and is needed for stable communication with the 6051. The default value is 75 ms.</p>
<dt>pause_between_commands</p>
<dd>This is the time between two commands the drivers must wait. The exact values should be hand tuned. If the system does not respond or drops commands try to increase this value. Default is 200 ms.</p>
<dt>pause_between_bytes</p>
<dd>This is the time the driver waits between 2 bytes in multi-byte commands. The hardware handshake does not work with all devices so this parameter was introduced to support it. The default is 2 ms.</p>
<dt>number_ga</p>
<dd>This is the number of GA. This parameter does not have a real effect since the interface supports the addresses 1..256 only. Keep the default value 256 untouched.</p>
<dt>number_gl</p>
<dd>Like the number of GA this number gives the maximum GL address. Since this number is limited to 80, keep the default value 80 untouched.</p>
<dt>number_fb</p>
<dd>This is the number of 6088 modules attached to the 6051/6050 device. The valid range is from 0..31. The default value is 0 (no modules are attached). Please note that 6088 modules attached to other devices (memory) cannot be accessed.</p>
<dt>Example</p>
<dd>
<pre>&lt;bus&gt;
 &lt;m605x&gt;
 &lt;number_ga&gt;120&lt;/number_fb&gt;
 &lt;number_gl&gt;60&lt;/number_fb&gt;
 &lt;number_fb&gt;8&lt;/number_fb&gt;
 &lt;ga_min_activetime&gt;150&lt;/ga_min_activetime&gt;
 &lt;pause_between_bytes&gt;2&lt;/pause_between_bytes&gt;
 &lt;pause_between_commands&gt;50&lt;/pause_between_commands&gt;
 &lt;/m605x&gt;
 &lt;auto_power_on&gt;no&lt;/auto_power_on&gt;
 &lt;verbosity&gt;4&lt;/verbosity&gt;
 &lt;device&gt;/dev/ttyS0&lt;/device&gt;
&lt;/bus&gt;</pre>
</dl>
<h3>selectrix</h3>
<p>Selectrix CC-2000 and Rautenhaus SLX852.</p>
<dl>
<dt>number_ga</p>
<dd>TODO</p>
<dt>number_gl</p>
<dd>TODO</p>
<dt>number_fb</p>
<dd>TODO</p>
<dt>controller</p>
<dd>TODO</dl>
<h3>zimo</h3>
<p>This bus provides support for the old ASCII based Zimo MX1 interface protocol. The baud rate can not be changed and has an internal preset of 9600 Baud.</p>
<dl>
<dt>number_ga</p>
<dd>This value sets the maximum number for the GA address range. For protocol M (Maerklin/Motorola) the upper limit is 63, for protocol N (NMRA/DCC) the upper limit is 2044 (according to Lenz-DCC address scheme). The Z (Zimo) protocol is not supported yet. The default value is 256.</p>
<dt>number_gl</p>
<dd>This value sets the maximum number for the GL address range. The default value is 80.</p>
<dt>number_fb</p>
<dd>Not supported. The default value is 0.</p>
<dt>fb_delay_time_0</p>
<dd>Not supported. </p>
</dl>
<h2>Files</h2>
<p><i>/etc/srcpd.conf</i></p>
<h2>See Also</h2>
<p><code>srcpd&nbsp;<wbr>(8)</code> </p>
<h2>Authors</h2>
<p>This man page was written by Matthias Trute (mtrute [at] users.sourceforge.net), Frank Schimschke (schmischi [at] users.sourceforge.net) and Guido Scholz (gscholz [at] users.sourceforge.net).</p>
