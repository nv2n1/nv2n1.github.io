---
title: "dmi_first_match(9)"
name: "dmi_first_match"
section: "9"
letter: "d"
url: "/docs/linux/man/9-dmi_first_match/"
---

dmi_first_match - find dmi_system_id structure matching system DMI data

<h2>Synopsis</h2>

<pre><code>const struct dmi_system_id *dmi_first_match(const struct dmi_system_id *list);</code></pre>

<h2>Arguments</h2>

<i>list</i>
<dl><dd><dd>array of dmi_system_id structures to match against All non-null elements of the list must match their slot's (field index's) data (i.e., each list string must be a substring of the specified DMI slot's string data) to be considered a successful match.</dl>

<h2>Description</h2>

Walk the blacklist table until the first match is found. Return the pointer to the matching entry or NULL if there's no match.

<h2>Copyright</h2>


