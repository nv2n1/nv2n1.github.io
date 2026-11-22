---

title: "dm_date(1)"
name: "dm_date"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dm_date/"
---

dm_date - print out the system date and time 

<h2>SYNOPSIS</h2>

 This performs the same operation as the unix 'date' command, but using the Date::Manip module. 

 <pre><code>
dm_date[OPTION]...[+FORMAT]
</code></pre>

<h2>DESCRIPTION</h2>

 This displays information about the current system time, or some other time. Options are:
<dl>
<dt>-h, --help
</dt><dd> Print online help.
</dd><dt>-d STRING, --date=STRING
</dt><dd> Display time described by STRING. STRING can be any string which can be parsed by Date::Manip. Please refer to the Date::Manip::Date documentation for details.
</dd><dt>-f DATEFILE, --file=DATEFILE
</dt><dd> This reads each line in DATEFILE, and extracts a date from it and prints out the information. 
 Blank lines and lines starting with a pound (#) are ignored. Lines not containing a valid date are also ignored.
</dd><dt>-r FILE, --reference=FILE
</dt><dd> Displays the last modification time of FILE.
</dd><dt>-R, --rfc-2822
</dt><dd> Displayc the date and time in RFC 2822 format. 
 Example: Mon, 07 Aug 2006 12:34:56 -0600
</dd><dt>-u, --utc, --universal
</dt><dd> Converts the date to UT (GMT) and prints out the information.</dd></dl>
 

 Only one of -d, -f, or -r should be included. If more than one is included, the first one from the list (-d, -f, -r) is used and any other is ignored. 

 The format string starts with a plus (+) and contains any of the format directives described in Date::Manip::Date.

<h2>KNOWN BUGS</h2>

 None known.

<h2>BUGS AND QUESTIONS</h2>

 Please refer to the Date::Manip::Problems documentation for information on submitting bug reports or questions to the author.

<h2>SEE ALSO</h2>

 Date::Manip::Date

<h2>LICENSE</h2>

 This script is free software; you can redistribute it and/or modify it under the same terms as Perl itself.

<h2>AUTHOR</h2>

 Sullivan Beck (sbeck [at] cpan.org)
