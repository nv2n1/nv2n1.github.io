---
title: "solterm(1)"
name: "solterm"
section: "1"
letter: "s"
url: "/docs/linux/man/1-solterm/"
description: "solterm – An IPMI Serial over LAN program"
---

<h2 class="name">NAME</h2>
<p> solterm &#8211; An IPMI Serial over LAN program</p>
<h2>SYNOPSIS</h2>
<p> <code>solterm</code> </p>
<p> <code>&lt;connection parms&gt;</code> [<code>-e</code> <i>escape_char</i>] [<code>-notencrypted</code>] [<code>-notauthenticated</code>] [<code>-bitrate</code> <i>(9600|19200|38400|57600|115200)</i>] [<code>-alerts</code> <i>(succeed|defer|fail)</i>] [<code>-holdoff</code>] [<code>-ack-retries</code> <i>n</i>] [<code>-ack-timeout</code> <i>microseconds]</i> [<code>-v</code>] [<code>-q</code>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>solterm</code> program allows a user to make a remote serial connection over IPMI. The requires that the remote system support IPMI 2.0 Serial Over LAN. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&lt;connection parms&gt;</code></p>
<dd> The parameters for the connection depend on the connection type. These are all described in openipmi_conparms (7) </p>
<dt><code>-e&nbsp;<wbr></code><i>escape_char</i></p>
<dd> The character to use to escape, or exit, the program. Entering this character right after a newline is entered causes the program to go into command mode. A single character after this performs a command. The default escape character is &quot;~&quot; as shown below. Supported commands are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>~.</p>
<dd> Terminate the program</p>
<dt>~B</p>
<dd> Send a serial BREAK over the connection</p>
<dt>~F</p>
<dd> Flush all buffers</p>
<dt>~R</p>
<dd> Assert the Ring Indicator (RI) line</p>
<dt>~r</p>
<dd> Deassert the Ring Indicator (RI) line</p>
<dt>~D</p>
<dd> Assert DCD and DSR lines</p>
<dt>~d</p>
<dd> Deassert DCD and DSR lines</p>
<dt>~C</p>
<dd> Pause the output using CTS</p>
<dt>~c</p>
<dd> Put CTS under BMC control</p>
<dt>~?</p>
<dd> Help on escape commands</p>
<dt>~~</p>
<dd> Enter the escape character twice to send it.</dl>
</dl>
<dt><code>-notencrypted</code></p>
<dd> Do not encrypt the SOL data going over the connection. </p>
<dt><code>-notauthenticated</code></p>
<dd> Do not do integrity checks on the SOL data going over the connection. </p>
<dt><code>-bitrate</code></p>
<dd> Set the bitrate to the given value. The default is whatever the BMC has set it to. </p>
<dt><code>-alerts</code></p>
<dd> This specifies what to do if a alert that requires a callout occurs on the line.</p>
<dl>
<dt>
<dd>
<dl>
<dt>succeed</p>
<dd> specifies that serial/modem alerts are to succeed while SoL is active.</p>
<dt>deferred</p>
<dd> specifies that serial/modem alerts are to be deferred for the duration of the SoL session.</p>
<dt>fail</p>
<dd> specifies that serial/modem alerts automatically fail during the SoL session. This is the default.</dl>
</dl>
<dt><code>-holdoff</code></p>
<dd> Specifies that CTS, DTR, and DSR are to be deasserted at the start of the SoL session so that the configuration may be modified before the handshake is released. </p>
<dt><code>-v</code></p>
<dd> Be more verbose. Maybe specified multiple time for more output. </p>
<dt><code>-q</code></p>
<dd> Be less verbose. Maybe specified multiple time for less output. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-openipmi_conparms/">openipmi_conparms</a></code>(7) </p>
<h2>KNOWN PROBLEMS</h2>
<p> None </p>
<h2>AUTHOR</h2>
<p> Darius Davis &lt;dariusd [at] users.sourceforge.net&gt; </p>
<h2>Index</h2>
