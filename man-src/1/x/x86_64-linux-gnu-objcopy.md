---
title: "x86_64-linux-gnu-objcopy(1)"
name: "x86_64-linux-gnu-objcopy"
section: "1"
letter: "x"
url: "/docs/linux/man/1-x86_64-linux-gnu-objcopy/"
---

<h2 class="name">NAME</h2>
 

 objcopy - copy and translate object files 

<h2>SYNOPSIS</h2>

 objcopy [<b>-F</b> <i>bfdname</i>|<b>--target=</b><i>bfdname</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>-I</b>&nbsp;<i>bfdname</i>|<b>--input-target=</b><i>bfdname</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>-O</b>&nbsp;<i>bfdname</i>|<b>--output-target=</b><i>bfdname</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>-B</b>&nbsp;<i>bfdarch</i>|<b>--binary-architecture=</b><i>bfdarch</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>-S</b>|<b>--strip-all</b>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>-g</b>|<b>--strip-debug</b>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--strip-unneeded</b>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>-K</b>&nbsp;<i>symbolname</i>|<b>--keep-symbol=</b><i>symbolname</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--keep-file-symbols</b>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--keep-section-symbols</b>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>-N</b>&nbsp;<i>symbolname</i>|<b>--strip-symbol=</b><i>symbolname</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--strip-unneeded-symbol=</b><i>symbolname</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>-G</b>&nbsp;<i>symbolname</i>|<b>--keep-global-symbol=</b><i>symbolname</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--localize-hidden</b>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>-L</b>&nbsp;<i>symbolname</i>|<b>--localize-symbol=</b><i>symbolname</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--globalize-symbol=</b><i>symbolname</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--globalize-symbols=</b><i>filename</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>-W</b>&nbsp;<i>symbolname</i>|<b>--weaken-symbol=</b><i>symbolname</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>-w</b>|<b>--wildcard</b>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>-x</b>|<b>--discard-all</b>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>-X</b>|<b>--discard-locals</b>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>-b</b>&nbsp;<i>byte</i>|<b>--byte=</b><i>byte</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>-i</b>&nbsp;[<i>breadth</i>]|<b>--interleave</b>[=<i>breadth</i>]] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--interleave-width=</b><i>width</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>-j</b>&nbsp;<i>sectionpattern</i>|<b>--only-section=</b><i>sectionpattern</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>-R</b>&nbsp;<i>sectionpattern</i>|<b>--remove-section=</b><i>sectionpattern</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--keep-section=</b><i>sectionpattern</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--remove-relocations=</b><i>sectionpattern</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>-p</b>|<b>--preserve-dates</b>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>-D</b>|<b>--enable-deterministic-archives</b>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>-U</b>|<b>--disable-deterministic-archives</b>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--debugging</b>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--gap-fill=</b><i>val</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--pad-to=</b><i>address</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--set-start=</b><i>val</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--adjust-start=</b><i>incr</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--change-addresses=</b><i>incr</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--change-section-address</b>&nbsp;<i>sectionpattern</i>{=,+,-}<i>val</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--change-section-lma</b>&nbsp;<i>sectionpattern</i>{=,+,-}<i>val</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--change-section-vma</b>&nbsp;<i>sectionpattern</i>{=,+,-}<i>val</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--change-warnings</b>]&nbsp;[<b>--no-change-warnings</b>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--set-section-flags</b>&nbsp;<i>sectionpattern</i>=<i>flags</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--set-section-alignment</b>&nbsp;<i>sectionpattern</i>=<i>align</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--add-section</b>&nbsp;<i>sectionname</i>=<i>filename</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--dump-section</b>&nbsp;<i>sectionname</i>=<i>filename</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--update-section</b>&nbsp;<i>sectionname</i>=<i>filename</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--rename-section</b>&nbsp;<i>oldname</i>=<i>newname</i>[,<i>flags</i>]] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--long-section-names</b>&nbsp;{enable,disable,keep}] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--change-leading-char</b>]&nbsp;[<b>--remove-leading-char</b>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--reverse-bytes=</b><i>num</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--srec-len=</b><i>ival</i>]&nbsp;[<b>--srec-forceS3</b>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--redefine-sym</b>&nbsp;<i>old</i>=<i>new</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--redefine-syms=</b><i>filename</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--weaken</b>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--keep-symbols=</b><i>filename</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--strip-symbols=</b><i>filename</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--strip-unneeded-symbols=</b><i>filename</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--keep-global-symbols=</b><i>filename</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--localize-symbols=</b><i>filename</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--weaken-symbols=</b><i>filename</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--add-symbol</b>&nbsp;<i>name</i>=[<i>section</i>:]<i>value</i>[,<i>flags</i>]] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--alt-machine-code=</b><i>index</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--prefix-symbols=</b><i>string</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--prefix-sections=</b><i>string</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--prefix-alloc-sections=</b><i>string</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--add-gnu-debuglink=</b><i>path-to-file</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--only-keep-debug</b>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--strip-dwo</b>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--extract-dwo</b>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--extract-symbol</b>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--writable-text</b>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--readonly-text</b>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--pure</b>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--impure</b>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--file-alignment=</b><i>num</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--heap=</b><i>size</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--image-base=</b><i>address</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--section-alignment=</b><i>num</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--stack=</b><i>size</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--subsystem=</b><i>which</i>:<i>major</i>.<i>minor</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--compress-debug-sections</b>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--decompress-debug-sections</b>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--elf-stt-common=</b><i>val</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--merge-notes</b>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--no-merge-notes</b>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--verilog-data-width=</b><i>val</i>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>-v</b>|<b>--verbose</b>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>-V</b>|<b>--version</b>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<b>--help</b>]&nbsp;[<b>--info</b>] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>infile</i>&nbsp;[<i>outfile</i>]

