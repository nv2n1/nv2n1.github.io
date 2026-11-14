---
title: "stonith_admin(8)"
name: "stonith_admin"
section: "8"
letter: "s"
url: "/docs/linux/man/8-stonith_admin/"
description: "Pacemaker – Part of the Pacemaker cluster resource manager"
---

<p>Pacemaker &#8211; Part of the Pacemaker cluster resource manager</p>
<h2>Synopsis</h2>
<p><code>stonith_admin</code> <i>mode </i>[<i>options</i>]</p>
<h2>Description</h2>
<p>stonith_admin &#8211; Provides access to the stonith-ng API. </p>
<p> Allows the administrator to add/remove/list devices, check device and host status and fence hosts</p>
<h2>Options</h2>
<dl>
<dt>-?, <code>&#8211;help</code></p>
<dd>This text</p>
<dt>-$, <code>&#8211;version</code></p>
<dd>Version information</p>
<dt><code>-V</code>, <code>&#8211;verbose</code></p>
<dd>Increase debug output</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd>Print only essential output</dl>
<h3>Commands:</h3>
<dl>
<dt><code>-l</code>, <code>&#8211;list</code>=<i>value</i></p>
<dd>List devices that can terminate the specified host</p>
<dt><code>-L</code>, <code>&#8211;list-registered</code></p>
<dd>List all registered devices</p>
<dt><code>-I</code>, <code>&#8211;list-installed</code></p>
<dd>List all installed devices</p>
<dt> <code>-M</code>, <code>&#8211;metadata</code> Check the device&#8217;s metadata</p>
<dt><code>-Q</code>, <code>&#8211;query</code>=<i>value</i></p>
<dd>
<dd>Check the device&#8217;s status</p>
<dt><code>-F</code>, <code>&#8211;fence</code>=<i>value</i></p>
<dd>Fence the named host</p>
<dt><code>-U</code>, <code>&#8211;unfence</code>=<i>value</i></p>
<dd>Unfence the named host</p>
<dt><code>-B</code>, <code>&#8211;reboot</code>=<i>value</i></p>
<dd>Reboot the named host</p>
<dt><code>-C</code>, <code>&#8211;confirm</code>=<i>value</i></p>
<dd>Confirm the named host is now safely down</p>
<dt><code>-H</code>, <code>&#8211;history</code>=<i>value</i></p>
<dd>Retrieve last fencing operation for specified node (or &#8216;*&#8217; for all)</p>
<dt><code>-h</code>, <code>&#8211;last</code>=<i>value</i></p>
<dd>Indicate when the named node was last fenced. Optional: <code>&#8211;as-node-id</code></p>
<dt><code>-R</code>, <code>&#8211;register</code>=<i>value</i></p>
<dd>Register the named stonith device. Requires: <code>&#8211;agent</code>, optional: <code>&#8211;option</code></p>
<dt> <code>-D</code>, <code>&#8211;deregister</code>=<i>value</i> De-register the named stonith device</p>
<dt><code>-r</code>, <code>&#8211;register-level</code>=<i>value</i></p>
<dd>
<dd>Register a stonith level for the named target, specified as one of:</p>
<dd>NAME, @PATTERN, or ATTR=VALUE. Requires: <code>&#8211;index</code>, one or more <code>&#8211;device</code> entries</p>
<dt><code>-d</code>, <code>&#8211;deregister-level</code>=<i>value</i></p>
<dd>De-register a stonith level for the named target</p>
<dd>Target is specified as for <code>&#8211;register-level</code>. Requires: <code>&#8211;index</code></dl>
<h3>Options and modifiers:</h3>
<dl>
<dt><code>-a</code>, <code>&#8211;agent</code>=<i>value</i></p>
<dd>The agent (eg. fence_xvm) to instantiate when calling with <code>&#8211;register</code></p>
<dt> <code>-e</code>, <code>&#8211;env-option</code>=<i>value</i></p>
<dt> <code>-o</code>, <code>&#8211;option</code>=<i>value</i></p>
<dt><code>-T</code>, <code>&#8211;tag</code>=<i>value</i></p>
<dd>
<dd>Identify fencing operations with the specified tag.</p>
<dd>Useful when there are multiple entities that might be invoking <a href="/docs/linux/man/8-stonith_admin/">stonith_admin</a>(8)</p>
<dt><code>-v</code>, <code>&#8211;device</code>=<i>value</i></p>
<dd>A device to associate with a given host and stonith level</p>
<dt><code>-i</code>, <code>&#8211;index</code>=<i>value</i></p>
<dd>The stonith level (1-9)</p>
<dt><code>-t</code>, <code>&#8211;timeout</code>=<i>value</i></p>
<dd>Operation timeout in seconds</p>
<dt><code>-n</code>, <code>&#8211;as-node-id</code></p>
<dd>(Advanced) The supplied node is the corosync nodeid (Only for use with <code>&#8211;last</code>)</p>
<dt><code>&#8211;tolerance</code>=<i>value</i></p>
<dd>(Advanced) Do nothing if an equivalent <code>&#8211;fence</code> request succeeded less than N seconds earlier</p>
<dt> <code>-L</code>, <code>&#8211;list-all</code> legacy alias for <code>&#8211;list-registered</code></dl>
<h2>Author</h2>
<dd>Written by Andrew Beekhof</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to pacemaker [at] oss.clusterlabs.org</p>
