---

title: "aconnect(1)"
name: "aconnect"
section: "1"
letter: "a"
url: "/docs/linux/man/1-aconnect/"
description: "aconnect – ALSA sequencer connection manager"
---

<p> aconnect &#8211; ALSA sequencer connection manager</p>
<h2>SYNOPSIS</h2>
<p> <code>aconnect</code> [-d] [-options] sender receiver<br/>
 <code>aconnect</code> -i|-o [-options]<br/>
 <code>aconnect</code> -x </p>
<h2>DESCRIPTION</h2>
<p> <code>aconnect</code> is a utility to connect and disconnect two existing ports on ALSA sequencer system. The ports with the arbitrary subscription permission, such as created by <code>aseqview(1),</code> can be connected to any (MIDI) device ports using <code>aconnect.</code> For example, to connect from port 64:0 to 65:0, run as follows:</p>
<dl>
<dt>
</dt><dd> % aconnect 64:0 65:0</dd></dl>
<p> The connection is one-way, and the whole data to the sender port (64:0) is redirected to the receiver port (65:0). When another port (e.g. 65:1) is attached to the same sender port, the data is sent to both receiver ports. For disconnection, use <code>-d</code> option. </p>
<pre>
% aconnect -d 64:0 65:0
</pre>
<p> The address can be given using the client&#8217;s name. </p>
<pre>
% aconnect External:0 Emu8000:1
</pre>
<p> Then the port 0 of the client matching with the string &quot;External&quot; is connected to the port 1 of the client matching with the &quot;Emu8000&quot;. </p>
<p> Another function of <code>aconnect</code> is to list the present ports on the given condition. The input ports, which may become <i>sender</i> ports, can be listed with <code>-i</code> option. </p>
<pre><code>
% aconnect - i
                 client 0 : 'System'[type = kernel] 0 'Timer           ' 1 'Announce        ' client 64 : 'External MIDI-0'[type = kernel] 0 'MIDI 0-0        '
</code></pre>
<p> Similarly, to see the output ports, use <code>-o</code> flag. </p>
<p> You can remove all existing exported connections using <code>-x</code> option. This function is useful for terminating the ALSA drivers, because the modules with sequencer connections cannot be unloaded unless their connections are removed. </p>
<h2>OPTIONS</h2>
<h3>CONNECTION MANAGEMENT</h3>
<dl>
<dt><code>-d, &#8211;disconnect</code></dt>
<dd> Disconnect the given subscription.</dd>
<dt><code>-e, &#8211;exclusive</code></dt>
<dd> Connect ports with exclusive mode. Both sender and receiver ports can be no longer connected by any other ports.</dd>
<dt><code>-r, &#8211;real queue</code></dt>
<dd> Convert time-stamps of event packets to the current value of the given <i>real-time</i> queue. This is option is, however, not so useful, since the receiver port must use (not necessarily own) the specified queue.</dd>
<dt><code>-t, &#8211;tick queue</code></dt>
<dd> Like <code>-r</code> option, but time-stamps are converted to the current value of the given <i>tick</i> queue. </dd>
</dl>
<h3>LIST PORTS</h3>
<dl>
<dt><code>-i, &#8211;input</code></dt>
<dd> List existing input (readable) ports. This option is exclusive to <code>-o.</code></dd>
<dt><code>-o, &#8211;output</code></dt>
<dd> List existing output (writable) ports. This option is exclusive to <code>-i.</code></dd>
<dt><code>-l, &#8211;list</code></dt>
<dd> List the current connection status. The connected and connecting ports from/to each port are listed together. The suffix flag <code>[ex]</code> means the connection is exclusive. The suffix flag <code>[real:#]</code> and <code>[tick:#]</code> mean the connection includes real-time and tick conversion on the listed queue, respectively. </dd>
</dl>
<h3>REMOVE ALL CONNECTIONS</h3>
<dl>
<dt><code>-x, &#8211;removeall</code></dt>
<dd> Remove all exported connections. </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-aseqnet/">aseqnet</a>(1), aseqview(1) </p>
<h2>AUTHOR</h2>
<p> Takashi Iwai &lt;tiwai [at] suse.de&gt; </p>
