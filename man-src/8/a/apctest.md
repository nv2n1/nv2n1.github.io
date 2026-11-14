---
title: "apctest(8)"
name: "apctest"
section: "8"
letter: "a"
url: "/docs/linux/man/8-apctest/"
description: "apctest –"
---

<p><code>apctest</code> &#8211; </p>
<p><a href="/docs/linux/man/8-apcupsd/">apcupsd</a>(8) test program</p>
<h2>Synopsis</h2>
<h2>Description</h2>
<p>is a program that enables the running of certain low-level tests to check the operation of the attached simple signalling American Power Conversion Corp (APC) UPS and to check that your <a href="/docs/linux/man/8-apcupsd/">apcupsd</a>(8) configuration is correctly setup and can establish communication with the UPS. For an APC UPS operating in APC smart protocol mode, enables the reading and programming of the values of the UPS EEPROM configuration variables as well and the performing of a battery runtime calibration. It also provides a simple TTY chat mode which allows direct interaction with the UPS via the APC smart protocol. For details of this protocol and the available commands, refer to the detailed &quot;APC Smart Protocol&quot; section in the apcupsd manual. IMPORTANT: Before running  </p>
<li> Check that the UPSCABLE, UPSTYPE and DEVICE configuration directives in the apcupsd.conf5 configuration file have been set appropriately; and
<li> Shutdown apcupsd if it is running. You cannot run both apcupsd and at the same time. </ul>
<p> When run, displays a menu of options which are different depending on whether the UPS is connected to a USB port or to a serial port. For a serial port connection, there are two different menus depending on whether the UPS is operating in APC smart protocol mode or simple signalling mode &#8211; this also depends on which cable is used to connect to the UPS. If a simple signalling cable is used to connect to a Smart-UPS, the UPS will only be able to operate in simple signalling mode. saves a transcript of the session to the file apctest.out in the directory from which the program was called. Its content is useful for debugging purposes.</p>
<h2>Usb Port</h2>
<p>When using a UPS connected to a USB port (eg Back-UPS RS 1500), the following menu options will appear:</p>
<h3>Option 1) Test kill UPS power</h3>
<p>Performs a power down of the UPS into hibernate mode.</p>
<h3>Option 2) Perform self-test</h3>
<p>Performs an immediate self-test (switches to battery power to do so).</p>
<h3>Option 3) Read last self-test result</h3>
<p>Displays the last self-test result.</p>
<h3>Option 4) View/Change battery date</h3>
<p>Displays the current battery replacement date and optionally allows you to change it &#8211; useful when the battery is replaced so that you can accurately keep track of its age.</p>
<h3>Option 5) View manufacturing date</h3>
<p>Displays the date the UPS was manufactured.</p>
<h3>Option 6) View/Change alarm behavior</h3>
<p>Sets the delay period before the UPS starts sounding its alarm when the utility power is lost.</p>
<h3>Option 7) View/Change sensitivity</h3>
<p>Changes how sensitive the UPS is to the utility power quality and voltage fluctuations &#8211; (H)igh, (M)edium or (L)ow. The higher the sensitivity, the faster the UPS will switch to battery power or activate SmartBoost/SmartTrim (features that avoid using battery power provided the under/over voltage is within 12% of nominal). This setting should normally be set to High unless the UPS switches to battery power frequently, in which case a less sensitive setting will preserve UPS batteries&#8230; if the connected equipment can tolerate the power quality.</p>
<h3>Option 8) View/Change low transfer voltage</h3>
<p>Sets the low voltage level at which the UPS switches to battery or activates SmartBoost.</p>
<h3>Option 9) View/Change high transfer voltage</h3>
<p>Sets the high voltage level at which the UPS switches to battery or activates SmartTrim.</p>
<h3>Option 10) Perform battery calibration</h3>
<p>This performs a battery runtime calibration. This can only be performed if your battery is charged to 100% of capacity. The runtime calibration discharges the UPS battery to approximately 25% of capacity. The exact percentage depends on the UPS model. </p>
<p> The advantage of doing this calibration is that the UPS will recalibrate the remaining runtime counter that it maintains and therefore report a more accurate estimated runtime. As batteries age, they tend to hold less charge, so the UPS&#8217;s internal runtime counter may not be accurate after several years. </p>
<p> It is recommended that battery runtime calibration be performed annually. Performing it too often shortens the lifetime of the UPS batteries.</p>
<h3>Option 11) Test Alarm</h3>
<p>This option will cause the UPS alarm beeper to sound for several seconds.</p>
<h3>Option 12) View/Change self-test interval</h3>
<p>This option allows you to change the time interval between automatic UPS self-tests.</p>
<h3>Option Q) Quit</h3>
<p>Exits from the program.</p>
<h2>Serial Port (Smart Protocol Mode)</h2>
<p>When using a UPS operating in APC smart protocol mode (eg a Smart-UPS) the following menu options will appear:</p>
<h3>Option 1) Query the UPS for all known values</h3>
<p>Selecting this option probes the UPS for all EEPROM configuration variable values known to and displays them in rather raw format. This output can be useful for providing technical support if you are having problems with the behaviour of the UPS or <a href="/docs/linux/man/8-apcupsd/">apcupsd</a>(8).</p>
<h3>Option 2) Perform a Battery Runtime Calibration</h3>
<p>This performs a battery runtime calibration. This can only be performed if your battery is charged to 100% of capacity. The runtime calibration discharges the UPS battery to approximately 25% of capacity. The exact percentage depends on the UPS model. can optionally abort the calibration if it detects that the battery charge is below 10%. </p>
<p> The advantage of doing this calibration is that the UPS will recalibrate the remaining runtime counter that it maintains and therefore report a more accurate estimated runtime. As batteries age, they tend to hold less charge, so the UPS&#8217;s internal runtime counter may not be accurate after several years. </p>
<p> It is recommended that battery runtime calibration be performed annually. Performing it too often shortens the lifetime of the UPS batteries.</p>
<h3>Option 3) Abort Battery Calibration</h3>
<p>This option aborts an in progress battery runtime calibration.</p>
<h3>Option 4) Monitor Battery Calibration progress</h3>
<p>Allows restarting of the monitoring of a battery runtime calibration.</p>
<h3>Option 5) Program EEPROM</h3>
<p>Allows the programming of the values of a Smart-UPS&#8217;s EEPROM configuration variables. </p>
<p> Choosing this option presents a sub-menu of programming options which are detailed below.</p>
<dl>
<dt><code>Option 1) Print EEPROM values</code></p>
<dd>Prints the value of all EEPROM configuration variables known to <code>.</code></p>
<dt><code>Option 2) Change Battery date</code></p>
<dd>Changes the battery date &#8211; useful when the battery is replaced so that you can accurately keep track of its age.</p>
<dt><code>Option 3) Change UPS name</code></p>
<dd>Changes the UPS name &#8211; use no more than 8 characters to name the UPS.</p>
<dt><code>Option 4) Change sensitivity</code></p>
<dd>Changes how sensitive the UPS is to the utility power quality and voltage fluctuations &#8211; (H)igh, (M)edium or (L)ow. The higher the sensitivity, the faster the UPS will switch to battery power or activate SmartBoost/SmartTrim (features that avoid using battery power provided the under/over voltage is within 12% of nominal). This setting should normally be set to High unless the UPS switches to battery power frequently, in which case a less sensitive setting will preserve UPS batteries&#8230; if the connected equipment can tolerate the power quality.</p>
<dt><code>Option 5) Change alarm delay</code></p>
<dd>Changes the delay period before the UPS starts sounding its alarm when the utility power is lost.</p>
<dt><code>Option 6) Change low battery warning delay</code></p>
<dd>Changes the remaining runtime minutes at which the UPS will send the low battery signal. When the UPS internally calculates that the specified number of minutes remains before battery power will be exhausted, it sends the low battery warning.</p>
<dt><code>Option 7) Change wakeup delay</code></p>
<dd>Changes the delay before the UPS restores power to connected equipment when the utility power returns after shutting down in hibernate mode.</p>
<dt><code>Option 8) Change shutdown delay</code></p>
<dd>Changes the delay for which the UPS waits before shutting off power to the connected equipment after being commanded to power down in hibernate mode.</p>
<dt><code>Option 9) Change low transfer voltage</code></p>
<dd>Changes the low voltage level at which the UPS switches to battery or activates SmartBoost.</p>
<dt><code>Option 10) Change high transfer voltage</code></p>
<dd>Changes the high voltage level at which the UPS switches to battery or activates SmartTrim.</p>
<dt><code>Option 11) Change battery return threshold percent</code></p>
<dd>Changes the battery charge percentage required after power down in hibernate mode before to the UPS will restore power to connected equipment on the return of utility power.</p>
<dt><code>Option 12) Change output voltage when on batteries</code></p>
<dd>Changes the nominal voltage output when the UPS is running on battery power.</p>
<dt><code>Option 13) Change the self test interval</code></p>
<dd>Changes or disables the automatic self-test interval.</p>
<dt><code>Option 14) Set EEPROM with configuration file values</code></p>
<dd>This option allows the bulk programming of the EEPROM configuration variables from the values contained in the /etc/apcupsd.conf configuration file. Refer to the &quot;APCTEST EEPROM CONFIGURATION DIRECTIVES&quot; section of the man page for apcupsd.conf5</p>
<dt><code>Option 15) Quit</code></p>
<dd>This option exits back to the previous (main) menu.</dl>
<h3>Option 6) Enter TTY mode communicating with UPS</h3>
<p>This option allows direct interaction with the attached UPS using the APC smart protocol commands. </p>
<p> WARNING: Take special care what commands you enter because it is possible to cause the UPS to suddenly shutdown or, in the worst case, modify the UPS in such a way as to permanently disable it. Do NOT experiment with unknown or unsupported commands. Caveat Utilitor!</p>
<h3>Option 7) Quit</h3>
<p>Exits from the program.</p>
<h2>Serial Port (Simple Signalling Mode)</h2>
<p>When using an APC UPS operating in simple signalling mode the following menu options will appear:</p>
<h3>Option 1) Test 1 &#8211; normal mode</h3>
<p>The test result depends on the model of UPS and type of cable being used. Refer to the &quot;Using apctest on Serial-Line UPSses&quot; section in the apcupsd manual for details.</p>
<h3>Option 2) Test 2 &#8211; no cable</h3>
<p>The test result depends on the model of UPS and type of cable being used. Refer to the &quot;Using apctest on Serial-Line UPSses&quot; section in the apcupsd manual for details.</p>
<h3>Option 3) Test 3 &#8211; no power</h3>
<p>The test result depends on the model of UPS and type of cable being used. Refer to the &quot;Using apctest on Serial-Line UPSses&quot; section in the apcupsd manual for details.</p>
<h3>Option 4) Test 4 &#8211; low battery (requires Test 3 first)</h3>
<p>The test result depends on the model of UPS and type of cable being used. Refer to the &quot;Using apctest on Serial-Line UPSses&quot; section in the apcupsd manual for details.</p>
<h3>Option 5) Test 5 &#8211; battery exhausted</h3>
<p>The test result depends on the model of UPS and type of cable being used. Refer to the &quot;Using apctest on Serial-Line UPSses&quot; section in the apcupsd manual for details.</p>
<h3>Option 6) Test 6 &#8211; kill UPS power</h3>
<p>The test result depends on the model of UPS and type of cable being used. Refer to the &quot;Using apctest on Serial-Line UPSses&quot; section in the apcupsd manual for details.</p>
<h3>Option 7) Test 7 &#8211; run tests 1 through 5</h3>
<p>This option has guess which cable should be used with the attached UPS.</p>
<h3>Option 9) Quit</h3>
<p>Exits from the program.</p>
<h2>Files</h2>
<p>/etc/apcupsd/apcupsd.conf default configuration file </p>
<p> apctest.out transcript of the session</p>
<h2>See Also</h2>
<p>apcupsd.conf5, <a href="/docs/linux/man/8-apcupsd/">apcupsd</a>(8). </p>
<p> The HTML apcupsd manual installed on your system or available online at <a rel="nofollow" href="http://www.apcupsd.org/">http://www.apcupsd.org/</a></p>
<h2>Authors</h2>
<h3>This page</h3>
<p>An Trevor Roydhouse (current) An Robert Huff</p>
<h3>Software</h3>
<p>An Adam Kropelin (current Project Manager and Code Maintainer) An Kern Sibbald (former Project Manager and Code Maintainer) An Riccardo Facchetti (former Project Manager and Code Maintainer) An Andre M. Hedrick (Project Founder and former Code Maintainer)</p>
<h3>Contributors</h3>
<p>An enormous number of users who have devoted their time and energy to this project &#8212; thanks.</p>
