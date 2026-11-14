---
title: "qsfilter2(1)"
name: "qsfilter2"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qsfilter2/"
---

<h2 class="name">NAME</h2>
 

 qsfilter2 - an utility to generate mod_qos request line rules out from existing access/audit log data. 

<h2>SYNOPSIS</h2>

 qsfilter2 -i &lt;path&gt; [-c &lt;path&gt;] [-d &lt;num&gt;] [-h] [-b &lt;num&gt;] [-p|-s|-m|-o] [-l &lt;len&gt;] [-n] [-e] [-u 'uni'] [-k &lt;prefix&gt;] [-t] [-f &lt;path&gt;] [-v 0|1|2]

<h2>DESCRIPTION</h2>

 mod_qos implements a request filter which validates each request line. The module supports both, negative and positive security model. The QS_Deny* directives are used to specify request line patterns which are not allowed to access the server (negative security model / blacklist). These rules are used to restrict access to certain resources which should not be available to users or to protect the server from malicious patterns. The QS_Permit* rules implement a positive security model (whitelist). These directives are used to define allowed request line patterns. Request which do not match any of thses patterns are not allowed to access the server. 

 qsfilter2 is an audit log analyzer used to generate filter rules (perl compatible regular expressions) which may be used by mod_qos to deny access for suspect requests (QS_PermitUri rules). It parses existing audit log files in order to generate request patterns covering all allowed requests.

<h2>OPTIONS</h2>

<dl>
<dt>-i &lt;path&gt;
<dd> Input file containing request URIs. The URIs for this file have to be extracted from the servers access logs. Each line of the input file contains a request URI consiting of a path and and query. 
&nbsp;<wbr>&nbsp;<wbr>Example: 
&nbsp;<wbr>/aaa/index.do 
&nbsp;<wbr>/aaa/edit?image=1.jpg 
&nbsp;<wbr>/aaa/image/1.jpg 
&nbsp;<wbr>/aaa/view?page=1 
&nbsp;<wbr>/aaa/edit?document=1 

 These access log data must include current request URIs but also request lines from previous rule generation steps. It must also include request lines which cover manually generated rules.
<dt>-c &lt;path&gt;
<dd> mod_qos configuration file defining QS_DenyRequestLine and QS_PermitUri directives. qsfilter2 generates rules from access log data automatically. Manually generated rules (QS_PermitUri) may be provided from this file. Note: each manual rule must be represented by a request URI in the input data (-i) in order to make sure not to be deleted by the rule optimisation algorithm. QS_Deny* rules from this file are used to filter request lines which should not be used for whitelist rule generation. 
&nbsp;<wbr>&nbsp;<wbr>Example: 
&nbsp;<wbr>#&nbsp;<wbr>manually defined whitelist rule: 
&nbsp;<wbr>QS_PermitUri&nbsp;<wbr>+view deny&nbsp;<wbr>&quot;^[/a-zA-Z0-9]+/view\?(page=[0-9]+)?$&quot; 
&nbsp;<wbr>#&nbsp;<wbr>filter unwanted request line patterns: 
&nbsp;<wbr>QS_DenyRequestLine&nbsp;<wbr>+printable deny&nbsp;<wbr>&quot;.*[\x00-\x19].*&quot; 

 

