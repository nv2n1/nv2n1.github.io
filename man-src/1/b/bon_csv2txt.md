---
title: "bon_csv2txt(1)"
name: "bon_csv2txt"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bon_csv2txt/"
description: "bon_csv2html program to convert CSV format Bonnie++ data to a HTML form using tables suitable for display on a web page. NB Lynx can’t display this properly, and due to the size it probably require..."
---

<h2>NAME</h2>
<p> <code>bon_csv2html</code> program to convert CSV format Bonnie++ data to a HTML form using tables suitable for display on a web page. NB Lynx can&#8217;t display this properly, and due to the size it probably requires 1024&#215;768 monitor to display properly. </p>
<p> <code>bon_csv2txt</code> program to convert CSV format Bonnie++ data to plain-text format suitable for pasting into an email or reading on a Braille display. </p>
<h2>DESCRIPTION</h2>
<p> They take CSV format (comma-delimited spreadsheet files AKA Comma Seperated Values in MS land) data on standard input and produce HTML or plain text on standard output respectively. </p>
<h2>FORMAT</h2>
<p> This is a list of the fields used in the CSV files format version 2. Format version 1 was the type used in Bonnie++ &lt; 1.90. Before each field I list the field number as well as the name given in the heading</p>
<dl>
<dt><code>0 format_version</code></p>
<dd> Version of the output format in use (1.97)</p>
<dt><code>1 bonnie_version</code></p>
<dd> (1.97)</p>
<dt><code>2 name</code></p>
<dd> Machine Name</p>
<dt><code>3 concurrency</code></p>
<dd> The number of copies of each operation to be run at the same time</p>
<dt><code>4 seed</code></p>
<dd> Random number seed</p>
<dt><code>5 file_size</code></p>
<dd> Size in megs for the IO tests</p>
<dt><code>6 chunk_size</code></p>
<dd> Size of chunks in bytes</p>
<dt><code>7 putc,putc_cpu</code></p>
<dd> Results for writing a character at a time K/s,%CPU</p>
<dt><code>9 put_block,put_block_cpu</code></p>
<dd> Results for writing a block at a time K/s,%CPU</p>
<dt><code>11 rewrite,rewrite_cpu</code></p>
<dd> Results for reading and re-writing a block at a time K/s,%CPU</p>
<dt><code>13 getc,getc_cpu</code></p>
<dd> Results for reading a character at a time K/s,%CPU</p>
<dt><code>15 get_block,get_block_cpu</code></p>
<dd> Results for reading a block at a time K/s,%CPU</p>
<dt><code>17 seeks,seeks_cpu</code></p>
<dd> Results for the seek test seeks/s,%CPU</p>
<dt><code>19 num_files</code></p>
<dd> Number of files for file-creation tests (units of 1024 files)</p>
<dt><code>20 max_size</code></p>
<dd> The maximum size of files for file-creation tests. Or the type of files for links.</p>
<dt><code>21 min_size</code></p>
<dd> The minimum size of files for file-creation tests.</p>
<dt><code>22 num_dirs</code></p>
<dd> The number of directories for creation of files in multiple directories.</p>
<dt><code>23 file_chunk_size</code></p>
<dd> The size of blocks for writing multiple files.</p>
<dt><code>24 seq_create,seq_create_cpu</code></p>
<dd> Rate of creating files sequentially files/s,%CPU</p>
<dt><code>26 seq_stat,seq_stat_cpu</code></p>
<dd> Rate of reading/stating files sequentially files/s,%CPU</p>
<dt><code>28 seq_del,seq_del_cpu</code></p>
<dd> Rate of deleting files sequentially files/s,%CPU</p>
<dt><code>30 ran_create,ran_create_cpu</code></p>
<dd> Rate of creating files in random order files/s,%CPU</p>
<dt><code>32 ran_stat,ran_stat_cpu</code></p>
<dd> Rate of deleting files in random order files/s,%CPU</p>
<dt><code>34 ran_del,ran_del_cpu</code></p>
<dd> Rate of deleting files in random order files/s,%CPU</p>
<dt><code>36 putc_latency,put_block_latency,rewrite_latency</code></p>
<dd> Latency (maximum amount of time for a single operation) for putc, put_block, and reqrite</p>
<dt><code>39 getc_latency,get_block_latency,seeks_latency</code></p>
<dd> Latency for getc, get_block, and seeks</p>
<dt><code>42 seq_create_latency,seq_stat_latency,seq_del_latency</code></p>
<dd> Latency for seq_create, seq_stat, and seq_del</p>
<dt><code>45 ran_create_latency,ran_stat_latency,ran_del_latency</code></p>
<dd> Latency for ran_create, ran_stat, and ran_del</dl>
<p> A string that starts with &#8216;#&#8217; is a comment. </p>
<h2>AUTHOR</h2>
<p> These programs were written by Russell Coker &lt;russell [at] coker.com.au&gt;. May be freely used and distributed without restriction. </p>
<h2>Index</h2>
