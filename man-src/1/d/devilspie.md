---
title: "devilspie(1)"
name: "devilspie"
section: "1"
letter: "d"
url: "/docs/linux/man/1-devilspie/"
description: "devilspie – perform actions on windows as they are created"
---

<h2>NAME</h2>
<p> devilspie &#8211; perform actions on windows as they are created </p>
<h2>SYNOPSIS</h2>
<p> <code>devilspie</code> <i>[OPTION</i>]&#8230; <i>configuration-files&#8230;</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>devilspie</code> is a program which can detect windows as they are created, and perform actions on them if they match as set of criteria. </p>
<p> The configuration files are a set of s-expressions. </p>
<p> Command-lines options:</p>
<dl>
<dt><code>-a</code> <code>&#8211;apply-to-existing</code></p>
<dd> Apply to all existing windows instead of just new windows.</p>
<dt><code>-d</code> <code>&#8211;debug</code></p>
<dd> Output debug information</p>
<dt><code>-l</code> <code>&#8211;list-symbols</code></p>
<dd> List available symbols supported in input files.</p>
<dt><code>-s</code> <i>symname</i> <code>&#8211;symbol-doc</code>=<i>symname</i></p>
<dd>
&nbsp;<wbr>Get detailed help on symbol&nbsp;<wbr><i>symname</i>&nbsp;<wbr>(&#8216;all&#8217;&nbsp;<wbr>for all symbols). </p>
</dl>
<h2>ALLOWED SYMBOLS</h2>
<p> In the input files, the following symbols are known by <i>devilspie</i>:</p>
<dl>
<dt><code>is</code></p>
<dd> String equality, (is a b) means a is the same as b.</p>
<dt><code>contains</code></p>
<dd> Substring, (contains haystack needle) means haystack contains needle.</p>
<dt><code>matches</code></p>
<dd> Regexp matches, (matches str pattern) means the regexp pattern matches str.</p>
<dt><code>window_name</code></p>
<dd> Return the title of the current window (String).</p>
<dt><code>window_role</code></p>
<dd> Return the role (as determined by the WM_WINDOW_ROLE hint) of the current window (String).</p>
<dt><code>window_class</code></p>
<dd> Return the class of the current window (String).</p>
<dt><code>window_xid</code></p>
<dd> Return the X11 window id of the current window (Integer).</p>
<dt><code>application_name</code></p>
<dd> Return the application name (as determined by libwnck) of the current window (String).</p>
<dt><code>window_property</code></p>
<dd> Returns the given property of the window, e.g. pass &quot;_NET_WM_STATE&quot; (String).</p>
<dt><code>window_workspace</code></p>
<dd> Returns the workspace a window is on (Integer).</p>
<dt><code>debug</code></p>
<dd> Debugging function, outputs the current window&#8217;s title, name, role and geometry (Returns TRUE).</p>
<dt><code>print</code></p>
<dd> Print args (without trailing returns boolean).</p>
<dt><code>println</code></p>
<dd> Print args (with trailing returns boolean).</p>
<dt><code>str</code></p>
<dd> Transform parameters into strings and concat them.</p>
<dt><code>hex</code></p>
<dd> Transform the integer parameter into an unsigned hexadecimal string (with 0x prefix).</p>
<dt><code>geometry</code></p>
<dd> Set position + size (as tring) of current window (returns boolean).</p>
<dt><code>fullscreen</code></p>
<dd> Make the current window fullscreen (returns TRUE).</p>
<dt><code>focus</code></p>
<dd> Focus the current window (returns TRUE).</p>
<dt><code>center</code></p>
<dd> Center position of current window (returns boolean).</p>
<dt><code>maximize</code></p>
<dd> Maximise the current window (returns TRUE).</p>
<dt><code>maximize_vertically</code></p>
<dd> Maximise vertically the current window (returns TRUE).</p>
<dt><code>maximize_horizontally</code></p>
<dd> Maximise horizontally the current window (returns TRUE).</p>
<dt><code>unmaximize</code></p>
<dd> Un-maximise the current window (returns TRUE).</p>
<dt><code>minimize</code></p>
<dd> Minimise the current window (returns TRUE).</p>
<dt><code>unminimize</code></p>
<dd> Un-minimise the current window (returns TRUE).</p>
<dt><code>shade</code></p>
<dd> Shade (&quot;roll up&quot;) the current window (returns TRUE).</p>
<dt><code>unshade</code></p>
<dd> Un-shade (&quot;roll down&quot;) the current window (returns TRUE).</p>
<dt><code>close</code></p>
<dd> Close the current window (returns TRUE).</p>
<dt><code>pin</code></p>
<dd> Pin the current window to all workspaces (returns TRUE).</p>
<dt><code>unpin</code></p>
<dd> Unpin the current window from all workspaces (returns TRUE).</p>
<dt><code>stick</code></p>
<dd> Make the current window stick to all viewports (returns TRUE).</p>
<dt><code>unstick</code></p>
<dd> Unstick the window from viewports (returns TRUE).</p>
<dt><code>set_workspace</code></p>
<dd> Move the window to a specific workspace number, counting from 1 (returns boolean).</p>
<dt><code>set_viewport</code></p>
<dd> Move the window to a specific viewport number, counting from 1 (returns boolean).</p>
<dt><code>skip_pager</code></p>
<dd> Remove the current window from the window list (returns TRUE).</p>
<dt><code>skip_tasklist</code></p>
<dd> Remove the current window from the pager (returns TRUE).</p>
<dt><code>above</code></p>
<dd> Set the current window to be above all normal windows (returns TRUE).</p>
<dt><code>below</code></p>
<dd> Set the current window to be below all normal windows (returns TRUE).</p>
<dt><code>decorate</code></p>
<dd> Add the window manager decorations to the current window (returns boolean).</p>
<dt><code>undecorate</code></p>
<dd> Remove the window manager decorations from the current window (returns boolean).</p>
<dt><code>wintype</code></p>
<dd> Set the window type of the current window (returns boolean). Accepted values are: normal, dialog, menu, toolbar, splashscreen, utility, dock, desktop.</p>
<dt><code>opacity</code></p>
<dd> Change the opacity level (as integer in 0..100) of the current window (returns boolean).</p>
<dt><code>spawn_async</code></p>
<dd> Execute a command in the background (returns boolean). Command is given as a single string, or as a series of strings (similar to execl).</p>
<dt><code>spawn_sync</code></p>
<dd> Execute a command in the foreground (returns command output as string, or FALSE on error). Command is given as a single string, or as a series of strings (similar to execl). </p>
</dl>
<h2>BUGS</h2>
<p> This manpage is almost useless, as it was thrown together on a train. </p>
<h2>AUTHOR</h2>
<p> This manual page was written by Ross Burton &lt;ross [at] burtonini.com&gt;. </p>
<h2>Index</h2>
