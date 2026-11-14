---
title: "remote-viewer(1)"
name: "remote-viewer"
section: "1"
letter: "r"
url: "/docs/linux/man/1-remote-viewer/"
description: "remote-viewer – a simple remote desktop client"
---

<h2 class="name">NAME</h2>
<p> remote-viewer &#8211; a simple remote desktop client </p>
<h2>SYNOPSIS</h2>
<p> <code>remote-viewer</code> [<font SIZE="-1">OPTIONS</font>] &#8212; [<font SIZE="-1">URI</font>]</p>
<h2>DESCRIPTION</h2>
<p> <code>remote-viewer</code> is a simple remote display client. The supported protocols are <font SIZE="-1">SPICE</font> and <font SIZE="-1">VNC.</font> </p>
<p> Starting remote-viewer without <font SIZE="-1">URI</font> will open a simple dialog with an entry and a list of previously successfully accessed <font SIZE="-1">URI.</font> </p>
<p> The <font SIZE="-1">URI</font> can also point to a connection settings file, see the <font SIZE="-1">CONNECTION FILE</font> section for a description of the format.</p>
<h2>OPTIONS</h2>
<p> The following options are accepted when running <tt>&quot;remote-viewer&quot;</tt>:</p>
<dl>
<dt>-h, &#8211;help</p>
<dd> Display command line help summary</p>
<dt>-V, &#8211;version</p>
<dd> Display program version number</p>
<dt>-v, &#8211;verbose</p>
<dd> Display information about the connection</p>
<dt>-z <font SIZE="-1">PCT,</font> &#8211;zoom=PCT</p>
<dd> Zoom level of the display window in percentage. Range 10-400.</p>
<dt>-f, &#8211;full-screen</p>
<dd> Start with the windows maximized to fullscreen. </p>
<p> If supported, the remote display will be reconfigured to match the physical client monitor configuration, by enabling or disabling extra monitors as necessary. This is currently implemented by the Spice backend only. </p>
<p> To specify which client monitors are used in fullscreen mode, see the <font SIZE="-1">CONFIGURATION</font> section below.</p>
<dt>-t <font SIZE="-1">TITLE,</font> &#8211;title <font SIZE="-1">TITLE</font></p>
<dd> Set the window title to <font SIZE="-1"><code>TITLE</code></font></p>
<dt>&#8211;spice-controller</p>
<dd> Use the <font SIZE="-1">SPICE</font> controller to initialize the connection with the <font SIZE="-1">SPICE</font> server. This option is used by the <font SIZE="-1">SPICE</font> browser addons to allow web page to start a client.</p>
<dt>&#8211;debug</p>
<dd> Print debugging information</p>
<dt>-H <font SIZE="-1">HOTKEYS,</font> &#8211;hotkeys <font SIZE="-1">HOTKEYS</font></p>
<dd> Set global hotkey bindings. By default, keyboard shortcuts only work when the guest display widget does not have focus. Any actions specified in <font SIZE="-1"><code>HOTKEYS</code></font> will be effective even when the guest display widget has input focus. The format for <font SIZE="-1"><code>HOTKEYS</code></font> is &lt;action1&gt;=&lt;key1&gt;[+&lt;key2&gt;][,&lt;action2&gt;=&lt;key3&gt;[+&lt;key4&gt;]]. Key-names are case-insensitive. Valid actions are: toggle-fullscreen, release-cursor, secure-attention, smartcard-insert and smartcard-remove. The <tt>&quot;secure-attention&quot;</tt> action sends a secure attention sequence (Ctrl+Alt+Del) to the guest. Examples: </p>
<pre>
  --hotkeys=toggle-fullscreen=shift+f11,release-cursor=shift+f12
  --hotkeys=release-cursor=ctrl+alt
