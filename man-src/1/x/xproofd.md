---
title: "xproofd(1)"
name: "xproofd"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xproofd/"
description: "xproofd – PROOF (The Parallel ROOT Facility) xrootd version"
---

<h2 class="name">NAME</h2>
<p> xproofd &#8211; PROOF (The Parallel ROOT Facility) xrootd version </p>
<h2>SYNOPSIS</h2>
<p> <code>xproofd</code> [<code> -c </code><i>cfn</i> ] [<code> -d </code>] [<code> -l </code><i>fnc</i> ] [<code> -n </code><i>name</i> ] [<code> -p </code><i>port</i> ] [<code> -P </code><i>prot</i> ] [<i> prot_options </i>]</p>
<h2>DESCRIPTION</h2>
<p> Using <code>PROOF</code><i> (The P</i>arallel <i>ROO</i>T <i>F</i>acility) one can analyze trees in parallel on a cluster of computers. The <code>PROOF</code> system consists of the <i><a href="/docs/linux/man/1-xproofd/">xproofd</a></i>(1) from-end program which is started via <i><a href="/docs/linux/man/8-inetd/">inetd</a></i>(8). </p>
<p> <i>xproofd</i> takes care of user authentication and overlays itself then with the desired version of the <i><a href="/docs/linux/man/1-proofserv/">proofserv</a></i>(1) executable. </p>
<p> interactive module <i><a href="/docs/linux/man/1-root/">root</a></i>(1), except that it reads its commands from a socket instead of from the terminal. </p>
<p> Since it is a remote server it will not do graphics and therefore is not linked with any graphics libraries (Motif, X11, etc.). </p>
<h2>SETTING UP PROOF</h2>
<p> Since you need to handle sensitive system files, you need to have root (the user, not the program!) privileges. Also, it&#8217;s recommended that you read the appropriate <i><a href="/docs/linux/man/1-man/">man</a></i>(1) pages first. These are <i><a href="/docs/linux/man/8-inetd/">inetd</a></i>(8) (the internet daemon), <i><a href="/docs/linux/man/8-sysklogd/">sysklogd</a></i>(8) and <i><a href="/docs/linux/man/3-syslog/">syslog</a></i>(3) (the system logger daemon), and <i><a href="/docs/linux/man/8-init/">init</a></i>(8) (the SYSV process control initializer). </p>
<p> In other words:</p>
<dl>
<dt>
<dd> <i>Be very VERY carefull when installing </i><code>xproofd</code></dl>
<p> There, I said it. And ofcourse, no warrenties what so ever.</p>
<dl>
<dt>1</p>
<dd> Make sure every node has <code>ROOT</code> installed. We&#8217;ll assume you installed the <code>ROOT</code> applications in &lt;<i>bindir</i>&gt; (e.g. <i>/usr/bin</i>) and the <code>PROOF</code> configuration files in files in <i>&lt;xproofdir&gt;/etc</i><code> (e.g. </code><i>/usr/share/root/etc</i><code>). </p>
<dt>2</p>
<dd> The TCP port 1094 was allocated by IANA</code>, ( <i><a rel="nofollow" href="http://www.iana.org">www.iana.org</a></i> ), to <code>xrootd</code>, so add to <i>/etc/services</i> the lines: </p>
<pre>
  xproofd  1093/tcp
  xrootd   1094/tcp
</pre>
<dt>3</p>
<dd> On each node, add to <i>/etc/inetd.conf</i> the lines: </p>
<pre>
  xproofd stream tcp nowait root &lt;<i>bindir</i>&gt;/xproofd xproofd &lt;<i>xproofdir</i>&gt;/proof
  xrootd stream tcp nowait root &lt;<i>bindir</i>&gt;/xrootd xrootd -i
</pre>
<p> You can substitute the &lt;<i>xproofdir</i>&gt; with any directory that holds your <code>PROOF</code> configuration, for example <i>/etc/root/proof</i>. However, it should be shared among all nodes in the cluster. </p>
<dt>4</p>
<dd> Restart <code>inetd</code> or force it to re-read the config file: </p>
<pre>
  kill -1 &lt;<i>inetd pid</i>&gt;
</pre>
<p> If you use <code>SYSV</code> <i><a href="/docs/linux/man/8-init/">init</a></i>(8) scripts, you can probaly just do </p>
<pre>
  /etc/init.d/inetd restart
</pre>
<p> or whatever is appropriate for your system. </p>
<dt>5</p>
<dd> On the master node, add to <i>/etc/syslog.conf</i> the line: </p>
<pre>
    local5,local6.debug     &lt;<i>xproofdir</i>&gt;/log/proof.log
</pre>
<p> and all slave nodes: </p>
<pre>
    local5,local6.debug     @&lt;<i>master hostname</i>&gt;
</pre>
<p> where &lt;<i>master hostname</i>&gt; is domain name of the master node. All PROOF syslog messages will be collected on the master node. Just make one node in the cluster the master, all others are slaves. </p>
<dt>6</p>
<dd> On all nodes, change the below lines in <i>/etc/syslog.conf</i>, </p>
<pre>
    *.info;mail.none;news.none;authpriv.none  /var/log/messages
</pre>
<p> to: </p>
<pre>
    *.info;local5,local6,mail.none;news.none;authpriv.none  /var/log/messages
</pre>
<dt>7</p>
<dd> Create an empty &lt;<i>xproofdir</i>&gt;/log/proof.log: </p>
<pre>
    echo &quot;&quot; &gt; &lt;<i>xproofdir</i>&gt;/log/proof.log
