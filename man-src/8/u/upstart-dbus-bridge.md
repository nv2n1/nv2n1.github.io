---
title: "upstart-dbus-bridge(8)"
name: "upstart-dbus-bridge"
section: "8"
letter: "u"
url: "/docs/linux/man/8-upstart-dbus-bridge/"
description: "upstart-dbus-bridge – Bridge between Upstart and D-Bus"
---

<p>upstart-dbus-bridge &#8211; Bridge between Upstart and D-Bus</p>
<h2>Synopsis</h2>
<p><code>upstart-dbus-bridge</code> [<i>OPTIONS</i>]&#8230;</p>
<h2>Description</h2>
<p><code>upstart-dbus-bridge</code> receives information about D-Bus signals and creates <code><a href="/docs/linux/man/8-init/">init</a></code>(8) events for them. With no options, monitors signals on the D-Bus system bus and emits an Upstart event called <i>dbus</i> via a D-Bus system bus connection to Upstart. When run with <code>&#8211;user</code>, monitors signals on the users D-Bus session bus and emits Upstart events via the private D-Bus connection to the users Session Init. See <code><a href="/docs/linux/man/1-dbus-daemon/">dbus-daemon</a></code>(1) and for further details. </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;always</code></p>
<dd>Always emit events on receipt of D-Bus signal regardless of whether jobs care about them.</p>
<dt><code>&#8211;daemon</code></p>
<dd>Detach and run in the background.</p>
<dt><code>&#8211;debug</code></p>
<dd>Enable debugging output.</p>
<dt><code>&#8211;help</code></p>
<dd>Show brief usage summary.</p>
<dt><code>&#8211;session</code></p>
<dd>Monitor signals on the D-Bus session bus.</p>
<dt><code>&#8211;system</code></p>
<dd>Monitor signals on the D-Bus system bus.</p>
<dt><code>&#8211;user</code></p>
<dd>User-session mode: connect to Upstart via the user session rather than over the D-Bus system bus.</p>
<dt><code>&#8211;bus-name</code></p>
<dd>Set a name for the bus to be passed as an additional argument to the event under the property BUS. Used to distinguish multiple D-Bus bridges.</p>
<dt><code>&#8211;verbose</code></p>
<dd>Enable verbose output.</dl>
<h2>Restrictions</h2>
<p>D-Bus signals emitted by Upstart itself are ignored.</p>
<h2>Author</h2>
<p>Written by James Hunt &lt;<code>james.hunt [at] canonical.com</code>&gt;</p>
<h2>Bugs</h2>
<p>Report bugs at &lt;<code><a rel="nofollow" href="https://launchpad.net/ubuntu/+source/upstart/+bugs">https://launchpad.net/ubuntu/+source/upstart/+bugs</a></code>&gt;</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2013 Canonical Ltd. </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-dbus-daemon/">dbus-daemon</a></code>(1) <code><a href="/docs/linux/man/7-dbus-event/">dbus-event</a></code>(7) <code><a href="/docs/linux/man/5-init/">init</a></code>(5) <code><a href="/docs/linux/man/8-init/">init</a></code>(8) </p>
