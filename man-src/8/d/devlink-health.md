---
title: "devlink-health(8)"
name: "devlink-health"
section: "8"
letter: "d"
url: "/docs/linux/man/8-devlink-health/"
description: "devlink-health – devlink health reporting and recovery"
---

<p>devlink-health &#8211; devlink health reporting and recovery</p>
<h2>Synopsis</h2>
<pre><code>devlink

[ OPTIONS ]

health

{ COMMAND |

    help }

OPTIONS := {

    -V[ersion] }</code></pre>
<p> <code>devlink health show</code> [ { <i>DEV</i> | <i>DEV/PORT_INDEX</i> } <code>reporter</code> REPORTER<i> ] </i><br />
 <code>devlink health recover</code> { <i>DEV</i> | <i>DEV/PORT_INDEX</i> } <code>reporter</code> <i>REPORTER</i><br />
 <code>devlink health diagnose</code> { <i>DEV</i> | <i>DEV/PORT_INDEX</i> } <code>reporter</code> <i>REPORTER</i><br />
 <code>devlink health dump show</code> { <i>DEV</i> | <i>DEV/PORT_INDEX</i> } <code>reporter</code> <i>REPORTER</i><br />
 <code>devlink health test</code> { <i>DEV</i> | <i>DEV/PORT_INDEX</i> } <code>reporter</code> <i>REPORTER</i><br />
 <code>devlink health dump clear</code> { <i>DEV</i> | <i>DEV/PORT_INDEX</i> } <code>reporter</code> <i>REPORTER</i><br />
 <code>devlink health set</code> { <i>DEV</i> | <i>DEV/PORT_INDEX</i> } <code>reporter</code> <i>REPORTER</i> [ <code>grace_period </code><i>MSEC</i> ] [ <code>auto_recover</code> { <code>true</code> | <code>false</code> } ] [ <code>auto_dump</code> { <code>true</code> | <code>false</code> } ]<br />
 <code>devlink health help</code> </p>
<h2>Description</h2>
<h3>devlink health show &#8211; Show status and configuration on all supported reporters.</h3>
<p>Displays info about reporters registered on devlink devices and ports. <i>DEV</i> &#8211; specifies the devlink device.<br />
 <i>DEV/PORT_INDEX</i> &#8211; specifies the devlink port. <i>REPORTER</i> &#8211; specifies the reporter&#8217;s name registered on specified devlink device or port.</p>
<h3>devlink health recover &#8211; Initiate a recovery operation on a reporter.</h3>
<p>This action performs a recovery and increases the recoveries counter on success. <i>DEV</i> &#8211; specifies the devlink device.<br />
 <i>DEV/PORT_INDEX</i> &#8211; specifies the devlink port. <i>REPORTER</i> &#8211; specifies the reporter&#8217;s name registered on specified devlink device or port.</p>
<h3>devlink health diagnose &#8211; Retrieve diagnostics data on a reporter.</h3>
<p><i>DEV</i> &#8211; specifies the devlink device.<br />
 <i>DEV/PORT_INDEX</i> &#8211; specifies the devlink port. <i>REPORTER</i> &#8211; specifies the reporter&#8217;s name registered on specified devlink device or port.</p>
<h3>devlink health test &#8211; Trigger a test event on a reporter.</h3>
<p><i>DEV</i> &#8211; specifies the devlink device. <i>REPORTER</i> &#8211; specifies the reporter&#8217;s name registered on the devlink device.</p>
<h3>devlink health dump show &#8211; Display the last saved dump.</h3>
<p>devlink health saves a single dump per reporter. If an dump is not already stored by the Devlink, this command will generate a new dump. The dump can be generated either automatically when a reporter reports on an error or manually at the user&#8217;s request. <i>DEV</i> &#8211; specifies the devlink device.<br />
 <i>DEV/PORT_INDEX</i> &#8211; specifies the devlink port. <i>REPORTER</i> &#8211; specifies the reporter&#8217;s name registered on specified devlink device or port.</p>
<h3>devlink health dump clear &#8211; Delete the saved dump.</h3>
<p>Deleting the saved dump enables a generation of a new dump on the next &quot;devlink health dump show&quot; command. <i>DEV</i> &#8211; specifies the devlink device.<br />
 <i>DEV/PORT_INDEX</i> &#8211; specifies the devlink port. <i>REPORTER</i> &#8211; specifies the reporter&#8217;s name registered on specified devlink device or port.</p>
<h3>devlink health set &#8211; Configure health reporter.</h3>
<p>Please note that some params are not supported on a reporter which doesn&#8217;t support a recovery or dump method. <i>DEV</i> &#8211; specifies the devlink device.<br />
 <i>DEV/PORT_INDEX</i> &#8211; specifies the devlink port. <i>REPORTER</i> &#8211; specifies the reporter&#8217;s name registered on specified devlink device or port.</p>
<dl>
<dt><code>grace_period</code><i> MSEC </i></p>
<dd>Time interval between consecutive auto recoveries.</p>
<dt><code>auto_recover</code> { <code>true</code> | <code>false</code> }</p>
<dd>Indicates whether the devlink should execute automatic recover on error.</p>
<dt><code>auto_dump</code> { <code>true</code> | <code>false</code> }</p>
<dd>Indicates whether the devlink should execute automatic dump on error. </p>
<h2>Examples</h2>
<p>devlink health show</p>
<dl>
<dd>List status and configuration of available reporters on devices and ports.</dl>
<p> devlink health show pci/0000:00:09.0/1 reporter tx</p>
<dl>
<dd>List status and configuration of tx reporter registered on port on pci/0000:00:09.0/1</dl>
<p> devlink health recover pci/0000:00:09.0 reporter fw_fatal</p>
<dl>
<dd>Initiate recovery on fw_fatal reporter registered on device on pci/0000:00:09.0.</dl>
<p> devlink health recover pci/0000:00:09.0/1 reporter tx</p>
<dl>
<dd>Initiate recovery on tx reporter registered on port on pci/0000:00:09.0/1.</dl>
<p> devlink health diagnose pci/0000:00:09.0 reporter fw</p>
<dl>
<dd>List diagnostics data on the specified device and reporter.</dl>
<p> devlink health dump show pci/0000:00:09.0/1 reporter tx</p>
<dl>
<dd>Display the last saved dump on the specified port and reporter.</dl>
<p> devlink health dump clear pci/0000:00:09.0/1 reporter tx</p>
<dl>
<dd>Delete saved dump on the specified port and reporter.</dl>
<p> devlink health set pci/0000:00:09.0 reporter fw_fatal grace_period 3500</p>
<dl>
<dd>Set time interval between auto recoveries to minimum of 3500 msec on the specified device and reporter.</dl>
<p> devlink health set pci/0000:00:09.0/1 reporter tx grace_period 3500</p>
<dl>
<dd>Set time interval between auto recoveries to minimum of 3500 msec on the specified port and reporter.</dl>
<p> devlink health set pci/0000:00:09.0 reporter fw_fatal auto_recover false</p>
<dl>
<dd>Turn off auto recovery on the specified device and reporter. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-devlink/">devlink</a></code>(8), <code><a href="/docs/linux/man/8-devlink-dev/">devlink-dev</a></code>(8), <code><a href="/docs/linux/man/8-devlink-port/">devlink-port</a></code>(8), <code><a href="/docs/linux/man/8-devlink-param/">devlink-param</a></code>(8), <code><a href="/docs/linux/man/8-devlink-region/">devlink-region</a></code>(8), </p>
<h2>Author</h2>
<p>Aya Levin &lt;ayal [at] mellanox.com&gt;</p>
