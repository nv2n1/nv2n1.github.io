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
&nbsp;<wbr>1</p>
<dd>Time of connect</p>
<dt>
&nbsp;<wbr>2</p>
<dd>Caller&#8217;s number (if transmitted)</p>
<dt>
&nbsp;<wbr>3</p>
<dd>Called number</p>
<dt>
&nbsp;<wbr>4</p>
<dd>Duration of connection in seconds</p>
<dt>
&nbsp;<wbr>5</p>
<dd>Duration of connection in 1/100 seconds</p>
<dt>
&nbsp;<wbr>6</p>
<dd>Time of connect (as usual in seconds since 1970)</p>
<dt>
&nbsp;<wbr>7</p>
<dd>Number of charge signals received (-1 if you don&#8217;t get charge signals)</p>
<dt>
&nbsp;<wbr>8</p>
<dd>I = Incoming or O = Outgoing</p>
<dt>
&nbsp;<wbr>9</p>
<dd>Cause Code if connection was not established</p>
<dt>10</p>
<dd>Number of bytes transferred (incoming)</p>
<dt>11</p>
<dd>Number of bytes transferred (outgoing)</p>
<dt>12</p>
<dd>Version number of <code>isdnlog</code></p>
<dt>13</p>
<dd>ISDN Service Code</p>
<dt>14</p>
<dd>1 = called by isdn user, 0 = called by analog user</p>
<dt>15</p>
<dd>Costs per charge unit (e.g. 0.062 in Germany)</p>
<dt>16</p>
<dd>Currency of charge unit (e.g. EUR in most parts of Europe)</p>
<dt>17</p>
<dd>Total cost of connection</p>
<dt>18</p>
<dd>Provider</p>
<dt>19</p>
<dd>Zone </p>
<h2>Files</h2>
<dl>
<dt><i>/var/log/isdn.log</i></p>
<dd>This file: isdnlog log file. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-isdnlog/">isdnlog</a></code>(8) </p>
<h2>Author</h2>
<p>This manual page was written by Andreas Jellinghaus &lt;aj [at] dungeon.inka.de&gt;, for Debian GNU/Linux and isdn4linux.<br />
 Now maintained by Paul Slootman &lt;paul [at] debian.org&gt;.</p>
