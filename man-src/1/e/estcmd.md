---
title: "estcmd(1)"
name: "estcmd"
section: "1"
letter: "e"
url: "/docs/linux/man/1-estcmd/"
description: "estcmd – command line interface of the core API"
---

<h2 class="name">NAME</h2>
<p> estcmd &#8211; command line interface of the core API</p>
<h2>SYNOPSIS</h2>
<p> <code>estcmd create [-tr] [-apn|-acc] [-xs|-xl|-xh|-xh2|-xh3] [-sv|-si|-sa] [-attr name type] db</code> </p>
<p> <code>estcmd put [-tr] [-cl] [-ws] [-apn|-acc] [-xs|-xl|-xh||-xh2|-xh3] [-sv|-si|-sa] db [file]</code> </p>
<p> <code>estcmd out [-cl] [-pc enc] db expr</code> </p>
<p> <code>estcmd edit [-pc enc] db expr name [value]</code> </p>
<p> <code>estcmd get [-nl|-nb] [-pidx path] [-pc enc] db expr [attr]</code> </p>
<p> <code>estcmd list [-nl|-nb] [-lp] db</code> </p>
<p> <code>estcmd uriid [-nl|-nb] [-pidx path] [-pc enc] db expr</code> </p>
<p> <code>estcmd meta db [name [value]]</code> </p>
<p> <code>estcmd inform [-nl|-nb] db</code> </p>
<p> <code>estcmd optimize [-onp] [-ond] db</code> </p>
<p> <code>estcmd merge [-cl] db target</code> </p>
<p> <code>estcmd repair [-rst|-rsh] db</code> </p>
<p> <code>estcmd search [-nl|-nb] [-pidx path] [-ic enc] [-vu|-va|-vf|-vs|-vh|-vx|-dd] [-sn wnum hnum anum] [-kn num] [-um] [-ec rn] [-gs|-gf|-ga] [-cd] [-ni] [-sf|-sfr|-sfu|-sfi] [-hs] [-attr expr] [-ord expr] [-max num] [-sk num] [-aux num] [-dis name] [-sim id] db [phrase]</code> </p>
<p> <code>estcmd gather [-tr] [-cl] [-ws] [-no] [-fe|-ft|-fh|-fm] [-fx sufs cmd] [-fz] [-fo] [-rm sufs] [-ic enc] [-il lang] [-bc] [-lt num] [-lf num] [-pc enc] [-px name] [-aa name value] [-apn|-acc] [-xs|-xl|-xh|-xh2|-xh3] [-sv|-si|-sa] [-ss name] [-sd] [-cm] [-cs num] [-ncm] [-kn num] [-um] db [file|dir]</code> </p>
<p> <code>estcmd purge [-cl] [-no] [-fc] [-pc enc] [-attr expr] db [prefix]</code> </p>
<p> <code>estcmd extkeys [-no] [-fc] [-dfdb file] [-ncm] [-ni] [-kn num] [-um] [-attr expr] db [prefix]</code> </p>
<p> <code>estcmd words [-nl|-nb] [-dfdb file] [-kw|-kt] db</code> </p>
<p> <code>estcmd draft [-ft|-fh|-fm] [-ic enc] [-il lang] [-bc] [-lt num] [-kn num] [-um] [file]</code> </p>
<p> <code>estcmd break [-ic enc] [-il lang] [-apn|-acc] [-wt] [file]</code> </p>
<p> <code>estcmd iconv [-ic enc] [-il lang] [-oc enc] [file]</code> </p>
<p> <code>estcmd regex [-inv] [-repl str] expr [file]</code> </p>
<p> <code>estcmd scandir [-tf|-td] [-pa|-pu] [dir]</code> </p>
<p> <code>estcmd multi [-db db] [-nl|-nb] [-ic enc] [-gs|-gf|-ga] [-cd] [-ni] [-sf|-sfr|-sfu|-sfi] [-hs] [-hu] [-attr expr] [-ord expr] [-max num] [-sk num] [-aux num] [-dis name] [phrase]</code> </p>
<p> <code>estcmd randput [-ren|-rla|-reu|-ror|-rjp|-rch] [-cs num] db dnum</code> </p>
<p> <code>estcmd wicked db dnum</code> </p>
<p> <code>estcmd regression db</code> </p>
<p> <code>estcmd version</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>estcmd</code> is an aggregation of sub commands. The name of a sub command is specified by the first argument. Other arguments are parsed according to each sub command. The argument <i>db</i> specifies the path of an index.</p>
<dl>
<dt><code>estcmd create [-tr] [-apn|-acc] [-xs|-xl|-xh|-xh2|-xh3] [-sv|-si|-sa] [-attr name type] db</code></p>
<dd> Create an index.<br />
 If <code>-tr</code> is specified, a new index is created regardless if one exists.<br />
 If <code>-apn</code> is specified, N-gram analysis is performed against European text also.<br />
 If <code>-acc</code> is specified, character category analysis is performed instead of N-gram analysis.<br />
 If <code>-xs</code> is specified, the index is tuned to register less than 50000 documents.<br />
 If <code>-xl</code> is specified, the index is tuned to register more than 300000 documents.<br />
 If <code>-xh</code> is specified, the index is tuned to register more than 1000000 documents.<br />
 If <code>-xh2</code> is specified, the index is tuned to register more than 5000000 documents.<br />
 If <code>-xh3</code> is specified, the index is tuned to register more than 10000000 documents.<br />
 If <code>-sv</code> is specified, scores are stored as void.<br />
 If <code>-si</code> is specified, scores are stored as 32-bit integer.<br />
 If <code>-sa</code> is specified, scores are stored as-is and marked not to be tuned when search.<br />
 <code>-attr</code> specifies an attribute index and its data type. This option can be specified multiple times.</p>
