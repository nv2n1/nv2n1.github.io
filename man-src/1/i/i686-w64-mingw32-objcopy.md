---
title: "i686-w64-mingw32-objcopy(1)"
name: "i686-w64-mingw32-objcopy"
section: "1"
letter: "i"
url: "/docs/linux/man/1-i686-w64-mingw32-objcopy/"
description: "objcopy – copy and translate object files"
---

<h2 class="name">NAME</h2>
<p> objcopy &#8211; copy and translate object files </p>
<h2>SYNOPSIS</h2>
<p> objcopy [<code>-F</code> <i>bfdname</i>|<code>&#8211;target=</code><i>bfdname</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-I</code>&nbsp;<wbr><i>bfdname</i>|<code>&#8211;input-target=</code><i>bfdname</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-O</code>&nbsp;<wbr><i>bfdname</i>|<code>&#8211;output-target=</code><i>bfdname</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-B</code>&nbsp;<wbr><i>bfdarch</i>|<code>&#8211;binary-architecture=</code><i>bfdarch</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-S</code>|<code>&#8211;strip-all</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-g</code>|<code>&#8211;strip-debug</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-K</code>&nbsp;<wbr><i>symbolname</i>|<code>&#8211;keep-symbol=</code><i>symbolname</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-N</code>&nbsp;<wbr><i>symbolname</i>|<code>&#8211;strip-symbol=</code><i>symbolname</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;strip-unneeded-symbol=</code><i>symbolname</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-G</code>&nbsp;<wbr><i>symbolname</i>|<code>&#8211;keep-global-symbol=</code><i>symbolname</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;localize-hidden</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-L</code>&nbsp;<wbr><i>symbolname</i>|<code>&#8211;localize-symbol=</code><i>symbolname</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;globalize-symbol=</code><i>symbolname</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-W</code>&nbsp;<wbr><i>symbolname</i>|<code>&#8211;weaken-symbol=</code><i>symbolname</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-w</code>|<code>&#8211;wildcard</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-x</code>|<code>&#8211;discard-all</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-X</code>|<code>&#8211;discard-locals</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-b</code>&nbsp;<wbr><i>byte</i>|<code>&#8211;byte=</code><i>byte</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-i</code>&nbsp;<wbr>[<i>breadth</i>]|<code>&#8211;interleave</code>[=<i>breadth</i>]]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;interleave-width=</code><i>width</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-j</code>&nbsp;<wbr><i>sectionpattern</i>|<code>&#8211;only-section=</code><i>sectionpattern</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-R</code>&nbsp;<wbr><i>sectionpattern</i>|<code>&#8211;remove-section=</code><i>sectionpattern</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-p</code>|<code>&#8211;preserve-dates</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-D</code>|<code>&#8211;enable-deterministic-archives</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-U</code>|<code>&#8211;disable-deterministic-archives</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;debugging</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;gap-fill=</code><i>val</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;pad-to=</code><i>address</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;set-start=</code><i>val</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;adjust-start=</code><i>incr</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;change-addresses=</code><i>incr</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;change-section-address</code>&nbsp;<wbr><i>sectionpattern</i>{=,+,-}<i>val</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;change-section-lma</code>&nbsp;<wbr><i>sectionpattern</i>{=,+,-}<i>val</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;change-section-vma</code>&nbsp;<wbr><i>sectionpattern</i>{=,+,-}<i>val</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;change-warnings</code>]&nbsp;<wbr>[<code>&#8211;no-change-warnings</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;set-section-flags</code>&nbsp;<wbr><i>sectionpattern</i>=<i>flags</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;add-section</code>&nbsp;<wbr><i>sectionname</i>=<i>filename</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;dump-section</code>&nbsp;<wbr><i>sectionname</i>=<i>filename</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;rename-section</code>&nbsp;<wbr><i>oldname</i>=<i>newname</i>[,<i>flags</i>]]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;long-section-names</code>&nbsp;<wbr>{enable,disable,keep}]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;change-leading-char</code>]&nbsp;<wbr>[<code>&#8211;remove-leading-char</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;reverse-bytes=</code><i>num</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;srec-len=</code><i>ival</i>]&nbsp;<wbr>[<code>&#8211;srec-forceS3</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;redefine-sym</code>&nbsp;<wbr><i>old</i>=<i>new</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;redefine-syms=</code><i>filename</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;weaken</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;keep-symbols=</code><i>filename</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;strip-symbols=</code><i>filename</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;strip-unneeded-symbols=</code><i>filename</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;keep-global-symbols=</code><i>filename</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;localize-symbols=</code><i>filename</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;globalize-symbols=</code><i>filename</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;weaken-symbols=</code><i>filename</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;alt-machine-code=</code><i>index</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;prefix-symbols=</code><i>string</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;prefix-sections=</code><i>string</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;prefix-alloc-sections=</code><i>string</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;add-gnu-debuglink=</code><i>path-to-file</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;keep-file-symbols</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;only-keep-debug</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;strip-dwo</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;extract-dwo</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;extract-symbol</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;writable-text</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;readonly-text</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;pure</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;impure</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;file-alignment=</code><i>num</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;heap=</code><i>size</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;image-base=</code><i>address</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;section-alignment=</code><i>num</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;stack=</code><i>size</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;subsystem=</code><i>which</i>:<i>major</i>.<i>minor</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;compress-debug-sections</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;decompress-debug-sections</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;dwarf-depth=</code><i>n</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;dwarf-start=</code><i>n</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-v</code>|<code>&#8211;verbose</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-V</code>|<code>&#8211;version</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;help</code>]&nbsp;<wbr>[<code>&#8211;info</code>]<br />
&nbsp;<wbr>&nbsp;<wbr><i>infile</i>&nbsp;<wbr>[<i>outfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <font SIZE="-1">GNU </font><code>objcopy</code> utility copies the contents of an object file to another. <code>objcopy</code> uses the <font SIZE="-1">GNU BFD</font> Library to read and write the object files. It can write the destination object file in a format different from that of the source object file. The exact behavior of <code>objcopy</code> is controlled by command-line options. Note that <code>objcopy</code> should be able to copy a fully linked file between any two formats. However, copying a relocatable object file between any two formats may not work as expected. </p>
<p> <code>objcopy</code> creates temporary files to do its translations and deletes them afterward. <code>objcopy</code> uses <font SIZE="-1">BFD</font> to do all its translation work; it has access to all the formats described in <font SIZE="-1">BFD</font> and thus is able to recognize most formats without being told explicitly. </p>
<p> <code>objcopy</code> can be used to generate S-records by using an output target of <code>srec</code> (e.g., use <code>-O srec</code>). </p>
<p> <code>objcopy</code> can be used to generate a raw binary file by using an output target of <code>binary</code> (e.g., use <code>-O binary</code>). When <code>objcopy</code> generates a raw binary file, it will essentially produce a memory dump of the contents of the input object file. All symbols and relocation information will be discarded. The memory dump will start at the load address of the lowest section copied into the output file. </p>
<p> When generating an S-record or a raw binary file, it may be helpful to use <code>-S</code> to remove sections containing debugging information. In some cases <code>-R</code> will be useful to remove sections which contain information that is not needed by the binary file. </p>
<p> Note&#8212;<code>objcopy</code> is not able to change the endianness of its input files. If the input format has an endianness (some formats do not), <code>objcopy</code> can only copy the inputs into file formats that have the same endianness or which have no endianness (e.g., <code>srec</code>). (However, see the <code>&#8211;reverse-bytes</code> option.)</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>infile</i></p>
<dd>
<dt><i>outfile</i></p>
<dd> The input and output files, respectively. If you do not specify <i>outfile</i>, <code>objcopy</code> creates a temporary file and destructively renames the result with the name of <i>infile</i>.</p>
<dt><code>-I</code> <i>bfdname</i></p>
<dd>
<dt><code>&#8211;input-target=</code><i>bfdname</i></p>
<dd> Consider the source file&#8217;s object format to be <i>bfdname</i>, rather than attempting to deduce it.</p>
<dt><code>-O</code> <i>bfdname</i></p>
<dd>
<dt><code>&#8211;output-target=</code><i>bfdname</i></p>
<dd> Write the output file using the object format <i>bfdname</i>.</p>
<dt><code>-F</code> <i>bfdname</i></p>
<dd>
<dt><code>&#8211;target=</code><i>bfdname</i></p>
<dd> Use <i>bfdname</i> as the object format for both the input and the output file; i.e., simply transfer data from source to destination with no translation.</p>
<dt><code>-B</code> <i>bfdarch</i></p>
<dd>
<dt><code>&#8211;binary-architecture=</code><i>bfdarch</i></p>
<dd> Useful when transforming a architecture-less input file into an object file. In this case the output architecture can be set to <i>bfdarch</i>. This option will be ignored if the input file has a known <i>bfdarch</i>. You can access this binary data inside a program by referencing the special symbols that are created by the conversion process. These symbols are called _binary_<i>objfile</i>_start, _binary_<i>objfile</i>_end and _binary_<i>objfile</i>_size. e.g. you can transform a picture file into an object file and then access it in your code using these symbols.</p>
<dt><code>-j</code> <i>sectionpattern</i></p>
<dd>
<dt><code>&#8211;only-section=</code><i>sectionpattern</i></p>
<dd> Copy only the indicated sections from the input file to the output file. This option may be given more than once. Note that using this option inappropriately may make the output file unusable. Wildcard characters are accepted in <i>sectionpattern</i>.</p>
<dt><code>-R</code> <i>sectionpattern</i></p>
<dd>
<dt><code>&#8211;remove-section=</code><i>sectionpattern</i></p>
<dd> Remove any section matching <i>sectionpattern</i> from the output file. This option may be given more than once. Note that using this option inappropriately may make the output file unusable. Wildcard characters are accepted in <i>sectionpattern</i>. Using both the <code>-j</code> and <code>-R</code> options together results in undefined behaviour.</p>
<dt><code>-S</code></p>
<dd>
<dt><code>&#8211;strip-all</code></p>
<dd> Do not copy relocation and symbol information from the source file.</p>
<dt><code>-g</code></p>
<dd>
<dt><code>&#8211;strip-debug</code></p>
<dd> Do not copy debugging symbols or sections from the source file.</p>
<dt><code>&#8211;strip-unneeded</code></p>
<dd> Strip all symbols that are not needed for relocation processing.</p>
<dt><code>-K</code> <i>symbolname</i></p>
<dd>
<dt><code>&#8211;keep-symbol=</code><i>symbolname</i></p>
<dd> When stripping symbols, keep symbol <i>symbolname</i> even if it would normally be stripped. This option may be given more than once.</p>
<dt><code>-N</code> <i>symbolname</i></p>
<dd>
<dt><code>&#8211;strip-symbol=</code><i>symbolname</i></p>
<dd> Do not copy symbol <i>symbolname</i> from the source file. This option may be given more than once.</p>
<dt><code>&#8211;strip-unneeded-symbol=</code><i>symbolname</i></p>
<dd> Do not copy symbol <i>symbolname</i> from the source file unless it is needed by a relocation. This option may be given more than once.</p>
<dt><code>-G</code> <i>symbolname</i></p>
<dd>
<dt><code>&#8211;keep-global-symbol=</code><i>symbolname</i></p>
<dd> Keep only symbol <i>symbolname</i> global. Make all other symbols local to the file, so that they are not visible externally. This option may be given more than once.</p>
<dt><code>&#8211;localize-hidden</code></p>
<dd> In an <font SIZE="-1">ELF</font> object, mark all symbols that have hidden or internal visibility as local. This option applies on top of symbol-specific localization options such as <code>-L</code>.</p>
<dt><code>-L</code> <i>symbolname</i></p>
<dd>
<dt><code>&#8211;localize-symbol=</code><i>symbolname</i></p>
<dd> Make symbol <i>symbolname</i> local to the file, so that it is not visible externally. This option may be given more than once.</p>
<dt><code>-W</code> <i>symbolname</i></p>
<dd>
<dt><code>&#8211;weaken-symbol=</code><i>symbolname</i></p>
<dd> Make symbol <i>symbolname</i> weak. This option may be given more than once.</p>
<dt><code>&#8211;globalize-symbol=</code><i>symbolname</i></p>
<dd> Give symbol <i>symbolname</i> global scoping so that it is visible outside of the file in which it is defined. This option may be given more than once.</p>
<dt><code>-w</code></p>
<dd>
<dt><code>&#8211;wildcard</code></p>
<dd> Permit regular expressions in <i>symbolname</i>s used in other command line options. The question mark (?), asterisk (*), backslash (\) and square brackets ([]) operators can be used anywhere in the symbol name. If the first character of the symbol name is the exclamation point (!) then the sense of the switch is reversed for that symbol. For example: </p>
<pre>
          -w -W !foo -W fo*
</pre>
<p> would cause objcopy to weaken all symbols that start with &#8220;fo&#8221; except for the symbol &#8220;foo&#8221;.</p>
<dt><code>-x</code></p>
<dd>
<dt><code>&#8211;discard-all</code></p>
<dd> Do not copy non-global symbols from the source file.</p>
<dt><code>-X</code></p>
<dd>
<dt><code>&#8211;discard-locals</code></p>
<dd> Do not copy compiler-generated local symbols. (These usually start with <code>L</code> or <code>.</code>.)</p>
<dt><code>-b</code> <i>byte</i></p>
<dd>
<dt><code>&#8211;byte=</code><i>byte</i></p>
<dd> If interleaving has been enabled via the <code>&#8211;interleave</code> option then start the range of bytes to keep at the <i>byte</i>th byte. <i>byte</i> can be in the range from 0 to <i>breadth</i>-1, where <i>breadth</i> is the value given by the <code>&#8211;interleave</code> option.</p>
<dt><code>-i [</code><i>breadth</i><code>]</code></p>
<dd>
<dt><code>&#8211;interleave[=</code><i>breadth</i><code>]</code></p>
<dd> Only copy a range out of every <i>breadth</i> bytes. (Header data is not affected). Select which byte in the range begins the copy with the <code>&#8211;byte</code> option. Select the width of the range with the <code>&#8211;interleave-width</code> option. </p>
<p> This option is useful for creating files to program <font SIZE="-1">ROM. </font> It is typically used with an <tt>&quot;srec&quot;</tt> output target. Note that <code>objcopy</code> will complain if you do not specify the <code>&#8211;byte</code> option as well. </p>
<p> The default interleave breadth is 4, so with <code>&#8211;byte</code> set to 0, <code>objcopy</code> would copy the first byte out of every four bytes from the input to the output.</p>
<dt><code>&#8211;interleave-width=</code><i>width</i></p>
<dd> When used with the <code>&#8211;interleave</code> option, copy <i>width</i> bytes at a time. The start of the range of bytes to be copied is set by the <code>&#8211;byte</code> option, and the extent of the range is set with the <code>&#8211;interleave</code> option. </p>
<p> The default value for this option is 1. The value of <i>width</i> plus the <i>byte</i> value set by the <code>&#8211;byte</code> option must not exceed the interleave breadth set by the <code>&#8211;interleave</code> option. </p>
<p> This option can be used to create images for two 16-bit flashes interleaved in a 32-bit bus by passing <code>-b 0 -i 4 &#8211;interleave-width=2</code> and <code>-b 2 -i 4 &#8211;interleave-width=2</code> to two <code>objcopy</code> commands. If the input was &#8216;12345678&#8217; then the outputs would be &#8216;1256&#8217; and &#8216;3478&#8217; respectively.</p>
<dt><code>-p</code></p>
<dd>
<dt><code>&#8211;preserve-dates</code></p>
<dd> Set the access and modification dates of the output file to be the same as those of the input file.</p>
<dt><code>-D</code></p>
<dd>
<dt><code>&#8211;enable-deterministic-archives</code></p>
<dd> Operate in <i>deterministic</i> mode. When copying archive members and writing the archive index, use zero for UIDs, GIDs, timestamps, and use consistent file modes for all files. </p>
<p> If <i>binutils</i> was configured with <code>&#8211;enable-deterministic-archives</code>, then this mode is on by default. It can be disabled with the <code>-U</code> option, below.</p>
<dt><code>-U</code></p>
<dd>
<dt><code>&#8211;disable-deterministic-archives</code></p>
<dd> Do <i>not</i> operate in <i>deterministic</i> mode. This is the inverse of the <code>-D</code> option, above: when copying archive members and writing the archive index, use their actual <font SIZE="-1">UID, GID,</font> timestamp, and file mode values. </p>
<p> This is the default unless <i>binutils</i> was configured with <code>&#8211;enable-deterministic-archives</code>.</p>
<dt><code>&#8211;debugging</code></p>
<dd> Convert debugging information, if possible. This is not the default because only certain debugging formats are supported, and the conversion process can be time consuming.</p>
<dt><code>&#8211;gap-fill</code> <i>val</i></p>
<dd> Fill gaps between sections with <i>val</i>. This operation applies to the <i>load address</i> (<font SIZE="-1">LMA</font>) of the sections. It is done by increasing the size of the section with the lower address, and filling in the extra space created with <i>val</i>.</p>
<dt><code>&#8211;pad-to</code> <i>address</i></p>
<dd> Pad the output file up to the load address <i>address</i>. This is done by increasing the size of the last section. The extra space is filled in with the value specified by <code>&#8211;gap-fill</code> (default zero).</p>
<dt><code>&#8211;set-start</code> <i>val</i></p>
<dd> Set the start address of the new file to <i>val</i>. Not all object file formats support setting the start address.</p>
<dt><code>&#8211;change-start</code> <i>incr</i></p>
<dd>
<dt><code>&#8211;adjust-start</code> <i>incr</i></p>
<dd> Change the start address by adding <i>incr</i>. Not all object file formats support setting the start address.</p>
<dt><code>&#8211;change-addresses</code> <i>incr</i></p>
<dd>
<dt><code>&#8211;adjust-vma</code> <i>incr</i></p>
<dd> Change the <font SIZE="-1">VMA</font> and <font SIZE="-1">LMA</font> addresses of all sections, as well as the start address, by adding <i>incr</i>. Some object file formats do not permit section addresses to be changed arbitrarily. Note that this does not relocate the sections; if the program expects sections to be loaded at a certain address, and this option is used to change the sections such that they are loaded at a different address, the program may fail.</p>
<dt><code>&#8211;change-section-address</code> <i>sectionpattern</i><code>{=,+,-}</code><i>val</i></p>
<dd>
<dt><code>&#8211;adjust-section-vma</code> <i>sectionpattern</i><code>{=,+,-}</code><i>val</i></p>
<dd> Set or change both the <font SIZE="-1">VMA</font> address and the <font SIZE="-1">LMA</font> address of any section matching <i>sectionpattern</i>. If <code>=</code> is used, the section address is set to <i>val</i>. Otherwise, <i>val</i> is added to or subtracted from the section address. See the comments under <code>&#8211;change-addresses</code>, above. If <i>sectionpattern</i> does not match any sections in the input file, a warning will be issued, unless <code>&#8211;no-change-warnings</code> is used.</p>
<dt><code>&#8211;change-section-lma</code> <i>sectionpattern</i><code>{=,+,-}</code><i>val</i></p>
<dd> Set or change the <font SIZE="-1">LMA</font> address of any sections matching <i>sectionpattern</i>. The <font SIZE="-1">LMA</font> address is the address where the section will be loaded into memory at program load time. Normally this is the same as the <font SIZE="-1">VMA</font> address, which is the address of the section at program run time, but on some systems, especially those where a program is held in <font SIZE="-1">ROM,</font> the two can be different. If <code>=</code> is used, the section address is set to <i>val</i>. Otherwise, <i>val</i> is added to or subtracted from the section address. See the comments under <code>&#8211;change-addresses</code>, above. If <i>sectionpattern</i> does not match any sections in the input file, a warning will be issued, unless <code>&#8211;no-change-warnings</code> is used.</p>
<dt><code>&#8211;change-section-vma</code> <i>sectionpattern</i><code>{=,+,-}</code><i>val</i></p>
<dd> Set or change the <font SIZE="-1">VMA</font> address of any section matching <i>sectionpattern</i>. The <font SIZE="-1">VMA</font> address is the address where the section will be located once the program has started executing. Normally this is the same as the <font SIZE="-1">LMA</font> address, which is the address where the section will be loaded into memory, but on some systems, especially those where a program is held in <font SIZE="-1">ROM,</font> the two can be different. If <code>=</code> is used, the section address is set to <i>val</i>. Otherwise, <i>val</i> is added to or subtracted from the section address. See the comments under <code>&#8211;change-addresses</code>, above. If <i>sectionpattern</i> does not match any sections in the input file, a warning will be issued, unless <code>&#8211;no-change-warnings</code> is used.</p>
<dt><code>&#8211;change-warnings</code></p>
<dd>
<dt><code>&#8211;adjust-warnings</code></p>
<dd> If <code>&#8211;change-section-address</code> or <code>&#8211;change-section-lma</code> or <code>&#8211;change-section-vma</code> is used, and the section pattern does not match any sections, issue a warning. This is the default.</p>
<dt><code>&#8211;no-change-warnings</code></p>
<dd>
<dt><code>&#8211;no-adjust-warnings</code></p>
<dd> Do not issue a warning if <code>&#8211;change-section-address</code> or <code>&#8211;adjust-section-lma</code> or <code>&#8211;adjust-section-vma</code> is used, even if the section pattern does not match any sections.</p>
<dt><code>&#8211;set-section-flags</code> <i>sectionpattern</i><code>=</code><i>flags</i></p>
<dd> Set the flags for any sections matching <i>sectionpattern</i>. The <i>flags</i> argument is a comma separated string of flag names. The recognized names are <code>alloc</code>, <code>contents</code>, <code>load</code>, <code>noload</code>, <code>readonly</code>, <code>code</code>, <code>data</code>, <code>rom</code>, <code>share</code>, and <code>debug</code>. You can set the <code>contents</code> flag for a section which does not have contents, but it is not meaningful to clear the <code>contents</code> flag of a section which does have contents&#8212;just remove the section instead. Not all flags are meaningful for all object file formats.</p>
<dt><code>&#8211;add-section</code> <i>sectionname</i><code>=</code><i>filename</i></p>
<dd> Add a new section named <i>sectionname</i> while copying the file. The contents of the new section are taken from the file <i>filename</i>. The size of the section will be the size of the file. This option only works on file formats which can support sections with arbitrary names. Note &#8211; it may be necessary to use the <code>&#8211;set-section-flags</code> option to set the attributes of the newly created section.</p>
<dt><code>&#8211;dump-section</code> <i>sectionname</i><code>=</code><i>filename</i></p>
<dd> Place the contents of section named <i>sectionname</i> into the file <i>filename</i>, overwriting any contents that may have been there previously. This option is the inverse of <code>&#8211;add-section</code>. This option is similar to the <code>&#8211;only-section</code> option except that it does not create a formatted file, it just dumps the contents as raw binary data, without applying any relocations. The option can be specified more than once.</p>
<dt><code>&#8211;rename-section</code> <i>oldname</i><code>=</code><i>newname</i><code>[,</code><i>flags</i><code>]</code></p>
<dd> Rename a section from <i>oldname</i> to <i>newname</i>, optionally changing the section&#8217;s flags to <i>flags</i> in the process. This has the advantage over usng a linker script to perform the rename in that the output stays as an object file and does not become a linked executable. </p>
<p> This option is particularly helpful when the input format is binary, since this will always create a section called .data. If for example, you wanted instead to create a section called .rodata containing binary data you could use the following command line to achieve it: </p>
<pre>
          objcopy -I binary -O &lt;output_format&gt; -B &lt;architecture&gt; \
           --rename-section .data=.rodata,alloc,load,readonly,data,contents \
           &lt;input_binary_file&gt; &lt;output_object_file&gt;
</pre>
<dt><code>&#8211;long-section-names {enable,disable,keep}</code></p>
<dd> Controls the handling of long section names when processing <tt>&quot;COFF&quot;</tt> and <tt>&quot;PE-COFF&quot;</tt> object formats. The default behaviour, <code>keep</code>, is to preserve long section names if any are present in the input file. The <code>enable</code> and <code>disable</code> options forcibly enable or disable the use of long section names in the output object; when <code>disable</code> is in effect, any long section names in the input object will be truncated. The <code>enable</code> option will only emit long section names if any are present in the inputs; this is mostly the same as <code>keep</code>, but it is left undefined whether the <code>enable</code> option might force the creation of an empty string table in the output file.</p>
<dt><code>&#8211;change-leading-char</code></p>
<dd> Some object file formats use special characters at the start of symbols. The most common such character is underscore, which compilers often add before every symbol. This option tells <code>objcopy</code> to change the leading character of every symbol when it converts between object file formats. If the object file formats use the same leading character, this option has no effect. Otherwise, it will add a character, or remove a character, or change a character, as appropriate.</p>
<dt><code>&#8211;remove-leading-char</code></p>
<dd> If the first character of a global symbol is a special symbol leading character used by the object file format, remove the character. The most common symbol leading character is underscore. This option will remove a leading underscore from all global symbols. This can be useful if you want to link together objects of different file formats with different conventions for symbol names. This is different from <code>&#8211;change-leading-char</code> because it always changes the symbol name when appropriate, regardless of the object file format of the output file.</p>
<dt><code>&#8211;reverse-bytes=</code><i>num</i></p>
<dd> Reverse the bytes in a section with output contents. A section length must be evenly divisible by the value given in order for the swap to be able to take place. Reversing takes place before the interleaving is performed. </p>
<p> This option is used typically in generating <font SIZE="-1">ROM</font> images for problematic target systems. For example, on some target boards, the 32-bit words fetched from 8-bit ROMs are re-assembled in little-endian byte order regardless of the <font SIZE="-1">CPU</font> byte order. Depending on the programming model, the endianness of the <font SIZE="-1">ROM</font> may need to be modified. </p>
<p> Consider a simple file with a section containing the following eight bytes: <tt>12345678</tt>. </p>
<p> Using <code>&#8211;reverse-bytes=2</code> for the above example, the bytes in the output file would be ordered <tt>21436587</tt>. </p>
<p> Using <code>&#8211;reverse-bytes=4</code> for the above example, the bytes in the output file would be ordered <tt>43218765</tt>. </p>
<p> By using <code>&#8211;reverse-bytes=2</code> for the above example, followed by <code>&#8211;reverse-bytes=4</code> on the output file, the bytes in the second output file would be ordered <tt>34127856</tt>.</p>
<dt><code>&#8211;srec-len=</code><i>ival</i></p>
<dd> Meaningful only for srec output. Set the maximum length of the Srecords being produced to <i>ival</i>. This length covers both address, data and crc fields.</p>
<dt><code>&#8211;srec-forceS3</code></p>
<dd> Meaningful only for srec output. Avoid generation of S1/S2 records, creating S3-only record format.</p>
<dt><code>&#8211;redefine-sym</code> <i>old</i><code>=</code><i>new</i></p>
<dd> Change the name of a symbol <i>old</i>, to <i>new</i>. This can be useful when one is trying link two things together for which you have no source, and there are name collisions.</p>
<dt><code>&#8211;redefine-syms=</code><i>filename</i></p>
<dd> Apply <code>&#8211;redefine-sym</code> to each symbol pair &quot;<i>old</i> <i>new</i>&quot; listed in the file <i>filename</i>. <i>filename</i> is simply a flat file, with one symbol pair per line. Line comments may be introduced by the hash character. This option may be given more than once.</p>
<dt><code>&#8211;weaken</code></p>
<dd> Change all global symbols in the file to be weak. This can be useful when building an object which will be linked against other objects using the <code>-R</code> option to the linker. This option is only effective when using an object file format which supports weak symbols.</p>
<dt><code>&#8211;keep-symbols=</code><i>filename</i></p>
<dd> Apply <code>&#8211;keep-symbol</code> option to each symbol listed in the file <i>filename</i>. <i>filename</i> is simply a flat file, with one symbol name per line. Line comments may be introduced by the hash character. This option may be given more than once.</p>
<dt><code>&#8211;strip-symbols=</code><i>filename</i></p>
<dd> Apply <code>&#8211;strip-symbol</code> option to each symbol listed in the file <i>filename</i>. <i>filename</i> is simply a flat file, with one symbol name per line. Line comments may be introduced by the hash character. This option may be given more than once.</p>
<dt><code>&#8211;strip-unneeded-symbols=</code><i>filename</i></p>
<dd> Apply <code>&#8211;strip-unneeded-symbol</code> option to each symbol listed in the file <i>filename</i>. <i>filename</i> is simply a flat file, with one symbol name per line. Line comments may be introduced by the hash character. This option may be given more than once.</p>
<dt><code>&#8211;keep-global-symbols=</code><i>filename</i></p>
<dd> Apply <code>&#8211;keep-global-symbol</code> option to each symbol listed in the file <i>filename</i>. <i>filename</i> is simply a flat file, with one symbol name per line. Line comments may be introduced by the hash character. This option may be given more than once.</p>
<dt><code>&#8211;localize-symbols=</code><i>filename</i></p>
<dd> Apply <code>&#8211;localize-symbol</code> option to each symbol listed in the file <i>filename</i>. <i>filename</i> is simply a flat file, with one symbol name per line. Line comments may be introduced by the hash character. This option may be given more than once.</p>
<dt><code>&#8211;globalize-symbols=</code><i>filename</i></p>
<dd> Apply <code>&#8211;globalize-symbol</code> option to each symbol listed in the file <i>filename</i>. <i>filename</i> is simply a flat file, with one symbol name per line. Line comments may be introduced by the hash character. This option may be given more than once.</p>
<dt><code>&#8211;weaken-symbols=</code><i>filename</i></p>
<dd> Apply <code>&#8211;weaken-symbol</code> option to each symbol listed in the file <i>filename</i>. <i>filename</i> is simply a flat file, with one symbol name per line. Line comments may be introduced by the hash character. This option may be given more than once.</p>
<dt><code>&#8211;alt-machine-code=</code><i>index</i></p>
<dd> If the output architecture has alternate machine codes, use the <i>index</i>th code instead of the default one. This is useful in case a machine is assigned an official code and the tool-chain adopts the new code, but other applications still depend on the original code being used. For <font SIZE="-1">ELF</font> based architectures if the <i>index</i> alternative does not exist then the value is treated as an absolute number to be stored in the e_machine field of the <font SIZE="-1">ELF</font> header.</p>
<dt><code>&#8211;writable-text</code></p>
<dd> Mark the output text as writable. This option isn&#8217;t meaningful for all object file formats.</p>
<dt><code>&#8211;readonly-text</code></p>
<dd> Make the output text write protected. This option isn&#8217;t meaningful for all object file formats.</p>
<dt><code>&#8211;pure</code></p>
<dd> Mark the output file as demand paged. This option isn&#8217;t meaningful for all object file formats.</p>
<dt><code>&#8211;impure</code></p>
<dd> Mark the output file as impure. This option isn&#8217;t meaningful for all object file formats.</p>
<dt><code>&#8211;prefix-symbols=</code><i>string</i></p>
<dd> Prefix all symbols in the output file with <i>string</i>.</p>
<dt><code>&#8211;prefix-sections=</code><i>string</i></p>
<dd> Prefix all section names in the output file with <i>string</i>.</p>
<dt><code>&#8211;prefix-alloc-sections=</code><i>string</i></p>
<dd> Prefix all the names of all allocated sections in the output file with <i>string</i>.</p>
<dt><code>&#8211;add-gnu-debuglink=</code><i>path-to-file</i></p>
<dd> Creates a .gnu_debuglink section which contains a reference to <i>path-to-file</i> and adds it to the output file.</p>
<dt><code>&#8211;keep-file-symbols</code></p>
<dd> When stripping a file, perhaps with <code>&#8211;strip-debug</code> or <code>&#8211;strip-unneeded</code>, retain any symbols specifying source file names, which would otherwise get stripped.</p>
<dt><code>&#8211;only-keep-debug</code></p>
<dd> Strip a file, removing contents of any sections that would not be stripped by <code>&#8211;strip-debug</code> and leaving the debugging sections intact. In <font SIZE="-1">ELF</font> files, this preserves all note sections in the output. </p>
<p> The intention is that this option will be used in conjunction with <code>&#8211;add-gnu-debuglink</code> to create a two part executable. One a stripped binary which will occupy less space in <font SIZE="-1">RAM</font> and in a distribution and the second a debugging information file which is only needed if debugging abilities are required. The suggested procedure to create these files is as follows:</p>
<dl>
<dt>
<dd>
<dl>
<dt>1.&lt;Link the executable as normal. Assuming that is is called&gt;</p>
<dd> <tt>&quot;foo&quot;</tt> then&#8230;</p>
<dt>1.&lt;Run &quot;objcopy &#8211;only-keep-debug foo foo.dbg&quot; to&gt;</p>
<dd> create a file containing the debugging info.</p>
<dt>1.&lt;Run &quot;objcopy &#8211;strip-debug foo&quot; to create a&gt;</p>
<dd> stripped executable.</p>
<dt>1.&lt;Run &quot;objcopy &#8211;add-gnu-debuglink=foo.dbg foo&quot;&gt;</p>
<dd> to add a link to the debugging info into the stripped executable.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Note&#8212;the choice of <tt>&quot;.dbg&quot;</tt> as an extension for the debug info file is arbitrary. Also the <tt>&quot;--only-keep-debug&quot;</tt> step is optional. You could instead do this:</p>
<dl>
<dt>1.&lt;Link the executable as normal.&gt;</p>
<dd>
<dt>1.&lt;Copy &quot;foo&quot; to &quot;foo.full&quot;&gt;</p>
<dd>
<dt>1.&lt;Run &quot;objcopy &#8211;strip-debug foo&quot;&gt;</p>
<dd>
<dt>1.&lt;Run &quot;objcopy &#8211;add-gnu-debuglink=foo.full foo&quot;&gt;</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd>
<p> i.e., the file pointed to by the <code>&#8211;add-gnu-debuglink</code> can be the full executable. It does not have to be a file created by the <code>&#8211;only-keep-debug</code> switch. </p>
<p> Note&#8212;this switch is only intended for use on fully linked files. It does not make sense to use it on object files where the debugging information may be incomplete. Besides the gnu_debuglink feature currently only supports the presence of one filename containing debugging information, not multiple filenames on a one-per-object-file basis.</dl>
<dt><code>&#8211;strip-dwo</code></p>
<dd> Remove the contents of all <font SIZE="-1">DWARF </font>.dwo sections, leaving the remaining debugging sections and all symbols intact. This option is intended for use by the compiler as part of the <code>-gsplit-dwarf</code> option, which splits debug information between the .o file and a separate .dwo file. The compiler generates all debug information in the same file, then uses the <code>&#8211;extract-dwo</code> option to copy the .dwo sections to the .dwo file, then the <code>&#8211;strip-dwo</code> option to remove those sections from the original .o file.</p>
<dt><code>&#8211;extract-dwo</code></p>
<dd> Extract the contents of all <font SIZE="-1">DWARF </font>.dwo sections. See the <code>&#8211;strip-dwo</code> option for more information.</p>
<dt><code>&#8211;file-alignment</code> <i>num</i></p>
<dd> Specify the file alignment. Sections in the file will always begin at file offsets which are multiples of this number. This defaults to 512. [This option is specific to <font SIZE="-1">PE</font> targets.]</p>
<dt><code>&#8211;heap</code> <i>reserve</i></p>
<dd>
<dt><code>&#8211;heap</code> <i>reserve</i><code>,</code><i>commit</i></p>
<dd> Specify the number of bytes of memory to reserve (and optionally commit) to be used as heap for this program. [This option is specific to <font SIZE="-1">PE</font> targets.]</p>
<dt><code>&#8211;image-base</code> <i>value</i></p>
<dd> Use <i>value</i> as the base address of your program or dll. This is the lowest memory location that will be used when your program or dll is loaded. To reduce the need to relocate and improve performance of your dlls, each should have a unique base address and not overlap any other dlls. The default is 0x400000 for executables, and 0x10000000 for dlls. [This option is specific to <font SIZE="-1">PE</font> targets.]</p>
<dt><code>&#8211;section-alignment</code> <i>num</i></p>
<dd> Sets the section alignment. Sections in memory will always begin at addresses which are a multiple of this number. Defaults to 0x1000. [This option is specific to <font SIZE="-1">PE</font> targets.]</p>
<dt><code>&#8211;stack</code> <i>reserve</i></p>
<dd>
<dt><code>&#8211;stack</code> <i>reserve</i><code>,</code><i>commit</i></p>
<dd> Specify the number of bytes of memory to reserve (and optionally commit) to be used as stack for this program. [This option is specific to <font SIZE="-1">PE</font> targets.]</p>
<dt><code>&#8211;subsystem</code> <i>which</i></p>
<dd>
<dt><code>&#8211;subsystem</code> <i>which</i><code>:</code><i>major</i></p>
<dd>
<dt><code>&#8211;subsystem</code> <i>which</i><code>:</code><i>major</i><code>.</code><i>minor</i></p>
<dd> Specifies the subsystem under which your program will execute. The legal values for <i>which</i> are <tt>&quot;native&quot;</tt>, <tt>&quot;windows&quot;</tt>, <tt>&quot;console&quot;</tt>, <tt>&quot;posix&quot;</tt>, <tt>&quot;efi-app&quot;</tt>, <tt>&quot;efi-bsd&quot;</tt>, <tt>&quot;efi-rtd&quot;</tt>, <tt>&quot;sal-rtd&quot;</tt>, and <tt>&quot;xbox&quot;</tt>. You may optionally set the subsystem version also. Numeric values are also accepted for <i>which</i>. [This option is specific to <font SIZE="-1">PE</font> targets.]</p>
<dt><code>&#8211;extract-symbol</code></p>
<dd> Keep the file&#8217;s section flags and symbols but remove all section data. Specifically, the option:</p>
<dl>
<dt>
<dd>
<dl>
<dt>*&lt;removes the contents of all sections;&gt;</p>
<dd>
<dt>*&lt;sets the size of every section to zero; and&gt;</p>
<dd>
<dt>*&lt;sets the file&#8217;s start address to zero.&gt;</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd>
<p> This option is used to build a <i>.sym</i> file for a VxWorks kernel. It can also be a useful way of reducing the size of a <code>&#8211;just-symbols</code> linker input file.</dl>
<dt><code>&#8211;compress-debug-sections</code></p>
<dd> Compress <font SIZE="-1">DWARF</font> debug sections using zlib.</p>
<dt><code>&#8211;decompress-debug-sections</code></p>
<dd> Decompress <font SIZE="-1">DWARF</font> debug sections using zlib.</p>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd> Show the version number of <code>objcopy</code>.</p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;verbose</code></p>
<dd> Verbose output: list all object files modified. In the case of archives, <code>objcopy -V</code> lists all members of the archive.</p>
<dt><code>&#8211;help</code></p>
<dd> Show a summary of the options to <code>objcopy</code>.</p>
<dt><code>&#8211;info</code></p>
<dd> Display a list showing all architectures and object formats available.</p>
<dt><code>@</code><i>file</i></p>
<dd> Read command-line options from <i>file</i>. The options read are inserted in place of the original @<i>file</i> option. If <i>file</i> does not exist, or cannot be read, then the option will be treated literally, and not removed. </p>
<p> Options in <i>file</i> are separated by whitespace. A whitespace character may be included in an option by surrounding the entire option in either single or double quotes. Any character (including a backslash) may be included by prefixing the character to be included with a backslash. The <i>file</i> may itself contain additional @<i>file</i> options; any such options will be processed recursively.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-ld/">ld</a></i>(1), <i><a href="/docs/linux/man/1-objdump/">objdump</a></i>(1), and the Info entries for <i>binutils</i>.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 1991-2014 Free Software Foundation, Inc. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with no Invariant Sections, with no Front-Cover Texts, and with no Back-Cover Texts. A copy of the license is included in the section entitled &#8220;<font SIZE="-1">GNU</font> Free Documentation License&#8221;. </p>
<h2>Index</h2>
