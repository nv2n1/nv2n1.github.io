---
title: "xpdtest(1)"
name: "xpdtest"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xpdtest/"
description: "xpdtest – xproofd test utility"
---

<h2 class="name">NAME</h2>
<p> xpdtest &#8211; xproofd test utility </p>
<h2>SYNOPSIS</h2>
<p> <code>xpdtest</code> <i>[options]</i></p>
<h2>DESCRIPTION</h2>
<p> This manual page documents the <code>xpdtest</code> program, an utility whose purpose is to test the status of an xproofd daemon running on the local machine. The target is to run <code>xpdtest</code> inside a monitor infrastructure, for example <code>monit</code> (see <i><a rel="nofollow" href="http://mmonit.com/monit/">http://mmonit.com/monit/</a></i> ), capable to take some decisions and to do some actions following the result of <code>xpdtest.</code> </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help, -h</code></p>
<dd> Gives a short list of options avaliable, and exit</p>
<dt><code>-t</code> &lt;test&gt;</p>
<dd> type of test to be run:<br />
&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ping the daemon&nbsp;<wbr>(includes process existence check if pid specified;&nbsp;<wbr>see below)<br />
&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ping the daemon and check connection for default user<br />
&nbsp;<wbr>2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ping the daemon and check connection for the default user and all recent users </p>
<p> The default user is the one specified in the URL (e.g. &#8216;user&#8217; for user [at] localhost); if no explicit specification is found in the URL, the user under which <code>xpdtest</code> is run is used; it can be also passed via the environment variable <code>XPDTEST_TEST.</code></p>
<dt><code>-u</code> &lt;url&gt;</p>
<dd> URL where the xproofd under test responds; it can be also passed via the environment variable <code>XPDTEST_URL</code> (default is &#8216;localhost:1093&#8217;).</p>
<dt><code>-d</code> &lt;sbdir&gt;</p>
<dd> sandbox directory used to find out the users of the facility when test is 2; it can be also passed via the environment variable <code>XPDTEST_SBOXDIR</code> (default is &#8216;/tmp/proofbox&#8217;).</p>
<dt><code>-s</code> &lt;span&gt;</p>
<dd> define the time interval, in minutes, to define &#8216;recent&#8217; users when test is 2: only users who connected within this interval are checked; use -1 for infinite; it can be also passed via the environment variable <code>XPDTEST_TIMESPAN</code> (default is -1).</p>
<dt><code>-T</code> &lt;timeout&gt;</p>
<dd> define the time, in seconds, waited for the session to start successfully; it can be also passed via the environment variable <code>XPDTEST_TIMESOUT</code> (default is 10 seconds).</p>
<dt><code>-l</code> &lt;logfile&gt;</p>
<dd> log file if not screen; deleted if the required test fails unless &#8216;-k&#8217; is specified (see below);it can be also passed via the environment variable <code>XPDTEST_LOGFILE.</code></p>
<dt><code>-p</code> &lt;pidfile&gt;</p>
<dd> file with the process ID as a integer number in the first line; if this file is given a quick test on the process existence is done using kill(pid,0); it can be also passed via the environment variable <code>XPDTEST_PIDFILE.</code></p>
<dt><code>-k</code></p>
<dd> keep log file at path given via &#8216;-l&#8217; in all cases; it can be also passed via the environment variable <code>XPDTEST_KEEP</code> (default is &#8216;no keep&#8217;).</p>
<dt><code>-v</code></p>
<dd> set <code>gDebug=1</code> for the underline ROOT calls; it can be also passed via the environment variable <code>XPDTEST_VERBOSE</code> (default is &#8216;no verbose&#8217;).</dl>
<h2>RETURN</h2>
<p> <code>xpdtest</code> returns 0 on success and 1 in case of test failure. Errors are printed on the screen or saved into the specified log file. </p>
<h2>FILES</h2>
<p> The file <code>xpdtest_popen_file</code> in the temporary directory (typically /tmp) is used to parse the output of <code>TProof::Open().</code> The file is overwritten by each new attempt; after a run of <code>xpdtest</code> it contains the result of the last session open attempt. </p>
<h2>NOTES</h2>
<p> The connection attempt is done in <code>&#8216;masteronly&#8217;</code> mode. For daemons running in <code>&#8216;worker&#8217;</code> mode the attempt will fail with a well defined error message (&#8216;Server not allowed to be top master&#8217;); since this indicates that the daemon is anyhow responsive, a positive detection of such a pattern in the error message is interpreted as the attempt having being successful. </p>
<h2>ORIGINAL AUTHORS</h2>
<p> The ROOT team:</p>
<dl>
<dt>
<dd> <code>Rene Brun</code> and <code>Fons Rademakers</code></dl>
<p> More information can be found at the <code>ROOT</code> website: <i><a rel="nofollow" href="http://root.cern.ch">http://root.cern.ch</a></i></p>
<h2>COPYRIGHT</h2>
<p> This library is free software; you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation; either version 2.1 of the License, or (at your option) any later version. </p>
<p> This library is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details. </p>
<p> You should have received a copy of the GNU Lesser General Public License along with this library; if not, write to the Free Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Gerardo Ganis &lt;gerardo.ganis [at] cern.ch&gt;, for the GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>
