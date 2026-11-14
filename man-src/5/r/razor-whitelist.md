---
title: "razor-whitelist(5)"
name: "razor-whitelist"
section: "5"
letter: "r"
url: "/docs/linux/man/5-razor-whitelist/"
---

&quot;razor-whitelist&quot; - Format for Vipul's Razor Whitelist

<h2>Description</h2>

The razor whitelist is a list of email addresses and body signatures. Emails that match the whitelist are not processed by any of the Razor Agents. That is, They are not checked, reported, or revoked. In the case of <i><a HREF="/docs/linux/man/1-razor-check/">razor-check</a></i>(1), they are instantly marked as non-spam.

<h2>Location</h2>

The razor whitelist is usually <tt>&quot;&lt;razorhome&gt;/razor-whitelist&quot;</tt>. The <tt>&quot;whitelist&quot;</tt> parameter in <i><a HREF="/docs/linux/man/5-razor-agent-conf/">razor-agent.conf</a></i>(5) should point to this file. If the <tt>&quot;whitelist&quot;</tt> parameter in <i><a HREF="/docs/linux/man/5-razor-agent-conf/">razor-agent.conf</a></i>(5) is missing, <tt>&quot;whitelist&quot;</tt> is not used.

<h2>Format</h2>

Each whitelist rule is placed on a line of its own. Lines that begin in a `#' character are considered to be comments and are ignored by the parser. A rule contains the name of a header and the string to match against the header, separated by whitespace. Here are some examples: 

 <pre> to bugtraq [at] securityfocus.com
 cc a.list [at] somewhere.net</pre>These rules imply that when a mail contains <tt>&quot;bugtraq [at] securityfocus.com&quot;</tt> in its `to' and `cc' headers, it should be whitelisted. It's worth noting that a match occurs if the address string matches any part of the address. 

 <pre> from @mydomain.com</pre>A special rule called `sha1' can be used for whitelisting signatures. For example: 

 <pre> sha1 75f8bcc2357366bbfa9c6ab0b6e5648ed0cf7083</pre>whitelists a message with the body of `test'.

<h2>Authors</h2>

Vipul Ved Prakash &lt;mail [at] vipul.net&gt;, and Chad Norwood &lt;chad [at] samo.org&gt;

<h2>See Also</h2>

<i><a HREF="/docs/linux/man/1-razor-agents/">razor-agents</a></i>(1), <i><a HREF="/docs/linux/man/5-razor-agent-conf/">razor-agent.conf</a></i>(5), <i><a HREF="/docs/linux/man/1-razor-check/">razor-check</a></i>(1), <i><a HREF="/docs/linux/man/1-razor-admin/">razor-admin</a></i>(1), <i><a HREF="/docs/linux/man/1-razor-report/">razor-report</a></i>(1), <i><a HREF="/docs/linux/man/1-razor-revoke/">razor-revoke</a></i>(1)

<h2>License</h2>

This is free software, distributed under the Artistic License 2.0.