<dt><code>estcmd put [-tr] [-cl] [-apn|-acc] [-xs|-xl|-xh|-xh2|-xh3] [-sv|-si|-sa] db [file]</code></p>
<dd> Register a document of document draft to an index.<br />
 <i>file</i> specifies a target file. If it is omitted, the standard input is read.<br />
 If <code>-tr</code> is specified, a new index is created regardless if one exists.<br />
 If <code>-cl</code> is specified, regions of a overwritten document are cleaned up.<br />
 If <code>-ws</code> is specified, scores are weighted statically with score weighting attribute.<br />
 If <code>-apn</code> is specified, N-gram analysis is performed against European text also.<br />
 If <code>-acc</code> is specified, character category analysis is performed instead of N-gram analysis.<br />
 If <code>-xs</code> is specified, the index is tuned to register less than 50000 documents.<br />
 If <code>-xl</code> is specified, the index is tuned to register more than 300000 documents.<br />
 If <code>-xh</code> is specified, the index is tuned to register more than 1000000 documents.<br />
 If <code>-xh2</code> is specified, the index is tuned to register more than 5000000 documents.<br />
 If <code>-xh3</code> is specified, the index is tuned to register more than 10000000 documents.<br />
 If <code>-sv</code> is specified, scores are stored as void.<br />
 If <code>-si</code> is specified, scores are stored as 32-bit integer.<br />
 If <code>-sa</code> is specified, scores are stored as-is and marked not to be tuned when search.</p>
<dt><code>estcmd out [-pc enc] [-cl] db expr</code></p>
<dd> Remove information of a document from an index.<br />
 <i>expr</i> specifies the ID number, the URI, or the local path of a document.<br />
 If <code>-cl</code> is specified, regions of the document are cleaned up.<br />
 <code>-pc</code> specifies the encoding of file paths. By default, it is ISO-8859-1.</p>
<dt><code>estcmd edit [-pc enc] db expr name [value]</code></p>
<dd> Edit an attribute of a document in an index.<br />
 <i>expr</i> specifies the ID number, the URI, or the local path of a document.<br />
 <i>name</i> specifies the name of an attribute.<br />
 <i>value</i> specifies the value of the attribute. If it is omitted, the attribute is removed.<br />
 <code>-pc</code> specifies the encoding of the file path and the attribute value. By default, it is ISO-8859-1.</p>
<dt><code>estcmd get [-nl|-nb] [-pidx path] [-pc enc] db expr [attr]</code></p>
<dd> Output document draft of a document in an index.<br />
 <i>expr</i> specifies the ID number, the URI, or the local path of a document.<br />
 If <i>attr</i> is specified, only the value of the attribute is output.<br />
 If <code>-nl</code> is specified, the index is opened without file locking.<br />
 If <code>-nb</code> is specified, file locking is performed without blocking.<br />
 <code>-pidx</code> specifies the path of a pseudo index. This option can be specified multiple times.<br />
 <code>-pc</code> specifies the encoding of file paths. By default, it is ISO-8859-1.</p>
