---

title: "xkbbell(1)"
name: "xkbbell"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xkbbell/"
description: "xkbbell – XKB extension user utility"
---

<p> <code>xkbbell</code> [-display &lt;dpy&gt;] [-synch] [-dev &lt;id&gt;] [-force] [-nobeep] [-bf &lt;id&gt;] [-kf &lt;id&gt;] [-v &lt;volume&gt;] [-w &lt;id&gt;] [-help|-version]</p>
<p> user utility</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-display &lt;dpy&gt;</code></dt>
<dd> specifies which display to use</dd>
<dt><code>-synch</code></dt>
<dd> turns on synchronization</dd></dl>
<dl>
<dt><code>-dev &lt;id&gt;</code></dt>
<dd> specifies which device to use</dd></dl>
<dl>
<dt><code>-force</code></dt>
<dd> force audible bell</dd></dl>
<dl>
<dt><code>-nobeep</code></dt>
<dd> suppress server bell, event only</dd></dl>
<dl>
<dt><code>-bf &lt;id&gt;</code></dt>
<dd> specifies which bell feedback to use</dd></dl>
<dl>
<dt><code>-kf &lt;id&gt;</code></dt>
<dd> specifies which keyboard feedback to use</dd></dl>
<dl>
<dt><code>-v &lt;volume&gt;</code></dt>
<dd> specifies which volume to use</dd></dl>
<dl>
<dt><code>-w &lt;id&gt;</code></dt>
<dd> specifies which window to use</dd></dl>
<dl>
<dt><code>-help</code></dt>
<dd> print list of options and exit</dd></dl>
<dl>
<dt><code>-version</code></dt>
<dd> print program version and exit</dd></dl>
<p> If neither device nor feedback are specified, xkbbell uses the default values for the core keyboard device. </p>
