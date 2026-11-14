---
title: "lttng-ust-dl(3)"
name: "lttng-ust-dl"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lttng-ust-dl/"
description: "lttng-ust-dl — LTTng UST 2.x Dynamic Linker Tracing"
---

<h2 class="name">NAME</h2>
<p> lttng-ust-dl &#8212; LTTng UST 2.x Dynamic Linker Tracing</p>
<h2>SYNOPSIS</h2>
<p> Launch your application with:</p>
<dl>
<dt><code>LD_PRELOAD=liblttng-ust-dl.so</code> appname</p>
<dd></dl>
<p> This LD_PRELOAD library causes all calls to dlopen and dlclose in the application to be traced with LTTng. In addition to loading this library, enabling this tracing requires the following two events to be enabled: &quot;ust_baddr:push&quot; and &quot;ust_baddr:pop&quot;. </p>
<h2>DESCRIPTION</h2>
<p> The events have the following detailed definitions: </p>
<dl>
<dt>ust_baddr:push</p>
<dd> This event is used to trace dlopen calls. The base address (where the dynamic linker has placed the shared object) is recorded in the &quot;baddr&quot; field. The path to the shared object gets recorded in the &quot;sopath&quot; field (as string). The file size of the loaded object (in bytes) is recorded to the &quot;size&quot; field and its time of last modification (in seconds since Epoch) is recorded in the &quot;mtime&quot; field.</p>
<dt>ust_baddr:pop</p>
<dd> This event is used to trace dlclose calls. The base address of the shared object that got closed is recorded in the &quot;baddr&quot; field.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-lttng-ust/">lttng-ust</a>(3), <a href="/docs/linux/man/3-dlopen/">dlopen</a>(3), <a href="/docs/linux/man/1-lttng/">lttng</a>(1) </p>
<h2>BUGS</h2>
<p> If you encounter any issues or usability problem, please report it on our mailing list &lt;lttng-dev [at] lists.lttng.org&gt; to help improve this project. </p>
<h2>CREDITS</h2>
<p> liblttng-ust is distributed under the GNU Lesser General Public License version 2.1. The headers are distributed under the MIT license. </p>
<p> See <a rel="nofollow" href="http://lttng.org">http://lttng.org</a> for more information on the LTTng project. </p>
<p> Mailing list for support and development: &lt;lttng-dev [at] lists.lttng.org&gt;. </p>
<p> You can find us on IRC server irc.oftc.net (OFTC) in #lttng. </p>
<h2>AUTHORS</h2>
<p> liblttng-ust was originally written by Mathieu Desnoyers, with additional contributions from various other people. It is currently maintained by Mathieu Desnoyers &lt;mathieu.desnoyers [at] efficios.com&gt;. </p>
<h2>Index</h2>
