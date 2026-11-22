---

title: "ocsinventory-agent(1)"
name: "ocsinventory-agent"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ocsinventory-agent/"
description: "ocsinventory-agent – Unified client for OCS-Inventory"
---

<p> ocsinventory-agent &#8211; Unified client for OCS-Inventory </p>
<h2>SYNOPSIS</h2>
<p> <code>ocsinventory-agent</code> [&nbsp;<wbr><code>-fhilpruw</code>&nbsp;<wbr>] [&nbsp;<wbr><i>&#8211;server server</i>&nbsp;<wbr>|&nbsp;<wbr><i>&#8211;local&nbsp;<wbr>/tmp</i>&nbsp;<wbr>]&#8230;</p>
<h2>EXAMPLES</h2>
<pre><code>
% ocsinventory - agent-- server localhost
#send an inventory to the OCS server
                     % ocsinventory -
    agent-- server http : // localhost/ocsinventory2
#send an inventory over http to a server with a non standard
#virtual directory
                          %
                          ocsinventory -
    agent-- server https : // localhost/ocsinventory
#send an inventory over https to the OCS server
                           %
                           ocsinventory -
    agent-- local / tmp
#write an inventory in the / tmp directory
        % ocsinventory -
    agent-- server localhost-- user = toto-- password = pw-- realm = "Restricted Area"
#send a report to a server protected by a basic authentification
                                                                         % ocsinventory -
                                                                     agent-- lazy
#send an inventory only if the a random delay between 0 and PROLOG_FREQ had been run over.
                                                                         % ocsinventory -
                                                                     agent-- delaytime 60 - d
#If NO PROLOG_FREQ has been preset, pick a time between execution and --delaytime for the agent to contact the server[default is 3600 seconds]
</code></pre>
<h2>DESCRIPTION</h2>
<p> <i>ocsinventory-agent</i> creates inventory and send or write them. This agent is the successor of the former linux_agent which was released with OCS 1.01 and prior. It also replaces the Solaris/AIX/BSD unofficial agents. The detailed list of supported Operating System is available in the Wiki.</p>
<dl>
<dt><i>GNU/Linux</i></dt>
<dd>
</dd><dt><i>Solaris</i></dt>
<dd>
</dd><dt><i>FreeBSD</i></dt>
<dd>
</dd><dt><i>NetBSD</i></dt>
<dd>
</dd><dt><i>OpenBSD</i></dt>
<dd>
</dd><dt><i></i><i>AIX</i><i></i></dt>
<dd>
</dd><dt><i>MacOSX</i></dt>
<dd>
</dd><dt><i>GNU/kFreeBSD</i></dt>
<dd></dd></dl>
<h2>OPTIONS</h2>
<p> Most of the options are available in a <i>short</i> form and a <i>long</i> form. For example, the two lines below are all equivalent: </p>
<pre>
    % ocsinventory-agent -s localhost
    % ocsinventory-agent --server localhost
</pre>
<dl>
<dt><code>&#8211;backend-collect-timeout=SECONDS_BEFORE_KILL</code></dt>
<dd> Time before OCS kills modules processing which don&#8217;t end before the timeout.</dd>
<dt><code>&#8211;basevardir</code>=<i></i><i>DIR</i><i></i></dt>
<dd> Indicate the place where the agent should store its files.</dd>
<dt><code>-d</code>, <code>&#8211;daemon</code></dt>
<dd> Launch ocsinventory-agent in background. Proc::Daemon is needed.</dd>
<dt><code>&#8211;debug</code></dt>
<dd> Turn the debug mode on.</dd>
<dt><code>&#8211;devlib</code></dt>
<dd> This option is designed for backend module developer. With it enabled, ocsinventry-agent won&#8217;t try to load the Backend module installed on the system. Instead it will scan the ./lib directory.</dd>
<dt><code>&#8211;delaytime=SECONDS_TO_WAIT</code></dt>
<dd> This option defaults to waiting a <i>random()</i> time between 0 and 3600 before initially contacting the server assuming NO PROLOG_FREQ has been set. Once PROLOG_FREQ has been set, it uses that number at the top end of it&#8217;s random setting. Useful for pre-setting a deployed agent&#8217;s initial start time (so you don&#8217;t jam the server all at once, but don&#8217;t have to wait an hour to make sure the deployment worked).</dd>
<dt><code>-f</code>, <code>&#8211;force</code></dt>
<dd> The agent will first contact the server during the PROLOG period. If the server doesn&#8217;t know the machine or has outdated informations, it will ask for an inventory. With this option, the agent doesn&#8217;t run the PROLOG with the server first but directly sends an inventory.</dd>
<dt><code>-i</code>, <code>&#8211;info</code></dt>
<dd> Turn the verbose mode on. The flag is ignored if <code>&#8211;debug</code> is enable.</dd>
<dt><code>&#8211;lazy</code></dt>
<dd> Do not contact the server more than one time during the PROLOG_FREQ and do an exit if there is nothing to do. Useful if you want to start the agent script regulary from the crontab but don&#8217;t want to overload the server.</dd>
<dt><code>-l</code>, <code>&#8211;local</code>=<i></i><i>DIR</i><i></i></dt>
<dd> Write an inventory in the <i></i><i>DIR</i><i></i> directory. A new file will be created if needed.</dd>
<dt><code>&#8211;logfile</code>=<i></i><i>FILE</i><i></i></dt>
<dd> Log message in <i></i><i>FILE</i><i></i> and turn off STDERR</dd>
<dt><code>-p</code>, <code>&#8211;password</code>=<i></i><i>PASSWORD</i><i></i></dt>
<dd> Use <i></i><i>PASSWORD</i><i></i> for an HTTP identification with the server.</dd>
<dt><code>-P</code>, <code>&#8211;proxy</code>=<i></i><i>PROXY</i><i></i></dt>
<dd> Use <i></i><i>PROXY</i><i></i> to specify a proxy HTTP server. By default, the agent uses HTTP_PROXY environment variable.</dd>
<dt><code>-r</code>, <code>&#8211;realm</code>=<i></i><i>REALM</i><i></i></dt>
<dd> Use <i></i><i>REALM</i><i></i> for an HTTP identification with the server. For example, the value can be &#8216;Restricted Area&#8217;. You can find it in the login popup of your Internet browser.</dd>
<dt><code>-s</code>, <code>&#8211;server</code>=<i></i><i>URI</i><i></i></dt>
<dd> The uri of the server. If <i></i><i>URI</i><i></i> doesn&#8217;t start with http:// or <a rel="nofollow" href="https://,">https://,</a> the assume the parameter is a hostname and rewrite it like that: </dd>
<pre>
    % <a rel="nofollow" href="http://servername/ocsinventory">http://servername/ocsinventory</a>
</pre>
<p> If you want to use https or another virtual directory you need to enter the full path. </p>
<p> <code>&#8211;server</code> is ignored if <code>&#8211;local</code> is in use.</p>
<dt><code>&#8211;stdout</code></dt>
<dd> Print the inventory on stdout. </dd>
<pre>
    % ocsinventory-agent --stdout &gt; /tmp/report.xml
    # prepare an inventory and write it in the /tmp/report.xml file.
    # A file will be created.
</pre>
<dt><code>&#8211;scan-homedirs</code></dt>
<dd> Authorized OCS to scan home directories to increase the Virtual Machine inventory.</dd>
<dt><code>&#8211;tag</code>=<i></i><i>TAG</i><i></i></dt>
<dd> Mark the machine with the <i></i><i>TAG</i><i></i> tag. Once the initial inventory is accepted by the server this value is ignored and you&#8217;ve to change the information directly on the server. The server do so in order to centralize the administration of the machine.</dd>
<dt><code>-u</code> <i></i><i>USER</i><i></i>, <code>&#8211;user</code>=<i></i><i>USER</i><i></i></dt>
<dd> Use <i></i><i>USER</i><i></i> for the server authentification.</dd>
<dt><code>&#8211;version</code>=<i></i><i>USER</i><i></i></dt>
<dd> Print the version and exit.</dd>
<dt><code>-w</code> <i></i><i>DURATION</i><i></i>, <code>&#8211;wait</code>=<i></i><i>DURATION</i><i></i></dt>
<dd> Wait before initializing the connexion with the server. If <i></i><i>DURATION</i><i></i> equal <i>server</i> the agent will use the PROLOG_FREQ of the server to determine the duration of this periode. Exactly like it would had done if it was in &#8211;daemon mode. Else if duration is a numerical value, it will be used directly. </dd>
<pre>
    % ocsinventory-agent --wait 5 --server localhost
</pre>
<dt><code>&#8211;nosoftware</code></dt>
<dd> Do not inventory the software installed on the machine. <code>&#8211;nosoft</code> also works but is deperecated.</dd></dl>
<h2>CONFIG FILE</h2>
<p> The agent try to initialize the settings from the <code>ocsinventory-agent.cfg</code> config file. </p>
<p> It looks for the file in these directories:</p>
<dl>
<dt>/etc/ocsinventory</dt>
<dd>
</dd><dt>/usr/local/etc/ocsinventory</dt>
<dd>
</dd><dt>/etc/ocsinventory-agent</dt>
<dd></dd></dl>
<h2>AUTHORS</h2>
<p> The maintainer is Goneri LE BOUDER &lt;goneri [at] rulezlan.org&gt; </p>
<p> Please read the AUTHORS, Changes and THANKS files to see who is behind OCS Inventory Agent.</p>
<h2>SEE ALSO</h2>
<dl>
<dt>OCS-Inventory website,</dt>
<dd>
<pre>
 <a rel="nofollow" href="http://www.ocsinventory-ng.org/">http://www.ocsinventory-ng.org/</a>
</pre>
</dd><dt>LaunchPad project page,</dt>
<dd>
<pre>
 <a rel="nofollow" href="http://launchpad.net/ocsinventory-unix-agent">http://launchpad.net/ocsinventory-unix-agent</a>
</pre>
</dd><dt>forum,</dt>
<dd>
<pre>
 <a rel="nofollow" href="http://forums.ocsinventory-ng.org/">http://forums.ocsinventory-ng.org/</a>
</pre>
</dd><dt>and wiki</dt>
<dd>
<pre>
 <a rel="nofollow" href="http://wiki.ocsinventory-ng.org/">http://wiki.ocsinventory-ng.org/</a>
</pre>
</dd></dl>
<h2>BUGS</h2>
<p> Please, use the forum as much as possible. You can open your own bug tickets. Patches are welcome. You can also use LaunchPad bugtracker or push your Bazaar branch on LaunchPad and do a merge request.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2006-2009 OCS Inventory contributors </p>
<pre>
 This program is free software; you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation; either version 2 of the License, or
 (at your option) any later version.
 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 GNU General Public License for more details.
 You should have received a copy of the GNU General Public License
 along with this program; if not, write to the Free Software
 Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
</pre>
