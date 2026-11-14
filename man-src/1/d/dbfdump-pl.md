---
title: "dbfdump-pl(1)"
name: "dbfdump-pl"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbfdump-pl/"
---

dbfdump.pl - Dump the record of the dbf file 

<h2>Format</h2><pre> dbfdump.pl [options] files</pre>where options are 

 <pre> --rs output record separator (default newline)
 --fs output field separator (default colon)
 --fields comma separated list of fields to print (default all)
 --undef string to print for NULL values (default empty)
 --memofile specifies unstandard name of attached memo file
 --memosep separator for dBase III dbt's (default \x1a\x1a)
 --nomemo do not try to read the memo (dbt/fpt) file
 --info print info about the file and fields
 with additional --SQL parameter, outputs the SQL create table
 --version print version of the XBase library
 --table output in nice table format (only available when
 Data::ShowTable is installed, overrides rs and fs)</pre><h2>Synopsis</h2><pre> dbfdump.pl -fields id,msg table.dbf
 dbfdump.pl -fs=' : ' table
 dbfdump.pl --nomemo file.dbf
 ssh user [at] host 'cat file.dbf.gz' | gunzip - | dbfdump.pl -</pre><h2>Description</h2>Dbfdump prints to standard output the content of dbf files listed. By default, it prints all fields, separated by colons, one record on a line. The output record and column separators can be changed by switches on the command line. You can also ask only for some fields to be printed. 

 The content of associated memo files (dbf, fpt) is printed for memo fields, unless you use the <tt>&quot;--nomemo&quot;</tt> option. 

 You can specify reading the standard input by putting dash (-) instead of file name.
<h2>Available From</h2><a rel="nofollow" HREF="http://www.adelton.com/perl/DBD-XBase/">http://www.adelton.com/perl/DBD-XBase/</a>
<h2>Author</h2>(c) 1998--2011 Jan Pazdziora.
<h2>See Also</h2><i><a HREF="/docs/linux/man/1-perl/">perl</a></i>(1); <i><a HREF="/docs/linux/man/3-xbase/">XBase</a></i>(3)
