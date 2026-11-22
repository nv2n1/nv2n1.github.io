---

title: "pod2html(1)"
name: "pod2html"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pod2html/"
---

pod2html - convert .pod files to .html files 

<h2>SYNOPSIS</h2>

 <pre><code>
pod2html-- help-- htmldir = &lt;name&gt; --htmlroot = &lt;URL&gt; --infile = &lt;name&gt; --outfile = &lt;name&gt; --podpath = &lt;name&gt; : ... : &lt;name&gt; --podroot = &lt;name&gt; --cachedir = &lt;name&gt; --flush-- recurse-- norecurse-- quiet-- noquiet-- verbose-- noverbose-- index-- noindex-- backlink-- nobacklink-- header-- noheader-- poderrors-- nopoderrors-- css = &lt;URL&gt; --title = &lt;name&gt;
</code></pre>

<h2>DESCRIPTION</h2>

 Converts files from pod format (see perlpod) to HTML format.

<h2>ARGUMENTS</h2>

 pod2html takes the following arguments:
<dl>
<dt>help
</dt><dd> <pre>
  --help
</pre> 
 Displays the usage message.
</dd><dt>htmldir
</dt><dd> <pre>
  --htmldir=name
</pre> 
 Sets the directory to which all cross references in the resulting HTML file will be relative. Not passing this causes all links to be absolute since this is the value that tells Pod::Html the root of the documentation tree. 
 Do not use this and --htmlroot in the same call to pod2html; they are mutually exclusive.
</dd><dt>htmlroot
</dt><dd> <pre>
  --htmlroot=URL
</pre> 
 Sets the base URL for the HTML files. When cross-references are made, the HTML root is prepended to the URL. 
 Do not use this if relative links are desired: use --htmldir instead. 
 Do not pass both this and --htmldir to pod2html; they are mutually exclusive.
</dd><dt>infile
</dt><dd> <pre>
  --infile=name
</pre> 
 Specify the pod file to convert. Input is taken from STDIN if no infile is specified.
</dd><dt>outfile
</dt><dd> <pre>
  --outfile=name
</pre> 
 Specify the HTML file to create. Output goes to STDOUT if no outfile is specified.
</dd><dt>podroot
</dt><dd> <pre>
  --podroot=name
</pre> 
 Specify the base directory for finding library pods.
</dd><dt>podpath
</dt><dd> <pre>
  --podpath=name:...:name
</pre> 
 Specify which subdirectories of the podroot contain pod files whose HTML converted forms can be linked-to in cross-references.
</dd><dt>cachedir
</dt><dd> <pre>
  --cachedir=name
</pre> 
 Specify which directory is used for storing cache. Default directory is the current working directory.
</dd><dt>flush
</dt><dd> <pre>
  --flush
</pre> 
 Flush the cache.
</dd><dt>backlink
</dt><dd> <pre>
  --backlink
</pre> 
 Turn =head1 directives into links pointing to the top of the HTML file.
</dd><dt>nobacklink
</dt><dd> <pre>
  --nobacklink
</pre> 
 Do not turn =head1 directives into links pointing to the top of the HTML file (default behaviour).
</dd><dt>header
</dt><dd> <pre>
  --header
</pre> 
 Create header and footer blocks containing the text of the ``NAME'' section.
</dd><dt>noheader
</dt><dd> <pre>
  --noheader
</pre> 
 Do not create header and footer blocks containing the text of the ``NAME'' section (default behaviour).
</dd><dt>poderrors
</dt><dd> <pre>
  --poderrors
</pre> 
 Include a ``POD ERRORS'' section in the outfile if there were any POD errors in the infile (default behaviour).
</dd><dt>nopoderrors
</dt><dd> <pre>
  --nopoderrors
</pre> 
 Do not include a ``POD ERRORS'' section in the outfile if there were any POD errors in the infile.
</dd><dt>index
</dt><dd> <pre>
  --index
</pre> 
 Generate an index at the top of the HTML file (default behaviour).
</dd><dt>noindex
</dt><dd> <pre>
  --noindex
</pre> 
 Do not generate an index at the top of the HTML file.
</dd><dt>recurse
</dt><dd> <pre>
  --recurse
</pre> 
 Recurse into subdirectories specified in podpath (default behaviour).
</dd><dt>norecurse
</dt><dd> <pre>
  --norecurse
</pre> 
 Do not recurse into subdirectories specified in podpath.
</dd><dt>css
</dt><dd> <pre>
  --css=URL
</pre> 
 Specify the URL of cascading style sheet to link from resulting HTML file. Default is none style sheet.
</dd><dt>title
</dt><dd> <pre>
  --title=title
</pre> 
 Specify the title of the resulting HTML file.
</dd><dt>quiet
</dt><dd> <pre>
  --quiet
</pre> 
 Don't display mostly harmless warning messages.
</dd><dt>noquiet
</dt><dd> <pre>
  --noquiet
</pre> 
 Display mostly harmless warning messages (default behaviour). But this is not the same as ``verbose'' mode.
</dd><dt>verbose
</dt><dd> <pre>
  --verbose
</pre> 
 Display progress messages.
</dd><dt>noverbose
</dt><dd> <pre>
  --noverbose
</pre> 
 Do not display progress messages (default behaviour).</dd></dl>

<h2>AUTHOR</h2>

 Tom Christiansen, &lt;tchrist [at] perl.com&gt;.

<h2>BUGS</h2>

 See Pod::Html for a list of known bugs in the translator.

<h2>SEE ALSO</h2>

 perlpod, Pod::Html

<h2>COPYRIGHT</h2>

 This program is distributed under the Artistic License.
