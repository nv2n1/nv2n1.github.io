---
title: "dpkgchangelogentry(3)"
name: "dpkgchangelogentry"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dpkgchangelogentry/"
---

Dpkg::Changelog::Entry - represents a changelog entry 

<h2>Description</h2>This object represents a changelog entry. It is composed of a set of lines with specific purpose: an header line, changes lines, a trailer line. Blank lines can be between those kind of lines.
<h2>Functions</h2><dl COMPACT><dt>my $entry = Dpkg::Changelog::Entry-&gt;<i>new()</i>
</dt><dd>Creates a new object. It doesn't represent a real changelog entry until one has been successfully parsed or built from scratch.
</dd><dt>my $str = $entry-&gt;<i>output()</i>
</dt><dd></dd><dt>&quot;$entry&quot;
</dt><dd>Get a string representation of the changelog entry.
</dd><dt>$entry-&gt;output($fh)
</dt><dd>Print the string representation of the changelog entry to a filehandle.
</dd><dt>$entry-&gt;get_part($part)
</dt><dd>Return either a string (for a single line) or an array ref (for multiple lines) corresponding to the requested part. <tt>$part</tt> can be ``header, ''changes``, ''trailer``, ''blank_after_header``, ''blank_after_changes``, ''blank_after_trailer&quot;.
</dd><dt>$entry-&gt;set_part($part, $value)
</dt><dd>Set the value of the corresponding part. <tt>$value</tt> can be a string or an array ref.
</dd><dt>$entry-&gt;extend_part($part, $value)
</dt><dd>Concatenate <tt>$value</tt> at the end of the part. If the part is already a multi-line value, <tt>$value</tt> is added as a new line otherwise it's concatenated at the end of the current line.
</dd><dt>$is_empty = $entry-&gt;<i>is_empty()</i>
</dt><dd>Returns 1 if the changelog entry doesn't contain anything at all. Returns 0 as soon as it contains something in any of its non-blank parts.
</dd><dt>$entry-&gt;<i>normalize()</i>
</dt><dd>Normalize the content. Strip whitespaces at end of lines, use a single empty line to separate each part.
</dd><dt>my $src = $entry-&gt;<i>get_source()</i>
</dt><dd>Return the name of the source package associated to the changelog entry.
</dd><dt>my $ver = $entry-&gt;<i>get_version()</i>
</dt><dd>Return the version associated to the changelog entry.
</dd><dt>my @dists = $entry-&gt;<i>get_distributions()</i>
</dt><dd>Return a list of target distributions for this version.
</dd><dt>$fields = $entry-&gt;<i>get_optional_fields()</i>
</dt><dd>Return a set of optional fields exposed by the changelog entry. It always returns a Dpkg::Control object (possibly empty though).
</dd><dt>$urgency = $entry-&gt;<i>get_urgency()</i>
</dt><dd>Return the urgency of the associated upload.
</dd><dt>my $maint = $entry-&gt;<i>get_maintainer()</i>
</dt><dd>Return the string identifying the person who signed this changelog entry.
</dd><dt>my $time = $entry-&gt;<i>get_timestamp()</i>
</dt><dd>Return the timestamp of the changelog entry.
</dd><dt>my $str = $entry-&gt;<i>get_dpkg_changes()</i>
</dt><dd>Returns a string that is suitable for usage in a <tt>&quot;Changes&quot;</tt> field in the output format of <tt>&quot;dpkg-parsechangelog&quot;</tt>.</dd></dl><h2>Changes</h2><h3>Version 1.00</h3>Mark the module as public.
<h2>Author</h2>Raphaël Hertzog &lt;hertzog [at] debian.org&gt;.