<h2>DESCRIPTION</h2>

 The <font SIZE="-1">GNU</font> <b>objcopy</b> utility copies the contents of an object file to another. <b>objcopy</b> uses the <font SIZE="-1">GNU BFD</font> Library to read and write the object files. It can write the destination object file in a format different from that of the source object file. The exact behavior of <b>objcopy</b> is controlled by command-line options. Note that <b>objcopy</b> should be able to copy a fully linked file between any two formats. However, copying a relocatable object file between any two formats may not work as expected. 

 <b>objcopy</b> creates temporary files to do its translations and deletes them afterward. <b>objcopy</b> uses <font SIZE="-1">BFD</font> to do all its translation work; it has access to all the formats described in <font SIZE="-1">BFD</font> and thus is able to recognize most formats without being told explicitly. 

 <b>objcopy</b> can be used to generate S-records by using an output target of <b>srec</b> (e.g., use <b>-O srec</b>). 

 <b>objcopy</b> can be used to generate a raw binary file by using an output target of <b>binary</b> (e.g., use <b>-O binary</b>). When <b>objcopy</b> generates a raw binary file, it will essentially produce a memory dump of the contents of the input object file. All symbols and relocation information will be discarded. The memory dump will start at the load address of the lowest section copied into the output file. 

 When generating an S-record or a raw binary file, it may be helpful to use <b>-S</b> to remove sections containing debugging information. In some cases <b>-R</b> will be useful to remove sections which contain information that is not needed by the binary file. 

 Note---<b>objcopy</b> is not able to change the endianness of its input files. If the input format has an endianness (some formats do not), <b>objcopy</b> can only copy the inputs into file formats that have the same endianness or which have no endianness (e.g., <b>srec</b>). (However, see the <b>--reverse-bytes</b> option.)

<h2>OPTIONS</h2>

<dl>
<dt><i>infile</i>
<dd>
<dt><i>outfile</i>
<dd> The input and output files, respectively. If you do not specify <i>outfile</i>, <b>objcopy</b> creates a temporary file and destructively renames the result with the name of <i>infile</i>.
<dt><b>-I</b> <i>bfdname</i>
<dd>
<dt><b>--input-target=</b><i>bfdname</i>
<dd> Consider the source file's object format to be <i>bfdname</i>, rather than attempting to deduce it.
<dt><b>-O</b> <i>bfdname</i>
<dd>
<dt><b>--output-target=</b><i>bfdname</i>
<dd> Write the output file using the object format <i>bfdname</i>.
<dt><b>-F</b> <i>bfdname</i>
<dd>
<dt><b>--target=</b><i>bfdname</i>
<dd> Use <i>bfdname</i> as the object format for both the input and the output file; i.e., simply transfer data from source to destination with no translation.
<dt><b>-B</b> <i>bfdarch</i>
<dd>
<dt><b>--binary-architecture=</b><i>bfdarch</i>
<dd> Useful when transforming a architecture-less input file into an object file. In this case the output architecture can be set to <i>bfdarch</i>. This option will be ignored if the input file has a known <i>bfdarch</i>. You can access this binary data inside a program by referencing the special symbols that are created by the conversion process. These symbols are called _binary_<i>objfile</i>_start, _binary_<i>objfile</i>_end and _binary_<i>objfile</i>_size. e.g. you can transform a picture file into an object file and then access it in your code using these symbols.
<dt><b>-j</b> <i>sectionpattern</i>
<dd>
<dt><b>--only-section=</b><i>sectionpattern</i>
<dd> Copy only the indicated sections from the input file to the output file. This option may be given more than once. Note that using this option inappropriately may make the output file unusable. Wildcard characters are accepted in <i>sectionpattern</i>. 

 If the first character of <i>sectionpattern</i> is the exclamation point (!) then matching sections will not be copied, even if earlier use of <b>--only-section</b> on the same command line would otherwise copy it. For example: 

 <pre>
          --only-section=.text.* --only-section=!.text.foo
</pre> 

 will copy all sectinos matching '.text.*' but not the section '.text.foo'.
<dt><b>-R</b> <i>sectionpattern</i>
<dd>
<dt><b>--remove-section=</b><i>sectionpattern</i>
<dd> Remove any section matching <i>sectionpattern</i> from the output file. This option may be given more than once. Note that using this option inappropriately may make the output file unusable. Wildcard characters are accepted in <i>sectionpattern</i>. Using both the <b>-j</b> and <b>-R</b> options together results in undefined behaviour. 

 If the first character of <i>sectionpattern</i> is the exclamation point (!) then matching sections will not be removed even if an earlier use of <b>--remove-section</b> on the same command line would otherwise remove it. For example: 

 <pre>
          --remove-section=.text.* --remove-section=!.text.foo
</pre> 

 will remove all sections matching the pattern '.text.*', but will not remove the section '.text.foo'.
<dt><b>--keep-section=</b><i>sectionpattern</i>
<dd> When removing sections from the output file, keep sections that match <i>sectionpattern</i>.
<dt><b>--remove-relocations=</b><i>sectionpattern</i>
<dd> Remove non-dynamic relocations from the output file for any section matching <i>sectionpattern</i>. This option may be given more than once. Note that using this option inappropriately may make the output file unusable, and attempting to remove a dynamic relocation section such as <b>.rela.plt</b> from an executable or shared library with <b>--remove-relocations=.plt</b> will not work. Wildcard characters are accepted in <i>sectionpattern</i>. For example: 

 <pre>
          --remove-relocations=.text.*
</pre> 

 will remove the relocations for all sections matching the pattern '.text.*'. 

 If the first character of <i>sectionpattern</i> is the exclamation point (!) then matching sections will not have their relocation removed even if an earlier use of <b>--remove-relocations</b> on the same command line would otherwise cause the relocations to be removed. For example: 

 <pre>
          --remove-relocations=.text.* --remove-relocations=!.text.foo
