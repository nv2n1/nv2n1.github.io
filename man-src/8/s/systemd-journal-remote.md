---
title: "systemd-journal-remote(8)"
name: "systemd-journal-remote"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-journal-remote/"
description: "systemd-journal-remote – Receive journal messages over the network"
---

<p>systemd-journal-remote &#8211; Receive journal messages over the network</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>systemd-journal-remote</code> [OPTIONS&#8230;] [-o/&#8211;output=<i>DIR</i>|<i>FILE</i>] [SOURCES&#8230;]</dl>
<h2>Description</h2>
<dd>systemd-journal-remote is a command to receive serialized journal events and store them to the journal. Input streams are in the m[blue]<code>Journal Export Format</code>m[]<font SIZE="-2">[1]</font>, i.e. like the output from <code>journalctl &#8211;output=export</code>. For transport over the network, this serialized stream is usually carried over an HTTPS connection.</p>
<h2>Sources</h2>
<p>Sources can be either &quot;active&quot; (<code>systemd-journal-remote</code> requests and pulls the data), or &quot;passive&quot; (<code>systemd-journal-remote</code> waits for a connection and then receives events pushed by the other side). </p>
<p> <code>systemd-journal-remote</code> can read more than one event stream at a time. They will be interleaved in the output file. In case of &quot;active&quot; connections, each &quot;source&quot; is one stream, and in case of &quot;passive&quot; connections, each connection can result in a separate stream. Sockets can be configured in &quot;accept&quot; mode (i.e. only one connection), or &quot;listen&quot; mode (i.e. multiple connections, each resulting in a stream). </p>
<p> When there are no more connections, and no more can be created (there are no listening sockets), then <code>systemd-journal-remote</code> will exit. </p>
<p> Active sources can be specified in the following ways: </p>
<dl>
<dd>When <code>&#8211;</code> is given as a positional argument, events will be read from standard input. Other positional arguments will be treated as filenames to open and read from.</dl>
<p> <code>&#8211;url=</code><i>ADDRESS</i></p>
<dl>
<dd>With the <code>&#8211;url=</code><i>ADDRESS</i> option, events will be retrieved using HTTP from <i>ADDRESS</i>. This URL should refer to the root of a remote <code><a href="/docs/linux/man/8-systemd-journal-gatewayd/">systemd-journal-gatewayd</a></code>(8) instance (e.g. m[blue]<code><a rel="nofollow" href="http://some.host:19531/">http://some.host:19531/</a></code>m[] or m[blue]<code><a rel="nofollow" href="https://some.host:19531/">https://some.host:19531/</a></code>m[]).</dl>
<p> Passive sources can be specified in the following ways: </p>
<p> <code>&#8211;listen-raw=</code><i>ADDRESS</i></p>
<dl>
<dd><i>ADDRESS</i> must be an address suitable for <code>ListenStream=</code> (cf. <code><a href="/docs/linux/man/5-systemd-socket/">systemd.socket</a></code>(5)). <code>systemd-journal-remote</code> will listen on this socket for connections. Each connection is expected to be a stream of journal events.</dl>
<p> <code>&#8211;listen-http=</code><i>ADDRESS</i>, <code>&#8211;listen-https=</code><i>ADDRESS</i></p>
<dl>
<dd><i>ADDRESS</i> must be either a negative integer, in which case it will be interpreted as the (negated) file descriptor number, or an address suitable for <code>ListenStream=</code> (c.f. <code><a href="/docs/linux/man/5-systemd-socket/">systemd.socket</a></code>(5)). In the first case, matching file descriptor must be inherited through <i>$LISTEN_FDS</i>/<i>$LISTEN_PID</i>. In the second case, an HTTP or HTTPS server will be spawned on this port, respectively for <code>&#8211;listen-http</code> and <code>&#8211;listen-https</code>. Currenntly, only POST requests to /upload with &quot;Content-Type: application/vnd.fdo.journal&quot; are supported.</dl>
<p> <i>$LISTEN_FDS</i></p>
<dl>
<dd><code>systemd-journal-remote</code> supports the <i>$LISTEN_FDS</i>/<i>$LISTEN_PID</i> protocol. Open sockets inherited through socket activation behave like those opened with <code>&#8211;listen-raw=</code> described above, unless they are specified as an argument in <code>&#8211;listen-http=-</code><i>n</i> or <code>&#8211;listen-https=-</code><i>n</i> above. In the latter case, an HTTP or HTTPS server will be spawned using this descriptor and connections must be made over the HTTP protocol.</dl>
<h2>Sinks</h2>
<p>The location of the output journal can be specified with <code>-o</code> or <code>&#8211;output=</code>. For &quot;active&quot; sources, this option is required. </p>
<p> <code>&#8211;output=</code><i>FILE</i></p>
<dl>
<dd>Will write to this journal file. The filename must end with .journal. The file will be created if it does not exist. If necessary (journal file full, or corrupted), the file will be renamed following normal journald rules and a new journal file will be created in its stead.</dl>
<p> <code>&#8211;output=</code><i>DIR</i></p>
<dl>
<dd>Will create journal files underneath directory <i>DIR</i>. The directory must exist. If necessary (journal files over size, or corrupted), journal files will be rotated following normal journald rules. Names of files underneath <i>DIR</i> will be generated using the rules described below.</dl>
<p> If <code>&#8211;output=</code> is not used, the output directory /var/log/journal/remote/ will be used. In case the output file is not specified, journal files will be created underneath the selected directory. Files will be called remote-<i>hostname</i>.journal, where the <i>hostname</i> part is the escaped hostname of the source endpoint of the connection, or the numerical address if the hostname cannot be determined. </p>
<p> In case of &quot;active&quot; sources, the output file name must always be given explicitly.</p>
<h2>Options</h2>
<p>The following options are understood: </p>
<p> <code>&#8211;split-mode</code></p>
<dl>
<dd>One of <code>none</code> or <code>host</code>. For the first, only one output journal file is used. For the latter, a separate output file is used, based on the hostname of the other endpoint of a connection. </p>
<p> In case of &quot;active&quot; sources, the output file name must always be given explicitly and only <code>none</code> is allowed.</dl>
<p> <code>&#8211;compress</code>, <code>&#8211;no-compress</code></p>
<dl>
<dd>Compress or not, respectively, the data in the journal using XZ.</dl>
<p> <code>&#8211;seal</code>, <code>&#8211;no-seal</code></p>
<dl>
<dd>Periodically sign or not, respectively, the data in the journal using Forward Secure Sealing.</dl>
<p> <code>&#8211;getter=</code><i>PROG &#8211;option1 &#8211;option2</i></p>
<dl>
<dd>Program to invoke to retrieve data. The journal event stream must be generated on standard output. </p>
<p> Examples: </p>
<dl>
<dd>
<pre>--getter='curl &quot;-HAccept: application/vnd.fdo.journal&quot; <a rel="nofollow" href="https://some.host:19531/'">https://some.host:19531/'</a></pre>
</dl>
<dl>
<dd>
<pre>--getter='wget --header=&quot;Accept: application/vnd.fdo.journal&quot; -O- <a rel="nofollow" href="https://some.host:19531/'">https://some.host:19531/'</a></pre>
</dl>
</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Print a short help text and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dd>Print a short version string and exit.</dl>
<h2>Examples</h2>
<p>Copy local journal events to a different journal directory:</p>
<dl>
<dd>
<pre>journalctl -o export | systemd-journal-remote -o /tmp/dir -</pre>
</dl>
<p> Retrieve events from a remote <code><a href="/docs/linux/man/8-systemd-journal-gatewayd/">systemd-journal-gatewayd</a></code>(8) instance and store them in /var/log/journal/some.host/remote-some~host.journal:</p>
<dl>
<dd>
<pre>systemd-journal-remote --url <a rel="nofollow" href="http://some.host:19531/">http://some.host:19531/</a></pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-systemd-journal-upload/">systemd-journal-upload</a></code>(8), <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1), <code><a href="/docs/linux/man/8-systemd-journald-service/">systemd-journald.service</a></code>(8), <code><a href="/docs/linux/man/8-systemd-journal-gatewayd-service/">systemd-journal-gatewayd.service</a></code>(8)<code><a href="/docs/linux/man/5-journal-remote-conf/">journal-remote.conf</a></code>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>Journal Export Format</p>
<dl>
<dd><a rel="nofollow" href="http://www.freedesktop.org/wiki/Software/systemd/export">http://www.freedesktop.org/wiki/Software/systemd/export</a></dl>
<dt> 2.</p>
<dd><a rel="nofollow" href="http://some.host:19531/">http://some.host:19531/</a></p>
<dt> 3.</p>
<dd><a rel="nofollow" href="https://some.host:19531/">https://some.host:19531/</a> </p>
