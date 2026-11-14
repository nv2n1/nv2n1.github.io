---
title: "cntlist(5)"
name: "cntlist"
section: "5"
letter: "c"
url: "/docs/linux/man/5-cntlist/"
description: "cntlist – file listing number of times each tagged sense occurs in a semantic concordance, sorted most to least frequently tagged"
---

<p>cntlist &#8211; file listing number of times each tagged sense occurs in a semantic concordance, sorted most to least frequently tagged </p>
<p> cntlist.rev &#8211; file listing number of times each tagged sense occurs in a semantic concordance, sorted by sense key</p>
<h2>Description</h2>
<p>A cntlist file for a semantic concordance lists the number of times each semantically tagged sense occurs in the concordance and its sense number in the WordNet database. Each line in the file corresponds to a sense in the WordNet database to which at least one semantic tag points. Only senses that are tagged in a concordance are in the concordance&#8217;s cntlist file.</p>
<h3>WordNet Database <i>cntlist</i> File</h3>
<p>In the WordNet database, words are assigned sense numbers based on frequency of use in semantically tagged corpora. The cntlist file used by <code><a href="/docs/linux/man/1-grind/">grind</a></code>(1) to build the WordNet database and assign the sense numbers is a union of the cntlist files from the various semantic concordances that were formerly released by Princeton University. This combined cntlist file is provided with the WordNet package and is found in the <code>WNSEARCHDIR</code> directory. The <i>cntlist.rev</i> file is used at run-time by the WordNet library code and browser interfaces to print in the output display the number of times each sense has been tagged.</p>
<h3>File Format</h3>
<p>Each line in a cntlist file contains information for one sense. The file is ordered from most to least frequently tagged sense. The fields are separated by one space, and each line is terminated with a newline character. Senses having the same <i>tag_cnt</i> value are listed in reverse alphabetical order of the <i>lemma</i> field of the <i>sense_key</i>. Each line in <code>cntlist</code> is of the form:</p>
<dl>
<dd><i>tag_cnt~~sense_key~~sense_number</i></dl>
<p> where <i>tag_cnt</i> is the decimal number of times the sense is tagged in the corresponding semantic concordance. <i>sense_key</i> is a WordNet sense encoding and <i>sense_number</i> is a WordNet sense number as described in The <i>cntlist.rev</i> file contains the same fields described above, in the following order:</p>
<dl>
<dd><i>sense_key~~sense_number~~tag_cnt</i></dl>
<h2>Notes</h2>
<p>Princeton no longer maintains or releases the Semantic Concordance files. The <i>cntlist</i> file used to order the senses in WordNet 3.0 was generated from the Semantic Concordance files at the point that they were last updated in 2001. In general, the order of senses presented usually reflects what the user would expect, however sense ordering is now less reliable than in prior releases and should not be construed as an accurate indicator of frequency of use.</p>
<h2>Environment Variables (Unix)</h2>
<dl>
<dt><code>WNHOME</code></p>
<dd>Base directory for WordNet. Default is <code>/usr/local/WordNet-3.0</code>.</p>
<dt><code>WNSEARCHDIR</code></p>
<dd>Directory in which the WordNet database has been installed. Default is <code>WNHOME/dict</code>.</dl>
<h2>Registry (Windows)</h2>
<dl>
<dt><code>HKEY_LOCAL_MACHINE\SOFTWARE\WordNet\3.0\WNHome</code></p>
<dd>Base directory for WordNet. Default is <code>C:\Program~Files\WordNet\3.0</code>.</p>
<dt><code>HKEY_CURRENT_USER\SOFTWARE\WordNet\3.0\wnres</code></p>
<dd>User&#8217;s default browser options.</dl>
<h2>Files</h2>
<dl>
<dt><code>cntlist, cntlist.rev</code></p>
<dd>file of combined semantic concordance <code>cntlist</code> files. Used to assign sense numbers in WordNet database</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-grind/">grind</a></code>(1), <code><a href="/docs/linux/man/5-wnintro/">wnintro</a></code>(5), <code><a href="/docs/linux/man/5-senseidx/">senseidx</a></code>(5). </p>