<dt>-d &lt;num&gt;
<dd> Depth (sub locations) of the path string which is defined as a literal string. Default is 1.
<dt>-h
<dd> Always use a string representing the handler name in the path even the url does not have a query. See also -d option.
<dt>-b &lt;num&gt;
<dd> Replaces url pattern by the regular expression when detecting a base64/hex encoded string. Detecting sensibility is defined by a numeric value. You should use values higher than 5 (default) or 0 to disable this function.
<dt>-p
<dd> Repesents query by pcre only (no literal strings).
<dt>-s
<dd> Uses one single pcre for the whole query string.
<dt>-m
<dd> Uses one pcre for multipe query values (recommended mode).
<dt>-o
<dd> Does not care the order of query parameters.
<dt>-l &lt;len&gt;
<dd> Outsizes the query length by the defined length ({0,size+len}), default is 10.
<dt>-n
<dd> Disables redundant rules elimination.
<dt>-e
<dd> Exit on error.
<dt>-u 'uni'
<dd> Enables additional decoding methods. Use the same settings as you have used for the QS_Decoding directive.
<dt>-p
<dd> Repesents query by pcre only (no literal strings). Determines the worst case performance for the generated whitelist by applying each rule for each request line (output is real time filter duration per request line in milliseconds).
<dt>-k &lt;prefix&gt;
<dd> Prefix used to generate rule identifiers (QSF by default).
<dt>-t
<dd> Calculates the maximal latency per request (worst case) using the generated rules.
<dt>-f &lt;path&gt;
<dd> Filters the input by the provided path (prefix) only processing matching lines.
<dt>-v &lt;level&gt;
<dd> Verbose mode. (0=silent, 1=rule source, 2=detailed). Default is 1. Don't use rules you haven't checked the request data used to generate it! Level 1 is highly recommended (as long as you don't have created the log data using your own web crawler).</dl>

<h2>OUTPUT</h2>

 The output of qsfilter2 is written to stdout. The output contains the generated QS_PermitUri directives but also information about the source which has been used to generate these rules. It is very important to check the validity of each request line which has been used to calculate the QS_PermitUri rules. Each request line which has been used to generate a new rule is shown in the output prefixed by &quot;ADD line &lt;line number&gt;:&quot;. These request lines should be stored and reused at any later rule generation (add them to the URI input file). The subsequent line shows the generated rule. At the end of data processing a list of all generated QS_PermitUri rules is shown. These directives may be used withn the configuration file used by mod_qos.

<h2>EXAMPLE</h2>

 
&nbsp;<wbr>&nbsp;<wbr>./qsfilter2 -i loc.txt -c httpd.conf -m -e 
&nbsp;<wbr>&nbsp;<wbr>... 
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>ADD line 1:&nbsp;<wbr>/aaa/index.do 
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>003&nbsp;<wbr>^(/[a-zA-Z0-9\-_]+)+[/]?\.?[a-zA-Z]{0,4}$ 
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>ADD line 3:&nbsp;<wbr>/aaa/view?page=1 
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>---&nbsp;<wbr>^[/a-zA-Z0-9]+/view\?(page=[0-9]+)?$ 
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>ADD line 4:&nbsp;<wbr>/aaa/edit?document=1 
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>004&nbsp;<wbr>^[/a-zA-Z]+/edit\?((document)(=[0-9]*)*[&amp;]?)*$ 
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>ADD line 5:&nbsp;<wbr>/aaa/edit?image=1.jpg 
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>005&nbsp;<wbr>^[/a-zA-Z]+/edit\?((image)(=[0-9\.a-zA-Z]*)*[&amp;]?)*$ 
&nbsp;<wbr>&nbsp;<wbr>... 
&nbsp;<wbr>&nbsp;<wbr>QS_PermitUri&nbsp;<wbr>+QSF001 deny&nbsp;<wbr>&quot;^[/a-zA-Z]+/edit\?((document|image)(=[0-9\.a-zA-Z]*)*[&amp;]?)*$&quot; 
&nbsp;<wbr>&nbsp;<wbr>QS_PermitUri&nbsp;<wbr>+QSF002 deny&nbsp;<wbr>&quot;^[/a-zA-Z0-9]+/view\?(page=[0-9]+)?$&quot; 
&nbsp;<wbr>&nbsp;<wbr>QS_PermitUri&nbsp;<wbr>+QSF003 deny&nbsp;<wbr>&quot;^(/[a-zA-Z0-9\-_]+)+[/]?\.?[a-zA-Z]{0,4}$&quot; 

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/1-qsexec/">qsexec</a>(1), <a HREF="/docs/linux/man/1-qsgeo/">qsgeo</a>(1), <a HREF="/docs/linux/man/1-qsgrep/">qsgrep</a>(1), <a HREF="/docs/linux/man/1-qshead/">qshead</a>(1), <a HREF="/docs/linux/man/1-qslog/">qslog</a>(1), <a HREF="/docs/linux/man/1-qslogger/">qslogger</a>(1), <a HREF="/docs/linux/man/1-qspng/">qspng</a>(1), <a HREF="/docs/linux/man/1-qsrotate/">qsrotate</a>(1), <a HREF="/docs/linux/man/1-qssign/">qssign</a>(1), <a HREF="/docs/linux/man/1-qstail/">qstail</a>(1)

<h2>AUTHOR</h2>

 Pascal Buchbinder, <a rel="nofollow" HREF="http://opensource.adnovum.ch/mod_qos/">http://opensource.adnovum.ch/mod_qos/</a> 

<h2>Index</h2>


