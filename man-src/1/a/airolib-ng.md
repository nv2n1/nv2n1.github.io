---
title: "airolib-ng(1)"
name: "airolib-ng"
section: "1"
letter: "a"
url: "/docs/linux/man/1-airolib-ng/"
description: "airolib-ng – manage and create a WPA/WPA2 pre-computed hashes tables"
---

<h2 class="name">NAME</h2>
<p> airolib-ng &#8211; manage and create a WPA/WPA2 pre-computed hashes tables </p>
<h2>SYNOPSIS</h2>
<p> <code>airolib-ng</code> &lt;database&gt; &lt;operation&gt; [options]</p>
<h2>DESCRIPTION</h2>
<p> <code>airolib-ng</code> is a tool for the aircrack-ng suite to store and manage essid and password lists, compute their Pairwise Master Keys (PMKs) and use them in WPA/WPA2 cracking. The program uses the lightweight SQLite3 database as the storage mechanism which is available on most platforms. The SQLite3 database was selected taking in consideration platform availability plus management, memory and disk overhead.</p>
<h2>DATABASE</h2>
<dl>
<dt><i>database</i></p>
<dd> It is name of the database file. Optionally specify the full path.</dl>
<h2>OPERATION</h2>
<dl>
<dt><i>&#8211;stats</i></p>
<dd> Output information about the database.</p>
<dt><i>&#8211;sql &lt;sql&gt;</i></p>
<dd> Execute specified SQL statement.</p>
<dt><i>&#8211;clean [all]</i></p>
<dd> Clean the database from old junk. When specifying &#8216;all&#8217;, it will also reduce filesize if possible and run an integrity check.</p>
<dt><i>&#8211;batch</i></p>
<dd> Start batch-processing all combinations of ESSIDs and passwords.</p>
<dt><i>&#8211;verify [all]</i></p>
<dd> Verify a set of randomly chosen PMKs. If &#8216;all&#8217; is given, all invalid PMK in the database will be deleted.</p>
<dt><i>&#8211;import [essid|passwd] &lt;file&gt;</i></p>
<dd> Import a flat file as a list of ESSIDs or passwords.</p>
<dt><i>import cowpatty &lt;file&gt;</i></p>
<dd> Import a coWPAtty file.</p>
<dt><i>&#8211;export cowpatty &lt;essid&gt; &lt;file&gt;</i></p>
<dd> Export to a cowpatty file.</dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Thomas d&#8217;Otreppe. Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-airbase-ng/">airbase-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-aireplay-ng/">aireplay-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-airmon-ng/">airmon-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-airodump-ng/">airodump-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-airodump-ng-oui-update/">airodump-ng-oui-update</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-airserv-ng/">airserv-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-airtun-ng/">airtun-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-besside-ng/">besside-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-easside-ng/">easside-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-tkiptun-ng/">tkiptun-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-wesside-ng/">wesside-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/1-aircrack-ng/">aircrack-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airdecap-ng/">airdecap-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airdecloak-ng/">airdecloak-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-besside-ng-crawler/">besside-ng-crawler</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-buddy-ng/">buddy-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-ivstools/">ivstools</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-kstats/">kstats</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-makeivs-ng/">makeivs-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-packetforge-ng/">packetforge-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-wpaclean/">wpaclean</a>(1)</code> </p>
<h2>Index</h2>
