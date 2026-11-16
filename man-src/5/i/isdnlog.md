---
title: "isdnlog(5)"
name: "isdnlog"
section: "5"
letter: "i"
url: "/docs/linux/man/5-isdnlog/"
description: "/var/log/isdn.log – isdn log file"
---

<p>/var/log/isdn.log &#8211; isdn log file</p>
<h2>Description</h2>
<p>The main purpose of <code>isdnlog</code> is to create a log file with information about all incoming and outgoing calls, namely: this file. The file has 19 fields, separated by pipe characters &quot;|&quot; with fixed length. The fields are:</p>
<dl>
<dt>
&nbsp;<wbr>1</dt>
<dd>Time of connect</dd>
<dt>
&nbsp;<wbr>2</dt>
<dd>Caller&#8217;s number (if transmitted)</dd>
<dt>
&nbsp;<wbr>3</dt>
<dd>Called number</dd>
<dt>
&nbsp;<wbr>4</dt>
<dd>Duration of connection in seconds</dd>
<dt>
&nbsp;<wbr>5</dt>
<dd>Duration of connection in 1/100 seconds</dd>
<dt>
&nbsp;<wbr>6</dt>
<dd>Time of connect (as usual in seconds since 1970)</dd>
<dt>
&nbsp;<wbr>7</dt>
<dd>Number of charge signals received (-1 if you don&#8217;t get charge signals)</dd>
<dt>
&nbsp;<wbr>8</dt>
<dd>I = Incoming or O = Outgoing</dd>
<dt>
&nbsp;<wbr>9</dt>
<dd>Cause Code if connection was not established</dd>
<dt>10</dt>
<dd>Number of bytes transferred (incoming)</dd>
<dt>11</dt>
<dd>Number of bytes transferred (outgoing)</dd>
<dt>12</dt>
<dd>Version number of <code>isdnlog</code></dd>
<dt>13</dt>
<dd>ISDN Service Code</dd>
<dt>14</dt>
<dd>1 = called by isdn user, 0 = called by analog user</dd>
<dt>15</dt>
<dd>Costs per charge unit (e.g. 0.062 in Germany)</dd>
<dt>16</dt>
<dd>Currency of charge unit (e.g. EUR in most parts of Europe)</dd>
<dt>17</dt>
<dd>Total cost of connection</dd>
<dt>18</dt>
<dd>Provider</dd>
<dt>19</dt>
<dd>Zone </dd>
<h2>Files</h2>
<dl>
<dt><i>/var/log/isdn.log</i></dt>
<dd>This file: isdnlog log file. </dd>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-isdnlog/">isdnlog</a></code>(8) </p>
<h2>Author</h2>
<p>This manual page was written by Andreas Jellinghaus &lt;aj [at] dungeon.inka.de&gt;, for Debian GNU/Linux and isdn4linux.<br />
 Now maintained by Paul Slootman &lt;paul [at] debian.org&gt;.</p>
</dl>