</pre> 

 will remove all relocations for sections matching the pattern '.text.*', but will not remove relocations for the section '.text.foo'.
<dt><b>-S</b>
<dd>
<dt><b>--strip-all</b>
<dd> Do not copy relocation and symbol information from the source file. Also deletes debug sections.
<dt><b>-g</b>
<dd>
<dt><b>--strip-debug</b>
<dd> Do not copy debugging symbols or sections from the source file.
<dt><b>--strip-unneeded</b>
<dd> Remove all symbols that are not needed for relocation processing in addition to debugging symbols and sections stripped by <b>--strip-debug</b>.
<dt><b>-K</b> <i>symbolname</i>
<dd>
<dt><b>--keep-symbol=</b><i>symbolname</i>
<dd> When stripping symbols, keep symbol <i>symbolname</i> even if it would normally be stripped. This option may be given more than once.
<dt><b>-N</b> <i>symbolname</i>
<dd>
<dt><b>--strip-symbol=</b><i>symbolname</i>
<dd> Do not copy symbol <i>symbolname</i> from the source file. This option may be given more than once.
<dt><b>--strip-unneeded-symbol=</b><i>symbolname</i>
<dd> Do not copy symbol <i>symbolname</i> from the source file unless it is needed by a relocation. This option may be given more than once.
<dt><b>-G</b> <i>symbolname</i>
<dd>
<dt><b>--keep-global-symbol=</b><i>symbolname</i>
<dd> Keep only symbol <i>symbolname</i> global. Make all other symbols local to the file, so that they are not visible externally. This option may be given more than once. Note: this option cannot be used in conjunction with the <b>--globalize-symbol</b> or <b>--globalize-symbols</b> options.
<dt><b>--localize-hidden</b>
<dd> In an <font SIZE="-1">ELF</font> object, mark all symbols that have hidden or internal visibility as local. This option applies on top of symbol-specific localization options such as <b>-L</b>.
<dt><b>-L</b> <i>symbolname</i>
<dd>
<dt><b>--localize-symbol=</b><i>symbolname</i>
<dd> Convert a global or weak symbol called <i>symbolname</i> into a local symbol, so that it is not visible externally. This option may be given more than once. Note - unique symbols are not converted.
<dt><b>-W</b> <i>symbolname</i>
<dd>
<dt><b>--weaken-symbol=</b><i>symbolname</i>
<dd> Make symbol <i>symbolname</i> weak. This option may be given more than once.
<dt><b>--globalize-symbol=</b><i>symbolname</i>
<dd> Give symbol <i>symbolname</i> global scoping so that it is visible outside of the file in which it is defined. This option may be given more than once. Note: this option cannot be used in conjunction with the <b>-G</b> or <b>--keep-global-symbol</b> options.
<dt><b>-w</b>
<dd>
<dt><b>--wildcard</b>
<dd> Permit regular expressions in <i>symbolname</i>s used in other command line options. The question mark (?), asterisk (*), backslash (\) and square brackets ([]) operators can be used anywhere in the symbol name. If the first character of the symbol name is the exclamation point (!) then the sense of the switch is reversed for that symbol. For example: 

 <pre>
          -w -W !foo -W fo*
</pre> 

 would cause objcopy to weaken all symbols that start with ``fo'' except for the symbol ``foo''.
<dt><b>-x</b>
<dd>
<dt><b>--discard-all</b>
<dd> Do not copy non-global symbols from the source file.
<dt><b>-X</b>
<dd>
<dt><b>--discard-locals</b>
<dd> Do not copy compiler-generated local symbols. (These usually start with <b>L</b> or <b>.</b>.)
<dt><b>-b</b> <i>byte</i>
<dd>
<dt><b>--byte=</b><i>byte</i>
<dd> If interleaving has been enabled via the <b>--interleave</b> option then start the range of bytes to keep at the <i>byte</i>th byte. <i>byte</i> can be in the range from 0 to <i>breadth</i>-1, where <i>breadth</i> is the value given by the <b>--interleave</b> option.
<dt><b>-i [</b><i>breadth</i><b>]</b>
<dd>
<dt><b>--interleave[=</b><i>breadth</i><b>]</b>
<dd> Only copy a range out of every <i>breadth</i> bytes. (Header data is not affected). Select which byte in the range begins the copy with the <b>--byte</b> option. Select the width of the range with the <b>--interleave-width</b> option. 

 This option is useful for creating files to program <font SIZE="-1">ROM.</font> It is typically used with an <tt>&quot;srec&quot;</tt> output target. Note that <b>objcopy</b> will complain if you do not specify the <b>--byte</b> option as well. 

 The default interleave breadth is 4, so with <b>--byte</b> set to 0, <b>objcopy</b> would copy the first byte out of every four bytes from the input to the output.
<dt><b>--interleave-width=</b><i>width</i>
<dd> When used with the <b>--interleave</b> option, copy <i>width</i> bytes at a time. The start of the range of bytes to be copied is set by the <b>--byte</b> option, and the extent of the range is set with the <b>--interleave</b> option. 

 The default value for this option is 1. The value of <i>width</i> plus the <i>byte</i> value set by the <b>--byte</b> option must not exceed the interleave breadth set by the <b>--interleave</b> option. 

 This option can be used to create images for two 16-bit flashes interleaved in a 32-bit bus by passing <b>-b 0 -i 4 --interleave-width=2</b> and <b>-b 2 -i 4 --interleave-width=2</b> to two <b>objcopy</b> commands. If the input was '12345678' then the outputs would be '1256' and '3478' respectively.
<dt><b>-p</b>
<dd>
<dt><b>--preserve-dates</b>
<dd> Set the access and modification dates of the output file to be the same as those of the input file.
<dt><b>-D</b>
<dd>
<dt><b>--enable-deterministic-archives</b>
<dd> Operate in <i>deterministic</i> mode. When copying archive members and writing the archive index, use zero for UIDs, GIDs, timestamps, and use consistent file modes for all files. 

 If <i>binutils</i> was configured with <b>--enable-deterministic-archives</b>, then this mode is on by default. It can be disabled with the <b>-U</b> option, below.
