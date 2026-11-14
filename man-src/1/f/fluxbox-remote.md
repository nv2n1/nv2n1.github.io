---
title: "fluxbox-remote(1)"
name: "fluxbox-remote"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fluxbox-remote/"
description: "fluxbox-remote – command line access to key commands for"
---

<h2 class="name">NAME</h2>
<p> fluxbox-remote &#8211; command line access to key commands for </p>
<p><a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1)</p>
<h2>SYNOPSIS</h2>
<p> <code>fluxbox-remote</code> <i>command</i></p>
<h2>DESCRIPTION</h2>
<p> <i><a href="/docs/linux/man/1-fluxbox-remote/">fluxbox-remote</a>(1)</i> is designed to allow scripts to execute most key commands from <i><a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1)</i>. <i><a href="/docs/linux/man/1-fluxbox-remote/">fluxbox-remote</a>(1)</i> will only work with <i><a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1)</i>: its communications with <i><a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1)</i> are not standardized in any way. It is recommended that a standards-based tool such as <i><a href="/docs/linux/man/1-wmctrl/">wmctrl</a>(1)</i> be used whenever possible, in order for scripts to work with other window managers.</p>
<h2>CAVEATS</h2>
<p> <i><a href="/docs/linux/man/1-fluxbox-remote/">fluxbox-remote</a>(1)</i> uses the X11 protocol to communicate with <i><a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1)</i>. Therefore, it is possible for any user with access to the <i><a href="/docs/linux/man/7-x/">X</a>(7)</i> server to use <i><a href="/docs/linux/man/1-fluxbox-remote/">fluxbox-remote</a>(1)</i>. For this reason, several key commands have been disabled. Users should be aware of the security implications when enabling <i><a href="/docs/linux/man/1-fluxbox-remote/">fluxbox-remote</a>(1)</i>, especially when using a forwarded <i><a href="/docs/linux/man/7-x/">X</a>(7)</i> connection.</p>
<h2>RESOURCES</h2>
<p> session.screen0.allowRemoteActions: &lt;boolean&gt;</p>
<dl>
<dt>
<dd> This resource in ~/.fluxbox/init must be set to &#8216;true&#8217; in order for <i><a href="/docs/linux/man/1-fluxbox-remote/">fluxbox-remote</a>(1)</i> to function. Please read the <code>CAVEATS</code> first.</dl>
<h2>ENVIRONMENT</h2>
<p> In order to communicate with <i><a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1)</i>, the DISPLAY environment variable must be set properly. Usually, the value should be &#8216;:0.0&#8217;.</p>
<h2>AUTHORS</h2>
<p> This man page written by Mark Tiefenbruck &lt;mark at fluxbox.org&gt;</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1) <a href="/docs/linux/man/5-fluxbox-keys/">fluxbox-keys</a>(5) <a href="/docs/linux/man/1-wmctrl/">wmctrl</a>(1)</p>
<h2>AUTHOR</h2>
<p> <code>Mark Tiefenbruck</code> &lt;mark [at] fluxbox.org&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>Index</h2>
