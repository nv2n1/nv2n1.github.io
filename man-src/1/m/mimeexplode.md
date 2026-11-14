---
title: "mimeexplode(1)"
name: "mimeexplode"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mimeexplode/"
---

<h2 class="name">NAME</h2>
 

 mimeexplode - explode one or more MIME messages 

<h2>SYNOPSIS</h2>

 <pre>
    mimeexplode &lt;mime-msg-file&gt; &lt;mime-msg-file&gt; ...
    
    someprocess | mimeexplode -
</pre>

<h2>DESCRIPTION</h2>

 Takes one or more files from the command line that contain <font SIZE="-1">MIME</font> messages, and explodes their contents out into subdirectories of the current working directory. The subdirectories are just called <tt>&quot;msg0&quot;</tt>, <tt>&quot;msg1&quot;</tt>, <tt>&quot;msg2&quot;</tt>, etc. Existing directories are skipped over. 

 The message information is output to the stdout, like this: 

 <pre>
    Message: msg3 (inputfile1.msg)
        Part: msg3/filename-1.dat (text/plain)
        Part: msg3/filename-2.dat (text/plain)
    Message: msg5 (input-file2.msg)
        Part: msg5/dir.gif (image/gif)
        Part: msg5/face.jpg (image/jpeg)
    Message: msg6 (infile3)
        Part: msg6/filename-1.dat (text/plain)
</pre> 

 This was written as an example of the <font SIZE="-1">MIME::</font> modules in the MIME-parser package I wrote. It may prove useful as a quick-and-dirty way of splitting a <font SIZE="-1">MIME</font> message if you need to decode something, and you don't have a <font SIZE="-1">MIME</font> mail reader on hand.

<h2>COMMAND LINE OPTIONS</h2>

 None yet.

<h2>AUTHOR</h2>

 Eryq <tt>&quot;eryq [at] zeegee.com&quot;</tt>, in a big hurry... 

<h2>Index</h2>


