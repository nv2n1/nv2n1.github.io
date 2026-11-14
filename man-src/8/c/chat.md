---
title: "chat(8)"
name: "chat"
section: "8"
letter: "c"
url: "/docs/linux/man/8-chat/"
description: "chat – Automated conversational script with a modem"
---

<p>chat &#8211; Automated conversational script with a modem</p>
<h2>Synopsis</h2>
<p><code>chat</code> [ <i>options</i> ] <i>script</i></p>
<h2>Description</h2>
<p>The <i>chat</i> program defines a conversational exchange between the computer and the modem. Its primary purpose is to establish the connection between the Point-to-Point Protocol Daemon (<i>pppd</i>) and the remote&#8217;s <i>pppd</i> process.</p>
<h2>Options</h2>
<dl>
<dt><code>-f </code><i>&lt;chat file&gt;</i></p>
<dd>Read the chat script from the chat <i>file</i>. The use of this option is mutually exclusive with the chat script parameters. The user must have read access to the file. Multiple lines are permitted in the file. Space or horizontal tab characters should be used to separate the strings.</p>
<dt><code>-t </code><i>&lt;timeout&gt;</i></p>
<dd>Set the timeout for the expected string to be received. If the string is not received within the time limit then the reply string is not sent. An alternate reply may be sent or the script will fail if there is no alternate reply string. A failed script will cause the <i>chat</i> program to terminate with a non-zero error code. You can also use the TIMEOUT string in order to specify the timeout.</p>
<dt><code>-r </code><i>&lt;report file&gt;</i></p>
<dd>Set the file for output of the report strings. If you use the keyword <i>REPORT</i>, the resulting strings are written to this file. If this option is not used and you still use <i>REPORT</i> keywords, the <i>stderr</i> file is used for the report strings.</p>
<dt><code>-e</code></p>
<dd>Start with the echo option turned on. Echoing may also be turned on or off at specific points in the chat script by using the <i>ECHO</i> keyword. When echoing is enabled, all output from the modem is echoed to <i>stderr</i>.</p>
<dt><code>-E</code></p>
<dd>Enables environment variable substitution within chat scripts using the standard <i>$xxx</i> syntax.</p>
<dt><code>-v</code></p>
<dd>Request that the <i>chat</i> script be executed in a verbose mode. The <i>chat</i> program will then log the execution state of the chat script as well as all text received from the modem and the output strings sent to the modem. The default is to log through the SYSLOG; the logging method may be altered with the -S and -s flags.</p>
<dt><code>-V</code></p>
<dd>Request that the <i>chat</i> script be executed in a stderr verbose mode. The <i>chat</i> program will then log all text received from the modem and the output strings sent to the modem to the stderr device. This device is usually the local console at the station running the chat or pppd program.</p>
<dt><code>-s</code></p>
<dd>Use stderr. All log messages from &#8216;-v&#8217; and all error messages will be sent to stderr.</p>
<dt><code>-S</code></p>
<dd>Do not use the SYSLOG. By default, error messages are sent to the SYSLOG. The use of -S will prevent both log messages from &#8216;-v&#8217; and error messages from being sent to the SYSLOG.</p>
<dt><code>-T </code><i>&lt;phone number&gt;</i></p>
<dd>Pass in an arbitrary string, usually a phone number, that will be substituted for the \T substitution metacharacter in a send string.</p>
<dt><code>-U </code><i>&lt;phone number 2&gt;</i></p>
<dd>Pass in a second string, usually a phone number, that will be substituted for the 
