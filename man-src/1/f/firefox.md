---
title: "firefox(1)"
name: "firefox"
section: "1"
letter: "f"
url: "/docs/linux/man/1-firefox/"
description: "firefox – a free and open source web browser from Mozilla"
---

<h2 class="name">NAME</h2>
<p> firefox &#8211; a free and open source web browser from Mozilla</p>
<h2>SYNOPSIS</h2>
<p> <code>firefox</code> [<i>OPTIONS</i>] [<i>url</i>] </p>
<h2>DESCRIPTION</h2>
<p> See <a rel="nofollow" href="http://support.mozilla.com/">http://support.mozilla.com/</a> for help using the browser. This manpage only describes how to run it. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Prints the command line options.</p>
<dt><code>-g, &#8211;debug</code></p>
<dd> Starts <code>firefox</code> in a debugger.</p>
<dt><code>-d, &#8211;debugger</code></p>
<dd> Specify the debugger in which to start <code>firefox</code>. The default is gdb. Used in conjunction with <code>-g</code>.</p>
<dt><code>-a, &#8211;debugger-args</code></p>
<dd> Specify arguments to pass to the debugger. Used in conjunction with <code>-g</code>.</p>
<dt><code>-no-remote</code></p>
<dd> Don&#8217;t connect to any other running instances of <code>firefox</code>. Use this if you want to run <code>firefox</code> in an entirely new process. By default, <code>firefox</code> will delegate a command to an already running instance.</p>
<dt><code>-ProfileManager</code></p>
<dd> Start the profilemanager. Use this to choose the profile you would like to run <code>firefox</code> with. You will need to also use <code>-no-remote</code> if there is already a running <code>firefox</code> instance.</p>
<dt><code>-P</code> <i>profile</i></p>
<dd> Start <code>firefox</code> with the profile named <i>profile</i>. Will start the profile manager if a valid profile name is not specified. You will need to also use <code>-no-remote</code> if there is already a running <code>firefox</code> instance.</p>
<dt><code>-safe-mode</code></p>
<dd> Start <code>firefox</code> in safe-mode. This disables all third-party extensions, and may be necessary if you are having problems with an extension you installed.</p>
<dt><code>-new-tab</code> <i>url</i></p>
<dd> Open <i>url</i> in a new tab.</p>
<dt><code>-new-window</code> <i>url</i></p>
<dd> Open <i>url</i> in a new window.</p>
<dt><code>-v, -version</code></p>
<dd> Print the current version of <code>firefox</code>.</p>
<dt><code>-UILocale</code> <i>locale</i></p>
<dd> Start <code>firefox</code> with the specified locale <i>locale</i>. Use this to override your environment</p>
<dt><code>-preferences</code></p>
<dd> Open the preferences dialog.</p>
<dt><code>-private</code></p>
<dd> Start <code>firefox</code> in private browsing mode</p>
<dt><code>-private-toggle</code></p>
<dd> Toggle private browsing mode</p>
<dt><code>-setDefaultBrowser</code></p>
<dd> Set <code>firefox</code> as the default web browser</p>
<dt><code>-search</code> <i>term</i></p>
<dd> Search for <i>term</i> with your default search engine</p>
<dt><code>-jsconsole</code></p>
<dd> Open the Error console. If <code>firefox</code> is not already running, this will open a new browser window too </p>
</dl>
<h2>Index</h2>
