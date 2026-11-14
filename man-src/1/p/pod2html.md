---
title: "pod2html(1)"
name: "pod2html"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pod2html/"
---

<h2 class="name">NAME</h2>
 

 pod2html - convert .pod files to .html files 

<h2>SYNOPSIS</h2>

 <pre><code>
pod2html-- help-- htmldir = &lt;name&gt; --htmlroot = &lt;URL&gt; --infile = &lt;name&gt; --outfile = &lt;name&gt; --podpath = &lt;name&gt; : ... : &lt;name&gt; --podroot = &lt;name&gt; --cachedir = &lt;name&gt; --flush-- recurse-- norecurse-- quiet-- noquiet-- verbose-- noverbose-- index-- noindex-- backlink-- nobacklink-- header-- noheader-- poderrors-- nopoderrors-- css = &lt;URL&gt; --title = &lt;name&gt;
</code></pre>

<h2>DESCRIPTION</h2>

 Converts files from pod format (see perlpod) to <font SIZE="-1">HTML</font> format.

<h2>ARGUMENTS</h2>

 pod2html takes the following arguments:
<dl>
<dt>help
<dd> <pre>
  --help
</pre> 

 Displays the usage message.
<dt>htmldir
<dd> <pre>
  --htmldir=name
</pre> 

 Sets the directory to which all cross references in the resulting <font SIZE="-1">HTML</font> file will be relative. Not passing this causes all links to be absolute since this is the value that tells Pod::Html the root of the documentation tree. 

 Do not use this and --htmlroot in the same call to pod2html; they are mutually exclusive.
<dt>htmlroot
<dd> <pre>
  --htmlroot=URL
</pre> 

 Sets the base <font SIZE="-1">URL</font> for the <font SIZE="-1">HTML</font> files. When cross-references are made, the <font SIZE="-1">HTML</font> root is prepended to the <font SIZE="-1">URL.</font> 

 Do not use this if relative links are desired: use --htmldir instead. 

 Do not pass both this and --htmldir to pod2html; they are mutually exclusive.
<dt>infile
<dd> <pre>
  --infile=name
</pre> 

 Specify the pod file to convert. Input is taken from <font SIZE="-1">STDIN</font> if no infile is specified.
<dt>outfile
<dd> <pre>
  --outfile=name
</pre> 

 Specify the <font SIZE="-1">HTML</font> file to create. Output goes to <font SIZE="-1">STDOUT</font> if no outfile is specified.
<dt>podroot
<dd> <pre>
  --podroot=name
</pre> 

 Specify the base directory for finding library pods.
<dt>podpath
<dd> <pre>
  --podpath=name:...:name
</pre> 

 Specify which subdirectories of the podroot contain pod files whose <font SIZE="-1">HTML</font> converted forms can be linked-to in cross-references.
<dt>cachedir
<dd> <pre>
  --cachedir=name
</pre> 

 Specify which directory is used for storing cache. Default directory is the current working directory.
<dt>flush
<dd> <pre>
  --flush
</pre> 

 Flush the cache.
<dt>backlink
<dd> <pre>
  --backlink
</pre> 

 Turn =head1 directives into links pointing to the top of the <font SIZE="-1">HTML</font> file.
<dt>nobacklink
<dd> <pre>
  --nobacklink
</pre> 

 Do not turn =head1 directives into links pointing to the top of the <font SIZE="-1">HTML</font> file (default behaviour).
<dt>header
<dd> <pre>
  --header
</pre> 

 Create header and footer blocks containing the text of the ``<font SIZE="-1">NAME''</font> section.
<dt>noheader
<dd> <pre>
  --noheader
</pre> 

 Do not create header and footer blocks containing the text of the ``<font SIZE="-1">NAME''</font> section (default behaviour).
<dt>poderrors
<dd> <pre>
  --poderrors
</pre> 

 Include a ``<font SIZE="-1">POD ERRORS''</font> section in the outfile if there were any <font SIZE="-1">POD</font> errors in the infile (default behaviour).
<dt>nopoderrors
<dd> <pre>
  --nopoderrors
</pre> 

 Do not include a ``<font SIZE="-1">POD ERRORS''</font> section in the outfile if there were any <font SIZE="-1">POD</font> errors in the infile.
<dt>index
<dd> <pre>
  --index
</pre> 

 Generate an index at the top of the <font SIZE="-1">HTML</font> file (default behaviour).
<dt>noindex
<dd> <pre>
  --noindex
</pre> 

 Do not generate an index at the top of the <font SIZE="-1">HTML</font> file.
<dt>recurse
<dd> <pre>
  --recurse
</pre> 

 Recurse into subdirectories specified in podpath (default behaviour).
<dt>norecurse
<dd> <pre>
  --norecurse
</pre> 

 Do not recurse into subdirectories specified in podpath.
<dt>css
<dd> <pre>
  --css=URL
</pre> 

 Specify the <font SIZE="-1">URL</font> of cascading style sheet to link from resulting <font SIZE="-1">HTML</font> file. Default is none style sheet.
<dt>title
<dd> <pre>
  --title=title
</pre> 

 Specify the title of the resulting <font SIZE="-1">HTML</font> file.
<dt>quiet
<dd> <pre>
  --quiet
</pre> 

 Don't display mostly harmless warning messages.
<dt>noquiet
<dd> <pre>
  --noquiet
</pre> 

 Display mostly harmless warning messages (default behaviour). But this is not the same as ``verbose'' mode.
<dt>verbose
<dd> <pre>
  --verbose
</pre> 

 Display progress messages.
<dt>noverbose
<dd> <pre>
  --noverbose
</pre> 

 Do not display progress messages (default behaviour).</dl>

<h2>AUTHOR</h2>

 Tom Christiansen, &lt;tchrist [at] perl.com&gt;.

<h2>BUGS</h2>

 See Pod::Html for a list of known bugs in the translator.

<h2>SEE ALSO</h2>

 perlpod, Pod::Html

<h2>COPYRIGHT</h2>

 This program is distributed under the Artistic License. 

<h2>Index</h2>


