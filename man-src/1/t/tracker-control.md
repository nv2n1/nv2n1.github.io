---
title: "tracker-control(1)"
name: "tracker-control"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tracker-control/"
description: "tracker-control – Manage Tracker processes and data"
---

<h2 class="name">NAME</h2>
<p> tracker-control &#8211; Manage Tracker processes and data</p>
<h2>SYNOPSIS</h2>
<p> <code>tracker-control</code> [<i>OPTION</i>&#8230;] </p>
<h2>DESCRIPTION</h2>
<p> <code>tracker-control</code> manages and checks status of all Tracker processes and data. </p>
<p> Controls Tracker both at process level, and at entity level (store, miners). </p>
<p> To start or stop miners, you can use <code>&#8211;start.</code> The store is started automatically by the D-Bus calls from the miners. </p>
<p> It also allows checking the status of the Tracker store and all data miners. For <code>tracker-store</code> , the status is always <code>Idle</code> unless it is restoring a backup and/or replaying a journal (regardless of load from applications or miners). For a list of common statuses, see <code>&#8211;list-common-statuses.</code> </p>
<p> The miners can be paused or resumed using this command and you can also list miners running and available. </p>
<h2>COMMON OPTIONS</h2>
<dl>
<dt><code>-?, &#8211;help</code></p>
<dd> Show summary of options by group.</p>
<dt><code>-?, &#8211;help-all</code></p>
<dd> Show all groups and options.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Returns the version of this program. </p>
</dl>
<h2>GENERAL OPTIONS</h2>
<dl>
<dt><code>-p, &#8211;list-processes</code></p>
<dd> This lists all Tracker processes in the system.</p>
<dt><code>-k, &#8211;kill=[all|store|miners]</code></p>
<dd> This uses SIGKILL to stop all Tracker processes found matching the parameter, if no extra parameter is passed, <code>all</code> will be assumed. This is not advised unless you are having problems stopping Tracker in the first place. This <code>GUARANTEES</code> death.</p>
<dt><code>-t, &#8211;terminate=[all|store|miners]</code></p>
<dd> This uses SIGTERM to stop all Tracker processes found matching the parameter, if no extra parameter is passed, <code>all</code> will be assumed. This is recommended over &#8211;kill because it gives the processes time to shutdown cleanly.</p>
<dt><code>-r, &#8211;hard-reset</code></p>
<dd> This kills all processes in the same way that <code>&#8211;kill</code> does but it also removes all databases. Restarting <code>tracker-store</code> re-creates the databases.</p>
<dt><code>-e, &#8211;soft-reset</code></p>
<dd> A soft reset works exactly the same way that <code>&#8211;hard-reset</code> does, with the exception that the backup and journal are not removed. These are restored when <code>tracker-store</code> is restarted.</p>
<dt><code>-c, &#8211;remove-config</code></p>
<dd> This removes all config files in $HOME/.config/tracker. All files listed are files which were found and successfully removed. Restarting the respective processes re-creates the default configuration files.</p>
<dt><code>-s, &#8211;start</code></p>
<dd> Starts all miners. This indirectly starts tracker-store too because it is needed for miners to operate properly.</p>
<dt><code>-b, &#8211;backup=FILE</code></p>
<dd> Begins backing up the Tracker databases to the <code>FILE</code> given.</p>
<dt><code>-o, &#8211;restore=FILE</code></p>
<dd> Begins restoring a previous backup (see <code>&#8211;backup</code> ) to the Tracker databases. The <code>FILE</code> points to the location of the backup.</p>
<dt><code>&#8211;get-log-verbosity</code></p>
<dd> This displays the log verbosity for ALL components using GSettings for this configuration. For possible values, see <code>&#8211;set-log-verbosity.</code></p>
<dt><code>&#8211;set-log-verbosity=[debug|detailed|minimal|errors]</code></p>
<dd> This sets the log verbosity for ALL components using GSettings using this configuration option (&#8216;verbosity&#8217;).</p>
<dt><code>&#8211;collect-debug-info</code></p>
<dd> Useful when debugging problems to diagnose the state of Tracker on your system. The data is output to stdout. Useful if bugs are filed against the project itself. </p>
<p> Data collected includes Tracker version in use, disk space available, size of the databases on the disk, the configuration in use, states of the index (e.g. last filesystem crawl, data set locale, etc.) and finally statistics about the data in the database (e.g. how many nfo:FileDataObject resources exist). </p>
</dl>
<h2>STATUS OPTIONS</h2>
<dl>
<dt><code>-S, &#8211;status</code></p>
<dd> Show the current status of all Tracker entities (store and all available miners).</p>
<dt><code>-F, &#8211;follow</code></p>
<dd> Follow status changes as they happen. This requires Ctrl+C to stop and return to the command line. Each new status is put on a new line.</p>
<dt><code>-w, &#8211;watch=[ONTOLOGY]</code></p>
<dd> Watch changes that happen to the database in real time. This requires Ctrl+C to stop and return to the command line. </p>
<p> If the <code>ONTOLOGY</code> is unspecified, all changes are shown. The <code>ONTOLOGY</code> can be a comma separated list of shorthand or long hand ontology properties. For example: </p>
<pre>
    $ tracker-control -w nie:url,nie:mimeType,nfo:fileSize,nie:dataSource
    Now listening for resource updates to the database
    All nie:plainTextContent properties are omitted
    Press Ctrl+C to stop
    'nfo:Document'
       'nfo:fileSize' = '1770'
       'nie:dataSource' = '<a rel="nofollow" href="http://www.tracker-project.org/ontologies/tracker#extractor-data-source'">http://www.tracker-project.org/ontologies/tracker#extractor-data-source'</a>
       'nie:mimeType' = 'text/plain'
       'nie:url' = 'file:///home/martyn/.bash_aliases'
    'nfo:Document'
       'nie:dataSource' = '<a rel="nofollow" href="http://www.tracker-project.org/ontologies/tracker#extractor-data-source'">http://www.tracker-project.org/ontologies/tracker#extractor-data-source'</a>
    ...
</pre>
<dt><code>&#8211;list-common-statuses</code></p>
<dd> This will list statuses most commonly produced by miners and the store. These statuses are not translated when sent over D-Bus and should be translated by each application. These are not considered static and are subject to change at any point. </p>
<p> Additionally, these statuses are not the only ones which may be reported by a miner. There may be other states pertaining to the specific roles of the miner in question. </p>
</dl>
<h2>MINER OPTIONS</h2>
<dl>
<dt><code>-m, &#8211;reindex-mime-type=MIME</code></p>
<dd> Re-index files which match the <i>MIME</i> type supplied. This is usually used when installing new extractors which support <i>MIME</i> types previously unsupported. This forces Tracker to re-index those files. You can use <code>&#8211;reindex-mime-type</code> more than once per <i>MIME</i> type.</p>
<dt><code>-f, &#8211;index-file=FILE</code></p>
<dd> (Re)index a file matching the <i>FILE</i> type supplied.</p>
<dt><code>&#8211;list-miners-running</code></p>
<dd> This will list all miners which have responded to a D-Bus call. Sometimes it is helpfult to use this command with <code>&#8211;list-miners-available.</code></p>
<dt><code>&#8211;list-miners-available</code></p>
<dd> This will list all miners which are available even if they are not running at the moment.</p>
<dt><code>&#8211;pause-details</code></p>
<dd> For listing all miners which are paused and the reasons for being paused, you can use this. It will also display the application that requested the pause too.</p>
<dt><code>&#8211;miner=MINER</code></p>
<dd> This argument is used with <code>&#8211;pause</code> or <code>&#8211;resume</code> to say which miner you want to pause or resume. You can use the full D-Bus name, e.g. <code>org.freedesktop.Tracker1.Miner.Files</code> OR you can use the suffix, e.g. <code>Files</code></p>
<dt><code>&#8211;pause=REASON</code></p>
<dd> The REASON here is useful to know WHY the miner should be paused. A miner can be paused many times by multiple applications. Only when all pauses have been resumed will it continue. If successful, a cookie will be given to uniquely identify the request. This cookie is used to resume the pause at a later stage.</p>
<dt><code>&#8211;pause-for-process=REASON</code></p>
<dd> This works exactly the same way as <code>&#8211;pause</code> with the exception that it only keeps the pause active while the calling process is alive. As soon as you press Ctrl+C the pause is resumed automatically.</p>
<dt><code>&#8211;resume=COOKIE</code></p>
<dd> The COOKIE is given by a successful <code>&#8211;pause</code> command. It is a number which identifies each pause request. When all pauses have been resumed, the miner will resume working. </p>
</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>TRACKER_MINERS_DIR</code></p>
<dd> Miners that are installed should have a .desktop file in /usr/share/tracker/miners/, this is how tracker-control knows about miners which exist but may not have not been started. This environment variable allows the location that miner .desktop files are loaded from to be overridden by setting it to a new path.</p>
<dt><code>TRACKER_MINERS_DIR_DISABLED</code></p>
<dd> If you don&#8217;t have .desktop files for miners, you can use this environment variable to get status information from <code>RUNNING</code> processes. This doesn&#8217;t give any indication for miners <code>NOT</code> running. This uses registered miners on DBus to know about existing Tracker based data miners. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tracker-store/">tracker-store</a></code>(1). </p>
<h2>Index</h2>
