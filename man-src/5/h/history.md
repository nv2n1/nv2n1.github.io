---
title: "history(5)"
name: "history"
section: "5"
letter: "h"
url: "/docs/linux/man/5-history/"
---

history - record of current and recently expired Usenet articles

<h2>Description</h2>

The file <i>&lt;pathdb in inn.conf&gt;/history</i> keeps a record of all articles currently stored in the news system, as well as those that have been received but since expired. In a typical production environment, this file will be many megabytes. 

 The file consists of text lines. Each line corresponds to one article. The file is normally kept sorted in the order in which articles are received, although this is not a requirement. <i><a HREF="/docs/linux/man/8-innd/">Innd</a></i>(8) appends a new line each time it files an article, and <i><a HREF="/docs/linux/man/8-expire/">expire</a></i>(8) builds a new version of the file by removing old articles and purging old entries. 

 Each line consists of two or three fields separated by a tab, shown below as <i>\t</i>:
<dl><dd><pre>[Hash] \t date
[Hash] \t date \t token</pre></dl>
 

 The <i>Hash</i> field is the ASCII representation of the hash of the Message-ID header. This is directly used for the key of the <i><a HREF="/docs/linux/man/3-dbz/">dbz</a></i>(3). 

 The <i>date</i> field consists of three sub-fields separated by a tilde. All sub-fields are the text representation of the number of seconds since the epoch --- <i>i.e.</i>, a <i>time_t</i>; see <i><a HREF="/docs/linux/man/2-gettimeofday/">gettimeofday</a></i>(2). The first sub-field is the article's arrival date. If copies of the article are still present then the second sub-field is either the value of the article's Expires header, or a hyphen if no expiration date was specified. If an article has been expired then the second sub-field will be a hyphen. The third sub-field is the value of the article's Date header, recording when the article was posted. 

 The <i>token</i> field is a token of the article. This field is empty if the article has been expired. 

 For example, an article whose Message-ID was &lt;7q2saq$sal$1@isrv4.pa.vix.com&gt;, posted on 26 Aug 1999 08:02:34 GMT and recieved at 26 Aug 1999 08:06:54 GMT, could have a history line (broken into three lines for display) like the following:
<dl><dd><pre>[E6184A5BC2898A35A3140B149DE91D5C] \t
 935678987~-~935678821 \t
 @030154574F00000000000007CE3B000004BA@</pre></dl>
 

 In addition to the text file, there is a <i><a HREF="/docs/linux/man/3-dbz/">dbz</a></i>(3) database associated with the file that uses the Message-ID field as a key to determine the offset in the text file where the associated line begins. For historical reasons, the key includes the trailing \0 byte (which is not stored in the text file).

<h2>History</h2>

Written by Rich $alz &lt;rsalz [at] uunet.uu.net&gt; for InterNetNews. This is revision 3782, dated 2000-08-17.

<h2>See Also</h2>

<a HREF="/docs/linux/man/3-dbz/">dbz</a>(3), <a HREF="/docs/linux/man/8-expire/">expire</a>(8), <a HREF="/docs/linux/man/5-inn-conf/">inn.conf</a>(5), <a HREF="/docs/linux/man/8-innd/">innd</a>(8), <a HREF="/docs/linux/man/8-makehistory/">makehistory</a>(8). 
