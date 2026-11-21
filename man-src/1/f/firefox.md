---

title: "firefox(1)"
name: "firefox"
section: "1"
letter: "f"
url: "/docs/linux/man/1-firefox/"
description: "firefox – a free and open source web browser from Mozilla"
---

<p> firefox &#8211; a free and open source web browser from Mozilla</p>
<h2>SYNOPSIS</h2>
<p> <code>firefox</code> [<i>OPTIONS</i>] [<i>url</i>] </p>
<h2>DESCRIPTION</h2>
<p> See <a rel="nofollow" href="http://support.mozilla.com/">http://support.mozilla.com/</a> for help using the browser. This manpage only describes how to run it. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd> Prints the command line options.</dd>
<dt><code>-g, &#8211;debug</code></dt>
<dd> Starts <code>firefox</code> in a debugger.</dd>
<dt><code>-d, &#8211;debugger</code></dt>
<dd> Specify the debugger in which to start <code>firefox</code>. The default is gdb. Used in conjunction with <code>-g</code>.</dd>
<dt><code>-a, &#8211;debugger-args</code></dt>
<dd> Specify arguments to pass to the debugger. Used in conjunction with <code>-g</code>.</dd>
<dt><code>-no-remote</code></dt>
<dd> Don&#8217;t connect to any other running instances of <code>firefox</code>. Use this if you want to run <code>firefox</code> in an entirely new process. By default, <code>firefox</code> will delegate a command to an already running instance.</dd>
<dt><code>-ProfileManager</code></dt>
<dd> Start the profilemanager. Use this to choose the profile you would like to run <code>firefox</code> with. You will need to also use <code>-no-remote</code> if there is already a running <code>firefox</code> instance.</dd>
<dt><code>-P</code> <i>profile</i></dt>
<dd> Start <code>firefox</code> with the profile named <i>profile</i>. Will start the profile manager if a valid profile name is not specified. You will need to also use <code>-no-remote</code> if there is already a running <code>firefox</code> instance.</dd>
<dt><code>-safe-mode</code></dt>
<dd> Start <code>firefox</code> in safe-mode. This disables all third-party extensions, and may be necessary if you are having problems with an extension you installed.</dd>
<dt><code>-new-tab</code> <i>url</i></dt>
<dd> Open <i>url</i> in a new tab.</dd>
<dt><code>-new-window</code> <i>url</i></dt>
<dd> Open <i>url</i> in a new window.</dd>
<dt><code>-v, -version</code></dt>
<dd> Print the current version of <code>firefox</code>.</dd>
<dt><code>-UILocale</code> <i>locale</i></dt>
<dd> Start <code>firefox</code> with the specified locale <i>locale</i>. Use this to override your environment</dd>
<dt><code>-preferences</code></dt>
<dd> Open the preferences dialog.</dd>
<dt><code>-private</code></dt>
<dd> Start <code>firefox</code> in private browsing mode</dd>
<dt><code>-private-toggle</code></dt>
<dd> Toggle private browsing mode</dd>
<dt><code>-setDefaultBrowser</code></dt>
<dd> Set <code>firefox</code> as the default web browser</dd>
<dt><code>-search</code> <i>term</i></dt>
<dd> Search for <i>term</i> with your default search engine</dd>
<dt><code>-jsconsole</code></dt>
<dd> Open the Error console. If <code>firefox</code> is not already running, this will open a new browser window too </dd>
</dl>
