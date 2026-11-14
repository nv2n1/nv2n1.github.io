---
title: "ktutil(1)"
name: "ktutil"
section: "1"
letter: "k"
url: "/docs/linux/man/1-ktutil/"
description: "ktutil – Kerberos keytab file maintenance utility"
---

<h2>NAME</h2>
<p> ktutil &#8211; Kerberos keytab file maintenance utility</p>
<h2>SYNOPSIS</h2>
<p> <code>ktutil</code></p>
<h2>DESCRIPTION</h2>
<p> The ktutil command invokes a command interface from which an administrator can read, write, or edit entries in a keytab or Kerberos V4 srvtab file.</p>
<h2>COMMANDS</h2>
<h3>list</h3>
<p> <code>list</code> </p>
<p> Displays the current keylist. </p>
<p> Alias: <code>l</code></p>
<h3>read_kt</h3>
<p> <code>read_kt</code> <i>keytab</i> </p>
<p> Read the Kerberos V5 keytab file <i>keytab</i> into the current keylist. </p>
<p> Alias: <code>rkt</code></p>
<h3>read_st</h3>
<p> <code>read_st</code> <i>srvtab</i> </p>
<p> Read the Kerberos V4 srvtab file <i>srvtab</i> into the current keylist. </p>
<p> Alias: <code>rst</code></p>
<h3>write_kt</h3>
<p> <code>write_kt</code> <i>keytab</i> </p>
<p> Write the current keylist into the Kerberos V5 keytab file <i>keytab</i>. </p>
<p> Alias: <code>wkt</code></p>
<h3>write_st</h3>
<p> <code>write_st</code> <i>srvtab</i> </p>
<p> Write the current keylist into the Kerberos V4 srvtab file <i>srvtab</i>. </p>
<p> Alias: <code>wst</code></p>
<h3>clear_list</h3>
<p> <code>clear_list</code> </p>
<p> Clear the current keylist. </p>
<p> Alias: <code>clear</code></p>
<h3>delete_entry</h3>
<p> <code>delete_entry</code> <i>slot</i> </p>
<p> Delete the entry in slot number <i>slot</i> from the current keylist. </p>
<p> Alias: <code>delent</code></p>
<h3>add_entry</h3>
<p> <code>add_entry</code> {<code>-key</code>|<code>-password</code>} <code>-p</code> <i>principal</i> <code>-k</code> <i>kvno</i> <code>-e</code> <i>enctype</i> </p>
<p> Add <i>principal</i> to keylist using key or password. </p>
<p> Alias: <code>addent</code></p>
<h3>list_requests</h3>
<p> <code>list_requests</code> </p>
<p> Displays a listing of available commands. </p>
<p> Aliases: <code>lr</code>, <code>?</code></p>
<h3>quit</h3>
<p> <code>quit</code> </p>
<p> Quits ktutil. </p>
<p> Aliases: <code>exit</code>, <code>q</code></p>
<h2>EXAMPLE</h2>
<pre><code>
ktutil:  add_entry -password -p alice [at] BLEEP.COM -k 1 -e
    aes128-cts-hmac-sha1-96
Password for alice [at] BLEEP.COM:
ktutil:  add_entry -password -p alice [at] BLEEP.COM -k 1 -e
    aes256-cts-hmac-sha1-96
Password for alice [at] BLEEP.COM:
ktutil:  write_kt keytab
ktutil:
</code></pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-kadmin/">kadmin</a>(1)</i>, <i><a href="/docs/linux/man/8-kdb5_util/">kdb5_util</a>(8)</i></p>
<h2>AUTHOR</h2>
<p> MIT</p>
<h2>COPYRIGHT</h2>
<p> 1985-2017, MIT </p>
<h2>Index</h2>
