---
title: "amserverconfig(8)"
name: "amserverconfig"
section: "8"
letter: "a"
url: "/docs/linux/man/8-amserverconfig/"
description: "amserverconfig – program to setup initial Amanda configuration"
---

<p>amserverconfig &#8211; program to setup initial Amanda configuration</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>amserverconfig</code> <i>config</i> [&#8211;template&nbsp;<wbr><i>template</i>] [&#8211;no-vtape] [&#8211;tapetype&nbsp;<wbr><i>tapetype</i>] [&#8211;tpchanger&nbsp;<wbr><i>tpchanger</i>] [&#8211;tapedev&nbsp;<wbr><i>tapedev</i>] [&#8211;changerfile&nbsp;<wbr><i>changerfile</i>] [&#8211;changerdev&nbsp;<wbr><i>changerdev</i>] [&#8211;labelstr&nbsp;<wbr><i>labelstr</i>] [&#8211;mailto&nbsp;<wbr><i>mailto</i>] [&#8211;dumpcycle&nbsp;<wbr><i>dumpcycle</i>] [&#8211;runspercycle&nbsp;<wbr><i>runspercycle</i>] [&#8211;runtapes&nbsp;<wbr><i>runtapes</i>] [&#8211;tapecycle&nbsp;<wbr><i>tapecycle</i>] [&#8211;help]</dl>
<h2>Description</h2>
<dd>After Amanda rpms are successfully installed, <code>amserverconfig</code> will setup initial Amanda configuration files. It will create /var/lib/amanda/guntar-lists directory if one does not exist. <code>amserverconfig</code> does not change existing Amanda configurations. <code>amserverconfig</code> must be run by user amandabackup.</p>
<h2>Options</h2>
<p>Options may be abbreviated, as long as the abbreviation is not ambiguous. Option argument can either separated by &#8216;=&#8217; or a space. Example: &#8211;templ=harddisk &#8211;tapedev /dev/nst0 </p>
<p> <code>amserverconfig</code> builds a new &quot;config&quot; Amanda configuration. Customize the configuration with the options below. </p>
<p> <code>&#8211;template template</code></p>
<dl>
<dd>build Amanda configuration with pre-configured template files. Currently, <code>harddisk</code>, <code>single-tape</code>, <code>tape-changer</code> and <code>S3</code> are the valid inputs for this option. Pre-configured template files can be found in /var/lib/amanda/template.d. This option may be combined with other options. </p>
<p> If tape-changer is chosen for this option, program mtx is required. <code>amserverconfig</code> will search for mtx in the following directory: &quot;/usr/sbin&quot;, &quot;/usr/local/sbin&quot;, &quot;/usr/local/bin&quot;, &quot;/usr/bin&quot;, &quot;/bin&quot; and amandabackup&#8217;s PATH. </p>
<p> If harddisk is chosen and &#8211;no-vtape is not specified, <code>amserverconfig</code> will create and label virtual tape file://var/lib/amanda/vtapes/$config.</dl>
<p> <code>&#8211;no-vtape</code></p>
<dl>
<dd>Do not create virtual tapes in the harddisk template case.</dl>
<p> <code>&#8211;tapedev tapedev</code></p>
<dl>
<dd>The path name of non-rewinding tape device. default [file://var/lib/amanda/vtapes/$config]</dl>
<p> <code>&#8211;tpchanger tpchanger</code></p>
<dl>
<dd>The name of the tape changer. default [chg-disk]</dl>
<p> <code>&#8211;changerdev changerdev</code></p>
<dl>
<dd>A tape changer configuration parameter. default [/dev/null]</dl>
<p> <code>&#8211;changerfile changerfile</code></p>
<dl>
<dd>A tape changer configuration parameter. default [/etc/amanda/$config/changer.conf]</dl>
<p> <code>&#8211;labelstr labelstr</code></p>
<dl>
<dd>The tape label constraint regular expression. default [^$config-[0-9][0-9]*$] </p>
<p> If this option is used with &#8211;template=harddisk, only alphanumeric string is supported.</dl>
<p> <code>&#8211;tapetype tapetype</code></p>
<dl>
<dd>The type of tape drive associated with tapedev or tpchanger. default [HARDDISK]</dl>
<p> <code>&#8211;mailto mailto</code></p>
<dl>
<dd>A space separated list of recipients for mail reports. default [amandabackup]</dl>
<p> <code>&#8211;dumpcycle dumpcycle</code></p>
<dl>
<dd>The number of days in the backup cycle. default [1week]</dl>
<p> <code>&#8211;runspercycle runspercycle</code></p>
<dl>
<dd>The number of days in the backup cycle. default [5]</dl>
<p> <code>&#8211;runtapes runtapes</code></p>
<dl>
<dd>The maximum number of tapes used in a single run. default [1]</dl>
<p> <code>&#8211;tapecycle tapecycle</code></p>
<dl>
<dd>The size of tape rotation. default [25]</dl>
<p> <code>&#8211;help</code></p>
<dl>
<dd>Display usage.</dl>
<h2>Files</h2>
<p><code>/var/lib/amanda/template.d</code></p>
<dl>
<dd>Amanda configuration template files install location</dl>
<p> <code>/var/lib/amanda</code></p>
<dl>
<dd>amandabackup home directory</dl>
<p> <code>/var/lib/amanda/gnutar-lists</code></p>
<dl>
<dd>A directory which contains backup timestamp and list of files backed up.</dl>
<p> <code>/etc/amanda/$config</code></p>
<dl>
<dd>Amanda configuration files location for $config(e.g: DailySet1).</dl>
<p> <code>/etc/amanda/template.d</code></p>
<dl>
<dd>A directory contains dumptypes and tapetypes files used by all Amanda configurations.</dl>
<p> <code>/etc/amandates</code></p>
<dl>
<dd>Amanda file on the client. It keeps track of structures of previous dumps.</dl>
<p> <code>/tmp/amanda</code></p>
<dl>
<dd>directory contains Amanda debug log files.</dl>
<h2>Return Value</h2>
<p>On success, zero is returned. On error, 1 is returned.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5), <code><a href="/docs/linux/man/8-amaddclient/">amaddclient</a></code>(8) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Author</h2>
<p><code>Kevin Till</code> &lt;kevin.till [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>
