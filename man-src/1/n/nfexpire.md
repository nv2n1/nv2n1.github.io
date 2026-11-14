---
title: "nfexpire(1)"
name: "nfexpire"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nfexpire/"
description: "nfexpire – data expiry program"
---

<h2>NAME</h2>
<p> nfexpire &#8211; data expiry program</p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>nfexpire [options]</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>nfexpire</code></p>
<dd>is used to manage the expiration of old netflow data files, created by <a href="/docs/linux/man/1-nfcapd/">nfcapd</a>(1) or other data collectors such as <a href="/docs/linux/man/1-sfcapd/">sfcapd</a>(1). Data expiration is done either by <a href="/docs/linux/man/1-nfcapd/">nfcapd</a>(1) in auto expiry mode, or by nfexpire which can by run at any time or any desired time interval by cron. nfexpire can also be savely run while nfcapd auto expires files, for cleaning up full disks etc. nfexpire is sub directory hierarchy aware, and handles any format automatically. For a fast and efficient expiration, nfexpire creates and maintains a stat file named <code>.nfstat</code> in the data directory. Any <i>directory</i> supplied with the options below corresponds to the data directory supplied to <a href="/docs/linux/man/1-nfcapd/">nfcapd</a>(1) using option -l. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-l </code><i>directory</i></p>
<dd> List current data statistics in directory <i>datadir</i>.</p>
<dt><code>-r </code><i>directory</i></p>
<dd> Rescan the specified directory to update the statfile. To be used only when explicit update is required. Usually nfexpire takes care itself about rescanning, when needed.</p>
<dt><code>-e </code><i>datadir</i></p>
<dd> Expire files in the specified <i>directory</i>. Expire limits are taken from statfile ( see -u ) or from supplied options -s -t and -w. Command line options overwrite stat file values, however the statfile limits are not changed.</p>
<dt><code>-s </code><i>maxsize</i></p>
<dd> Set size limit for the directory. The specified <i>limit</i> accepts values such as 100M, 100MB 1G 1.5G etc. Accpeted size factors are K, KB, M, MB, G, GB and T, TB. If no factor is supplied bytes (B) is assumed. A value of 0 disables the max size limit.</p>
<dt><code>-t </code><i>maxlife_time</i></p>
<dd> Sets the max life time for files in the directory. The supplied <i>maxlife_time</i> accepts values such as 31d, 240H 1.5d etc. Accpeted time scales are w (weeks) d (days) H (hours). A value of 0 disables the max lifetime limit. If no scale is given, H (hours) are assumed.</p>
<dt><code>-u </code><i>datadir</i></p>
<dd> Updates the max size and lifetime limits, specified by -s -t and -w and stores them in the statfile as default values. A running <a href="/docs/linux/man/1-nfcapd/">nfcapd</a>(1) processs doing auto expiry will take these new values starting with the next expiry cycle. Running nfexpire next time doing file expiration will take these new limits unless -s -t or -w are specified.</p>
<dt><code>-w </code><i>watermark</i></p>
<dd> Set the water mark in % for expiring data. If a limit is hit, files get expired down to this level in % of that limit. If not set, the default is 95%.</p>
<dt><code>-h</code></p>
<dd> Print help text on stdout with all options and exit.</p>
<dt><code>-p</code></p>
<dd> Directories specified by -e, -l and -r are interpreted as profile directories. Only NfSen will need this option.</p>
<dt><code>-Y</code></p>
<dd> Print result in parseable format. Only NfSen will need this option.</dl>
<h2>RETURN VALUE</h2>
<p> Returns</p>
<dl>
<dt>
<dd>
<p> 0 No error. </p>
<p> 255 Initialization failed. </p>
<p> 250 Internal error.</dl>
<h2>NOTES</h2>
<p> There are two ways to expire files: nfcapd in auto-expire mode ( option -e ) and nfexpire running by hand or periodically as cron job. Both ways synchronize access to the files, therefore both ways can be run in parallel if required.</p>
<dl>
<dt><code>Expiring by nfcapd in auto-expire mode: option -e</code></p>
<dd> If nfcapd is started with option -e, the auto-expire mode is enabled. After each cycle ( typically 5min ) nfcapd expires files according to the limits set with nfexpire using options -u -s -t and -w. If initially no limits are set, no files get expired.</p>
<dt><code>Expiring by nfexpire</code></p>
<dd> nfexpire can be run at any time to expire files. It automatically syncs up with the files created by nfcapd in the mean time since the last expire run, if a nfcapd collector process is running for that directory in question and expires the files according the limits set.</p>
<dt><code>Limits</code></p>
<dd> Files are expired according to two limits: maximum disk space used by all files in the directory and maximum lifetime of data files, whatever limit is reached first. If one of the limit is hit the expire process will delete files down to the watermark of that limit.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-nfcapd/">nfcapd</a>(1)</p>
<h2>BUGS</h2>
<h2>Index</h2>
