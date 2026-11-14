---
title: "systemd-journal-gatewayd-socket(8)"
name: "systemd-journal-gatewayd-socket"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-journal-gatewayd-socket/"
description: "systemd-journal-gatewayd.service, systemd-journal-gatewayd.socket, systemd-journal-gatewayd – HTTP server for journal events"
---

<p>systemd-journal-gatewayd.service, systemd-journal-gatewayd.socket, systemd-journal-gatewayd &#8211; HTTP server for journal events</p>
<h2>Synopsis</h2>
<p>systemd-journal-gatewayd.service </p>
<p> systemd-journal-gatewayd.socket</p>
<dl>
<dt> <code>/usr/lib/systemd/systemd-journal-gatewayd</code> [OPTIONS&#8230;]</dl>
<h2>Description</h2>
<p><code>systemd-journal-gatewayd</code></p>
<dd>serves journal events over the network. Clients must connect using HTTP. The server listens on port 19531 by default. If <code>&#8211;cert=</code> is specified, the server expects HTTPS connections. </p>
<p> The program is started by <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) and expects to receive a single socket. Use <code>systemctl start systemd-journal-gatewayd.socket</code> to start the service, and <code>systemctl enable systemd-journal-gatewayd.socket</code> to have it started on boot.</p>
<h2>Options</h2>
<p>The following options are understood: </p>
<p> <code>&#8211;cert=</code></p>
<dl>
<dd>Specify the path to a file containing a server certificate in PEM format. This option switches <code>systemd-journal-gatewayd</code> into HTTPS mode and must be used together with <code>&#8211;key=</code>.</dl>
<p> <code>&#8211;key=</code></p>
<dl>
<dd>Specify the path to a file containing a server key in PEM format corresponding to the certificate specified with <code>&#8211;cert=</code>.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Print a short help text and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dd>Print a short version string and exit.</dl>
<h2>Supported Urls</h2>
<p>The following URLs are recognized: </p>
<p> /browse</p>
<dl>
<dd>Interactive browsing.</dl>
<p> /entries[?option1&amp;option2=value&#8230;]</p>
<dl>
<dd>Retrieval of events in various formats. </p>
<p> The <code>Accept:</code> part of the HTTP header determines the format. Supported values are described below. </p>
<p> The <code>Range:</code> part of the HTTP header determines the range of events returned. Supported values are described below. </p>
<p> GET parameters can be used to modify what events are returned. Supported parameters are described below.</dl>
<p> /machine</p>
<dl>
<dd>Return a JSON structure describing the machine. </p>
<p> Example: </p>
<dl>
<dd>
<pre>{ &quot;machine_id&quot; : &quot;8cf7ed9d451ea194b77a9f118f3dc446&quot;,
 &quot;boot_id&quot; : &quot;3d3c9efaf556496a9b04259ee35df7f7&quot;,
 &quot;hostname&quot; : &quot;fedora&quot;,
 &quot;os_pretty_name&quot; : &quot;Fedora 19 (Rawhide)&quot;,
 &quot;virtualization&quot; : &quot;kvm&quot;,
 ...}</pre>
</dl>
</dl>
<p> /fields/<i>FIELD_NAME</i></p>
<dl>
<dd>Return a list of values of this field present in the logs.</dl>
<h2>Accept Header</h2>
<p><code>Accept: </code><i>format</i> </p>
<p> Recognized formats: </p>
<p> <code>text/plain</code></p>
<dl>
<dd>The default. Plaintext syslog-like output, one line per journal entry (like <code>journalctl &#8211;output short</code>).</dl>
<p> <code>application/json</code></p>
<dl>
<dd>Entries are formatted as JSON data structures, one per line (like <code>journalctl &#8211;output json</code>). See m[blue]<code>Journal JSON Format</code>m[]<font SIZE="-2">[1]</font> for more information.</dl>
<p> <code>application/event-stream</code></p>
<dl>
<dd>Entries are formatted as JSON data structures, wrapped in a format suitable for m[blue]<code>Server-Sent Events</code>m[]<font SIZE="-2">[2]</font> (like <code>journalctl &#8211;output json-sse</code>).</dl>
<p> <code>application/vnd.fdo.journal</code></p>
<dl>
<dd>Entries are serialized into a binary (but mostly text-based) stream suitable for backups and network transfer (like <code>journalctl &#8211;output export</code>). See m[blue]<code>Journal Export Format</code>m[]<font SIZE="-2">[3]</font> for more information.</dl>
<h2>Range Header</h2>
<p><code>Range: entries=</code><i>cursor</i><code>[[:</code><i>num_skip</i><code>]:</code><i>num_entries</i><code>]</code> </p>
<p> where <code>cursor</code> is a cursor string, <code>num_skip</code> is an integer, <code>num_entries</code> is an unsigned integer. </p>
<p> Range defaults to all available events.</p>
<h2>Url Get Parameters</h2>
<p>Following parameters can be used as part of the URL: </p>
<p> follow</p>
<dl>
<dd>wait for new events (like <code>journalctl &#8211;follow</code>, except that the number of events returned is not limited).</dl>
<p> discrete</p>
<dl>
<dd>Test that the specified cursor refers to an entry in the journal. Returns just this entry.</dl>
<p> boot</p>
<dl>
<dd>Limit events to the current boot of the system (like <code>journalctl &#8211;this&#8211;boot</code>).</dl>
<p> <i>KEY</i>=<i>match</i></p>
<dl>
<dd>Match journal fields. See <code><a href="/docs/linux/man/7-systemd-journal-fields/">systemd.journal-fields</a></code>(7).</dl>
<h2>Examples</h2>
<p>Retrieve events from this boot from local journal in m[blue]<code>Journal Export Format</code>m[]<font SIZE="-2">[3]</font>: </p>
<dl>
<dd>
<pre>curl --silent -H'Accept: application/vnd.fdo.journal' \
 '<a rel="nofollow" href="http://localhost:19531/entries?boot'">http://localhost:19531/entries?boot'</a></pre>
</dl>
<p> Listen for core dumps: </p>
<dl>
<dd>
<pre>curl '<a rel="nofollow" href="http://localhost:19531/entries?follow">http://localhost:19531/entries?follow</a>&amp;MESSAGE_ID=fc2e22bc6ee647b6b90729ab34a250b1'</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1), <code><a href="/docs/linux/man/8-systemd-journald-service/">systemd-journald.service</a></code>(8), <code><a href="/docs/linux/man/7-systemd-journal-fields/">systemd.journal-fields</a></code>(7),</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>Journal JSON Format</p>
<dl>
<dd><a rel="nofollow" href="http://www.freedesktop.org/wiki/Software/systemd/json">http://www.freedesktop.org/wiki/Software/systemd/json</a></dl>
<dt> 2.</p>
<dd>Server-Sent Events</p>
<dl>
<dd><a rel="nofollow" href="https://developer.mozilla.org/en-US/docs/Server-sent_events/Using_server-sent_events">https://developer.mozilla.org/en-US/docs/Server-sent_events/Using_server-sent_events</a></dl>
<dt> 3.</p>
<dd>Journal Export Format</p>
<dl>
<dd><a rel="nofollow" href="http://www.freedesktop.org/wiki/Software/systemd/export">http://www.freedesktop.org/wiki/Software/systemd/export</a></dl>