<dt><b>-U</b>
<dd>
<dt><b>--disable-deterministic-archives</b>
<dd> Do <i>not</i> operate in <i>deterministic</i> mode. This is the inverse of the <b>-D</b> option, above: when copying archive members and writing the archive index, use their actual <font SIZE="-1">UID, GID,</font> timestamp, and file mode values. 

 This is the default unless <i>binutils</i> was configured with <b>--enable-deterministic-archives</b>.
<dt><b>--debugging</b>
<dd> Convert debugging information, if possible. This is not the default because only certain debugging formats are supported, and the conversion process can be time consuming.
<dt><b>--gap-fill</b> <i>val</i>
<dd> Fill gaps between sections with <i>val</i>. This operation applies to the <i>load address</i> (<font SIZE="-1">LMA</font>) of the sections. It is done by increasing the size of the section with the lower address, and filling in the extra space created with <i>val</i>.
<dt><b>--pad-to</b> <i>address</i>
<dd> Pad the output file up to the load address <i>address</i>. This is done by increasing the size of the last section. The extra space is filled in with the value specified by <b>--gap-fill</b> (default zero).
<dt><b>--set-start</b> <i>val</i>
<dd> Set the start address (also known as the entry address) of the new file to <i>val</i>. Not all object file formats support setting the start address.
<dt><b>--change-start</b> <i>incr</i>
<dd>
<dt><b>--adjust-start</b> <i>incr</i>
<dd> Change the start address (also known as the entry address) by adding <i>incr</i>. Not all object file formats support setting the start address.
<dt><b>--change-addresses</b> <i>incr</i>
<dd>
<dt><b>--adjust-vma</b> <i>incr</i>
<dd> Change the <font SIZE="-1">VMA</font> and <font SIZE="-1">LMA</font> addresses of all sections, as well as the start address, by adding <i>incr</i>. Some object file formats do not permit section addresses to be changed arbitrarily. Note that this does not relocate the sections; if the program expects sections to be loaded at a certain address, and this option is used to change the sections such that they are loaded at a different address, the program may fail.
<dt><b>--change-section-address</b> <i>sectionpattern</i><b>{=,+,-}</b><i>val</i>
<dd>
<dt><b>--adjust-section-vma</b> <i>sectionpattern</i><b>{=,+,-}</b><i>val</i>
<dd> Set or change both the <font SIZE="-1">VMA</font> address and the <font SIZE="-1">LMA</font> address of any section matching <i>sectionpattern</i>. If <b>=</b> is used, the section address is set to <i>val</i>. Otherwise, <i>val</i> is added to or subtracted from the section address. See the comments under <b>--change-addresses</b>, above. If <i>sectionpattern</i> does not match any sections in the input file, a warning will be issued, unless <b>--no-change-warnings</b> is used.
<dt><b>--change-section-lma</b> <i>sectionpattern</i><b>{=,+,-}</b><i>val</i>
<dd> Set or change the <font SIZE="-1">LMA</font> address of any sections matching <i>sectionpattern</i>. The <font SIZE="-1">LMA</font> address is the address where the section will be loaded into memory at program load time. Normally this is the same as the <font SIZE="-1">VMA</font> address, which is the address of the section at program run time, but on some systems, especially those where a program is held in <font SIZE="-1">ROM,</font> the two can be different. If <b>=</b> is used, the section address is set to <i>val</i>. Otherwise, <i>val</i> is added to or subtracted from the section address. See the comments under <b>--change-addresses</b>, above. If <i>sectionpattern</i> does not match any sections in the input file, a warning will be issued, unless <b>--no-change-warnings</b> is used.
<dt><b>--change-section-vma</b> <i>sectionpattern</i><b>{=,+,-}</b><i>val</i>
<dd> Set or change the <font SIZE="-1">VMA</font> address of any section matching <i>sectionpattern</i>. The <font SIZE="-1">VMA</font> address is the address where the section will be located once the program has started executing. Normally this is the same as the <font SIZE="-1">LMA</font> address, which is the address where the section will be loaded into memory, but on some systems, especially those where a program is held in <font SIZE="-1">ROM,</font> the two can be different. If <b>=</b> is used, the section address is set to <i>val</i>. Otherwise, <i>val</i> is added to or subtracted from the section address. See the comments under <b>--change-addresses</b>, above. If <i>sectionpattern</i> does not match any sections in the input file, a warning will be issued, unless <b>--no-change-warnings</b> is used.
<dt><b>--change-warnings</b>
<dd>
<dt><b>--adjust-warnings</b>
<dd> If <b>--change-section-address</b> or <b>--change-section-lma</b> or <b>--change-section-vma</b> is used, and the section pattern does not match any sections, issue a warning. This is the default.
<dt><b>--no-change-warnings</b>
<dd>
<dt><b>--no-adjust-warnings</b>
<dd> Do not issue a warning if <b>--change-section-address</b> or <b>--adjust-section-lma</b> or <b>--adjust-section-vma</b> is used, even if the section pattern does not match any sections.
<dt><b>--set-section-flags</b> <i>sectionpattern</i><b>=</b><i>flags</i>
<dd> Set the flags for any sections matching <i>sectionpattern</i>. The <i>flags</i> argument is a comma separated string of flag names. The recognized names are <b>alloc</b>, <b>contents</b>, <b>load</b>, <b>noload</b>, <b>readonly</b>, <b>code</b>, <b>data</b>, <b>rom</b>, <b>exclude</b>, <b>share</b>, and <b>debug</b>. You can set the <b>contents</b> flag for a section which does not have contents, but it is not meaningful to clear the <b>contents</b> flag of a section which does have contents---just remove the section instead. Not all flags are meaningful for all object file formats. In particular the <b>share</b> flag is only meaningful for <font SIZE="-1">COFF</font> format files and not for <font SIZE="-1">ELF</font> format files.
<dt><b>--set-section-alignment</b> <i>sectionpattern</i><b>=</b><i>align</i>
<dd> Set the alignment for any sections matching <i>sectionpattern</i>. <i>align</i> specifies the alignment in bytes and must be a power of two, i.e. 1, 2, 4, 8....
<dt><b>--add-section</b> <i>sectionname</i><b>=</b><i>filename</i>
<dd> Add a new section named <i>sectionname</i> while copying the file. The contents of the new section are taken from the file <i>filename</i>. The size of the section will be the size of the file. This option only works on file formats which can support sections with arbitrary names. Note - it may be necessary to use the <b>--set-section-flags</b> option to set the attributes of the newly created section.
<dt><b>--dump-section</b> <i>sectionname</i><b>=</b><i>filename</i>
<dd> Place the contents of section named <i>sectionname</i> into the file <i>filename</i>, overwriting any contents that may have been there previously. This option is the inverse of <b>--add-section</b>. This option is similar to the <b>--only-section</b> option except that it does not create a formatted file, it just dumps the contents as raw binary data, without applying any relocations. The option can be specified more than once.
<dt><b>--update-section</b> <i>sectionname</i><b>=</b><i>filename</i>
<dd> Replace the existing contents of a section named <i>sectionname</i> with the contents of file <i>filename</i>. The size of the section will be adjusted to the size of the file. The section flags for <i>sectionname</i> will be unchanged. For <font SIZE="-1">ELF</font> format files the section to segment mapping will also remain unchanged, something which is not possible using <b>--remove-section</b> followed by <b>--add-section</b>. The option can be specified more than once. 

 Note - it is possible to use <b>--rename-section</b> and <b>--update-section</b> to both update and rename a section from one command line. In this case, pass the original section name to <b>--update-section</b>, and the original and new section names to <b>--rename-section</b>.
