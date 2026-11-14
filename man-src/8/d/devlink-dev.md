---
title: "devlink-dev(8)"
name: "devlink-dev"
section: "8"
letter: "d"
url: "/docs/linux/man/8-devlink-dev/"
description: "devlink-dev – devlink device configuration"
---

<p>devlink-dev &#8211; devlink device configuration</p>
<h2>Synopsis</h2>
<pre><code>devlink

[ OPTIONS ]

dev

{ COMMAND |

    help }

OPTIONS := {

    -V[ersion] |
    -n[no-nice-names] }</code></pre>
<p> <code>devlink dev show</code> [ <i>DEV</i> ]<br />
 <code>devlink dev help</code><br />
 <code>devlink dev eswitch set</code> <i>DEV</i> [ <code>mode</code> { <code>legacy</code> | <code>switchdev</code> } ] [ <code>inline-mode</code> { <code>none</code> | <code>link</code> | <code>network</code> | <code>transport</code> } ] [ <code>encap-mode</code> { <code>none</code> | <code>basic</code> } ]<br />
 <code>devlink dev eswitch show</code> <i>DEV</i> </p>
<pre><code>devlink dev param set

DEV

name

PARAMETER

value

VALUE

cmode { runtime | driverinit | permanent }</code></pre>
<p> <code>devlink dev param show</code> [ <i>DEV</i> <code>name</code> <i>PARAMETER</i> ]<br />
 <code>devlink dev reload</code> <i>DEV</i> [ <code>netns</code> { <i>PID</i> | <i>NAME</i> | <i>ID</i> } ] [ <code>action</code> { <code>driver_reinit</code> | <code>fw_activate</code> } ] [ <code>limit no_reset</code> ]<br />
 <code>devlink dev info</code> [ <i>DEV</i> ]<br />
 <code>devlink dev flash</code> <i>DEV</i> <code>file</code> <i>PATH</i> [ <code>target</code> <i>ID</i> ] </p>
