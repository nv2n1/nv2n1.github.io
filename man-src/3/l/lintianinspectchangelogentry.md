---
title: "lintianinspectchangelogentry(3)"
name: "lintianinspectchangelogentry"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianinspectchangelogentry/"
---

Lintian::Inspect::Changelog::Entry - represents one entry in a Debian changelog 

<h2>Synopsis</h2><h2>Description</h2><h3>Methods</h3><i>init</i> 

 Creates a new object, no options. 

 <i>new</i> 

 Alias for init. 

 <i>is_empty</i> 

 Checks if the object is actually initialized with data. Due to limitations in Parse::DebianChangelog this currently simply checks if one of the fields Source, Version, Maintainer, Date, or Changes is initialized.
<h3>Accessors</h3>The following fields are available via accessor functions (all fields are string values unless otherwise noted):
<dl COMPACT><dt>Source
<dd><dt>Version
<dd><dt>Distribution
<dd><dt>Urgency
<dd><dt>Urgency_Comment
<dd><dt>&quot;Urgency_LC&quot;
<dd><dt>&quot;ExtraFields&quot;
<dd>Extra_Fields (all fields except for urgency as hash; <font SIZE="-1">POD</font> spelling forces the underscore)
<dt>Header
<dd>Header (the whole header in verbatim form)
<dt>Changes
<dd>Changes (the actual content of the bug report, in verbatim form)
<dt>Trailer
<dd>Trailer (the whole trailer in verbatim form)
<dt>Closes
<dd>Closes (Array of bug numbers)
<dt>Maintainer
<dd><dt>&quot;MaintainerEmail&quot;
<dd><dt>Date
<dd><dt>Timestamp
<dd>Timestamp (Date expressed in seconds since the epoch)
<dt><font SIZE="-1">ERROR</font>
<dd><font SIZE="-1">ERROR</font> (last parse error related to this entry in the format described at Parse::DebianChangelog::get_parse_errors.</dl><h2>See Also</h2>Originally based on Parse::DebianChangelog by Frank Lichtenheld, &lt;frank [at] lichtenheld.de&gt;
<h2>Author</h2>Written by Felix Lechner &lt;felix.lechner [at] lease-up.com&gt; for Lintian in response to #933134.
<h2>Copyright And License</h2>Please see in the code; <font SIZE="-1">FSF</font>'s standard short text triggered a <font SIZE="-1">POD</font> spelling error here.
