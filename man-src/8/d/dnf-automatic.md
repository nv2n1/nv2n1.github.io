---
title: "dnf-automatic(8)"
name: "dnf-automatic"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dnf-automatic/"
description: "dnf.automatic – DNF Automatic"
---

<p>dnf.automatic &#8211; DNF Automatic</p>
<h2>Synopsis</h2>
<p><code>dnf-automatic [&lt;config file&gt;]</code></p>
<h2>Description</h2>
<p>Alternative CLI to <code>dnf upgrade</code> with specific facilities to make it suitable to be executed automatically and regularly from systemd timers, cron jobs and similar. </p>
<p> The operation of the tool is completely controlled by the configuration file and the command only accepts single optional argument pointing to it. If no configuration file is passed from the command line, <code>/etc/dnf/automatic.conf</code> is used. </p>
<p> The tool synchronizes package metadata as needed and then checks for updates available for the given system and then either exits, downloads the packages or downloads and applies the packages. The outcome of the operation is then reported by a selected mechanism, for instance via the standard output, email or motd messages.</p>
<h2>Configuration File Format</h2>
<p>The configuration file is separated into topical sections.</p>
<h3><code>[command]</code> section</h3>
<p>Setting the mode of operation of the program.</p>
<dl>
<dt><code>apply_updates</code></p>
<dd>boolean, default: False </p>
<p> Whether packages comprising the available should be applied (i.e. installed via RPM). Implies <code>download_updates</code>.</p>
<dt><code>download_updates</code></p>
<dd>boolean, default: False </p>
<p> Whether packages comprising the available should be downloaded.</p>
<dt><code>upgrade_type</code></p>
<dd>either one of <code>default</code>, <code>security</code>, default: <code>default</code> </p>
<p> What kind of upgrades to look at. <code>default</code> signals looking for all available updates, <code>security</code> only those with an issued security advisory.</dl>
<h3><code>[emitters]</code> section</h3>
<p>Choosing how the results should be reported.</p>
<dl>
<dt><code>emit_via</code></p>
<dd>list, default: <code>email, stdio, motd</code> </p>
<p> List of emitters to report the results through. Available emitters are <code>stdio</code> to print the result to standard output, <code>email</code> to send the report via email and <code>motd</code> sends the result to <i>/etc/motd</i> file.</p>
<dt><code>system_name</code></p>
<dd>string, default: hostname of the given system </p>
<p> How the system is called in the reports.</dl>
<h3><code>[email]</code> section</h3>
<p>The email emitter configuration.</p>
<dl>
<dt><code>email_from</code></p>
<dd>string, default: <code>root</code> </p>
<p> Message&#8217;s &quot;From:&quot; address.</p>
<dt><code>email_to</code></p>
<dd>list, default: <code>root</code> </p>
<p> List of recipients of the message.</p>
<dt><code>email_host</code></p>
<dd>string, default: <code>localhost</code> </p>
<p> Hostname of the SMTP server used to send the message.</dl>
<h3><code>[base]</code> section</h3>
<p>Can be used to override settings from DNF&#8217;s main configuration file. See <code>command_ref</code>.</p>
<h2>Author</h2>
<p>See AUTHORS in DNF source distribution.</p>
<h2>Copyright</h2>
<p>2012-2014, Red Hat, Licensed under GPLv2+</p>