<h2>Description</h2>
<h3>devlink dev show &#8211; display devlink device attributes</h3>
<p><i>DEV</i> &#8211; specifies the devlink device to show. If this argument is omitted all devices are listed. Format is: BUS_NAME/BUS_ADDRESS</p>
<h3>devlink dev eswitch show &#8211; display devlink device eswitch attributes</h3>
<h3>devlink dev eswitch set &#8211; sets devlink device eswitch attributes</h3>
<dl>
<dt><code>mode</code> { <code>legacy</code> | <code>switchdev</code> }</p>
<dd>Set eswitch mode <i>legacy</i> &#8211; Legacy SRIOV <i>switchdev</i> &#8211; SRIOV switchdev offloads</p>
<dt><code>inline-mode</code> { <code>none</code> | <code>link</code> | <code>network</code> | <code>transport</code> }</p>
<dd>Some HWs need the VF driver to put part of the packet headers on the TX descriptor so the e-switch can do proper matching and steering. <i>none</i> &#8211; None <i>link</i> &#8211; L2 mode <i>network</i> &#8211; L3 mode <i>transport</i> &#8211; L4 mode</p>
<dt><code>encap-mode</code> { <code>none</code> | <code>basic</code> }</p>
<dd>Set eswitch encapsulation support <i>none</i> &#8211; Disable encapsulation support <i>basic</i> &#8211; Enable encapsulation support</dl>
<h3>devlink dev param set &#8211; set new value to devlink device configuration parameter</h3>
<dl>
<dt><code>name</code><i> PARAMETER</i></p>
<dd>Specify parameter name to set.</p>
<dt><code>value</code><i> VALUE</i></p>
<dd>New value to set.</p>
<dt><code>cmode</code> { <code>runtime</code> | <code>driverinit</code> | <code>permanent</code> }</p>
<dd>Configuration mode in which the new value is set. <i>runtime</i> &#8211; Set new value while driver is running. This configuration mode doesn&#8217;t require any reset to apply the new value. <i>driverinit</i> &#8211; Set new value which will be applied during driver initialization. This configuration mode requires restart driver by devlink reload command to apply the new value. <i>permanent</i> &#8211; New value is written to device&#8217;s non-volatile memory. This configuration mode requires hard reset to apply the new value.</dl>
<h3>devlink dev param show &#8211; display devlink device supported configuration parameters attributes</h3>
<p><code>name</code> <i>PARAMETER</i> Specify parameter name to show. If this argument is omitted all parameters supported by devlink devices are listed.</p>
<h3>devlink dev reload &#8211; perform hot reload of the driver.</h3>
<p><i>DEV</i> &#8211; Specifies the devlink device to reload. <code>netns</code> {<i> PID </i>|<i> NAME </i>|<i> ID </i>} &#8211; Specifies the network namespace to reload into, either by pid, name or id. <code>action</code> { <code>driver_reinit</code> | <code>fw_activate</code> } &#8211; Specifies the reload action required. If this argument is omitted <i>driver_reinit</i> action will be used. Note that even though user asks for a specific action, the driver implementation might require to perform another action alongside with it. For example, some driver do not support driver reinitialization being performed without fw activation. Therefore, the devlink reload command returns the list of actions which were actrually performed. <i>driver_reinit</i> &#8211; Driver entities re-initialization, applying devlink-param and devlink-resource values. <i>fw_activate</i> &#8211; Activates new firmware if such image is stored and pending activation. If no limitation specified this action may involve firmware reset. If no new image pending this action will reload current firmware image. <code>limit no_reset</code> &#8211; Specifies limitation on reload action. If this argument is omitted limit is unspecificed and the reload action is not limited. In such case driver implementation may include reset or downtime as needed to perform the actions. <i>no_reset</i> &#8211; No reset allowed, no down time allowed, no link flap and no configuration is lost.</p>
<h3>devlink dev info &#8211; display device information.</h3>
<p>Display device information provided by the driver. This command can be used to query versions of the hardware components or device components which can&#8217;t be updated ( <i>fixed</i> ) as well as device firmware which can be updated. For firmware components <i>running</i> displays the versions of firmware currently loaded into the device, while <i>stored</i> reports the versions in device&#8217;s flash. <i>Running</i> and <i>stored</i> versions may differ after flash has been updated, but before reboot. <i>DEV</i> &#8211; specifies the devlink device to show. If this argument is omitted all devices are listed.</p>
<h3>devlink dev flash &#8211; write device&#8217;s non-volatile memory.</h3>
<p><i>DEV</i> &#8211; specifies the devlink device to write to. <code>file</code> <i>PATH</i> &#8211; Path to the file which will be written into device&#8217;s flash. The path needs to be relative to one of the directories searched by the kernel firmware loaded, such as /lib/firmware. <code>component</code> <i>NAME</i> &#8211; If device stores multiple firmware images in non-volatile memory, this parameter may be used to indicate which firmware image should be written. The value of <i>NAME</i> should match the component names from <code>devlink dev info</code> and may be driver-dependent. </p>
<h2>Examples</h2>
<p>devlink dev show</p>
<dl>
<dd>Shows the state of all devlink devices on the system.</dl>
<p> devlink dev show pci/0000:01:00.0</p>
<dl>
<dd>Shows the state of specified devlink device.</dl>
<p> devlink dev eswitch show pci/0000:01:00.0</p>
<dl>
<dd>Shows the eswitch mode of specified devlink device.</dl>
<p> devlink dev eswitch set pci/0000:01:00.0 mode switchdev</p>
<dl>
<dd>Sets the eswitch mode of specified devlink device to switchdev.</dl>
<p> devlink dev param show pci/0000:01:00.0 name max_macs</p>
<dl>
<dd>Shows the parameter max_macs attributes.</dl>
<p> devlink dev param set pci/0000:01:00.0 name internal_error_reset value true cmode runtime</p>
<dl>
<dd>Sets the parameter internal_error_reset of specified devlink device to true.</dl>
<p> devlink dev reload pci/0000:01:00.0</p>
<dl>
<dd>Performs hot reload of specified devlink device.</dl>
<p> devlink dev flash pci/0000:01:00.0 file firmware.bin</p>
<dl>
<dd>Flashes the specified devlink device with provided firmware file name. If the driver supports it, user gets updates about the flash status. For example:<br />
 Preparing to flash<br />
 Flashing 100%<br />
 Flashing done</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-devlink/">devlink</a></code>(8), <code><a href="/docs/linux/man/8-devlink-port/">devlink-port</a></code>(8), <code><a href="/docs/linux/man/8-devlink-sb/">devlink-sb</a></code>(8), <code><a href="/docs/linux/man/8-devlink-monitor/">devlink-monitor</a></code>(8), </p>
<h2>Author</h2>
<p>Jiri Pirko &lt;jiri [at] mellanox.com&gt;</p>
