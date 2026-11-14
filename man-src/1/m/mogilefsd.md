---
title: "mogilefsd(1)"
name: "mogilefsd"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mogilefsd/"
description: "mogilefsd — MogileFS tracker daemon"
---

<h2 class="name">NAME</h2>
<p> mogilefsd &#8212; MogileFS tracker daemon </p>
<h2>USAGE</h2>
<p> This is the main MogileFS daemon, mogilefsd, also called the &#8220;tracker&#8221;. All interaction with a MogileFS installation begins by a client talking to a tracker (you should run several in parallel for redundancy). </p>
<p> See MogileFS::Client for a client library.</p>
<h2>ARCHITECTURE</h2>
<h2>Processes</h2>
<p> The mogilefsd daemon is an event-loop in the parent process, handling with epoll/kqueue/etc (see Danga::Socket) tons of client connections, while managing a bunch of worker processes underneath. </p>
<p> The worker processes under mogilefsd include:</p>
<dl>
<dt><code>Client query processing</code> &#8212; implements the MogileFS client/server protocol</p>
<dd> See MogileFS::Worker::Query.</p>
<dt><code>Monitoring</code> &#8212; monitors hosts and devices</p>
<dd> See MogileFS::Worker::Monitor.</p>
<dt><code>Replicate</code> &#8212; replicates files</p>
<dd> See MogileFS::Worker::Replicate.</p>
<dt><code>Deleter</code> &#8212; deletes files from storage nodes (protocol deletes from namespace are immediate)</p>
<dd> See MogileFS::Worker::Delete.</p>
<dt><code>Reaper</code> &#8212; re-enqueues files for replication when disks are marked dead</p>
<dd> See MogileFS::Worker::Reaper.</p>
<dt><code>Checker/Fsck</code> &#8212; background filesystem consistency checker</p>
<dd> See MogileFS::Worker::Checker.</dl>
<h2>Data Storage</h2>
<p> See MogileFS::Store.</p>
<h2>AUTHORS</h2>
<p> Brad Fitzpatrick &lt;brad [at] danga.com&gt; </p>
<p> Mark Smith &lt;junior [at] danga.com&gt; </p>
<p> Brad Whitaker &lt;whitaker [at] danga.com&gt;</p>
<h2>COPYRIGHT</h2>
<pre>
 Copyright 2004, Danga Interactive
 Copyright 2005-2006, Six Apart Ltd.
</pre>
<h2>LICENSE</h2>
<p> Same terms as Perl itself. Artistic/GPLv2, at your choosing.</p>
<h2>SEE ALSO</h2>
<p> mogstored &#8212; MogileFS storage daemon </p>
<p> &lt;<a rel="nofollow" href="http://danga.com/mogilefs/">http://danga.com/mogilefs/</a>&gt; </p>
<h2>Index</h2>
