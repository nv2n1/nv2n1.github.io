---
title: "tracker3-daemon(1)"
name: "tracker3-daemon"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tracker3-daemon/"
description: "tracker3-daemon – Start, stop, restart and list daemons responsible for indexing content"
---

<h2 class="name">NAME</h2>
<p> tracker3-daemon &#8211; Start, stop, restart and list daemons responsible for indexing content </p>
<h2>SYNOPSIS</h2>
<pre><code>
tracker3 daemon [options...]
tracker3 daemon -s | -t [daemons] | -k [daemons] | -l
tracker3 daemon -f | -w [ontology]
tracker3 daemon --miner &lt;miner&gt; --pause[-for-process] &lt;reason&gt;
tracker3 daemon --miner &lt;miner&gt; --resume &lt;cookie&gt;
</code></pre>
<h2>DESCRIPTION</h2>
<p> Tracker indexes content with daemon processes that run in the background. The <code>tracker3 daemon</code> command allows for control of these components. This ranges from starting, stopping and killing processes to pausing and resuming them. </p>
<p> In addition to all this, there are ways to follow or watch what is happening in real time from a top level and right down where the SPARQL commits are happening too. </p>
<p> If no arguments are provided this command will show the current status of all Tracker data miners. </p>
<p> The data miners can be paused or resumed using this command and you can also list miners running and available.</p>
<h2>OPTIONS</h2>
<p> <code>-p, &#8211;list-processes</code></p>
<dl>
<dt>
<dd> This lists all Tracker processes in the system.</dl>
<p> *-k, &#8211;kill</p>
<dl>
<dt>
<dd> This uses SIGKILL to stop all Tracker processes found matching the parameter, if no extra parameter is passed, &quot;all&quot; will be assumed. This is not advised unless you are having problems stopping Tracker in the first place. This <code>GUARANTEES</code> death.</dl>
<p> *-t, &#8211;terminate=</p>
<dl>
<dt>
<dd> This uses SIGTERM to stop all Tracker processes. This is recommended over &#8211;kill because it gives the processes time to shutdown cleanly.</dl>
<p> <code>-s, &#8211;start</code></p>
<dl>
<dt>
<dd> Starts all miners.</dl>
<p> <code>-f, &#8211;follow</code></p>
<dl>
<dt>
<dd> Follow status changes to daemons as they happen. This is a top level view of what is happening. You will see the name for each daemon and a state with the progress in that state.</dl>
<p> This requires Ctrl+C to stop and return to the command line. Each new status is put on a new line. </p>
<p> <code>-w, &#8211;watch=[</code><i>ontology</i><code>]</code></p>
<dl>
<dt>
<dd> Watch changes that happen to the database in real time. This requires Ctrl+C to stop and return to the command line.</dl>
<p> If <i>ontology</i> is unspecified, all updates are shown. The <i>ontology</i> can be a comma separated list of shorthand or long hand ontology properties. For example: </p>
<dl>
<dt>
<dd>
<pre>
    $ tracker3 daemon -w nie:url,nie:mimeType,nfo:fileSize,nie:dataSource
    Now listening for resource updates to the database
    All nie:plainTextContent properties are omitted
    Press Ctrl+C to stop
    'nfo:Document'
       'nfo:fileSize' = '1770'
       'nie:dataSource' = '<a rel="nofollow" href="http://tracker.api.gnome.org/ontology/v3/tracker#extractor-data-source'">http://tracker.api.gnome.org/ontology/v3/tracker#extractor-data-source'</a>
       'nie:mimeType' = 'text/plain'
       'nie:url' = 'file:///home/martyn/.bash_aliases'
    'nfo:Document'
       'nie:dataSource' = '<a rel="nofollow" href="http://tracker.api.gnome.org/ontology/v3/tracker#extractor-data-source'">http://tracker.api.gnome.org/ontology/v3/tracker#extractor-data-source'</a>
    ...
</pre>
</dl>
<p> <code>&#8211;list-common-statuses</code></p>
<dl>
<dt>
<dd> This will list statuses most commonly produced by miners and the store. These statuses are not translated when sent over D-Bus and should be translated by each application. These are not considered static and are subject to change at any point.</dl>
<p> Additionally, these statuses are not the only ones which may be reported by a miner. There may be other states pertaining to the specific roles of the miner in question. </p>
<p> <code>&#8211;list-miners-running</code></p>
<dl>
<dt>
<dd> This will list all miners which have responded to a D-Bus call. Sometimes it is helpful to use this command with <code>&#8211;list-miners-available.</code></dl>
<p> <code>&#8211;list-miners-available</code></p>
<dl>
<dt>
<dd> This will list all miners which are available even if they are not running at the moment.</dl>
<p> <code>&#8211;pause-details</code></p>
<dl>
<dt>
<dd> For listing all miners which are paused and the reasons for being paused, you can use this. It will also display the application that requested the pause too.</dl>
<p> <code>&#8211;miner=&lt;</code><i>miner</i><code>&gt;</code></p>
<dl>
<dt>
<dd> This argument is used with <code>&#8211;pause</code> or <code>&#8211;resume</code> to say which miner you want to pause or resume. You can use the full D-Bus name, e.g. &quot;org.freedesktop.Tracker3.Miner.Files&quot; OR you can use the suffix, e.g. &quot;Files&quot;.</dl>
<p> <code>&#8211;pause=&lt;</code><i>reason</i><code>&gt;</code></p>
<dl>
<dt>
<dd> The <i>reason</i> here is useful to know WHY the miner should be paused. A miner can be paused many times by multiple applications. Only when all pauses have been resumed will it continue. If successful, a cookie will be given to uniquely identify the request. This cookie is used to resume the pause at a later stage.</dl>
<p> <code>&#8211;pause-for-process=&lt;</code><i>reason</i><code>&gt;</code></p>
<dl>
<dt>
<dd> This works exactly the same way as <code>&#8211;pause</code> with the exception that it only keeps the pause active while the calling process is alive. As soon as you press Ctrl+C the pause is resumed automatically.</dl>
<p> <code>&#8211;resume=&lt;</code><i>cookie</i><code>&gt;</code></p>
<dl>
<dt>
<dd> The <i>cookie</i> is given by a successful <code>&#8211;pause</code> command. It is a number which identifies each pause request. When all pauses have been resumed, the miner will resume working.</dl>
<h2>Index</h2>
