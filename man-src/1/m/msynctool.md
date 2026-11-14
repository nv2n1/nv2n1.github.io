---
title: "msynctool(1)"
name: "msynctool"
section: "1"
letter: "m"
url: "/docs/linux/man/1-msynctool/"
description: "msynctool – Command line interface for OpenSync"
---

<h2>NAME</h2>
<p> msynctool &#8211; Command line interface for OpenSync</p>
<h2>SYNTAX</h2>
<p> msynctool <i>option</i> [<i>arguments</i>] [<i>option</i>]<br />
 msynctool &#8211;sync SYNC_GROUP</p>
<h2>DESCRIPTION</h2>
<p> Command line interface for OpenSync<br />
 You can use this tool to synchronize your devices and applications using the OpenSync framework from the command line. </p>
<dl>
<dt>&#8211; First you have to create a SYNC_GROUP:</p>
<dd>
<dt>
<dd> msynctool &#8211;addgroup evo2-sync</p>
<dt>&#8211; Now you have to add the members to this group. (2 at least)</p>
<dd></dl>
<p> <code>Note: The first argument to the &#8211;addmember command is the group to which you want to add a member, the second argument is the name of the plugin to add.</code></p>
<dl>
<dt>
<dd> msynctool &#8211;addmember evo2-sync evo2-sync</p>
<dt>
<dd> msynctool &#8211;addmember evo2-sync file-sync</p>
<dt>&#8211; The next thing you have to do is to configure the plugins.</p>
<dd>
<dt>
<dd> msynctool &#8211;configure evo2-sync 1<br />
 (configures the first group member)</p>
<dt>
<dd> msynctool &#8211;configure evo2-sync 2<br />
 (configures the second group member)</p>
<dt>&#8211; Now your group is ready for usage!</p>
<dd>
<dt>
<dd> msynctool &#8211;sync evo2-sync </p>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;listgroups</code></p>
<dd> Lists all groups</p>
<dt><code>&#8211;listplugins</code></p>
<dd> Lists all plugins</p>
<dt><code>&#8211;listobjects</code></p>
<dd> Lists all objtypes that the engine understands</p>
<dt>
<dd> objtypes: <i>contact</i>, <i>data</i>, <i>event</i>, <i>note</i>, <i>todo</i></p>
<dt><code>&#8211;showformats</code> <i>objtype</i></p>
<dd> Lists all formats that a objtype can have</p>
<dt><code>&#8211;showgroup</code> <i>groupname</i></p>
<dd> Lists all members of the group</p>
<dt><code>&#8211;sync</code> <i>groupname</i></p>
<dd> Sync all members in a group</p>
<dt><code>&#8211;filter-objtype</code> <i>objtype</i></p>
<dd> Filter out objtype</p>
<dt>
<dd> For example, the following syncs only contacts:</p>
<dt>
<dd> msynctool &#8211;sync evo2-sync &#8211;filter-objtype event &#8211;filter-objtype note &#8211;filter-objtype todo</dl>
<p> <code>Note: if you use &quot;&#8211;filter-objtype data&quot; it syncs nothing !?</code></p>
<dl>
<dt><code>&#8211;slow-sync</code> <i>objtype</i></p>
<dd> Perform a slow-sync of all members in the group</p>
<dt><code>[&#8211;wait]</code></p>
<dd> Don&#8217;t immediately start to sync, but wait for a client to initialize the sync</p>
<dt><code>[&#8211;multi]</code></p>
<dd> Repeat to wait for sync alerts</p>
<dt><code>&#8211;addgroup</code> <i>groupname</i></p>
<dd> Add a new group</p>
<dt><code>&#8211;delgroup</code> <i>groupname</i></p>
<dd> Delete the given group</p>
<dt><code>&#8211;addmember</code> <i>groupname</i> <i>plugintype</i></p>
<dd> Add a member to the group</p>
<dt><code>&#8211;configure</code> <i>groupname</i> <i>memberid</i></p>
<dd> Configure a member. memberid as returned by <code>&#8211;showgroup</code></p>
<dt><code>[&#8211;manual]</code></p>
<dd> Make manual engine iterations. Only for debugging</p>
<dt><code>[&#8211;configdir]</code></p>
<dd> Set a different configdir than ~/.opensync</p>
<dt><code>[&#8211;conflict 1-9/d/i/n]</code></p>
<dd> Resolve all conflicts as side <i>1-9</i> wins, <i>d</i>uplicate, <i>i</i>gnore, or keep <i>n</i>ewer</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>OSYNC_TRACE</code></p>
<dd> When you want to provide trace files please turn on tracing like this:</p>
<dt>
<dd> export OSYNC_TRACE=/path/to/log/dir</p>
<dt>
<dd> When you run some opensync commands now, opensync will generate a couple of Thread*.log files in this directory.</p>
<dt>
<dd> You can exclude sensitive data in the trace files with:</p>
<dt>
<dd> export OSYNC_PRIVACY=1</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-convcard/">convcard</a></code>(1),<code><a href="/docs/linux/man/5-file-sync-conf/">file-sync.conf</a></code>(5)</p>
<h2>AUTHORS</h2>
<p> This manual page was written for the Debian GNU/Linux project by Matthias Jahn &lt;jahn.matthias [at] freenet.de&gt;. But it may be used by other distributions. </p>
<p> msynctool was written by Armin Bauer and the OpenSync project </p>
<h2>Index</h2>