</pre>
<p> Note that hotkeys for which no binding is given are disabled. Although the hotkeys specified here are handled by the client, it is still possible to send these key combinations to the guest via a menu item.</p>
<dt>-k, &#8211;kiosk</p>
<dd> Start in kiosk mode. In this mode, the application will start in fullscreen with minimal <font SIZE="-1">UI.</font> It will prevent the user from quitting or performing any interaction outside of usage of the remote desktop session. </p>
<p> Note that it can&#8217;t offer a complete secure solution by itself. Your kiosk system must have additional configuration and security settings to lock down the <font SIZE="-1">OS.</font> In particular, you must configure or disable the window manager, limit the session capabilities, use some restart/watchdog mechanism, disable <font SIZE="-1">VT</font> switching etc.</p>
<dt>&#8211;kiosk-quit &lt;never|on-disconnect&gt;</p>
<dd> By default, when kiosk mode is enabled, virt-viewer will remain open when the connection to the remote server is terminated. By setting kiosk-quit option to &#8220;on-disconnect&#8221; value, virt-viewer will quit instead.</dl>
<h2>HOTKEY</h2>
<p> A key binding combination is described by a series of key strings separated by &#8216;+&#8217; that must be pressed together in order to activate the associated action. </p>
<p> It must be composed of modifiers (shift, ctrl or alt) and a non-modifier key. For example, &#8220;shift+f11&#8221;.</p>
<h2>CONNECTION FILE</h2>
<p> <code>remote-viewer</code> connection file is of <font SIZE="-1">INI</font> file format, with a mandatory [virt-viewer] group and &#8220;type&#8221; key.</p>
<h3>Example</h3>
<p> Opening a file with the following content will start remote-viewer in fullscreen and connect to the host &#8220;betsiboka&#8221; using the <font SIZE="-1">SPICE</font> protocol: </p>
<pre>
 [virt-viewer]
 type=spice
 host=betsiboka
 port=5900
 fullscreen=1
