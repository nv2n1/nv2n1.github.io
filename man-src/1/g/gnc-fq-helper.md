---
title: "gnc-fq-helper(1)"
name: "gnc-fq-helper"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gnc-fq-helper/"
---

<h2 class="name">NAME</h2>
 

 gnc-fq-helper - allows gnucash to communicate with Finance::Quote 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>over pipes from guile. The requests and responses 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>are scheme forms. 

<h2>SYNOPSIS</h2>

 gnc-fq-helper

<h2>DESCRIPTION</h2>

 Input: (on standard input - one entry per line and one line per entry, and double quotes must only be delimiters, not string content --- remember, we don't have a real scheme parser on the perl side :&gt;). 

 (&lt;method-name&gt; symbol symbol symbol ...) 

 where &lt;method-name&gt; indicates the desired Finance::Quote method. The currently recognized subset is yahoo, yahoo_europe, fidelity_direct, troweprice_direct, vanguard, asx, tiaacref, and currency. 

 For currency quotes, the symbols alternate between the 'from' and 'to' currencies. 

 For example: 

 (yahoo ``<font SIZE="-1">IBM</font>'' ``<font SIZE="-1">LNUX</font>'') (fidelity_direct ``<font SIZE="-1">FBIOX</font>'' ``<font SIZE="-1">FSELX</font>'') (currency ``<font SIZE="-1">USD</font>'' ``<font SIZE="-1">AUD</font>'') 

 Output (on standard output, one output form per input line): 

 Schemified version of gnc-fq's output, basically an alist of alists, as in the example below. Right now, only the fields that this script knows about (and knows how to convert to scheme) are returned, so the conversion function will have to be updated whenever Finance::Quote changes. Currently you'll get symbol, gnc:time-no-zone, and currency, and either last, nav, or price. Fields with gnc: prefixes are non-Finance::Quote fields. gnc:time-no-zone is returned as a string of the form ``YYYY-MM-DD <font SIZE="-1">HH:MM:SS</font>'', basically the unmolested (and underspecified) output of the quote source. It's up to you to know what it's proper timezone really is. i.e. if you know the time was in America/Chicago, you'll need to convert it to that. 

 For example: 

 <pre>
 $ echo '(yahoo &quot;CSCO&quot; &quot;JDSU&quot; &quot;^IXIC&quot;)' | ./gnc-fq-helper
((&quot;CSCO&quot; (symbol . &quot;CSCO&quot;)
         (gnc:time-no-zone . &quot;2001-03-13 19:27:00&quot;)
         (last . 20.375)
         (currency . &quot;USD&quot;))
 (&quot;JDSU&quot; (symbol . &quot;JDSU&quot;)
         (gnc:time-no-zone . &quot;2001-03-13 19:27:00&quot;)
         (last . 23.5625)
         (currency . &quot;USD&quot;))
(&quot;^IXIC&quot; (symbol . ^IXIC)
         (gnc:time-no-zone . 2002-12-04 17:16:00)
         (last . 1430.35)
         (currency . failed-conversion)))
</pre> 

 On error, the overall result may be #f, or on individual errors, the list sub-item for a given symbol may be #f, like this: 

 <pre>
 $ echo '(yahoo &quot;CSCO&quot; &quot;JDSU&quot;)' | ./gnc-fq-helper
(#f
 (&quot;JDSU&quot; (symbol . &quot;JDSU&quot;)
         (gnc:time-no-zone . &quot;2001-03-13 19:27:00&quot;)
         (last . 23.5625)
         (currency . &quot;USD&quot;)))
</pre> 

 further, errors may be stored with each quote as indicated in Finance::Quote, and whenever the conversion to scheme data fails, the field will have the value 'failed-conversion, and accordingly this symbol will never be a legitimate conversion. 

 Exit status 

 0 - success non-zero - failure 

<h2>Index</h2>


