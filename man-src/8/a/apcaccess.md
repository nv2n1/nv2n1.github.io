---
title: "apcaccess(8)"
name: "apcaccess"
section: "8"
letter: "a"
url: "/docs/linux/man/8-apcaccess/"
description: "apcaccess – retrieve status information from"
---

<p><code>apcaccess</code> &#8211; retrieve status information from </p>
<p><a href="/docs/linux/man/8-apcupsd/">apcupsd</a>(8)</p>
<h2>Synopsis</h2>
<p>[-f &lt;config-file&gt;] [-h &lt;host&gt;[:&lt;port&gt;]] [-p &lt;parameter-name&gt;] [-u] [&lt;command&gt;] [&lt;host&gt;[:&lt;port&gt;]]</p>
<h2>Description</h2>
<p>is a program which prints out the complete status of most American Power Conversion Corp. (APC) UPSes provided you have the <a href="/docs/linux/man/8-apcupsd/">apcupsd</a>(8) daemon installed, properly configured and running. It can access status information from any APC UPS attached to the localhost or attached to any computer on the network which is running apcuspd in NIS mode. The command line options are:</p>
<dl>
<dt><code>-f</code></dt>
<dd>configuration file of apcupsd (default is usually /etc/apcupsd/apcupsd.conf)</dd>
<dt><code>-h </code></dt>
<dd>hostname and port of apcupsd to communicate with. The default hostname and port are obtained from the configuration file.</dd>
<dt><code>-p</code></dt>
<dd>Report only the value of the named parameter instead of all parameters and values.</dd>
<dt><code>-u</code></dt>
<dd>Remove units field for easier parsing by scripts.</dd>
<dt><code>&lt;command&gt;</code></dt>
<dd>An optional command, unless a hostname is also being specified. The only implemented command is <i>status</i> Shorthand for <i>status localhost:3551</i> This produces a full printout of the available status information for the associated UPS.</dd>
<dt><code>&lt;host&gt;</code></dt>
<dd>An optional hostname which may be a bare machine name, fully qualified domain name or IP address.</dd>
<dt><code>:&lt;port&gt;</code></dt>
<dd>An optional port number where a hostname argument has been specified. The default is 3551, the official port number assigned by <code>IANA </code> for the apcupsd NIS server. The default hostname and port are obtained from the configuration file.</dd></dl>
<p> uses apcupsd&#8217;s inbuilt Network Information Server (NIS) &#8212; no relation to Sun&#8217;s NIS/YP service &#8212; to obtain the current status information from the UPS on the local or remote computer. It is therefore necessary to have the following configuration directives: </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>NETSERVER on</code></dt>
<dd>
</dd><dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>NISPORT 3551</code></dt>
<dd></dd></dl>
<p> in the /etc/apcupsd/apcupsd.conf configuration file so that the Network Information Server will be accessible. Firewall rules for appropriate network access may also be needed.</p>
<h2>Status Report Format</h2>
<p>The status report output format is simple ASCII. Generally there is a single piece of information on each line of output. The content varies based on the model of UPS being used and, in some cases, the firmware version.</p>
<h2>Examples</h2>
<p>Set out below is a sample of the status output which may be generated for the specified UPS models.</p>
<h3>All models</h3>
<dl>
<dt><code>APC</code></dt>
<dd>: version, number of records and number of bytes following</dd>
<dt><code>DATE</code></dt>
<dd>: Date and time of last update from UPS</dd>
<dt><code>HOSTNAME</code></dt>
<dd>: hostname of computer running apcupsd</dd>
<dt><code>VERSION</code></dt>
<dd>: apcupsd version number, date and operating system</dd>
<dt><code>UPSNAME</code></dt>
<dd>: UPS name from configuration file (dumb) or EEPROM (smart)</dd>
<dt><code>CABLE</code></dt>
<dd>: Cable type specified in the configuration file</dd>
<dt><code>MODEL</code></dt>
<dd>: UPS model derived from UPS information</dd>
<dt><code>UPSMODE</code></dt>
<dd>: Mode in which UPS is operating</dd>
<dt><code>STARTTIME</code></dt>
<dd>: Date and time apcupsd was started</dd>
<dt><code>STATUS</code></dt>
<dd>: UPS status. One or more of the following (space-separated): CAL TRIM BOOST ONLINE ONBATT OVERLOAD LOWBATT REPLACEBATT NOBATT SLAVE SLAVEDOWN<br />
 or<br />
 COMMLOST<br />
 or<br />
 SHUTTING DOWN</dd>
