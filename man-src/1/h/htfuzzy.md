---
title: "htfuzzy(1)"
name: "htfuzzy"
section: "1"
letter: "h"
url: "/docs/linux/man/1-htfuzzy/"
description: "htfuzzy – fuzzy command-line search utility for the ht://Dig search engine"
---

<h2 class="name">NAME</h2>
<p> htfuzzy &#8211; fuzzy command-line search utility for the ht://Dig search engine </p>
<h2>SYNOPSIS</h2>
<p> <code>htfuzzy [-c configfile] [-v] algorithm</code> <i>[options]</i></p>
<h2>DESCRIPTION</h2>
<p> Description to follow here</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c </code><i>configfile</i></p>
<dd> Use the specified <i>configfile</i> instead of the default.</p>
<dt><code>-v </code></p>
<dd> <i>Verbose mode</i> <i> -vv</i> , <i>-vvv</i><br />
&nbsp;<wbr>etc ). Specifying more than two v&#8217;s is probably only useful for debugging purposes.</dl>
<h2>Supported Algorithms</h2>
<dl>
<dt>Different algoritms are supported for searching:</p>
<dd> <i>soundex</i> Creates a slightly modified soundex key database. Differences with the standard soundex algorithm are: Keys are 6 digits and the first letter is also encoded. <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><br />
 <i>metaphone</i> Creates a metaphone key database. This algorithm is more specific to English, but will get fewer &quot;weird&quot; matches than the soundex algorithm. </p>
<p> <i>accents</i> (No description of the algorithm at the moment) </p>
<p> <i>endings</i> Creates two databases which can be used to match common word endings. The creation of these databases requires a list of affix rules and a dictionary which uses those affix rules. The format of the affix rules and dictionary files are the ones used by the ispell program. Included with the distribution are the affix rules for English and a fairly small English dictionary. Other languages can be supported by getting the appropriate affix rules and dictionaries. These are available for many languages; check the ispell distribu- tion for more details. </p>
<p> <i>synonyms</i> Creates a database of synonyms for words. It reads a text database of synonyms and creates a database that htsearch can then use. Each line of the text database consists of words where the first word will have the other words on that line as synonyms. </p>
</dl>
<h2>Notes on searching</h2>
<dl>
<dt>Please consult specialised literature to find out how the different algorithms work or simply try another</p>
<dd> search stragegy you do not get the intended search results. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt><code>/etc/htdig/htdig.conf</code></p>
<dd> The default configuration file. <code>/var/lib/htdig/db.accents.db</code> (Output) Maps between characters with and without accents for accents fuzzy rule <code>/var/lib/htdig/db.metaphone.db</code> (Output) Database of similar-sounding words for metaphone fuzzy rule <code>/var/lib/htdig/db.soundex.db</code> (Output) Database of similar-sounding words for soundex fuzzy rule <code>/var/www/html/htdig/english.0, /var/www/html/htdig/english.aff</code> (Input) List of words and affix rules used to generate endings <code>/var/www/html/htdig/root2word.db, /var/www/html/htdig/word2rood.db</code> (Output) Database used for endings fuzzy rule <code>/var/www/html/htdig/synonyms</code> (Input) List of groups of words considered synonymous <code>/var/www/html/htdig/synonyms.db</code> (Output) Database used for synonyms fuzzy rule</dl>
<h2>SEE ALSO</h2>
<p> Please refer to the HTML pages (in the htdig-doc package) <code>/usr/share/doc/htdig-doc/html/index.html</code> and the manual pages <i><a href="/docs/linux/man/8-htdigconfig/">htdigconfig</a>(8)</i> , <i><a href="/docs/linux/man/1-htmerge/">htmerge</a>(1)</i> , <i><a href="/docs/linux/man/1-htnotify/">htnotify</a>(1)</i> , <i><a href="/docs/linux/man/1-htsearch/">htsearch</a>(1)</i> and <i><a href="/docs/linux/man/1-rundig/">rundig</a>(1)</i> for a detailed description of ht://Dig and its commands.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Robert Ribnitz. It is based on documentation of ht://Dig, and on earlier manpages provided by Christian Schwarz and Stijn de Bekker. </p>
<h2>Index</h2>