<dt><code>estcmd list [-nl|-nb] [-lp] db</code></p>
<dd> Output a list of all document in an index.<br />
 If <code>-nl</code> is specified, the index is opened without file locking.<br />
 If <code>-nb</code> is specified, file locking is performed without blocking.<br />
 If <code>-lp</code> is specified, local path equivalent to URL of &quot;file://&quot; is output.</p>
<dt><code>estcmd uriid [-nl|-nb] [-pidx path] [-pc enc] db expr</code></p>
<dd> Output the ID number of a document specified by URI.<br />
 <i>expr</i> specifies the URI or the local path of a document.<br />
 If <code>-nl</code> is specified, the index is opened without file locking.<br />
 If <code>-nb</code> is specified, file locking is performed without blocking.<br />
 <code>-pidx</code> specifies the path of a pseudo index. This option can be specified multiple times.<br />
 <code>-pc</code> specifies the encoding of file paths. By default, it is ISO-8859-1.</p>
<dt><code>estcmd meta db [name [value]]</code></p>
<dd> Handle meta data.<br />
 <i>name</i> specifies the name of a piece of meta data. If it is omitted, a list of all names is output.<br />
 <i>value</i> specifies the value of the meta data to be recorded. If it is omitted, the current value is output. If it is an empty string, the meta data is removed.</p>
<dt><code>estcmd inform [-nl|-nb] db</code></p>
<dd> Output the number of documents and the number of unique words in an index.<br />
 If <code>-nl</code> is specified, the index is opened without file locking.<br />
 If <code>-nb</code> is specified, file locking is performed without blocking.</p>
<dt><code>estcmd optimize [-onp] [-ond] db</code></p>
<dd> Optimize an index and clean up dispensable regions.<br />
 If <code>-onp</code> is specified, it is omitted to clean up dispensable regions.<br />
 If <code>-ond</code> is specified, it is omitted to optimize the database files.</p>
<dt><code>estcmd merge [-cl] db target</code></p>
<dd> Merge another index.<br />
 <i>target</i> specifies the path of another index.<br />
 If <code>-cl</code> is specified, regions of overwritten documents are cleaned up.</p>
<dt><code>estcmd repair [-rst|-rsh] db</code></p>
<dd> Repair a broken index.<br />
 If <code>-rst</code> is specified, strict consistency check is performed.<br />
 If <code>-rsh</code> is specified, consistency check is omitted.</p>
