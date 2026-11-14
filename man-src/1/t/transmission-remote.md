---
title: "transmission-remote(1)"
name: "transmission-remote"
section: "1"
letter: "t"
url: "/docs/linux/man/1-transmission-remote/"
description: "transmission-remote – a remote control utility for transmission-daemon1 and transmission(1)"
---

<h2>NAME</h2>
<p> <code>transmission-remote</code> &#8211; a remote control utility for transmission-daemon1 and <a href="/docs/linux/man/1-transmission/">transmission</a>(1)</p>
<h2>SYNOPSIS</h2>
<p> -words [<i>host:port | host | port</i> ] [-<code>a </code><i>filenames-or-URLs </i>[-<code>as</code> ] ] [-<code>AS</code> ] [-<code>asd </code><i>number</i> ] [-<code>asu </code><i>number</i> ] [-<code>asc</code> ] [-<code>ASC</code> ] [-<code>b</code> ] [-<code>c </code><i>path | &#8211;</i><code>C</code> ] [-<code>d </code><i>number | &#8211;</i><code>D</code> ] [-<code>e </code><i>size</i> ] [-<code>er | ep | et</code> ] [-<code>-exit</code> ] [-<code>f</code> ] [-<code>g </code><i>files</i> ] [-<code>G </code><i>files</i> ] [-<code>gsr </code><i>ratio</i> ] [-<code>GSR</code> ] [-<code>h</code> ] [-<code>i</code> ] [-<code>ic</code> ] [-<code>if</code> ] [-<code>ip</code> ] [-<code>it</code> ] [-<code>l</code> ] [-<code>m | M</code> ] [-<code>n </code><i>user:pass</i> ] [-<code>ne</code> ] [-<code>N </code><i>netrc</i> ] [-<code>o | O</code> ] [-<code>p </code><i>port</i> ] [-<code>Bh </code>[-<code>Bn </code>[-<code></p>
<dl>
<p> </code> ] ] ] [-<code>ph </code><i>files</i> ] [-<code>pl </code><i>files</i> ] [-<code>pn </code><i>files</i> ] [-<code>pr </code><i>peers</i> ] [-<code>r</code> ] [-<code>rad</code> ] [-<code>s | S</code> ] [-<code>sr </code><i>ratio</i> ] [-<code>SR</code> ] [-<code>srd</code> ] [-<code>si</code> ] [-<code>st</code> ] [-<code>t </code><i>all | active | id | hash</i> ] [-<code>hl</code> ] [-<code>HL</code> ] [-<code>u </code><i>number | &#8211;</i><code>U</code> ] [-<code>utp | no-utp</code> ] [-<code>v</code> ] [-<code>V</code> ] [-<code>w </code><i>download-dir</i> ] [-<code>x | X</code> ] [-<code>y | Y</code> ] [-<code>pi</code> ]</dl>
</dl>
<h2>DESCRIPTION</h2>
<p> is a remote control utility for <a href="/docs/linux/man/1-transmission/">transmission</a>(1) and transmission-daemon1. </p>
<p> By default, connects to the transmission session at localhost:9091. Other sessions can be controlled by specifying a different host and/or port.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a &#8211;add </code><i>filenames-or-URLs </i>Add torrents to transmission.</p>
<dd>
<dt><code>-b &#8211;debug</code></p>
<dd> Enable debugging mode.</p>
<dt><code>-as &#8211;alt-speed</code></p>
<dd> Use the alternate Limits.</p>
<dt><code>-AS &#8211;no-alt-speed</code></p>
<dd> Don&#8217;t use the alternate Limits.</p>
<dt><code>-asd &#8211;alt-speed-downlimit </code><i>limit</i></p>
<dd> Limit the alternate download speed to <i>limit</i> kilobytes per second.</p>
<dt><code>-asu &#8211;alt-speed-uplimit </code><i>limit</i></p>
<dd> Limit the alternate upload speed to <i>limit</i> kilobytes per second.</p>
<dt><code>-asc &#8211;alt-speed-scheduler</code></p>
<dd> Use the scheduled on/off times.</p>
<dt><code>-ASC &#8211;no-alt-speed-scheduler</code></p>
<dd> Don&#8217;t use the scheduled on/off days and times.</p>
<dt><code>&#8211;alt-speed-time-begin </code><i>time</i></p>
<dd> <i>Time</i> to start using the alt speed limits (in hhmm).</p>
<dt><code>&#8211;alt-speed-time-end </code><i>time</i></p>
<dd> <i>Time</i> to stop using the alt speed limits (in hhmm).</p>
<dt><code>&#8211;alt-speed-days </code><i>days</i></p>
<dd> Set the number of <i>days</i> on which to enable the speed scheduler, using a list such as &quot;2,4-6&quot;.</p>
<dt><code>&#8211;torrent-done-script </code><i>filename</i></p>
<dd> Specify a <i>file</i> to run each time a torrent finishes</p>
<dt><code>&#8211;no-torrent-done-script</code></p>
<dd> Don&#8217;t run any script when a torrent finishes</p>
<dt><code>-c &#8211;incomplete-dir </code><i>dir</i></p>
<dd> When adding new torrents, store their contents in <i>directory</i> until the torrent is done.</p>
<dt><code>-C &#8211;no-incomplete-dir</code></p>
<dd> Don&#8217;t store incomplete torrents in a different directory.</p>
<dt><code>-d &#8211;downlimit </code><i>limit</i></p>
<dd> Limit the maximum download speed to <i>limit</i> kB/s. If current torrent(s) are selected this operates on them. Otherwise, it changes the global setting.</p>
<dt><code>-D &#8211;no-downlimit</code></p>
<dd> Disable download speed limits. If current torrent(s) are selected this operates on them. Otherwise, it changes the global setting.</p>
<dt><code>-e &#8211;cache </code><i>size</i></p>
<dd> Set the session&#8217;s maximum memory cache size in MiB. This cache is used to reduce disk IO.</p>
<dt><code>-er &#8211;encryption-required</code></p>
<dd> Encrypt all peer connections.</p>
<dt><code>-ep &#8211;encryption-preferred</code></p>
<dd> Prefer encrypted peer connections.</p>
<dt><code>-et &#8211;encryption-tolerated</code></p>
<dd> Prefer unencrypted peer connections.</p>
<dt><code>&#8211;exit</code></p>
<dd> Tell the Transmission to initiate a shutdown.</p>
<dt><code>-f &#8211;files</code></p>
<dd> Get a file list for the current torrent(s)</p>
<dt><code>-g &#8211;get </code><i>all | file-index | files</i></p>
<dd> Mark file(s) for download. <i>all</i> marks all all of the torrent&#8217;s files for downloading, <i>file-index</i> adds a single file to the download list, and <i>files</i> adds multiple files to the download list, such as &quot;-g1,3-5&quot; to add files #1, #3, #4, and #5 to the download list.</p>
<dt><code>-G &#8211;no-get </code><i>all | file-index | files</i></p>
<dd> Mark file(s) for not downloading.</p>
<dt><code>-gsr &#8211;global-seedratio </code><i>ratio</i></p>
<dd> All torrents, unless overridden by a per-torrent setting, should seed until a specific <i>ratio</i></p>
<dt><code>-GSR &#8211;no-global-seedratio</code></p>
<dd> All torrents, unless overridden by a per-torrent setting, should seed regardless of ratio</p>
<dt><code>-h &#8211;help</code></p>
<dd> Print command-line option descriptions.</p>
<dt><code>-i &#8211;info</code></p>
<dd> Show details of the current torrent(s)</p>
<dt><code>-if &#8211;info-files</code></p>
<dd> List the specified torrent&#8217;s files</p>
<dt><code>-ip &#8211;info-peers</code></p>
<dd> List the specified torrent&#8217;s peers</p>
<dt><code>-ic &#8211;info-pieces</code></p>
<dd> List the specified torrent&#8217;s pieces</p>
<dt><code>-it &#8211;info-trackers</code></p>
<dd> List the specified torrent&#8217;s trackers</p>
<dt><code>-si &#8211;session-info</code></p>
<dd> List session information from the server</p>
<dt><code>-st &#8211;session-stats</code></p>
<dd> List statistical information from the server</p>
<dt><code>-l &#8211;list</code></p>
<dd> List all torrents</p>
<dt><code>-m &#8211;portmap</code></p>
<dd> Enable portmapping via NAT-PMP or UPnP</p>
<dt><code>-M &#8211;no-portmap</code></p>
<dd> Disable portmapping</p>
<dt><code>-n &#8211;auth </code><i>username:password</i></p>
<dd> Set the <i>username</i> and <i>password</i> for authentication</p>
<dt><code>-ne &#8211;authenv</code></p>
<dd> Set the authentication information from the <i>TR_AUTH</i> environment variable which must be formatted as <i>username:password.</i></p>
<dt><code>-N &#8211;netrc </code><i>filename</i></p>
<dd> Set the authentication information from a <i>netrc file.</i> See <a href="/docs/linux/man/5-netrc/">netrc</a>(5) for more information.</p>
<dt><code>-o &#8211;dht</code></p>
<dd> Enable distributed hash table (DHT).</p>
<dt><code>-O &#8211;no-dht</code></p>
<dd> Disable distribued hash table (DHT).</p>
<dt><code>-p &#8211;port </code><i>port</i></p>
<dd> Set the <i>port</i> for use when listening for incoming peer connections</p>
<dt><code>-Bh </code>&#8211;<code>-bandwidth-high</code></p>
<dd> Give this torrent first chance at available bandwidth</p>
<dt><code>-Bn </code>&#8211;<code>-bandwidth-normal</code></p>
<dd> Give this torrent the bandwidth left over by high priority torrents</p>
<dt><code>&#8211;</p>
<dl>
<p> </code></p>
<dd> Give this torrent the bandwidth left over by high and normal priority torrents</p>
<dt><code>-ph &#8211;priority-high </code><i>all | file-index | files</i></p>
<dd> Try to download the specified file(s) first. <i>all</i> marks all of the torrent&#8217;s files as normal priority, <i>file-index</i> sets a single file&#8217;s priority as normal, and <i>files</i> sets multiple files&#8217; priorities as normal, such as &quot;-pn1,3-5&quot; to normalize files #1, #3, #4, and #5.</p>
<dt><code>-pn &#8211;priority-normal </code><i>all | file-index | files</i></p>
<dd> Try to download the specified files normally.</p>
<dt><code>-pl &#8211;priority-low </code><i>all | file-index | files</i></p>
<dd> Try to download the specified files last</p>
<dt><code>-pr &#8211;peers </code><i>number</i></p>
<dd> Set the maximum number of peers. If current torrent(s) are selected this operates on them. Otherwise, it changes the global setting.</p>
<dt><code>-r &#8211;remove</code></p>
<dd> Remove the current torrent(s). This does not delete the downloaded data.</p>
<dt><code>-rad &#8211;remove-and-delete</code></p>
<dd> Remove the current torrent(s) and delete their downloaded data.</p>
<dt><code>&#8211;reannounce</code></p>
<dd> Reannounce the current torrent(s). This is the same as the GUI&#8217;s &quot;ask tracker for more peers&quot; button.</p>
<dt><code>&#8211;move</code></p>
<dd> Move the current torrents&#8217; data from their current locations to the specified directory.</p>
<dt><code>&#8211;find</code></p>
<dd> Tell Transmission where to look for the current torrents&#8217; data.</p>
<dt><code>-sr &#8211;seedratio </code><i>ratio</i></p>
<dd> Let the current torrent(s) seed until a specific <i>ratio</i></p>
<dt><code>-SR &#8211;no-seedratio</code></p>
<dd> Let the current torrent(s) seed regardless of ratio</p>
<dt><code>-srd &#8211;seedratio-default</code></p>
<dd> Let the current torrent(s) use the global seedratio settings</p>
<dt><code>-td &#8211;tracker-add </code><i>tracker</i></p>
<dd> Add a tracker to a torrent</p>
<dt><code>-tr &#8211;tracker-remove </code><i>trackerId </i>Remove a tracker from a torrent</p>
<dd>
<dt><code>-s &#8211;start</code></p>
<dd> Start the current torrent(s)</p>
<dt><code>-S &#8211;stop</code></p>
<dd> Stop the current torrent(s) from downloading or seeding</p>
<dt><code>&#8211;start-paused</code></p>
<dd> Start added torrents paused</p>
<dt><code>&#8211;no-start-paused</code></p>
<dd> Start added torrents unpaused</p>
<dt><code>-t &#8211;torrent </code><i>all | active | id | torrent-hash</i></p>
<dd> Set the current torrent(s) for use by subsequent options. The literal <i>all</i> will apply following requests to all torrents; the literal <i>active</i> will apply following requests to recently-active torrents; and specific torrents can be chosen by <i>id</i> or <i>hash</i> To set more than one current torrent, join their ids together in a list, such as &quot;-t2,4,6-8&quot; to operate on the torrents whose IDs are 2, 4, 6, 7, and 8.</p>
<dt><code>&#8211;trash-torrent</code></p>
<dd> Delete torrents after adding</p>
<dt><code>&#8211;no-trash-torrent</code></p>
<dd> Do not delete torrents after adding</p>
<dt><code>-hl &#8211;honor-session</code></p>
<dd> Make the current torrent(s) honor the session limits.</p>
<dt><code>-HL &#8211;no-honor-session</code></p>
<dd> Make the current torrent(s) not honor the session limits.</p>
<dt><code>-u &#8211;uplimit </code><i>limit</i></p>
<dd> Limit the maximum upload speed to <i>limit</i> kB/s. If current torrent(s) are selected this operates on them. Otherwise, it changes the global setting.</p>
<dt><code>-U &#8211;no-uplimit</code></p>
<dd> Disable upload speed limits.</p>
<dt><code>&#8211;utp</code></p>
<dd> Enable uTP for peer connections.</p>
<dt><code>&#8211;no-utp</code></p>
<dd> Disable uTP for peer connections. If current torrent(s) are selected this operates on them. Otherwise, it changes the global setting.</p>
<dt><code>-v &#8211;verify</code></p>
<dd> Verify the current torrent(s)</p>
<dt><code>-V &#8211;version</code></p>
<dd> Show version number and exit</p>
<dt><code>-w &#8211;download-dir </code><i>directory</i></p>
<dd> When used in conjunction with &#8211;add, set the new torrent&#8217;s download folder. Otherwise, set the default download folder.</p>
<dt><code>-x &#8211;pex</code></p>
<dd> Enable peer exchange (PEX).</p>
<dt><code>-X &#8211;no-pex</code></p>
<dd> Disable peer exchange (PEX).</p>
<dt><code>-y &#8211;lds</code></p>
<dd> Enable local peer discovery (LPD).</p>
<dt><code>-Y &#8211;no-lds</code></p>
<dd> Disable local peer discovery (LPD).</p>
<dt><code>-pi &#8211;peer-info</code></p>
<dd> List the current torrent&#8217;s connected peers. In the `status&#8217; section of the list, the following shorthand is used:</p>
<dt><code>&#8211;blocklist-update</code></p>
<dd> Update blocklist from URL specified in remote client&#8217;s settings with <i>blocklist-url</i> key.</dl>
</dl>
</dl>
<h2>EXAMPLES</h2>
<p> List all torrents: </p>
<blockquote>
<pre>
$ transmission-remote -l
</pre>
</blockquote>
<p> List all active torrents: </p>
<blockquote>
<pre>
$ transmission-remote -tactive -l
</pre>
</blockquote>
<p> Set download and upload limits to 400 kB/sec and 60 kB/sec: </p>
<blockquote>
<pre>
$ transmission-remote -d400 -u60
$ transmission-remote --downlimit=400 --uplimit=60
</pre>
</blockquote>
<p> Set alternate download and upload limits to 100 kB/sec and 20 kB/sec: </p>
<blockquote>
<pre>
$ transmission-remote -asd100 -asu20
$ transmission-remote --alt-speed-downlimit=100 --alt-speed-uplimit=20
</pre>
</blockquote>
<p> Set the scheduler to use the alternate speed limits on weekdays between 10AM and 11PM </p>
<blockquote>
<pre><code>
$ transmission - remote-- alt - speed - time - begin = 1000 $ transmission - remote-- alt - speed - time - end = 2300 $ transmission - remote-- alt - speed - days = 1 - 5 $ transmission - remote-- alt - speed - scheduler
</code></pre>
</blockquote>
<p> List all torrents&#8217; IDs and states: </p>
<blockquote>
<pre>
$ transmission-remote -l
</pre>
</blockquote>
<p> List all torrents from a remote session that requires authentication: </p>
<blockquote>
<pre>
$ transmission-remote host:9091 --auth=username:password -l
</pre>
</blockquote>
<p> Start all torrents: </p>
<blockquote>
<pre>
$ transmission-remote -tall --start
</pre>
</blockquote>
<p> Add two torrents: </p>
<blockquote>
<pre>
$ transmission-remote -a one.torrent two.torrent
</pre>
</blockquote>
<p> Add all torrents in ~/Desktop: </p>
<blockquote>
<pre>
$ transmission-remote -a ~/Desktop/*torrent
</pre>
</blockquote>
<p> Get detailed information on the torrent whose ID is &#8216;1&#8217;: </p>
<blockquote>
<pre>
$ transmission-remote -t1 -i
</pre>
</blockquote>
<p> Get a list of a torrent&#8217;s files: </p>
<blockquote>
<pre>
$ transmission-remote -t1 -f
</pre>
</blockquote>
<p> Download only its second and fourth files: </p>
<blockquote>
<pre>
$ transmission-remote -t1 -Gall -g2,4
</pre>
</blockquote>
<p> Set all torrents&#8217; first two files&#8217; priorities to high: </p>
<blockquote>
<pre>
$ transmission-remote -tall -ph1,2
</pre>
</blockquote>
<p> Set all torrents&#8217; files&#8217; priorities to normal: </p>
<blockquote>
<pre>
$ transmission-remote -tall -pnall
</pre>
</blockquote>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>http_proxy</code></p>
<dd> Sets the proxy to use for http tracker announces.</dl>
<h2>AUTHORS</h2>
<p> An -nosplit An Jordan Lee , An Josh Elsasser , An Eric Petit , and An Mitchell Livingston .</p>
<h2>SEE ALSO</h2>
<p> transmission-create1, transmission-daemon1, transmission-edit1, transmission-gtk1, transmission-qt1, transmission-remote1, transmission-show1 </p>
<p> <a rel="nofollow" href="http://www.transmissionbt.com/">http://www.transmissionbt.com/</a> </p>
<h2>Index</h2>
