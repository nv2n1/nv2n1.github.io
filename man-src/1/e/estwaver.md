---
title: "estwaver(1)"
name: "estwaver"
section: "1"
letter: "e"
url: "/docs/linux/man/1-estwaver/"
description: "estwaver – command line interface of web crawler"
---

<h2 class="name">NAME</h2>
<p> estwaver &#8211; command line interface of web crawler</p>
<h2>SYNOPSIS</h2>
<p> <code>estwaver init [-apn|-acc] [-xs|-xl|-xh] [-sv|-si|-sa] rootdir</code> </p>
<p> <code>estwaver crawl [-restart|-revisit|-revcont] rootdir</code> </p>
<p> <code>estwaver unittest rootdir</code> </p>
<p> <code>estwaver fetch [-proxy hostr port] [-tout num] [-il lang] url</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>estwaver</code> is an aggregation of sub commands. The name of a sub command is specified by the first argument. Other arguments are parsed according to each sub command. The argument <i>rootdir</i> specifies the crawler root directory which contains configuration file and so on.</p>
<dl>
<dt><code>estwaver init [-apn|-acc] [-xs|-xl|-xh] [-sv|-si|-sa] rootdir</code></p>
<dd> Create the crawler root directory.<br />
 If <code>-apn</code> is specified, N-gram analysis is performed against European text also.<br />
 If <code>-acc</code> is specified, character category analysis is performed instead of N-gram analysis.<br />
 If <code>-xs</code> is specified, the index is tuned to register less than 50000 documents.<br />
 If <code>-xl</code> is specified, the index is tuned to register more than 300000 documents.<br />
 If <code>-xh</code> is specified, the index is tuned to register more than 1000000 documents.<br />
 If <code>-sv</code> is specified, scores are stored as void.<br />
 If <code>-si</code> is specified, scores are stored as 32-bit integer.<br />
 If <code>-sa</code> is specified, scores are stored as-is and marked not to be tuned when search.</p>
<dt><code>estwaver crawl [-restart|-revisit|-revcont] rootdir</code></p>
<dd> Start crawling.<br />
 If <code>-restart</code> is specified, crawling is restarted from the seed documents.<br />
 If <code>-revisit</code> is specified, collected documents are revisited.<br />
 If <code>-revcont</code> is specified, collected documents are revisited and then crawling is continued.&lt;/dd&gt;</p>
<dt><code>estwaver unittest rootdir</code></p>
<dd> Perform unit tests.</p>
<dt><code>estwaver fetch [-proxy hostr port] [-tout num] [-il lang] url</code></p>
<dd> Fetch a document.<br />
 <i>url</i> specifies the URL of a document.<br />
 <code>-proxy</code> specifies the host name and the port number of the proxy server.<br />
 <code>-tout</code> specifies timeout in seconds.<br />
 <code>-il</code> specifies the preferred language. By default, it is English.</dl>
<p> All sub commands return 0 if the operation is success, else return 1. A running crawler finishes with closing the database when it catches the signal 1 (SIGHUP), 2 (SIGINT), 3 (SIGQUIT), or 15 (SIGTERM). </p>
<p> When crawling finishes, there is a directory <code>_index</code> in the crawler root directory. It is an index available by <code>estcmd</code> and so on. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-estconfig/">estconfig</a></code>(1), <code><a href="/docs/linux/man/1-estcmd/">estcmd</a></code>(1), <code><a href="/docs/linux/man/1-estmaster/">estmaster</a></code>(1), <code><a href="/docs/linux/man/1-estcall/">estcall</a></code>(1), <code><a href="/docs/linux/man/3-estraier/">estraier</a></code>(3), <code><a href="/docs/linux/man/3-estnode/">estnode</a></code>(3) </p>
<h2>Index</h2>
