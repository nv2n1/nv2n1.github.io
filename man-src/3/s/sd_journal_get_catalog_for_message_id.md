---
title: "sd_journal_get_catalog_for_message_id(3)"
name: "sd_journal_get_catalog_for_message_id"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sd_journal_get_catalog_for_message_id/"
description: "sd_journal_get_catalog, sd_journal_get_catalog_for_message_id – Retrieve message catalog entry"
---

<p>sd_journal_get_catalog, sd_journal_get_catalog_for_message_id &#8211; Retrieve message catalog entry</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;systemd/sd-journal.h&gt;

int sd_journal_get_catalog(sd_journal *j, char **ret);

int sd_journal_get_catalog_for_message_id(sd_id128_t id, char **ret);</code></pre>
<h2>Description</h2>
<p><code>sd_journal_get_catalog()</code></p>
<dd>retrieves a message catalog entry for the current journal entry. This will look up an entry in the message catalog by using the &quot;MESSAGE_ID=&quot; field of the current journal entry. Before returning the entry all journal field names in the catalog entry text enclosed in &quot;@&quot; will be replaced by the respective field values of the current entry. If a field name referenced in the message catalog entry does not exist, in the current journal entry, the &quot;@&quot; will be removed, but the field name otherwise left untouched. </p>
<p> <code>sd_journal_get_catalog_for_message_id()</code> works similar to <code>sd_journal_get_catalog()</code> but the entry is looked up by the specified message ID (no open journal context is necessary for this), and no field substitution is performed. </p>
<p> For more information about the journal message catalog please refer to the m[blue]<code>Journal Message Catalogs</code>m[]<font SIZE="-2">[1]</font> documentation page.</p>
<h2>Return Value</h2>
<p><code>sd_journal_get_catalog()</code> and <code>sd_journal_get_catalog_for_message_id()</code> return 0 on success or a negative errno-style error code. If no matching message catalog entry is found, -ENOENT is returned. </p>
<p> On successful return, <i>ret</i> points to a new string, which must be freed with <code><a href="/docs/linux/man/3-free/">free</a></code>(3).</p>
<h2>Notes</h2>
<p>The <code>sd_journal_get_catalog()</code> and <code>sd_journal_get_catalog_for_message_id()</code> interfaces are available as a shared library, which can be compiled and linked to with the <code>libsystemd</code>&nbsp;<wbr><code><a href="/docs/linux/man/1-pkg-config/">pkg-config</a></code>(1) file.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/7-systemd-journal-fields/">systemd.journal-fields</a></code>(7), <code><a href="/docs/linux/man/3-sd-journal/">sd-journal</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_open/">sd_journal_open</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_next/">sd_journal_next</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_get_data/">sd_journal_get_data</a></code>(3), <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>Journal Message Catalogs</p>
<dl>
<dd><a rel="nofollow" href="http://www.freedesktop.org/wiki/Software/systemd/catalog">http://www.freedesktop.org/wiki/Software/systemd/catalog</a></dl>
