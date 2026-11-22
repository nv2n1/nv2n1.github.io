---

title: "virt-viewer(1)"
name: "virt-viewer"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virt-viewer/"
description: "virt-viewer – display the graphical console for a virtual machine"
---

<p> virt-viewer &#8211; display the graphical console for a virtual machine </p>
<h2>SYNOPSIS</h2>
<p> <code>virt-viewer</code> [OPTIONS] &#8212; DOMAIN-NAME|ID|UUID</p>
<h2>DESCRIPTION</h2>
<p> <code>virt-viewer</code> is a minimal tool for displaying the graphical console of a virtual machine. The console is accessed using the VNC or SPICE protocol. The guest can be referred to based on its name, ID, or UUID. If the guest is not already running, then the viewer can be told to wait until it starts before attempting to connect to the console. The viewer can connect to remote hosts to lookup the console information and then also connect to the remote console using the same network transport.</p>
<h2>OPTIONS</h2>
<p> The following options are accepted when running <tt>&quot;virt-viewer&quot;</tt>:</p>
<dl>
<dt>-h, &#8211;help</dt>
<dd> Display command line help summary</dd>
<dt>-V, &#8211;version</dt>
<dd> Display program version number</dd>
<dt>-v, &#8211;verbose</dt>
<dd> Display information about the connection</dd>
<dt>-c URI, &#8211;connect=URI</dt>
<dd> Specify the hypervisor connection URI</dd>
<dt>-w, &#8211;wait</dt>
<dd> Wait for the domain to start up before attempting to connect to the console</dd>
<dt>-r, &#8211;reconnect</dt>
<dd> Automatically reconnect to the domain if it shuts down and restarts</dd>
<dt>-z PCT, &#8211;zoom=PCT</dt>
<dd> Zoom level of the display window in percentage. Range 10-400.</dd>
<dt>-d, &#8211;direct</dt>
<dd> Do not attempt to tunnel the console over SSH, even if the main connection URI used SSH.</dd>
<dt>-a, &#8211;attach</dt>
<dd> Instead of making a direct TCP/UNIX socket connection to the remote display, ask libvirt to provide a pre-connected socket for the display. This avoids the need to authenticate with the remote display server directly. This option will only work when connecting to a guest that is running on the same host as the virt-viewer program. If attaching to the guest via libvirt fails, virt-viewer will automatically fallback to trying a regular direct TCP/UNIX socket connection.</dd>
<dt>-f, &#8211;full-screen</dt>
<dd> Start with the window maximised to fullscreen </dd>
<p> If supported, the remote display will be reconfigured to match the physical client monitor configuration, by enabling or disabling extra monitors as necessary. This is currently implemented by the Spice backend only. </p>
<p> To specify which client monitors are used in fullscreen mode, see the CONFIGURATION section below.</p>
<dt>&#8211;debug</dt>
<dd> Print debugging information</dd>
<dt>-H HOTKEYS, &#8211;hotkeys HOTKEYS</dt>
<dd> Set global hotkey bindings. By default, keyboard shortcuts only work when the guest display widget does not have focus. Any actions specified in <code>HOTKEYS</code> will be effective even when the guest display widget has input focus. The format for <code>HOTKEYS</code> is &lt;action1&gt;=&lt;key1&gt;[+&lt;key2&gt;][,&lt;action2&gt;=&lt;key3&gt;[+&lt;key4&gt;]]. Key-names are case-insensitive. Valid actions are: toggle-fullscreen, release-cursor, secure-attention, smartcard-insert and smartcard-remove. The <tt>&quot;secure-attention&quot;</tt> action sends a secure attention sequence (Ctrl+Alt+Del) to the guest. Examples: </dd>
<pre>
  --hotkeys=toggle-fullscreen=shift+f11,release-cursor=shift+f12
  --hotkeys=release-cursor=ctrl+alt
