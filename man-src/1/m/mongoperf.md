---
title: "mongoperf(1)"
name: "mongoperf"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mongoperf/"
description: "mongoperf – MongoDB Performance Utility"
---

<h2>NAME</h2>
<p> mongoperf &#8211; MongoDB Performance Utility</p>
<h2>SYNOPSIS</h2>
<p> <code>mongoperf</code> is a utility to check disk I/O performance independently of MongoDB. </p>
<p> It times tests of random disk I/O and presents the results. You can use <code>mongoperf</code> for any case apart from MongoDB. The <code>mmf</code> <code>true</code> mode is completely generic. In that mode it is somewhat analogous to tools such as <i>bonnie++</i> (albeit mongoperf is simpler). </p>
<p> Specify options to <code>mongoperf</code> using a JavaScript document. </p>
<p> <code>SEE ALSO:</code></p>
<dl>
<dt>&bull;</p>
<dd> <i>bonnie</i></p>
<dt>&bull;</p>
<dd> <i>bonnie++</i></p>
<dt>&bull;</p>
<dd> <i>Output from an example run</i></p>
<dt>&bull;</p>
<dd> <i>Checking Disk Performance with the mongoperf Utility</i></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>mongoperf</code></p>
<dd>
<dt><code>mongoperf</code></p>
<dd>
<dt><code>&#8211;help, -h</code></p>
<dd> Returns information on <code>mongoperf</code> options and usage.</p>
<dt><code>&lt;jsonconfig&gt;</code></p>
<dd> <code>mongoperf</code> accepts configuration options in the form of a file that holds a <i>JSON</i> document. You must stream the content of this file into <code>mongoperf</code>, as in the following operation: </p>
<pre>
mongoperf &lt; config
</pre>
<p> In this example <code>config</code> is the name of a file that holds a JSON document that resembles the following example: </p>
<pre>
{
  nThreads:&lt;n&gt;,
  fileSizeMB:&lt;n&gt;,
  sleepMicros:&lt;n&gt;,
  mmf:&lt;bool&gt;,
  r:&lt;bool&gt;,
  w:&lt;bool&gt;,
  recSizeKB:&lt;n&gt;,
  syncDelay:&lt;n&gt;
}
</pre>
<p> See the <i>Configuration Fields</i> section for documentation of each of these fields.</dl>
<h2>CONFIGURATION FIELDS</h2>
<dl>
<dt><code>mongoperf.nThreads</code></p>
<dd> <i>Type:</i> Integer. </p>
<p> <i>Default:</i> 1 </p>
<p> Defines the number of threads <code>mongoperf</code> will use in the test. To saturate your system&#8217;s storage system you will need multiple threads. Consider setting <code>nThreads</code> to <code>16</code>.</p>
<dt><code>mongoperf.fileSizeMB</code></p>
<dd> <i>Type:</i> Integer. </p>
<p> <i>Default:</i> 1 megabyte (i.e. 1024<font SIZE="-2">2</font> bytes) </p>
<p> Test file size.</p>
<dt><code>mongoperf.sleepMicros</code></p>
<dd> <i>Type:</i> Integer. </p>
<p> <i>Default:</i> 0 </p>
<p> <code>mongoperf</code> will pause for the number of specified <code>sleepMicros</code> divided by the <code>nThreads</code> between each operation.</p>
<dt><code>mongoperf.mmf</code></p>
<dd> <i>Type:</i> Boolean. </p>
<p> <i>Default:</i> <code>false</code> </p>
<p> Set <code>mmf</code> to <code>true</code> to use memory mapped files for the tests. </p>
<p> Generally:</p>
<dt>&bull;</p>
<dd> when <code>mmf</code> is <code>false</code>, <code>mongoperf</code> tests direct, physical, I/O, without caching. Use a large file size to test heavy random I/O load and to avoid I/O coalescing.</p>
<dt>&bull;</p>
<dd> when <code>mmf</code> is <code>true</code>, <code>mongoperf</code> runs tests of the caching system, and can use normal file system cache. Use <code>mmf</code> in this mode to test file system cache behavior with memory mapped files.</p>
<dt><code>mongoperf.r</code></p>
<dd> <i>Type:</i> Boolean. </p>
<p> <i>Default:</i> <code>false</code> </p>
<p> Set <code>r</code> to <code>true</code> to perform reads as part of the tests. </p>
<p> Either <code>r</code> or <code>w</code> must be <code>true</code>.</p>
<dt><code>mongoperf.w</code></p>
<dd> <i>Type:</i> Boolean. </p>
<p> <i>Default:</i> <code>false</code> </p>
<p> Set <code>w</code> to <code>true</code> to perform writes as part of the tests. </p>
<p> Either <code>r</code> or <code>w</code> must be <code>true</code>.</p>
<dt><code>mongoperf.recSizeKB</code></p>
<dd> New in version 2.4. </p>
<p> <i>Type:</i> Integer. </p>
<p> <i>Default:</i> 4 kb </p>
<p> The size of each write operation.</p>
<dt><code>mongoperf.syncDelay</code></p>
<dd> <i>Type:</i> Integer. </p>
<p> <i>Default:</i> 0 </p>
<p> Seconds between disk flushes. <code>mongoperf.syncDelay</code> is similar to <i>&#8211;syncdelay</i> for <code>mongod</code>. </p>
<p> The <code>syncDelay</code> controls how frequently <code>mongoperf</code> performs an asynchronous disk flush of the memory mapped file used for testing. By default, <code>mongod</code> performs this operation every 60 seconds. Use <code>syncDelay</code> to test basic system performance of this type of operation. </p>
<p> Only use <code>syncDelay</code> in conjunction with <code>mmf</code> set to <code>true</code>. </p>
<p> The default value of <code>0</code> disables this.</dl>
<h2>USE</h2>
<pre>
mongoperf &lt; jsonconfigfile
</pre>
<p> Replace <code>jsonconfigfile</code> with the path to the <code>mongoperf</code> configuration. You may also invoke <code>mongoperf</code> in the following form: </p>
<pre>
echo &quot;{nThreads:16,fileSizeMB:1000,r:true}&quot; | ./mongoperf
</pre>
<p> In this operation:</p>
<dl>
<dt>&bull;</p>
<dd> <code>mongoperf</code> tests direct physical random read io&#8217;s, using 16 concurrent reader threads.</p>
<dt>&bull;</p>
<dd> <code>mongoperf</code> uses a 1 gigabyte test file. </p>
<p> Consider using <code>iostat</code>, as invoked in the following example to monitor I/O performance during the test. </p>
<pre>
iostat -xm 2
</pre>
</dl>
<h2>AUTHOR</h2>
<p> MongoDB Documentation Project</p>
<h2>COPYRIGHT</h2>
<p> 2011-2014, MongoDB, Inc. </p>
<h2>Index</h2>