<dt><code>MASTERUPD</code></dt>
<dd>: Last time the master sent an update to the slave</dd>
<dt><code>ENDAPC</code></dt>
<dd>: Date and time of status information was written</dd></dl>
<h3>Smart-UPS and Matrix-UPS (Smart Signalling)</h3>
<dl>
<dt><code>LINEV</code></dt>
<dd>: Current input line voltage</dd>
<dt><code>LOADPCT</code></dt>
<dd>: Percentage of UPS load capacity used as estimated by UPS</dd>
<dt><code>BCHARGE</code></dt>
<dd>: Current battery capacity charge percentage</dd>
<dt><code>TIMELEFT</code></dt>
<dd>: Remaining runtime left on battery as estimated by the UPS</dd>
<dt><code>MBATTCHG</code></dt>
<dd>: Min battery charge % (BCHARGE) required for system shutdown</dd>
<dt><code>MINTIMEL</code></dt>
<dd>: Min battery runtime (MINUTES) required for system shutdown</dd>
<dt><code>MAXTIME</code></dt>
<dd>: Max battery runtime (TIMEOUT) after which system is shutdown</dd>
<dt><code>MAXLINEV</code></dt>
<dd>: Maximum input line voltage since apcupsd started</dd>
<dt><code>MINLINEV</code></dt>
<dd>: Min (observed) input line voltage since apcupsd started</dd>
<dt><code>OUTPUTV</code></dt>
<dd>: Current UPS output voltage</dd>
<dt><code>SENSE</code></dt>
<dd>: Current UPS sensitivity setting for voltage fluctuations</dd>
<dt><code>DWAKE</code></dt>
<dd>: Time UPS waits after power off when the power is restored</dd>
<dt><code>DSHUTD</code></dt>
<dd>: Delay before UPS powers down after command received</dd>
<dt><code>DLOWBATT</code></dt>
<dd>: Low battery signal sent when this much runtime remains</dd>
<dt><code>LOTRANS</code></dt>
<dd>: Input line voltage below which UPS will switch to battery</dd>
<dt><code>HITRANS</code></dt>
<dd>: Input line voltage above which UPS will switch to battery</dd>
<dt><code>RETPCT</code></dt>
<dd>: Battery charge % required after power off to restore power</dd>
<dt><code>ITEMP</code></dt>
<dd>: UPS internal temperature in degrees Celcius</dd>
<dt><code>ALARMDEL</code></dt>
<dd>: Delay period before UPS starts sounding alarm</dd>
<dt><code>BATTV</code></dt>
<dd>: Current battery voltage</dd>
<dt><code>LINEFREQ</code></dt>
<dd>: Current line frequency in Hertz</dd>
<dt><code>LASTXFER</code></dt>
<dd>: Reason for last transfer to battery since apcupsd startup</dd>
<dt><code>NUMXFERS</code></dt>
<dd>: Number of transfers to battery since apcupsd startup</dd>
<dt><code>XONBATT</code></dt>
<dd>: Date, time of last transfer to battery since apcupsd startup</dd>
<dt><code>TONBATT</code></dt>
<dd>: Seconds currently on battery</dd>
<dt><code>CUMONBATT</code></dt>
<dd>: Cumulative seconds on battery since apcupsd startup</dd>
<dt><code>XOFFBAT</code></dt>
<dd>: Date, time of last transfer off battery since apcupsd startup</dd>
<dt><code>SELFTEST</code></dt>
<dd>: Date and time of last self test since apcupsd startup</dd>
<dt><code>STESTI</code></dt>
<dd>: Self-test interval</dd>
<dt><code>STATFLAG</code></dt>
<dd>: UPS status flag in hex</dd>
<dt><code>DIPSW</code></dt>
<dd>: Current UPS DIP switch settings</dd>
<dt><code>REG1</code></dt>
<dd>: Fault register 1 in hex</dd>
<dt><code>REG2</code></dt>
<dd>: Fault register 2 in hex</dd>
<dt><code>REG3</code></dt>
<dd>: Fault register 3 in hex</dd>
<dt><code>MANDATE</code></dt>
<dd>: UPS date of manufacture</dd>
<dt><code>SERIALNO</code></dt>
<dd>: UPS serial number</dd>
<dt><code>BATTDATE</code></dt>
<dd>: Date battery last replaced (if set)</dd>
<dt><code>NOMOUTV</code></dt>
<dd>: Nominal output voltage to supply when on battery power</dd>
<dt><code>NOMBATTV</code></dt>
<dd>: Nominal battery voltage</dd>
<dt><code>EXTBATTS</code></dt>
<dd>: Number of external batteries (for XL models)</dd>
<dt><code>BADBATTS</code></dt>
<dd>: Number of bad external battery packs (for XL models)</dd>
<dt><code>FIRMWARE</code></dt>
<dd>: UPS firmware version</dd>
<dt><code>APCMODEL</code></dt>
<dd>: APC model information</dd></dl>
<h3>Newer Back-UPS Pro (Smart Signalling)</h3>
<dl>
<dt><code>LINEV</code></dt>
<dd>: Current input line voltage</dd>
<dt><code>LOADPCT</code></dt>
<dd>: Percentage of UPS load capacity used</dd>
<dt><code>MBATTCHG</code></dt>
<dd>: Min battery charge % (BCHARGE) required for system shutdown</dd>
<dt><code>MINTIMEL</code></dt>
<dd>: Min battery runtime (MINUTES) required for system shutdown</dd>
<dt><code>MAXTIME</code></dt>
<dd>: Max battery runtime (TIMEOUT) after which system is shutdown</dd>
<dt><code>MAXLINEV</code></dt>
<dd>: Maximum input line voltage since apcupsd startup</dd>
<dt><code>MINLINEV</code></dt>
<dd>: Minimum input line voltage since apcupsd startup</dd>
<dt><code>OUTPUTV</code></dt>
<dd>: Current UPS output voltage</dd>
<dt><code>BATTV</code></dt>
<dd>: Current battery charge voltage</dd>
<dt><code>STATFLAG</code></dt>
<dd>: UPS status flag in hex</dd></dl>
<h3>Back-UPS RS 1500 (USB)</h3>
<dl>
<dt><code>LINEV</code></dt>
<dd>: Current input line voltage</dd>
<dt><code>LOADPCT</code></dt>
<dd>: Percentage of UPS load capacity used</dd>
<dt><code>BCHARGE</code></dt>
<dd>: Current battery capacity charge percentage</dd>
<dt><code>TIMELEFT</code></dt>
<dd>: Remaining runtime left on battery as estimated by UPS</dd>
<dt><code>MBATTCHG</code></dt>
<dd>: Min battery charge % (BCHARGE) required for system shutdown</dd>
<dt><code>MINTIMEL</code></dt>
<dd>: Min battery runtime (MINUTES) required for system shutdown</dd>
<dt><code>MAXTIME</code></dt>
<dd>: Max battery runtime (TIMEOUT) after which system is shutdown</dd>
<dt><code>*OUTPUTV</code></dt>
<dd>: Current UPS output voltage</dd>
<dt><code>*DWAKE</code></dt>
<dd>: Time UPS waits after power off when the power is restored</dd>
<dt><code>*DSHUTD</code></dt>
<dd>: Delay before UPS powers down after command received</dd>
<dt><code>LOTRANS</code></dt>
<dd>: Input line voltage below which UPS will switch to battery</dd>
<dt><code>HITRANS</code></dt>
<dd>: Input line voltage above which UPS will switch to battery</dd>
<dt><code>*RETPCT</code></dt>
<dd>: Battery charge % required after power off to restore power</dd>
<dt><code>*ITEMP</code></dt>
<dd>: UPS internal temperature in degrees Celcius</dd>
<dt><code>ALARMDEL</code></dt>
<dd>: Delay period before UPS starts sounding alarm</dd>
<dt><code>BATTV</code></dt>
<dd>: Current battery voltage</dd>
<dt><code>*LINEFREQ</code></dt>
<dd>: Current line frequency in Hertz</dd>
<dt><code>*LASTXFER</code></dt>
<dd>: Reason for last transfer to battery since apcupsd startup</dd>
<dt><code>NUMXFERS</code></dt>
<dd>: Number of transfers to battery since apcupsd startup</dd>
<dt><code>XONBATT</code></dt>
<dd>: Date, time of last transfer to battery since apcupsd startup</dd>
<dt><code>TONBATT</code></dt>
<dd>: Seconds currently on battery</dd>
<dt><code>CUMONBATT</code></dt>
<dd>: Cumulative seconds on battery since apcupsd startup</dd>
<dt><code>XOFFBAT</code></dt>
<dd>: Date, time of last transfer off battery since apcupsd startup</dd>
<dt><code>SELFTEST</code></dt>
<dd>: Date and time of last self test since apcupsd startup</dd>
<dt><code>STATFLAG</code></dt>
<dd>: UPS status flag in hex</dd>
<dt><code>MANDATE</code></dt>
<dd>: UPS date of manufacture</dd>
<dt><code>SERIALNO</code></dt>
<dd>: UPS serial number</dd>
<dt><code>BATTDATE</code></dt>
<dd>: Date battery last replaced (if set)</dd>
<dt><code>NOMBATTV</code></dt>
<dd>: Nominal battery voltage</dd>
<dt><code>FIRMWARE</code></dt>
<dd>: UPS firmware version</dd>
<dt><code>APCMODEL</code></dt>
<dd>: APC model information</dd>
<dt><code>* presence dependant on USB firmware version.</code></dt>
<dd></dd></dl>
<h3>Web/SNMP (AP9716) or PowerNet SNMP (AP9605) SmartSlot Card</h3>
<dl>
<dt><code>LINEV</code></dt>
<dd>: Current input line voltage</dd>
<dt><code>LOADPCT</code></dt>
<dd>: Percentage of UPS load capacity used as estimated by UPS</dd>
<dt><code>BCHARGE</code></dt>
<dd>: Current battery capacity charge percentage</dd>
<dt><code>TIMELEFT</code></dt>
<dd>: Remaining runtime left on battery as estimated by UPS</dd>
<dt><code>MBATTCHG</code></dt>
<dd>: Min battery charge % (BCHARGE) required for system shutdown</dd>
<dt><code>MINTIMEL</code></dt>
<dd>: Min battery runtime (MINUTES) required for system shutdown</dd>
<dt><code>MAXTIME</code></dt>
<dd>: Max battery runtime (TIMEOUT) after which system is shutdown</dd>
<dt><code>MAXLINEV</code></dt>
<dd>: Maximum input line voltage since apcupsd startup</dd>
<dt><code>MINLINEV</code></dt>
<dd>: Minimum input line voltage since apcupsd startup</dd>
<dt><code>OUTPUTV</code></dt>
<dd>: UPS output voltage</dd>
<dt><code>SENSE</code></dt>
<dd>: Current UPS sensitivity setting for voltage fluctuations</dd>
<dt><code>DWAKE</code></dt>
<dd>: Time UPS waits after power off when the power is restored</dd>
<dt><code>DSHUTD</code></dt>
<dd>: Delay before UPS powers down after command received</dd>
<dt><code>DLOWBATT</code></dt>
<dd>: Low battery signal sent when this much runtime remains</dd>
<dt><code>LOTRANS</code></dt>
<dd>: Input line voltage below which UPS will switch to battery</dd>
<dt><code>HITRANS</code></dt>
<dd>: Input line voltage above which UPS will switch to battery</dd>
<dt><code>RETPCT</code></dt>
<dd>: Battery charge % required after power off to restore power</dd>
<dt><code>ITEMP</code></dt>
<dd>: UPS internal temperature in degrees Celcius</dd>
<dt><code>ALARMDEL</code></dt>
<dd>: Delay period before UPS starts sounding alarm</dd>
<dt><code>LINEFREQ</code></dt>
<dd>: Current line frequency in Hertz</dd>
<dt><code>NUMXFERS</code></dt>
<dd>: Number of transfers to battery since apcupsd startup</dd>
<dt><code>TONBATT</code></dt>
<dd>: Seconds currently on battery</dd>
<dt><code>CUMONBATT</code></dt>
<dd>: Cumulative seconds on battery since apcupsd startup</dd>
<dt><code>XOFFBATT</code></dt>
<dd>: Date, time of last transfer off battery since apcupsd startup</dd>
<dt><code>STESTI</code></dt>
<dd>: Self-test interval</dd>
<dt><code>STATFLAG</code></dt>
<dd>: UPS status flag in hex</dd>
<dt><code>DIPSW</code></dt>
<dd>: Current UPS DIP switch settings</dd>
<dt><code>MANDATE</code></dt>
<dd>: UPS date of manufacture</dd>
<dt><code>SERIALNO</code></dt>
<dd>: UPS serial number</dd>
<dt><code>BATTDATE</code></dt>
<dd>: Date battery last replaced (if set)</dd>
<dt><code>NOMOUTV</code></dt>
<dd>: Nominal output voltage to supply when on battery power</dd>
<dt><code>NOMPOWER</code></dt>
<dd>: Nominal power output in watts</dd>
<dt><code>EXTBATTS</code></dt>
<dd>: Number of external batteries (for XL models)</dd>
<dt><code>BADBATTS</code></dt>
<dd>: Number of bad external battery packs (for XL models)</dd>
<dt><code>FIRMWARE</code></dt>
<dd>: UPS firmware version</dd>
<dt><code>APCMODEL</code></dt>
<dd>: APC model information</dd></dl>
<h3>Share-UPS (AP9270) (Basic port)</h3>
<dl>
<dt><code>MBATTCHG</code></dt>
<dd>: Min battery charge % (BCHARGE) required for system shutdown</dd>
<dt><code>MINTIMEL</code></dt>
<dd>: Min battery runtime (MINUTES) required for system shutdown</dd>
<dt><code>MAXTIME</code></dt>
<dd>: Max battery runtime (TIMEOUT) after which system is shutdown</dd>
<dt><code>NUMXFERS</code></dt>
<dd>: Number of transfers to battery since apcupsd startup</dd>
<dt><code>TONBATT</code></dt>
<dd>: Seconds currently on battery</dd>
<dt><code>CUMONBATT</code></dt>
<dd>: Cumulative seconds on battery since apcupsd startup</dd>
<dt><code>XOFFBATT</code></dt>
<dd>: Date, time of last transfer off battery since apcupsd startup</dd>
<dt><code>STATFLAG</code></dt>
<dd>: UPS status flag in hex</dd></dl>
<h3>UPS Environmental Monitoring SmartSlot Card (AP9612TH)</h3>
<dl>
<dt><code>HUMIDITY</code></dt>
<dd>: Ambient humidity</dd>
<dt><code>AMBTEMP</code></dt>
<dd>: Ambient temperature</dd></dl>
<h3>Back-UPS Pro and Smart-UPS v/s (Smart Signalling)</h3>
<dl>
<dt><code>LINEFAIL</code></dt>
<dd>: Input line voltage status.</dd>
<dt><code>BATTSTAT</code></dt>
<dd>: Battery status.</dd>
<dt><code>LASTXFER</code></dt>
<dd>: Last (observed) transfer to battery.</dd></dl>
<h3>Back-UPS and Net-UPS (Simple Signalling)</h3>
<dl>
<dt><code>LINEFAIL</code></dt>
<dd>: Input line voltage status.</dd>
<dt><code>BATTSTAT</code></dt>
<dd>: Battery status.</dd>
<dt><code>STATFLAG</code></dt>
<dd>: UPS status flag in hex.</dd></dl>
<h2>Files</h2>
<p>/etc/apcupsd/apcupsd.conf</p>
<h2>See Also</h2>
<p>apcupsd.conf5, <a href="/docs/linux/man/8-apcupsd/">apcupsd</a>(8). </p>
<p> The HTML apcupsd manual installed on your system or available online at <a rel="nofollow" href="http://www.apcupsd.org/">http://www.apcupsd.org/</a></p>
<h2>Authors</h2>
<h3>This page</h3>
<p>An Trevor Roydhouse</p>
<h3>Software</h3>
<p>An Adam Kropelin (current Project Manager and Code Maintainer) An Kern Sibbald (former Project Manager and Code Maintainer) An Riccardo Facchetti (former Project Manager and Code Maintainer) An Andre M. Hedrick (Project Founder and former Code Maintainer)</p>
<h3>Contributors</h3>
<p>An enormous number of users who have devoted their time and energy to this project &#8212; thanks.</p>