</pre>
<p> Note that hotkeys for which no binding is given are disabled. Although the hotkeys specified here are handled by the client, it is still possible to send these key combinations to the guest via a menu item.</p>
<dt>-k, &#8211;kiosk</dt>
<dd> Start in kiosk mode. In this mode, the application will start in fullscreen with minimal UI. It will prevent the user from quitting or performing any interaction outside of usage of the remote desktop session. </dd>
<p> Note that it can&#8217;t offer a complete secure solution by itself. Your kiosk system must have additional configuration and security settings to lock down the OS. In particular, you must configure or disable the window manager, limit the session capabilities, use some restart/watchdog mechanism, disable VT switching etc.</p>
<dt>&#8211;kiosk-quit &lt;never|on-disconnect&gt;</dt>
<dd> By default, when kiosk mode is enabled, virt-viewer will remain open when the connection to the remote server is terminated. By setting kiosk-quit option to &#8220;on-disconnect&#8221; value, virt-viewer will quit instead. Please note that &#8211;reconnect takes precedence over this option, and will attempt to do a reconnection before it quits.</dd></dl>
<h2>CONFIGURATION</h2>
<p> A small number of configuration options can be controlled by editing the settings file located in the user configuration directory: </p>
<pre>
    &lt;USER-CONFIG-DIR&gt;/virt-viewer/settings
</pre>
<p> This file is a text file in INI format, with application options in the [virt-viewer] group and per-guest options in a group identified by the guest&#8217;s UUID. The application options should not be edited manually. There is also a special [fallback] group which specifies options for all guests that don&#8217;t have an explicit group. </p>
<p> For each guest, the initial fullscreen monitor configuration can be specified by using the <code>monitor-mapping</code> key. This configuration only takes effect when the -f/&#8211;full-screen option is specified. </p>
<p> The value of this key is a list of mappings between a guest display and a client monitor. Each mapping is separated by a semicolon character, and the mappings have the format &lt;GUEST-DISPLAY-ID&gt;:&lt;CLIENT-MONITOR-ID&gt;. </p>
<p> For example, to map guest displays 1 and 2 to client monitors 2 and 3 for the guest with a UUID of e4591275-d9d3-4a44-a18b-ef2fbc8ac3e2, use: </p>
<pre>
    [e4591275-d9d3-4a44-a18b-ef2fbc8ac3e2]
    monitor-mapping=1:2;2:3
</pre>
<h2>EXAMPLES</h2>
<p> To connect to the guest called &#8216;demo&#8217; running under Xen </p>
<pre>
   virt-viewer demo
</pre>
<p> To connect to the guest with ID 7 running under QEMU </p>
<pre>
   virt-viewer --connect <a href="qemu:///system">qemu:///system</a> 7
</pre>
<p> To wait for the guest with UUID 66ab33c0-6919-a3f7-e659-16c82d248521 to startup and then connect, also reconnecting upon restart of VM </p>
<pre>
   virt-viewer --reconnect --wait 66ab33c0-6919-a3f7-e659-16c82d248521
</pre>
<p> To connect to a remote console using TLS </p>
<pre>
   virt-viewer --connect <a href="xen://example.org/">xen://example.org/</a> demo
</pre>
<p> To connect to a remote host using SSH, lookup the guest config and then make a direct non-tunnelled connection of the console </p>
<pre>
   virt-viewer --direct --connect xen+<a href="ssh://root@example.org/">ssh://root@example.org/</a> demo
</pre>
<h2>AUTHOR</h2>
<p> Written by Daniel P. Berrange, based on the GTK-VNC example program gvncviewer.</p>
<h2>BUGS</h2>
<p> Report bugs to the mailing list <tt>&quot;<a rel="nofollow" href="http://www.redhat.com/mailman/listinfo/virt-tools-list">http://www.redhat.com/mailman/listinfo/virt-tools-list</a>&quot;</tt></p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2007-2014 Red Hat, Inc., and various contributors. This is free software. You may redistribute copies of it under the terms of the GNU General Public License <tt>&quot;<a rel="nofollow" href="https://www.gnu.org/licenses/gpl-2.0.html">https://www.gnu.org/licenses/gpl-2.0.html</a>&quot;</tt>. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <tt><a href="/docs/linux/man/1-virsh/">virsh</a>(1)</tt>, <tt>&quot;<a href="/docs/linux/man/1-virt-manager/">virt-manager</a>(1)&quot;</tt>, the project website <tt>&quot;<a rel="nofollow" href="http://virt-manager.org">http://virt-manager.org</a>&quot;</tt> </p>
