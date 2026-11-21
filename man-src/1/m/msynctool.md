---

title: "msynctool(1)"
name: "msynctool"
section: "1"
letter: "m"
url: "/docs/linux/man/1-msynctool/"
description: "msynctool – Command line interface for OpenSync"
---

<p> msynctool &#8211; Command line interface for OpenSync</p>
<h2>SYNTAX</h2>
<p> msynctool <i>option</i> [<i>arguments</i>] [<i>option</i>]<br />
 msynctool &#8211;sync SYNC_GROUP</p>
<h2>DESCRIPTION</h2>
<p> Command line interface for OpenSync<br />
 You can use this tool to synchronize your devices and applications using the OpenSync framework from the command line. </p>
<dl>
<dt>&#8211; First you have to create a SYNC_GROUP:</dt>
<dd>
</dd><dt>
</dt><dd> msynctool &#8211;addgroup evo2-sync</dd>
<dt>&#8211; Now you have to add the members to this group. (2 at least)</dt>
<dd></dd></dl>
<p> <code>Note: The first argument to the &#8211;addmember command is the group to which you want to add a member, the second argument is the name of the plugin to add.</code></p>
<dl>
<dt>
</dt><dd> msynctool &#8211;addmember evo2-sync evo2-sync</dd>
<dt>
</dt><dd> msynctool &#8211;addmember evo2-sync file-sync</dd>
<dt>&#8211; The next thing you have to do is to configure the plugins.</dt>
<dd>
</dd><dt>
</dt><dd> msynctool &#8211;configure evo2-sync 1<br />
 (configures the first group member)</dd>
<dt>
</dt><dd> msynctool &#8211;configure evo2-sync 2<br />
 (configures the second group member)</dd>
<dt>&#8211; Now your group is ready for usage!</dt>
<dd>
</dd><dt>
</dt><dd> msynctool &#8211;sync evo2-sync </dd>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;listgroups</code></dt>
<dd> Lists all groups</dd>
<dt><code>&#8211;listplugins</code></dt>
<dd> Lists all plugins</dd>
<dt><code>&#8211;listobjects</code></dt>
<dd> Lists all objtypes that the engine understands</dd>
<dt>
</dt><dd> objtypes: <i>contact</i>, <i>data</i>, <i>event</i>, <i>note</i>, <i>todo</i></dd>
<dt><code>&#8211;showformats</code> <i>objtype</i></dt>
<dd> Lists all formats that a objtype can have</dd>
<dt><code>&#8211;showgroup</code> <i>groupname</i></dt>
<dd> Lists all members of the group</dd>
<dt><code>&#8211;sync</code> <i>groupname</i></dt>
<dd> Sync all members in a group</dd>
<dt><code>&#8211;filter-objtype</code> <i>objtype</i></dt>
<dd> Filter out objtype</dd>
<dt>
</dt><dd> For example, the following syncs only contacts:</dd>
<dt>
</dt><dd> msynctool &#8211;sync evo2-sync &#8211;filter-objtype event &#8211;filter-objtype note &#8211;filter-objtype todo</dd></dl>
<p> <code>Note: if you use &quot;&#8211;filter-objtype data&quot; it syncs nothing !?</code></p>
<dl>
<dt><code>&#8211;slow-sync</code> <i>objtype</i></dt>
<dd> Perform a slow-sync of all members in the group</dd>
<dt><code>[&#8211;wait]</code></dt>
<dd> Don&#8217;t immediately start to sync, but wait for a client to initialize the sync</dd>
<dt><code>[&#8211;multi]</code></dt>
<dd> Repeat to wait for sync alerts</dd>
<dt><code>&#8211;addgroup</code> <i>groupname</i></dt>
<dd> Add a new group</dd>
<dt><code>&#8211;delgroup</code> <i>groupname</i></dt>
<dd> Delete the given group</dd>
<dt><code>&#8211;addmember</code> <i>groupname</i> <i>plugintype</i></dt>
<dd> Add a member to the group</dd>
<dt><code>&#8211;configure</code> <i>groupname</i> <i>memberid</i></dt>
<dd> Configure a member. memberid as returned by <code>&#8211;showgroup</code></dd>
<dt><code>[&#8211;manual]</code></dt>
<dd> Make manual engine iterations. Only for debugging</dd>
<dt><code>[&#8211;configdir]</code></dt>
<dd> Set a different configdir than ~/.opensync</dd>
<dt><code>[&#8211;conflict 1-9/d/i/n]</code></dt>
<dd> Resolve all conflicts as side <i>1-9</i> wins, <i>d</i>uplicate, <i>i</i>gnore, or keep <i>n</i>ewer</dd></dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>OSYNC_TRACE</code></dt>
<dd> When you want to provide trace files please turn on tracing like this:</dd>
<dt>
</dt><dd> export OSYNC_TRACE=/path/to/log/dir</dd>
<dt>
</dt><dd> When you run some opensync commands now, opensync will generate a couple of Thread*.log files in this directory.</dd>
<dt>
</dt><dd> You can exclude sensitive data in the trace files with:</dd>
<dt>
</dt><dd> export OSYNC_PRIVACY=1</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-convcard/">convcard</a></code>(1),<code>file-sync.conf</code>(5)</p>
<h2>AUTHORS</h2>
<p> This manual page was written for the Debian GNU/Linux project by Matthias Jahn &lt;jahn.matthias [at] freenet.de&gt;. But it may be used by other distributions. </p>
<p> msynctool was written by Armin Bauer and the OpenSync project </p>
