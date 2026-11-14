---
title: "pom2(1)"
name: "pom2"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pom2/"
---

<h2 class="name">NAME</h2>
 

 pom2 - convert POD to Text, HTML, etc., with Pod::POM 

<h2>SYNOPSIS</h2>

 <pre>
    pom2 text MyFile.pm &gt; MyFile.txt
    pom2 html MyFile.pm &gt; MyFile.html
    pom2 pod  MyFile.pm &gt; Myfile.pod
    pom2 format [options] MyFile.pm &gt; Myfile.xyz
</pre>

<h2>DESCRIPTION</h2>

 This script uses <tt>&quot;Pod::POM&quot;</tt> to convert a Pod document into text, <font SIZE="-1">HTML,</font> back into Pod (e.g. to normalise a document to fix any markup errors), or any other format for which you have a view module. 

 If the viewer is not one of the viewers bundled with <tt>&quot;Pod::POM&quot;</tt>, the script searches for an installed <tt>&quot;Pod::POM::View&quot;</tt> module that matches the specified format. For example if you have <tt>&quot;Pod::POM::View::DocBook&quot;</tt> installed then you could say: 

 <pre>
    pod2 docbook MyFile.pm &gt; MyFile.xml
</pre> 

 If any options other than <tt>&quot;--help&quot;</tt> are specified then they are passed to the constructor method of the view class. For example: 

 <pre>
    pod2 docbook --root=chapter --titlecasing MyFile.pm &gt; MyFile.xml
</pre> 

 would convert the Pod document to a DocBook chapter document with the titlecasing option enabled. Note that any string prefixed by &quot;<tt>&quot;--&quot;</tt>&quot; is taken as a valid option and passed to the constructor; if no value is specified then a value of 1 is passed in.

<h2>AUTHOR</h2>

 Andy Wardley &lt;abw [at] kfs.org&gt; 

 extended by Andrew Ford &lt;A.Ford [at] ford-mason.co.uk&gt;

<h2>VERSION</h2>

 This is version 0.3 of pom2.

<h2>COPYRIGHT</h2>

 Copyright (C) 2000, 2001 Andy Wardley. All Rights Reserved. 

 Copyright (C) 2009 Andrew Ford. All Rights Reserved. 

 This module is free software; you can redistribute it and/or modify it under the same terms as Perl itself.

<h2>SEE ALSO</h2>

 For further information please see Pod::POM. 

<h2>Index</h2>


