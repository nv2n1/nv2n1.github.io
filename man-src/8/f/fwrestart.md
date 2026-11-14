---
title: "fwrestart(8)"
name: "fwrestart"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fwrestart/"
description: "fwrestart – Re-initialize the firewall rules, disabling firewall shell session is locked out."
---

<p>fwrestart &#8211; Re-initialize the firewall rules, disabling firewall shell session is locked out.</p>
<h2>Synopsis</h2>
<p><code>fwrestart</code> </p>
<h2>Description</h2>
<p>fwrestart uses terminal auto-response codes to safely re-start firewall rules over a remote shell session. It sends a request to your terminal (xterm, for example), which responds back automatically. When that response is received, ensuring that fwrestart can communicate with the terminal, fwrestart then issues a command to restart the firewall. It then tries another request to the terminal, and if that is not received within 5 seconds, a command is run to clear the firewall and an appropriate error is generated. The goal is to be able to automatically detect when changes to the firewall block the administrative shell session, and to take corrective action. By default the commands used to restart and clear the firewall are &quot;/sbin/service iptables start&quot; and &quot;/sbin/service iptables stop&quot;. These commands can be changed by modifying the values of &quot;fwRestartCmd&quot; and &quot;fwClearCmd&quot; at the beginning of the fwrestart script. </p>
<h2>Examples</h2>
<p>Re-load firewall rules, checking to ensure that the new rules don&#8217;t block the current session:<br />
fwrestart </p>
<h2>Environment</h2>
<p>A KRUD installation (<a rel="nofollow" href="http://www.tummy.com/krud">http://www.tummy.com/krud</a>).</p>
<h2>Author</h2>
<p>Sean Reifschneider (jafo [at] tummy.com) of tummy.com, ltd. </p>
<p> krudfind is a KRUD Linux product. </p>
<p> <a rel="nofollow" href="http://www.tummy.com/krud/">http://www.tummy.com/krud/</a></p>
