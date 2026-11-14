---
title: "download-entities-pl(1)"
name: "download-entities-pl"
section: "1"
letter: "d"
url: "/docs/linux/man/1-download-entities-pl/"
---

download-entities - download and parse XML Entity definitions 

<h2>Synopsis</h2><pre> $ perl download-entities.pl -i # interactive
 $ perl download-entities.pl &gt; output-file.pm
 $ perl download-entities.pl output-file.pm
 
 # instead of <a rel="nofollow" HREF="http://www.w3.org/2003/entities/iso9573-2003/">http://www.w3.org/2003/entities/iso9573-2003/</a>
 $ perl download-entities.pl <a rel="nofollow" HREF="http://my.server.com/entities.html">http://my.server.com/entities.html</a></pre><h2>Description</h2>This script downloads the definitions of <font SIZE="-1">XML</font> entities from <a rel="nofollow" HREF="http://www.w3.org/2003/entities/iso9573-2003/">http://www.w3.org/2003/entities/iso9573-2003/</a> or from whatever address you give it as an argument. The argument should be an <font SIZE="-1">URL </font>(that LWP::UserAgent::get can access) pointing to a document with (absolute or relative) references to files ending with the <tt>&quot;.ent&quot;</tt> suffix. These files are expected to be <font SIZE="-1">DTD</font>'s with lines like 

 <pre> &lt;!ENTITY amp &quot;&amp;#38;&quot; &gt;</pre>The script parses these files and prints the perl module to the standard output. If you wish, you can give ``file'' as another argument to the script and it will then print it to ``file''. You can also specify the output file in the environment variable <tt>&quot;OUTPUT_FILE&quot;</tt>. 

 The index and the output file are distinguished by the presence of ``://'' substring. If you want to use a locally stored index file (the one with the .ent references), you can access it by saying 

 <pre> perl download.pl file:///path/to/index.html</pre>Note that the script currently distinguishes between relative and absolute paths by looking at whether the href contains a ``://'' substring. This can lead to crashes when the links look like href=``/path/file.ent''. 

 Also, the script assumes the links have exactly the format <i>href=``...''</i> - with double quotes.
<h3>Interactive download</h3>In case you run into problems downloading the documents, you can try to run the script with the <tt>&quot;-i&quot;</tt> or <tt>&quot;--interactive&quot;</tt> option. This will let you skip downloads or enter alternative URLs for individual documents. 

 The interactive mode is also triggered when the <tt>&quot;INTERACTIVE&quot;</tt> environment variable is set to a true value (in Perl sense).
<h3>Options</h3>Beside the <tt>&quot;--interactive&quot;</tt> option, this script also accepts the <tt>&quot;--timeout&quot;</tt> option. It specifies the timeout for LWP::UserAgent in seconds when downloading. The same is controlled by the <tt>&quot;DOWNLOAD_TIMEOUT&quot;</tt> environment variable. The defaule (180s) timeout is used when not specified. 

 <pre> # 10 seconds timeout - croak on failure
 perl download-entities.pl --timeout 10 &gt; XML/Entities/Data.pm
 # 5 seconds timeout - croak on failure
 DOWNLOAD_TIMEOUT=5 perl download-entities.pl &gt; XML/Entities/Data.pm
 # 1 second timeout - ask on failure
 perl download-entities.pl --interactive --timeout 1 &gt; XML/Entities/Data.pm</pre><h3>Dependencies</h3>This script has dependencies that the <tt>&quot;XML::Entities&quot;</tt> module does not and are therefore not mentioned in the <font SIZE="-1">META</font>.yml file. These are <tt>&quot;LWP::UserAgent&quot;</tt>, <tt>&quot;File::Basename&quot;</tt> and <tt>&quot;Fatal&quot;</tt>.
<h2>Copyright</h2>Copyright 2010 Jan Oldrich Kruza &lt;sixtease [at] cpan.org&gt;. All rights reserved. 

 This library is free software; you can redistribute it and/or modify it under the same terms as Perl itself.