<dt><b>--add-symbol</b> <i>name</i><b>=[</b><i>section</i><b>:]</b><i>value</i><b>[,</b><i>flags</i><b>]</b>
<dd> Add a new symbol named <i>name</i> while copying the file. This option may be specified multiple times. If the <i>section</i> is given, the symbol will be associated with and relative to that section, otherwise it will be an <font SIZE="-1">ABS</font> symbol. Specifying an undefined section will result in a fatal error. There is no check for the value, it will be taken as specified. Symbol flags can be specified and not all flags will be meaningful for all object file formats. By default, the symbol will be global. The special flag 'before=<i>othersym</i>' will insert the new symbol in front of the specified <i>othersym</i>, otherwise the symbol(s) will be added at the end of the symbol table in the order they appear.
<dt><b>--rename-section</b> <i>oldname</i><b>=</b><i>newname</i><b>[,</b><i>flags</i><b>]</b>
<dd> Rename a section from <i>oldname</i> to <i>newname</i>, optionally changing the section's flags to <i>flags</i> in the process. This has the advantage over using a linker script to perform the rename in that the output stays as an object file and does not become a linked executable. This option accepts the same set of flags as the <b>--sect-section-flags</b> option. 

 This option is particularly helpful when the input format is binary, since this will always create a section called .data. If for example, you wanted instead to create a section called .rodata containing binary data you could use the following command line to achieve it: 

 <pre>
          objcopy -I binary -O &lt;output_format&gt; -B &lt;architecture&gt; \
           --rename-section .data=.rodata,alloc,load,readonly,data,contents \
           &lt;input_binary_file&gt; &lt;output_object_file&gt;
</pre>
<dt><b>--long-section-names {enable,disable,keep}</b>
<dd> Controls the handling of long section names when processing <tt>&quot;COFF&quot;</tt> and <tt>&quot;PE-COFF&quot;</tt> object formats. The default behaviour, <b>keep</b>, is to preserve long section names if any are present in the input file. The <b>enable</b> and <b>disable</b> options forcibly enable or disable the use of long section names in the output object; when <b>disable</b> is in effect, any long section names in the input object will be truncated. The <b>enable</b> option will only emit long section names if any are present in the inputs; this is mostly the same as <b>keep</b>, but it is left undefined whether the <b>enable</b> option might force the creation of an empty string table in the output file.
<dt><b>--change-leading-char</b>
<dd> Some object file formats use special characters at the start of symbols. The most common such character is underscore, which compilers often add before every symbol. This option tells <b>objcopy</b> to change the leading character of every symbol when it converts between object file formats. If the object file formats use the same leading character, this option has no effect. Otherwise, it will add a character, or remove a character, or change a character, as appropriate.
<dt><b>--remove-leading-char</b>
<dd> If the first character of a global symbol is a special symbol leading character used by the object file format, remove the character. The most common symbol leading character is underscore. This option will remove a leading underscore from all global symbols. This can be useful if you want to link together objects of different file formats with different conventions for symbol names. This is different from <b>--change-leading-char</b> because it always changes the symbol name when appropriate, regardless of the object file format of the output file.
<dt><b>--reverse-bytes=</b><i>num</i>
<dd> Reverse the bytes in a section with output contents. A section length must be evenly divisible by the value given in order for the swap to be able to take place. Reversing takes place before the interleaving is performed. 

 This option is used typically in generating <font SIZE="-1">ROM</font> images for problematic target systems. For example, on some target boards, the 32-bit words fetched from 8-bit ROMs are re-assembled in little-endian byte order regardless of the <font SIZE="-1">CPU</font> byte order. Depending on the programming model, the endianness of the <font SIZE="-1">ROM</font> may need to be modified. 

 Consider a simple file with a section containing the following eight bytes: <tt>12345678</tt>. 

 Using <b>--reverse-bytes=2</b> for the above example, the bytes in the output file would be ordered <tt>21436587</tt>. 

 Using <b>--reverse-bytes=4</b> for the above example, the bytes in the output file would be ordered <tt>43218765</tt>. 

 By using <b>--reverse-bytes=2</b> for the above example, followed by <b>--reverse-bytes=4</b> on the output file, the bytes in the second output file would be ordered <tt>34127856</tt>.
