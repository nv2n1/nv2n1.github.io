---
title: "lintiantags(3)"
name: "lintiantags"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintiantags/"
---

Lintian::Tags - Manipulate and output Lintian tags 

<h2>Synopsis</h2><pre> my $tags = Lintian::Tags-&gt;new;
 my $proc = Lintian::Processable::Package-&gt;new ('/path/to/file');
 $tags-&gt;file_start ($proc);
 $tags-&gt;file_overrides ('/path/to/an/overrides-file');
 $tags-&gt;tag ('lintian-tag', 'extra tag information');
 tag ('other-lintian-tag', 'with some extra data');
 tag ('third-lintian-tag'); # with no extra).
 my %overrides = $tags-&gt;overrides ($proc);
 my %stats = $tags-&gt;statistics;
 if ($tags-&gt;displayed ('lintian-tag')) {
 # do something if that tag would be displayed...
 }</pre><h2>Description</h2>This module stores metadata about Lintian tags, stores configuration about which tags should be displayed, handles displaying tags if appropriate, and stores cumulative statistics about what tags have been seen. It also accepts override information and determines whether a tag has been overridden, keeping override statistics. Finally, it supports answering metadata questions about Lintian tags, such as what references Lintian has for that tag. 

 Each Lintian::Tags object has its own tag list, file list, and associated statistics. Separate Lintian::Tags objects can be maintained and used independently. However, as a convenience for Lintian's most typical use case and for backward compatibility, the first created Lintian::Tags object is maintained as a global default. The <i>tag()</i> method can be called as a global function instead of a method, in which case it will act on that global default Lintian::Tags object.
<h2>Class Methods</h2><dl COMPACT><dt><i>new()</i>
<dd>Creates a new Lintian::Tags object, initializes all of its internal statistics and configuration to the defaults, and returns the newly created object.
<dt>tag(<font SIZE="-1">TAG,</font> [<font SIZE="-1">EXTRA, ...</font>])
<dd>Issue the Lintian tag <font SIZE="-1">TAG,</font> possibly suppressing it or not displaying it based on configuration. <font SIZE="-1">EXTRA,</font> if present, is additional information to display with the tag. It can be given as a list of strings, in which case they're joined by a single space before display. 

 This method can be called either as a class method (which is exported by the Lintian::Tags module) or as an instance method. If called as a class method, it uses the first-constructed Lintian::Tags object as its underlying object. 

 This method throws an exception if it is called without <i>file_start()</i> being called first or if an attempt is made to issue an unknown tag.</dl><h2>Instance Methods</h2><h3>Configuration</h3><dl COMPACT><dt>display(<font SIZE="-1">OPERATION, RELATION, SEVERITY, CERTAINTY</font>)
<dd>Configure which tags are displayed by severity and certainty. <font SIZE="-1">OPERATION</font> is <tt>&quot;+&quot;</tt> to display the indicated tags, <tt>&quot;-&quot;</tt> to not display the indicated tags, or <tt>&quot;=&quot;</tt> to not display any tags except the indicated ones. <font SIZE="-1">RELATION</font> is one of <tt>&quot;&lt;&quot;</tt>, <tt>&quot;&lt;=&quot;</tt>, <tt>&quot;=&quot;</tt>, <tt>&quot;&gt;=&quot;</tt>, or <tt>&quot;&gt;&quot;</tt>. The <font SIZE="-1">OPERATION</font> will be applied to all pairs of severity and certainty that match the given <font SIZE="-1">RELATION</font> on the <font SIZE="-1">SEVERITY</font> and <font SIZE="-1">CERTAINTY</font> arguments. If either of those arguments are undefined, the action applies to any value for that variable. For example: 

 <pre> $tags-&gt;display('=', '&gt;=', 'important');</pre>turns off display of all tags and then enables display of any tag (with any certainty) of severity important or higher. 

 <pre> $tags-&gt;display('+', '&gt;', 'normal', 'possible');</pre>adds to the current configuration display of all tags with a severity higher than normal and a certainty higher than possible (so important/certain and serious/certain). 

 <pre> $tags-&gt;display('-', '=', 'minor', 'possible');</pre>turns off display of tags of severity minor and certainty possible. 

 This method throws an exception on errors, such as an unknown severity or certainty or an impossible constraint (like <tt>&quot;&gt; serious&quot;</tt>).