<dt><code>estcmd search [-nl|-nb] [-pidx path] [-ic enc] [-vu|-va|-vf|-vs|-vh|-vx|-dd] [-sn wnum hnum anum] [-kn num] [-um] [-ec rn] [-gs|-gf|-ga] [-cd] [-ni] [-sf|-sfr|-sfu|-sfi] [-hs] [-attr expr] [-ord expr] [-max num] [-sk num] [-aux num] [-dis name] [-sim id] db [phrase]</code></p>
<dd> Search an index for documents.<br />
 <i>phrase</i> specifies the search phrase.<br />
 If <code>-nl</code> is specified, the index is opened without file locking.<br />
 If <code>-nb</code> is specified, file locking is performed without blocking.<br />
 <code>-pidx</code> specifies the path of a pseudo index. This option can be specified multiple times.<br />
 <code>-ic</code> specifies the input encoding. By default, it is UTF-8.<br />
 If <code>-vu</code> is specified, TSV of ID number and URI are output.<br />
 If <code>-va</code> is specified, multipart format including attributes is output.<br />
 If <code>-vf</code> is specified, multipart format including document draft is output.<br />
 If <code>-vs</code> is specified, multipart format including attributes and snippets is output.<br />
 If <code>-vh</code> is specified, human readable format including attributes and snippets is output.<br />
 If <code>-vx</code> is specified, XML including including attributes and snippets is output.<br />
 If <code>-dd</code> is specified, document draft data are dumped and saved into separated files.<br />
 <code>-sn</code> specifies the number of whole width of snippet and width of strings picked up from the beginning of the text and width of strings picked up around each highlighted word.<br />
 <code>-kn</code> specifies the number of keywords to be extracted. By default, keyword extraction is not performed.<br />
 If <code>-um</code> is specified, morphological analyzers are used for keyword extraction.<br />
 <code>-ec</code> specifies lower limit of similarity eclipse.<br />
 If <code>-gs</code> is specified, every key of N-gram is checked. By default, it is alternately.<br />
 If <code>-gf</code> is specified, keys of N-gram are checked every three.<br />
 If <code>-ga</code> is specified, keys of N-gram are checked every four.<br />
 If <code>-cd</code> is specified, whether documents match the search phrase definitely is checked.<br />
 If <code>-ni</code> is specified, TF-IDF tuning is omitted.<br />
 If <code>-sf</code> is specified, the phrase is treated as a simplified form.<br />
 If <code>-sfr</code> is specified, the phrase is treated as a rough form.<br />
 If <code>-sfu</code> is specified, the phrase is treated as a union form.<br />
 If <code>-sfi</code> is specified, the phrase is treated as an intersection form.<br />
 If <code>-hs</code> is specified, score information is output as an attribute.<br />
 <code>-attr</code> specifies an attribute search condition. This option can be specified multiple times.<br />
 <code>-ord</code> specifies the order expression. By default, it is descending by score.<br />
 <code>-max</code> specifies the maximum number of shown documents. Negative means unlimited. By default, it is 10.<br />
 <code>-sk</code> specifies the number of documents to be skipped. By default, it is 0.<br />
 <code>-aux</code> specifies permission to adopt result of the auxiliary index. If it is not more than 0, the auxiliary index is not used. By default, it is 32.<br />
 <code>-dis</code> specifies the name of the distinct attribute.<br />
 <code>-sim</code> specifies the ID number of the seed document for similarity search.</p>
<dt><code>estcmd gather [-tr] [-cl] [-ws] [-no] [-fe|-ft|-fh|-fm] [-fx sufs cmd] [-fz] [-fo] [-rm sufs] [-ic enc] [-il lang] [-bc] [-lt num] [-lf num] [-pc enc] [-px name] [-aa name value] [-apn|-acc] [-xs|-xl|-xh|-xh2|-xh3] [-sv|-si|-sa] [-ss name] [-sd] [-cm] [-cs num] [-ncm] [-kn num] [-um] db [file|dir]</code></p>
<dd> Scan the local file system and register documents into an index.<br />
 If the third argument is the name of a file, a list of paths of target documents are read from it. If it is &quot;-&quot;, the standard input is specified.<br />
 If the third argument is the name of a directory. All files under the directory are treated as target documents.<br />
 If <code>-tr</code> is specified, a new index is created regardless if one exists.<br />
 If <code>-cl</code> is specified, regions of overwritten documents are cleaned up.<br />
 If <code>-ws</code> is specified, scores are weighted statically with score weighting attribute.<br />
 If <code>-no</code> is specified, operations are printed but not executed actually.<br />
 If <code>-fe</code> is specified, target files are treated as document draft. By default, the format is detected by the suffix of each document.<br />
 If <code>-ft</code> is specified, target files are treated as plain text.<br />
 If <code>-fh</code> is specified, target files are treated as HTML.<br />
 If <code>-fm</code> is specified, target files are treated as MIME.<br />
 If <code>-fx</code> is specified, target files with the specified suffixes are processed by the specified outer command. &quot;*&quot; matches any file. If the command is leaded by &quot;T@&quot;, the output of the command is treated as plain text. If the command is leaded by &quot;H@&quot;, the output of the command is treated as HTML. If the command is leaded by &quot;M@&quot;, the output of the command is treated as MIME. Else, the output is treated as document draft. This option can be specified multiple times.<br />
 If <code>-fz</code> is specified, documents which do not corresponding to the condition of <code>-fx</code> are ignored.<br />
 If <code>-fo</code> is specified, target files are not read. It is useful for efficient process of the outer command.<br />
 If <code>-rm</code> is specified, target files with the specified suffixes are removed. &quot;*&quot; matches any file. This option can be specified multiple times.<br />
 <code>-ic</code> specifies the input encoding. By default, it is detected automatically.<br />
 <code>-il</code> specifies the preferred input language. By default, English is preferred.<br />
 If <code>-bc</code> is specified, binary files are detected and ignored.<br />
 <code>-lt</code> specifies the text size limitation by kilo bytes. By default, it is 128KB. If it is negative, the size is unlimited.<br />
 <code>-lf</code> specifies the file size limitation by mega bytes. By default, it is 32MB. If it is negative, the size is unlimited.<br />
 <code>-pc</code> specifies the encoding of file paths. By default, it is ISO-8859-1.<br />
 <code>-px</code> specifies the name of an attribute read from the list of paths. As the list of paths can be in TSV format, the first field is treated as the path of a target document, the second field and the followers are definitions of attribute values. <code>-px</code> specifies the name of each values of the second field and the followers. This option can be specified multiple times.<br />
 <code>-aa</code> specifies the name and the value of an additional attribute. This option can be specified multiple times.<br />
 If <code>-apn</code> is specified, N-gram analysis is performed against European text also.<br />
 If <code>-acc</code> is specified, character category analysis is performed instead of N-gram analysis.<br />
 If <code>-xs</code> is specified, the index is tuned to register less than 50000 documents.<br />
 If <code>-xl</code> is specified, the index is tuned to register more than 300000 documents.<br />
 If <code>-xh</code> is specified, the index is tuned to register more than 1000000 documents.<br />
 If <code>-xh2</code> is specified, the index is tuned to register more than 5000000 documents.<br />
 If <code>-xh3</code> is specified, the index is tuned to register more than 10000000 documents.<br />
 If <code>-sv</code> is specified, scores are stored as void.<br />
 If <code>-si</code> is specified, scores are stored as 32-bit integer.<br />
 If <code>-sa</code> is specified, scores are stored as-is and marked not to be tuned when search.<br />
 <code>-ss</code> specifies the name of an attribute for substitute score.<br />
 If <code>-sd</code> is specified, the modification date of each file is recorded as an attribute.<br />
 If <code>-cm</code> is specified, documents whose modification date has not changed are ignored.<br />
 <code>-cs</code> specifies the size of cache memory by mega bytes. By default, it is 64MB.<br />
 If <code>-ncm</code> is specified, checking availability of the virtual memory is omitted.<br />
 <code>-kn</code> specifies the number of keywords to be extracted. By default, keyword extraction is not performed.<br />
 If <code>-um</code> is specified, morphological analyzers are used for keyword extraction.</p>