<dt><b>--srec-len=</b><i>ival</i>
<dd> Meaningful only for srec output. Set the maximum length of the Srecords being produced to <i>ival</i>. This length covers both address, data and crc fields.
<dt><b>--srec-forceS3</b>
<dd> Meaningful only for srec output. Avoid generation of S1/S2 records, creating S3-only record format.
<dt><b>--redefine-sym</b> <i>old</i><b>=</b><i>new</i>
<dd> Change the name of a symbol <i>old</i>, to <i>new</i>. This can be useful when one is trying link two things together for which you have no source, and there are name collisions.
<dt><b>--redefine-syms=</b><i>filename</i>
<dd> Apply <b>--redefine-sym</b> to each symbol pair &quot;<i>old</i> <i>new</i>&quot; listed in the file <i>filename</i>. <i>filename</i> is simply a flat file, with one symbol pair per line. Line comments may be introduced by the hash character. This option may be given more than once.
<dt><b>--weaken</b>
<dd> Change all global symbols in the file to be weak. This can be useful when building an object which will be linked against other objects using the <b>-R</b> option to the linker. This option is only effective when using an object file format which supports weak symbols.
<dt><b>--keep-symbols=</b><i>filename</i>
<dd> Apply <b>--keep-symbol</b> option to each symbol listed in the file <i>filename</i>. <i>filename</i> is simply a flat file, with one symbol name per line. Line comments may be introduced by the hash character. This option may be given more than once.
<dt><b>--strip-symbols=</b><i>filename</i>
<dd> Apply <b>--strip-symbol</b> option to each symbol listed in the file <i>filename</i>. <i>filename</i> is simply a flat file, with one symbol name per line. Line comments may be introduced by the hash character. This option may be given more than once.
<dt><b>--strip-unneeded-symbols=</b><i>filename</i>
<dd> Apply <b>--strip-unneeded-symbol</b> option to each symbol listed in the file <i>filename</i>. <i>filename</i> is simply a flat file, with one symbol name per line. Line comments may be introduced by the hash character. This option may be given more than once.
<dt><b>--keep-global-symbols=</b><i>filename</i>
<dd> Apply <b>--keep-global-symbol</b> option to each symbol listed in the file <i>filename</i>. <i>filename</i> is simply a flat file, with one symbol name per line. Line comments may be introduced by the hash character. This option may be given more than once.
<dt><b>--localize-symbols=</b><i>filename</i>
<dd> Apply <b>--localize-symbol</b> option to each symbol listed in the file <i>filename</i>. <i>filename</i> is simply a flat file, with one symbol name per line. Line comments may be introduced by the hash character. This option may be given more than once.
<dt><b>--globalize-symbols=</b><i>filename</i>
<dd> Apply <b>--globalize-symbol</b> option to each symbol listed in the file <i>filename</i>. <i>filename</i> is simply a flat file, with one symbol name per line. Line comments may be introduced by the hash character. This option may be given more than once. Note: this option cannot be used in conjunction with the <b>-G</b> or <b>--keep-global-symbol</b> options.
<dt><b>--weaken-symbols=</b><i>filename</i>
<dd> Apply <b>--weaken-symbol</b> option to each symbol listed in the file <i>filename</i>. <i>filename</i> is simply a flat file, with one symbol name per line. Line comments may be introduced by the hash character. This option may be given more than once.
<dt><b>--alt-machine-code=</b><i>index</i>
<dd> If the output architecture has alternate machine codes, use the <i>index</i>th code instead of the default one. This is useful in case a machine is assigned an official code and the tool-chain adopts the new code, but other applications still depend on the original code being used. For <font SIZE="-1">ELF</font> based architectures if the <i>index</i> alternative does not exist then the value is treated as an absolute number to be stored in the e_machine field of the <font SIZE="-1">ELF</font> header.
<dt><b>--writable-text</b>
<dd> Mark the output text as writable. This option isn't meaningful for all object file formats.
<dt><b>--readonly-text</b>
<dd> Make the output text write protected. This option isn't meaningful for all object file formats.
<dt><b>--pure</b>
<dd> Mark the output file as demand paged. This option isn't meaningful for all object file formats.
<dt><b>--impure</b>
<dd> Mark the output file as impure. This option isn't meaningful for all object file formats.
<dt><b>--prefix-symbols=</b><i>string</i>
<dd> Prefix all symbols in the output file with <i>string</i>.
<dt><b>--prefix-sections=</b><i>string</i>
<dd> Prefix all section names in the output file with <i>string</i>.
<dt><b>--prefix-alloc-sections=</b><i>string</i>
<dd> Prefix all the names of all allocated sections in the output file with <i>string</i>.
<dt><b>--add-gnu-debuglink=</b><i>path-to-file</i>
<dd> Creates a .gnu_debuglink section which contains a reference to <i>path-to-file</i> and adds it to the output file. Note: the file at <i>path-to-file</i> must exist. Part of the process of adding the .gnu_debuglink section involves embedding a checksum of the contents of the debug info file into the section. 

 If the debug info file is built in one location but it is going to be installed at a later time into a different location then do not use the path to the installed location. The <b>--add-gnu-debuglink</b> option will fail because the installed file does not exist yet. Instead put the debug info file in the current directory and use the <b>--add-gnu-debuglink</b> option without any directory components, like this: 

 <pre>
         objcopy --add-gnu-debuglink=foo.debug