</pre>
<dt>8</p>
<dd> Restart syslogd or force it to re-read the config file: </p>
<pre>
  kill -1 &lt;<i>syslogd pid</i>&gt;.
</pre>
<p> If you use <code>SYSV</code> <i><a href="/docs/linux/man/8-init/">init</a></i>(8) scripts, you can probaly just do </p>
<pre>
  /etc/init.d/sysklogd restart
</pre>
<p> or whatever is appropriate for your system. </p>
<dt>9</p>
<dd> Edit &lt;<i>xproofdir</i>&gt;<i>/etc/proof.conf</i> to reflect your cluster configuration. See the example <i>proof.conf</i> file for more information.</dl>
<p> If you installed <code>ROOT</code> using some precompiled package (for example a <code>Redhat Linux</code> or a <code>Debian GNU/Linux</code> package), steps 2 to 4 may already be done for you. </p>
<p> If you&#8217;re running <code>Linux</code>, Steps 5 to 7 can be somewhat automated using the script <i>proof-facility</i> in &lt;<i>xproofdir</i>&gt; of your distribution. This script uses <i><a href="/docs/linux/man/1-syslog-facility/">syslog-facility</a></i>(1), from the <code>Linux</code> <i><a href="/docs/linux/man/1-syslog/">syslog</a></i>(1) distribution, and may run on other platforms as well &#8211; but no warrenties mind you! </p>
<p> Step 9 is completely up to the user.</p>
<h2>EXAMPLE</h2>
<p> That&#8217;s it. To test PROOF try the following: </p>
<pre><code>
root[1] gROOT-&gt;Proof("&lt;master hostname&gt;")
    root[2] gPROOF-&gt;Print()&lt;shows information on the master and all active slave servers&gt; root[3]
        .q
</code></pre>
<h2>FILES</h2>
<dl>
<dt>&lt;<i>xproofdir</i><code>&gt;</p>
<dd> The location of your PROOF</code><i> data. In binary packages, like for </i><code>Redhat Linux</code><i>I or </i><code>Debian GNU/Linux</code>, this will probably be <i>/usr/share/root/proof</i><code>. If you got a binary </code><i><a href="/docs/linux/man/1-tar/">tar</a></i>(1)-ball from the <code>ROOT</code> website, or a build it yourself without the static paths option, then this directory could be ROOTSYS/proof. However, you may set it to something else when starting your server.</p>
<dt>&lt;<i>xproofdir</i><code>&gt;/etc</code></p>
<dd> This directory holds all the configuration files for your cluster(s).</p>
<dt>&lt;<i>xproofdir</i><code>&gt;/etc/&lt;cluster&gt;.conf</code></p>
<dd> This is the cluster named &lt;<i>cluster</i>&gt; configuration file. See &lt;<i>xproofdir</i><code>&gt;/etc/&lt;cluster&gt;.conf.sample</code> for an example.</p>
<dt>&lt;<i>xproofdir</i><code>&gt;/etc/motd</code></p>
<dd> This is Message-Of-The-Day file. See &lt;<i>xproofdir</i><code>&gt;/etc/motd.sample</code> for an example.</p>
<dt>&lt;<i>xproofdir</i><code>&gt;/etc/noproof</code></p>
<dd> If this file is present, all <code>PROOF</code> services will be diabled. See &lt;<i>xproofdir</i><code>&gt;/etc/noproof.sample</code> for an example.</p>
<dt>&lt;<i>xproofdir</i><code>&gt;/etc/proof.conf</code></p>
<dd> This is the <code>PROOF</code> configuration file. See &lt;<i>xproofdir</i><code>&gt;/etc/proof.conf.sample</code> for an example.</p>
<dt><code>~/.rootnetrc.conf</code></p>
<dd> Configuration file for network access. Here you specify login names and pass word, so it <code>MUST</code><i> be read/write-able only by the user. See &lt;xproofdir</i><code>&gt;/etc/rootnetrc.conf.sample</code> for an example.</p>
<dt>&lt;<i>xproofdir</i><code>&gt;/log</code></p>
<dd> This directory holds the log files from the master and slaves. &lt;<i>xproofdir</i><code>&gt;/log/proof.log</code> <i><a href="/docs/linux/man/1-syslog/">Syslog</a></i>(1) log file for <code>PROOF</code>.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-proofserv/">proofserv</a></i>(1) , <i><a href="/docs/linux/man/1-root/">root</a></i>(1) , <i><a href="/docs/linux/man/1-rootd/">rootd</a></i>(1) , <i><a href="/docs/linux/man/1-xrootd/">xrootd</a></i>(1) </p>
<p> More information can be found at the <code>ROOT</code> website: <i><a rel="nofollow" href="http://root.cern.ch">http://root.cern.ch</a></i></p>
<h2>ORIGINAL AUTHORS</h2>
<p> The ROOT team (see web page above):</p>
<dl>
<dt>
<dd> <code>Rene Brun</code> and <code>Fons Rademakers</code></dl>
<h2>COPYRIGHT</h2>
<p> This library is free software; you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation; either version 2.1 of the License, or (at your option) any later version. </p>
<p> This library is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details. </p>
<p> You should have received a copy of the GNU Lesser General Public License along with this library; if not, write to the Free Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Christian Holm Christensen &lt;cholm [at] nbi.dk&gt;, for the Debian GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>
