---
title: "aide(1)"
name: "aide"
section: "1"
letter: "a"
url: "/docs/linux/man/1-aide/"
description: "aide – Advanced Intrusion Detection Environment"
---

<h2>NAME</h2>
<p> <code>aide</code> &#8211; Advanced Intrusion Detection Environment</p>
<h2>SYNOPSIS</h2>
<p> <code>aide</code> [<code>parameters</code>] <code>command</code></p>
<h2>DESCRIPTION</h2>
<p> <code>aide</code> is an intrusion detection system for checking the integrity of files. </p>
<h2>COMMANDS</h2>
<dl>
<dt>&#8211;check, -C</p>
<dd> Checks the database for inconsistencies. You must have an initialized database to do this. This is also the default command. Without any command <code>aide</code> does a check.</p>
<dt>&#8211;init, -i</p>
<dd> Initialize the database. You must initialize a database and move it to the appropriate place before you can use the &#8211;check command.</p>
<dt>&#8211;update, -u</p>
<dd> Checks the database and updates the database non-interactively. The input and output databases must be different.</p>
<dt>&#8211;compare</p>
<dd> Compares two databases. They must be defined in configfile with database=&lt;url&gt; and database_new=&lt;url&gt;.</p>
<dt>&#8211;config-check, -D</p>
<dd> Stops after reading in the configuration file. Any errors will be reported. If <code>aide</code> was compiled with the &quot;<code>&#8211;with-dbhmackey</code>&quot; option, a hash for the config file will be calculated. See the aide manual for more information.</dl>
<h2>PARAMETERS</h2>
<dl>
<dt>&#8211;config=<code>configfile</code> , -c <code>configfile</code></p>
<dd> Configuration is read from file <code>configfile</code> instead of &quot;./aide.conf&quot;. Use &#8216;-&#8216; for stdin.</p>
<dt>&#8211;before=&quot;<code>configparameters</code>&quot; , -B &quot;<code>configparameters</code>&quot;</p>
<dd> These <code>configparameters</code> are handled before the reading of the configuration file. See aide.conf (5) for more details on what to put here.</p>
<dt>&#8211;after=&quot;<code>configparameters</code>&quot; , -A &quot;<code>configparameters</code>&quot;</p>
<dd> These <code>configparameters</code> are handled after the reading of the configuration file. See aide.conf (5) for more details on what to put here.</p>
<dt>&#8211;verbose=<code>verbosity_level</code>,-V<code>verbosity_level</code></p>
<dd> Controls how verbose <code>aide</code> is. Value must [0-255]. The default is 5. With no argument Value is set to 20. This parameter overrides the value set in a configuration file.</p>
<dt>&#8211;report=<code>reporter</code>,-r <code>reporter</code></p>
<dd> <code>reporter</code> is a URL which tells <code>aide</code> where to send it&#8217;s output. See aide.conf (5) section URLS for available values.</p>
<dt>&#8211;version,-v</p>
<dd> <code>aide</code> prints out its version number</p>
<dt>&#8211;help,-h</p>
<dd> Prints out the standard help message.</dl>
<h2>DIAGNOSTICS</h2>
<p> Normally, the exit status is 0 if no errors occurred. Except when the <code>&#8211;check</code> command was requested, in which case the exit status is defined as:</p>
<dl>
<dt>1 * (new files detected?) +</p>
<dd>
<dt>2 * (removed files detected?) +</p>
<dd>
<dt>4 * (changed files detected?)</p>
<dd></dl>
<p> Additionally, the following exit codes are defined for generic error conditions:</p>
<dl>
<dt>14 Error writing error</p>
<dd>
<dt>15 Invalid argument error</p>
<dd>
<dt>16 Unimplemented function error</p>
<dd>
<dt>17 Invalid configureline error</p>
<dd>
<dt>18 IO error</p>
<dd>
<dt>19 Version mismatch error</p>
<dd></dl>
<h2>NOTES</h2>
<p> Please note that due to mmap issues, aide cannot be terminated with SIGTERM. Use SIGKILL to terminate. </p>
<h2>FILES</h2>
<p> <code>/etc/aide.conf</code> Default aide configuration file. <code>/var/lib/aide.db</code> Default aide database. <code>/var/lib/aide.db.new</code> Default aide output database.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-aide-conf/">aide.conf</a></code>(5) <code><a rel="nofollow" href="http://www.cs.tut.fi/~rammer/aide/manual.html">http://www.cs.tut.fi/~rammer/aide/manual.html</a></code></p>
<h2>BUGS</h2>
<p> There are probably bugs in this release. Please report them at <a rel="nofollow" href="http://sourceforge.net/projects/aide">http://sourceforge.net/projects/aide</a> . Bug fixes are more than welcome. Unified diffs are preferred.</p>
<h2>DISCLAIMER</h2>
<p> All trademarks are the property of their respective owners. No animals were harmed while making this webpage or this piece of software. Although some pizza delivery guy&#8217;s feelings were hurt. </p>
<h2>Index</h2>
