---
title: "convertxls2csv(1)"
name: "convertxls2csv"
section: "1"
letter: "c"
url: "/docs/linux/man/1-convertxls2csv/"
---

<h2 class="name">NAME</h2>
 

 xls2csv - A script that recodes a spreadsheet's charset and saves as CSV. 

<h2>DESCRIPTION</h2>

 This script will recode a spreadsheet into a different character set and output the recoded data as a csv file. 

 The script came about after many headaches from dealing with Excel spreadsheets from clients that were being received in various character sets.

<h2>OPTIONS</h2>

 <pre>
        -x     : filename of the source spreadsheet
        -b     : the character set the source spreadsheet is in (before)
        -c     : the filename to save the generated csv file as
        -a     : the character set the csv file should be converted to (after)
        -q     : quiet mode
        -s     : print a list of supported character sets
        -h     : print help message
        -v     : get version information
        -W     : list worksheets in the spreadsheet specified by -x
        -w     : specify the worksheet name to convert (defaults to the first worksheet)
        -n     : specify the worksheet number to convert (you cannot use this option with -w)
        -f     : force the worsheet to be fully parsed. This disables the feature that skips rows when the first cell is blank
</pre>

<h2>EXAMPLE USAGE</h2>

 The following example will convert a spreadsheet that is in the <font SIZE="-1">WINDOWS-1252</font> character set (WinLatin1) and save it as a csv file in the <font SIZE="-1">UTF-8</font> character set. 

 <pre>
        xls2csv -x &quot;1252spreadsheet.xls&quot; -b WINDOWS-1252 -c &quot;ut8csvfile.csv&quot; -a UTF-8
</pre> 

 This example with convert the worksheet named ``Users'' in the given spreadsheet. 

 <pre>
        xls2csv -x &quot;multi_worksheet_spreadsheet.xls&quot; -w &quot;Users&quot; -c &quot;users.csv&quot;
</pre>

<h2>NOTES</h2>

 The spreadsheet's charset (-b) will default to <font SIZE="-1">UTF-8</font> if not set. 

 If the csv's charset (-a) is not set, the <font SIZE="-1">CSV</font> file will be created using the same charset as the spreadsheet.

<h2>REQUIRED MODULES</h2>

 This script requires the following modules: 

 <pre>
        Locale::Recode
        Unicode::Map
        Spreadsheet::ParseExcel
        Spreadsheet::ParseExcel::FmtUnicode (should be included with Spreadsheet::ParseExcel)
        Text::CSV_XS
</pre>

<h2>CAVEATS</h2>

 It probably will not work work with spreadsheets that use formulas. 

 A line in the spreadsheet is assumed to be blank if there is nothing in the first column. 

 Some users have reported problems trying to convert a spreadsheet while it was opened in a different application. You should probably make sure that no other programs are working with the spreadsheet while you are converting it.

<h2>AUTHOR</h2>

 Ken Prows (perl [at] xev.net)

<h2>COPYRIGHT</h2>

 Copyright (C) 2005-2012 Ken Prows. All rights reserved. 

 This script is free software; you can redistribute it and/or modify it under the same terms as Perl itself. 

<h2>Index</h2>