<dt><code>estcmd purge [-cl] [-no] [-fc] [-pc enc] [-attr expr] db [prefix]</code></p>
<dd> Purge information of documents which do not exist on the file system.<br />
 If <i>prefix</i> is specified, only documents whose URIs are begins with it. It can be specified by the local path of a directory.<br />
 If <code>-cl</code> is specified, regions of the deleted documents are cleaned up.<br />
 If <code>-no</code> is specified, operations are printed but not executed actually.<br />
 If <code>-fc</code> is specified, information of all target documents are deleted.<br />
 <code>-pc</code> specifies the encoding of file paths. By default, it is ISO-8859-1.<br />
 <code>-attr</code> specifies an attribute search condition. This option can be specified multiple times.</p>
<dt><code>estcmd extkeys [-no] [-fc] [-dfdb file] [-ncm] [-ni] [-kn num] [-um] [-attr expr] db [prefix]</code></p>
<dd> Create a database of keywords extracted from documents.<br />
 If <i>prefix</i> is specified, only documents whose URIs are begins with it.<br />
 If <code>-no</code> is specified, operations are printed but not executed actually.<br />
 If <code>-fc</code> is specified, all target documents are processed whichever they have existing records or not.<br />
 <code>-dfdb</code> specifies an outher database of document frequency. By default, document frequency is calculated dynamically according to the index.<br />
 If <code>-ncm</code> is specified, checking availability of the virtual memory is omitted.<br />
 If <code>-ni</code> is specified, TF-IDF tuning is omitted.<br />
 <code>-kn</code> specifies the number of keywords to be extracted. By default, it is 32.<br />
 If <code>-um</code> is specified, morphological analyzers are used for keyword extraction.<br />
 <code>-attr</code> specifies an attribute search condition. This option can be specified multiple times.</p>
