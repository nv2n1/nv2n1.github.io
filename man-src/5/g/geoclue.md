---
title: "geoclue(5)"
name: "geoclue"
section: "5"
letter: "g"
url: "/docs/linux/man/5-geoclue/"
description: "geoclue.conf – geoclue configuration parameters"
---

<p>geoclue.conf &#8211; geoclue configuration parameters</p>
<h2>Synopsis</h2>
<p><code>/etc/geoclue/geoclue.conf</code></p>
<h2>Description</h2>
<p>The geoclue geoclue.conf configuration file specifies parameters that control the operation of geoclue. </p>
<p> All configurations settings below are mandatory and the defaults are what you see before you edit them in geoclue.conf. If you want to keep the default values around, copy and comment out the appropriate line(s) before changing them.</p>
<h2>Agent Configuration Options</h2>
<p><i>[agent]</i> is used to begin the agent configuration.</p>
<dl>
<dt><code>whitelist</p>
<dd>Whitelist of desktop IDs (without .desktop part) of all agents we recognise, separated by a &#8216;;&#8217;.</p>
<dd>whitelist=geoclue-demo-agent;gnome-shell;io.elementary.desktop.agent-geoclue2</code> </p>
<dt><code>[network-nmea]</p>
<dd>Network NMEA source configuration options</p>
<dd>enable=true </code><br />
 Fetch location from NMEA sources on local network? </p>
<dt><code>[3G]</p>
<dd>3G source configuration options</p>
<dd>enable=true </code><br />
 Enable 3G source </p>
<dt><code>[cdma]</p>
<dd>CDMA source configuration options</p>
<dd>enable=true </code><br />
 Enable CDMA source </p>
<dt><code>[modem-gps]</p>
<dd>Modem GPS source configuration options</p>
<dd>enable=true </code><br />
 Enable Modem-GPS source </p>
<dt><code>[wifi]</p>
<dd>WiFi source configuration options</p>
<dd>enable=true </code><br />
 Enable WiFi source</p>
<dd><code>url=</code><i><a rel="nofollow" href="https://location.services.mozilla.com/v1/geolocate?key=geoclue">https://location.services.mozilla.com/v1/geolocate?key=geoclue</a></i><br />
 URL to the wifi geolocation service. The key can currenty be anything, just needs to be present but that is likely going to change in future.</p>
<dd><code>submit-data=false</code> Submit data to Mozilla Location Service<br />
 If set to true, geoclue will automatically submit network data to Mozilla each time it gets a GPS lock.</p>
<dd><code>submission-url=</code><i><a rel="nofollow" href="https://location.services.mozilla.com/v1/submit?key=geoclue">https://location.services.mozilla.com/v1/submit?key=geoclue</a></i><br />
 URL to submission API of Mozilla Location Service</p>
<dd><code>submission-nick=geoclue</code><br />
 A nickname to submit network data with. A nickname must be 2-32 characters long.
</dl>
<h2>Application Configuration Options</h2>
<p>Having an entry here for an application with <code>allowed=true</code> means that geoclue will not ask agent to authorize the application. This is to ensure that applications with built-in authorization mechanism (e.g web browsers) do not have to be bound to agents. </p>
<p> If your application is denied access to location information and your operating system doesn&#8217;t provide any mechanism to change that, it is likely a bug in your operation system (or geoclue). The solution is to report the issue with all details, rather than adding your application to this list.</p>
<dl>
<dt>Format:</p>
<dd>
<dl>
<dd><code>[random-app]</code><br />
 Desktop ID of application without .desktop part </p>
<p> <code>allowed=true|false</code><br />
 Allowed access to location information? </p>
<p> <code>system=true|false</code><br />
 Is application a system component? </p>
<p> <code>users=</code><br />
 List of UIDs of all users for which this application is allowed location info access, separate by &#8216;;&#8217;. Keep it empty for allowing it for all users.</dl>
<dt>Examples:</p>
<dd>
<dl>
<dd><code>[gnome-datetime-panel]</code><br />
 allowed=true<br />
 system=true<br />
 users= </p>
<p> <code>[gnome-color-panel]</code><br />
 allowed=true<br />
 system=true<br />
 users= </p>
<p> <code>[org.gnome.Shell]</code><br />
 allowed=true<br />
 system=true<br />
 users= </p>
<p> <code>[io.elementary.desktop.agent-geoclue2]</code><br />
 allowed=true<br />
 system=true<br />
 users= </p>
<p> <code>[epiphany]</code><br />
 allowed=true<br />
 system=false<br />
 users= </p>
<p> <code>[firefox]</code><br />
 allowed=true<br />
 system=false<br />
 users=
</dl>
</dl>
<h2>Author</h2>
<pre>Sachin Chand</pre>
