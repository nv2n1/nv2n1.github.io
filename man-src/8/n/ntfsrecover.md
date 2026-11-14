---
title: "ntfsrecover(8)"
name: "ntfsrecover"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ntfsrecover/"
description: "ntfsrecover – Recover updates committed by Windows on an NTFS volume"
---

<p>ntfsrecover &#8211; Recover updates committed by Windows on an NTFS volume</p>
<h2>Synopsis</h2>
<p><code>ntfsrecover</code> [<i>options</i>] <i>device</i></p>
<h2>Description</h2>
<p><code>ntfsrecover</code> applies to the metadata the updates which were requested on Windows but could not be completed because they were interrupted by some event such as a power failure, a hardware crash, a software crash or the device being unplugged. Doing so, the file system is restored to a consistent state, however updates to user data may still be lost. Updating the file system generally requires updating several records which should all be made for the file system to be kept consistent. For instance, creating a new file requires reserving an inode number (set a bit in a bit map), creating a file record (store the file name and file attributes), and registering the file in a directory (locate the file from some path). When an unfortunate event occurs, and one of these updates could be done but not all of them, the file system is left inconsistent. A group of updates which have all to be done to preserve consistency is called a transaction, and the end of updates within a transaction is called the commitment of the transaction. To protect from unfortunate events, Windows first logs in a special file all the metadata update requests without applying any, until the commitment is known. If the event occurs before the commitment, no update has been made and the file system is consistent. If the event occurs after the update, the log file can be analyzed later and the transactions which were committed can be executed again, thus restoring the integrity of the file system. <code>ntfsrecover</code> similarly examines the log file and applies the updates within committed transactions which could not be done by Windows. Currently, ntfs-3g does not log updates, so <code>ntfsrecover</code> cannot be used to restore consistency after an unfortunate event occurred while the file system was updated by Linux. </p>
<h2>Options</h2>
<p>Below is a summary of all the options that <code>ntfsrecover</code> accepts. The normal usage is to use no option at all, as most of these options are oriented towards developers needs. </p>
<p> Nearly all options have two equivalent names. The short name is preceded by <code>&#8211;</code> and the long name is preceded by <code>&#8212;</code>. Any single letter options, that don&#8217;t take an argument, can be combined into a single command, e.g. <code>-bv</code> is equivalent to <code>-b -v</code>. Long named options can be abbreviated to any unique prefix of their name.</p>
<dl>
<dt><code>-b</code>, <code>&#8211;backward</code></p>
<dd>Examine the actions described in the logfile backward from the latest one to the earliest one without applying any update. This may encompass records generated during several sessions, and when Windows is restarted, it often does not restart writing where it ended the previous session, so this leads to errors and bad sequencing when examining the full log file.</p>
<dt><code>-c</code>, <code>&#8211;clusters</code> <code>CLUSTER-RANGE</code></p>
<dd>Restrict the output generated when using options -b -f -u -p to the actions operating on a cluster within the given cluster range. CLUSTER-RANGE is defined by the first and last cluster numbers separated by a hyphen, for instance 100-109 or 0x3e8-0x3ff. A single number means restricting to a single cluster. The first four log blocks have a special role and they are always shown.</p>
<dt><code>-f</code>, <code>&#8211;forward</code> <code>NUM</code></p>
<dd>Examine the actions described in the logfile forward from the first one to the last one without applying any update. As the log file is reused circularly, the first one is generally not the earliest. Moreover when Windows is restarted, it often does not restart writing where it ended the previous sessions, and this leads to errors when examining a log file generated during several sessions.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Show some help information.</p>
<dt><code>-k</code>, <code>&#8211;kill-fast-restart</code></p>
<dd>When Windows has been interrupted with fast restart mode activated, part of pending changes are kept in the Windows cache and only the same Windows version can recover them. This option can be used to apply the changes recorded in the log file and drop the ones in the Windows cache. This is dangerous and may cause loss of data.</p>
<dt><code>-n</code>, <code>&#8211;no-action</code></p>
<dd>Do not apply any modification, useful when using the options -p, -s or -u.</p>
<dt><code>-p</code>, <code>&#8211;play</code> <code>COUNT</code></p>
<dd>Undo COUNT transaction sets and redo a single one, a transaction set being all transactions between two consecutive checkpoints. This is useful for replaying some transaction in the past. As a few actions are not undoable, this is not always possible.</p>
<dt><code>-r</code>, <code>&#8211;range</code> <code>BLOCK-RANGE</code></p>
<dd>Examine the actions described in the logfile forward restricted to the requested log file block range without applying any update. The first four log blocks have a special role and they are always examined.</p>
<dt><code>-s</code>, <code>&#8211;sync</code></p>
<dd>Sync the file system by applying the committed actions which have not been synced previously. This is the default option, used when none of the options -n, -f, -r, -p and -u are present. </p>
<p> The option -s can be repeated to request applying the committed actions mentioned in the obsolete restart page. This is useful for testing the situations where the latest restart page cannot be read though it can actually be read.</p>
<dt><code>-t</code>, <code>&#8211;transactions</code> <code>COUNT</code></p>
<dd>Display the transaction parameters when examining the log file with one of the options &#8211;forward, &#8211;backward or &#8211;range.</p>
<dt><code>-u</code>, <code>&#8211;undo</code> <code>COUNT</code></p>
<dd>Undo COUNT transaction sets, thus resetting the file system to some checkpoint in the past, a transaction set being all transactions between two consecutive checkpoints. As a few actions are not undoable, this is not always possible.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Display more debug/warning/error messages. This option may be used twice to display even more information.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Show the version number, copyright and license of <code>ntfsrecover</code>.</dl>
<h2>Examples</h2>
<p>Sync an NTFS volume on /dev/sda1.</p>
<dl>
<dd><code>ntfsrecover -s /dev/sda1</code></dl>
<p> Display all actions which updated a cluster in range 100 to 119 :</p>
<dl>
<dd><code>ntfsrecover &#8211;verbose &#8211;backward &#8211;clusters=100-119 /dev/sda1</code> </p>
<h2>Bugs</h2>
<p>If you find a bug please send an email describing the problem to the development team:<br />
 ntfs-3g-devel [at] lists.sf.net</p>
<h2>Authors</h2>
<p><code>ntfsrecover</code> was written by Jean-Pierre Andre</p>
<h2>Availability</h2>
<p><code>ntfsrecover</code> is part of the <code>ntfs-3g</code> package and is available from:<br />
 <a rel="nofollow" href="https://github.com/tuxera/ntfs-3g/wiki/">https://github.com/tuxera/ntfs-3g/wiki/</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ntfs-3g/">ntfs-3g</a></code>(8), <code><a href="/docs/linux/man/8-ntfsfix/">ntfsfix</a></code>(8), <code><a href="/docs/linux/man/8-ntfsprogs/">ntfsprogs</a></code>(8) </p>