</pre> 

 At debug time the debugger will attempt to look for the separate debug info file in a set of known locations. The exact set of these locations varies depending upon the distribution being used, but it typically includes:
<dl>
<dt>
<dd>
<dl>
<dt>&quot;* The same directory as the executable.&quot;
<dd>
<dt>&quot;* A sub-directory of the directory containing the executable&quot;
<dd> called .debug
<dt>&quot;* A global debug directory such as /usr/lib/debug.&quot;
<dd></dl>
</dl>

<dl>
<dt>
<dd> 

 As long as the debug info file has been installed into one of these locations before the debugger is run everything should work correctly.</dl>

<dt><b>--keep-section-symbils</b>
<dd> When stripping a file, perhaps with <b>--strip-debug</b> or <b>--strip-unneeded</b>, retain any symbols specifying section names, which would otherwise get stripped.
<dt><b>--keep-file-symbols</b>
<dd> When stripping a file, perhaps with <b>--strip-debug</b> or <b>--strip-unneeded</b>, retain any symbols specifying source file names, which would otherwise get stripped.
<dt><b>--only-keep-debug</b>
<dd> Strip a file, removing contents of any sections that would not be stripped by <b>--strip-debug</b> and leaving the debugging sections intact. In <font SIZE="-1">ELF</font> files, this preserves all note sections in the output. 

 Note - the section headers of the stripped sections are preserved, including their sizes, but the contents of the section are discarded. The section headers are preserved so that other tools can match up the debuginfo file with the real executable, even if that executable has been relocated to a different address space. 

 The intention is that this option will be used in conjunction with <b>--add-gnu-debuglink</b> to create a two part executable. One a stripped binary which will occupy less space in <font SIZE="-1">RAM</font> and in a distribution and the second a debugging information file which is only needed if debugging abilities are required. The suggested procedure to create these files is as follows:
<dl>
<dt>
<dd>
<dl>
<dt>1.&lt;Link the executable as normal. Assuming that it is called&gt;
<dd> <tt>&quot;foo&quot;</tt> then...
<dt>1.&lt;Run &quot;objcopy --only-keep-debug foo foo.dbg&quot; to&gt;
<dd> create a file containing the debugging info.
<dt>1.&lt;Run &quot;objcopy --strip-debug foo&quot; to create a&gt;
<dd> stripped executable.
<dt>1.&lt;Run &quot;objcopy --add-gnu-debuglink=foo.dbg foo&quot;&gt;
<dd> to add a link to the debugging info into the stripped executable.</dl>
</dl>

<dl>
<dt>
<dd> 

 Note---the choice of <tt>&quot;.dbg&quot;</tt> as an extension for the debug info file is arbitrary. Also the <tt>&quot;--only-keep-debug&quot;</tt> step is optional. You could instead do this:
<dl>
<dt>1.&lt;Link the executable as normal.&gt;
<dd>
<dt>1.&lt;Copy &quot;foo&quot; to &quot;foo.full&quot;&gt;
<dd>
<dt>1.&lt;Run &quot;objcopy --strip-debug foo&quot;&gt;
<dd>
<dt>1.&lt;Run &quot;objcopy --add-gnu-debuglink=foo.full foo&quot;&gt;
<dd></dl>
</dl>

<dl>
<dt>
<dd> 

 i.e., the file pointed to by the <b>--add-gnu-debuglink</b> can be the full executable. It does not have to be a file created by the <b>--only-keep-debug</b> switch. 

 Note---this switch is only intended for use on fully linked files. It does not make sense to use it on object files where the debugging information may be incomplete. Besides the gnu_debuglink feature currently only supports the presence of one filename containing debugging information, not multiple filenames on a one-per-object-file basis.</dl>

<dt><b>--strip-dwo</b>
<dd> Remove the contents of all <font SIZE="-1">DWARF</font> .dwo sections, leaving the remaining debugging sections and all symbols intact. This option is intended for use by the compiler as part of the <b>-gsplit-dwarf</b> option, which splits debug information between the .o file and a separate .dwo file. The compiler generates all debug information in the same file, then uses the <b>--extract-dwo</b> option to copy the .dwo sections to the .dwo file, then the <b>--strip-dwo</b> option to remove those sections from the original .o file.
<dt><b>--extract-dwo</b>
<dd> Extract the contents of all <font SIZE="-1">DWARF</font> .dwo sections. See the <b>--strip-dwo</b> option for more information.
<dt><b>--file-alignment</b> <i>num</i>
<dd> Specify the file alignment. Sections in the file will always begin at file offsets which are multiples of this number. This defaults to 512. [This option is specific to <font SIZE="-1">PE</font> targets.]
<dt><b>--heap</b> <i>reserve</i>
<dd>
<dt><b>--heap</b> <i>reserve</i><b>,</b><i>commit</i>
<dd> Specify the number of bytes of memory to reserve (and optionally commit) to be used as heap for this program. [This option is specific to <font SIZE="-1">PE</font> targets.]
<dt><b>--image-base</b> <i>value</i>
<dd> Use <i>value</i> as the base address of your program or dll. This is the lowest memory location that will be used when your program or dll is loaded. To reduce the need to relocate and improve performance of your dlls, each should have a unique base address and not overlap any other dlls. The default is 0x400000 for executables, and 0x10000000 for dlls. [This option is specific to <font SIZE="-1">PE</font> targets.]
<dt><b>--section-alignment</b> <i>num</i>
<dd> Sets the section alignment field in the <font SIZE="-1">PE</font> header. Sections in memory will always begin at addresses which are a multiple of this number. Defaults to 0x1000. [This option is specific to <font SIZE="-1">PE</font> targets.]
<dt><b>--stack</b> <i>reserve</i>
<dd>
<dt><b>--stack</b> <i>reserve</i><b>,</b><i>commit</i>
<dd> Specify the number of bytes of memory to reserve (and optionally commit) to be used as stack for this program. [This option is specific to <font SIZE="-1">PE</font> targets.]
<dt><b>--subsystem</b> <i>which</i>
<dd>
<dt><b>--subsystem</b> <i>which</i><b>:</b><i>major</i>
<dd>
<dt><b>--subsystem</b> <i>which</i><b>:</b><i>major</i><b>.</b><i>minor</i>
<dd> Specifies the subsystem under which your program will execute. The legal values for <i>which</i> are <tt>&quot;native&quot;</tt>, <tt>&quot;windows&quot;</tt>, <tt>&quot;console&quot;</tt>, <tt>&quot;posix&quot;</tt>, <tt>&quot;efi-app&quot;</tt>, <tt>&quot;efi-bsd&quot;</tt>, <tt>&quot;efi-rtd&quot;</tt>, <tt>&quot;sal-rtd&quot;</tt>, and <tt>&quot;xbox&quot;</tt>. You may optionally set the subsystem version also. Numeric values are also accepted for <i>which</i>. [This option is specific to <font SIZE="-1">PE</font> targets.]
<dt><b>--extract-symbol</b>
<dd> Keep the file's section flags and symbols but remove all section data. Specifically, the option:
<dl>
<dt>
<dd>
<dl>
<dt>*&lt;removes the contents of all sections;&gt;
<dd>
<dt>*&lt;sets the size of every section to zero; and&gt;
<dd>
<dt>*&lt;sets the file's start address to zero.&gt;
<dd></dl>
</dl>

