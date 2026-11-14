---
title: "snap(8)"
name: "snap"
section: "8"
letter: "s"
url: "/docs/linux/man/8-snap/"
description: "snap – Tool to interact with snaps"
---

<p>snap &#8211; Tool to interact with snaps</p>
<h2>Synopsis</h2>
<p><code>snap</code> [OPTIONS]</p>
<h2>Description</h2>
<p>The snap command lets you install, configure, refresh and remove snaps. Snaps are packages that work across many different Linux distributions, enabling secure delivery and operation of the latest apps and utilities.</p>
<h2>Options</h2>
<h2>Commands</h2>
<h3>abort</h3>
<p>Abort a pending change </p>
<p> The <i>abort</i> command attempts to abort a change that still has pending tasks. </p>
<p> <code>Usage</code>: snap [OPTIONS] abort [abort-OPTIONS]</p>
<dl>
<dt><code>&#8211;last</code></p>
<dd>Select last change of given type (install, refresh, remove, try, auto-refresh, etc.). A question mark at the end of the type means to do nothing (instead of returning an error) if no change of the given type is found. Note the question mark could need protecting from the shell.</dl>
<h3>ack</h3>
<p>Add an assertion to the system </p>
<p> The <i>ack</i> command tries to add an assertion to the system assertion database. </p>
<p> The assertion may also be a newer revision of a pre-existing assertion that it will replace. </p>
<p> To succeed the assertion must be valid, its signature verified with a known public key and the assertion consistent with and its prerequisite in the database.</p>
<h3>alias</h3>
<p>Set up a manual alias </p>
<p> The <i>alias</i> command aliases the given snap application to the given alias. </p>
<p> Once this manual alias is setup the respective application command can be invoked just using the alias. </p>
<p> <code>Usage</code>: snap [OPTIONS] alias [alias-OPTIONS]</p>
<dl>
<dt><code>&#8211;no-wait</code></p>
<dd>Do not wait for the operation to finish but just print the change id.</dl>
<h3>aliases</h3>
<p>List aliases in the system </p>
<p> The <i>aliases</i> command lists all aliases available in the system and their status. </p>
<p> $ snap aliases &lt;snap&gt; </p>
<p> Lists only the aliases defined by the specified snap. </p>
<p> An alias noted as undefined means it was explicitly enabled or disabled but is not defined in the current revision of the snap, possibly temporarily (e.g. because of a revert). This can cleared with &#8216;snap alias &#8211;reset&#8217;.</p>
<h3>changes</h3>
<p>List system changes </p>
<p> The <i>changes</i> command displays a summary of system changes performed recently. </p>
<p> <code>Usage</code>: snap [OPTIONS] changes [changes-OPTIONS]</p>
<dl>
<dt><code>&#8211;abs-time</code></p>
<dd>Display absolute times (in RFC 3339 format). Otherwise, display relative times up to 60 days, then YYYY-MM-DD.</dl>
<h3>check-snapshot</h3>
<p>Check a snapshot </p>
<p> The <i>check-snapshot</i> command verifies the user, system and configuration data of the snaps included in the specified snapshot. </p>
<p> The check operation runs the same data integrity verification that is performed when a snapshot is restored. </p>
<p> By default, this command checks all the data in a snapshot. Alternatively, you can specify the data of which snaps to check, or for which users, or a combination of these. </p>
<p> If a snap is included in a check-snapshot operation, excluding its system and configuration data from the check is not currently possible. This restriction may be lifted in the future. </p>
<p> <code>Usage</code>: snap [OPTIONS] check-snapshot [check-snapshot-OPTIONS]</p>
<dl>
<dt><code>&#8211;no-wait</code></p>
<dd>Do not wait for the operation to finish but just print the change id.</p>
<dt><code>&#8211;users</code></p>
<dd>Check data of only specific users (comma-separated) (default: all users)</dl>
<h3>connect</h3>
<p>Connect a plug to a slot </p>
<p> The <i>connect</i> command connects a plug to a slot. It may be called in the following ways: </p>
<p> $ snap connect &lt;snap&gt;:&lt;plug&gt; &lt;snap&gt;:&lt;slot&gt; </p>
<p> Connects the provided plug to the given slot. </p>
<p> $ snap connect &lt;snap&gt;:&lt;plug&gt; &lt;snap&gt; </p>
<p> Connects the specific plug to the only slot in the provided snap that matches the connected interface. If more than one potential slot exists, the command fails. </p>
<p> $ snap connect &lt;snap&gt;:&lt;plug&gt; </p>
<p> Connects the provided plug to the slot in the core snap with a name matching the plug name. </p>
<p> <code>Usage</code>: snap [OPTIONS] connect [connect-OPTIONS]</p>
<dl>
<dt><code>&#8211;no-wait</code></p>
<dd>Do not wait for the operation to finish but just print the change id.</dl>
<h3>connections</h3>
<p>List interface connections </p>
<p> The <i>connections</i> command lists connections between plugs and slots in the system. </p>
<p> Unless &lt;snap&gt; is provided, the listing is for connected plugs and slots for all snaps in the system. In this mode, pass &#8211;all to also list unconnected plugs and slots. </p>
<p> $ snap connections &lt;snap&gt; </p>
<p> Lists connected and unconnected plugs and slots for the specified snap. </p>
<p> <code>Usage</code>: snap [OPTIONS] connections [connections-OPTIONS]</p>
<dl>
<dt><code>&#8211;all</code></p>
<dd>Show connected and unconnected plugs and slots</dl>
<h3>create-cohort</h3>
<p>Create cohort keys for a set of snaps </p>
<p> The <i>create-cohort</i> command creates a set of cohort keys for a given set of snaps. </p>
<p> A cohort is a view or snapshot of a snap&#8217;s &quot;channel map&quot; at a given point in time that fixes the set of revisions for the snap given other constraints (e.g. channel or architecture). The cohort is then identified by an opaque per-snap key that works across systems. Installations or refreshes of the snap using a given cohort key would use a fixed revision for up to 90 days, after which a new set of revisions would be fixed under that same cohort key and a new 90 days window started.</p>
<h3>debug</h3>
<p>Run debug commands </p>
<p> The debug command contains a selection of additional sub-commands. </p>
<p> Debug commands can be removed without notice and may not work on non-development systems.</p>
<h3>debug confinement</h3>
<p>Print the confinement mode the system operates in </p>
<p> The <i>confinement</i> command will print the confinement mode (strict, partial or none) the system operates in.</p>
<h3>debug connectivity</h3>
<p>Check network connectivity status </p>
<p> The <i>connectivity</i> command checks the network connectivity of snapd.</p>
<h3>debug migrate-home</h3>
<p>Migrate snaps&#8217; directory to ~/Snap. </p>
<p> Migrate snaps&#8217; directory to ~/Snap. </p>
<p> <code>Usage</code>: snap [OPTIONS] debug migrate-home [migrate-home-OPTIONS]</p>
<dl>
<dt><code>&#8211;no-wait</code></p>
<dd></dl>
<h3>debug paths</h3>
<p>Print system paths </p>
<p> The <i>paths</i> command prints the list of paths detected and used by snapd.</p>
<h3>debug sandbox-features</h3>
<p>Print sandbox features available on the system </p>
<p> The sandbox command prints tags describing features of individual sandbox components used by snapd on a given system. </p>
<p> <code>Usage</code>: snap [OPTIONS] debug sandbox-features [sandbox-features-OPTIONS]</p>
<dl>
<dt><code>&#8211;required</code></p>
<dd>Ensure that given backend:feature is available</dl>
<h3>debug stacktraces</h3>
<p>Obtain stacktraces of all snapd goroutines </p>
<p> Obtain stacktraces of all snapd goroutines.</p>
<h3>debug state</h3>
<p>Inspect a snapd state file. </p>
<p> Inspect a snapd state file, bypassing snapd API. </p>
<p> <code>Usage</code>: snap [OPTIONS] debug state [state-OPTIONS]</p>
<dl>
<dt><code>&#8211;abs-time</code></p>
<dd>Display absolute times (in RFC 3339 format). Otherwise, display relative times up to 60 days, then YYYY-MM-DD.</p>
<dt><code>&#8211;changes</code></p>
<dd>List all changes</p>
<dt><code>&#8211;task</code></p>
<dd>ID of the task to inspect</p>
<dt><code>&#8211;change</code></p>
<dd>ID of the change to inspect</p>
<dt><code>&#8211;check</code></p>
<dd>Check change consistency</p>
<dt><code>&#8211;connections</code></p>
<dd>List all connections</p>
<dt><code>&#8211;connection</code></p>
<dd>Show details of the matching connections (snap or snap:plug,snap:slot or snap:plug-or-slot</p>
<dt><code>&#8211;is-seeded</code></p>
<dd>Output seeding status (true or false)</p>
<dt><code>&#8211;dot</code></p>
<dd>Dot (graphviz) output</p>
<dt><code>&#8211;no-hold</code></p>
<dd>Omit tasks in &#8216;Hold&#8217; state in the change output</dl>
<h3>debug timings</h3>
<p>Get the timings of the tasks of a change </p>
<p> The <i>timings</i> command displays details about the time each task runs. </p>
<p> <code>Usage</code>: snap [OPTIONS] debug timings [timings-OPTIONS]</p>
<dl>
<dt><code>&#8211;last</code></p>
<dd>Select last change of given type (install, refresh, remove, try, auto-refresh, etc.). A question mark at the end of the type means to do nothing (instead of returning an error) if no change of the given type is found. Note the question mark could need protecting from the shell.</p>
<dt><code>&#8211;ensure</code></p>
<dd>Show timings for a change related to the given Ensure activity (one of: auto-refresh, become-operational, refresh-catalogs, refresh-hints, seed)</p>
<dt><code>&#8211;all</code></p>
<dd>Show timings for all executions of the given Ensure or startup activity, not just the latest</p>
<dt><code>&#8211;startup</code></p>
<dd>Show timings for the startup of given subsystem (one of: load-state, ifacemgr)</p>
<dt><code>&#8211;verbose</code></p>
<dd>Show more information</dl>
<h3>disable</h3>
<p>Disable a snap in the system </p>
<p> The <i>disable</i> command disables a snap. The binaries and services of the snap will no longer be available, but all the data is still available and the snap can easily be enabled again. </p>
<p> <code>Usage</code>: snap [OPTIONS] disable [disable-OPTIONS]</p>
<dl>
<dt><code>&#8211;no-wait</code></p>
<dd>Do not wait for the operation to finish but just print the change id.</dl>
<h3>disconnect</h3>
<p>Disconnect a plug from a slot </p>
<p> The <i>disconnect</i> command disconnects a plug from a slot. It may be called in the following ways: </p>
<p> $ snap disconnect &lt;snap&gt;:&lt;plug&gt; &lt;snap&gt;:&lt;slot&gt; </p>
<p> Disconnects the specific plug from the specific slot. </p>
<p> $ snap disconnect &lt;snap&gt;:&lt;slot or plug&gt; </p>
<p> Disconnects everything from the provided plug or slot. The snap name may be omitted for the core snap. </p>
<p> When an automatic connection is manually disconnected, its disconnected state is retained after a snap refresh. The &#8211;forget flag can be added to the disconnect command to reset this behaviour, and consequently re-enable an automatic reconnection after a snap refresh. </p>
<p> <code>Usage</code>: snap [OPTIONS] disconnect [disconnect-OPTIONS]</p>
<dl>
<dt><code>&#8211;no-wait</code></p>
<dd>Do not wait for the operation to finish but just print the change id.</p>
<dt><code>&#8211;forget</code></p>
<dd>Forget remembered state about the given connection.</dl>
<h3>download</h3>
<p>Download the given snap </p>
<p> The <i>download</i> command downloads the given snap and its supporting assertions to the current directory with .snap and .assert file extensions, respectively. </p>
<p> <code>Usage</code>: snap [OPTIONS] download [download-OPTIONS]</p>
<dl>
<dt><code>&#8211;channel</code></p>
<dd>Use this channel instead of stable</p>
<dt><code>&#8211;edge</code></p>
<dd>Install from the edge channel</p>
<dt><code>&#8211;beta</code></p>
<dd>Install from the beta channel</p>
<dt><code>&#8211;candidate</code></p>
<dd>Install from the candidate channel</p>
<dt><code>&#8211;stable</code></p>
<dd>Install from the stable channel</p>
<dt><code>&#8211;revision</code></p>
<dd>Download the given revision of a snap, to which you must have developer access</p>
<dt><code>&#8211;basename</code></p>
<dd>Use this basename for the snap and assertion files (defaults to &lt;snap&gt;_&lt;revision&gt;)</p>
<dt><code>&#8211;target-directory</code></p>
<dd>Download to this directory (defaults to the current directory)</p>
<dt><code>&#8211;cohort</code></p>
<dd>Download from the given cohort</dl>
<h3>enable</h3>
<p>Enable a snap in the system </p>
<p> The <i>enable</i> command enables a snap that was previously disabled. </p>
<p> <code>Usage</code>: snap [OPTIONS] enable [enable-OPTIONS]</p>
<dl>
<dt><code>&#8211;no-wait</code></p>
<dd>Do not wait for the operation to finish but just print the change id.</dl>
<h3>export-snapshot</h3>
<p>Export a snapshot </p>
<p> Export a snapshot to the given filename.</p>
<h3>find</h3>
<p>Find packages to install </p>
<p> The <i>find</i> command queries the store for available packages. </p>
<p> With the &#8211;private flag, which requires the user to be logged-in to the store (see &#8216;snap help login&#8217;), it instead searches for private snaps that the user has developer access to, either directly or through the store&#8217;s collaboration feature. </p>
<p> A green check mark (given color and unicode support) after a publisher name indicates that the publisher has been verified. </p>
<p> <code>Usage</code>: snap [OPTIONS] find [find-OPTIONS]</p>
<dl>
<dd><code>Aliases</code>: search </p>
<dt><code>&#8211;private</code></p>
<dd>Search private snaps.</p>
<dt><code>&#8211;narrow</code></p>
<dd>Only search for snaps in “stable”.</p>
<dt><code>&#8211;section</code> [<i>=&quot;show-all-sections-please&quot;</i>] &lt;default: <i>&quot;no-section-specified&quot;</i>&gt;</p>
<dd>Restrict the search to a given section.</p>
<dt><code>&#8211;color</code> &lt;default: <i>&quot;auto&quot;</i>&gt;</p>
<dd>Use a little bit of color to highlight some things.</p>
<dt><code>&#8211;unicode</code> &lt;default: <i>&quot;auto&quot;</i>&gt;</p>
<dd>Use a little bit of Unicode to improve legibility.</dl>
<h3>forget</h3>
<p>Delete a snapshot </p>
<p> The <i>forget</i> command deletes a snapshot. This operation can not be undone. </p>
<p> A snapshot contains archives for the user, system and configuration data of each snap included in the snapshot. </p>
<p> By default, this command forgets all the data in a snapshot. Alternatively, you can specify the data of which snaps to forget. </p>
<p> <code>Usage</code>: snap [OPTIONS] forget [forget-OPTIONS]</p>
<dl>
<dt><code>&#8211;no-wait</code></p>
<dd>Do not wait for the operation to finish but just print the change id.</dl>
<h3>get</h3>
<p>Print configuration options </p>
<p> The <i>get</i> command prints configuration options for the provided snap. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;$&nbsp;snap get snap-name username<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;frank </p>
<p> If multiple option names are provided, the corresponding values are returned: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;$&nbsp;snap get snap-name username password<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Key&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;username&nbsp;<wbr>&nbsp;frank<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;password&nbsp;<wbr>&nbsp;&#8230; </p>
<p> Nested values may be retrieved via a dotted path: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;$&nbsp;snap get snap-name author.name<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;frank </p>
<p> <code>Usage</code>: snap [OPTIONS] get [get-OPTIONS]</p>
<dl>
<dt><code>-t</code></p>
<dd>Strict typing with nulls and quoted strings</p>
<dt><code>-d</code></p>
<dd>Always return document, even with single key</p>
<dt><code>-l</code></p>
<dd>Always return list, even with single key</dl>
<h3>help</h3>
<p>Show help about a command </p>
<p> The <i>help</i> command displays information about snap commands. </p>
<p> <code>Usage</code>: snap [OPTIONS] help [help-OPTIONS]</p>
<dl>
<dt><code>&#8211;all</code></p>
<dd>Show a short summary of all commands</dl>
<h3>import-snapshot</h3>
<p>Import a snapshot </p>
<p> Import an exported snapshot set to the system. The snapshot is imported with a new snapshot ID and can be restored using the restore command. </p>
<p> <code>Usage</code>: snap [OPTIONS] import-snapshot [import-snapshot-OPTIONS]</p>
<dl>
<dt><code>&#8211;abs-time</code></p>
<dd></dl>
<h3>info</h3>
<p>Show detailed information about snaps </p>
<p> The <i>info</i> command shows detailed information about snaps. </p>
<p> The snaps can be specified by name or by path; names are looked for both in the store and in the installed snaps; paths can refer to a .snap file, or to a directory that contains an unpacked snap suitable for &#8216;snap try&#8217; (an example of this would be the &#8216;prime&#8217; directory snapcraft produces). </p>
<p> <code>Usage</code>: snap [OPTIONS] info [info-OPTIONS]</p>
<dl>
<dt><code>&#8211;color</code> &lt;default: <i>&quot;auto&quot;</i>&gt;</p>
<dd>Use a little bit of color to highlight some things.</p>
<dt><code>&#8211;unicode</code> &lt;default: <i>&quot;auto&quot;</i>&gt;</p>
<dd>Use a little bit of Unicode to improve legibility.</p>
<dt><code>&#8211;abs-time</code></p>
<dd>Display absolute times (in RFC 3339 format). Otherwise, display relative times up to 60 days, then YYYY-MM-DD.</p>
<dt><code>&#8211;verbose</code></p>
<dd>Include more details on the snap (expanded notes, base, etc.)</dl>
<h3>install</h3>
<p>Install snaps on the system </p>
<p> The <i>install</i> command installs the named snaps on the system. </p>
<p> To install multiple instances of the same snap, append an underscore and a unique identifier (for each instance) to a snap&#8217;s name. </p>
<p> With no further options, the snaps are installed tracking the stable channel, with strict security confinement. All available channels of a snap are listed in its &#8216;snap info&#8217; output. </p>
<p> Revision choice via the &#8211;revision override requires the user to have developer access to the snap, either directly or through the store&#8217;s collaboration feature, and to be logged in (see &#8216;snap help login&#8217;). </p>
<p> Note that a later refresh will typically undo a revision override, taking the snap back to the current revision of the channel it&#8217;s tracking. </p>
<p> Use &#8211;name to set the instance name when installing from snap file. </p>
<p> <code>Usage</code>: snap [OPTIONS] install [install-OPTIONS]</p>
<dl>
<dt><code>&#8211;color</code> &lt;default: <i>&quot;auto&quot;</i>&gt;</p>
<dd>Use a little bit of color to highlight some things.</p>
<dt><code>&#8211;unicode</code> &lt;default: <i>&quot;auto&quot;</i>&gt;</p>
<dd>Use a little bit of Unicode to improve legibility.</p>
<dt><code>&#8211;no-wait</code></p>
<dd>Do not wait for the operation to finish but just print the change id.</p>
<dt><code>&#8211;channel</code></p>
<dd>Use this channel instead of stable</p>
<dt><code>&#8211;edge</code></p>
<dd>Install from the edge channel</p>
<dt><code>&#8211;beta</code></p>
<dd>Install from the beta channel</p>
<dt><code>&#8211;candidate</code></p>
<dd>Install from the candidate channel</p>
<dt><code>&#8211;stable</code></p>
<dd>Install from the stable channel</p>
<dt><code>&#8211;devmode</code></p>
<dd>Put snap in development mode and disable security confinement</p>
<dt><code>&#8211;jailmode</code></p>
<dd>Put snap in enforced confinement mode</p>
<dt><code>&#8211;classic</code></p>
<dd>Put snap in classic mode and disable security confinement</p>
<dt><code>&#8211;revision</code></p>
<dd>Install the given revision of a snap, to which you must have developer access</p>
<dt><code>&#8211;dangerous</code></p>
<dd>Install the given snap file even if there are no pre-acknowledged signatures for it, meaning it was not verified and could be dangerous (&#8211;devmode implies this)</p>
<dt><code>&#8211;unaliased</code></p>
<dd>Install the given snap without enabling its automatic aliases</p>
<dt><code>&#8211;name</code></p>
<dd>Install the snap file under the given instance name</p>
<dt><code>&#8211;cohort</code></p>
<dd>Install the snap in the given cohort</p>
<dt><code>&#8211;ignore-validation</code></p>
<dd>Ignore validation by other snaps blocking the installation</p>
<dt><code>&#8211;transaction</code> &lt;default: <i>&quot;per-snap&quot;</i>&gt;</p>
<dd>Have one transaction per-snap or one for all the specified snaps</p>
<dt><code>&#8211;quota-group</code></p>
<dd>Add the snap to a quota group on install</dl>
<h3>interface</h3>
<p>Show details of snap interfaces </p>
<p> The <i>interface</i> command shows details of snap interfaces. </p>
<p> If no interface name is provided, a list of interface names with at least one connection is shown, or a list of all interfaces if &#8211;all is provided. </p>
<p> <code>Usage</code>: snap [OPTIONS] interface [interface-OPTIONS]</p>
<dl>
<dt><code>&#8211;attrs</code></p>
<dd>Show interface attributes</p>
<dt><code>&#8211;all</code></p>
<dd>Include unused interfaces</dl>
<h3>known</h3>
<p>Show known assertions of the provided type </p>
<p> The <i>known</i> command shows known assertions of the provided type. If header=value pairs are provided after the assertion type, the assertions shown must also have the specified headers matching the provided values. </p>
<p> <code>Usage</code>: snap [OPTIONS] known [known-OPTIONS]</p>
<dl>
<dt><code>&#8211;remote</code></p>
<dd>Query the store for the assertion, via snapd if possible</p>
<dt><code>&#8211;direct</code></p>
<dd>Query the store for the assertion, without attempting to go via snapd</dl>
<h3>list</h3>
<p>List installed snaps </p>
<p> The <i>list</i> command displays a summary of snaps installed in the current system. </p>
<p> A green check mark (given color and unicode support) after a publisher name indicates that the publisher has been verified. </p>
<p> <code>Usage</code>: snap [OPTIONS] list [list-OPTIONS]</p>
<dl>
<dt><code>&#8211;all</code></p>
<dd>Show all revisions</p>
<dt><code>&#8211;color</code> &lt;default: <i>&quot;auto&quot;</i>&gt;</p>
<dd>Use a little bit of color to highlight some things.</p>
<dt><code>&#8211;unicode</code> &lt;default: <i>&quot;auto&quot;</i>&gt;</p>
<dd>Use a little bit of Unicode to improve legibility.</dl>
<h3>login</h3>
<p>Authenticate to snapd and the store </p>
<p> The <i>login</i> command authenticates the user to snapd and the snap store, and saves credentials into the ~/.snap/auth.json file. Further communication with snapd will then be made using those credentials. </p>
<p> It&#8217;s not necessary to log in to interact with snapd. Doing so, however, enables interactions without sudo, as well as some some developer-oriented features as detailed in the help for the find, install and refresh commands. </p>
<p> An account can be set up at <a rel="nofollow" href="https://login.ubuntu.com">https://login.ubuntu.com</a></p>
<h3>logout</h3>
<p>Log out of snapd and the store </p>
<p> The <i>logout</i> command logs the current user out of snapd and the store.</p>
<h3>logs</h3>
<p>Retrieve logs for services </p>
<p> The <i>logs</i> command fetches logs of the given services and displays them in chronological order. </p>
<p> <code>Usage</code>: snap [OPTIONS] logs [logs-OPTIONS]</p>
<dl>
<dt><code>&#8211;abs-time</code></p>
<dd>Display absolute times (in RFC 3339 format). Otherwise, display relative times up to 60 days, then YYYY-MM-DD.</p>
<dt><code>-n</code> &lt;default: <i>&quot;10&quot;</i>&gt;</p>
<dd>Show only the given number of lines, or &#8216;all&#8217;.</p>
<dt><code>-f</code></p>
<dd>Wait for new lines and print them as they come in.</dl>
<h3>model</h3>
<p>Get the active model for this device </p>
<p> The <i>model</i> command returns the active model assertion information for this device. </p>
<p> By default, only the essential model identification information is included in the output, but this can be expanded to include all of an assertion&#8217;s non-meta headers. </p>
<p> The verbose output is presented in a structured, yaml-like format. </p>
<p> Similarly, the active serial assertion can be used for the output instead of the model assertion. </p>
<p> <code>Usage</code>: snap [OPTIONS] model [model-OPTIONS]</p>
<dl>
<dt><code>&#8211;abs-time</code></p>
<dd>Display absolute times (in RFC 3339 format). Otherwise, display relative times up to 60 days, then YYYY-MM-DD.</p>
<dt><code>&#8211;color</code> &lt;default: <i>&quot;auto&quot;</i>&gt;</p>
<dd>Use a little bit of color to highlight some things.</p>
<dt><code>&#8211;unicode</code> &lt;default: <i>&quot;auto&quot;</i>&gt;</p>
<dd>Use a little bit of Unicode to improve legibility.</p>
<dt><code>&#8211;serial</code></p>
<dd>Print the serial assertion instead of the model assertion.</p>
<dt><code>&#8211;verbose</code></p>
<dd>Print all specific assertion fields.</p>
<dt><code>&#8211;assertion</code></p>
<dd>Print the raw assertion.</dl>
<h3>okay</h3>
<p>Acknowledge warnings </p>
<p> The <i>okay</i> command acknowledges the warnings listed with &#8216;snap warnings&#8217;. </p>
<p> Once acknowledged a warning won&#8217;t appear again unless it re-occurrs and sufficient time has passed.</p>
<h3>pack</h3>
<p>Pack the given directory as a snap </p>
<p> The <i>pack</i> command packs the given snap-dir as a snap and writes the result to target-dir. If target-dir is omitted, the result is written to current directory. If both source-dir and target-dir are omitted, the pack command packs the current directory. </p>
<p> The default file name for a snap can be derived entirely from its snap.yaml, but in some situations it&#8217;s simpler for a script to feed the filename in. In those cases, &#8211;filename can be given to override the default. If this filename is not absolute it will be taken as relative to target-dir. </p>
<p> When used with &#8211;check-skeleton, pack only checks whether snap-dir contains valid snap metadata and raises an error otherwise. Application commands listed in snap metadata file, but appearing with incorrect permission bits result in an error. Commands that are missing from snap-dir are listed in diagnostic messages. </p>
<p> <code>Usage</code>: snap [OPTIONS] pack [pack-OPTIONS]</p>
<dl>
<dt><code>&#8211;check-skeleton</code></p>
<dd>Validate snap-dir metadata only</p>
<dt><code>&#8211;filename</code></p>
<dd>Output to this filename</p>
<dt><code>&#8211;compression</code></p>
<dd>Compression to use (e.g. xz or lzo)</dl>
<h3>prefer</h3>
<p>Enable aliases from a snap, disabling any conflicting aliases </p>
<p> The <i>prefer</i> command enables all aliases of the given snap in preference to conflicting aliases of other snaps whose aliases will be disabled (or removed, for manual ones). </p>
<p> <code>Usage</code>: snap [OPTIONS] prefer [prefer-OPTIONS]</p>
<dl>
<dt><code>&#8211;no-wait</code></p>
<dd>Do not wait for the operation to finish but just print the change id.</dl>
<h3>prepare-image</h3>
<p>Prepare a device image </p>
<p> The <i>prepare-image</i> command performs some of the steps necessary for creating device images. </p>
<p> For core images it is not invoked directly but usually via ubuntu-image. </p>
<p> For preparing classic images it supports a &#8211;classic mode </p>
<p> <code>Usage</code>: snap [OPTIONS] prepare-image [prepare-image-OPTIONS]</p>
<dl>
<dt><code>&#8211;classic</code></p>
<dd>Enable classic mode to prepare a classic model image</p>
<dt><code>&#8211;preseed</code></p>
<dd>Preseed (UC20+ only)</p>
<dt><code>&#8211;preseed-sign-key</code></p>
<dd>Name of the key to use to sign preseed assertion, otherwise use the default key</p>
<dt><code>&#8211;apparmor-features-dir</code></p>
<dd>Optional path to apparmor kernel features directory (UC20+ only)</p>
<dt><code>&#8211;sysfs-overlay</code></p>
<dd>Optional sysfs overlay to be used when running preseeding steps</p>
<dt><code>&#8211;arch</code></p>
<dd>Specify an architecture for snaps for &#8211;classic when the model does not</p>
<dt><code>&#8211;channel</code></p>
<dd>The channel to use</p>
<dt><code>&#8211;snap</code> <i>&lt;snap&gt;[=&lt;channel&gt;]</i></p>
<dd>Include the given snap from the store or a local file and/or specify the channel to track for the given snap</dl>
<h3>reboot</h3>
<p>Reboot into selected system and mode </p>
<p> The <i>reboot</i> command reboots the system into a particular mode of the selected recovery system. </p>
<p> When called without a system label and without a mode it will just trigger a regular reboot. </p>
<p> When called without a system label but with a mode it will use the current system to enter the given mode. </p>
<p> Note that &quot;recover&quot;, &quot;factory-reset&quot; and &quot;run&quot; modes are only available for the current system. </p>
<p> <code>Usage</code>: snap [OPTIONS] reboot [reboot-OPTIONS]</p>
<dl>
<dt><code>&#8211;run</code></p>
<dd>Boot into run mode</p>
<dt><code>&#8211;install</code></p>
<dd>Boot into install mode</p>
<dt><code>&#8211;recover</code></p>
<dd>Boot into recover mode</p>
<dt><code>&#8211;factory-reset</code></p>
<dd>Boot into factory-reset mode</dl>
<h3>recovery</h3>
<p>List available recovery systems </p>
<p> The <i>recovery</i> command lists the available recovery systems. </p>
<p> With &#8211;show-keys it displays recovery keys that can be used to unlock the encrypted partitions if the device-specific automatic unlocking does not work. </p>
<p> <code>Usage</code>: snap [OPTIONS] recovery [recovery-OPTIONS]</p>
<dl>
<dt><code>&#8211;color</code> &lt;default: <i>&quot;auto&quot;</i>&gt;</p>
<dd>Use a little bit of color to highlight some things.</p>
<dt><code>&#8211;unicode</code> &lt;default: <i>&quot;auto&quot;</i>&gt;</p>
<dd>Use a little bit of Unicode to improve legibility.</p>
<dt><code>&#8211;show-keys</code></p>
<dd>Show recovery keys (if available) to unlock encrypted partitions.</dl>
<h3>refresh</h3>
<p>Refresh snaps in the system </p>
<p> The <i>refresh</i> command updates the specified snaps, or all snaps in the system if none are specified. </p>
<p> With no further options, the snaps are refreshed to the current revision of the channel they&#8217;re tracking, preserving their confinement options. All available channels of a snap are listed in its &#8216;snap info&#8217; output. </p>
<p> Revision choice via the &#8211;revision override requires the user to have developer access to the snap, either directly or through the store&#8217;s collaboration feature, and to be logged in (see &#8216;snap help login&#8217;). </p>
<p> Note a later refresh will typically undo a revision override. </p>
<p> Hold (&#8211;hold) is used to postpone snap refresh updates for all snaps when no snaps are specified, or for the specified snaps. </p>
<p> When no snaps are specified &#8211;hold is only effective on auto-refreshes and will not block either general refresh requests from &#8216;snap refresh&#8217; or specific snap requests from &#8216;snap refresh target-snap&#8217;. </p>
<p> When snaps are specified &#8211;hold is effective on both their auto-refreshes and general refresh requests from &#8216;snap refresh&#8217;. However, specific snap requests from &#8216;snap refresh target-snap&#8217; remain unblocked and will proceed. </p>
<p> <code>Usage</code>: snap [OPTIONS] refresh [refresh-OPTIONS]</p>
<dl>
<dt><code>&#8211;color</code> &lt;default: <i>&quot;auto&quot;</i>&gt;</p>
<dd>Use a little bit of color to highlight some things.</p>
<dt><code>&#8211;unicode</code> &lt;default: <i>&quot;auto&quot;</i>&gt;</p>
<dd>Use a little bit of Unicode to improve legibility.</p>
<dt><code>&#8211;abs-time</code></p>
<dd>Display absolute times (in RFC 3339 format). Otherwise, display relative times up to 60 days, then YYYY-MM-DD.</p>
<dt><code>&#8211;no-wait</code></p>
<dd>Do not wait for the operation to finish but just print the change id.</p>
<dt><code>&#8211;channel</code></p>
<dd>Use this channel instead of stable</p>
<dt><code>&#8211;edge</code></p>
<dd>Install from the edge channel</p>
<dt><code>&#8211;beta</code></p>
<dd>Install from the beta channel</p>
<dt><code>&#8211;candidate</code></p>
<dd>Install from the candidate channel</p>
<dt><code>&#8211;stable</code></p>
<dd>Install from the stable channel</p>
<dt><code>&#8211;devmode</code></p>
<dd>Put snap in development mode and disable security confinement</p>
<dt><code>&#8211;jailmode</code></p>
<dd>Put snap in enforced confinement mode</p>
<dt><code>&#8211;classic</code></p>
<dd>Put snap in classic mode and disable security confinement</p>
<dt><code>&#8211;amend</code></p>
<dd>Allow refresh attempt on snap unknown to the store</p>
<dt><code>&#8211;revision</code></p>
<dd>Refresh to the given revision, to which you must have developer access</p>
<dt><code>&#8211;cohort</code></p>
<dd>Refresh the snap into the given cohort</p>
<dt><code>&#8211;leave-cohort</code></p>
<dd>Refresh the snap out of its cohort</p>
<dt><code>&#8211;list</code></p>
<dd>Show the new versions of snaps that would be updated with the next refresh</p>
<dt><code>&#8211;time</code></p>
<dd>Show auto refresh information but do not perform a refresh</p>
<dt><code>&#8211;ignore-validation</code></p>
<dd>Ignore validation by other snaps blocking the refresh</p>
<dt><code>&#8211;transaction</code> &lt;default: <i>&quot;per-snap&quot;</i>&gt;</p>
<dd>Have one transaction per-snap or one for all the specified snaps</p>
<dt><code>&#8211;hold</code> [<i>=&quot;forever&quot;</i>]</p>
<dd>Hold refreshes for a specified duration (or forever, if no value is specified)</p>
<dt><code>&#8211;unhold</code></p>
<dd>Remove refresh hold</dl>
<h3>remove</h3>
<p>Remove snaps from the system </p>
<p> The <i>remove</i> command removes the named snap instance from the system. </p>
<p> By default all the snap revisions are removed, including their data and the common data directory. When a &#8211;revision option is passed only the specified revision is removed. </p>
<p> Unless automatic snapshots are disabled, a snapshot of all data for the snap is saved upon removal, which is then available for future restoration with snap restore. The &#8211;purge option disables automatically creating snapshots. </p>
<p> <code>Usage</code>: snap [OPTIONS] remove [remove-OPTIONS]</p>
<dl>
<dt><code>&#8211;no-wait</code></p>
<dd>Do not wait for the operation to finish but just print the change id.</p>
<dt><code>&#8211;revision</code></p>
<dd>Remove only the given revision</p>
<dt><code>&#8211;purge</code></p>
<dd>Remove the snap without saving a snapshot of its data</dl>
<h3>restart</h3>
<p>Restart services </p>
<p> The <i>restart</i> command restarts the given services. </p>
<p> If the &#8211;reload option is given, for each service whose app has a reload command, a reload is performed instead of a restart. </p>
<p> <code>Usage</code>: snap [OPTIONS] restart [restart-OPTIONS]</p>
<dl>
<dt><code>&#8211;no-wait</code></p>
<dd>Do not wait for the operation to finish but just print the change id.</p>
<dt><code>&#8211;reload</code></p>
<dd>If the service has a reload command, use it instead of restarting.</dl>
<h3>restore</h3>
<p>Restore a snapshot </p>
<p> The <i>restore</i> command replaces the current user, system and configuration data of included snaps, with the corresponding data from the specified snapshot. </p>
<p> By default, this command restores all the data in a snapshot. Alternatively, you can specify the data of which snaps to restore, or for which users, or a combination of these. </p>
<p> If a snap is included in a restore operation, excluding its system and configuration data from the restore is not currently possible. This restriction may be lifted in the future. </p>
<p> <code>Usage</code>: snap [OPTIONS] restore [restore-OPTIONS]</p>
<dl>
<dt><code>&#8211;no-wait</code></p>
<dd>Do not wait for the operation to finish but just print the change id.</p>
<dt><code>&#8211;users</code></p>
<dd>Restore data of only specific users (comma-separated) (default: all users)</dl>
<h3>revert</h3>
<p>Reverts the given snap to the previous state </p>
<p> The <i>revert</i> command reverts the given snap to its state before the latest refresh. This will reactivate the previous snap revision, and will use the original data that was associated with that revision, discarding any data changes that were done by the latest revision. As an exception, data which the snap explicitly chooses to share across revisions is not touched by the revert process. </p>
<p> <code>Usage</code>: snap [OPTIONS] revert [revert-OPTIONS]</p>
<dl>
<dt><code>&#8211;no-wait</code></p>
<dd>Do not wait for the operation to finish but just print the change id.</p>
<dt><code>&#8211;devmode</code></p>
<dd>Put snap in development mode and disable security confinement</p>
<dt><code>&#8211;jailmode</code></p>
<dd>Put snap in enforced confinement mode</p>
<dt><code>&#8211;classic</code></p>
<dd>Put snap in classic mode and disable security confinement</p>
<dt><code>&#8211;revision</code></p>
<dd>Revert to the given revision</dl>
<h3>run</h3>
<p>Run the given snap command </p>
<p> The <i>run</i> command executes the given snap command with the right confinement and environment. </p>
<p> <code>Usage</code>: snap [OPTIONS] run [run-OPTIONS] &lt;NAME-OF-SNAP&gt;.&lt;NAME-OF-APP&gt; [&lt;SNAP-APP-ARG&gt;&#8230;]</p>
<dl>
<dt><code>&#8211;shell</code></p>
<dd>Run a shell instead of the command (useful for debugging)</p>
<dt><code>&#8211;debug-log</code></p>
<dd>Enable debug logging during early snap startup phases</p>
<dt><code>&#8211;strace</code> [<i>=&quot;with-strace&quot;</i>] &lt;default: <i>&quot;no-strace&quot;</i>&gt;</p>
<dd>Run the command under strace (useful for debugging). Extra strace options can be specified as well here. Pass &#8211;raw to strace early snap helpers.</p>
<dt><code>&#8211;gdbserver</code> [<i>=&quot;:0&quot;</i>] &lt;default: <i>&quot;no-gdbserver&quot;</i>&gt;</p>
<dd>Run the command with gdbserver</p>
<dt><code>&#8211;trace-exec</code></p>
<dd>Display exec calls timing data</dl>
<h3>save</h3>
<p>Save a snapshot of the current data </p>
<p> The <i>save</i> command creates a snapshot of the current user, system and configuration data for the given snaps. </p>
<p> By default, this command saves the data of all snaps for all users. Alternatively, you can specify the data of which snaps to save, or for which users, or a combination of these. </p>
<p> If a snap is included in a save operation, excluding its system and configuration data from the snapshot is not currently possible. This restriction may be lifted in the future. </p>
<p> <code>Usage</code>: snap [OPTIONS] save [save-OPTIONS]</p>
<dl>
<dt><code>&#8211;no-wait</code></p>
<dd>Do not wait for the operation to finish but just print the change id.</p>
<dt><code>&#8211;abs-time</code></p>
<dd>Display absolute times (in RFC 3339 format). Otherwise, display short relative times.</p>
<dt><code>&#8211;users</code></p>
<dd>Snapshot data of only specific users (comma-separated) (default: all users)</dl>
<h3>saved</h3>
<p>List currently stored snapshots </p>
<p> The <i>saved</i> command displays a list of snapshots that have been created previously with the &#8216;save&#8217; command. </p>
<p> <code>Usage</code>: snap [OPTIONS] saved [saved-OPTIONS]</p>
<dl>
<dt><code>&#8211;abs-time</code></p>
<dd>Display absolute times (in RFC 3339 format). Otherwise, display short relative times.</p>
<dt><code>&#8211;id</code></p>
<dd>Show only a specific snapshot.</dl>
<h3>services</h3>
<p>Query the status of services </p>
<p> The <i>services</i> command lists information about the services specified, or about the services in all currently installed snaps.</p>
<h3>set</h3>
<p>Change configuration options </p>
<p> The <i>set</i> command changes the provided configuration options as requested. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;$&nbsp;snap set snap-name username=frank password=$PASSWORD </p>
<p> All configuration changes are persisted at once, and only after the snap&#8217;s configuration hook returns successfully. </p>
<p> Nested values may be modified via a dotted path: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;$&nbsp;snap set snap-name author.name=frank </p>
<p> Configuration option may be unset with exclamation mark:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;$&nbsp;snap set snap-name author! </p>
<p> <code>Usage</code>: snap [OPTIONS] set [set-OPTIONS]</p>
<dl>
<dt><code>&#8211;no-wait</code></p>
<dd>Do not wait for the operation to finish but just print the change id.</p>
<dt><code>-t</code></p>
<dd>Parse the value strictly as JSON document</p>
<dt><code>-s</code></p>
<dd>Parse the value as a string</dl>
<h3>start</h3>
<p>Start services </p>
<p> The <i>start</i> command starts, and optionally enables, the given services. </p>
<p> <code>Usage</code>: snap [OPTIONS] start [start-OPTIONS]</p>
<dl>
<dt><code>&#8211;no-wait</code></p>
<dd>Do not wait for the operation to finish but just print the change id.</p>
<dt><code>&#8211;enable</code></p>
<dd>As well as starting the service now, arrange for it to be started on boot.</dl>
<h3>stop</h3>
<p>Stop services </p>
<p> The <i>stop</i> command stops, and optionally disables, the given services. </p>
<p> <code>Usage</code>: snap [OPTIONS] stop [stop-OPTIONS]</p>
<dl>
<dt><code>&#8211;no-wait</code></p>
<dd>Do not wait for the operation to finish but just print the change id.</p>
<dt><code>&#8211;disable</code></p>
<dd>As well as stopping the service now, arrange for it to no longer be started on boot.</dl>
<h3>switch</h3>
<p>Switches snap to a different channel </p>
<p> The <i>switch</i> command switches the given snap to a different channel without doing a refresh. All available channels of a snap are listed in its &#8216;snap info&#8217; output. </p>
<p> <code>Usage</code>: snap [OPTIONS] switch [switch-OPTIONS]</p>
<dl>
<dt><code>&#8211;no-wait</code></p>
<dd>Do not wait for the operation to finish but just print the change id.</p>
<dt><code>&#8211;channel</code></p>
<dd>Use this channel instead of stable</p>
<dt><code>&#8211;edge</code></p>
<dd>Install from the edge channel</p>
<dt><code>&#8211;beta</code></p>
<dd>Install from the beta channel</p>
<dt><code>&#8211;candidate</code></p>
<dd>Install from the candidate channel</p>
<dt><code>&#8211;stable</code></p>
<dd>Install from the stable channel</p>
<dt><code>&#8211;cohort</code></p>
<dd>Switch the snap into the given cohort</p>
<dt><code>&#8211;leave-cohort</code></p>
<dd>Switch the snap out of its cohort</dl>
<h3>tasks</h3>
<p>List a change&#8217;s tasks </p>
<p> The <i>tasks</i> command displays a summary of tasks associated with an individual change. </p>
<p> <code>Usage</code>: snap [OPTIONS] tasks [tasks-OPTIONS]</p>
<dl>
<dd><code>Aliases</code>: change </p>
<dt><code>&#8211;abs-time</code></p>
<dd>Display absolute times (in RFC 3339 format). Otherwise, display relative times up to 60 days, then YYYY-MM-DD.</p>
<dt><code>&#8211;last</code></p>
<dd>Select last change of given type (install, refresh, remove, try, auto-refresh, etc.). A question mark at the end of the type means to do nothing (instead of returning an error) if no change of the given type is found. Note the question mark could need protecting from the shell.</dl>
<h3>try</h3>
<p>Test an unpacked snap in the system </p>
<p> The <i>try</i> command installs an unpacked snap into the system for testing purposes. The unpacked snap content continues to be used even after installation, so non-metadata changes there go live instantly. Metadata changes such as those performed in snap.yaml will require reinstallation to go live. </p>
<p> If snap-dir argument is omitted, the try command will attempt to infer it if either snapcraft.yaml file and prime directory or meta/snap.yaml file can be found relative to current working directory. </p>
<p> <code>Usage</code>: snap [OPTIONS] try [try-OPTIONS]</p>
<dl>
<dt><code>&#8211;no-wait</code></p>
<dd>Do not wait for the operation to finish but just print the change id.</p>
<dt><code>&#8211;devmode</code></p>
<dd>Put snap in development mode and disable security confinement</p>
<dt><code>&#8211;jailmode</code></p>
<dd>Put snap in enforced confinement mode</p>
<dt><code>&#8211;classic</code></p>
<dd>Put snap in classic mode and disable security confinement</dl>
<h3>unalias</h3>
<p>Remove a manual alias, or the aliases for an entire snap </p>
<p> The <i>unalias</i> command removes a single alias if the provided argument is a manual alias, or disables all aliases of a snap, including manual ones, if the argument is a snap name. </p>
<p> <code>Usage</code>: snap [OPTIONS] unalias [unalias-OPTIONS]</p>
<dl>
<dt><code>&#8211;no-wait</code></p>
<dd>Do not wait for the operation to finish but just print the change id.</dl>
<h3>unset</h3>
<p>Remove configuration options </p>
<p> The <i>unset</i> command removes the provided configuration options as requested. </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>$ snap unset snap-name name address</p>
<p> All configuration changes are persisted at once, and only after the snap&#8217;s configuration hook returns successfully. </p>
<p> Nested values may be removed via a dotted path: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>$ snap unset snap-name user.name</p>
<p> <code>Usage</code>: snap [OPTIONS] unset [unset-OPTIONS]</p>
<dl>
<dt><code>&#8211;no-wait</code></p>
<dd>Do not wait for the operation to finish but just print the change id.</dl>
<h3>version</h3>
<p>Show version details </p>
<p> The <i>version</i> command displays the versions of the running client, server, and operating system.</p>
<h3>wait</h3>
<p>Wait for configuration </p>
<p> The <i>wait</i> command waits until a configuration becomes true.</p>
<h3>warnings</h3>
<p>List warnings </p>
<p> The <i>warnings</i> command lists the warnings that have been reported to the system. </p>
<p> Once warnings have been listed with &#8216;snap warnings&#8217;, &#8216;snap okay&#8217; may be used to silence them. A warning that&#8217;s been silenced in this way will not be listed again unless it happens again, _and_ a cooldown time has passed. </p>
<p> Warnings expire automatically, and once expired they are forgotten. </p>
<p> <code>Usage</code>: snap [OPTIONS] warnings [warnings-OPTIONS]</p>
<dl>
<dt><code>&#8211;abs-time</code></p>
<dd>Display absolute times (in RFC 3339 format). Otherwise, display relative times up to 60 days, then YYYY-MM-DD.</p>
<dt><code>&#8211;unicode</code> &lt;default: <i>&quot;auto&quot;</i>&gt;</p>
<dd>Use a little bit of Unicode to improve legibility.</p>
<dt><code>&#8211;all</code></p>
<dd>Show all warnings</p>
<dt><code>&#8211;verbose</code></p>
<dd>Show more information</dl>
<h3>watch</h3>
<p>Watch a change in progress </p>
<p> The <i>watch</i> command waits for the given change-id to finish and shows progress (if available). </p>
<p> <code>Usage</code>: snap [OPTIONS] watch [watch-OPTIONS]</p>
<dl>
<dt><code>&#8211;last</code></p>
<dd>Select last change of given type (install, refresh, remove, try, auto-refresh, etc.). A question mark at the end of the type means to do nothing (instead of returning an error) if no change of the given type is found. Note the question mark could need protecting from the shell.</dl>
<h3>whoami</h3>
<p>Show the email the user is logged in with </p>
<p> The <i>whoami</i> command shows the email the user is logged in with.</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>Online documentation</p>
<dl>
<dd><a rel="nofollow" href="https://docs.snapcraft.io">https://docs.snapcraft.io</a></dl>
</dl>
<h2>Bugs</h2>
<p>Please report all bugs with <i><a rel="nofollow" href="https://bugs.launchpad.net/snapd/+filebug">https://bugs.launchpad.net/snapd/+filebug</a></i> </p>
