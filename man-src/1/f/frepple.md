---
title: "frepple(1)"
name: "frepple"
section: "1"
letter: "f"
url: "/docs/linux/man/1-frepple/"
description: "frepple – open source production planning and scheduling"
---

<h2>NAME</h2>
<p> frepple &#8211; open source production planning and scheduling </p>
<h2>SYNOPSIS</h2>
<p> <code>frepple [options]</code> <i>&lt;files&gt;</i><br />
 <code>frepple [options]</code> <i>&lt;directories&gt;</i><br />
 <code>frepple [options]</code> </p>
<h2>DESCRIPTION</h2>
<p> FrePPLe is an open source production planning and scheduling application. </p>
<p> This program reads XML input data, and also embeds a Python interpeter to execute instructions in the Python language. </p>
<p> The input data can be provided in the following ways:<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; Passing one or more XML files.<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; Passing one or more directories as arguments.<br />
&nbsp;<wbr>The program will process all files with the extension&nbsp;<wbr>&#8216;.xml&#8217;&nbsp;<wbr>found<br />
&nbsp;<wbr>in the directories in alphabetical order.<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; Passing one or more Python files with the extension&nbsp;<wbr>&#8216;.py&#8217;.<br />
&nbsp;<wbr>The Python commands are executed in the embedded interpreter.<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; When passing no file or directory arguments, input will be read<br />
&nbsp;<wbr>from the standard input. XML data can be redirected or piped to the<br />
&nbsp;<wbr>application. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-validate -v</code></p>
<dd> Validate the xml input for correctness.</p>
<dt><code>-check -c</code></p>
<dd> Only validate the input, without executing the content.</p>
<dt><code>-? -h -help</code></p>
<dd> Show instructions. </p>
</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt>FREPPLE_HOME</p>
<dd> Optionally points to a directory where the initialization files will be searched. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt>./init.xml $FREPPLE_HOME/init.xml /usr/share/frepple/init.xml</p>
<dd> XML data automatically loaded upon startup. The first file with the name init.xml in the above sequence is processed. </p>
<dt>./frepple.xsd $FREPPLE_HOME/frepple.xsd /usr/share/frepple/frepple.xsd</p>
<dd> XML Schema definition for validation of the XML input data. The first file with the name frepple.xsd in the above sequence is processed. </p>
<dt>./init.py $FREPPLE_HOME/init.py /usr/share/frepple/init.py</p>
<dd> Python commands executed automatically upon startup. The first file with the name init.py in the above sequence is processed. </p>
</dl>
<h2>RETURNS</h2>
<p> 0 when successful, non-zero in case of errors </p>
<h2>AUTHORS</h2>
<p> <code>FrePPLe</code> is developed as Open Source under the AGPL license, v3 or later. </p>
<p> The authors and contributors are listed on <a rel="nofollow" href="http://frepple.com.">http://frepple.com.</a> </p>
<h2>Index</h2>