<dl>
<dt>
<dd> 

 This option is used to build a <i>.sym</i> file for a VxWorks kernel. It can also be a useful way of reducing the size of a <b>--just-symbols</b> linker input file.</dl>

<dt><b>--compress-debug-sections</b>
<dd> Compress <font SIZE="-1">DWARF</font> debug sections using zlib with <font SIZE="-1">SHF_COMPRESSED</font> from the <font SIZE="-1">ELF ABI.</font> Note - if compression would actually make a section <i>larger</i>, then it is not compressed.
<dt><b>--compress-debug-sections=none</b>
<dd>
<dt><b>--compress-debug-sections=zlib</b>
<dd>
<dt><b>--compress-debug-sections=zlib-gnu</b>
<dd>
<dt><b>--compress-debug-sections=zlib-gabi</b>
<dd> For <font SIZE="-1">ELF</font> files, these options control how <font SIZE="-1">DWARF</font> debug sections are compressed. <b>--compress-debug-sections=none</b> is equivalent to <b>--decompress-debug-sections</b>. <b>--compress-debug-sections=zlib</b> and <b>--compress-debug-sections=zlib-gabi</b> are equivalent to <b>--compress-debug-sections</b>. <b>--compress-debug-sections=zlib-gnu</b> compresses <font SIZE="-1">DWARF</font> debug sections using zlib. The debug sections are renamed to begin with <b>.zdebug</b> instead of <b>.debug</b>. Note - if compression would actually make a section <i>larger</i>, then it is not compressed nor renamed.
<dt><b>--decompress-debug-sections</b>
<dd> Decompress <font SIZE="-1">DWARF</font> debug sections using zlib. The original section names of the compressed sections are restored.
<dt><b>--elf-stt-common=yes</b>
<dd>
<dt><b>--elf-stt-common=no</b>
<dd> For <font SIZE="-1">ELF</font> files, these options control whether common symbols should be converted to the <tt>&quot;STT_COMMON&quot;</tt> or <tt>&quot;STT_OBJECT&quot;</tt> type. <b>--elf-stt-common=yes</b> converts common symbol type to <tt>&quot;STT_COMMON&quot;</tt>. <b>--elf-stt-common=no</b> converts common symbol type to <tt>&quot;STT_OBJECT&quot;</tt>.
<dt><b>--merge-notes</b>
<dd>
<dt><b>--no-merge-notes</b>
<dd> For <font SIZE="-1">ELF</font> files, attempt (or do not attempt) to reduce the size of any <font SIZE="-1">SHT_NOTE</font> type sections by removing duplicate notes.
<dt><b>-V</b>
<dd>
<dt><b>--version</b>
<dd> Show the version number of <b>objcopy</b>.
<dt><b>--verilog-data-width=</b><i>bytes</i>
<dd> For Verilog output, this options controls the number of bytes converted for each output data element. The input target controls the endianness of the conversion.
<dt><b>-v</b>
<dd>
<dt><b>--verbose</b>
<dd> Verbose output: list all object files modified. In the case of archives, <b>objcopy -V</b> lists all members of the archive.
<dt><b>--help</b>
<dd> Show a summary of the options to <b>objcopy</b>.
<dt><b>--info</b>
<dd> Display a list showing all architectures and object formats available.
<dt><b>@</b><i>file</i>
<dd> Read command-line options from <i>file</i>. The options read are inserted in place of the original @<i>file</i> option. If <i>file</i> does not exist, or cannot be read, then the option will be treated literally, and not removed. 

 Options in <i>file</i> are separated by whitespace. A whitespace character may be included in an option by surrounding the entire option in either single or double quotes. Any character (including a backslash) may be included by prefixing the character to be included with a backslash. The <i>file</i> may itself contain additional @<i>file</i> options; any such options will be processed recursively.</dl>

<h2>SEE ALSO</h2>

 <b><a HREF="/docs/linux/man/1-ld/">ld</a></b>(1), <b><a HREF="/docs/linux/man/1-objdump/">objdump</a></b>(1), and the Info entries for <i>binutils</i>.

<h2>COPYRIGHT</h2>

 Copyright (c) 1991-2022 Free Software Foundation, Inc. 

 Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with no Invariant Sections, with no Front-Cover Texts, and with no Back-Cover Texts. A copy of the license is included in the section entitled ``<font SIZE="-1">GNU</font> Free Documentation License''. 

<h2>Index</h2>


