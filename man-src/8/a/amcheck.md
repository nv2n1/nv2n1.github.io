---
title: "amcheck(8)"
name: "amcheck"
section: "8"
letter: "a"
url: "/docs/linux/man/8-amcheck/"
description: "amcheck – run Amanda self-checks"
---

<p>amcheck &#8211; run Amanda self-checks</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>amcheck</code> [-am] [-w] [-sclt] [-M&nbsp;<wbr><i>address</i>] [&#8211;client-verbose] [&#8211;exact-match] [<code>-o</code>&nbsp;<wbr><i>configoption</i>&#8230;] <i>config</i> [<i>host</i>&nbsp;<wbr>[<i>disk</i>&#8230;]&#8230;]</dl>
<h2>Description</h2>
<p><code>Amcheck</code></p>
<dd>runs a number of self-checks on both the Amanda tape server host and the Amanda client hosts. </p>
<p> On the tape server host, <code>amcheck</code> can go through the same tape checking used at the start of the nightly <code>amdump</code> run to verify the correct tape for the next run is mounted. </p>
<p> <code>Amcheck</code> can also do a self-check on all client hosts to make sure each host is running and that permissions on filesystems to be backed up are correct. </p>
<p> You can specify many host/disk expressions, only disks that match an expression will be checked. All disks are checked if no expressions are given. </p>
<p> See the <code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8) man page for more details about Amanda.</p>
<h2>Options</h2>
<p><code>-s</code></p>
<dl>
<dd>Run the tape server local and tape checks (same as <code>-lt</code>).</dl>
<p> <code>-c</code></p>
<dl>
<dd>Run the client host checks. Multiple specific clients can be checked by specifying the client name.</dl>
<p> <code>-l</code></p>
<dl>
<dd>Run the local tests (e.g. permissions) on the server host.</dl>
<p> <code>-t</code></p>
<dl>
<dd>Run the tape tests on the server host.</dl>
<p> <code>-w</code></p>
<dl>
<dd>Enables a DESTRUCTIVE check for write-protection on the tape (which would otherwise cause the subsequent <code>amdump</code> to fail). If the tape is writable, this check causes all data after the tape label to be erased. If the <code>autolabel</code> option is enabled, this check may ERASE any non-Amanda tape in the drive or changer. The check enable the tape tests on the server host and is only made if the tape is otherwise correct.</dl>
<p> <code>-m</code></p>
<dl>
<dd>Nothing is printed, but mail is sent if any errors are detected. The mail goes to the <code>mailto</code> address specified in the <i>amanda.conf</i> file or the <i>address</i> value if <code>-M</code> is set.</dl>
<p> <code>-a</code></p>
<dl>
<dd>Like <code>-m</code> but the mail is always sent.</dl>
<p> <code>-M</code> <i>address</i></p>
<dl>
<dd>Mail the report to <i>address</i> instead of the <code>mailto</code> value from <i>amanda.conf</i>. Implies <code>-m</code>.</dl>
<p> <code>&#8211;client-verbose</code></p>
<dl>
<dd>Print all client messages.</dl>
<p> <code>&#8211;exact-match</code></p>
<dl>
<dd>The host and disk are parsed as exact values</dl>
<p> <i>host</i> [<i>disk</i>]*</p>
<dl>
<dd>Specify the host and disk on which the command will work.</dl>
<p> <code>-o </code><i>configoption</i></p>
<dl>
<dd>See the &quot;CONFIGURATION OVERRIDE&quot; section in <code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8).</dl>
<p> The default is <code>-cs</code>.</p>
<h2>Examples</h2>
<p>In this example, both the tape server and client tests are run. The results are displayed on standard output. </p>
<pre>% amcheck daily
Amanda Tape Server Host Check
-----------------------------
/amanda2/amanda/work: 911475 KB disk space available, that's plenty.
NOTE: skipping tape-writable test.
Tape VOL10 label ok.
Server check took 34.966 seconds.
Amanda Backup Client Hosts Check
--------------------------------
WARNING: northstar: selfcheck request timed out. Host down?
WARNING: drinkme: selfcheck request timed out. Host down?
WARNING: scruffy: selfcheck request timed out. Host down?
Client check: 136 hosts checked in 51.945 seconds, 3 problems found.
(brought to you by Amanda 2.5.0) </pre>
<p>In this example, if the line <code>mailto csd-amanda</code> is in <i>amanda.conf</i>, mail will be sent to <code>csd-amanda</code> if the server check returns an error. </p>
<pre>% amcheck -s -m daily </pre>
<h2>Messages</h2>
<p>fatal slot <i>slot</i>: <i>error message</i></p>
<dl>
<dd>(error) The tape changer detected some kind of fatal error while trying to load slot <i>slot</i>.</dl>
<p> slot <i>slot</i>: <i>error message</i></p>
<dl>
<dd>(warning) The tape changer detected some kind of non-fatal error (e.g. an empty slot was detected) while trying to load slot <i>slot</i>, or an error was detected trying to read the tape label.</dl>
<p> slot <i>slot</i>: date <i>YYYYMMDD</i> label <i>label</i> (<i>result</i>)</p>
<dl>
<dd>(info) Tape <i>label</i> in slot <i>slot</i> was loaded and found to have been last written on <i>YYYYMMDD</i>. If the tape is new, the date field will be an <i>X</i>. The <i>result</i> may be one of: </p>
<p> exact label match</p>
<dl>
<dd>This is the expected tape.</dl>
<p> no match</p>
<dl>
<dd>This label does not match the <code>labelstr</code> pattern in <i>amanda.conf</i>. Tape scanning will continue.</dl>
<p> active tape</p>
<dl>
<dd>This tape is still active and cannot be overwritten. Tape scanning will continue.</dl>
<p> first labelstr match</p>
<dl>
<dd>This tape is the first one that matches the <code>labelstr</code> pattern in <i>amanda.conf</i>. Tape scanning will continue if necessary.</dl>
<p> labelstr match</p>
<dl>
<dd>This tape is the next one that matches the <code>labelstr</code> pattern in <i>amanda.conf</i>. Tape scanning will continue.</dl>
</dl>
<p> ERROR: cannot look up dump user <i>user</i></p>
<dl>
<dd>(error) Dump user <i>user</i> from <i>amanda.conf</i> could not be found in the system password information.</dl>
<p> ERROR: cannot look up my own uid (<i>uid</i>)</p>
<dl>
<dd>(error) User id <i>uid</i> running <code>amcheck</code> could not be found in the system password information.</dl>
<p> ERROR: running as user <i>runuser</i> instead of <i>dumpuser</i></p>
<dl>
<dd>(error) <code>Amcheck</code> should be run as the dump user <i>dumpuser</i> from <i>amanda.conf</i> instead of <i>runuser</i>.</dl>
<p> ERROR: program dir <i>directory</i>: not accessible</p>
<dl>
<dd>(error) The directory Amanda expects to find its auxiliary programs in, <i>directory</i>, is not accessible.</dl>
<p> ERROR: program <i>program</i>: does not exist</p>
<dl>
<dd>(error) Program <i>program</i> needed on the tape server could not be found.</dl>
<p> ERROR: program <i>program</i>: not a file</p>
<dl>
<dd>(error) Program <i>program</i> needed on the tape server exists but is not a file.</dl>
<p> ERROR: program <i>program</i>: not executable</p>
<dl>
<dd>(error) Program <i>program</i> needed on the tape server exists but is not executable.</dl>
<p> WARNING: program <i>program</i>: not setuid-root</p>
<dl>
<dd>(warning) Program <i>program</i> needed on the tape server exists but should be owned by user &quot;root&quot; and setuid.</dl>
<p> ERROR: <i>XXX</i> dir <i>directory</i>: not writable</p>
<dl>
<dd>(error) Directory <i>directory</i> is either not writable, i.e. the dump user will not be able to create or remove files, or cannot be accessed, perhaps because a parent directory does not allow search permission. The <i>XXX</i> may be: </p>
<p> log</p>
<dl>
<dd>for the Amanda log directory (see <code>logdir</code> in <code>amanda.conf</code>)</dl>
<p> oldlog</p>
<dl>
<dd>for the directory that holds the old log files (see <code>logdir</code> in <code>amanda.conf</code>)</dl>
<p> info</p>
<dl>
<dd>for an Amanda database information directory (see <code>curinfo</code> in <code>amanda.conf</code>) or</dl>
<p> index</p>
<dl>
<dd>for an Amanda index directory (see <code>indexdir</code> in <code>amanda.conf</code>)</dl>
<p> tapelist</p>
<dl>
<dd>for the <code><a href="/docs/linux/man/5-tapelist/">tapelist</a></code>(5)</dl>
</dl>
<p> NOTE: <i>XXX</i> dir <i>directory</i>: does not exist</p>
<dl>
<dd>(info) A database (info) or index directory does not exist or cannot be accessed. This might just mean this is a new client or disk, but if that is not the case, this should be treated as an error.</dl>
<p> NOTE: it will be created on the next run</p>
<dl>
<dd>(info) This indicates the info directory listed in the previous message will be created on the next run.</dl>
<p> ERROR: <i>XXX</i> dir <i>name</i>: not a directory</p>
<dl>
<dd>(error) <code>Amcheck</code> expected <i>name</i> to be a directory, but it is something else (e.g. file).</dl>
<p> WARNING: info file file: does not exist</p>
<dl>
<dd>(warning) File <i>file</i> does not exist in the text format database. Since the parent directories do exist, the file should already have been created.</dl>
<p> ERROR: info file name: not a file</p>
<dl>
<dd>(error) <code>Amcheck</code> expected <i>name</i> to be a file, but it is something else (e.g. file).</dl>
<p> ERROR: info file file: not readable</p>
<dl>
<dd>(error) The text format database file <i>file</i> is not readable.</dl>
<p> ERROR: log file file: not writable</p>
<dl>
<dd>(error) Log file <i>file</i> (file <code>log</code> in <code>logdir</code> from <code>amanda.conf</code>) is either not writable, or cannot be accessed, perhaps because a parent directory does not allow search permission.</dl>
<p> ERROR: tape list <i>tapelist</i>: not writable</p>
<dl>
<dd>(error) <code><a href="/docs/linux/man/5-tapelist/">tapelist</a></code>(5) is not writable or was not found.</dl>
<p> ERROR: tape list <i>tapelist</i>: parse error</p>
<dl>
<dd>(error) <code><a href="/docs/linux/man/5-tapelist/">tapelist</a></code>(5) could not be read or parsed.</dl>
<p> WARNING: tapedev is /dev/null, dumps will be thrown away</p>
<dl>
<dd>(warning) The <code>tapedev</code> parameter in <code>amanda.conf</code> is set to /dev/null and Amanda uses that when debugging to throw all the dump images away.</dl>
<p> WARNING: hold file file exists</p>
<dl>
<dd>(info) Hold file <i>file</i> exists and will cause <code>amdump</code> to pause at the beginning until it is removed.</dl>
<p> ERROR: holding disk <i>disk</i>: statfs: <i>error message</i></p>
<dl>
<dd>(error) An error was returned from the <i>statfs</i> system call on holding disk <i>disk</i> (maybe because it does not exist).</dl>
<p> ERROR: holding disk <i>disk</i>: not writable</p>
<dl>
<dd>(error) Holding disk <i>disk</i>, is not writable, probably because the caller does not have write permission or a parent directory does not allow search permission.</dl>
<p> WARNING: holding disk <i>disk</i>: available space unknown <i>N</i> KB requested.</p>
<dl>
<dd>(warning) <code>Amcheck</code> could not determine the amount of available space on holding disk <i>disk</i> to see if there were at least <i>N</i> KBytes available.</dl>
<p> WARNING: holding disk <i>disk</i>: only <i>F</i> KB free (<i>R</i> KB requested).</p>
<dl>
<dd>(warning) <i>amanda.conf</i> requested <i>R</i> KBytes of free space on holding disk <i>disk</i>, but only <i>F</i> KBytes were available. 10 MBytes is subtracted for each backup process (see the <code>inparallel</code> <i>amanda.conf</i> option) to allow for unexpected overruns. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 Even though this message is listed as a warning, it causes <code>amcheck</code> to exit with a non-zero status. </p>
</dl>
</dl>
<p> Holding disk <i>disk</i>: <i>N</i> KB disk space available, that&#8217;s plenty.</p>
<dl>
<dd>(info) There was sufficient free space on holding disk <i>disk</i>.</dl>
<p> WARNING: holding disk <i>disk</i>: only <i>F</i> KB free, using nothing</p>
<dl>
<dd>(warning) Holding disk <i>disk</i> has <i>F</i> KBytes of free space, but that is not enough for what is requested in <i>amanda.conf</i>.</dl>
<p> Holding disk <i>disk</i>: <i>F</i> KB disk space available, using <i>U</i> KB</p>
<dl>
<dd>(info) Holding disk <i>disk</i> has <i>F</i> KBytes of free space and Amanda will be using up to <i>U</i> Kbytes.</dl>
<p> WARNING: if a tape changer is not available, runtapes must be set to 1.</p>
<dl>
<dd>(warning) The <code>runtapes</code> <i>amanda.conf</i> option must be set to 1 if the <code>tpchanger</code> <i>amanda.conf</i> option is not set.</dl>
<p> ERROR: <i>error message</i>.</p>
<dl>
<dd>(error) An error was detected while initializing the tape changer.</dl>
<p> ERROR: <i>tape device</i>: <i>error message</i>.</p>
<dl>
<dd>(error) An error was detected while processing the tape label.</dl>
<p> ERROR: cannot overwrite active tape <i>label</i>.</p>
<dl>
<dd>(error) Tape <i>label</i> is still active and cannot be used.</dl>
<p> ERROR: label <i>label</i> doesn&#8217;t match labelstr <i>pattern</i> .</p>
<dl>
<dd>(error) The label on tape <i>label</i> does not match the <code>labelstr</code> <i>amanda.conf</i> option.</dl>
<p> (expecting a new tape)</p>
<dl>
<dd>(info) The tape is not OK and a new tape was expected.</dl>
<p> (expecting tape <i>label</i> or a new tape)</p>
<dl>
<dd>(info) The tape is not OK and either tape <i>label</i> or a new tape was expected.</dl>
<p> ERROR: tape <i>label</i> label ok, but is not writable.</p>
<dl>
<dd>(error) Tape <i>label</i> is OK, but the write enable test failed.</dl>
<p> Tape <i>label</i> is writable.</p>
<dl>
<dd>(info) Tape <i>label</i> is OK and the write enable test succeeded.</dl>
<p> NOTE: skipping tape-writable test.</p>
<dl>
<dd>(info) The tape write test (see the <code>-w</code> option) was not enabled.</dl>
<p> WARNING: skipping tape test because amdump or amflush seem to be running, WARNING: if they are not, you must run amcleanup</p>
<dl>
<dd>(warning) It looked to <code>amcheck</code> like either <code>amdump</code> or <code>amflush</code> were running because a log file or amdump file exists. If they are not running, you probably need to run <code>amcleanup</code> to clear up a previous failure. Otherwise, you need to wait until they complete before running <code>amcheck</code>.</dl>
<p> NOTE: skipping tape checks</p>
<dl>
<dd>(info) The tape tests are being skipped because you used the <code>-t</code> command line option.</dl>
<p> WARNING: <i>compress</i> is not executable, server-compression and indexing will not work</p>
<dl>
<dd>(warning) Compression program <i>compress</i> is not executable, so compression on the tape server host and creating index files will not work.</dl>
<p> Tape <i>label</i> label ok.</p>
<dl>
<dd>(info) Tape <i>label</i> is OK for the next run.</dl>
<p> Server check took <i>S</i> seconds.</p>
<dl>
<dd>(info) Reports how long the tape server host checks took.</dl>
<p> ERROR: <i>host</i>: could not resolve hostname</p>
<dl>
<dd>(error) Could not look up client hostname <i>host</i>.</dl>
<p> Client check: <i>H</i> hosts checked in <i>S</i> seconds, <i>N</i> problems found.</p>
<dl>
<dd>(info) Reports the number of client hosts checked, how long it took and the number of errors detected.</dl>
<p> WARNING: <i>host</i>: selfcheck request timed out. Host down?</p>
<dl>
<dd>(warning) There was no response from <i>host</i> when trying to do the client checks. The host might really be down or it might not be configured properly.</dl>
<p> ERROR: <i>host</i> NAK: <i>message</i></p>
<dl>
<dd>(error) <i>Host</i> reported a negative acknowledgment error of <i>message</i> to the status check request.</dl>
<p> ERROR: <i>host</i> NAK: [NAK parse failed]</p>
<dl>
<dd>(error) <code>Amcheck</code> could not parse the negative acknowledgment error from <i>host</i>. There might be an Amanda version mismatch between the host running <code>amcheck</code> and <i>host</i>.</dl>
<p> ERROR: <i>host</i> [mutual-authentication failed]</p>
<dl>
<dd>(error) Kerberos authentication failed while contacting <i>host</i>.</dl>
<p> ERROR: <i>host</i>: <i>message</i></p>
<dl>
<dd>(error) Error <i>message</i> was reported by the status check on <i>host</i>.</dl>
<h2>Exit Code</h2>
<p>The exit code of <code>amcheck</code> is one of: </p>
<pre> 0 = success
 1 = error</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5), <code><a href="/docs/linux/man/8-amdump/">amdump</a></code>(8) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Authors</h2>
<p><code>James da Silva</code> &lt;jds [at] amanda.org&gt; </p>
<p> <code>Stefan G. Weichinger</code> &lt;sgw [at] amanda.org&gt;</p>
