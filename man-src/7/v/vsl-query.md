---
title: "vsl-query(7)"
name: "vsl-query"
section: "7"
letter: "v"
url: "/docs/linux/man/7-vsl-query/"
---

Varnish VSL Query Expressions -

<h2>Overview</h2>

The Varnish VSL Query Expressions extracts transactions from the Varnish shared memory log, and perform queries on the transactions before reporting matches. 

 A transaction is a set of log lines that belongs together, e.g. a client request or a backend request. The API monitors the log, and collects all log records that make up a transaction before reporting on that transaction. Transactions can also be grouped, meaning backend transactions are reported together with the client transaction that initiated it. 

 A query is run on a group of transactions. A query expression is true if there is a log record within the group that satisfies the condition. It is false only if none of the log records satisfies the condition. Query expressions can be combined using boolean functions.

<h2>Grouping</h2>

When grouping transactions, there is a hierarchy structure showing which transaction initiated what. The level increases by one by an 'initiated by' relation, so for example a backend transaction will have one higher level than the client transaction that initiated it on a cache miss. Request restart transactions does not have it's level increased. This is to help predicting the level for a given transaction. 

 Levels start counting at 1, except when using raw where it will always be 0. 

 The grouping modes are:
<dl><dt>&bull;
<dd>Session 

 All transactions initiated by a client connection are reported together. All log data is buffered until the client connection is closed, which can cause session grouping mode to potentially consume a lot of memory.
<dt>&bull;
<dd>Request 

 Transactions are grouped by request, where the set will include the request itself as well as any backend requests or ESI-subrequests. Session data is not reported. This is the default.
<dt>&bull;
<dd>VXID 

 Transactions are not grouped, so each VXID is reported in it's entirety. Sessions, requests, ESI-requests and backend requests are all reported individually. Non-transactional data is not reported (VXID == 0).
<dt>&bull;
<dd>Raw 

 Every log record will make up a transaction of it's own. All data, including non-transactional data will be reported. 

 Example transaction hierarchy 

 <pre>Lvl 1: Client request (cache miss)
 Lvl 2: Backend request
 Lvl 2: ESI subrequest (cache miss)
 Lvl 3: Backend request
 Lvl 3: Backend request (VCL restart)
 Lvl 3: ESI subrequest (cache miss)
 Lvl 4: Backend request
 Lvl 2: ESI subrequest (cache hit)</pre></dl>

<h2>Query Language</h2>

A query expression consists of record selection criteria, and optionally an operator and a value to match against the selected records. 

 <pre>&lt;record selection criteria&gt; &lt;operator&gt; &lt;operand&gt;</pre>

<h3>Record selection criteria</h3>

The record selection criteria determines what kind records from the transaction group the expression applies to. Syntax: 

 <pre>{level}taglist:record-prefix[field]</pre>Taglist is mandatory, the other components are optional. 

 The level limits the expression to a transaction at that level. If left unspecified, the expression is applied to transactions at all levels. Level is a positive integer or zero. If level is followed by a '+' character, it expresses greater than or equal. If level is followed by a '-', it expresses less than or equal. 

 The taglist is a comma-separated list of VSL record tags that this expression should be checked against. Each list element can be a tag name or a tag glob. Globs allow a '*' either in the beginning of the name or at the end, and will select all tags that match either the prefix or subscript. A single '*' will select all tags. 

 The record prefix will further limit the matches to those records that has this prefix as it's first part of the record content followed by a colon. The part of the log record matched against will then be limited to what follows the prefix and colon. This is useful when matching against specific HTTP headers. The record prefix matching is done case insensitive. 

 The field will, if present, treat the log record as a white space separated list of fields, and only the nth part of the record will be matched against. Fields start counting at 1. 

 An expression using only a record selection criteria will be true if there is any record in the transaction group that is selected by the criteria.

<h3>Operators</h3>

The following matching operators are available:
<dl><dt>&bull;
<dd>== != &lt; &lt;= &gt; &gt;= 

 Numerical comparison. The record contents will be converted to either an integer or a float before comparison, depending on the type of the operand.
<dt>&bull;
<dd>eq ne 

 String comparison. 'eq' tests string equality, 'ne' tests for not equality.
<dt>&bull;
<dd>~ !~ 

 Regular expression matching. '~' is a positive match, '!~' is a non-match.</dl>

<h3>Operand</h3>

The operand is the value the selected records will be matched against. 

 An operand can be quoted or unquoted. Quotes can be either single or double quotes, and for quoted operands a backslash can be used to escape the quotes. 

 Unquoted operands can only consist of the following characters: 

 <pre>a-z A-Z 0-9 + - _ . *</pre>The following types of operands are available:
<dl><dt>&bull;
<dd>Integer 

 A number without any fractional part, valid for the numerical comparison operators. The integer type is used when the operand does not contain any period (.) characters.
<dt>&bull;
<dd>Float 

 A number with a fractional part, valid for the numerical comparison operators. The float type is used when the operand does contain a period (.) character.
<dt>&bull;
<dd>String 

 A sequence of characters, valid for the string equality operators.
<dt>&bull;
<dd>Regular expression 

 A PCRE regular expression. Valid for the regular expression operators.</dl>

<h3>Boolean functions</h3>

Query expressions can be linked together using boolean functions. The following are available, in decreasing precedence:
<dl><dt>&bull;
<dd>not &lt;expr&gt; 

 Inverts the result of &lt;expr&gt;
<dt>&bull;
<dd>&lt;expr1&gt; and &lt;expr2&gt; 

 True only if both expr1 and expr2 are true
<dt>&bull;
<dd>&lt;expr1&gt; or &lt;expr2&gt; 

 True if either of expr1 or expr2 is true 

 Expressions can be grouped using parenthesis.</dl>

<h2>Query Expression Examples</h2>

<dl><dt>&bull;
<dd>Transaction group contains a request URL that equals to &quot;/foo&quot; 

 <pre>ReqURL eq &quot;/foo&quot;</pre><dt>&bull;
<dd>Transaction group contains a request cookie header 

 <pre>ReqHeader:cookie</pre><dt>&bull;
<dd>Transaction group doesn't contain a request cookie header 

 <pre>not ReqHeader:cookie</pre><dt>&bull;
<dd>Transaction group contains a request user-agent header that contains &quot;iPod&quot; and the request delivery time exceeds 1 second 

 <pre>ReqHeader:user-agent ~ &quot;iPod&quot; and ReqEnd[5] &gt; 1.</pre><dt>&bull;
<dd>Transaction group contains a backend response status larger than or equal to 500 

 <pre>BerespStatus &gt;= 500</pre><dt>&bull;
<dd>Transaction group contains a request response status of 304, but where the request did not contain an if-modified-since header 

 <pre>ReqStatus == 304 and not ReqHeader:if-modified-since</pre><dt>&bull;
<dd>Transactions that have had backend failures or long delivery time on their ESI subrequests. (Assumes request grouping mode). 

 <pre>BerespStatus &gt;= 500 or {2+}ReqEnd[5] &gt; 1.</pre></dl>

<h2>History</h2>

This document was written by Martin Blix Grydeland.
