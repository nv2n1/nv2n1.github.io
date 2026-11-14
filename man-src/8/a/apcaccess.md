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
<dt><code>-f</code></p>
<dd>configuration file of apcupsd (default is usually /etc/apcupsd/apcupsd.conf)</p>
<dt><code>-h </code></p>
<dd>hostname and port of apcupsd to communicate with. The default hostname and port are obtained from the configuration file.</p>
<dt><code>-p</code></p>
<dd>Report only the value of the named parameter instead of all parameters and values.</p>
<dt><code>-u</code></p>
<dd>Remove units field for easier parsing by scripts.</p>
<dt><code>&lt;command&gt;</code></p>
<dd>An optional command, unless a hostname is also being specified. The only implemented command is <i>status</i> Shorthand for <i>status localhost:3551</i> This produces a full printout of the available status information for the associated UPS.</p>
<dt><code>&lt;host&gt;</code></p>
<dd>An optional hostname which may be a bare machine name, fully qualified domain name or IP address.</p>
<dt><code>:&lt;port&gt;</code></p>
<dd>An optional port number where a hostname argument has been specified. The default is 3551, the official port number assigned by <code>IANA </code> for the apcupsd NIS server. The default hostname and port are obtained from the configuration file.</dl>
<p> uses apcupsd&#8217;s inbuilt Network Information Server (NIS) &#8212; no relation to Sun&#8217;s NIS/YP service &#8212; to obtain the current status information from the UPS on the local or remote computer. It is therefore necessary to have the following configuration directives: </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>NETSERVER on</code></p>
<dd>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>NISPORT 3551</code></p>
<dd></dl>
<p> in the /etc/apcupsd/apcupsd.conf configuration file so that the Network Information Server will be accessible. Firewall rules for appropriate network access may also be needed.</p>
<h2>Status Report Format</h2>
<p>The status report output format is simple ASCII. Generally there is a single piece of information on each line of output. The content varies based on the model of UPS being used and, in some cases, the firmware version.</p>
<h2>Examples</h2>
<p>Set out below is a sample of the status output which may be generated for the specified UPS models.</p>
<h3>All models</h3>
<dl>
<dt><code>APC</code></p>
<dd>: version, number of records and number of bytes following</p>
<dt><code>DATE</code></p>
<dd>: Date and time of last update from UPS</p>
<dt><code>HOSTNAME</code></p>
<dd>: hostname of computer running apcupsd</p>
<dt><code>VERSION</code></p>
<dd>: apcupsd version number, date and operating system</p>
<dt><code>UPSNAME</code></p>
<dd>: UPS name from configuration file (dumb) or EEPROM (smart)</p>
<dt><code>CABLE</code></p>
<dd>: Cable type specified in the configuration file</p>
<dt><code>MODEL</code></p>
<dd>: UPS model derived from UPS information</p>
<dt><code>UPSMODE</code></p>
<dd>: Mode in which UPS is operating</p>
<dt><code>STARTTIME</code></p>
<dd>: Date and time apcupsd was started</p>
<dt><code>STATUS</code></p>
<dd>: UPS status. One or more of the following (space-separated): CAL TRIM BOOST ONLINE ONBATT OVERLOAD LOWBATT REPLACEBATT NOBATT SLAVE SLAVEDOWN<br />
 or<br />
 COMMLOST<br />
 or<br />
 SHUTTING DOWN</p>
