---
title: "amaddclient(8)"
name: "amaddclient"
section: "8"
letter: "a"
url: "/docs/linux/man/8-amaddclient/"
description: "amaddclient – program to add client to an existing Amanda configuration"
---

<p>amaddclient &#8211; program to add client to an existing Amanda configuration</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>amaddclient</code> &#8211;config <i>config</i> ||<br />
&nbsp;<wbr>&#8211;client&nbsp;<wbr><i>client name</i>&nbsp;<wbr>||<br />
&nbsp;<wbr>&#8211;diskdev&nbsp;<wbr><i>directory to backup</i>&nbsp;<wbr>[&#8211;m]&nbsp;<wbr>[&#8211;dumptype&nbsp;<wbr><i>string</i>]&nbsp;<wbr>[&#8211;includefile&nbsp;<wbr><i>string</i>]&nbsp;<wbr>[&#8211;includelist&nbsp;<wbr><i>string</i>]&nbsp;<wbr>[&#8211;excludefile&nbsp;<wbr><i>string</i>]&nbsp;<wbr>[&#8211;excludelist&nbsp;<wbr><i>string</i>]&nbsp;<wbr>[&#8211;user&nbsp;<wbr><i>string</i>]&nbsp;<wbr>[&#8211;auth&nbsp;<wbr><i>string</i>]&nbsp;<wbr>[&#8211;gnutar_list_dir&nbsp;<wbr><i>string</i>]&nbsp;<wbr>[&#8211;amandates&nbsp;<wbr><i>string</i>]&nbsp;<wbr>[&#8211;no-client-update]&nbsp;<wbr>[&#8211;batch]&nbsp;<wbr>[&#8211;help]</dl>
<h2>Description</h2>
<dd>After Amanda rpms are successfully installed and <code>amserverconfig</code> is run, <code>amaddclient</code> will add client to the Amanda configuration. <code>amaddclient</code> create or update Amanda <code><a href="/docs/linux/man/5-disklist/">disklist</a></code>(5) file and create or update /var/lib/amanda/.amandahosts file on the server. </p>
<p> If &#8211;no-client-update is not specified, <code>amaddclient</code> will attempt to update or create /var/lib/amanda/.amandahost, amanda-client.conf and gnutar-lists on the client. (See <a href="/docs/linux/man/1-ssh-keygen/">ssh-keygen</a>(1) and <a href="/docs/linux/man/1-ssh-add/">ssh-add</a>(1) for detail.) </p>
<p> <code>amaddclient</code> must be run by user amandabackup. </p>
<p> &#8211;config, &#8211;client and &#8211;diskdev must be specified.</p>
<h2>Options</h2>
<dl>
<dd>Options may be abbreviated, as long as the abbreviation is not ambiguous. Option argument can either separated by &#8216;=&#8217; or a space. Example: &#8211;conf=v253, &#8211;client client8.zmanda.com</dl>
<p> <code>&#8211;config config</code></p>
<dl>
<dd>Amanda configuration which this program will add the client to.</dl>
<p> <code>&#8211;client client</code></p>
<dl>
<dd>The name of the client machine to add. FQDN name recommended.</dl>
<p> <code>&#8211;diskdev diskdev</code></p>
<dl>
<dd>Directory for this Amanda configuration to backup.</dl>
<p> <code>&#8211;m</code></p>
<dl>
<dd>Modify existing entry in the <code><a href="/docs/linux/man/5-disklist/">disklist</a></code>(5) file. </p>
<p> Note: if <code><a href="/docs/linux/man/5-disklist/">disklist</a></code>(5) file has been modified manually, this option might not work.</dl>
<p> <code>&#8211;dumptype dumptype</code></p>
<dl>
<dd>dumptype to use. Dumptype must be defined in /etc/amanda/template.d/dumptypes or /etc/amanda/$config/amanda.conf file. Default: [user-tar]</dl>
<p> <code>&#8211;user string</code></p>
<dl>
<dd>name of user using <code>amrecover</code> on the client, default is root.</dl>
<p> <code>&#8211;auth string</code></p>
<dl>
<dd>authentication method to use when running <code>amrecover</code> from the client , default is bsdtcp.</dl>
<p> <code>&#8211;gnutar_list_dir string</code></p>
<dl>
<dd>directory where gnutar keep its state file on the client. Absolute path required. Default is /var/lib/amanda/gnutar-lists. If &#8211;no-client-update is not set, this program will attempt to create the directory on the client.</dl>
<p> <code>&#8211;amandates string</code></p>
<dl>
<dd>file where amanda keep the date of each dumplevel on the client, default is /etc/amandates.</dl>
<p> <code>&#8211;batch</code></p>
<dl>
<dd>Turn on batch mode when copying files to the client, default is off</dl>
<p> <code>&#8211;no-client-update</code></p>
<dl>
<dd>If this option is set, <code>amaddclient</code> will not attempt to update/create .amandahosts, amanda-client.conf and gnutar-lists file on the client.</dl>
<p> <code>&#8211;help</code></p>
<dl>
<dd>Display usage.</dl>
<dl>
<dd>&nbsp;<wbr> If any of the following four options are used, <code>amaddclient</code> will extend the dumptype definition to an in-line definition in the <code><a href="/docs/linux/man/5-disklist/">disklist</a></code>(5) file.</dl>
<p> <code>&#8211;includefile string</code></p>
<dl>
<dd>string is a glob expression</dl>
<p> <code>&#8211;includelist string</code></p>
<dl>
<dd>string is a file name on the client containing glob expressions. Specify either &#8211;includefile or &#8211;includelist.</dl>
<p> <code>&#8211;excludefile string</code></p>
<dl>
<dd>string is a glob expression</dl>
<p> <code>&#8211;excludelist string</code></p>
<dl>
<dd>string is a file name on the client containing glob expressions. Specify either &#8211;excludefile or &#8211;excludelist.</dl>
<h2>Files</h2>
<p><code>/var/lib/amanda/template.d</code></p>
<dl>
<dd>Amanda configuration template files install location</dl>
<p> <code>/var/lib/amanda</code></p>
<dl>
<dd>amandabackup home directory</dl>
<p> <code>/var/lib/amanda/.amandahosts</code></p>
<dl>
<dd>Amanda authentication file.</dl>
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
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5), <code><a href="/docs/linux/man/8-amserverconfig/">amserverconfig</a></code>(8), <code><a href="/docs/linux/man/1-ssh-keygen/">ssh-keygen</a></code>(1), <code><a href="/docs/linux/man/1-ssh-add/">ssh-add</a></code>(1), <code><a href="/docs/linux/man/1-scp/">scp</a></code>(1) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Author</h2>
<p><code>Kevin Till</code> &lt;kevin.till [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>
