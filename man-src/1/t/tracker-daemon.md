---
title: "tracker-daemon(1)"
name: "tracker-daemon"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tracker-daemon/"
description: "tracker-daemon – Start, stop, restart and list daemons responsible for indexing content"
---

<h2 class="name">NAME</h2>
<p> tracker-daemon &#8211; Start, stop, restart and list daemons responsible for indexing content</p>
<h2>SYNOPSIS</h2>
<pre><code>
tracker daemon [options...]
tracker daemon -s | -t [daemons] | -k [daemons] | -l
tracker daemon -f | -w [ontology]
tracker daemon --miner &lt;miner&gt; --pause[-for-process] &lt;reason&gt;
tracker daemon --miner &lt;miner&gt; --resume &lt;cookie&gt;
</code></pre>
<h2>DESCRIPTION</h2>
<p> Tracker has many components to it including a &quot;store&quot; for handling data set updates and &quot;miners&quot; for handling data mining in their respective areas. </p>
<p> The <code>tracker daemon</code> command allows for control of these components. This ranges from starting, stopping and killing processes to pausing and resuming them. </p>
<p> In addition to all this, there are ways to change the log verbsity for all processes that generate logs and to follow or watch what is happening in real time from a top level and right down where the SPARQL commits are happening too. </p>
<p> If no arguments are provided this command will show the current status of all Tracker entities (store and all available data miners). </p>
<p> For <code>tracker-store</code>, the status is always &quot;Idle&quot; unless it is restoring a backup and/or replaying a journal (see also <code>tracker reset &#8211;soft</code>). For a list of common statuses, see <code>&#8211;list-common-statuses</code>. </p>
<p> The data miners can be paused or resumed using this command and you can also list miners running and available. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-p, &#8211;list-processes</code></p>
<dd> This lists all Tracker processes in the system.</p>
<dt><code>-k, &#8211;kill</code>=[<i>daemons</i>]</p>
<dd> This uses SIGKILL to stop all Tracker processes found matching the parameter, if no extra parameter is passed, &quot;all&quot; will be assumed. This is not advised unless you are having problems stopping Tracker in the first place. This <code>GUARANTEES</code> death. </p>
<p> The possible <i>daemons</i> options are: </p>
<dl>
<dt>
<dd> &bull; <i>all</i> &#8211; All daemons. </p>
<p> &bull; <i>store</i> &#8211; Only the <code>tracker-store</code>. </p>
<p> &bull; <i>miners</i> &#8211; Only data miners. </p>
</dl>
<dt><code>-t, &#8211;terminate</code>=[daemons]</p>
<dd> This uses SIGTERM to stop all Tracker processes found matching the parameter, if no extra parameter is passed, &quot;all&quot; will be assumed. This is recommended over &#8211;kill because it gives the processes time to shutdown cleanly. </p>
<p> For a list of possible <i>daemons</i>, see &#8211;kill.</p>
<dt><code>-s, &#8211;start</code></p>
<dd> Starts all miners. This indirectly starts <code>tracker-store</code> too because it is needed for miners to operate properly. The store is started from D-Bus.</p>
<dt><code>&#8211;get-log-verbosity</code></p>
<dd> This displays the log verbosity for ALL components using GSettings for this configuration. For possible values, see <code>&#8211;set-log-verbosity.</code></p>
<dt><code>&#8211;set-log-verbosity</code>=&lt;<i>verbosity</i>&gt;</p>
<dd> This sets the log verbosity for ALL daemons using GSettings to store their &quot;verbosity&quot; configuration. </p>
<p> The possible <i>verbosity</i> options are: </p>
<dl>
<dt>
<dd> &bull; <i>debug</i> &#8211; Show EVERYTHING, from debug messages to errors. This often includes actual SQL being executed. </p>
<p> &bull; <i>detailed</i> &#8211; Show enough detail to understand what is happening. </p>
<p> &bull; <i>minimal</i> &#8211; Show an overview of what is going on, e.g. stats and when things start or stop. </p>
<p> &bull; <i>errors</i> &#8211; Show only warnings, criticals, errors or fatal events.</dl>
<dt><code>-f, &#8211;follow</code></p>
<dd> Follow status changes to daemons as they happen. This is a top level view of what is happening. You will see the name for each daemon and a state with the progress in that state. </p>
<p> This requires Ctrl+C to stop and return to the command line. Each new status is put on a new line. </p>
<dt><code>-w, &#8211;watch</code>=[<i>ontology</i>]</p>
<dd> Watch changes that happen to the database in real time. This requires Ctrl+C to stop and return to the command line. </p>
<p> If <i>ontology</i> is unspecified, all updates are shown. The <i>ontology</i> can be a comma separated list of shorthand or long hand ontology properties. For example: </p>
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
<p> Additionally, these statuses are not the only ones which may be reported by a miner. There may be other states pertaining to the specific roles of the miner in question.</p>
<dt><code>&#8211;list-miners-running</code></p>
<dd> This will list all miners which have responded to a D-Bus call. Sometimes it is helpful to use this command with <code>&#8211;list-miners-available.</code></p>
<dt><code>&#8211;list-miners-available</code></p>
<dd> This will list all miners which are available even if they are not running at the moment.</p>
<dt><code>&#8211;pause-details</code></p>
<dd> For listing all miners which are paused and the reasons for being paused, you can use this. It will also display the application that requested the pause too.</p>
<dt><code>&#8211;miner</code>=&lt;<i>miner</i>&gt;</p>
<dd> This argument is used with <code>&#8211;pause</code> or <code>&#8211;resume</code> to say which miner you want to pause or resume. You can use the full D-Bus name, e.g. &quot;org.freedesktop.Tracker1.Miner.Files&quot; OR you can use the suffix, e.g. &quot;Files&quot;.</p>
<dt><code>&#8211;pause</code>=&lt;<i>reason</i>&gt;</p>
<dd> The <i>reason</i> here is useful to know WHY the miner should be paused. A miner can be paused many times by multiple applications. Only when all pauses have been resumed will it continue. If successful, a cookie will be given to uniquely identify the request. This cookie is used to resume the pause at a later stage.</p>
<dt><code>&#8211;pause-for-process</code>=&lt;<i>reason</i>&gt;</p>
<dd> This works exactly the same way as <code>&#8211;pause</code> with the exception that it only keeps the pause active while the calling process is alive. As soon as you press Ctrl+C the pause is resumed automatically.</p>
<dt><code>&#8211;resume</code>=&lt;<i>cookie</i>&gt;</p>
<dd> The <i>cookie</i> is given by a successful <code>&#8211;pause</code> command. It is a number which identifies each pause request. When all pauses have been resumed, the miner will resume working. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tracker-store/">tracker-store</a></code>(1). </p>
<h2>Index</h2>
