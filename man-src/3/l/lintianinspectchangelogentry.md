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
</dt><dd></dd><dt>Version
</dt><dd></dd><dt>Distribution
</dt><dd></dd><dt>Urgency
</dt><dd></dd><dt>Urgency_Comment
</dt><dd></dd><dt>&quot;Urgency_LC&quot;
</dt><dd></dd><dt>&quot;ExtraFields&quot;
</dt><dd>Extra_Fields (all fields except for urgency as hash; POD spelling forces the underscore)
</dd><dt>Header
</dt><dd>Header (the whole header in verbatim form)
</dd><dt>Changes
</dt><dd>Changes (the actual content of the bug report, in verbatim form)
</dd><dt>Trailer
</dt><dd>Trailer (the whole trailer in verbatim form)
</dd><dt>Closes
</dt><dd>Closes (Array of bug numbers)
</dd><dt>Maintainer
</dt><dd></dd><dt>&quot;MaintainerEmail&quot;
</dt><dd></dd><dt>Date
</dt><dd></dd><dt>Timestamp
</dt><dd>Timestamp (Date expressed in seconds since the epoch)
</dd><dt>ERROR
</dt><dd>ERROR (last parse error related to this entry in the format described at Parse::DebianChangelog::get_parse_errors.</dd></dl><h2>See Also</h2>Originally based on Parse::DebianChangelog by Frank Lichtenheld, &lt;frank [at] lichtenheld.de&gt;
<h2>Author</h2>Written by Felix Lechner &lt;felix.lechner [at] lease-up.com&gt; for Lintian in response to #933134.
<h2>Copyright And License</h2>Please see in the code; FSF's standard short text triggered a POD spelling error here.
