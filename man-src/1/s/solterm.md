---

title: "solterm(1)"
name: "solterm"
section: "1"
letter: "s"
url: "/docs/linux/man/1-solterm/"
description: "solterm – An IPMI Serial over LAN program"
---

<p> solterm &#8211; An IPMI Serial over LAN program</p>
<h2>SYNOPSIS</h2>
<p> <code>solterm</code> </p>
<p> <code>&lt;connection parms&gt;</code> [<code>-e</code> <i>escape_char</i>] [<code>-notencrypted</code>] [<code>-notauthenticated</code>] [<code>-bitrate</code> <i>(9600|19200|38400|57600|115200)</i>] [<code>-alerts</code> <i>(succeed|defer|fail)</i>] [<code>-holdoff</code>] [<code>-ack-retries</code> <i>n</i>] [<code>-ack-timeout</code> <i>microseconds]</i> [<code>-v</code>] [<code>-q</code>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>solterm</code> program allows a user to make a remote serial connection over IPMI. The requires that the remote system support IPMI 2.0 Serial Over LAN. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&lt;connection parms&gt;</code></dt>
<dd> The parameters for the connection depend on the connection type. These are all described in openipmi_conparms (7) </dd>
<dt><code>-e&nbsp;<wbr></code><i>escape_char</i></dt>
<dd> The character to use to escape, or exit, the program. Entering this character right after a newline is entered causes the program to go into command mode. A single character after this performs a command. The default escape character is &quot;~&quot; as shown below. Supported commands are:</dd>
<dl>
<dl>
<dt>~.</dt>
<dd> Terminate the program</dd>
<dt>~B</dt>
<dd> Send a serial BREAK over the connection</dd>
<dt>~F</dt>
<dd> Flush all buffers</dd>
<dt>~R</dt>
<dd> Assert the Ring Indicator (RI) line</dd>
<dt>~r</dt>
<dd> Deassert the Ring Indicator (RI) line</dd>
<dt>~D</dt>
<dd> Assert DCD and DSR lines</dd>
<dt>~d</dt>
<dd> Deassert DCD and DSR lines</dd>
<dt>~C</dt>
<dd> Pause the output using CTS</dd>
<dt>~c</dt>
<dd> Put CTS under BMC control</dd>
<dt>~?</dt>
<dd> Help on escape commands</dd>
<dt>~~</dt>
<dd> Enter the escape character twice to send it.</dd></dl>
</dl>
<dt><code>-notencrypted</code></dt>
<dd> Do not encrypt the SOL data going over the connection. </dd>
<dt><code>-notauthenticated</code></dt>
<dd> Do not do integrity checks on the SOL data going over the connection. </dd>
<dt><code>-bitrate</code></dt>
<dd> Set the bitrate to the given value. The default is whatever the BMC has set it to. </dd>
<dt><code>-alerts</code></dt>
<dd> This specifies what to do if a alert that requires a callout occurs on the line.</dd>
<dl>
<dl>
<dt>succeed</dt>
<dd> specifies that serial/modem alerts are to succeed while SoL is active.</dd>
<dt>deferred</dt>
<dd> specifies that serial/modem alerts are to be deferred for the duration of the SoL session.</dd>
<dt>fail</dt>
<dd> specifies that serial/modem alerts automatically fail during the SoL session. This is the default.</dd></dl>
</dl>
<dt><code>-holdoff</code></dt>
<dd> Specifies that CTS, DTR, and DSR are to be deasserted at the start of the SoL session so that the configuration may be modified before the handshake is released. </dd>
<dt><code>-v</code></dt>
<dd> Be more verbose. Maybe specified multiple time for more output. </dd>
<dt><code>-q</code></dt>
<dd> Be less verbose. Maybe specified multiple time for less output. </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-openipmi_conparms/">openipmi_conparms</a></code>(7) </p>
<h2>KNOWN PROBLEMS</h2>
<p> None </p>
<h2>AUTHOR</h2>
<p> Darius Davis &lt;dariusd [at] users.sourceforge.net&gt; </p>