</pre>
<h3>Key list</h3>
<dl>
<dt>&quot;version&quot; (string)</p>
<dd> If remote-viewer version number isn&#8217;t greater or equal to the required version, an error is raised with the expected version. </p>
<p> The version format accepted is a list of integers separated by &#8216;.&#8217;. It can be followed by a dash &#8216;-&#8216; and an additional build number with the same format. </p>
<p> Version comparison is done by comparing each integer from the list one by one. If any of the component is not a number, the version comparison will fail and consider that the 2 versions are considered to be the same.</p>
<dt>&quot;versions&quot; (osid:version list)</p>
<dd> This is a list of osid:version couples separated by &#8216;;&#8217;. osid is an arbitrary string, version is a version number in the same format as in the &#8216;version&#8217; field. A given couple indicates that remote-viewer builds matching the given &#8216;osid&#8217; (fedora22, debian7, &#8230;) must be at least version &#8216;version&#8217;. For consistency, it&#8217;s recommended to use libosinfo <font SIZE="-1">OS</font> shortids as the osid.</p>
<dt>&quot;newer-version-url&quot; (string)</p>
<dd> If specified, this field is an <font SIZE="-1">URL</font> which will be displayed to the user when a version check fails.</p>
<dt>&quot;type&quot; (string, mandatory)</p>
<dd> The session type, either &#8220;spice&#8221;, &#8220;vnc&#8221; or &#8220;ovirt&#8221;.</p>
<dt>&quot;host&quot; (string, mandatory)</p>
<dd> The server host to connect to.</p>
<dt>&quot;port&quot; (integer)</p>
<dd> The server port to connect to.</p>
<dt>&quot;tls-port&quot; (integer)</p>
<dd> The server <font SIZE="-1">TLS/SSL</font> port to connect to.</p>
<dt>&quot;username&quot; (string)</p>
<dd> The username for the session authentication.</p>
<dt>&quot;password&quot; (string)</p>
<dd> The password for the session authentication.</p>
<dt>&quot;disable-channels&quot; (string list)</p>
<dd> The list of session channels to disable. </p>
<p> The current <font SIZE="-1">SPICE</font> channels are: main, display, inputs, cursor, playback, record, smartcard, usbredir.</p>
<dt>&quot;tls-ciphers&quot; (string)</p>
<dd> Set the cipher list to use for the secure connection, in textual OpenSSL cipher list format. (see <i><a href="/docs/linux/man/1-ciphers/">ciphers</a></i>(1))</p>
<dt>&quot;title&quot; (string)</p>
<dd> String to present in the window title.</p>
<dt>&quot;fullscreen&quot; (boolean)</p>
<dd> Opens the client windows in fullscreen.</p>
<dt>&quot;ca&quot; (string)</p>
<dd> <font SIZE="-1">CA</font> certificate in <font SIZE="-1">PEM</font> format (using &#8220;
&#8221; to separate the lines). This will be used to verify the <font SIZE="-1">SSL</font> certificate used for <font SIZE="-1">SPICE TLS</font> sessions.</p>
<dt>&quot;host-subject&quot; (string)</p>
<dd> Verify the certificate subject matches with the given subject.</p>
<dt>&quot;toggle-fullscreen&quot; (hotkey string)</p>
<dd> Key binding for entering and leaving fullscreen mode. (see <font SIZE="-1">HOTKEY</font> for description of expected string)</p>
<dt>&quot;release-cursor&quot; (hotkey string)</p>
<dd> Key binding for releasing cursor grab. (see <font SIZE="-1">HOTKEY</font> for description of expected string)</p>
<dt>&quot;smartcard-insert&quot; (hotkey string)</p>
<dd> Key binding for inserting emulated smartcard. (see <font SIZE="-1">HOTKEY</font> for description of expected string)</p>
<dt>&quot;smartcard-remove&quot; (hotkey string)</p>
<dd> Key binding for removing emulated smartcard. (see <font SIZE="-1">HOTKEY</font> for description of expected string)</p>
<dt>&quot;color-depth&quot; (integer)</p>
<dd> Set the color depth of the guest display (16 or 32).</p>
<dt>&quot;disable-effects&quot; (string list)</p>
<dd> A list of desktop effects to disable in the remote guest. </p>
<p> The effects that can be disabled with <font SIZE="-1">SPICE</font> are: wallpaper, font-smooth, animation or all.</p>
<dt>&quot;enable-smartcard&quot; (boolean)</p>
<dd> Set to 1 to enable client smartcard redirection.</p>
<dt>&quot;enable-usbredir&quot; (boolean)</p>
<dd> Set to 1 to enable client <font SIZE="-1">USB</font> device redirection.</p>
<dt>&quot;enable-usb-autoshare&quot; (boolean)</p>
<dd> Set to 1 to enable client <font SIZE="-1">USB</font> devices auto-sharing.</p>
<dt>&quot;usb-filter&quot; (string)</p>
<dd> Set a string specifying a filter to use to determine which <font SIZE="-1">USB</font> devices to autoconnect when plugged in, a filter consists of one or more rules. Where each rule has the form of: </p>
<p> <tt>&quot;class,vendor,product,version,allow&quot;</tt> </p>
<p> Use -1 for class/vendor/product/version to accept any value. </p>
<p> And the rules themselves are concatenated like this: </p>
<p> <tt>&quot;rule1|rule2|rule3&quot;</tt></p>
<dt>&quot;secure-channels&quot; (string list)</p>
<dd> The list of session channels to secure. </p>
<p> The current <font SIZE="-1">SPICE</font> channels are: main, display, inputs, cursor, playback, record, smartcard, usbredir.</p>
<dt>&quot;delete-this-file&quot; (boolean)</p>
<dd> Set to 1 for the client to remove this connection file (if it can&#8217;t, it will fail silently)</p>
<dt>&quot;proxy&quot; (string)</p>
<dd> A proxy <font SIZE="-1">URL</font> to tunnel the connection through. </p>
<p> At the time of writing this documentation, the only supported proxy method with Spice is <font SIZE="-1">HTTP CONNECT.</font> </p>
<p> For example, to tunnel connection through foobar host <font SIZE="-1">HTTP</font> proxy on port 8080, use the value &#8220;<a rel="nofollow" href="http://foobar:8080''.">http://foobar:8080&#8221;.</a></dl>
<h3>oVirt Support</h3>
<p> The connection file can also carry some oVirt-specific options when oVirt support is compiled in. These options are used to interact with oVirt <font SIZE="-1">REST API.</font> This is currently only used in order to show a menu allowing to change the <font SIZE="-1">CD</font> image being used by the virtual machine from remote-viewer user interface. These options go in an optional [ovirt] group.</p>
<dl>
<dt>&quot;host&quot; (string, mandatory)</p>
<dd> The oVirt instance to connect to. This corresponds to the hostname one would connect to access the oVirt user or admin portal.</p>
<dt>&quot;vm-guid&quot; (string, mandatory)</p>
<dd> <font SIZE="-1">GUID</font> of the oVirt virtual machine to connect to.</p>
<dt>&quot;jsessionid&quot; (string)</p>
<dd> Value to set the &#8216;jsessionid&#8217; cookie to. With oVirt 3.6, setting this authentication cookie to a valid value will allow to interact with the oVirt <font SIZE="-1">REST API</font> without being asked for credentials.</p>
<dt>&quot;sso-token&quot; (string)</p>
<dd> Value to set the &#8216;Authorization&#8217; header to. With oVirt 4.0 or newer, setting this authentication header to a valid value will allow to interact with the oVirt <font SIZE="-1">REST API</font> without being asked for credentials.</p>
<dt>&quot;ca&quot; (string)</p>
<dd> <font SIZE="-1">CA</font> certificate in <font SIZE="-1">PEM</font> format (using &#8220;
&#8221; to separate the lines). This will be used to validate the certificate used for the oVirt <font SIZE="-1">REST</font> https session remote-viewer will establish.</dl>
<h2>CONFIGURATION</h2>
<p> A small number of configuration options can be controlled by editing the settings file located in the user configuration directory: </p>
<pre>
    &lt;USER-CONFIG-DIR&gt;/virt-viewer/settings
</pre>
<p> This file is a text file in <font SIZE="-1">INI</font> format, with application options in the [virt-viewer] group and per-guest options in a group identified by the guest&#8217;s <font SIZE="-1">UUID.</font> The application options should not be edited manually. There is also a special [fallback] group which specifies options for all guests that don&#8217;t have an explicit group. </p>
<p> For each guest, the initial fullscreen monitor configuration can be specified by using the <code>monitor-mapping</code> key. This configuration only takes effect when the -f/&#8211;full-screen option is specified. </p>
<p> The value of this key is a list of mappings between a guest display and a client monitor. Each mapping is separated by a semicolon character, and the mappings have the format &lt;<font SIZE="-1">GUEST-DISPLAY-ID</font>&gt;:&lt;<font SIZE="-1">CLIENT-MONITOR-ID</font>&gt;. </p>
<p> For example, to map guest displays 1 and 2 to client monitors 2 and 3 for the guest with a <font SIZE="-1">UUID</font> of e4591275-d9d3-4a44-a18b-ef2fbc8ac3e2, use: </p>
<pre>
    [e4591275-d9d3-4a44-a18b-ef2fbc8ac3e2]
    monitor-mapping=1:2;2:3
</pre>
<h2>EXAMPLES</h2>
<p> To connect to <font SIZE="-1">SPICE</font> server on host &#8220;makai&#8221; with port 5900 </p>
<pre>
   remote-viewer <a href="spice://makai:5900">spice://makai:5900</a>
</pre>
<p> To connect to <font SIZE="-1">VNC</font> server on host &#8220;tsingy&#8221; with port 5900 </p>
<pre>
   remote-viewer <a href="vnc://tsingy:5900">vnc://tsingy:5900</a>
</pre>
<p> To connect to a virtual machine named &#8220;toliara&#8221; on an oVirt server at example.org </p>
<pre>
   remote-viewer <a href="ovirt://[username@]example.org/toliara">ovirt://[username@]example.org/toliara</a>
</pre>
<h2>BUGS</h2>
<p> Report bugs to the mailing list <tt>&quot;<a rel="nofollow" href="http://www.redhat.com/mailman/listinfo/virt-tools-list">http://www.redhat.com/mailman/listinfo/virt-tools-list</a>&quot;</tt></p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2012-2014 Red Hat, Inc., and various contributors. This is free software. You may redistribute copies of it under the terms of the <font SIZE="-1">GNU</font> General Public License <tt>&quot;<a rel="nofollow" href="https://www.gnu.org/licenses/gpl-2.0.html">https://www.gnu.org/licenses/gpl-2.0.html</a>&quot;</tt>. There is <font SIZE="-1">NO WARRANTY,</font> to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <tt>&quot;<a href="/docs/linux/man/1-virt-viewer/">virt-viewer</a>(1)&quot;</tt>, the project website <tt>&quot;<a rel="nofollow" href="http://virt-manager.org">http://virt-manager.org</a>&quot;</tt> </p>
<h2>Index</h2>
