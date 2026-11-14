---
title: "dbcheck(8)"
name: "dbcheck"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dbcheck/"
description: "dbcheck – Bacula’s Catalog Database Check/Clean program"
---

<p>&nbsp;<wbr>dbcheck &#8211; Bacula&#8217;s Catalog Database Check/Clean program</p>
<h2>Synopsis</h2>
<p><code>dbcheck</code> [<i>options</i>] <i>working-directory</i> <i>bacula-database</i> <i>user</i> <i>password</i> [<i>dbhost</i>] [<i>dbport</i>]</p>
<h2>Description</h2>
<p>This manual page documents briefly the <code>dbcheck</code> command. </p>
<p> dbcheck will not repair your database if it is broken. Please see your vendor&#8217;s instructions for fixing broken database. </p>
<p> dbcheck is a simple program that will search for logical inconsistencies in the Bacula tables in your database, and optionally fix them. It is a database maintenance routine, in the sense that it can detect and remove unused rows, but it is not a database repair routine. To repair a database, see the tools furnished by the database vendor. Normally dbcheck should never need to be run, but if Bacula has crashed or you have a lot of Clients, Pools, or Jobs that you have removed, it could be useful.</p>
<h2>Options</h2>
<p>A summary of options is included below.</p>
<dl>
<dt><code>-?</code></p>
<dd>Show version and usage of program.</p>
<dt><code>-b</code></p>
<dd>If specified, dbcheck will run in batch mode, and it will proceed to examine and fix (if -f is set) all programmed inconsistency checks. By default, dbcheck will enter interactive mode (see below).</p>
<dt><code>-C&nbsp;<wbr></code><i>catalog</i></p>
<dd>catalog name in the director conf file.</p>
<dt><code>-c&nbsp;<wbr></code><i>config</i></p>
<dd>If the -c option is given with the Director&#8217;s conf file, there is no need to enter any of the command line arguments, in particular the working directory as dbcheck will read them from the file.</p>
<dt><code>-B</code></p>
<dd>print catalog configuration and exit.</p>
<dt><code>-d&nbsp;<wbr></code><i>nn</i></p>
<dd>set debug level to <i>nn</i>.</p>
<dt><code>-dt</code></p>
<dd>print timestamp in debug output.</p>
<dt><code>-f</code></p>
<dd>If specified, dbcheck will repair (fix) the inconsistencies it finds. Otherwise, it will report only.</p>
<dt><code>-v</code></p>
<dd>Set verbose mode.</dl>
<h2>Interactive Mode</h2>
<p>In interactive mode dbcheck will prompt with the following: </p>
<p> Hello, this is the database check/correct program. Please select the function you want to perform.<br />
&nbsp;<wbr>&nbsp;<wbr>1)&nbsp;<wbr>Toggle modify database flag<br />
&nbsp;<wbr>&nbsp;<wbr>2)&nbsp;<wbr>Toggle verbose flag<br />
&nbsp;<wbr>&nbsp;<wbr>3)&nbsp;<wbr>Repair bad Filename records<br />
&nbsp;<wbr>&nbsp;<wbr>4)&nbsp;<wbr>Repair bad Path records<br />
&nbsp;<wbr>&nbsp;<wbr>5)&nbsp;<wbr>Eliminate duplicate Filename records<br />
&nbsp;<wbr>&nbsp;<wbr>6)&nbsp;<wbr>Eliminate duplicate Path records<br />
&nbsp;<wbr>&nbsp;<wbr>7)&nbsp;<wbr>Eliminate orphaned Jobmedia records<br />
&nbsp;<wbr>&nbsp;<wbr>8)&nbsp;<wbr>Eliminate orphaned File records<br />
&nbsp;<wbr>&nbsp;<wbr>9)&nbsp;<wbr>Eliminate orphaned Path records<br />
&nbsp;<wbr>10)&nbsp;<wbr>Eliminate orphaned Filename records<br />
&nbsp;<wbr>11)&nbsp;<wbr>Eliminate orphaned FileSet records<br />
&nbsp;<wbr>12)&nbsp;<wbr>Eliminate orphaned Client records<br />
&nbsp;<wbr>13)&nbsp;<wbr>Eliminate orphaned Job records<br />
&nbsp;<wbr>14)&nbsp;<wbr>Eliminate all Admin records<br />
&nbsp;<wbr>15)&nbsp;<wbr>Eliminate all Restore records<br />
&nbsp;<wbr>16)&nbsp;<wbr>All&nbsp;<wbr>(3-15)<br />
&nbsp;<wbr>17)&nbsp;<wbr>Quit Select function number: </p>
<p> By entering 1 or 2, you can toggle the modify database flag (-f option) and the verbose flag (-v). It can be helpful and reassuring to turn off the modify database flag, then select one or more of the consistency checks (items 3 through 9) to see what will be done, then toggle the modify flag on and re-run the check. </p>
<p> The inconsistencies examined are the following: </p>
<p> Duplicate filename records. This can happen if you accidentally run two<br />
copies of Bacula at the same time, and they are both adding filenames<br />
simultaneously.&nbsp;<wbr>&nbsp;<wbr>It is a rare occurrence, but will create an<br />
inconsistent database.&nbsp;<wbr>&nbsp;<wbr>If this is the case, you will receive error<br />
messages during Jobs warning of duplicate database records.&nbsp;<wbr>&nbsp;<wbr>If you are<br />
not getting these error messages, there is no reason to run this check. </p>
<p> Repair bad Filename records. This checks and corrects filenames that have<br />
a trailing slash.&nbsp;<wbr>&nbsp;<wbr>They should not. </p>
<p> Repair bad Path records. This checks and corrects path names that do not<br />
have a trailing slash.&nbsp;<wbr>&nbsp;<wbr>They should. </p>
<p> Duplicate path records. This can happen if you accidentally run two copies<br />
of Bacula at the same time, and they are both adding filenames<br />
simultaneously.&nbsp;<wbr>&nbsp;<wbr>It is a rare occurrence, but will create an<br />
inconsistent database.&nbsp;<wbr>&nbsp;<wbr>See the item above for why this occurs and how<br />
you know it is happening. </p>
<p> Orphaned JobMedia records. This happens when a Job record is deleted<br />
(perhaps by a user issued SQL statement), but the corresponding JobMedia<br />
record&nbsp;<wbr>(one for each Volume used in the Job)&nbsp;<wbr>was not deleted.&nbsp;<wbr>&nbsp;<wbr>Normally,<br />
this should not happen, and even if it does, these records generally do<br />
not take much space in your database.&nbsp;<wbr>&nbsp;<wbr>However, by running this check,<br />
you can eliminate any such orphans. </p>
<p> Orphaned File records. This happens when a Job record is deleted (perhaps<br />
by a user issued SQL statement), but the corresponding File record&nbsp;<wbr>(one<br />
for each Volume used in the Job)&nbsp;<wbr>was not deleted.&nbsp;<wbr>&nbsp;<wbr>Note, searching for<br />
these records can be very time consuming&nbsp;<wbr>(i.e.&nbsp;<wbr>&nbsp;<wbr>it may take hours)&nbsp;<wbr>for a<br />
large database.&nbsp;<wbr>&nbsp;<wbr>Normally this should not happen as Bacula takes care to<br />
prevent it.&nbsp;<wbr>&nbsp;<wbr>Just the same, this check can remove any orphaned File<br />
records.&nbsp;<wbr>&nbsp;<wbr>It is recommended that you run this once a year since orphaned<br />
File records can take a large amount of space in your database.&nbsp;<wbr>&nbsp;<wbr>You<br />
might want to ensure that you have indexes on JobId, FilenameId, and<br />
PathId for the File table in your catalog before running this command. </p>
<p> Orphaned Path records. This condition happens any time a directory is<br />
deleted from your system and all associated Job records have been<br />
purged.&nbsp;<wbr>&nbsp;<wbr>During standard purging&nbsp;<wbr>(or pruning)&nbsp;<wbr>of Job records, Bacula<br />
does not check for orphaned Path records.&nbsp;<wbr>&nbsp;<wbr>As a consequence, over a<br />
period of time, old unused Path records will tend to accumulate and use<br />
space in your database.&nbsp;<wbr>&nbsp;<wbr>This check will eliminate them.&nbsp;<wbr>&nbsp;<wbr>It is<br />
recommended that you run this check at least once a year. </p>
<p> Orphaned Filename records. This condition happens any time a file is<br />
deleted from your system and all associated Job records have been<br />
purged.&nbsp;<wbr>&nbsp;<wbr>This can happen quite frequently as there are quite a large<br />
number of files that are created and then deleted.&nbsp;<wbr>&nbsp;<wbr>In addition, if you<br />
do a system update or delete an entire directory, there can be a very<br />
large number of Filename records that remain in the catalog but are no<br />
longer used. </p>
<p>During standard purging&nbsp;<wbr>(or pruning)&nbsp;<wbr>of Job records, Bacula does not<br />
check for orphaned Filename records.&nbsp;<wbr>&nbsp;<wbr>As a consequence, over a period of<br />
time, old unused Filename records will accumulate and use space in your<br />
database.&nbsp;<wbr>&nbsp;<wbr>This check will eliminate them.&nbsp;<wbr>&nbsp;<wbr>It is strongly recommended<br />
that you run this check at least once a year, and for large database<br />
(more than 200 Megabytes), it is probably better to run this once every<br />
6 months. </p>
<p> Orphaned Client records. These records can remain in the database long<br />
after you have removed a client. </p>
<p> Orphaned Job records. If no client is defined for a job or you do not run<br />
a job for a long time, you can accumulate old job records.&nbsp;<wbr>&nbsp;<wbr>This option<br />
allow you to remove jobs that are not attached to any client&nbsp;<wbr>(and thus<br />
useless). </p>
<p> All Admin records. This command will remove all Admin records,<br />
regardless of their age. </p>
<p> All Restore records. This command will remove all Restore records,<br />
regardless of their age. </p>
<p> By the way, I personally run dbcheck only where I have messed up my database due to a bug in developing Bacula code, so normally you should never need to run dbcheck inspite of the recommendations given above, which are given so that users don&#8217;t waste their time running dbcheck too often.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-bls/">bls</a></code>(1), <code><a href="/docs/linux/man/1-bextract/">bextract</a></code>(1).</p>
<h2>Author</h2>
<p>This manual page was written by Jose Luis Tallon &lt;jltallon [at] adv-solutions.net&gt;.</p>