<dt><code>estcmd words [-nl|-nb] [-dfdb file] [-kw|-kt] db</code></p>
<dd> Output a list of all unique words and each record size which is treated as docuemnt frequency.<br />
 If <code>-nl</code> is specified, the index is opened without file locking.<br />
 If <code>-nb</code> is specified, file locking is performed without blocking.<br />
 <code>-dfdb</code> specifies an outer database where the result is stored. By default, the result is output to the standard output as TSV. If the outer database already exists, the value of each record is incremented.<br />
 If <code>-kw</code> is specified, keywords and numbers of corresponding documents are output.<br />
 If <code>-kt</code> is specified, keywords and their related terms are output.</p>
<dt><code>estcmd draft [-ft|-fh|-fm] [-ic enc] [-il lang] [-bc] [-lt num] [-kn num] [-um] [file]</code></p>
<dd> For test and debug.</p>
<dt><code>estcmd break [-ic enc] [-il lang] [-apn|-acc] [-wt] [file]</code></p>
<dd> For test and debug.</p>
<dt><code>estcmd iconv [-ic enc] [-il lang] [-oc enc] [file]</code></p>
<dd> For test and debug.</p>
<dt><code>estcmd regex [-inv] [-repl str] expr [file]</code></p>
<dd> For test and debug.</p>
<dt><code>estcmd scandir [-tf|-td] [-pa|-pu] [dir]</code></p>
<dd> For test and debug.</p>
<dt><code>estcmd multi [-db db] [-nl|-nb] [-ic enc] [-gs|-gf|-ga] [-cd] [-ni] [-sf|-sfr|-sfu|-sfi] [-hs] [-hu] [-attr expr] [-ord expr] [-max num] [-sk num] [-aux num] [-dis name] [phrase]</code></p>
<dd> For test and debug.</p>
<dt><code>estcmd randput [-ren|-rla|-reu|-ror|-rjp|-rch] [-cs num] db dnum</code></p>
<dd> For test and debug.</p>
<dt><code>estcmd wicked db dnum</code></p>
<dd> For test and debug.</p>
<dt><code>estcmd regression db</code></p>
<dd> For test and debug.</p>
<dt><code>estcmd version</code></p>
<dd> Show the version information.</dl>
<p> All sub commands return 0 if the operation is success, else return 1. As for put, out, gather, purge, randput, wicked, and regression, they finish with closing the database when they catch the signal 1 (SIGHUP), 2 (SIGINT), 3 (SIGQUIT), 13 (SIGPIPE), or 15 (SIGTERM). </p>
<p> The data type of attribute indexes specified by <code>-attr</code> option of <code>create</code> sub command should be &quot;seq&quot; for sequencial type, &quot;str&quot; for string type, or &quot;num&quot; for number type. </p>
<p> Each pseudo index specified by <code>-pidx</code> option of <code>search</code> sub command and so on is a directory containing files of document draft. If you search a main index with pseudo indexes, meta search of the main index and pseudo indexes is performed. </p>
<p> The encoding name specified by <code>-ic</code> option should be such name registered to IETF as UTF-8, ISO-8859-1, and so on. The language name specified by <code>-il</code> option should be one of &quot;en&quot; (English), &quot;ja&quot; (Japanese, &quot;zh&quot; (Chinese), &quot;ko&quot; (Korean). </p>
<p> The outer command specified by -fx option of gather receives the path of the target document by the first argument and the path for output by the second argument. The original path of the target document is given as the value of the environment variable `ESTORIGFILE&#8217;. </p>
<p> Note that similarity search is very slow, by default. To improve the performance of similarity search, running &quot;estcmd extkeys&quot; beforehand is strongly recommended. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-estconfig/">estconfig</a></code>(1), <code><a href="/docs/linux/man/1-estmaster/">estmaster</a></code>(1), <code><a href="/docs/linux/man/1-estcall/">estcall</a></code>(1), <code><a href="/docs/linux/man/1-estwaver/">estwaver</a></code>(1), <code><a href="/docs/linux/man/3-estraier/">estraier</a></code>(3), <code><a href="/docs/linux/man/3-estnode/">estnode</a></code>(3) </p>
<p> Please see <code><a rel="nofollow" href="http://hyperestraier.sourceforge.net/uguide-en.html">http://hyperestraier.sourceforge.net/uguide-en.html</a></code> for detail. </p>
<h2>Index</h2>
