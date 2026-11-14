---
title: "inline2test(1)"
name: "inline2test"
section: "1"
letter: "i"
url: "/docs/linux/man/1-inline2test/"
---

<h2 class="name">NAME</h2>
 

 inline2test - The Test::Inline 2 Test Compiler 

<h2>SYNOPIS</h2>

 <pre>
  &gt; inline2test ./inline2test.conf
  
  # In your inline2test.conf
  input=lib
  output=t
  execute=0
  verbose=1
  readonly=1
  header=inline2text.txt
</pre>

<h2>DESCRIPTION</h2>

 <tt>&quot;inline2test&quot;</tt> is the Test::Inline 2 test compiler. 

 It's job is to scan through an arbitrary tree of Perl source code files, locate inline test sections, extract them, convert them to test scripts, and write them to an output path. 

<h2>Index</h2>


