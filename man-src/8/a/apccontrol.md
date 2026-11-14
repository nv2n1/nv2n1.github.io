---
title: "apccontrol(8)"
name: "apccontrol"
section: "8"
letter: "a"
url: "/docs/linux/man/8-apccontrol/"
description: "apccontrol –"
---

<p><code>apccontrol</code> &#8211; </p>
<p><a href="/docs/linux/man/8-apcupsd/">apcupsd</a>(8) event handler script</p>
<h2>Synopsis</h2>
<pre><code>{ &lt;event&gt; &lt;ups-name&gt; &lt;connected&gt; &lt;powered&gt; }</code></pre>
<h2>Description</h2>
<p>When <a href="/docs/linux/man/8-apcupsd/">apcupsd</a>(8) detects anomalies from the UPS being monitored, it triggers an event which usually results in one or more calls to the shell script. Each event causes to take a particular action. These actions default to sane behaviour for all the events that apcupsd is likely to encounter. However, you can change the behaviour of every single action. When apcupsd detects an event, it calls the script with the following four arguments: </p>
<dt><code>event</code></p>
<dd>This is the event that occurred. Refer to the list of possible events below.</p>
<dt><code>ups-name</code></p>
<dd>This is the name of the UPS as specified in the /etc/apcupsd/apcupsd.conf configuration file &#8211; not the name in the EEPROM of a smart UPS.</p>
<dt><code>connected</code></p>
<dd>This is 1 if apcupsd is connected to the UPS via a serial or USB port. In the case of a slave machine where apcupsd is not directly connected to the UPS, this value will be 0.</p>
<dt><code>powered</code></p>
<dd>This is 1 if the computer on which apcupsd is running is powered by the UPS and 0 if not. This is not currently implemented and always defaults to 0.</dl>
<p> Events are sent to the system log and, optionally, to the temporary events file ( /etc/apcupsd/apcupsd.events ) , and they also generate a call to which in turn will call any scripts you have placed in the /etc/apcupsd directory.</p>
<h3>List Of Events And Default Actions</h3>
<dl>
<dt><code>annoyme</code></p>
<dd>apcupsd generates this event when a shutdown is scheduled, and the time specified by the ANNOYME configuration directive in the /etc/apcupsd/apcupsd.conf file has expired. Default action &#8212; sends &quot;Power problems please logoff.&quot; to <a href="/docs/linux/man/1-wall/">wall</a>(1) and then exits.</p>
<dt><code>battattach</code></p>
<dd>apcupsd generates this event when it detects that the UPS battery has been reconnected after a battdetach event. Default action: does nothing.</p>
<dt><code>battdetach</code></p>
<dd>apcupsd generates this event when it detects that the UPS battery has been disconnected. Default action: does nothing.</p>
<dt><code>changeme</code></p>
<dd>apcupsd generates this event when it detects that the utility power is on, but the battery is not functioning correctly. This is repeated every 9 hours. Default action &#8212; sends &quot;Emergency! UPS batteries have failed Change them NOW&quot; to wall and then exits.</p>
<dt><code>commfailure</code></p>
<dd>apcupsd generates this event each time it loses communication with the monitored UPS. This event is not detected on simple signalling UPSes like the Back-UPS 650. Default action &#8212; sends &quot;Communications with UPS lost.&quot; to wall and then exits.</p>
<dt><code>commok</code></p>
<dd>apcupsd generates this event after a commfailure event when communication with the UPS is re-established. Default action &#8212; sends &quot;Communications with UPS restored.&quot; to wall and then exits.</p>
<dt><code>doreboot</code></p>
<dd>This event is deprecated and should not be used. Default action &#8212; sends &quot;Beginning Reboot Sequence&quot; to wall and then calls <a href="/docs/linux/man/8-shutdown/">shutdown</a>(8) with the &quot;-r now&quot; command line arguments to reboot the computer.</p>
<dt><code>doshutdown</code></p>
<dd>apcupsd generates this event to shutdown the computer when the UPS is running on battery power and one of the limits (time, run, load) is reached. Default action &#8212; sends &quot;Beginning Shutdown Sequence&quot; to wall and then calls <a href="/docs/linux/man/8-shutdown/">shutdown</a>(8) with the command line arguments &quot;-h now&quot; to shutdown the computer.</p>
<dt><code>emergency</code></p>
<dd>apcupsd generates this event when the UPS is on battery power, the battery is low and the utility power is on: a sure sign of battery failure! Default action &#8212; sends &quot;Emergency Shutdown. Possible UPS battery failure.&quot; to wall. Immediately after this, apcupsd generates a doshutdown event to shutdown the system.</p>
<dt><code>failing</code></p>
<dd>apcupsd generates this event when the UPS is running on batteries and the UPS sets the low battery signal indicating that battery power is nearly exhausted. After this event, apcupsd will immediately generate a doshutdown event. Default action &#8212; sends &quot;UPS battery power exhausted. Doing shutdown.&quot; to wall and then exits.</p>
<dt><code>killpower</code></p>
<dd>apcupsd does not normally generate this event. Instead, it is invoked directly from the system halt script as &#8216;apccontrol killpower&#8217; because the killpower event needs to be performed as late in system shutdown as possible. Default action &#8212; sends &quot;UPS now committed to shut down&quot; to wall, waits for 10 seconds and then issues the command &quot;apcupsd &#8211;killpower&quot; to put the UPS into hibernate mode and shut off power to the connected equipment. In the case of a smart UPS, the UPS will then wait for the expiry of any configured shutdown time delay specified by the SLEEP configuration directive. In hibernate mode, the UPS will restore utility power to the connected equipment subject to the values specified for the RETURNCHARGE and WAKEUP configuration directives.</p>
<dt><code>loadlimit</code></p>
<dd>apcupsd generates this event when the battery discharge limit specified by the BATTERYLEVEL configuration directive has been reached. Default action &#8212; sends &quot;UPS battery discharge limit reached. Doing shutdown&quot; to wall and then exits. After this event, apcupsd will immediately generate a doshutdown event.</p>
<dt><code>mainsback</code></p>
<dd>apcupsd generates this event when the utility power returns after a powerout event. The doshutdown event may or may not have been generated depending on the parameters you have defined and the length of the power outage. Attempting cancellation of a doshutdown event should never be tried as it is very unlikely to succeed and will almost certainly leave your computer in an indeterminate state. Default action &#8212; if the file /var/run/powerfail exists, sends &quot;Continuing with shutdown.&quot; to wall and then exits. Otherwise, does nothing.</p>
<dt><code>onbattery</code></p>
<dd>apcupsd generates this event if a power failure has been detected and the UPS is still on battery power at the expiry of the delay specified by the ONBATTERYDELAY configuration directive. Default action &#8212; sends &quot;Power failure. Running on UPS batteries.&quot; to wall and then exits.</p>
<dt><code>offbattery</code></p>
<dd>apcupsd generates this event when the utility power returns if, and only if, the onbattery event has been generated. Default &#8212; sends &quot;&quot;Power has returned&#8230;&quot; to wall and then exits.</p>
<dt><code>powerout</code></p>
<dd>apcupsd generates this event as soon as apcupsd detects that the UPS has switched to battery power and it is not a self-test. Default action &#8212; does nothing.</p>
<dt><code>remotedown</code></p>
<dd>apcupsd generates this event on a slave machine when it detects either (1) that the master has shutdown, or (2) that an onbattery event has occurred and communication with the master has been lost. Default action: sends &quot;Remote Shutdown. Beginning Shutdown Sequence.&quot; to wall and exits. Immediately after this, apcupsd generates a doshutdown event to shutdown the system.</p>
<dt><code>runlimit</code></p>
<dd>apcupsd generates this event when the remaining runtime limit specified by the MINUTES configuration directive expires while the UPS is on battery power as the result of a utility power outage. The remaining runtime is internally calculated by the UPS and monitored by apcuspd. Default action &#8212; sends &quot;UPS battery runtime percent reached. Doing shutdown.&quot; to wall and then exits. After this event, apcupsd will immediately generate a doshutdown event.</p>
<dt><code>timeout</code></p>
<dd>apcupsd generates this event when the time specified by the TIMEOUT configuration directive expires while the UPS is on battery power as the result of a utility power outage. This configuration directive is not normally used with smart UPSes which would instead rely on the more reliable remaining runtime (MINUTES) or the battery level (BATTERYLEVEL) configuration directives. Default action &#8212; send &quot;UPS battery runtime limit exceeded. Doing shutdown.&quot; to wall and then exits. After this event, apcupsd will immediately generate a doshutdown event.</p>
<dt><code>startselftest</code></p>
<dd>apcupsd generates this event when it detects the start of a UPS self test. Default action: does nothing.</p>
<dt><code>endselftest</code></p>
<dd>apcupsd generates this event when it detects the end of a UPS self test. Default action: does nothing.</dl>
<h3>Customising Event Actions</h3>
<p>Do <i>not</i> modify directly as it will be overwritten the next time you upgrade to a new release of apcupsd. The recommended way to customise an event action is simply to create an executable program or script file with the same name as the event and put that file in the /etc/apcupsd directory. Now, when the selected event occurs, will execute your program or script. If you want to also execute its default action for the selected event, your program or script should exit with an exit status of 0 (zero). If you do <i>not </i> want to also execute its default action for the selected event, your program or script must exit with an exit status of 99. Be aware that if you completely override the default action, you must ensure the proper shutdown of your computer if this is necessary. Some sample scripts (changeme, commfailure, commok, offbattery and onbattery) that email messages to root instead of broadcasting messages to all logged-in users may be found in /etc/apcupsd after an installation and also in the platforms/etc directory of the apcupsd source code. </p>
<h2>Files</h2>
<p>/etc/apcupsd/apccontrol</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-wall/">wall</a>(1), apcupsd.conf5, <a href="/docs/linux/man/8-apcupsd/">apcupsd</a>(8), <a href="/docs/linux/man/8-shutdown/">shutdown</a>(8). </p>
<p> The HTML apcupsd manual installed on your system or available online at <a rel="nofollow" href="http://www.apcupsd.org/">http://www.apcupsd.org/</a></p>
<h2>Authors</h2>
<h3>This page</h3>
<p>An Trevor Roydhouse</p>
<h3>Software</h3>
<p>An Adam Kropelin (current Project Manager and Code Maintainer) An Kern Sibbald (former Project Manager and Code Maintainer) An Riccardo Facchetti (former Project Manager and Code Maintainer) An Andre M. Hedrick (Project Founder and former Code Maintainer)</p>
<h3>Contributors</h3>
<p>An enormous number of users who have devoted their time and energy to this project &#8212; thanks.</p>
