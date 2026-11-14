---
title: "passenger-status(8)"
name: "passenger-status"
section: "8"
letter: "p"
url: "/docs/linux/man/8-passenger-status/"
description: "passenger-status – inspect Phusion Passenger’s internal status"
---

<p>passenger-status &#8211; inspect Phusion Passenger&#8217;s internal status</p>
<h2>Synopsis</h2>
<p><code>passenger-status</code> [<i>pid</i>]</p>
<h2>Description</h2>
<p><code>passenger-status</code> looks at the current status of a Phusion Passenger installation. It will locate Phusion Passenger automatically if it is running and will give you a list of instances if there is more than one Phusion Passenger instance running. You can then select the instance by specifying the relevant PID on the command line. </p>
<p> The <i>general information</i> section shows the following details:</p>
<dl>
<dt>max</p>
<dd>The maximum number of application instances that Phusion Passenger will spawn. This equals the value given for <i>PassengerMaxPoolSize</i> in the configuration.</p>
<dt>count</p>
<dd>The number of application instances that are currently alive. This value is always less than or equal to <i>max</i>.</p>
<dt>active</p>
<dd>The number of application instances that are currently processing requests. This value is always less than or equal to <i>count</i>.</p>
<dt>inactive</p>
<dd>The number of application instances that are currently not processing requests, i.e. are idle. Idle application instances will be shutdown after a while, as can be specified with <i>PassengerPoolIdleTime</i> in the configuration. The value of <i>inactive</i> equals <i>count</i> &#8211; <i>active</i>.</dl>
<p> The <i>applications</i> section shows each application instance, which directory it belongs to. The <i>sessions</i> field shows how many HTTP client are currently being processed by that application instance.</p>
<h2>Options</h2>
<dl>
<dt><code>pid</code></p>
<dd>The process ID of the Phusion Passenger instance you want to look at</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-passenger-memory-stats/">passenger-memory-stats</a>(8), <a href="/docs/linux/man/1-ps/">ps</a>(1), <a href="/docs/linux/man/1-top/">top</a>(1) </p>
<p> User guide at <a rel="nofollow" href="https://www.phusionpassenger.com/documentation_and_support">https://www.phusionpassenger.com/documentation_and_support</a></p>
<h2>Author</h2>
<p>Phusion Passenger is written by Phusion (<a rel="nofollow" href="http://www.phusion.nl)">http://www.phusion.nl)</a> </p>
<p> &quot;Phusion&quot; and &quot;Phusion Passenger&quot; are trademarks of Hongli Lai &amp; Ninh Bui. </p>
<p> This manual page was written by Neil Wilson &lt;neil [at] brightbox.co.uk&gt; for the Ubuntu project (but may be used by others).</p>
