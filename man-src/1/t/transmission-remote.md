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
<dt><code>-a &#8211;add </code><i>filenames-or-URLs </i>Add torrents to transmission.</dt>
<dd>
</dd><dt><code>-b &#8211;debug</code></dt>
<dd> Enable debugging mode.</dd>
<dt><code>-as &#8211;alt-speed</code></dt>
<dd> Use the alternate Limits.</dd>
<dt><code>-AS &#8211;no-alt-speed</code></dt>
<dd> Don&#8217;t use the alternate Limits.</dd>
<dt><code>-asd &#8211;alt-speed-downlimit </code><i>limit</i></dt>
<dd> Limit the alternate download speed to <i>limit</i> kilobytes per second.</dd>
<dt><code>-asu &#8211;alt-speed-uplimit </code><i>limit</i></dt>
<dd> Limit the alternate upload speed to <i>limit</i> kilobytes per second.</dd>
<dt><code>-asc &#8211;alt-speed-scheduler</code></dt>
<dd> Use the scheduled on/off times.</dd>
<dt><code>-ASC &#8211;no-alt-speed-scheduler</code></dt>
<dd> Don&#8217;t use the scheduled on/off days and times.</dd>
<dt><code>&#8211;alt-speed-time-begin </code><i>time</i></dt>
<dd> <i>Time</i> to start using the alt speed limits (in hhmm).</dd>
<dt><code>&#8211;alt-speed-time-end </code><i>time</i></dt>
<dd> <i>Time</i> to stop using the alt speed limits (in hhmm).</dd>
<dt><code>&#8211;alt-speed-days </code><i>days</i></dt>
<dd> Set the number of <i>days</i> on which to enable the speed scheduler, using a list such as &quot;2,4-6&quot;.</dd>
<dt><code>&#8211;torrent-done-script </code><i>filename</i></dt>
<dd> Specify a <i>file</i> to run each time a torrent finishes</dd>
<dt><code>&#8211;no-torrent-done-script</code></dt>
<dd> Don&#8217;t run any script when a torrent finishes</dd>
<dt><code>-c &#8211;incomplete-dir </code><i>dir</i></dt>
<dd> When adding new torrents, store their contents in <i>directory</i> until the torrent is done.</dd>
<dt><code>-C &#8211;no-incomplete-dir</code></dt>
<dd> Don&#8217;t store incomplete torrents in a different directory.</dd>
<dt><code>-d &#8211;downlimit </code><i>limit</i></dt>
<dd> Limit the maximum download speed to <i>limit</i> kB/s. If current torrent(s) are selected this operates on them. Otherwise, it changes the global setting.</dd>
<dt><code>-D &#8211;no-downlimit</code></dt>
<dd> Disable download speed limits. If current torrent(s) are selected this operates on them. Otherwise, it changes the global setting.</dd>
<dt><code>-e &#8211;cache </code><i>size</i></dt>
<dd> Set the session&#8217;s maximum memory cache size in MiB. This cache is used to reduce disk IO.</dd>
<dt><code>-er &#8211;encryption-required</code></dt>
<dd> Encrypt all peer connections.</dd>
<dt><code>-ep &#8211;encryption-preferred</code></dt>
<dd> Prefer encrypted peer connections.</dd>
<dt><code>-et &#8211;encryption-tolerated</code></dt>
<dd> Prefer unencrypted peer connections.</dd>
<dt><code>&#8211;exit</code></dt>
<dd> Tell the Transmission to initiate a shutdown.</dd>
<dt><code>-f &#8211;files</code></dt>
<dd> Get a file list for the current torrent(s)</dd>
<dt><code>-g &#8211;get </code><i>all | file-index | files</i></dt>
<dd> Mark file(s) for download. <i>all</i> marks all all of the torrent&#8217;s files for downloading, <i>file-index</i> adds a single file to the download list, and <i>files</i> adds multiple files to the download list, such as &quot;-g1,3-5&quot; to add files #1, #3, #4, and #5 to the download list.</dd>
<dt><code>-G &#8211;no-get </code><i>all | file-index | files</i></dt>
<dd> Mark file(s) for not downloading.</dd>
<dt><code>-gsr &#8211;global-seedratio </code><i>ratio</i></dt>
<dd> All torrents, unless overridden by a per-torrent setting, should seed until a specific <i>ratio</i></dd>
<dt><code>-GSR &#8211;no-global-seedratio</code></dt>
<dd> All torrents, unless overridden by a per-torrent setting, should seed regardless of ratio</dd>
<dt><code>-h &#8211;help</code></dt>
<dd> Print command-line option descriptions.</dd>
<dt><code>-i &#8211;info</code></dt>
<dd> Show details of the current torrent(s)</dd>
<dt><code>-if &#8211;info-files</code></dt>
<dd> List the specified torrent&#8217;s files</dd>
<dt><code>-ip &#8211;info-peers</code></dt>
<dd> List the specified torrent&#8217;s peers</dd>
<dt><code>-ic &#8211;info-pieces</code></dt>
<dd> List the specified torrent&#8217;s pieces</dd>
<dt><code>-it &#8211;info-trackers</code></dt>
<dd> List the specified torrent&#8217;s trackers</dd>
<dt><code>-si &#8211;session-info</code></dt>
<dd> List session information from the server</dd>
<dt><code>-st &#8211;session-stats</code></dt>
<dd> List statistical information from the server</dd>
<dt><code>-l &#8211;list</code></dt>
<dd> List all torrents</dd>
<dt><code>-m &#8211;portmap</code></dt>
<dd> Enable portmapping via NAT-PMP or UPnP</dd>
<dt><code>-M &#8211;no-portmap</code></dt>
<dd> Disable portmapping</dd>
<dt><code>-n &#8211;auth </code><i>username:password</i></dt>
<dd> Set the <i>username</i> and <i>password</i> for authentication</dd>
<dt><code>-ne &#8211;authenv</code></dt>
<dd> Set the authentication information from the <i>TR_AUTH</i> environment variable which must be formatted as <i>username:password.</i></dd>
<dt><code>-N &#8211;netrc </code><i>filename</i></dt>
<dd> Set the authentication information from a <i>netrc file.</i> See <a href="/docs/linux/man/5-netrc/">netrc</a>(5) for more information.</dd>
<dt><code>-o &#8211;dht</code></dt>
<dd> Enable distributed hash table (DHT).</dd>
<dt><code>-O &#8211;no-dht</code></dt>
<dd> Disable distribued hash table (DHT).</dd>
<dt><code>-p &#8211;port </code><i>port</i></dt>
<dd> Set the <i>port</i> for use when listening for incoming peer connections</dd>
<dt><code>-Bh </code>&#8211;<code>-bandwidth-high</code></dt>
<dd> Give this torrent first chance at available bandwidth</dd>
<dt><code>-Bn </code>&#8211;<code>-bandwidth-normal</code></dt>
<dd> Give this torrent the bandwidth left over by high priority torrents</dd>
<dt><code>&#8211;</dt>
<dl>
<p> </code></p>
<dd> Give this torrent the bandwidth left over by high and normal priority torrents</dd>
<dt><code>-ph &#8211;priority-high </code><i>all | file-index | files</i></dt>
<dd> Try to download the specified file(s) first. <i>all</i> marks all of the torrent&#8217;s files as normal priority, <i>file-index</i> sets a single file&#8217;s priority as normal, and <i>files</i> sets multiple files&#8217; priorities as normal, such as &quot;-pn1,3-5&quot; to normalize files #1, #3, #4, and #5.</dd>
<dt><code>-pn &#8211;priority-normal </code><i>all | file-index | files</i></dt>
<dd> Try to download the specified files normally.</dd>
<dt><code>-pl &#8211;priority-low </code><i>all | file-index | files</i></dt>
<dd> Try to download the specified files last</dd>
<dt><code>-pr &#8211;peers </code><i>number</i></dt>
<dd> Set the maximum number of peers. If current torrent(s) are selected this operates on them. Otherwise, it changes the global setting.</dd>
<dt><code>-r &#8211;remove</code></dt>
<dd> Remove the current torrent(s). This does not delete the downloaded data.</dd>
<dt><code>-rad &#8211;remove-and-delete</code></dt>
<dd> Remove the current torrent(s) and delete their downloaded data.</dd>
<dt><code>&#8211;reannounce</code></dt>
<dd> Reannounce the current torrent(s). This is the same as the GUI&#8217;s &quot;ask tracker for more peers&quot; button.</dd>
<dt><code>&#8211;move</code></dt>
<dd> Move the current torrents&#8217; data from their current locations to the specified directory.</dd>
<dt><code>&#8211;find</code></dt>
<dd> Tell Transmission where to look for the current torrents&#8217; data.</dd>
<dt><code>-sr &#8211;seedratio </code><i>ratio</i></dt>
<dd> Let the current torrent(s) seed until a specific <i>ratio</i></dd>
<dt><code>-SR &#8211;no-seedratio</code></dt>
<dd> Let the current torrent(s) seed regardless of ratio</dd>
<dt><code>-srd &#8211;seedratio-default</code></dt>
<dd> Let the current torrent(s) use the global seedratio settings</dd>
<dt><code>-td &#8211;tracker-add </code><i>tracker</i></dt>
<dd> Add a tracker to a torrent</dd>
<dt><code>-tr &#8211;tracker-remove </code><i>trackerId </i>Remove a tracker from a torrent</dt>
<dd>
</dd><dt><code>-s &#8211;start</code></dt>
<dd> Start the current torrent(s)</dd>
<dt><code>-S &#8211;stop</code></dt>
<dd> Stop the current torrent(s) from downloading or seeding</dd>
<dt><code>&#8211;start-paused</code></dt>
<dd> Start added torrents paused</dd>
<dt><code>&#8211;no-start-paused</code></dt>
<dd> Start added torrents unpaused</dd>
<dt><code>-t &#8211;torrent </code><i>all | active | id | torrent-hash</i></dt>
<dd> Set the current torrent(s) for use by subsequent options. The literal <i>all</i> will apply following requests to all torrents; the literal <i>active</i> will apply following requests to recently-active torrents; and specific torrents can be chosen by <i>id</i> or <i>hash</i> To set more than one current torrent, join their ids together in a list, such as &quot;-t2,4,6-8&quot; to operate on the torrents whose IDs are 2, 4, 6, 7, and 8.</dd>
<dt><code>&#8211;trash-torrent</code></dt>
<dd> Delete torrents after adding</dd>
<dt><code>&#8211;no-trash-torrent</code></dt>
<dd> Do not delete torrents after adding</dd>
<dt><code>-hl &#8211;honor-session</code></dt>
<dd> Make the current torrent(s) honor the session limits.</dd>
<dt><code>-HL &#8211;no-honor-session</code></dt>
<dd> Make the current torrent(s) not honor the session limits.</dd>
<dt><code>-u &#8211;uplimit </code><i>limit</i></dt>
<dd> Limit the maximum upload speed to <i>limit</i> kB/s. If current torrent(s) are selected this operates on them. Otherwise, it changes the global setting.</dd>
<dt><code>-U &#8211;no-uplimit</code></dt>
<dd> Disable upload speed limits.</dd>
<dt><code>&#8211;utp</code></dt>
<dd> Enable uTP for peer connections.</dd>
<dt><code>&#8211;no-utp</code></dt>
<dd> Disable uTP for peer connections. If current torrent(s) are selected this operates on them. Otherwise, it changes the global setting.</dd>
<dt><code>-v &#8211;verify</code></dt>
<dd> Verify the current torrent(s)</dd>
<dt><code>-V &#8211;version</code></dt>
<dd> Show version number and exit</dd>
<dt><code>-w &#8211;download-dir </code><i>directory</i></dt>
<dd> When used in conjunction with &#8211;add, set the new torrent&#8217;s download folder. Otherwise, set the default download folder.</dd>
<dt><code>-x &#8211;pex</code></dt>
<dd> Enable peer exchange (PEX).</dd>
<dt><code>-X &#8211;no-pex</code></dt>
<dd> Disable peer exchange (PEX).</dd>
<dt><code>-y &#8211;lds</code></dt>
<dd> Enable local peer discovery (LPD).</dd>
<dt><code>-Y &#8211;no-lds</code></dt>
<dd> Disable local peer discovery (LPD).</dd>
<dt><code>-pi &#8211;peer-info</code></dt>
<dd> List the current torrent&#8217;s connected peers. In the `status&#8217; section of the list, the following shorthand is used:</dd>
<dt><code>&#8211;blocklist-update</code></dt>
<dd> Update blocklist from URL specified in remote client&#8217;s settings with <i>blocklist-url</i> key.</dd></dl>
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
<dt><code>http_proxy</code></dt>
<dd> Sets the proxy to use for http tracker announces.</dd></dl>
<h2>AUTHORS</h2>
<p> An -nosplit An Jordan Lee , An Josh Elsasser , An Eric Petit , and An Mitchell Livingston .</p>
<h2>SEE ALSO</h2>
<p> transmission-create1, transmission-daemon1, transmission-edit1, transmission-gtk1, transmission-qt1, transmission-remote1, transmission-show1 </p>
<p> <a rel="nofollow" href="http://www.transmissionbt.com/">http://www.transmissionbt.com/</a> </p>
<h2>Index</h2>