<dt>show_experimental(<font SIZE="-1">BOOL</font>)
<dd>If <font SIZE="-1">BOOL</font> is true, configure experimental tags to be shown. If <font SIZE="-1">BOOL</font> is false, configure experimental tags to not be shown.
<dt>show_overrides(<font SIZE="-1">BOOL</font>)
<dd>If <font SIZE="-1">BOOL</font> is true, configure overridden tags to be shown. If <font SIZE="-1">BOOL</font> is false, configure overridden tags to not be shown.
<dt>sources([<font SIZE="-1">SOURCE</font> [, ...]])
<dd>Limits the displayed tags to only those from the listed sources. One or more sources may be given. If no sources are given, resets the Lintian::Tags object to display tags from any source. Tag sources are the names of references from the Ref metadata for the tags.
<dt>profile(<font SIZE="-1">PROFILE</font>)
<dd>Use the <font SIZE="-1">PROFILE</font> (Lintian::Profile) to determine which tags are suppressed, the severity of the tags and which tags are non-overridable.</dl><h3>File Metadata</h3><dl COMPACT><dt>file_start(<font SIZE="-1">PROC</font>)
<dd>Adds a new file from a processable, initializes the data structures used for statistics and overrides, and makes it the default file for which tags will be issued. Also call <i>Lintian::Output::print_end_pkg()</i> to end the previous file, if any, and <i>Lintian::Output::print_start_pkg()</i> to start the new file. 

 This method throws an exception if the file being added was already added earlier.
<dt>file_overrides(<font SIZE="-1">OVERRIDE-FILE</font>)
<dd>Read OVERRIDE-FILE and add the overrides found there which match the metadata of the current file (package and type). The overrides are added to the overrides hash in the info hash entry for the current file. 

 <i>file_start()</i> must be called before this method. This method throws an exception if there is no current file and calls <i>fail()</i> if the override file cannot be opened.
<dt>load_overrides
<dd>Loads overrides for the current file. This is basically a short-hand for finding the overrides file in the lab and calling files_overrides on it if it is present.
<dt><i>file_end()</i>
<dd>Ends processing of a file. 

 This does two things. First it emits ``unused-override'' tags for all unused overrides. Secondly, it calls Lintian::Output::print_end_pkg to mark the end of the package. 

 Note that this method is called by file_start if it detects another entry is already active.</dl><h3>Statistics</h3><dl COMPACT><dt>overrides(<font SIZE="-1">PROC</font>)
<dd>Returns a reference to the overrides hash for the given processable. The keys of this hash are the tags for which are overrides. The value for each key is another hash, whose keys are the extra data matched by that override and whose values are the counts of tags that matched that override. Overrides matching any tag by that name are stored with the empty string as metadata, so: 

 <pre> my $overrides = $tags-&gt;overrides('/some/file');
 print &quot;$overrides-&gt;{'some-tag'}{''}\n&quot;;</pre>will print out the number of tags that matched a general override for the tag some-tag, regardless of what extra data was associated with it.
<dt>statistics([<font SIZE="-1">PROC</font>])
<dd>Returns a reference to the statistics hash for the given processable or, if <font SIZE="-1">PROC</font> is omitted, a reference to the full statistics hash for all files. In the latter case, the returned hash reference has as keys the file names and as values the per-file statistics. 

 The per-file statistics has a set of hashes of keys to times seen in tags: tag names (the <tt>&quot;tags&quot;</tt> key), severities (the <tt>&quot;severity&quot;</tt> key), certainties (the <tt>&quot;certainty&quot;</tt> key), and tag codes (the <tt>&quot;types&quot;</tt> key). It also has an <tt>&quot;overrides&quot;</tt> key which has as its value another hash with those same four keys, which keeps statistics on overridden tags (not included in the regular counts).</dl><h3>Tag Reporting</h3><dl COMPACT><dt>displayed(<font SIZE="-1">TAG</font>)
<dd>Returns true if the given tag would be displayed given the current configuration, false otherwise. This does not check overrides, only whether the tag severity, certainty, and source warrants display given the configuration.
<dt>suppressed(<font SIZE="-1">TAG</font>)
<dd>Returns true if the given tag would be suppressed given the current configuration, false otherwise. This is different than <i>displayed()</i> in that a tag is only suppressed if Lintian treats the tag as if it's never been seen, doesn't update statistics, and doesn't change its exit status. Tags are suppressed via <i>profile()</i>.
<dt><i>ignored_overrides()</i>
<dd>Returns a hash of tags, for which overrides have been ignored. The keys are tag names and the value is the number of overrides that has been ignored.</dl><h2>Author</h2>Originally written by Russ Allbery &lt;rra [at] debian.org&gt; for Lintian.
<h2>See Also</h2><i><a HREF="/docs/linux/man/1-lintian/">lintian</a></i>(1), <i><a HREF="/docs/linux/man/3-lintian--output/">Lintian::Output</a></i>(3), <i><a HREF="/docs/linux/man/3-lintian--tag--info/">Lintian::Tag::Info</a></i>(3)
