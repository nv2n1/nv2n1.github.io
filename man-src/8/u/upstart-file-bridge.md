---
title: "upstart-file-bridge(8)"
name: "upstart-file-bridge"
section: "8"
letter: "u"
url: "/docs/linux/man/8-upstart-file-bridge/"
description: "upstart-file-bridge – Bridge between Upstart and inotify"
---

<p>upstart-file-bridge &#8211; Bridge between Upstart and inotify</p>
<h2>Synopsis</h2>
<p><code>upstart-file-bridge</code> [<i>OPTIONS</i>]&#8230;</p>
<h2>Description</h2>
<p><code>upstart-file-bridge</code> receives information about kernel file events that <code><a href="/docs/linux/man/7-inotify/">inotify</a></code>(7) has received and creates <code><a href="/docs/linux/man/8-init/">init</a></code>(8) events for them. Supported events exposed to Upstart allow jobs to detect creation, modification and deletion. See <code><a href="/docs/linux/man/7-file-event/">file-event</a></code>(7) for further details. The bridge works by querying the <code><a href="/docs/linux/man/8-init/">init</a></code>(8) daemon at bridge startup time to determine a list of all jobs whose <code>start on</code> or <code>stop on</code> conditions reference the <code>file</code> event. Further, the bridge arranges to be notified automatically when new jobs are created such that any subsequent jobs which reference the <code>file</code> event are also handled (as are job deletions). See <code><a href="/docs/linux/man/7-inotify/">inotify</a></code>(7) and for further details. </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;daemon</code></p>
<dd>Detach and run in the background.</p>
<dt><code>&#8211;debug</code></p>
<dd>Enable debugging output.</p>
<dt><code>&#8211;help</code></p>
<dd>Show brief usage summary.</p>
<dt><code>&#8211;user</code></p>
<dd>User-session mode: connect to Upstart via the user session rather than over the D-Bus system bus.</p>
<dt><code>&#8211;verbose</code></p>
<dd>Enable verbose output.</dl>
<h2>Job Environment Variables</h2>
<dl>
<dt><code>FILE</code></p>
<dd>Path to file to watch. When run without <code>&#8211;user</code>, this must be an absolute path. If <code>&#8211;user</code> is specified, certain relative path types are supported:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>If the path begins with &#8216;~/&#8217;, the value will be expanded as would be performed by a shell for matching purposes (although when the event is emitted, the original value will be used).</p>
<dt>&bull;</p>
<dd>If the path begins with &#8216;./&#8217;, &#8216;.&#8217; will be assumed to be the users home directory.</p>
<dt>&bull;</p>
<dd>In all other scenarios, if the path does not begin with &#8216;/&#8217;, it will be assumed to represent a file below the users home directory.</dl>
<p> If the path ends with a slash, it is considered to be a directory which changes the match behaviour (see below). </p>
<p> If the path is not a directory, the file (but not the directory) portion of the path may contain wildcard matches. See <code><a href="/docs/linux/man/3-fnmatch/">fnmatch</a></code>(3) and <code><a href="/docs/linux/man/7-glob/">glob</a></code>(7) for further details.</dl>
<dt><code>EVENT</code></p>
<dd>Event relating to <code>FILE</code> that job is interested in. If this variable is specified the value must be set to <code>create</code>, <code>modify</code> or <code>delete</code> depending on what type of file event the job is interested in. If <code>FILE</code> is not specified, the bridge will watch for all types and set this variable to the appropriate value when emitting the event.</dl>
<h2>Watch Type Behaviour</h2>
<p>The bridge emits events depending not only on the value of <code>EVENT</code>, but also on the entity specified by <code>FILE</code>:</p>
<h3>File</h3>
<p>An event will be emitted when the named file is created, modified or deleted depending on the value of <code>EVENT</code>. If <code>EVENT</code> is not specified, react to creation, modification and deletion. </p>
<p> If the file already exists when the job is registered, and <code>EVENT</code> either specifies <i>create</i> or the variable is not specified, the event will be emitted.</p>
<h3>Directory</h3>
<p>An event will be emitted when the named directory is created, modified (files within it are created, modified or deleted) or deleted depending on the value of <code>EVENT</code>. If <code>EVENT</code> is not specified, react to creation, modification and deletion. </p>
<p> If the directory already exists when the job is registered, and <code>EVENT</code> either specifies <i>create</i> or the variable is not specified, the event will be emitted.</p>
<h3>Glob</h3>
<p>One event will be emitted per match when the glob wildcard matches any files in the directory part is created, modified or deleted, depending on the value of <code>EVENT</code>. If <code>EVENT</code> is not specified, react to creation, modification and deletion. </p>
<p> If any matches already exist when the job is registered, and <code>EVENT</code> either specifies <i>create</i> or the variable is not specified, events will be emitted.</p>
<h2>Notes</h2>
<dl>
<dt>&bull;</p>
<dd>A single instance of the bridge may be run at the system level, but multiple further instances may be run per user session instance by using the <code>&#8211;user</code>.</p>
<dt>&bull;</p>
<dd>All job conditions specifying the <code>file</code> event are multi-shot: if the same file event occurs multiple times, the bridge will emit an Upstart event each time.</dl>
<h2>Limitations</h2>
<dl>
<dt>&bull;</p>
<dd>Since the bridge currently uses <code><a href="/docs/linux/man/7-inotify/">inotify</a></code>(7), it is subject to the same limitations; namely that recursive watches cannot be created reliably in all circumstances. As such, pathological scenarios such as deep directory trees being created and then quickly removed <code>cannot</code> be handled reliably. The following provides advice to minimise unexpected behaviour:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>Attempt to only watch for files to be created, modified or deleted in directories that are guaranteed to already exist at the time the job is registered by the bridge.</p>
<dt>&bull;</p>
<dd>If the system cannot guarantee that the directory will exist at job registration time, arrange for the directory to be created by an Upstart job before the bridge itself starts.</p>
<dt>&bull;</p>
<dd>In user session mode, if a job specifies a file to watch for and that file is created but inaccessible to the user running the bridge, no event will be emitted.</dl>
</dl>
<dt>&bull;</p>
<dd>Tilde expansion is only supported for the current user; that is &#8216;~otheruser&#8217; will not work.</dl>
<h2>Author</h2>
<p>Written by James Hunt &lt;<code>james.hunt [at] canonical.com</code>&gt;</p>
<h2>Bugs</h2>
<p>Report bugs at &lt;<code><a rel="nofollow" href="https://launchpad.net/ubuntu/+source/upstart/+bugs">https://launchpad.net/ubuntu/+source/upstart/+bugs</a></code>&gt;</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2013 Canonical Ltd. </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-init/">init</a></code>(5) <code><a href="/docs/linux/man/8-init/">init</a></code>(8) <code><a href="/docs/linux/man/7-inotify/">inotify</a></code>(7) <code><a href="/docs/linux/man/7-file-event/">file-event</a></code>(7) </p>
