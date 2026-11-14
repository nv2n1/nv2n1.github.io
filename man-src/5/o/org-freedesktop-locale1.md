---
title: "org-freedesktop-locale1(5)"
name: "org-freedesktop-locale1"
section: "5"
letter: "o"
url: "/docs/linux/man/5-org-freedesktop-locale1/"
description: "org.freedesktop.locale1 – The D-Bus interface of systemd-localed"
---

<p>org.freedesktop.locale1 &#8211; The D-Bus interface of systemd-localed</p>
<h2>Introduction</h2>
<p><code><a href="/docs/linux/man/8-systemd-localed-service/">systemd-localed.service</a></code>(8) is a system service that can be used to control the system locale and keyboard mapping from user programs. This page describes the D-Bus interface.</p>
<h2>The D-Bus Api</h2>
<p>The service exposes the following interfaces on the bus: </p>
<dl>
<dd>
<pre>node /org/freedesktop/locale1 {
 interface org.freedesktop.locale1 {
 methods:
 SetLocale(in as locale,
 in b interactive);
 SetVConsoleKeyboard(in s keymap,
 in s keymap_toggle,
 in b convert,
 in b interactive);
 SetX11Keyboard(in s layout,
 in s model,
 in s variant,
 in s options,
 in b convert,
 in b interactive);
 properties:
 readonly as Locale = ['...', ...];
 readonly s X11Layout = '...';
 readonly s X11Model = '...';
 readonly s X11Variant = '...';
 readonly s X11Options = '...';
 readonly s VConsoleKeymap = '...';
 readonly s VConsoleKeymapToggle = '...';
 };
 interface org.freedesktop.DBus.Peer { ... };
 interface org.freedesktop.DBus.Introspectable { ... };
 interface org.freedesktop.DBus.Properties { ... };
};</pre>
</dl>
<h3>Methods</h3>
<p>If you set a new system locale all old system locale settings will be dropped and the new settings will be saved to disk. The locale will also be passed to the system manager, and subsequently started daemons will inherit the new system locale. Note that already running daemons will not learn about the new value. </p>
<p> The <code>SetVConsoleKeyboard()</code> method may be used to set the key mapping for the virtual console. Similarly, <code>SetX11Keyboard()</code> may be used to set the default key mapping of any X11 servers. </p>
<p> Note that <code>SetVConsoleKeyboard()</code> instantly applies the new key mapping to the console, while <code>SetX11Keyboard()</code> simply sets a default that may be used by later sessions. </p>
<p> The boolean argument <i>convert</i> may be set to optionally convert the console keyboard configuration to X11 keyboard mappings and vice versa. If true and <code>SetVConsoleKeyboard()</code> is used, the nearest X11 keyboard setting for the chosen console setting is set. If true and <code>SetX11Keyboard()</code> is used, the nearest console keyboard setting for the chosen X11 setting is set. Hence, it is usually sufficient to call only one of the two functions. </p>
<p> For graphical UIs that need to set the system keyboard mapping simply invoke <code>SetX11Keyboard()</code>, set <i>convert=true</i> and ignore <code>SetVConsoleKeyboard()</code>. </p>
<p> Use the empty string for the keymap parameters you wish not to set. </p>
<p> The <i>interactive</i> boolean parameters can be used to control whether m[blue]<code>polkit</code>m[]<font SIZE="-2">[1]</font> should interactively ask the user for authentication credentials if required.</p>
<h3>Signals</h3>
<p>Whenever the system locale or keymap is changed via the daemon, <code>PropertyChanged</code> signals are sent out to which clients can subscribe.</p>
<h3>Properties</h3>
<p>The system locale is shown in the <i>Locale</i> property. It is an array containing environment-variable-assignment-like strings. The following strings are known: <i>LANG=</i>, <i>LC_CTYPE=</i>, <i>LC_NUMERIC=</i>, <i>LC_TIME=</i>, <i>LC_COLLATE=</i>, <i>LC_MONETARY=</i>, <i>LC_MESSAGES=</i>, <i>LC_PAPER=</i>, <i>LC_NAME=</i>, <i>LC_ADDRESS=</i>, <i>LC_TELEPHONE=</i>, <i>LC_MEASUREMENT=</i>, <i>LC_IDENTIFICATION=</i>. </p>
<p> The <i>X11Layout</i>, <i>X11Model</i>, <i>X11Variant</i>, and <i>X11Options</i> properties show values configurable with <code>SetX11Keyboard()</code> described above (or <code>SetVConsoleKeyboard()</code> with <i>convert=true</i>). The <i>VConsoleKeymap</i> and <i>VConsoleKeymapToggle</i> properties show values configurable with <code>SetVConsoleKeyboard()</code> (or <code>SetX11Keyboard()</code> with <i>convert=true</i>).</p>
<h3>Security</h3>
<p>Changing the system locale or keymap using this interface is authenticated via polkit. The polkit action for <code>SetLocale()</code> is <code>org.freedesktop.locale1.set-locale</code>. The polkit action for <code>SetX11Keyboard()</code> and <code>SetVConsoleKeyboard()</code> is <code>org.freedesktop.locale1.set-keyboard</code>.</p>
<h2>Examples</h2>
<p><code>Example 1. Introspect org.freedesktop.locale1 on the bus</code> </p>
<dl>
<dd>
<pre>$ gdbus introspect --system \
 --dest org.freedesktop.locale1 \
 --object-path /org/freedesktop/locale1</pre>
</dl>
<h2>Versioning</h2>
<p>These D-Bus interfaces follow m[blue]<code>the usual interface versioning guidelines</code>m[]<font SIZE="-2">[2]</font>.</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>polkit</p>
<dl>
<dd><a rel="nofollow" href="https://www.freedesktop.org/software/polkit/docs/latest/">https://www.freedesktop.org/software/polkit/docs/latest/</a></dl>
<dt> 2.</p>
<dd>the usual interface versioning guidelines</p>
<dl>
<dd><a rel="nofollow" href="http://0pointer.de/blog/projects/versioning-dbus.html">http://0pointer.de/blog/projects/versioning-dbus.html</a></dl>
