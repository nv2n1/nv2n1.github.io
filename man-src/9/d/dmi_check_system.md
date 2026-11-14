---
title: "dmi_check_system(9)"
name: "dmi_check_system"
section: "9"
letter: "d"
url: "/docs/linux/man/9-dmi_check_system/"
---

dmi_check_system - check system DMI data

<h2>Synopsis</h2>

<pre><code>int dmi_check_system(const struct dmi_system_id *list);</code></pre>

<h2>Arguments</h2>

<i>list</i>
<dl><dd><dd>array of dmi_system_id structures to match against All non-null elements of the list must match their slot's (field index's) data (i.e., each list string must be a substring of the specified DMI slot's string data) to be considered a successful match.</dl>

<h2>Description</h2>

Walk the blacklist table running matching functions until someone returns non zero or we hit the end. Callback function is called for each successful match. Returns the number of matches.

<h2>Copyright</h2>


