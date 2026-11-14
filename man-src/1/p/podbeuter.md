---
title: "podbeuter(1)"
name: "podbeuter"
section: "1"
letter: "p"
url: "/docs/linux/man/1-podbeuter/"
---

<h2 class="name">NAME</h2>
 

 podbeuter - a podcast download manage for text terminals 

<h2>SYNOPSIS</h2>

 <i>podbeuter</i> [-C configfile] [-q queuefile] [-a] [-h] 

<h2>DESCRIPTION</h2>

 <i>podbeuter</i> is a podcast manager for text terminals. It is a helper program to <i>newsbeuter</i> which queues podcast downloads into a file. These queued downloads can then be download with <i>newsbeuter</i>. 

<h2>OPTIONS</h2>

 

 -h
<dl>
<dt>
<dd> Display help</dl>
 

 -C configfile
<dl>
<dt>
<dd> Use an alternative configuration file</dl>
 

 -q queuefile
<dl>
<dt>
<dd> Use an alternative queue file</dl>
 

 -a
<dl>
<dt>
<dd> Start automatic download of all queued files on startup</dl>

<h2>PODCAST SUPPORT</h2>

 A podcast is a media file distributed over the internet using syndication feeds such as RSS, for later playback on portable players or computers. Newsbeuter contains support for downloading and saving podcasts. This support differs a bit from other podcast aggregators or &quot;podcatchers&quot; in how it is done. 

 Podcast content is transported in RSS feeds via special tags called &quot;enclosures&quot;. Newsbeuter recognizes these enclosures and stores the relevant information for every podcast item it finds in an RSS feed. Since version 2.0, it also recognizes and handles the Yahoo Media RSS extensions. What the user then can do is to add the podcast download URL to a download queue. Alternatively, newsbeuter can be configured to automatically do that. This queue is stored in the file $HOME/.newsbeuter/queue. 

 The user can then use the download manager &quot;podbeuter&quot; to download these files to a directory on the local filesystem. Podbeuter comes with the newsbeuter package, and features a look and feel very close to the one of newsbeuter. It also shares the same configuration file. 

 Podcasts that have been downloaded but haven't been played yet remain in the queue but are marked as downloaded. You can remove them by purging them from the queue with the <i>P</i> key. After you've played a file and close podbeuter, it will be removed from the queue. The downloaded file remains on the filesystem. 

<h2>CONFIGURATION COMMANDS</h2>

 

 <i>download-path</i> (parameters: &lt;path&gt;; default value: <i>~/</i>)
<dl>
<dt>
<dd> Specifies the directory where podbeuter shall download the files to. Optionally, the placeholders &quot;%n&quot; (for the podcast feed's name) and &quot;%h&quot; (for the podcast feed's hostname) can be used to place downloads in a directory structure. (example: download-path &quot;~/Downloads/%h/%n&quot;)</dl>
 

 <i>max-downloads</i> (parameters: &lt;number&gt;; default value: <i>1</i>)
<dl>
<dt>
<dd> Specifies the maximum number of parallel downloads when automatic download is enabled. (example: max-downloads 3)</dl>
 

 <i>player</i> (parameters: &lt;player command&gt;; default value: <i>&quot;&quot;</i>)
<dl>
<dt>
<dd> Specifies the player that shall be used for playback of downloaded files. (example: player &quot;mp3blaster&quot;)</dl>

<h2>FILES</h2>

 <i>$HOME/.newsbeuter/config</i> 

 <i>$HOME/.newsbeuter/queue</i> 

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/1-newsbeuter/">newsbeuter</a>(1). The documentation that comes with newsbeuter is a good source about the general use and configuration of newsbeuter's podcast support. 

<h2>AUTHORS</h2>

 Andreas Krennmair &lt;ak [at] newsbeuter.org&gt;, for contributors see AUTHORS file. 

<h2>NOTES</h2>

<dl>
<dt> 1.
<dd> ak [at] newsbeuter.org
<dl>
<dt>
<dd> mailto:ak [at] newsbeuter.org</dl>
 

</dl>

<h2>Index</h2>