<dt><code>MASTERUPD</code></p>
<dd>: Last time the master sent an update to the slave</p>
<dt><code>ENDAPC</code></p>
<dd>: Date and time of status information was written</dl>
<h3>Smart-UPS and Matrix-UPS (Smart Signalling)</h3>
<dl>
<dt><code>LINEV</code></p>
<dd>: Current input line voltage</p>
<dt><code>LOADPCT</code></p>
<dd>: Percentage of UPS load capacity used as estimated by UPS</p>
<dt><code>BCHARGE</code></p>
<dd>: Current battery capacity charge percentage</p>
<dt><code>TIMELEFT</code></p>
<dd>: Remaining runtime left on battery as estimated by the UPS</p>
<dt><code>MBATTCHG</code></p>
<dd>: Min battery charge % (BCHARGE) required for system shutdown</p>
<dt><code>MINTIMEL</code></p>
<dd>: Min battery runtime (MINUTES) required for system shutdown</p>
<dt><code>MAXTIME</code></p>
<dd>: Max battery runtime (TIMEOUT) after which system is shutdown</p>
<dt><code>MAXLINEV</code></p>
<dd>: Maximum input line voltage since apcupsd started</p>
<dt><code>MINLINEV</code></p>
<dd>: Min (observed) input line voltage since apcupsd started</p>
<dt><code>OUTPUTV</code></p>
<dd>: Current UPS output voltage</p>
<dt><code>SENSE</code></p>
<dd>: Current UPS sensitivity setting for voltage fluctuations</p>
<dt><code>DWAKE</code></p>
<dd>: Time UPS waits after power off when the power is restored</p>
<dt><code>DSHUTD</code></p>
<dd>: Delay before UPS powers down after command received</p>
<dt><code>DLOWBATT</code></p>
<dd>: Low battery signal sent when this much runtime remains</p>
<dt><code>LOTRANS</code></p>
<dd>: Input line voltage below which UPS will switch to battery</p>
<dt><code>HITRANS</code></p>
<dd>: Input line voltage above which UPS will switch to battery</p>
<dt><code>RETPCT</code></p>
<dd>: Battery charge % required after power off to restore power</p>
<dt><code>ITEMP</code></p>
<dd>: UPS internal temperature in degrees Celcius</p>
<dt><code>ALARMDEL</code></p>
<dd>: Delay period before UPS starts sounding alarm</p>
<dt><code>BATTV</code></p>
<dd>: Current battery voltage</p>
<dt><code>LINEFREQ</code></p>
<dd>: Current line frequency in Hertz</p>
<dt><code>LASTXFER</code></p>
<dd>: Reason for last transfer to battery since apcupsd startup</p>
<dt><code>NUMXFERS</code></p>
<dd>: Number of transfers to battery since apcupsd startup</p>
<dt><code>XONBATT</code></p>
<dd>: Date, time of last transfer to battery since apcupsd startup</p>
<dt><code>TONBATT</code></p>
<dd>: Seconds currently on battery</p>
<dt><code>CUMONBATT</code></p>
<dd>: Cumulative seconds on battery since apcupsd startup</p>
<dt><code>XOFFBAT</code></p>
<dd>: Date, time of last transfer off battery since apcupsd startup</p>
<dt><code>SELFTEST</code></p>
<dd>: Date and time of last self test since apcupsd startup</p>
<dt><code>STESTI</code></p>
<dd>: Self-test interval</p>
<dt><code>STATFLAG</code></p>
<dd>: UPS status flag in hex</p>
<dt><code>DIPSW</code></p>
<dd>: Current UPS DIP switch settings</p>
<dt><code>REG1</code></p>
<dd>: Fault register 1 in hex</p>
<dt><code>REG2</code></p>
<dd>: Fault register 2 in hex</p>
<dt><code>REG3</code></p>
<dd>: Fault register 3 in hex</p>
<dt><code>MANDATE</code></p>
<dd>: UPS date of manufacture</p>
<dt><code>SERIALNO</code></p>
<dd>: UPS serial number</p>
<dt><code>BATTDATE</code></p>
<dd>: Date battery last replaced (if set)</p>
<dt><code>NOMOUTV</code></p>
<dd>: Nominal output voltage to supply when on battery power</p>
<dt><code>NOMBATTV</code></p>
<dd>: Nominal battery voltage</p>
<dt><code>EXTBATTS</code></p>
<dd>: Number of external batteries (for XL models)</p>
<dt><code>BADBATTS</code></p>
<dd>: Number of bad external battery packs (for XL models)</p>
<dt><code>FIRMWARE</code></p>
<dd>: UPS firmware version</p>
<dt><code>APCMODEL</code></p>
<dd>: APC model information</dl>
<h3>Newer Back-UPS Pro (Smart Signalling)</h3>
<dl>
<dt><code>LINEV</code></p>
<dd>: Current input line voltage</p>
<dt><code>LOADPCT</code></p>
<dd>: Percentage of UPS load capacity used</p>
<dt><code>MBATTCHG</code></p>
<dd>: Min battery charge % (BCHARGE) required for system shutdown</p>
<dt><code>MINTIMEL</code></p>
<dd>: Min battery runtime (MINUTES) required for system shutdown</p>
<dt><code>MAXTIME</code></p>
<dd>: Max battery runtime (TIMEOUT) after which system is shutdown</p>
<dt><code>MAXLINEV</code></p>
<dd>: Maximum input line voltage since apcupsd startup</p>
<dt><code>MINLINEV</code></p>
<dd>: Minimum input line voltage since apcupsd startup</p>
<dt><code>OUTPUTV</code></p>
<dd>: Current UPS output voltage</p>
<dt><code>BATTV</code></p>
<dd>: Current battery charge voltage</p>
<dt><code>STATFLAG</code></p>
<dd>: UPS status flag in hex</dl>
<h3>Back-UPS RS 1500 (USB)</h3>
<dl>
<dt><code>LINEV</code></p>
<dd>: Current input line voltage</p>
<dt><code>LOADPCT</code></p>
<dd>: Percentage of UPS load capacity used</p>
<dt><code>BCHARGE</code></p>
<dd>: Current battery capacity charge percentage</p>
<dt><code>TIMELEFT</code></p>
<dd>: Remaining runtime left on battery as estimated by UPS</p>
<dt><code>MBATTCHG</code></p>
<dd>: Min battery charge % (BCHARGE) required for system shutdown</p>
<dt><code>MINTIMEL</code></p>
<dd>: Min battery runtime (MINUTES) required for system shutdown</p>
<dt><code>MAXTIME</code></p>
<dd>: Max battery runtime (TIMEOUT) after which system is shutdown</p>
<dt><code>*OUTPUTV</code></p>
<dd>: Current UPS output voltage</p>
<dt><code>*DWAKE</code></p>
<dd>: Time UPS waits after power off when the power is restored</p>
<dt><code>*DSHUTD</code></p>
<dd>: Delay before UPS powers down after command received</p>
<dt><code>LOTRANS</code></p>
<dd>: Input line voltage below which UPS will switch to battery</p>
<dt><code>HITRANS</code></p>
<dd>: Input line voltage above which UPS will switch to battery</p>
<dt><code>*RETPCT</code></p>
<dd>: Battery charge % required after power off to restore power</p>
<dt><code>*ITEMP</code></p>
<dd>: UPS internal temperature in degrees Celcius</p>
<dt><code>ALARMDEL</code></p>
<dd>: Delay period before UPS starts sounding alarm</p>
<dt><code>BATTV</code></p>
<dd>: Current battery voltage</p>
<dt><code>*LINEFREQ</code></p>
<dd>: Current line frequency in Hertz</p>
<dt><code>*LASTXFER</code></p>
<dd>: Reason for last transfer to battery since apcupsd startup</p>
<dt><code>NUMXFERS</code></p>
<dd>: Number of transfers to battery since apcupsd startup</p>
<dt><code>XONBATT</code></p>
<dd>: Date, time of last transfer to battery since apcupsd startup</p>
<dt><code>TONBATT</code></p>
<dd>: Seconds currently on battery</p>
<dt><code>CUMONBATT</code></p>
<dd>: Cumulative seconds on battery since apcupsd startup</p>
<dt><code>XOFFBAT</code></p>
<dd>: Date, time of last transfer off battery since apcupsd startup</p>
<dt><code>SELFTEST</code></p>
<dd>: Date and time of last self test since apcupsd startup</p>
<dt><code>STATFLAG</code></p>
<dd>: UPS status flag in hex</p>
<dt><code>MANDATE</code></p>
<dd>: UPS date of manufacture</p>
<dt><code>SERIALNO</code></p>
<dd>: UPS serial number</p>
<dt><code>BATTDATE</code></p>
<dd>: Date battery last replaced (if set)</p>
<dt><code>NOMBATTV</code></p>
<dd>: Nominal battery voltage</p>
<dt><code>FIRMWARE</code></p>
<dd>: UPS firmware version</p>
<dt><code>APCMODEL</code></p>
<dd>: APC model information</p>
<dt><code>* presence dependant on USB firmware version.</code></p>
<dd></dl>
<h3>Web/SNMP (AP9716) or PowerNet SNMP (AP9605) SmartSlot Card</h3>
<dl>
<dt><code>LINEV</code></p>
<dd>: Current input line voltage</p>
<dt><code>LOADPCT</code></p>
<dd>: Percentage of UPS load capacity used as estimated by UPS</p>
<dt><code>BCHARGE</code></p>
<dd>: Current battery capacity charge percentage</p>
<dt><code>TIMELEFT</code></p>
<dd>: Remaining runtime left on battery as estimated by UPS</p>
<dt><code>MBATTCHG</code></p>
<dd>: Min battery charge % (BCHARGE) required for system shutdown</p>
<dt><code>MINTIMEL</code></p>
<dd>: Min battery runtime (MINUTES) required for system shutdown</p>
<dt><code>MAXTIME</code></p>
<dd>: Max battery runtime (TIMEOUT) after which system is shutdown</p>
<dt><code>MAXLINEV</code></p>
<dd>: Maximum input line voltage since apcupsd startup</p>
<dt><code>MINLINEV</code></p>
<dd>: Minimum input line voltage since apcupsd startup</p>
<dt><code>OUTPUTV</code></p>
<dd>: UPS output voltage</p>
<dt><code>SENSE</code></p>
<dd>: Current UPS sensitivity setting for voltage fluctuations</p>
<dt><code>DWAKE</code></p>
<dd>: Time UPS waits after power off when the power is restored</p>
<dt><code>DSHUTD</code></p>
<dd>: Delay before UPS powers down after command received</p>
<dt><code>DLOWBATT</code></p>
<dd>: Low battery signal sent when this much runtime remains</p>
<dt><code>LOTRANS</code></p>
<dd>: Input line voltage below which UPS will switch to battery</p>
<dt><code>HITRANS</code></p>
<dd>: Input line voltage above which UPS will switch to battery</p>
<dt><code>RETPCT</code></p>
<dd>: Battery charge % required after power off to restore power</p>
<dt><code>ITEMP</code></p>
<dd>: UPS internal temperature in degrees Celcius</p>
<dt><code>ALARMDEL</code></p>
<dd>: Delay period before UPS starts sounding alarm</p>
<dt><code>LINEFREQ</code></p>
<dd>: Current line frequency in Hertz</p>
<dt><code>NUMXFERS</code></p>
<dd>: Number of transfers to battery since apcupsd startup</p>
<dt><code>TONBATT</code></p>
<dd>: Seconds currently on battery</p>
<dt><code>CUMONBATT</code></p>
<dd>: Cumulative seconds on battery since apcupsd startup</p>
<dt><code>XOFFBATT</code></p>
<dd>: Date, time of last transfer off battery since apcupsd startup</p>
<dt><code>STESTI</code></p>
<dd>: Self-test interval</p>
<dt><code>STATFLAG</code></p>
<dd>: UPS status flag in hex</p>
<dt><code>DIPSW</code></p>
<dd>: Current UPS DIP switch settings</p>
<dt><code>MANDATE</code></p>
<dd>: UPS date of manufacture</p>
<dt><code>SERIALNO</code></p>
<dd>: UPS serial number</p>
<dt><code>BATTDATE</code></p>
<dd>: Date battery last replaced (if set)</p>
<dt><code>NOMOUTV</code></p>
<dd>: Nominal output voltage to supply when on battery power</p>
<dt><code>NOMPOWER</code></p>
<dd>: Nominal power output in watts</p>
<dt><code>EXTBATTS</code></p>
<dd>: Number of external batteries (for XL models)</p>
<dt><code>BADBATTS</code></p>
<dd>: Number of bad external battery packs (for XL models)</p>
<dt><code>FIRMWARE</code></p>
<dd>: UPS firmware version</p>
<dt><code>APCMODEL</code></p>
<dd>: APC model information</dl>
<h3>Share-UPS (AP9270) (Basic port)</h3>
<dl>
<dt><code>MBATTCHG</code></p>
<dd>: Min battery charge % (BCHARGE) required for system shutdown</p>
<dt><code>MINTIMEL</code></p>
<dd>: Min battery runtime (MINUTES) required for system shutdown</p>
<dt><code>MAXTIME</code></p>
<dd>: Max battery runtime (TIMEOUT) after which system is shutdown</p>
<dt><code>NUMXFERS</code></p>
<dd>: Number of transfers to battery since apcupsd startup</p>
<dt><code>TONBATT</code></p>
<dd>: Seconds currently on battery</p>
<dt><code>CUMONBATT</code></p>
<dd>: Cumulative seconds on battery since apcupsd startup</p>
<dt><code>XOFFBATT</code></p>
<dd>: Date, time of last transfer off battery since apcupsd startup</p>
<dt><code>STATFLAG</code></p>
<dd>: UPS status flag in hex</dl>
<h3>UPS Environmental Monitoring SmartSlot Card (AP9612TH)</h3>
<dl>
<dt><code>HUMIDITY</code></p>
<dd>: Ambient humidity</p>
<dt><code>AMBTEMP</code></p>
<dd>: Ambient temperature</dl>
<h3>Back-UPS Pro and Smart-UPS v/s (Smart Signalling)</h3>
<dl>
<dt><code>LINEFAIL</code></p>
<dd>: Input line voltage status.</p>
<dt><code>BATTSTAT</code></p>
<dd>: Battery status.</p>
<dt><code>LASTXFER</code></p>
<dd>: Last (observed) transfer to battery.</dl>
<h3>Back-UPS and Net-UPS (Simple Signalling)</h3>
<dl>
<dt><code>LINEFAIL</code></p>
<dd>: Input line voltage status.</p>
<dt><code>BATTSTAT</code></p>
<dd>: Battery status.</p>
<dt><code>STATFLAG</code></p>
<dd>: UPS status flag in hex.</dl>
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
