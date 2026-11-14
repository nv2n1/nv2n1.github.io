---
title: "flasm(1)"
name: "flasm"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flasm/"
description: "flasm – A swf bytecode assembler/disassembler"
---

<h2>NAME</h2>
<p> flasm &#8211; A swf bytecode assembler/disassembler</p>
<h2>SYNOPSIS</h2>
<p> <code>flasm</code> [<code>-daubzx</code>] <i>filename</i></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code></p>
<dd> Disassemble the given <font SIZE="-1">SWF</font> file to the console</p>
<dt><code>-a</code></p>
<dd> Assemble the given flasm project</p>
<dt><code>-u</code></p>
<dd> Update <font SIZE="-1">SWF</font>, replace flasm macros</p>
<dt><code>-b</code></p>
<dd> generate __bytecode__ instruction or byte sequence</p>
<dt><code>-z</code></p>
<dd> ompress <font SIZE="-1">SWF</font> with Zlib</p>
<dt><code>-x</code></p>
<dd> Decompress <font SIZE="-1">SWF</font></dl>
<h2>EXAMPLES</h2>
<p> <i>flasm</i> <code>-d</code> foo.swf </p>
<p> Disassemble foo.swf to the console. To see action offsets in disassembly set showoffset and hexoffset options in <code>flasm.ini</code>. </p>
<p> <i>flasm</i> <code>-d</code> foo.swf &gt; foo.flm </p>
<p> Disassemble foo.swf, redirect the output to foo.flm. Alternatively you can simply call <i>flasm</i> without command: <i>flasm</i> foo.swf creates foo.flm in the same directory. </p>
<p> <i>flasm</i> <code>-a</code> foo.flm </p>
<p> Assemble foo.flm and update the <font SIZE="-1">SWF</font> defined inside. The backup of original <font SIZE="-1">SWF</font> is created with .$wf extension. </p>
<p> <i>flasm</i> <code>-u</code> foo.swf </p>
<p> Disassemble foo.swf to the temporary file. Execute <i>flasm</i> macros embedded in <font SIZE="-1">SWF</font>. Make trivial optimizations automatically: remove double nots, replace 0.0 with 0, rebuild constant pools, clear register arguments. Create .$wf backup, update the original <font SIZE="-1">SWF</font>. </p>
<p> It&#8217;s a good idea to update the final version of <font SIZE="-1">SWF</font> with <i>flasm</i> -u. Don&#8217;t expect the <font SIZE="-1">SWF</font> to be noticeably faster, it will just make it a bit smaller. </p>
<p> <i>flasm</i> <code>-b</code> foo.txt </p>
<p> produce __bytecode__ instruction or byte sequence, depending on boutput setting in <code>flasm.ini</code>. Takes as input a simple action list without any movie or frame declarations. Output is sent to console. Redirect it to file if you wish: <i>flasm</i> -b foo.txt &gt; foo.as When boutput is set to 1, <i>Flasm</i> produces binary output </p>
<p> <i>flasm</i> <code>-x</code> foo.swf </p>
<p> Decompress foo.swf, create .$wf backup. </p>
<p> <i>flasm</i> <code>-z</code> foo.swf </p>
<p> Compress foo.swf, create .$wf backup. Source <font SIZE="-1">SWF</font> doesn&#8217;t have to be Flash <font SIZE="-1">MX/MX</font> 2004 file. However, only Flash <font SIZE="-1">MX/MX</font> 2004 player will be able to play the resulting compressed file. </p>
<p> <i>flasm</i> settings are read from <code>flasm.ini</code>. There aren&#8217;t many of them, and they are commented. You may, for example, switch bytecode offsets on and off there.</p>
<h2>DESCRIPTION</h2>
<p> <i>flasm</i> disassembles your entire <font SIZE="-1">SWF</font> including all the timelines and events. Looking at disassembly, you learn how the Flash compiler works, which improves your ActionScript skills. You can also do some optimizations on the disassembled code by hand or adjust the code as you wish. <i>flasm</i> then applies your changes to the original <font SIZE="-1">SWF</font>, replacing original actions. </p>
<p> It&#8217;s also possible to embed <i>flasm</i> actions in your ActionScript, making optimizing of large projects more comfortable. <i>flasm</i> is not a decompiler. What you get is the human readable representation of <font SIZE="-1">SWF</font> bytecodes, not ActionScript source. If you&#8217;re looking for a decompiler, Flare may suit your needs. However, Flare can&#8217;t alter the <font SIZE="-1">SWF</font>.</p>
<h2>URL</h2>
<p> <i><a rel="nofollow" href="http://www.nowrap.de/flasm.html">http://www.nowrap.de/flasm.html</a></i></p>
<h2>AUTHORS</h2>
<p> Copyright (c) 2001 Opaque Industries<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(c)&nbsp;<wbr>2002-2004 Igor Kogan </p>
<p> All rights reserved. See <font SIZE="-1">LICENSE</font>.TXT for terms of use. </p>
<h2>Index</h2>
