---

title: "gtkterm(1)"
name: "gtkterm"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gtkterm/"
description: "gtkterm – A simple GTK+ serial port terminal"
---

<p> gtkterm &#8211; A simple GTK+ serial port terminal</p>
<h2>SYNOPSIS</h2>
<p> <code>gtkterm [ options ]</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>gtkterm </code> is a simple GTK+ terminal used to communicate with the serial port. </p>
<h2>OPTIONS</h2>
<p> <code>gtkterm </code> accepts the following options: </p>
<p> <code>-h, &#8211;help </code> Help screen.</p>
<dl>
<dt><code>-c, &#8211;config &lt;configuration&gt;</code></dt>
<dd> Load configuration (default is &quot;default&quot;).</dd>
<dt><code>-p, &#8211;port &lt;device&gt;</code></dt>
<dd> Serial port device (default /dev/ttyS0).</dd>
<dt><code>-s, &#8211;speed &lt;speed&gt;</code></dt>
<dd> Serial port speed (default 9600).</dd>
<dt><code>-b, &#8211;bits &lt;bits&gt; </code></dt>
<dd> Number of bits (default 8).</dd>
<dt><code>-t, &#8211;stopbits &lt;stopbits&gt;</code></dt>
<dd> Number of stopbits (default 1).</dd>
<dt><code>-a, &#8211;parity &lt;odd | even&gt; </code></dt>
<dd> Partity (default none).</dd>
<dt><code>-w, &#8211;flow &lt;Xon | CTS&gt;</code></dt>
<dd> Flow control (default none).</dd>
<dt><code>-d, &#8211;delay &lt;ms&gt;</code></dt>
<dd> End of line delay in ms (default none).</dd>
<dt><code>-r, &#8211;char &lt;char&gt;</code></dt>
<dd> Wait for a special char at end of line (default none).</dd>
<dt><code>-f, &#8211;file &lt;filename&gt;</code></dt>
<dd> Default file to send (default none).</dd>
<dt><code>-e, &#8211;echo</code></dt>
<dd> Set local echo. </dd>
</dl>
<h2>AUTHOR</h2>
<p> <code>gtkterm</code> was written by Julien Schmitt &lt;julien [at] jls-info.com&gt;. </p>
<p> This manual page was written by Sebastien Bacher &lt;seb128 [at] debian.org&gt;, for the Debian GNU/Linux system (but may be used by others). </p>
